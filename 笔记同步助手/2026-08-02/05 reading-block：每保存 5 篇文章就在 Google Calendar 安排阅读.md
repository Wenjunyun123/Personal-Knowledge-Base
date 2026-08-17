---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/reading-block
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: d2aa140f-2a61-483c-af12-2542961e3bc1
---

项目名称：reading-block

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：93

## 一句话理解

reading-block 是一个 Chrome 扩展，把“稍后阅读”从不断增长的收藏夹变成日历承诺：每累计保存 5 篇文章，就在 Google Calendar 中安排一个 30 分钟阅读时间块。

## 它具体解决什么问题

多数稍后阅读工具只负责收藏，不负责让用户真正读完。文章越存越多，列表本身就会变成新的信息负担。

reading-block 没有继续优化收藏体验，而是把阅读任务绑定到时间。它用一个简单规则建立反馈：5 篇文章对应一个 30 分钟日历块。

## 实际使用时会看到什么

用户可以通过扩展按钮或右键菜单保存当前文章。扩展的管理页面显示待读列表、已完成状态和阅读块安排情况。

达到 5 篇后，扩展会查找合适时间并向 Google Calendar 创建 30 分钟日程。读完文章后可以在本地列表中完成打卡。

## 核心实现

- Chrome Manifest V3 扩展。
- 使用 `storage` 保存本地文章和状态。
- 使用 `identity` 完成 Google OAuth。
- 通过 Google Calendar API 查找时间并创建事件。
- `contextMenus`、`activeTab`、`alarms` 等权限支撑保存和提醒。

## 适合谁

- 收藏很多文章，却很少真正回去阅读的人。
- 希望把输入型学习任务放进日历的人。
- 想研究小型 Chrome 扩展如何接入 Google Calendar 的开发者。

## 验证情况与边界

本次使用仓库未修改的 `options.js` 和 `styles.css` 在浏览器中渲染了真实管理界面，并通过 harness 注入代表性的 `chrome.storage` 数据。界面效果和逻辑来自仓库，数据不是用户真实收藏。由于 OAuth Client ID 需要用户配置，本次没有向真实 Google Calendar 写入日程。

## 项目地址

GitHub：https://github.com/zarazhangrui/reading-block

