---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/personalized-podcast
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: 8ccfdd77-8194-41bd-87da-d25020a3ea34
---

项目名称：personalized-podcast

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：409

## 一句话理解

personalized-podcast 是一个个人播客生成 Skill：Coding Agent 先把用户选定的资料写成双主持人脚本，再用 Fish Audio 为两个角色合成声音，拼成 MP3，并可发布为 GitHub Pages RSS。

## 它具体解决什么问题

文章和资料适合深度阅读，但通勤、散步和做家务时更适合听。普通 TTS 只是把一段文章从头念到尾，缺少对话节奏，也很难长期订阅。

这个项目把“资料理解、脚本改写、双角色 TTS、音频拼接和 RSS 发布”连成一条流水线，最终产物可以进入常见播客客户端。

## 实际使用时会看到什么

用户给出主题和资料后，Agent 会写出两位主持人的对话脚本。Fish Audio 分别生成每个角色的语音，pydub 和 ffmpeg 按顺序拼接成完整节目。

MP3 默认保存在本地。用户如果希望长期订阅，可以选择把封面、episode 数据、音频和 feed 发布到 GitHub Pages。

## 核心实现

- `speak.py` 按角色调用 TTS 并生成音频片段。
- pydub 与 ffmpeg 负责拼接、静音和格式处理。
- `publish.py` 更新 episode 数据和 RSS。
- `bootstrap.py` 负责首次配置。
- `utils.py` 封装共用路径和文件处理逻辑。

## 适合谁

- 想把个人阅读材料转换为通勤播客的人。
- 希望拥有私人、可订阅音频 feed 的用户。
- 想研究从大模型脚本到 TTS 与 RSS 发布完整链路的开发者。

## 验证情况与边界

本次检查了 Python 生成、拼接和发布脚本，但没有使用 Fish Audio API，也没有消耗外部额度生成新音频。仓库要求系统安装 ffmpeg。真实发布成品可以在作者的 `podcast-feed` 仓库中看到，但两个仓库的职责需要区分：本仓库负责生成流程，`podcast-feed` 负责静态发布结果。

## 项目地址

GitHub：https://github.com/zarazhangrui/personalized-podcast

