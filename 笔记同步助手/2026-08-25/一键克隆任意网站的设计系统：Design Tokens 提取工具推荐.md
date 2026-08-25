---
author: 哈工大AI工程师Peter
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/ApqAmgflrt
saved: 2026-08-25 15:30:43
tags:
  - 笔记同步助手
id: 23bf31f1-89ba-4e9a-8d2a-37234b6fcf05
---

作者：哈工大AI工程师Peter

## 问题背景

看到一个设计特别好的网站，想提取其中的设计细节作为参考，甚至想将整个网站克隆下来，应该怎么做？本文推荐一款工具，专门用于解决这一问题。

## 工具核心功能

该工具可以从任意 URL（即任意网站的链接）中，秒级提取整个网站的设计系统，并输出一个 `design.md` 文件。文件中包含以下内容：

![[笔记同步助手/images/9385f29c4f2f8b94510e82aba9ebfc5f_MD5.jpg|工具介绍与使用场景说明]]

工具介绍与使用场景说明

-   颜色（color tokens）
-   字体（typography）
-   组件（components）
-   间距（spacing）

本质上，它的作用是将任何一个网站转化为 **design tokens**（设计变量）。

## 使用方式

将生成的 `design.md` 文件投喂给各类设计 Agent，即可一键复刻网站设计，并在此基础上进行修改和提升。可兼容的设计 Agent 包括：

![[笔记同步助手/images/3d3c81d05f2d0f9cdd306aa99e5c23e2_MD5.jpg|design.md 输出文件与 design tokens 概念解释]]

design.md 输出文件与 design tokens 概念解释

-   Claude Design
-   OpenDesign
-   其他类似的设计类 AI 工具

## 安装与工作流

该工具只需安装一次，即可通过其内置的命令与解决方案，告知 Agent 如何完成网站的克隆与拷贝。整个流程实现"无缝链接"，帮助用户自动化完成设计复刻工作。

## 开源信息

![[笔记同步助手/images/e7074874884ec99ae4f1f4f694860516_MD5.jpg|项目总结与 GitHub 开源信息]]

项目总结与 GitHub 开源信息

该项目已在 GitHub 上开源，感兴趣的同学可以直接前往仓库查看详情。

## 总结

这是一款把"复制网站设计"这件事做到极简的工具：输入 URL → 提取 design tokens → 喂给 AI 设计 Agent → 完成复刻与改版。未来遇到需要参考或克隆优秀网站设计的场景，直接使用它即可。

## 全文整理

有人问我这样一个问题：看到一个设计特别优秀的网站，整体感觉很出色，想提取其中的一些设计细节作为参考，或者想把整个网站完整克隆下来，应该怎么办？

今天推荐的工具正是为这件事而生。它可以从任意 URL——也就是任何网站的链接——中，把网站的设计系统提取出来，生成一份 design.md 文件。这份文件里包含了颜色、字体、组件、间距等所有设计要素。拿到这个文件之后，你可以把它投喂给 Claude Design、OpenDesign、Antdesign、Trae Design 等设计 Agent，让它们一键完成复刻，甚至在复刻的基础上进行修改和优化。这个流程相当专业：秒级提取设计方案，工具之间无缝衔接，把"设计"这件事彻底打通。

具体功能我就不逐一展开了。简单来说，它安装一次之后，就可以告诉你的 Agent 如何去克隆和 copy 一个网站，并且配备了一套相当完整的命令与解决方案。把网站克隆这件事交给它就行了，未来有类似的需求直接上手用。

我也去它的 GitHub 主页看了一下。这个项目的核心价值在于：它可以把任意网站（any website）转换为 design tokens，也就是设计变量。

视频时长 1分2秒 · 消耗 6 积分 · 积分余额 1515

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/11681763-34cf-4c8b-b0b1-05b5b6535753?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FApqAmgflrt&s=vtoa)