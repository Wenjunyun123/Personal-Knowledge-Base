---
author: GeekTechs
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/ADADridQjM
saved: 2026-11-02 20:15:51
tags:
  - 笔记同步助手
id: 7d55b653-5f78-45d9-9bad-d9ef3adc9b01
---

**作者：**GeekTechs

Karpathy 不满 YouTube 的推荐系统，认为其中充斥着低质量内容，于是利用周末时间，在约两小时内搭建了一个名为 **HackerTube** 的视频发现网站。

## 项目目标

HackerTube 不依赖 YouTube 的个性化推荐数据，也不要求用户登录账号。其内容来自 Hacker News 社区评论：系统从评论中提取网友推荐过的 YouTube 视频，再按主题进行整理，从而提供更符合技术社区偏好的视频导航。

## 内容筛选流程

-   使用 **Claude Code** 执行主要工作，推理模型采用 **Opus 4.5**，强度设置为 **medium**。
-   遍历 Hacker News 的评论，筛出约 **4 万条**推荐信息。
-   从这些推荐中整理出 **6,454 个视频**。
-   最终覆盖约 **150 个主题**。

## Karpathy 的工作方式

整个开发流程几乎完全交给 Claude Code。Karpathy 表示，自己已经不再从事传统意义上的工程工作，而是主要通过与 Claude 对话来定义目标、安排步骤并让智能体完成具体任务。

![[笔记同步助手/images/9f2acfcafa0768e5bf5a904bebcab4a2_MD5.jpg|HackerTube 项目及视频主题分类页面]]

HackerTube 项目及视频主题分类页面

## 项目所需的基础准备

完成这个项目主要需要三项准备工作：申请 YouTube 数据接口密钥、开通服务器，以及购买域名。

## 核心启示

这个案例展示了智能体编程工具在快速原型开发中的价值：开发者可以把数据采集、筛选、分类和网站搭建等任务交给 AI 主导完成，将自身角色从逐行编写代码转向描述需求、验证结果和迭代方向。

## 全文整理

厌倦了 YouTube 的推荐系统，也嫌 YouTube 上尽是垃圾视频，Karpathy 周末花了两小时，用 Claude Code 重做了一个 YouTube。

这个项目叫 HackerTube，使用 Claude Opus 4.5、Medium 强度模式开发。页面里只有 Hacker News 网友推荐过的 YouTube 视频。整个流程几乎都交给了 Claude Code：它从 Hacker News 的全部评论中筛出四万条推荐，最终得到 6454 个视频，覆盖 150 个主题。

HackerTube 不使用账号个性化推荐，相关数据还可以导出给 Agent 使用。再造一个这样的网站，耗时约两小时。

Karpathy 只做了三件事：申请 YouTube 数据接口密钥、开通服务器，以及购买域名。其余工作基本都由 Claude Code 完成。他直言，自己其实已经不再做任何传统意义上的工程工作，只跟 Claude 对话，由它完成筛出四万条推荐等全部任务。

视频时长 35秒 · 消耗 3 积分 · 积分余额 1248

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/7271f044-5f5e-46be-8330-0051e81f9db5?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FADADridQjM&s=vtoa)