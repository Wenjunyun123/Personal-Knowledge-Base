---
author: lifcc
source: AI整理 - X (Twitter)
url: https://x.com/mylifcc/status/2090998309662171573
saved: 2026-08-23 00:36:45
tags:
  - 笔记同步助手
id: f05f70d4-6a79-4b21-8af0-ff8abb4f8e09
---

# Anthropic 员工 Thariq放出了他们内部非常爱用的一个skill，叫ELI5

## 豆包输入法：到底有哪些零件、数据会不会离开电脑？

### 一句话原理

系统接住输入 → 本地先猜 → 云端可帮忙 → 把结果写回 App。

### 三条小路（三种输入模式）

-   **基础打字**：键盘输入文字，命中本地规则就直接出。
-   **智能打字**：本地搞不定时，会把内容送往云端，借助更大候选和热词帮忙排序、联想。
-   **语音输入**：按住 fn 说话，本地有离线包就本地识别，没有就走云端流式语音识别，最后再做断句、标点与修正。

### 安装包里同时存在 offline 与 online ASR 两套实现

也就是说，豆包输入法其实是"两个脑袋"：

-   **本地脑袋**：负责拼音切分与纠错、离线语音识别。
-   **云端脑袋**：负责更大的候选与热词、云端语音识别。

原则是：简单的活儿交给本地，难题可以请云端帮忙。

### 本地都有什么？

-   系统词库 + 个人词库
-   候选排序与联想
-   离线语音模型
-   加密的本地数据库

### 什么会离开电脑？答案取决于你打开的模式

#### 基础键盘

-   官方称输入内容不上传。

#### 离线语音

-   声音在本地识别。

#### 智能键盘

-   输入串、部分文本与场景会实时送云端。

#### 云端语音

-   声音及必要上下文会送云端转写。

#### 上下文智能联想 / 账号与词库同步 / 更新、日志与统计

-   会涉及联网行为。

> **隐私开关提示**：可在「设置 → 输入模式与隐私保护」关闭云端智能输入；体验改进计划另有独立开关。

### 给大人看的静态证据

> 注：以下基于 macOS V0.9.6 官网当前提供的安装包做只读静态分析，未安装、未登录、未抓包、未绕过保护。
> 
> 安装包已通过 Apple Developer ID 签名 + 公证。 SHA-256：`7c699873be9d216925185b4976199cef898998e7b7838681d09604a50f65c6bb`

#### 主要二进制与符号线索

-   **OimeEngine + ONNX Runtime**：说明本地有词典、排序和机器学习推理能力。
-   **AVFoundation + ASR 资源**：说明它能录音，也带了离线语音模型资源。
-   **ime\_net\_sdk + TTNet**：说明它会访问输入法与语音服务。
-   **WCDB + SQLCipher**：说明个人状态 / 词库可保存在加密数据库中。
-   **Local / Cloud / LLM 候选合并**：二进制符号显示多路候选会被排序、刷新与合并。

#### Info.plist 与链接符号

`Info.plist` 声明了 `DoubaoImeInputController`、拼音输入源、后台输入法进程和麦克风用途；主程序链接了：

`InputMethodKit` · `AVFoundation` · `OimeEngine` · `libonnxruntime` · `libime_net_sdk` · `WCDBSwift` · `sqlcipher`

可见符号还包括：

`WaveKeyboardCandidateService` · `KeyboardGlobalContextServices` · `MakeCloudRequest` · `MakeLLMRequest` · `MergeCloudLLM` · `AsrOffWorker` · `AsrOnWorker` 以及个人词库同步路径。

### 我还不能断言什么

静态拆包只能证明"里面有哪些零件"，**不能**证明：

1.  某次实际输入具体发送了哪些字段；
2.  服务端模型具体多大；
3.  每个隐私开关的默认值是什么；
4.  官方政策承诺在网络上是否每一次都得到遵守。

要回答这些问题，需要在隔离的测试账号和无敏感文本环境中，做动态抓包与行为实验。

![[笔记同步助手/images/4506fd41ffa16b9c6ba83af6668c3b80_MD5.jpg|Image]]![[笔记同步助手/images/302c379340cd92ee87de81c899f62df5_MD5.jpg|Image]]![[笔记同步助手/images/f8dec8268a80d80605d1640b5d981a5e_MD5.jpg|Image]]![[笔记同步助手/images/ef3e4a1c76120ea175640d1f8cd71503_MD5.jpg|Image]]![[笔记同步助手/images/9f59821269f01c13056681fdb9952eff_MD5.jpg|Image]]

识别 1,440 字 · 本次未扣积分 · 积分余额 1542

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/e9123523-3744-4e06-a354-fd5ab054cad6?u=https%3A%2F%2Fx.com%2Fmylifcc%2Fstatus%2F2090998309662171573&s=vtoa)