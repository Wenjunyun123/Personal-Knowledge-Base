---
author: Codex
source: GitHub 仓库分析
url: https://github.com/zarazhangrui/youtube-to-ebook
saved: 2026-08-02 17:53:58
tags:
  - 笔记同步助手
id: 08c1f853-e2ee-4b11-8a8d-9c661777d8ed
---

项目名称：youtube-to-ebook

项目作者：Zara Zhang

分析日期：2026-08-02

Star 快照：524

## 一句话理解

youtube-to-ebook 是一条自动内容流水线：抓取关注频道的新视频，过滤 Shorts，获取 transcript，让 Claude 写成文章，打包成 EPUB，再通过邮件发送给用户。

## 它具体解决什么问题

YouTube 适合观看，但不方便进行文字检索、离线阅读和长期归档。关注频道较多时，用户还要逐个检查更新，判断哪些内容值得看。

这个项目把视频订阅转成定期电子书，让用户可以在 Kindle、手机或阅读器中集中阅读，而不是一直停留在视频平台的信息流里。

## 实际使用时会看到什么

流水线拉取频道最新视频，排除 Shorts 和已处理条目，获取字幕后生成文章。多篇文章会被打包成一份 EPUB，通过邮件发送。

Streamlit Dashboard 可以管理频道、手动生成与发送、查看处理指标、修改写作风格提示词、浏览归档并设置计划任务。

仓库相关演示资产中保存了一封真实历史邮件：标题为 “YOUR YOUTUBE DIGEST”，邮件包含 EPUB 附件。

## 核心实现

- `main.py` 串联抓取、过滤、转写、写作、发送和状态更新。
- Tracker 记录已处理视频，避免重复生成。
- Claude 负责把 transcript 改写成文章。
- EPUB 生成器汇总文章与目录。
- `dashboard.py` 提供 Streamlit 管理界面。
- launchd 配置支持 macOS 定时运行。

一个重要实现细节是：只有发送成功后，视频才会被标记为已处理，避免生成或邮件失败时永久漏掉内容。

## 适合谁

- 关注大量 YouTube 知识频道，却更喜欢阅读的人。
- 希望把视频内容沉淀为可检索个人资料库的人。
- 想研究多步骤内容 Agent、失败恢复和定时自动化的开发者。

## 验证情况与边界

本次检查了主流水线、Dashboard 和历史邮件效果图，但没有调用 YouTube、Claude 或邮件服务，也没有实际发送 EPUB。历史邮件图是仓库作者保存的成品证据，不是本次运行生成。

## 项目地址

GitHub：https://github.com/zarazhangrui/youtube-to-ebook

