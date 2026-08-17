---
author: Chasen
source: X
url: https://x.com/i/status/2079386843926442013
saved: 2026-07-21 23:56:34
tags:
  - 笔记同步助手
id: 9b3751a6-699d-49e7-a642-3162c01e71bc
---

🔗 [在 X 查看原文](https://x.com/chasen_liao/status/2079386843926442013)

我看 Cursor 最近写了一篇很值得看的 agent-swarm 文章：（也就是 Agent 蜂群）  
  
[cursor.com/zh-Hant/blog/agent-swarm-m…](https://cursor.com/zh-Hant/blog/agent-swarm-model-economics)  
  
核心其实不复杂：  
  
“把一个大任务变成一棵树”  
  
最上层是 Planner，负责理解目标、拆分任务、做架构决策。  
  
下面是 Worker，负责执行具体的小任务  
  
Planner 不写代码，Worker 也不需要理解整个项目。  
  
这就是第一层控制：隔离上下文。  
  
单个 Agent 最容易出现的问题是：  
  
它一边看全局目标，一边钻进局部实现。  
  
上下文越来越长，最后不是忘了全局，就是局部写崩。  
  
Cursor 的做法是让 Planner 保持全局视角，让 Worker 只处理一小块明确工作  
  
第二层控制，是隔离 ownership  
  
每个 Worker 在自己的代码副本里工作，完成后只提交一份 handoff：  
  
做了什么、发现了什么、还有什么风险  
  
它们不需要互相聊天，而是通过 Planner 向上汇报  
  
第三层控制，是把协作信息写进环境  
  
比如设计决策、共享文档、Field Guide  
下一个 Agent 不需要读完所有历史对话，只要读取已经沉淀下来的关键经验  
这有点像蚂蚁通过环境协作，而不是靠所有蚂蚁互相开会  
  
第四层控制，是专门处理冲突  
  
Planner 冲突，就合并设计决策。  
  
代码冲突，就交给中立的 Agent 处理。  
文件太大，就暂停提交并拆分模块。  
  
不是让所有 Agent 自由发挥，然后祈祷它们最后能 merge  
  
这套结构最终带来了什么？  
  
在 SQLite 重建实验中，Cursor 称新版 Agent Swarm 使用 Grok 4.5 在 4 小时内达到约 80% 测试通过率，而旧版还没到 2 小时就失控暂停。  
  
所以 Agent Swarm 的核心不是：  
  
“同时启动 1000 个 Agent。”  
  
而是：  
  
“如何让每个 Agent 只知道自己该知道的东西，只负责自己该负责的事情，并把结果交回正确的控制层。”  
  
这其实很像一个递归的管理系统：  
  
Planner 管理子 Planner。  
子 Planner 管理 Worker。  
Worker 负责具体执行。  
测试和 Review 负责反馈。  
  
套控制结构很值得学习：  
  
上下文隔离、任务 ownership、结构化 handoff、独立 Review  
  
并发只是表面  
  
真正让 Agent Swarm 变强的，是控制算法  
  
#AIAgent #Cursor #VibeCoding

![[笔记同步助手/images/24c244985084cef6eec4c5541c2d8b7a_MD5.jpg]]

---

## 💬 评论（6）

> **闪光小猫 🫆 @\_4gui**
> 
> 这不是 actor 吗

> **安叫兽|Bird🕊️ 🔶 BNB @ajs6888**
> 
> Planner 不写代码这点还挺关键，少背锅

> **lifcc @mylifcc**
> 
> 真详细

> **DoDo🍊同城约P🍊点主页 @brianna65at5**
> 
> 🌧️remarkable🐾

> **土豆喵🍊同城约P🍊看简介 @andrea38mt3**
> 
> 🌲glowing🕷️

> **甜甜🍊同城约P🍊点主页 @caitlyn52zk3**
> 
> 🦈witty🥛

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/0233a26c_1784649391366?u=https%3A%2F%2Fx.com%2Fchasen_liao%2Fstatus%2F2079386843926442013)