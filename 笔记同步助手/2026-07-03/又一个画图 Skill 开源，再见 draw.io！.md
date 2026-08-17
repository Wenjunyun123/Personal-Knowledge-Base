---
author: 小 G
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzAxOTcxNTIwNQ==&mid=2457994592&idx=1&sn=a75ae3bacc04af4ba98e22527e7a7d53&chksm=8d69903f305dc8a0ba41f66bbdff3f78245ab9cfcbc8120460f66086e697217363735d751fca&mpshare=1&scene=1&srcid=07033jFRicxvo1mqAZBbIwwV&sharer_shareinfo=997549eb7c5c97c9364130e88d21be2d&sharer_shareinfo_first=997549eb7c5c97c9364130e88d21be2d#rd
saved: 2026-07-03 23:31:24
tags:
  - 笔记同步助手
id: 72518bb7-c203-47c3-944d-99dd97f5133f
---
公众号名称：GitHubDaily

作者名称：小 G

发布时间：
很多时候开发者，需要向大家介绍清楚一个项目、一个功能的技术实现方案。
光是通过文字介绍，其实很多人都看不太懂，或者说不够直观通俗理解。
而通过一张清晰的架构图来讲解，效果就不一样了，但自己动手画图，还真折磨人的。
打开 draw.io 一个个框拖过去，对齐、连线、调颜色，半天时间就没。
后来有了 AI 后，便让它帮我们生图，但生成的效果总觉得差点意思。
直到最近，我在 GitHub 上偶然发现一个开源画图 Skill： Archify ，效果颇为不错。

![[笔记同步助手/images/4eb2bf8c84a003896ec30c961f7b8522_MD5.png|image-20260703175045606]]

把它装进 Claude Code、Codex 或者 OpenCode 等 Agent  工具之后。
只需要在对话里，用大白话把需求简单描述一遍，就能给我们生成想要的架构图。
比如说一句「用户请求先过网关，鉴权走 Redis，缓存没中就落到 Postgres」，一张时序图就有了。

![[笔记同步助手/images/bb981afe5617d9124e0832c595214ebb_MD5.png|image-20260703175127568]]

如果懒得自己组织语言，也可以直接让 Agent 分析当前代码库，自动整理出架构再出图。
生成的产物是一个 HTML 文件，没有任何依赖，可以直接发给同事打开查看。
甚至还内置深浅两套主题，一键切换，可以分别截图放到文档里看哪个主题更合适。

![[笔记同步助手/images/67cb06eb38dc612c19e042b0d7cd7014_MD5.png|image-20260703175345533]]

除了能画架构图外，工作流、时序图、数据流、生命周期，这些类型都支持。
像 CI/CD 流水线、审批流程、ETL 管道、订单状态机，日常技术常见画的图基本都可以。
而文件导出做的也不错，支持 PNG、JPEG、SVG、WebP 原生 4 倍高清分辨率渲染图导出。

![[笔记同步助手/images/c026b49257a9b0fefb2c33ec9138a56c_MD5.png|image-20260703175249521]]

同时是已经复制到剪贴板，转头就能贴进文档、PPT 或者项目 README 介绍里。
对于 SVG，导出的文件会同时带着深浅两套配色，可跟随系统的外观设置自动切换。
贴进到 GitHub README 后，系统若是深色模式看到深色图，浅色模式则看到浅色图。

![[笔记同步助手/images/c393b315d2b214eafa840a24c8dcd1db_MD5.png|image-20260703175535154]]

如果图画得不满意，可以继续在 Agent 对话里对它进行修改，改动满意为止。
另外这个 Skill 在导出图前，还会检查一遍图是否存在错乱的箭头、连线错误等问题。
先修复了再导出，避免让我们看到这些最基础的问题，还得我们反复让它调整修改。
至于安装使用，项目 README 给出的步骤挺麻烦的，我们直接让 Agent 自己装即可：

帮我安装一下这个 Skill，https://github.com/tt-a1i/archify
剩下的事 Agent 自己搞定。安装过程有个小门槛，渲染校验依赖到一个第三方包。
首次使用需要安装一下，不过这些 Agent 一般都会顺手帮我们装好。
写在最后
关于画图这件事上看似简单，但在我们的技术沟通里却能帮上大忙。
比如产品方案评审、新人交接、技术复盘，说再多的话，都不如看一张图来得直观。
过去画一张图，不仅要学习 Draw.io 工具的使用，还得花费时间成本。
现在有了这个 Skill，只需要在 Claude Code 或 Codex 上面，一句话描述即可生成。
这些 Agent 工具越来越像一个底座，真正的生产力，藏在我们往里装的一个个 Skill 里。
这个画图的 Skill，不妨收藏备用一下，如果有需要可以马上安装使用。
GitHub 项目地址： https://github.com/tt-a1i/archify
今天的分享到此结束，感谢大家抽空阅读，我们下期再见，Respect！

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/local-72518bb7-c203-47c3-944d-99dd97f5133f?u=https%3a%2f%2fmp.weixin.qq.com%2fs%3f__biz%3dMzAxOTcxNTIwNQ%3d%3d%26mid%3d2457994592%26idx%3d1%26sn%3da75ae3bacc04af4ba98e22527e7a7d53%26chksm%3d8d69903f305dc8a0ba41f66bbdff3f78245ab9cfcbc8120460f66086e697217363735d751fca%26mpshare%3d1%26scene%3d1%26srcid%3d07033jFRicxvo1mqAZBbIwwV%26sharer_shareinfo%3d997549eb7c5c97c9364130e88d21be2d%26sharer_shareinfo_first%3d997549eb7c5c97c9364130e88d21be2d%23rd&s=obsidian)
