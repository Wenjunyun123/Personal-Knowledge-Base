---
title: 笔记同步助手知识库索引
type: topic
aliases:
  - 知识库首页
tags:
  - knowledge-base/index
sources: []
created: 2026-08-10
updated: 2026-08-11
status: growing
---

# 笔记同步助手知识库

这里是“笔记同步助手”项目的导航入口。现有日期目录和 `images/` 保留为历史 Raw；新产生的结构化理解维护在 `wiki/`，规则与工作流维护在项目根目录。

## 从这里开始

- 维护规则：[[笔记同步助手/AGENTS]]
- 增量入库：[[笔记同步助手/workflows/增量入库]]
- 知识检索：[[笔记同步助手/workflows/知识检索]]
- 维护巡检：[[笔记同步助手/workflows/维护巡检]]
- 待人工确认：[[笔记同步助手/wiki/_待人工确认]]
- 变更记录：[[笔记同步助手/log]]

## 主题

- [[笔记同步助手/wiki/topics/AI 辅助个人知识管理]]

## 核心概念

- [[笔记同步助手/wiki/concepts/LLM Wiki]]
- [[笔记同步助手/wiki/concepts/Raw-Wiki-Schema 三层架构]]
- [[笔记同步助手/wiki/concepts/增量知识维护]]

## 工具与载体

- [[笔记同步助手/wiki/entities/Codex]]
- [[笔记同步助手/wiki/entities/Obsidian]]

## 已入库来源

- [[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]

## Raw 入口

- 历史同步资料：`笔记同步助手/YYYY-MM-DD/`
- 历史附件：`笔记同步助手/images/`
- 新的分类资料：[[笔记同步助手/raw/_README|raw 使用说明]]

## 当前策略

- 不搬迁历史日期目录，避免破坏同步工具和图片双链。
- 每次从一篇或一小批高价值资料开始，完成可追溯的增量更新。
- 产品推荐、模型版本和“最新”说法默认视为时效性信息，未经另行核验不升级为已确认事实。
- 当前 Git 根目录是父级 Vault `Personal-Knowledge-Base/`；origin 为 `Wenjunyun123/Personal-Knowledge-Base.git`，迁移后尚未提交或推送。
