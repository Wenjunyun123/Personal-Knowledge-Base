---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/vibe-coding-jam-presentation
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: c46e684b-9a51-4a60-9100-785b9325079e
---

项目名称：vibe-coding-jam-presentation

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：5

## 一句话理解

vibe-coding-jam-presentation 是一套真实使用过的 HTML 演讲作品《Code as a Medium for Storytelling》，通过 15 页演示、视频、项目截图和交互页面讲述 Vibe Coding 项目故事。

## 它具体解决什么问题

普通项目介绍容易变成“功能列表”。这个仓库试图回答的是：如何把代码项目组织成有节奏的现场故事，让观众先看到结果，再理解过程和作者的思考。

它不仅保存演示页面，还把演讲需要的视频、图片和 playground 一并放进仓库，形成可复现的演讲资料包。

## 实际使用时会看到什么

打开 `presentation.html` 后，会进入题为 “Code as a Medium for Storytelling | Zara @ Vibe Code Jam” 的演示。页脚显示完整演示共 15 页。

演示中可以切换项目故事、播放相关媒体，并使用仓库里的交互 HTML。仓库还保存了 YouTube to ebook、Codebase to groupchat 等项目的历史效果图。

## 核心实现

- 静态 HTML、CSS 和 JavaScript 组成演示运行时。
- 图片、MP4 和交互 playground 与主演示一起版本控制。
- 不依赖独立后端即可在浏览器播放。
- 项目成品截图同时成为其他仓库的历史效果证据。

## 适合谁

- 想用网页能力制作技术演讲的人。
- 需要在演讲中混合视频、交互页面和项目截图的创作者。
- 想研究如何把项目介绍写成故事，而不是 README 摘要的人。

## 验证情况与边界

本次通过本地 HTTP 服务实际打开了 `presentation.html`，确认标题页、导航与 15 页结构可以渲染。没有声称仓库中的所有视频和外部服务在本次环境重新生成或完整播放。

## 项目地址

GitHub：https://github.com/zarazhangrui/vibe-coding-jam-presentation

