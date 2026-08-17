---
title: Raw-Wiki-Schema 三层架构
type: concept
aliases:
  - Raw Wiki Schema
  - 知识库三层架构
tags:
  - knowledge-base/concept
  - information-architecture
sources:
  - "[[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]"
created: 2026-08-10
updated: 2026-08-10
status: growing
---

# Raw-Wiki-Schema 三层架构

## 一句话定义

一种把原始证据、结构化理解和维护规则分离的知识库组织方式。[[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]

## 核心内容

| 层 | 保存什么 | 谁可以改 | 本项目中的位置 |
|---|---|---|---|
| Raw | 文章、对话、笔记、附件等原始证据 | 同步/导入工具写入后，Agent 只读 | `YYYY-MM-DD/`、`images/`、`raw/` |
| Wiki | 来源摘要、概念、实体、主题 | Agent 增量维护，人审核 | `wiki/` |
| Schema | 入库、引用、冲突与验收规则 | 人主导，Agent 可提出改进 | `AGENTS.md`、`index.md`、`log.md`、`workflows/` |

文章给出的原始模板使用独立 `raw/` 目录；当前项目已有日期目录和共享图片目录，因此本次采用兼容映射，而不是批量迁移。这个映射是针对当前 Vault 的工程决策，不是来源原文的固定要求。

## 适用范围与限制

- 分层能降低 Agent 修改原始证据的风险，并让结构化结论可追溯。
- 同一 Vault 同时存在兼容 Raw 与分类 Raw，会增加检索入口；`AGENTS.md` 和工作流必须持续约束查重与范围。
- 如果未来改变同步助手输出路径，应先验证附件路径、重复检测和移动后的双链，再决定是否迁移。

## 相关页面

- [[笔记同步助手/wiki/concepts/LLM Wiki]]
- [[笔记同步助手/wiki/concepts/增量知识维护]]
- [[笔记同步助手/wiki/topics/AI 辅助个人知识管理]]

## 来源

- [[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]

## 待核实

- 笔记同步助手是否支持自定义输出到 `raw/articles/`，以及改变路径后是否会影响现有图片链接。

