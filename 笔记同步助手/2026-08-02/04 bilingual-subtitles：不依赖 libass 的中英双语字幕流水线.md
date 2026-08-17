---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/bilingual-subtitles
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: f4527e91-282d-4e65-90b4-b87628bf1dbf
---

项目名称：bilingual-subtitles

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：3

## 一句话理解

bilingual-subtitles 使用 Pillow 把中英双语字幕渲染成透明 PNG 图层，再通过 ffmpeg overlay 烧录进视频，从而绕开 libass 在字体、描边和双语排版上的限制。

## 它具体解决什么问题

中英双语字幕不只是把两行文字放到画面底部。中文不能随意在标点前后断行，英文要按单词换行，两种语言还经常需要不同字体、字号、描边和行距。

传统 ffmpeg 字幕方案依赖 libass，在不同系统上的字体解析和样式兼容容易出现差异。这个项目把排版控制交给 Pillow，再让 ffmpeg 只负责叠加图层。

## 实际使用时会看到什么

输入中英双语字幕后，脚本会为每个 cue 计算排版，生成带半透明背景的双层字幕。中文位于上方，英文位于下方，并根据画面分辨率自动缩放。

项目支持预览、正式烧录、字幕统计和 Markdown 说明等命令。适合在烧录整段视频前先检查断行、位置和字号。

## 核心实现

- 针对 CJK 文本进行字符级断词。
- 避免标点出现在不合适的行首位置。
- 根据最大宽度自动换行，必要时拆分 cue。
- `Style` 会以 1080p 为基准按视频尺寸缩放。
- Pillow 生成透明 RGBA 图层，ffmpeg 使用 overlay 合成。

## 适合谁

- 需要稳定生成中英双语硬字幕的视频创作者。
- 对字体、描边、背景框和断行有明确要求的人。
- 在 Windows、macOS 或服务器环境中遇到 libass 字体差异的人。

## 验证情况与边界

本次实际调用了仓库的 `render()` 函数，使用 Windows 中文和英文字体生成了双语字幕层，确认渲染器可以输出有效画面。验证时使用的是明确标注的合成背景，并未把它冒充真实视频。由于环境缺少 ffprobe，本次没有完成整段视频的 ffmpeg 烧录验证。

## 项目地址

GitHub：https://github.com/zarazhangrui/bilingual-subtitles

