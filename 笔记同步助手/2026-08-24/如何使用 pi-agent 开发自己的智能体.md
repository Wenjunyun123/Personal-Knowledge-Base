---
author: 费曼学徒冬瓜
source: AI整理 - 抖音
url: https://v.douyin.com/ZGsHZ9pgWTM/
saved: 2026-08-24 20:15:40
tags:
  - 笔记同步助手
id: a2f3da1f-0386-42bc-9423-201c60ae6251
---

**作者：**费曼学徒冬瓜

## 背景

pi-agent 之所以值得选用，是因为它先是一个顶尖的 coding-agent，同时也是一个开发框架——二次开发等于直接复用其成熟内核。视频作者此前曾把 pi-agent 的源码写成一本开源电子书，意外收获了两千多个 Star，于是趁热打铁推出了本期内容：介绍如何使用 pi-agent 打造自己的智能体。

## 配套 Skill：一句话提需求，AI 完成开发

作者准备了一个 Skill，使用者只需描述功能需求，AI 会自行调用 pi-agent 完成整个开发流程。

演示项目为 **DataAgent**：一个基于 Web 的应用，由 AI 自己构造而成。在搭建过程中，需要拦截危险的工具调用（dangerous tool calls），以保证运行安全。

整个流程大致为：

-   根据 Skill 查询 pi-agent 的用法；
-   自动开始搭建环境；
-   快速完成项目搭建。

## 效果演示

项目搭建完毕后，可以直接体验：随便向 DataAgent 提一个问题，它会自行解析需求、调用合适的工具，并把构造好的答复返回给用户。

![[笔记同步助手/images/32b57de7ce71e512f07088a18cbc7399_MD5.jpg|Skill 触发后 AI 自动搭建 DataAgent 项目的过程]]

Skill 触发后 AI 自动搭建 DataAgent 项目的过程

![[笔记同步助手/images/abbce1b5709b9d8b379086f6b0044312_MD5.jpg|DataAgent 运行时根据用户提问自行调用工具并给出答复的效果]]

DataAgent 运行时根据用户提问自行调用工具并给出答复的效果

## 配套教程

除了 Skill，作者还准备了一份极简教程。教程以构建 DataAgent 为案例，进行由浅入深的实战拆解，采用「人机协作编程」的视角，讲解如何基于 pi-agent 进行二次开发。

![[笔记同步助手/images/10bf25d0088eaf3b133ab1afaf1d38b3_MD5.jpg|配套教程内容展示，从浅入深拆解 DataAgent 的构建思路]]

配套教程内容展示，从浅入深拆解 DataAgent 的构建思路

## 使用建议

-   **想无脑上手**：直接使用 Skill，让 AI 自行调用 pi-agent 完成开发；
-   **想了解原理**：阅读配套教程，逐步理解二次开发机制；
-   **遇到功能设计难题**：使用 Skill 让 AI 搜索同类项目，自行解读源码，并结合你的项目给出解决方案。

## 小结

这套组合（pi-agent + Skill + 教程）门槛较低，对新手友好：既可以「用 Skill 让 AI 干活」，也可以「读教程搞懂底层」，甚至可以把 Skill 当作方案参考工具使用。

## 全文整理

之前我把 pagent 的源码写成了一本书，没想到拿了两千个 star，于是我赶紧一鼓作气，继续介绍如何使用 pi-agent 打造自己的智能体。

这次我准备了一个 skill：你只管提功能需求，pi-agent 会自己调用框架完成开发。我们的需求是开发一个 DataAgent，基于 Web 进行应用，基于 AI 自己造就好。因此要拦截危险操作（circle）。此外，根据这个 skill 查询 pi-agent 的用法，就可以开始搭建环境，很快就完成了这个项目。

来，我们体验一下。随便问个问题，AI 立即给出答复。

我准备了一份极简教程。这份教程围绕构建 DataAgent 进行讲解，由浅入深，以人工搜索编程的视角，告诉你如何用 pi-agent 进行二次开发。所以，如果你想无脑上手，那就直接使用 skill；如果你想掌握原理，那就看看这个教程。

此外，如果有个功能你不知道怎么设计，也可以使用这个 skill，让 AI 搜索同类开源项目进行参考。AI 搜索到同类项目之后，会自行解读源码，结合你的项目，给你一个解决方案。因此，我觉得这个 skill 还是很适合新手的。

感谢观看。

视频时长 1分1秒 · 消耗 6 积分 · 积分余额 1531

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/abb0b415-8c37-4de1-953a-c80afb758db3?u=https%3A%2F%2Fv.douyin.com%2FZGsHZ9pgWTM%2F&s=vtoa)