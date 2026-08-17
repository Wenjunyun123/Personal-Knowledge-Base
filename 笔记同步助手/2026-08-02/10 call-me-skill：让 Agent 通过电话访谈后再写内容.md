---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/call-me-skill
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: 02ba193a-51db-4818-b8f8-539714fc5451
---

项目名称：call-me-skill

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：13

## 一句话理解

call-me-skill 让 Agent 主动给用户打电话，通过语音访谈收集想法，等转写完成后再起草 X 或 LinkedIn 内容，把“面对空白文档写作”变成“先聊再写”。

## 它具体解决什么问题

很多人并不是没有观点，而是不习惯坐在编辑器里从第一句话开始写。口头表达通常更自然，也更容易说出具体例子和个人判断。

这个项目使用 Retell AI 发起电话，把用户回答转成 transcript，再结合模板和个人记忆生成社交媒体草稿。

## 实际使用时会看到什么

Agent 判断需要更深入了解用户观点时，可以触发电话。用户接听后与语音 Agent 对话，完成一轮访谈。

通话结束后，脚本轮询 Retell 的转写状态。完整 transcript 返回后，Agent 根据 X 或 LinkedIn 的不同写作模板整理内容，并把新的个人偏好同步到记忆中。

## 核心实现

- `trigger-call.sh` 发起电话。
- `poll-transcript.sh` 等待并获取转写。
- `setup-agent.sh` 初始化 Retell Agent 配置。
- `sync-memory.sh` 把访谈信息更新到个人上下文。
- 模板区分不同社交平台的文章结构。

## 适合谁

- 口头表达比文字写作更顺畅的创作者。
- 需要定期整理个人观点、发布社交内容的人。
- 想探索 Voice Agent 与个人记忆结合方式的开发者。

## 验证情况与边界

本次检查了触发、轮询、配置和记忆同步脚本，但没有配置 Retell API Key、Agent ID 或电话号码，也没有触发真实通话。因此可以确认工作流设计和调用边界，不能把它描述成已在本次环境完成端到端通话。

## 项目地址

GitHub：https://github.com/zarazhangrui/call-me-skill

