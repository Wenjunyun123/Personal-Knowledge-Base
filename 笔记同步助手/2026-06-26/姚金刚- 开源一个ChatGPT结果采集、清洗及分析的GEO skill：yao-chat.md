---
author: 姚金刚
source: X
url: https://x.com/yaojingang/status/2070093155698090028?s=20
saved: 2026-06-26 14:05:32
tags:
  - 笔记同步助手
id: 23ecc8c0-8402-42c0-ba48-25bdc5d64155
---

🔗 [在 X 查看原文](https://x.com/yaojingang/status/2070093155698090028)

开源一个ChatGPT结果采集、清洗及分析的GEO skill：yao-chatgpt-crawler  
以“豆包”为实体，进行了真实测试，豆包在ChatGPT的GEO诊断报告，详见文末链接  
  
运行流程与逻辑：  
1、先准备问题列表、重复次数、目标实体、实体类型、OpenCLI profile、采样间隔  
2、OpenCLI Browser Bridge 连接已登录的 ChatGPT Web profile，对一组问题，随机间隔策略做多次独立采  
3、最后完成数据清洗，汇总结果，生成 JSON、Markdown、Excel 和 HTML 报告  
4、生成的HTML数据分析报告，会看多个指标，包括：目标实体的提及率、平均提及次数、Top 1 / Top 3 / Top 5 概率、平均排名、情绪倾向、引用来源、域名结构、标题意图，以及目标实体和同类型竞品之间的差距  
5、关于实体判断：会区分人、公司、产品、概念词和噪声词，避免把“行业词”“泛品类词”“URL 参数”混进竞品表  
  
整体的原则是，基于真实 ChatGPT Web 多次结果模拟，而不是 API 模拟  
这对GEO分析会更有价值  
  
欢迎体验  
  
1、skill GitHub地址： [github.com/yaojingang/yao-geo-skills/…](https://github.com/yaojingang/yao-geo-skills/tree/main/skills/yao-chatgpt-crawler)  
2、示例报告相关文件地址： [github.com/yaojingang/yao-geo-skills/…](https://github.com/yaojingang/yao-geo-skills/tree/main/skills/yao-chatgpt-crawler/examples/doubao-model-products-real)  
3、HTML报告快速浏览地址： [doc.laoyao.cn/cxvinr](https://doc.laoyao.cn/cxvinr)

![[笔记同步助手/images/34cac65fa2b8205b21e9e36f5fe168a4_MD5.jpg]]

![[笔记同步助手/images/f8089177f6b58f485949eabcb575af73_MD5.jpg]]

![[笔记同步助手/images/75be66614f8cbe87b5f94b7f88683cac_MD5.jpg]]

![[笔记同步助手/images/b86d63d98542edaedb38abb602b9605d_MD5.jpg]]

---

## 💬 评论（4）

> **樱桃🍑找炮友🍑点主页🍑 @WMacadam97131**
> 
> 😵‍

> **热币.93 | 叶舟在线 📈 @nekoyuurii**
> 
> 开源实测思路确实清奇又硬核

> **薄荷🍑找炮友🍑点主页🍑 @quintina43124**
> 
> 🤐

> **AIlinccc @Linc\_AI**
> 
> 为了不浪费的我pro，也为了不让我女儿被垃圾教材毒害  
>   
> 我的第一款产品快上线了  
>   
> 起因是老婆在网上找了一些软件，真他妈敢收钱啊  
>   
> 5980/年，是干嘛的呢？就是一个听一句话选个图片的功能，教材质量差、图片全是真实的图片，甚至我猜测为了规避版权问题截的非常不完整  
>   
> 要不然就是有的产品，又是商场又是积分榜，不是内容太满，就是流程太绕，明明只希望孩子通过这个程序可以“听懂一句话”，最后变成点来点去看说明，找入口，还没进入状态，就没注意力了  
>   
> 所以，忍无可忍，决定自己做一款产品，就针对小朋友的英语启蒙。我的功能非常简单，把一切影响孩子注意力的非必要按钮全部删除，只需要根据听到的英语短句选择一张图片，自动跳到下一张、下一关  
>   
> 每关15个短句30个插画，全部都是根据我的提示词AI生成，教材是让ChatGPT蒸馏了Reading Eggs、Raz Kids、Oxford Discover、Oxford Phonics World、Starfall、Cambridge Young Learners这些，并且根据非母语孩子的学习路径进行了微调  
>   
> 我真牛逼！！！
> 
> ![[笔记同步助手/images/96a6a7b19c48c64d3e08e744c0189219_MD5.jpg]]
> 
> ![[笔记同步助手/images/7025aa2cec3152c14c805b1d492662c2_MD5.jpg]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/043e41a7_1782453931246?u=https%3A%2F%2Fx.com%2Fyaojingang%2Fstatus%2F2070093155698090028)