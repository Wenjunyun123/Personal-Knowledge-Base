---
name: hermes-obsidian-sync
description: Sync article links sent to Hermes/WeChat into the user's Obsidian Personal-Knowledge-Base vault using the existing 笔记同步助手 note format. Use when the user says they sent a link to Hermes or WeChat and wants it saved/synced to Obsidian, or when Codex must create/update notes under Personal-Knowledge-Base/笔记同步助手 from a URL, title, article body, social post, or WeChat card.
---

# Hermes Obsidian Sync

## Overview

Use this skill when Hermes receives a WeChat/social/article link and needs to make the result appear in the user's Obsidian vault in the same style as the installed `bijitongbu` plugin.

Default vault:

`E:\DATA\github-kb\Personal-Knowledge-Base`

Primary destination:

`Personal-Knowledge-Base\笔记同步助手\YYYY-MM-DD\...`

## Source Of Truth

Before writing a note, inspect the real vault state:

- Existing synced notes under `Personal-Knowledge-Base\笔记同步助手\<date>\`.
- Plugin settings at `Personal-Knowledge-Base\.obsidian\plugins\bijitongbu\data.json`.
- Image map and queue files under `Personal-Knowledge-Base\.obsidian\plugins\bijitongbu\`.

Do not print or store the plugin `apiKey`. PowerShell may render Chinese text as mojibake in this environment; trust real file paths and UTF-8 reads over garbled console display.

For observed formatting details, read `references/observed-format.md`.

## Workflow

1. Extract the URL from the Hermes/WeChat message.
2. Determine whether Hermes already supplied title, author, source, body text, and images.
3. If article body is missing and browsing is allowed, fetch the page and extract the main text. If extraction fails, create a link-only stub with `needs_content: true`.
4. Use `scripts/sync_article_to_vault.py` to create or update the note.
5. Verify that the target `.md` file exists and briefly report the path.

## Rendering Rules

Use independent article files when there is article/post content:

`笔记同步助手/YYYY-MM-DD/<author>- <title>.md`

Use the daily merged message file when the incoming item is only a WeChat card, video-card summary, or unsupported card:

`笔记同步助手/YYYY-MM-DD/同步助手_YYYY-MM-DD.md`

Frontmatter for article files should match the existing style:

```yaml
---
author: <author>
source: <source>
url: <url>
saved: YYYY-MM-DD HH:mm:ss
tags:
  - 笔记同步助手
id: <stable id>
---
```

Then include a source link, the article body, optional image links, and a short sync footer.

## Script Usage

Run from any working directory:

```powershell
python C:\Users\Y.Daria\.codex\skills\hermes-obsidian-sync\scripts\sync_article_to_vault.py `
  --url "https://mp.weixin.qq.com/s/example" `
  --title "文章标题" `
  --author "作者" `
  --source "WeChat" `
  --content-file "C:\path\article.txt"
```

For link-only messages:

```powershell
python C:\Users\Y.Daria\.codex\skills\hermes-obsidian-sync\scripts\sync_article_to_vault.py `
  --url "https://mp.weixin.qq.com/s/example" `
  --title "待解析文章" `
  --source "WeChat" `
  --content "Hermes received the link, but article body extraction has not completed." `
  --needs-content
```

For merged WeChat card messages:

```powershell
python C:\Users\Y.Daria\.codex\skills\hermes-obsidian-sync\scripts\sync_article_to_vault.py `
  --mode message `
  --url "https://weixin.qq.com/sph/example" `
  --title "视频号卡片标题" `
  --source "WeChat" `
  --content "卡片摘要"
```

## Safety

- Do not overwrite unrelated notes.
- If the target file exists with the same `id`, update it.
- If the target path exists with a different `id`, create a numbered filename.
- Keep generated images under `笔记同步助手/images` when local image paths are supplied.
- Do not call external APIs with real side effects unless the user explicitly asks.
