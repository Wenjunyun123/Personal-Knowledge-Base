---
author: GeekTechs
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/AhjEXKym4J
saved: 2026-11-19 23:36:23
tags:
  - 笔记同步助手
id: 63e5327f-bbeb-49a2-9702-7649a8108452
---

**作者：**GeekTechs

## 核心结论

清华大学与微软团队提出 DeepSeek Harness，通过缓存 Agent Loop 中已经确定的执行步骤，避免在每次工具反馈后重复进行下一步规划。该方法跳过了冗余推理，在将 Token 消耗降低 **87.93%** 的同时，使任务成功率提升了 **14%**。

## 问题背景：工具反馈触发重复规划

在传统 Agent Loop 中，每轮工具调用返回反馈后，系统都可能重新判断下一步行动，即使后续步骤实际上已经明确。这种重复规划会增加 Token 消耗，并带来不必要的推理开销。

## DeepSeek Harness 的优化思路

-   缓存已经确定的后续执行步骤。
-   当工具反馈与既定流程一致时，直接沿用缓存结果。
-   跳过重复推理，减少额外的模型调用与上下文消耗。

## 效果

-   **Token 消耗：**降低 87.93%。
-   **任务成功率：**提升 14%。
-   **整体收益：**在显著压缩调用成本的同时，Agent 的任务执行表现反而得到提升。

## 关键启示

对于流程相对稳定、下一步行动已经明确的 Agent 任务，不必在每次工具反馈后都重新规划。通过 Harness 复用既定决策，可以让模型将计算资源集中在真正需要重新判断的节点上，从而同时改善成本与性能。

![[笔记同步助手/images/e6f2f317f72cf4249c0e0b89fd9e3b0a_MD5.jpg|DeepSeek Harness 缓存已确定执行步骤并跳过重复推理的原理示意图]]

DeepSeek Harness 缓存已确定执行步骤并跳过重复推理的原理示意图

## 全文整理

DeepSeek Harness 竟然可以被清华、微软团队直接“瘦身”：Token 消耗削减87.93%，成功率却反而提升了14%。

此前，Agent 在每次获得工具反馈后，都要重新询问一遍 LLM，哪怕下一步操作早已确定。现在，清华、微软团队利用 Harness，将这些已经确定的步骤缓存下来，从而跳过重复推理。这一改动直接降低了成本，同时提升了性能。

视频时长 19秒 · 计费 2 积分 · 积分余额 1222

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/7c381b30-a747-449f-82fb-6ae5259b6878?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FAhjEXKym4J&s=vtoa)