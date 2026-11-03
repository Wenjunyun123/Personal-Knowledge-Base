---
author: GeekTechs
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/A5SQpi32kA
saved: 2026-11-03 16:44:54
tags:
  - 笔记同步助手
id: d37b79ae-947d-4714-ac76-9f5ce03a4a2c
---

**作者：**GeekTechs

## 传统 Browser Use 的局限

传统 Browser Use 通常通过截图识别页面元素，再模拟鼠标点击完成操作。这种方式速度较慢、Token 消耗较高，而且容易受到页面变化、识别误差等因素影响。

## WebMCP 的新思路

Chrome 推出的 WebMCP 让网站主动注册工具，并明确声明工具能够执行什么任务、需要哪些参数。AI 随后可以直接调用网页提供的 JavaScript 功能，无需再像人类一样逐步寻找按钮和模拟操作。

## 浏览器自动化的关键变化

WebMCP 将浏览器自动化的核心，从“让 AI 学会如何点击”转变为“让网页提供可直接调用的功能”。这种方式有望减少不必要的视觉识别与交互步骤，降低 Token 开销，同时提升自动化操作的稳定性和效率。

![[笔记同步助手/images/f8e9d5a64a5d35fc94a3fbe2f9208fa9_MD5.jpg|WebMCP 工具注册与网页功能调用流程示意]]

WebMCP 工具注册与网页功能调用流程示意

## 核心要点

-   传统方案依赖截图、元素识别与模拟点击。
-   WebMCP 允许网站主动注册自动化工具。
-   工具会声明自身能力及所需参数。
-   AI 可以直接调用网页提供的 JavaScript 功能。
-   浏览器自动化可能由逐步模拟操作转向结构化工具调用。

## 全文整理

传统 Browser Use 可能要凉了，Chrome 直接掀桌子。

Chrome 推出了 WebMCP，浏览器自动化可能迎来一场重大变革。

过去，AI 通常需要通过截图识别按钮、模拟点击来操作网页。这种方式不仅速度慢、成本高，而且容易出错。

现在，网站可以主动注册工具，声明自身能够完成哪些操作、需要哪些参数。AI 随后便可直接调用网页提供的 JavaScript 功能，不再需要像人类一样逐步模拟操作。

我们此前投入了大量 Token，教 AI 学会点击鼠标；而 Chrome 的思路是：为什么不直接调用函数？

这个思路太强了。

视频时长 29秒 · 消耗 3 积分 · 积分余额 1245

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c3699158-beac-4770-8b29-9a7772cd9589?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FA5SQpi32kA&s=vtoa)