---
author: Amto
source: X
url: https://x.com/XAMTO_AI/status/2079379079879385296?s=20
saved: 2026-07-22 00:09:51
tags:
  - 笔记同步助手
id: a8a68f1d-56d6-4f17-8c23-24c1eef8c0af
---

🔗 [在 X 查看原文](https://x.com/XAMTO_AI/status/2079379079879385296)

大型项目里问AI一个问题，它转头读几十个文件，代码还没开始写，token先烧掉一大截。这不是窗口不够大，是每次都要重新扫描。  
  
Graphify把这件事反过来。一次性把整个项目（代码、文档、PDF、图片）扫描成知识图谱存到本地，之后每次查询走图遍历，不再重新读原始文件。  
52个文件的混合语料上，每次查询token消耗降低71.5倍。  
  
代码用tree-sitter做AST解析，本地跑、不联网，提取的函数调用和import关系打上EXTRACTED标签。音频视频用faster-whisper本地转录。文档、PDF、图片走LLM做语义提取，这部分有token消耗，但SHA256缓存确保只跑变更过的文件。  
  
每条关系标了置信度：EXTRACTED是代码里直接可查的，INFERRED是模型推断的，AMBIGUOUS是不确定的。至少你知道哪些结论能信。  
  
输出三样：交互式HTML图谱、文字报告、graph.json持久化数据。  
  
Python3.10+，pip install graphifyy，graphify install注册到AI助手，对话框输入/graphify .。支持Claude Code、Cursor、Codex、OpenCode等20多个平台。  
  
高频查询场景省token效果最明显。  
  
[github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

![[笔记同步助手/images/729e725351b8bf5211b9832641728f35_MD5.png]]

---

## 💬 评论（7）

> **JahoJiang @JahoJiang**
> 
> 大型项目里文件频繁被修改，Agent在编辑时总要比较文件状态然后重新读取，这样的话这个项目的收益还有那么乐观吗

> **Martin @php\_martin**
> 
> 知识图谱能减少重复扫描，但代码频繁变化时增量更新才是决定体验的部分

> **hanqing @hanqing1120**
> 
> AI吃token像吃自助，Graphify直接开了个小灶，71.5倍省token，程序员钱包直呼内行。

> **高返70 BG云舟Visa卡可领 @ReannaKingdjj**
> 
> 终于不用狂烧token了

> **谭婧🌸同城上门♥极品外围 @AldenMaryewnk6**
> 
> 💞

> **尼古拉斯定投 @Nicolas\_DCA**
> 
> 其实这才是AI落地的现实问题：上下文不是越长越好，是越聪明越好。提前建图一次、查询走捷径，才是真正的工程思维。

> **Geek @geekbb**
> 
> Pi-Agent 教程：10 章把 Agent Loop、工具系统、消息系统、事件驱动、会话管理和上下文工程全部拆了一遍。每章都讲三层：概念是什么、源码怎么写的、为什么这么设计。三种阅读方式：Web 在线版带三栏配图、本地 Markdown 和 PDF 离线版。  
>   
> [github.com/buchidonggua/dg-ai-notes](https://github.com/buchidonggua/dg-ai-notes) [t.co/rrpcuX7sVM](https://t.co/rrpcuX7sVM)
> 
> ![[笔记同步助手/images/6dbb43390433f9657f84159061208eb6_MD5.jpg]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/d25a85be_1784650189975?u=https%3A%2F%2Fx.com%2FXAMTO_AI%2Fstatus%2F2079379079879385296)