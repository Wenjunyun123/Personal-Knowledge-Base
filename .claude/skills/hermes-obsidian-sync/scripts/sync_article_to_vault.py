#!/usr/bin/env python
"""Write a Hermes/WeChat article payload into the user's Obsidian vault."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


DEFAULT_VAULT = Path(r"E:\DATA\github-kb\Personal-Knowledge-Base")
NOTE_ROOT_NAME = "笔记同步助手"
TAG_NAME = "笔记同步助手"


@dataclass
class Payload:
    url: str
    title: str
    author: str
    source: str
    content: str
    saved: datetime
    mode: str
    needs_content: bool
    images: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync a Hermes article/link payload into the Obsidian notehelper folder."
    )
    parser.add_argument("--url", required=True)
    parser.add_argument("--title", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--source", default="")
    parser.add_argument("--content", default="")
    parser.add_argument("--content-file", default="")
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--date", default="")
    parser.add_argument("--mode", choices=["auto", "article", "message"], default="auto")
    parser.add_argument("--needs-content", action="store_true")
    parser.add_argument("--image", action="append", default=[])
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_plugin_settings(vault: Path) -> dict:
    data_path = vault / ".obsidian" / "plugins" / "bijitongbu" / "data.json"
    if not data_path.exists():
        return {}
    try:
        data = json.loads(data_path.read_text(encoding="utf-8-sig"))
        data.pop("apiKey", None)
        return data
    except Exception:
        return {}


def read_content(args: argparse.Namespace) -> str:
    if args.content_file:
        return Path(args.content_file).read_text(encoding="utf-8")
    return args.content


def source_from_url(url: str) -> str:
    host = re.sub(r"^https?://", "", url).split("/")[0].lower()
    if "weixin.qq.com" in host or "mp.weixin.qq.com" in host:
        return "WeChat"
    if "x.com" in host or "twitter.com" in host:
        return "X"
    if "zhihu.com" in host:
        return "Zhihu"
    if "xiaohongshu.com" in host:
        return "Xiaohongshu"
    return host or "Web"


def title_from_url(url: str) -> str:
    host = re.sub(r"^https?://", "", url).split("/")[0]
    return f"{host or 'article'} - Hermes link"


def stable_id(url: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, url.strip()))


def sanitize_filename(value: str) -> str:
    value = re.sub(r'[\\/:*?"<>|]+', "-", value).strip()
    value = re.sub(r"\s+", " ", value)
    value = value.rstrip(". ")
    return value[:120] or "untitled"


def ensure_unique_path(path: Path, item_id: str) -> Path:
    if not path.exists():
        return path
    existing = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^id:\s*(.+?)\s*$", existing, flags=re.MULTILINE)
    if match and match.group(1).strip() == item_id:
        return path
    stem = path.stem
    suffix = path.suffix
    for index in range(2, 1000):
        candidate = path.with_name(f"{stem} {index}{suffix}")
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"could not find a free filename for {path}")


def yaml_escape(value: str) -> str:
    if not value:
        return ""
    if re.search(r"[:#\n\r]|^\s|\s$", value):
        return json.dumps(value, ensure_ascii=False)
    return value


def copy_or_render_images(images: Iterable[str], vault: Path, note_root: Path) -> str:
    rendered: list[str] = []
    image_root = note_root / "images"
    for image in images:
        if re.match(r"^https?://", image):
            rendered.append(f"![]({image})")
            continue
        src = Path(image)
        if not src.exists():
            rendered.append(f"<!-- missing image: {image} -->")
            continue
        digest = hashlib.md5(src.read_bytes()).hexdigest()
        ext = src.suffix.lower() or ".jpg"
        image_root.mkdir(parents=True, exist_ok=True)
        dest = image_root / f"{digest}_MD5{ext}"
        if not dest.exists():
            shutil.copy2(src, dest)
        rel = dest.relative_to(vault).as_posix()
        rendered.append(f"![[{rel}]]")
    return "\n\n".join(rendered)


def build_article_markdown(payload: Payload, item_id: str, image_markdown: str) -> str:
    saved = payload.saved.strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "---",
        f"author: {yaml_escape(payload.author)}",
        f"source: {yaml_escape(payload.source)}",
        f"url: {yaml_escape(payload.url)}",
        f"saved: {saved}",
        "tags:",
        f"  - {TAG_NAME}",
    ]
    if payload.needs_content:
        lines.append("needs_content: true")
    lines.extend([f"id: {item_id}", "---", ""])
    lines.append(f"[在 {payload.source} 查看原文]({payload.url})")
    lines.append("")
    lines.append(payload.content.strip() or "Hermes received this link, but article body extraction has not completed.")
    if image_markdown:
        lines.extend(["", image_markdown])
    lines.extend(["", "---", "", "由 Hermes Obsidian Sync 写入。"])
    return "\n".join(lines).rstrip() + "\n"


def read_frontmatter_end(text: str) -> int:
    if not text.startswith("---\n"):
        return -1
    return text.find("\n---\n", 4)


def append_message_file(path: Path, payload: Payload, item_id: str) -> None:
    saved = payload.saved.strftime("%Y-%m-%d %H:%M:%S")
    section = "\n".join(
        [
            "",
            "---",
            f"#### {payload.title}",
            f"## {saved}",
            payload.content.strip() or payload.url,
            "",
        ]
    )
    if not path.exists():
        text = f"---\nsyncedIds: {item_id}\n---\n{section}"
        path.write_text(text, encoding="utf-8")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    if item_id in text:
        return
    end = read_frontmatter_end(text)
    if end >= 0:
        front = text[:end]
        rest = text[end:]
        if "syncedIds:" in front:
            front = re.sub(r"syncedIds:\s*(.*)", lambda m: f"syncedIds: {m.group(1).strip()} {item_id}".rstrip(), front, count=1)
        else:
            front += f"\nsyncedIds: {item_id}"
        text = front + rest
    path.write_text(text.rstrip() + "\n" + section, encoding="utf-8")


def resolve_saved(date_arg: str) -> datetime:
    if not date_arg:
        return datetime.now()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_arg, fmt)
        except ValueError:
            pass
    raise SystemExit(f"unsupported --date format: {date_arg}")


def main() -> int:
    args = parse_args()
    vault = Path(args.vault)
    if not vault.exists():
        raise SystemExit(f"vault not found: {vault}")
    note_root = vault / NOTE_ROOT_NAME
    note_root.mkdir(parents=True, exist_ok=True)
    settings = load_plugin_settings(vault)
    content = read_content(args)
    saved = resolve_saved(args.date)
    payload = Payload(
        url=args.url.strip(),
        title=args.title.strip() or title_from_url(args.url),
        author=args.author.strip() or "Hermes",
        source=args.source.strip() or source_from_url(args.url),
        content=content,
        saved=saved,
        mode=args.mode,
        needs_content=args.needs_content or not bool(content.strip()),
        images=args.image,
    )
    mode = payload.mode
    if mode == "auto":
        mode = "message" if payload.title.startswith("同步助手_") else "article"
    date_folder = note_root / saved.strftime("%Y-%m-%d")
    date_folder.mkdir(parents=True, exist_ok=True)
    item_id = stable_id(payload.url)
    if mode == "message":
        target = date_folder / f"同步助手_{saved.strftime('%Y-%m-%d')}.md"
        if not args.dry_run:
            append_message_file(target, payload, item_id)
    else:
        image_markdown = copy_or_render_images(payload.images, vault, note_root)
        filename = sanitize_filename(f"{payload.author}- {payload.title}")
        target = ensure_unique_path(date_folder / f"{filename}.md", item_id)
        markdown = build_article_markdown(payload, item_id, image_markdown)
        if not args.dry_run:
            target.write_text(markdown, encoding="utf-8")
    result = {
        "target": str(target),
        "mode": mode,
        "id": item_id,
        "endpoint": settings.get("endpoint", ""),
        "wrote": not args.dry_run,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
