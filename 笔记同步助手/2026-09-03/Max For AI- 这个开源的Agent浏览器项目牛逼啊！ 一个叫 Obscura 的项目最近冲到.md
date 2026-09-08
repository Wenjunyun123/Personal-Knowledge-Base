---
author: Max For AI
source: X
url: https://x.com/MaxForAI/status/2095168688643293458
saved: 2026-09-03 09:24:21
tags:
  - 笔记同步助手
id: f4d4f2bc-cdba-425f-ba1f-398edbb51caf
---

🔗 [在 X 查看原文](https://x.com/MaxForAI/status/2095168688643293458)

这个开源的Agent浏览器项目牛逼啊！  
  
一个叫 Obscura 的项目最近冲到 GitHub 22K Star，它干的事情很简单：重新造一个专门给 Agent 用的浏览器。  
  
Rust 编写，约 30MB 内存，不依赖 Chromium、不依赖 Node.js，直接运行 V8，同时兼容 CDP，原来的 Puppeteer / Playwright 基本不用推倒重来。  
  
Chrome 是给人设计的。  
  
标签页、扩展、视频、同步、账户、无障碍、各种 UI，一整套庞大的桌面浏览器基础设施。  
  
Agent 真正需要的东西少得多：运行 JS、读 DOM、发网络请求、点按钮、填表、截图。  
  
当未来一台服务器上同时跑几百甚至几千个 Browser Agent 时，每个实例占 200MB 和占 30MB，已经不是优化问题，而是基础设施成本的问题。  
  
顺便一提，Cloudflare 做 Agent 浏览器 Kitesurf 时，第一个原型就是从 Obscura 移植过去的。

![](https://pbs.twimg.com/media/HROIs2zbQAA3cSG.jpg)

---

**🧵 作者续推（1）**

> **2/** 官方 @obscura\_sh  
>   
> [github.com/h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura?ref=selfh.st)

---

## 💬 评论（16）

> **Le Kai @lekai2k**
> 
> 和ego-lite相比呢

> **JimiLonbo @jimmy\_longbow\_**
> 
> 和ego lite对比怎么样

> **fanghsoufanji @yg6888**
> 
> 感谢分享，明天用用看

> **Crio Songo @shuizhuyu**
> 
> 这个思路真的戳中痛点了，给Agent做专用浏览器确实能省好多资源，大规模部署的时候成本能降不少。

> **币安50高返林川Visa卡领取 @JonKnipetlmb**
> 
> 这玩意儿确实轻量 以后跑自动化省心多了

> **misaka @misaka5783**
> 
> 還有個lexmount/moli 也可以關注一下, 一樣是 rust 寫的

> **DeDi @alkaidy2025**
> 
> 每个实例占 200MB 和占 30MB，规模放大后全是账单

> **A\_q\_u\_a\_0 @A\_q\_u\_a\_0**
> 
> 还不是很完善，比起 CDP 机制不太灵，二开费劲。

> **DaDa | 🕊️ @0x99DaDa**
> 
> 如果不依赖Chromium，很多浏览器的兼容性问题怎么办？  
> AI就不需要考虑浏览器兼容性问题吗？  
> 很多网站对于AI抓取操作其实挺排斥的，因为对广告收入是致命伤害。  
> 如果是特定浏览器，会不会反而会被屏蔽？

> **睡觉了 @fawnlily98**
> 
> 比她好看的没她骚比她骚的没她好看@luojan18 🧑‍🚀032

> **五月花 @lunaalmond55**
> 
> 比她好看的没她骚比她骚的没她好看@luojan18 🫡798

> **TawnyaP @tawnyatrib**
> 
> 比她好看的没她骚比她骚的没她好看@pailolu 🥸3⁮👨‍🍼

> **Merari Jafet Acero @Merari\_Jafet**
> 
> 比她好看的没她骚比她骚的没她好看@ismodemy 🙎‍6⁮🤯

> **walter @walt\_fromm**
> 
> 比她好看的没她骚比她骚的没她好看@Jilioua 🤒9⁮‍♀️

> **Robert @RobertRebbaker**
> 
> 比她好看的没她骚比她骚的没她好看@Bumija 💁6⁮😉

> **Porsha Dumais @PorshaDumacx1p**
> 
> 🤡好看的没我骚🤔比我骚的没我好看😯

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/8bb2a050_1788398659946?u=https%3A%2F%2Fx.com%2FMaxForAI%2Fstatus%2F2095168688643293458)