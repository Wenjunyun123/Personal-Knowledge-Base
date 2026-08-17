---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/follow-builders
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: 07372803-4e9f-493b-9c12-cb6057327cd2
---

项目名称：follow-builders

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：6,114

## 一句话理解

follow-builders 是一个面向 Coding Agent 的信息订阅 Skill。它追踪播客、X 帖子和 AI 公司博客，把新增内容整理成每日或每周简报，再根据个人偏好完成本地投递。

## 它具体解决什么问题

真正耗时的往往不是“找到一个信息源”，而是长期追踪多个创作者、过滤重复内容、判断哪些内容值得看，再把结果放进自己的阅读流程。

这个项目把流程拆成两层：中央仓库维护预生成的公共 feed，本地 Agent 保存关注对象、摘要风格和投递节奏。这样既避免每个用户重复抓取同一批公开内容，又不会把个人偏好集中上传。

## 实际使用时会看到什么

用户可以订阅特定播客、X 账号或公司博客，选择 daily 或 weekly 节奏。Agent 读取最新 feed，筛选自上次投递以来的新条目，生成一份带标题、来源、摘要和链接的 digest。

仓库中的 feed JSON 是实际数据，而不是只写在 README 里的概念。本次检查到 2026-08-02 生成的播客和 X feed，其中包含最新节目与创作者动态。

## 核心实现

- `generate-feed.js` 负责生成和更新公共信息流。
- `prepare-digest.js` 根据时间窗口和用户偏好准备简报。
- `deliver.js` 负责本地投递和状态记录。
- 本地锁与状态文件避免重复投递。

整个数据流可以概括为：公开来源 → 结构化 feed → 本地筛选 → daily / weekly digest。

## 适合谁

- 希望持续追踪 AI 创作者和公司动态的人。
- 已经在使用 Codex、Claude Code 等 Agent，希望把资讯获取也做成 Skill 的人。
- 不想再依赖传统 RSS 阅读器手工筛选大量信息的人。

## 验证情况与边界

本次实际检查了当前 feed JSON、摘要准备脚本和投递脚本。仓库中的 `examples/sample-digest.md` 只是示例，因此没有把它当成本次真实生成的简报。由于没有配置用户的消息渠道，本次也没有实际发送任何内容。

## 项目地址

GitHub：https://github.com/zarazhangrui/follow-builders

