# Observed Obsidian Note Format

Observed in:

`E:\DATA\github-kb\Personal-Knowledge-Base\笔记同步助手\2026-07-09`

## Plugin Settings

The installed Obsidian plugin is:

`Personal-Knowledge-Base\.obsidian\plugins\bijitongbu`

Important settings in `data.json`:

- `endpoint`: `https://obsidian.notebooksyncer.com/api/graphql`
- `template`: `{{{content}}}`
- `folder`: equivalent to `笔记同步助手/{{{date}}}`
- `filename`: `{{{title}}}`
- `mergeMode`: `messages`
- `imageMode`: `local`
- image folder: equivalent to `笔记同步助手/images`

Do not expose the `apiKey` from `data.json`.

## Independent Article Files

File names are typically:

`<author>- <title>.md`

Frontmatter contains:

```yaml
---
author: <author>
source: <source>
url: <original url>
saved: YYYY-MM-DD HH:mm:ss
tags:
  - 笔记同步助手
id: <uuid-like id>
---
```

The body starts with a source link, then the captured article/social-post text, then optional image embeds such as:

```markdown
![[笔记同步助手/images/<hash>_MD5.jpg]]
```

Existing notes often end with a feedback link. The Hermes skill can instead add a short local sync footer unless the remote feedback URL is available.

## Daily Merged Message File

Unsupported WeChat cards/video cards are merged into:

`同步助手_YYYY-MM-DD.md`

The file has frontmatter like:

```yaml
---
syncedIds: <ids>
---
```

Each item is appended with a section resembling:

```markdown
---
#### <heading>
## YYYY-MM-DD HH:mm:ss
<content>
```

Use this mode only for card summaries, not full article content.
