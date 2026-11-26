---
author: Leaf Yeah!
source: AI整理 - X (Twitter)
url: https://x.com/leaf_sanren/status/2125814519129854230?a=V28j-QvX0H8hlgMgcLk&s=19
saved: 2026-11-26 23:11:41
tags:
  - 笔记同步助手
id: 1e9a1ee7-eb61-4140-a5f8-fb3fbc43df0e
---

作者：Leaf Yeah!

作者：Leaf Yeah!

## 工作流概览

这套组合将 AI 生成视频素材、Renoise 音乐制作与 Editroom 自动剪辑连接起来：Antigravity 负责接管剪辑时间线，通过多光标并发处理原片与复刻片，最终生成左右并排的视频对比。

This workflow connects AI-generated video material, music production in Renoise, and automatic editing in Editroom: Antigravity takes control of the editing timeline and uses multiple cursors to process the original footage and the recreated version in parallel, ultimately producing a side-by-side comparison video.

## 核心工具

-   **Renoise：**用一句话快速复刻具有千万播放量的广告配乐或音乐风格。
    
    **Renoise:** Quickly recreate the music or soundtrack style of high-performing advertisements with a single sentence.
    
-   **Editroom：**一款约 23MB 的免费开源剪辑器，内置 MCP 服务，可与 Antigravity 连接并接收自动化剪辑指令。
    
    **Editroom:** A roughly 23MB free, open-source video editor with a built-in MCP server that can connect to Antigravity and receive automated editing instructions.
    
-   **Antigravity：**直接操作 Editroom 时间线，并发导入与整理素材，完成原片和复刻片的并排剪辑。
    
    **Antigravity:** Directly operates the Editroom timeline, concurrently importing and organizing the original footage and the recreated version to arrange them side by side.
    

## 接入 Editroom MCP

首先下载并打开免费开源的 Editroom，然后将提示词粘贴到 Antigravity 的对话框中。提示词要求连接本机 Editroom MCP 服务，并注册一个名为 `editroom` 的 stdio MCP 服务器。

First, download and open the free, open-source Editroom, then paste the prompt into Antigravity's chat window. The prompt instructs Antigravity to connect to the local Editroom MCP server and register a stdio MCP server named `editroom`.

可使用以下命令注册 MCP 服务：

Use the following command to register the MCP server:

![视频画面：展示 Antigravity、Renoise 与 Editroom 组合实现 AI 出片和自动剪辑的工作流。](https://relay-1.bijitongbu.site/p/bd525b1853b2e4af9af7c1e98fe28517.jpg)

视频画面：展示 Antigravity、Renoise 与 Editroom 组合实现 AI 出片和自动剪辑的工作流。

```
"/Applications/Editroom.app/Contents/MacOS/Editroom" --mcp
```

注册完成后，需要验证 `editroom` 已经启用，并且能够被 Antigravity 发现。

After registration, verify that `editroom` is enabled and can be discovered by Antigravity.

## 自动化剪辑指令

连接成功后，可以继续要求 Antigravity 自动导入原片和 Renoise 复刻成片，将两段视频排列为左右并排的对比形式，并添加顶部字卡。

Once connected, ask Antigravity to automatically import the original footage and the recreated video made with Renoise, arrange them as a side-by-side comparison, and add a title card at the top.

可以根据实际剪辑任务，对最后的任务描述进行微调。

Adjust the final task description according to the specific editing requirements.

## 工作流价值

这套流程的重点不是单独使用某个 AI 工具，而是把生成、复刻、导入、排列和字幕包装串成一条自动化工作链，从而减少手动操作时间，并快速制作适合短视频发布的对比内容。

The key idea is not to use a single AI tool in isolation, but to connect generation, recreation, importing, arrangement, and title-card packaging into an automated workflow. This reduces manual editing time and makes it easier to produce comparison content for short-form video platforms.

## 素材转写说明

本次语音转写内容为：

The provided transcript reads:

“This Valentine's Day, everybody's green skins.”

“This Valentine's Day, everybody's green skins.”

## 全文整理

这个情人节，大家都是绿皮肤的。

视频时长 20秒 · 计费 2 积分 · 积分余额 1119

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/b82c76dc-7c59-42f3-a4fd-a44cc4a85baf?u=https%3A%2F%2Fx.com%2Fleaf_sanren%2Fstatus%2F2125814519129854230%3Fa%3DV28j-QvX0H8hlgMgcLk%26s%3D19&s=vtoa)