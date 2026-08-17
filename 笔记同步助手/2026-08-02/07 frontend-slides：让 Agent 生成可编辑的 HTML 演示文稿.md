---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/frontend-slides
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: f3fc59b5-4d31-4425-a654-6dba3cf28e2e
---

项目名称：frontend-slides

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：26,728

## 一句话理解

frontend-slides 是一个演示文稿生成 Skill，让 Agent 把主题、文档、网页或现有 PPTX 转成零依赖的 HTML 幻灯片，并保留动画、交互、编辑和部署能力。

## 它具体解决什么问题

传统 PPT 工具适合手工拖拽，但 Agent 很难稳定控制每一页的对齐、动效和响应式行为。单纯让模型输出 HTML，又容易出现页面溢出、风格漂移和移动端重排。

frontend-slides 不只提供提示词，而是同时定义设计选择流程、固定舞台、交互运行时、模板包和浏览器验证方法，把生成演示变成可重复的工程流程。

## 实际使用时会看到什么

最终产物是一个可以直接打开的 HTML 文件。用户可以用方向键、滚轮或触摸手势翻页，进入全屏，打印或导出 PDF，还可以进入编辑模式直接修改文字。

仓库包含 34 套大胆模板和一组安全预设。Agent 会先选择视觉语言，再生成整套演示，而不是让每一页随机换风格。

## 核心实现

- 固定 1920×1080 的 16:9 舞台，按视口整体缩放。
- 自带键盘、触摸、滚轮、页码和进度条控制。
- HTML 可零依赖运行，也支持 Google Fonts 等外部字体。
- 提供 PPTX 内容提取、PDF 导出和部署脚本。
- 强制使用浏览器截图与布局审计验证结果。

## 适合谁

- 希望让 Codex、Claude Code 等 Agent 直接制作演示的人。
- 需要比传统 PPT 更自由的网页动效和交互的人。
- 想把演示作为可部署网页交付的团队。

## 验证情况与边界

本次仓库分析本身就使用了 frontend-slides 的设计与运行时规范，最终生成了一套 28 页的 Repository Atlas HTML 演示，并通过浏览器检查 28 页布局、14 张图片和 42 个链接。因此，本次不仅阅读了说明，也实际使用了该 Skill。它仍然不是传统 WYSIWYG 编辑器，主要入口是 Agent 工作流和 HTML。

## 项目地址

GitHub：https://github.com/zarazhangrui/frontend-slides

