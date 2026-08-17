---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/longcut
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: e5f31f14-5ef4-482b-85a2-ff0cf224b129
---

项目名称：longcut

项目作者：SamuelZ12；Zara Zhang 的仓库为 fork

分析日期：2026-08-02

Star 快照：35

## 一句话理解

LongCut 是一个围绕 YouTube 长视频建立的 AI 学习应用。用户粘贴视频链接后，可以查看高光片段、同步转写、带时间戳问答、笔记和个人内容库。

## 它具体解决什么问题

长视频的信息密度不均匀。用户往往需要反复拖动进度条，才能找到关键片段；看完之后，笔记又与视频时间轴脱节。

LongCut 把视频、transcript、AI 问答和笔记放进同一个界面，回答可以回到具体时间点，减少模型脱离原视频自由发挥的空间。

## 实际使用时会看到什么

公开首页提供 YouTube URL 输入框。进入视频工作区后，可以浏览高光、选择不同语言 transcript、边看视频边阅读转写，并围绕视频提问。

仓库功能图还展示了多语言 transcript 选择器、视频播放器和高光区域。用户可以把视频与笔记保存在个人库中。

## 核心实现

- Next.js 15 与 React 19 前端。
- xAI 和 Gemini 模型适配器。
- Supadata 获取视频 transcript。
- Supabase 负责认证、数据持久化与限流。
- 依赖中包含 Stripe 支付能力。
- 安全中间件处理请求边界。

## 适合谁

- 经常通过 YouTube 长视频学习的人。
- 需要时间戳证据，而不是普通视频摘要的人。
- 想研究视频转写、RAG、笔记和用户系统如何组合的开发者。

## 验证情况与边界

本次实际打开了 https://www.longcut.ai/ 的公开首页，并检查了 Next.js、模型、Supabase 和转写相关源码。为了避免使用第三方额度或产生外部数据，本次没有提交视频 URL、登录账号或运行完整生成流程。

必须明确：该仓库是 `SamuelZ12/longcut` 的 fork，不能把上游项目全部实现归为 Zara Zhang 的原创开发。

## 项目地址

GitHub：https://github.com/zarazhangrui/longcut

公开网站：https://www.longcut.ai/

