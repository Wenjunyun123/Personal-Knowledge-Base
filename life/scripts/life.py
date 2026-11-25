#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生活数据录入与复盘。零依赖，Python 3.9+。

    python life.py ingest                 # 手机 inbox -> data/*.jsonl
    python life.py add 体重 72.4 kg -n 空腹
    python life.py today                  # 今天记了什么
    python life.py week                   # 生成周报 + 打印摘要
    python life.py check                  # 哪天断记了
"""
import argparse
import hashlib
import io
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
INBOX, DATA, REPORTS, IMPORTS = ROOT / "inbox", ROOT / "data", ROOT / "reports", ROOT / "import"

LINE_RE = re.compile(r"^\s*[-*]\s*(\d{1,2}:\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*(.*?)\s*$")
NUM_RE = re.compile(r"-?\d+(?:\.\d+)?")


def ensure_dirs():
    for d in (INBOX, DATA, REPORTS, IMPORTS):
        d.mkdir(parents=True, exist_ok=True)


def rec_id(r):
    return hashlib.sha1(f"{r['ts']}|{r['domain']}|{r['value']}|{r.get('note','')}".encode()).hexdigest()[:16]


def load_records():
    recs = []
    for f in sorted(DATA.glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            r["_id"] = rec_id(r)
            recs.append(r)
    return recs


def append_records(recs):
    by_month = defaultdict(list)
    for r in recs:
        by_month[r["ts"][:7]].append(r)
    for month, items in by_month.items():
        f = DATA / f"{month}.jsonl"
        with f.open("a", encoding="utf-8", newline="\n") as fh:
            for r in items:
                out = {k: v for k, v in r.items() if not k.startswith("_")}
                fh.write(json.dumps(out, ensure_ascii=False) + "\n")


def cmd_ingest(args):
    ensure_dirs()
    existing = {r["_id"] for r in load_records()}
    new, files, skipped = [], 0, 0
    for f in sorted(INBOX.glob("*.md")):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        if not m:
            continue
        day = m.group(1)
        files += 1
        for line in f.read_text(encoding="utf-8").splitlines():
            mm = LINE_RE.match(line)
            if not mm:
                continue
            hhmm, domain, value, note = mm.groups()
            r = {"ts": f"{day} {hhmm.zfill(5)}", "domain": domain.strip(),
                 "value": value.strip(), "note": note.strip(), "src": "phone"}
            rid = rec_id(r)
            if rid in existing:
                skipped += 1
                continue
            existing.add(rid)
            new.append(r)
    append_records(new)
    print(f"inbox 文件 {files} 个，新增 {len(new)} 条，已存在跳过 {skipped} 条")


def cmd_add(args):
    ensure_dirs()
    ts = args.at or datetime.now().strftime("%Y-%m-%d %H:%M")
    r = {"ts": ts, "domain": args.domain, "value": " ".join(args.value),
         "note": args.note or "", "src": "pc"}
    if rec_id(r) in {x["_id"] for x in load_records()}:
        print("已存在相同记录，跳过")
        return
    append_records([r])
    print(f"已记：{ts} | {r['domain']} | {r['value']}" + (f" | {r['note']}" if r["note"] else ""))


def cmd_today(args):
    today = datetime.now().strftime("%Y-%m-%d")
    recs = [r for r in load_records() if r["ts"].startswith(today)]
    if not recs:
        print(f"{today} 还没有记录。")
        return
    print(f"{today} 共 {len(recs)} 条：")
    for r in sorted(recs, key=lambda x: x["ts"]):
        note = f"  ({r['note']})" if r.get("note") else ""
        print(f"  {r['ts'][11:]}  {r['domain']}：{r['value']}{note}")


def num_of(value):
    m = NUM_RE.search(value.replace(",", ""))
    return float(m.group()) if m else None


def cmd_week(args):
    ensure_dirs()
    now = datetime.now()
    days = args.days
    start = (now - timedelta(days=days - 1)).strftime("%Y-%m-%d")
    recs = [r for r in load_records() if r["ts"][:10] >= start]
    iso = now.isocalendar()
    out = REPORTS / f"{iso.year}-W{iso.week:02d}.md"

    by_domain = defaultdict(list)
    for r in recs:
        by_domain[r["domain"]].append(r)

    lines = [f"# {iso.year} 第 {iso.week} 周 生活数据周报", "",
             f"> 统计区间：{start} ～ {now:%Y-%m-%d}　共 {len(recs)} 条记录", "",
             "## 汇总", "",
             "| 领域 | 记录数 | 均值 | 范围 |", "| --- | --- | --- | --- |"]
    for dom, items in sorted(by_domain.items(), key=lambda kv: -len(kv[1])):
        nums = [n for n in (num_of(i["value"]) for i in items) if n is not None]
        avg = f"{sum(nums)/len(nums):.2f}" if nums else "—"
        rng = f"{min(nums):g} ～ {max(nums):g}" if nums else "—"
        lines.append(f"| {dom} | {len(items)} | {avg} | {rng} |")

    lines += ["", "## 明细", ""]
    for dom, items in sorted(by_domain.items()):
        lines.append(f"### {dom}")
        lines.append("")
        for i in sorted(items, key=lambda x: x["ts"]):
            note = f" — {i['note']}" if i.get("note") else ""
            lines.append(f"- `{i['ts'][5:]}` {i['value']}{note}")
        lines.append("")

    lines += ["## 待 AI 填写", "",
              "- 本周 3 个发现：", "- 下周 1 个实验：", ""]
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")

    print(f"周报已生成：{out}")
    print(f"区间 {start} ～ {now:%Y-%m-%d}，{len(recs)} 条，覆盖领域：{'、'.join(sorted(by_domain)) or '无'}")


def cmd_check(args):
    recs = load_records()
    have = defaultdict(int)
    for r in recs:
        have[r["ts"][:10]] += 1
    now = datetime.now()
    print(f"共 {len(recs)} 条记录，最早 {recs[0]['ts'][:10] if recs else '—'}")
    missing = []
    for i in range(args.days):
        d = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        if have.get(d, 0) == 0:
            missing.append(d)
    print(f"最近 {args.days} 天里断记 {len(missing)} 天" + ("：" + "、".join(missing) if missing else "，全勤"))


def main():
    p = argparse.ArgumentParser(description="生活数据录入与复盘")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("ingest", help="手机 inbox 转 jsonl")
    s.set_defaults(func=cmd_ingest)

    s = sub.add_parser("add", help="记一条")
    s.add_argument("domain")
    s.add_argument("value", nargs="+")
    s.add_argument("-n", "--note", default="")
    s.add_argument("--at", help="自定义时间 'YYYY-MM-DD HH:MM'")
    s.set_defaults(func=cmd_add)

    s = sub.add_parser("today", help="看今天")
    s.set_defaults(func=cmd_today)

    s = sub.add_parser("week", help="生成周报")
    s.add_argument("--days", type=int, default=7)
    s.set_defaults(func=cmd_week)

    s = sub.add_parser("check", help="检查断记")
    s.add_argument("--days", type=int, default=14)
    s.set_defaults(func=cmd_check)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
