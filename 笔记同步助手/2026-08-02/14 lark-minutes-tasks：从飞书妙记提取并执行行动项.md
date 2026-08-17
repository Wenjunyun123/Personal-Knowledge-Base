---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/lark-minutes-tasks
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: 1b004238-503d-4ece-83af-2a676cb3afb8
---

项目名称：lark-minutes-tasks

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：63

## 一句话理解

lark-minutes-tasks 是一个会后行动 Skill：读取飞书妙记或文档转写，提取明确与隐含行动项，先让用户选择，再通过 lark-cli 创建任务、日历、文档或发送消息。

## 它具体解决什么问题

会议转写只能回答“大家说了什么”，不能保证事情真的被执行。会后最容易丢失的是谁负责、何时完成、需要通知谁，以及哪些承诺虽然没有说成任务句式，却已经隐含在对话里。

这个项目把转写阅读、行动识别、人类确认和工具执行连接起来。

## 实际使用时会看到什么

用户通过一条命令或 wake word 启动流程。Agent 读取飞书妙记或相关文档，整理出编号行动清单，区分明确任务和根据上下文推断出的隐含任务。

用户选择需要执行的项目后，Agent 才调用 lark-cli，完成创建日历、任务、文档、搜索资料或发送消息等操作。

## 核心实现

- `minutes.md` 定义完整命令行为和交互顺序。
- 先提取，再确认，最后执行，避免直接把推断当成用户指令。
- 使用 lark-cli 复用已有飞书授权和工具能力。
- 可以同时处理 Calendar、Tasks、Docs、Search 和 Messages。

## 适合谁

- 会议多、行动项容易散落在转写中的团队。
- 已经在飞书中管理任务、日历和文档的人。
- 想研究 Human-in-the-loop Agent 设计的开发者。

## 验证情况与边界

本次检查了 `minutes.md` 的命令规范和确认式执行流程，没有读取用户会议、没有连接飞书账号，也没有创建任务或发送消息。项目的重点是会议后的行动层，不是语音转写服务本身。

## 项目地址

GitHub：https://github.com/zarazhangrui/lark-minutes-tasks

