---
author: 大力Thinking
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/A8hptjuL48
saved: 2026-11-22 13:45:58
tags:
  - 笔记同步助手
id: 970a7e43-0138-4f4b-abd7-8e28e6b5960f
---

**作者：**大力Thinking

本文介绍如何在 Herdr 桌面端中使用 `hc` 创建子 Agent：让 Codex 作为主 Agent，在右侧窗格启动 Pi，并向 Pi 发出问候，最后将 Pi 的回复交回 Codex。

## 为什么需要子 Agent

如果在 Codex 中直接要求“创建子 Agent”，调用的是 Codex 自带的子 Agent 机制。通过 Herdr，则可以从统一入口管理不同类型的 Agent，例如 Codex、Claude Code、Pi，以及用于特定任务的 DeepSeek Agent。

不同 Agent 可以承担不同角色，并依据各自的能力与擅长领域协同完成工作。

## 创建 Pi 子 Agent 的步骤

1.  打开 Codex，使其作为当前的主 Agent。
    
2.  向 Codex 说明：需要在当前 Agent 的右侧创建新窗格。
    
3.  要求 Codex 使用 `hc` 创建并启动 Pi Agent，将其作为自己的子 Agent。
    
4.  让 Codex 向 Pi 发出“你好”的问候。
    
5.  将 Pi 的回复内容传回主 Agent。
    

### 可直接使用的指令

> 请将当前 Agent 作为主 Agent，然后在这个 Agent 右边创建一个新的窗格，用 `hc` 创建并启动 Pi Agent，作为这个 Agent 的子 Agent；向它发出一个“你好”的问候，最后把这个 Pi Agent 的问候返回内容传给主 Agent。

![[笔记同步助手/images/673a21dfc6c205a6ba30664e8f686ed8_MD5.jpg|Codex 接收创建 Pi 子 Agent 指令并通过 hc 启动 Pi 的界面]]

Codex 接收创建 Pi 子 Agent 指令并通过 hc 启动 Pi 的界面

## 子 Agent 的定义与配置

不同 Agent 的工作方式通常需要在 Agent 配置中预先定义，包括 Agent 的身份、职责，以及它能够调用哪些工具。配置完成后，Codex 可以在 Herdr 的右侧窗格中通过 `hc` 启动 Pi，并将执行结果返回主 Agent。

![[笔记同步助手/images/301d7793c62ab96c3e80be1b97cfc6fb_MD5.jpg|右侧窗格中显示由 hc 启动的 Pi 子 Agent 及其回复]]

右侧窗格中显示由 hc 启动的 Pi 子 Agent 及其回复

## 查看 Agent 的父子关系

执行完成后，可以在 Herdr 左侧通过柱状结构查看主 Agent 与子 Agent 之间的父子关系。示例中，Codex 是主 Agent，Pi 是由其通过 `hc` 创建的子 Agent。

![[笔记同步助手/images/c256df91c63df7fb34630bb2f72cc881_MD5.jpg|Herdr 左侧以柱状结构展示 Codex 主 Agent 与 Pi 子 Agent 的父子关系]]

Herdr 左侧以柱状结构展示 Codex 主 Agent 与 Pi 子 Agent 的父子关系

## 统一管理多种 Agent

子 Agent 不仅限于 Pi。使用 Claude Code 时，同样可以在 Herdr 中创建子 Agent。借助 Herdr 的统一管理能力，可以在同一工作区运行 Codex、Claude Code、Pi 等不同 Agent，并让它们分别承担不同角色、利用各自优势协同处理任务。

-   **Codex：**作为主 Agent，发起任务并接收子 Agent 的结果。
-   **Pi：**通过 `hc` 在右侧窗格中作为子 Agent 启动。
-   **Claude Code：**也可在 Herdr 中创建和管理子 Agent。
-   **Herdr：**提供统一的 Agent 运行、调度与父子关系展示入口。

## 全文整理

前一段时间，我跟大家分享过自己已经切换到了 Herdr 桌面端。这两天使用下来，总体感觉还是不错。今天给大家介绍一下，如何在 Herdr 桌面端创建子 Agent。

首先，打开 Codex。如果在 Codex 中直接说“创建子 Agent”，实际创建的会是 Codex 自带的子 Agent。我们更希望实现的，是通过派发 Agent 来管理 DeepSeek、管理 Pi Agent，让多个不同品牌的 Agent 协同工作。

需要派发子 Agent 时，可以这样告诉 Codex：

“请将当前 Agent 作为主 Agent，然后在这个 Agent 的右边创建一个新的窗格，用 HC 进行创建并启动 Pi Agent，将其作为当前 Agent 的子 Agent，向它发出‘你好’的问候，最后把 Pi Agent 返回的问候内容传给主 Agent。”

这个说法有些绕。一般情况下，派发子 Agent 的工作可以在 `agents.md` 中完成，在那里定义好不同的 Agent，包括每个 Agent 可以调用哪些工具。

现在可以看到，Codex 已经通过 Herdr 的 HC 调用了 Pi Agent，创建了这样的子 Agent，并把子 Agent 返回的内容传回 Codex，作为主 Agent 的回复。

在左侧还可以看到，Agent 之间的父子关系可以通过树形结构查看。也就是说，即使只使用 Claude Code，也可以创建子 Agent；但现在有了 Herdr，相当于多了一个“大管家”，可以在这里运行 Codex、运行 Claude Code、运行 Pi，再让每一个不同的 Agent 充当不同角色，根据各自的特性和擅长领域，完成各自更擅长的事情。

今天就分享到这里，我们下次见。

视频时长 1分51秒 · 计费 10 积分 · 积分余额 1163

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/3c894cd7-fec5-4a47-87b6-d2da32f37065?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FA8hptjuL48&s=vtoa)