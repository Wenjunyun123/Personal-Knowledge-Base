---
author: GitHubDaily
source: X
url: https://x.com/GitHub_Daily/status/2123929429311451577?a=TaCuRpVoKcwxuh-C6Ag&s=19
saved: 2026-11-23 22:06:31
tags:
  - 笔记同步助手
id: 712305bf-cba6-4d04-930c-42f4ff4c1a7e
---

🔗 [在 X 查看原文](https://x.com/GitHub_Daily/status/2123929429311451577)

看了不少 Agent 教程，也跟着敲完一个能调工具的小 Demo，真要自己从头搭一个，还是不清楚循环、工具、记忆该怎么拼到一起。  
  
斯坦福今年秋季开了一门 Engineering AI Agents 课，课号 CS329Z，第一次作业的代码放出来了，题目就是从零搭一套 Agent Harness，也就是包在模型外面负责调工具、跑循环的那层程序。  
  
作业拿一家公司的邮件存档当素材，先写邮件优先级分类、每日摘要、关键词检索和邮件问答，再把这些接成一个能调工具、跑命令、带记忆的 Agent。  
  
GitHub：[github.com/cs329z/assignment1-harness](http://github.com/cs329z/assignment1-harness)  
  
测试分两种，一种不调模型，专查空回复、格式错乱、工具报错这些异常处理。另一种真调模型打分，光分类那题就要调 60 次模型，跑一分钟左右。  
  
最后还有一轮模拟测试，几个预设角色轮流来跟我们的 Agent 对话，看它能不能把事办成。  
  
每次调用模型都会记账，还能自己设预算上限，循环跑飞了会先停下。  
  
我觉得这份作业比看一堆教程管用，测试把要求写得很死，哪里没做对一跑就知道。想把 Agent 底层弄明白的，可以照着做一遍。

![[笔记同步助手/images/560a894405e124c056c62e57b9e8ecc1_MD5.jpg]]

---

## 💬 评论（4）

> **无事乱翻书 @parkmanpcl**
> 
> 不调模型、专测工具报错这些异常的部分挺实在，Demo 最容易跳过的就是“出错了以后怎么办”😂

> **Martin（搞钱版） @0xMartin0307**
> 
> 循环 工具 记忆怎么拼到一起 从零搭一遍比看十篇教程都管用

> **minyu @YangmaoRadar**
> 
> 补充个实操细节：仓库是公开的 MIT 协议，确定性测试不调模型、免费跑；live 测试要自己填 OPENROUTER\_API\_KEY 走自己的账，不过能用 CS329Z\_EVAL\_SLICE=N 只跑前 N 条省钱，还有预算上限防循环跑飞。

> **Bojie Li @bojie\_li**
> 
> 两个月没有更新了，《深入理解 AI Agent》发布 3.0 版本了！  
>   
> \- 重写了各章节的大部分内容，消除了一些 AI 味，把综述式的文风改成了教学式的，更容易理解  
> \- 新增 Jev 类决策模型在事件过滤、工具安全判断、评测 rubric、RAG 筛选、多模态信息稀疏化等方面的应用  
> \- 新增 Meta Muse、Pine、dsh superagent 等 personal agent 的办事逻辑  
> \- 新增 Multica、LobeHub 等办公 agent  
> \- 新增 Anthropic 证明黎曼猜想、OpenAI 证明千禧年问题等科研 agent  
> \- 修订语音交互部分，纳入一些最新的工作  
> \- 重绘书中大量插图  
> \- 新增社区翻译的蒙古语版本  
> \- 合入社区的 30+ PR，解决 20+ issues

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/774da86e_1795442790433?u=https%3A%2F%2Fx.com%2FGitHub_Daily%2Fstatus%2F2123929429311451577)