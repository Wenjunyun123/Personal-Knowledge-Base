---
author: Xudong Han
source: X
url: https://x.com/i/status/2077246527756775933
saved: 2026-07-16 01:04:37
tags:
  - 笔记同步助手
id: 350c9019-d556-41de-bade-6d1969c672fb
---

🔗 [在 X 查看原文](https://x.com/Xudong07452910/status/2077246527756775933)

OpenAI 公布了 GPT-5.6 Sol 的最新提示词指南，核心可能就一句话：少写点废话，把任务边界讲清楚。  
  
这份文档真的很值得看，它并不是教你继续堆更长的 system prompt，而是建议把 prompt 做轻：目标是什么、成功标准是什么、哪些证据必须有、什么时候该停、哪些动作需要确认。  
  
这其实很符合新一代 Agent 的变化。  
  
模型越来越强以后，过度规定每一步流程，反而可能拖慢它、增加 token、制造冲突。真正重要的是给它一个清楚的任务契约，让它在安全边界内自己选择路径。  
  
我觉得这对 AI coding 特别有启发。  
  
以后写 AGENTS.md / system prompt，重点不再是把模型管得越死越好，最重要的是把验收标准、权限边界和验证流程写得足够清楚。  
  
[developers.openai.com/api/docs/guides…](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6)

---

**🧵 作者续推（1）**

> **2/** 关于最近有人使用 GPT-5.6 Sol 导致本地文件被删除这件事，该帖子有详细的解释。[x.com/Xudong07452910/status/207734090…](https://x.com/Xudong07452910/status/2077340904176722307?s=20)

---

## 💬 评论（11）

> **Keane @keane42443**
> 
> 这个真的是好东西，我今天就被震惊到了，真的一点废话不说 [t.co/WEc2xhtoIF](https://t.co/WEc2xhtoIF)
> 
> ![[笔记同步助手/images/ef9f266d1557cb554bb86626b4e2a3c6_MD5.jpg]]

> **石竟男 @shijingnan\_X**
> 
> 少写废话这条我太需要了😂 我现在最怕的不是不会写，是为了显得认真，先给它塞半页背景。

> **Uncle J @UncleJAI**
> 
> 这句我最近真有体感。模型强了以后，AGENTS.md 写得像百科全书，反而会把多个旧规则一起激活。现在我更愿意只钉四件事：目标、不可越界的权限、验收证据、何时停手。路径让模型选，但结果必须能复核。

> **Martin @php\_martin**
> 
> 👍 核心抓得准！模型越强，越要少 micromanage，多给清晰的“任务契约”（目标 + 成功标准 + 边界 + 停止条件）

> **Evan.Z @ddny09**
> 
> 确实这波提示词轻量化太对了，模型强了就别当保姆使唤，边界清楚就够了

> **ruoshuikun @ruoshuikun**
> 
> get 马上实践

> **安叫兽|Bird🕊️ 🔶 BNB @ajs6888**
> 
> 现在写 prompt 反而像写产品需求了

> **Loong🐉 @JiangL17208**
> 
> 这份指南的重点不是再写更长的 system prompt，而是把边界写清楚：目标、成功标准、证据、停损、需确认动作。Sol 这类模型对「任务合同」比堆话术更敏感。

> **WEEX AI Labs @WEEXAILabs**
> 
> 👀

> **福宝MM @linyi64965449**
> 
> OpenAI 公布了 GPT-5.6 Sol 的最新提示词指南，核心可能就一句话：少写点废话，把任务边界讲清楚。 这份文档真的很值得看，它并不是教你继续堆更长的 system prompt，而是建议把 prompt 做轻：目标是什么、成功标准是什么、哪些证据必须有、什么时候该停、哪些动作需要确认。

> **Gerard Sans | Axiom 🇬🇧 @gerardsans**
> 
> [x.com/gerardsans/status/2077185128757…](https://x.com/gerardsans/status/2077185128757944659)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/ecd1859b_1784135074563?u=https%3A%2F%2Fx.com%2FXudong07452910%2Fstatus%2F2077246527756775933)