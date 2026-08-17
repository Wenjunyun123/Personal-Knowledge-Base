---
author: 小 G
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzAxOTcxNTIwNQ==&mid=2457994581&idx=1&sn=0ae0cf3d382186aaa5c2ae81c6aa0ca6&chksm=8d4cdab82f63a200034904c71d75818122b10487023bfd9c6b116c741876cac273c38c850e04&mpshare=1&scene=1&srcid=0703eTJMf0LCRLBViSo0wbdx&sharer_shareinfo=cfa65126d41583d8bc19f93fce5b7d0e&sharer_shareinfo_first=cfa65126d41583d8bc19f93fce5b7d0e#rd
saved: 2026-07-03 01:46:44
tags:
  - 笔记同步助手
id: 19c23a91-4ec1-44c2-ab1c-46bed5ab0d67
---
公众号名称：GitHubDaily

作者名称：小 G

发布时间：
现在大部分开发者，都已经在用 Claude Code、Codex 辅助写代码。
但在实际工作当中，有时候代码的改动还是离不开编辑器，网页调试也还要打开浏览器。
这个时候就会打开好几个工具，在它们之间来回切换窗口，工作效率较低。
那有没有能把这些全部塞进一个原生终端里的工具，而不是在终端里依赖第三方插件。
无独有偶，在 GitHub 上挖到了  Terax ，一个仅 7MB 大小的轻量级 AI 终端工具。

![[笔记同步助手/images/6c82028a2dd09405bebaa0fe02f6d408_MD5.png|image-20260702190103622]]

体积虽小，但把 AI、终端、代码编辑器、文件管理器、网页预览全部都塞了进去。
最大亮点是侧边栏的 AI，是一个真能动手的 Agent，能读文件、改代码、跑 Shell 命令。
涉及到删写文件、执行命令这类高风险操作，也会弹出确认消息提醒，等我们点头才执行。
对于 AI 改动的代码可以让它不直接覆盖，而是弹出 diff 标签页，将改动一段段列出来。
先让我们审查是接受还是拒绝，对于公司项目来说，这种 AI 辅助写代码的方式还是最稳。

![[笔记同步助手/images/33914dcf9caba77377bbd18bc9b8d460_MD5.png|image-20260702190348220]]

另外还能给 AI 设定专门的子 Agent，比如配一个只读代码不给改权限的审查角色。
遇到复杂任务可以先切 Plan 模式，让它把步骤列出来给人过目，确认没问题再动手执行。
当需要执行一些耗时比较长的任务，还能放到到后台跑，不用一直盯着终端窗口等结果。

![[笔记同步助手/images/3cf7153e71c2e14870b8f86be14cda40_MD5.png]]

同时可以自由接入 OpenAI、Anthropic、Google 等主流模型服务商。
也可以通过 Ollama、LM Studio 接入本地跑的大模型，这样离线也能用，不需要联网。
对于密钥这些敏感数据，会存在系统的里，不会落进磁盘或者浏览器缓存，更加安全。
另外，它底层调用的是系统自带原生 WebView，没有把整个 Chromium 浏览器内核打包进去。

![[笔记同步助手/images/8b5151b79c446dec5ac15176b16f56a1_MD5.png|image-20260702190438995]]

对终端来说，它使用的是 WebGL 渲染，分屏、多标签这些都支持。
内置的代码编辑器用的是 CodeMirror 6，Python、Java、Rust 等主流编程语言都能写。
文件管理器也支持模糊搜索，而且支持选中文件直接拖进 AI 侧边栏当上下文使用。

![[笔记同步助手/images/53c1040a3889d8a1c12f151110febf64_MD5.png|image-20260702190139010]]

同时提供的 Git 面板多了个 Commit 视图，分支怎么分的、怎么合的，一眼就能看出来。
还有可以在项目根目录放一个  TERAX.md ，类似于  CLAUDE.md  文件。
可以把架构决策、踩过的坑、常用命令都能记进去，还能自己往里面补内容。
每次打开 AI 对话，先读一遍文件内容当上下文，不用每次都从头介绍一遍项目。
至于安装也不麻烦，提供开箱用的安装包，支持 macOS、Linux、Windows 系统。

![[笔记同步助手/images/297a3a9cb6a2d301bc8a57dfa276adf8_MD5.png|image-20260702190722202]]

当然它也还是有缺点的，不支持 LSP、代码跳转、类型提示等这些功能暂时没有。
另外也不支持安装第三方插件，相关扩展全靠官方自己更新维护，有时候还得换回 IDE 使用。
写在最后
但是工具这东西，并不是说非得大而全，本身Terax 也没打算取代 IDE。
它主要解决轻量、AI 优先、日常手动改代码等场景，让我们不用专门打开重量级的编辑器。
现在打着 AI 口号的开发工具一大堆，但不少都是套个壳，往里面塞个 AI 对话框的。
而 Terax 是从底层开始重构，专门为人与 Agent 协作干活的交互方式去设计。
体积小，不需要注册、不收集数据，开箱即用，这几点放在一起才是开源工具该有样子。
GitHub 项目地址： https://github.com/crynta/terax-ai
今天的分享到此结束，感谢大家抽空阅读，我们下期再见，Respect！

  

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/local-19c23a91-4ec1-44c2-ab1c-46bed5ab0d67?u=https%3a%2f%2fmp.weixin.qq.com%2fs%3f__biz%3dMzAxOTcxNTIwNQ%3d%3d%26mid%3d2457994581%26idx%3d1%26sn%3d0ae0cf3d382186aaa5c2ae81c6aa0ca6%26chksm%3d8d4cdab82f63a200034904c71d75818122b10487023bfd9c6b116c741876cac273c38c850e04%26mpshare%3d1%26scene%3d1%26srcid%3d0703eTJMf0LCRLBViSo0wbdx%26sharer_shareinfo%3dcfa65126d41583d8bc19f93fce5b7d0e%26sharer_shareinfo_first%3dcfa65126d41583d8bc19f93fce5b7d0e%23rd&s=obsidian)
