---
title: LLM Wiki
type: concept
aliases:
  - LLM 维基
  - Agent 维护型 Wiki
tags:
  - knowledge-base/concept
  - personal-knowledge-management
sources:
  - "[[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]"
created: 2026-08-10
updated: 2026-08-10
status: seed
---

# LLM Wiki

## 一句话定义

在本知识库中，LLM Wiki 指由 Agent 按长期规则增量维护、能追溯到原始资料的结构化知识层，而不是一次查询后即丢弃的临时回答。[[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]

## 核心内容

- 新资料进入后，先搜索已有 Wiki，再决定补充旧页或创建新页。
- 知识被拆为来源、概念、实体和主题页面，并通过双链关联。
- 分歧不会被静默覆盖，而是连同来源、时间和适用范围保留。
- 每轮维护都要更新索引与日志，留下可检查的持久变化。

以上是指定来源提出的方法框架，尚不是对所有 LLM 知识库实现的通用定义。[[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]

## 适用范围与限制

- 适合本地 Markdown、需要人工掌控规则与来源的个人知识管理。
- Agent 仍可能误读、漏引或过度拆页，因此必须有人审阅和校验。
- 页面持续增加后，需要定期合并同义页、检查孤立页和处理陈旧结论。

## 相关页面

- [[笔记同步助手/wiki/concepts/Raw-Wiki-Schema 三层架构]]
- [[笔记同步助手/wiki/concepts/增量知识维护]]
- [[笔记同步助手/wiki/topics/AI 辅助个人知识管理]]

## 来源

- [[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]

## 待核实

- 该术语与 Karpathy 原始材料中的用法是否完全一致。

