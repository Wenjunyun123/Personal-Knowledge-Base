---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/reading-block-lark
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: 7ba9c97f-4843-4c57-87dd-05470a2728df
---

项目名称：reading-block-lark

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：42

## 一句话理解

reading-block-lark 是 reading-block 的飞书版：同样以“每保存 5 篇文章，就安排 30 分钟阅读”为核心，但日程写入从 Google Calendar 改成了飞书日历。

## 它具体解决什么问题

对主要在飞书里工作的人来说，把阅读时间放进 Google Calendar 可能形成两个日历。这个版本让待读文章与工作日程进入同一个飞书时间系统。

项目还刻意采用本地 helper，而不是建立一个新的云端服务。浏览器里的文章数据保留在本地，只有创建日历所需的请求被发送给本机程序。

## 实际使用时会看到什么

扩展端负责保存文章、累计批次、展示本地列表和完成状态。达到 5 篇后，它会访问 `127.0.0.1:8787` 上的 Node helper，请求创建一个飞书日历块。

本地 helper 再调用已经由用户授权的 lark-cli，与飞书 Calendar API 交互。扩展本身不直接保存飞书密钥。

## 核心实现

- Chrome Manifest V3 扩展。
- Manifest 的 host permission 仅指向 localhost helper。
- `server.js` 在本机监听 8787 端口。
- storage、slots、batch、calendar 等模块管理文章与时间块逻辑。
- lark-cli 负责实际的飞书认证和日历操作。

## 适合谁

- 工作和个人计划主要放在飞书日历中的用户。
- 希望阅读数据尽量留在本机的人。
- 想研究浏览器扩展、本地 helper 与企业 API 分层方式的开发者。

## 验证情况与边界

本次检查了 Manifest、本地 helper 和共享模块，确认扩展到 localhost 再到 lark-cli 的调用路径。由于没有使用用户飞书授权，本次没有创建真实日程。项目仍需要用户先完成 lark-cli 的飞书认证。

## 项目地址

GitHub：https://github.com/zarazhangrui/reading-block-lark

