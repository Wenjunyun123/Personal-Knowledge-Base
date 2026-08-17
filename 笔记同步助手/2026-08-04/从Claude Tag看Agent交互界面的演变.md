---
author: 张咋啦Zara
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/A1neo0ZhqV
saved: 2026-08-04 14:40:13
tags:
  - 笔记同步助手
id: eda4dc2b-d9d7-4691-917e-4ec052db1203
---

作者：张咋啦Zara

## 缘起：一期 Anthropic 播客

起因是看到 Anthropic 某位员工的一期播客，对方提到一个在国内被严重低估的产品——Claude Tag。它的核心能力是把 Claude 和 Claude Code 的 Agent 能力无缝集成到 Slack 里。

![[笔记同步助手/images/138507e120cd7ceac3c2b8a0dcfea9ac_MD5.jpg|播客中介绍 Claude Tag：把 Claude 与 Claude Code 的 Agent 能力嵌入 Slack]]

播客中介绍 Claude Tag：把 Claude 与 Claude Code 的 Agent 能力嵌入 Slack

## Claude Tag 究竟解决了什么问题

播客里披露了一组数据：Anthropic 内部目前 65% 的 Pull Request 都是通过 Claude Tag 提交的。这个比例足以说明 Claude Tag 已经深度融入到他们日常的工作流中。

![[笔记同步助手/images/22671f3430ddd5b7f153a70b6dde5c2d_MD5.jpg|关键数据展示：Anthropic 内部 65% 的 PR 都由 Claude Tag 提交]]

关键数据展示：Anthropic 内部 65% 的 PR 都由 Claude Tag 提交

更值得注意的是，许多员工因为有了 Claude Tag，甚至不再单独打开 Claude Code——很多工作的闭环可以直接在 Slack 内完成。

### 一个典型的接力流程：全部发生在一个 Thread 里

-   产品同学在 Thread 里向 Claude 提出需求
-   Claude 输出原型
-   @ 设计同学在原帖下给出反馈
-   设计确认后，@ 研发同学直接进入开发
-   整件事在同一个 Slack Thread 里完成

不需要再开多个 Claude Code session，也不需要在不同工具间来回切换。

![[笔记同步助手/images/1a02a95938cf699dd36f3f83027d3aa8_MD5.jpg|Slack Thread 内的接力示例：产品提需求 → Claude 出原型 → 设计反馈 → 研发开发]]

Slack Thread 内的接力示例：产品提需求 → Claude 出原型 → 设计反馈 → 研发开发

## 由此引发的思考：人跟 Agent 交互的界面正在发生什么变化

### 我自己的演变路径

一月份刚开始接触 Claude Code 时，是在 Terminal 里使用。作为文科生，我这辈子都没打开过 Terminal，甚至要先理解"Terminal 是什么"才能勉强上手——一开始相当别扭，但当时也只有 Terminal 这一个选项。

![[笔记同步助手/images/ffe4eb6c5605f2101c2a0b8df57af54a_MD5.jpg|第一阶段：在 Terminal 中使用 Claude Code 的界面]]

第一阶段：在 Terminal 中使用 Claude Code 的界面

三、四月份开始出现桌面版客户端，体验比 Terminal 友好得多。到五月份左右，我基本已经把工作迁到了 Claude Code 的桌面客户端，Terminal 也就很少再打开。

![[笔记同步助手/images/8e5d1f7ed7bcac3c9849db59739f4b08_MD5.jpg|第二阶段：迁移到 Claude Code 桌面客户端]]

第二阶段：迁移到 Claude Code 桌面客户端

到了六、七月，飞书等 IM 工具陆续上线与 Claude Code 的集成。我把 Claude Code 接入到飞书后，桌面客户端打开的频率进一步降低——越来越多工作可以直接在飞书里完成。

![[笔记同步助手/images/45c6956b4fa67ae3d69e3fd0dda81f2a_MD5.jpg|第三阶段：Claude Code 集成进飞书后的工作界面]]

第三阶段：Claude Code 集成进飞书后的工作界面

我自己走过的路恰好是：**Terminal → 桌面客户端 → 飞书**。每往前走一步，都离我本来就熟悉的工作界面更近一些。我本来就不该先去学 Terminal——它对我而言并不 make sense。我最熟悉的界面就是飞书，找 Agent 的方式应该像"找人"一样自然。

### 更底层的判断：Coding Agents ＝ General Agents

这个认知在硅谷一、二月份基本已经形成——Coding Agents are General Agents。一切知识工作，理论上都可以借助 Coding Agent 完成并提效。

![[笔记同步助手/images/efb30bb9bc5bfe2df449f2eb814f87d5_MD5.jpg|核心观点：Coding Agents = General Agents，未来主要用户将是非程序员]]

核心观点：Coding Agents = General Agents，未来主要用户将是非程序员

顺着这个判断继续推：如果 Coding Agent ＝ General Agent，那未来 Coding Agent 的主要用户将是**非程序员**，非程序员的使用规模会远远超过程序员。

如果绝大部分用户不是程序员，他肯定不会去学 Terminal，也不会愿意单独下一款新的 App。他本来在哪工作就应该在哪工作——**Agent 应该主动去找人，而不是让人去找 Agent**。

## 小结

让 Agent 融入我们本已熟悉的工作流和界面，而不是让我们再学一个新产品、下一款新 App——这才是更自然的交互方向，也是 Claude Tag 给我们的最大启发。

## 全文整理

我昨天看了 Anthropic 公司一位员工参与的播客，他在节目中向听众介绍了 Claude Tag 这款产品。我觉得 Claude Tag 在国内被严重低估，可以借此机会跟不了解它的人简单介绍一下：它把 Claude 以及 Claude Code 的 Agent 能力无缝集成进了 Slack 之中。这位员工还分享说，Anthropic 现在内部所有产品相关的 Pull Request 中，有 65% 已经是由 Claude Tag 提交的。也就是说，Claude 已经非常深入地融入到了他们的日常工作流里，甚至很多员工因为有了 Claude，就不用再单独打开 Claude Code 了。我推测 Anthropic 沿着这个方向继续演进下去，员工甚至可以完全不用自己打开 Claude Code，直接在 Slack 里就能完成很多工作的闭环。

他还分享了一个细节：因为这种集成，他们在群聊里出现了大量的工作接力。比如一个产品经理可以在一个 Thread 里直接向 Claude 提出需求；Claude 做出原型之后，可以直接在消息里 @ 设计同学，让设计同学在下方针对原型给出反馈；设计确认完成后，再 @ 研发同学去开发。整个这件事就在一个 Slack 的 Thread 里完成了，不需要去开很多个 Claude Code 的 Session。我认为这代表了未来的趋势。

这件事促使我思考：我们跟 Agent 交互的界面，正在发生什么样的变化。

我想起今年一月份刚开始使用 Claude Code 的时候，是在 Terminal 里用的。那个时候我作为一个文科生，这辈子都没有打开过 Terminal，还要先去弄明白 Terminal 到底是什么，一开始非常不习惯，因为当时只有命令行这一种使用方式。

后来大概三四月份，Claude Code 开始有了客户端，也就是桌面版的 App；同一时期 Codex 的客户端也做得非常出色。所以我可能四五月份就已经把大部分工作迁移到了 Codex 的客户端，Terminal 就很少再打开了。客户端的体验要友好得多。

再往后到了六七月份，有了飞书 CLI 这类集成方案，我把 Codex 集成进了飞书，客户端打开的次数也随之减少。越来越多的工作可以直接在飞书里完成。

所以我自己的整个使用演变路径，就是从 Terminal 到客户端，再到飞书。我认为这是逐步走向我们本就熟悉的工作界面的过程。我本来就不该去学一个 Terminal，这件事本身就讲不通。我最熟悉的界面是飞书，就像找人一样去找 Codex 就好了。

所以我觉得，尤其当我们想让非研发团队把 Agent 用好的时候，首先需要建立一个关键认知：Coding Agents 等于 General Agents。这个判断大概在今年一二月份，硅谷就已经形成了共识。Coding Agents are General Agents——一切知识工作理论上都可以借助 Coding Agent 来完成并提升效率。如果 Coding Agent 等于 General Agent，那么未来 Coding Agent 的主要用户将是非程序员，使用 Coding Agent 的非程序员数量一定会远远超过程序员。如果绝大部分 Coding Agent 的使用者不是程序员，那么 Agent 显然不该运行在 Terminal 里，他们不会愿意去学 Terminal；甚至也不该要求他们单独下载一个 App，而是应该出现在他们本就在的地方。应该是 Agent 去找人，而不是让人去找 Agent。我们应当让 Agent 融入我们已经熟悉的工作场景和界面，而不是强迫用户去下载一个新的 App、学习一款新的产品。

视频时长 3分7秒 · 消耗 16 积分 · 积分余额 919

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/7892dbe3-05c6-4863-a52a-802f296cf19c?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FA1neo0ZhqV&s=vtoa)