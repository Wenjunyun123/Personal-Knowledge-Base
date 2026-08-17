---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/beautiful-feishu-whiteboard
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: a3e6d05d-b3de-4984-be7e-d3f512e359b6
---

项目名称：beautiful-feishu-whiteboard

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：617

## 一句话理解

beautiful-feishu-whiteboard 是一套给 Agent 使用的飞书白板设计 Skill，提供 35 种经过整理的配色、排版和图形风格，让生成的白板不再只有默认流程图效果。

## 它具体解决什么问题

Agent 能生成节点和连线，但“信息正确”不代表“白板好看”。如果没有明确设计规则，生成结果通常会出现层级不清、配色随意、连线拥挤和画布利用率低的问题。

这个项目把视觉风格变成可复用规范。Agent 可以根据内容选择 Editorial Forest、Neo Grid Bold 等设计方向，再用飞书原生可编辑图形搭建白板。

## 实际使用时会看到什么

每种风格都给出实际模板图，明确背景、主色、强调色、字体层级、卡片样式和连接方式。生成后的白板仍然由原生形状和 SVG 元素组成，用户可以在飞书里继续编辑，而不是只能得到一张不可修改的截图。

仓库截图展示了同一“LLM 训练三阶段”内容在不同视觉系统下的效果：Editorial Forest 使用克制的绿色和粉色，Neo Grid Bold 则采用黑色与荧光黄的强对比。

## 核心实现

- 35 套可检索的白板风格资产。
- 强调原生形状、连接器和信息层级。
- `RULES.md` 记录飞书白板真实渲染限制。
- 设计规范与生成步骤一同交给 Agent，而不只是提供配色表。

项目还明确提醒：飞书白板可能忽略透明度；导出图片时文字颜色有时不可靠；需要读取 live 或 raw 数据确认真实样式。

## 适合谁

- 经常用飞书白板做架构图、流程图和项目说明的人。
- 希望 Agent 生成结果仍可手工调整的团队。
- 想建立统一白板视觉语言的设计或产品团队。

## 验证情况与边界

本次检查了风格资产、规则文件和仓库真实模板截图。没有连接用户飞书空间，也没有代替用户创建白板。展示效果来自仓库保存的模板，不是本次重新绘制后冒充的成品。

## 项目地址

GitHub：https://github.com/zarazhangrui/beautiful-feishu-whiteboard

