---
author: Raytar
source: AI整理 - X (Twitter)
url: https://x.com/Raytar/status/2070219094255599645?s=20
saved: 2026-06-26 13:45:38
tags:
  - 笔记同步助手
id: 0f1bbafa-a675-440c-b39b-aed159aa7815
---

## Anthropic 内部员工培训：Claude Code 最佳实践

作者：Raytar

## 1\. Claude.md：项目的长期记忆

最佳实践之一是使用 `Claude.md` 文件。Claude Code 是带工具的 Agent，拥有轻量级提示指令，但本身没有长期记忆。`Claude.md` 可以跨会话、跨团队共享项目状态；启动 Claude Code 时，工作目录中的 `Claude.md` 会被直接加入上下文，作为开发者留下的重要说明。

One of the best practices is to use the `Claude.md` file. Claude Code is a tool-using agent with lightweight prompt instructions but no long-term memory. `Claude.md` shares project state across sessions and teams; when Claude Code starts, the `Claude.md` in the working directory is directly added to the context as an important note left by the developer.

![[笔记同步助手/images/59fc229909599d323b0379e688e95ffc_MD5.jpg|Claude.md 文件示例]]

Claude.md 文件示例

### 存放位置与作用

`Claude.md` 可放在项目中并提交到代码库供团队共享，也可放在 home 目录，让 Claude 在任何项目中读取个人通用偏好或规则。它适合记录单元测试运行方式、项目结构概览、模块职责、代码风格指南等信息，帮助 Claude 更快理解项目。可以逐步积累，不必一次写全。

You can place `Claude.md` in the project and commit it to the repository for team sharing, or put it in the home directory so Claude can read your personal preferences or rules across all projects. It's suitable for recording how to run unit tests, project structure overview, module responsibilities, code style guides, etc., helping Claude understand the project faster. You can accumulate it gradually; you don't need to write everything at once.

![[笔记同步助手/images/a7ac008c4999c20f9e8bb6c748a41243_MD5.jpg|Claude.md 存放位置]]

Claude.md 存放位置

## 2\. 权限管理与自动确认

默认情况下，Claude Code 可自由执行读取和搜索操作；涉及写入、运行 Bash 命令或修改本机内容时，会弹出确认 UI。权限提示通常提供允许、始终允许或拒绝等选项。合理配置权限可显著提升工作速度。

By default, Claude Code can freely perform read and search operations; when it involves writing, running Bash commands, or modifying local content, a confirmation UI will pop up. The permission prompt usually offers options like allow, always allow, or deny. Configuring permissions properly can significantly improve work speed.

![[笔记同步助手/images/2d20cc78a23e57c5f784c7596142dd7b_MD5.jpg|权限确认弹窗]]

权限确认弹窗

### Auto Accept Mode 与命令白名单

`Shift+Tab` 可启用 Auto Accept Mode，让 Claude Code 自动继续工作；也可在设置中预先批准特定命令。例如，如果经常运行 `npm run test`，可将该 Bash 命令设为始终允许，减少重复确认。

You can enable Auto Accept Mode with `Shift+Tab`, allowing Claude Code to continue working automatically; you can also pre-approve specific commands in settings. For example, if you frequently run `npm run test`, you can set that Bash command to always allowed, reducing repeated confirmations.

![[笔记同步助手/images/9b7a41f5f02db602aea48676661306a3_MD5.jpg|Auto Accept Mode 设置]]

Auto Accept Mode 设置

## 3\. 工具集成与 CLI 优先

集成设置很重要：Claude Code 擅长在终端工作，因此应优先利用带 CLI 的应用和工具。GitHub 的 `gh` 是典型例子；安装更多 CLI 工具或连接 MCP server，都能让 Claude Code 承担更多任务。经验建议：如果某个 CLI 工具知名、文档完善，在 CLI 与 MCP server 之间选择时，优先安装并使用 CLI。对内部自研工具，也可以告诉 Claude 如何使用；这类信息适合写入 `Claude.md`。

Integration settings matter: Claude Code excels at working in the terminal, so you should prioritize using CLI applications and tools. GitHub's `gh` is a typical example; installing more CLI tools or connecting MCP servers allows Claude Code to take on more tasks. Experience suggests: if a CLI tool is well-known and well-documented, prefer installing and using the CLI over an MCP server. For internal custom tools, you can also tell Claude how to use them; such information is suitable for `Claude.md`.

![[笔记同步助手/images/d115761a947ea3077550173a188a85aa_MD5.jpg|CLI 工具集成]]

CLI 工具集成

## 4\. 上下文管理：/clear 与 /compact

需要管理上下文：Claude 通过调用工具持续工作，交互越久上下文越大。Anthropic 模型上下文窗口约为 200,000 tokens，但仍可能被填满。长会话中，界面右下角会提示上下文窗口即将填满，此时有两个主要选择：`/clear` 或 `/compact`。

Context management is needed: Claude works by calling tools continuously, and the context grows with more interactions. Anthropic's model context window is about 200,000 tokens, but it can still be filled. In long sessions, the bottom right of the interface will indicate the context window is almost full, at which point you have two main options: `/clear` or `/compact`.

![[笔记同步助手/images/5dd3c2c19c7c2b4b49af30aba286ab75_MD5.jpg|上下文窗口提示]]

上下文窗口提示

`/clear` 会清空当前上下文并重新开始，但保留 `Claude.md` 等基础信息。`/compact` 会让 Claude 总结当前进展，类似写给接手开发者的交接说明，并用该摘要作为后续会话的起点。Anthropic 对 `/compact` 功能做了大量调优，使用户在上下文达到上限后仍能压缩历史、继续推进工作。

`/clear` clears the current context and starts fresh, but retains base information like `Claude.md`. `/compact` tells Claude to summarize the current progress, similar to handover notes for the next developer, and uses that summary as the starting point for subsequent sessions. Anthropic has tuned the `/compact` feature significantly, allowing users to compress history and continue working even after the context limit is reached.

![[笔记同步助手/images/7d429bb8213113e0f77b06027f988630_MD5.jpg|/compact 生成摘要]]

/compact 生成摘要

## 5\. 高效工作流与调试技巧

使用 Claude Code 时，先让它调查 bug 成因并给出修复计划，而不是直接要求修复；先审阅计划可节省时间、降低误改风险。Claude Code 有待办列表功能；处理大任务时可观察其 To-do，如发现方向异常，按 Escape 中断并要求调整计划。

When using Claude Code, first let it investigate the cause of a bug and give a fix plan, rather than asking for a fix directly; reviewing the plan first saves time and reduces the risk of incorrect changes. Claude Code has a to-do list feature; when handling large tasks, you can observe its to-dos, and if the direction seems wrong, press Escape to interrupt and ask it to adjust the plan.

![[笔记同步助手/images/43e1c4ad9f898835fc47b86df215ca56_MD5.jpg|待办列表与中断]]

待办列表与中断

### 小步验证与 TDD

“Smart vibe coding” 的核心不是放任 Claude 一路执行，而是让它小步改动、频繁验证。推荐结合测试驱动开发：让 Claude 做小变更、运行测试、确认通过，并检查 TypeScript 与 lint。应定期提交代码；如果 Claude 走偏，可以回退到最近稳定版本后重新尝试。

The core of "smart vibe coding" is not letting Claude run wild, but making small changes and frequent verifications. It's recommended to combine test-driven development: let Claude make small changes, run tests, confirm they pass, and check TypeScript and lint. Commit code regularly; if Claude goes astray, you can revert to a known good state and try again.

![[笔记同步助手/images/59d8ab2625ad12e7fba9b0c5895e17b2_MD5.jpg|小步验证与测试]]

小步验证与测试

### 多实例并行

进阶用法之一是同时运行多个 Claude 实例。一些 Anthropic 员工和客户会开 4 个，可用 tmux 或多个标签页来编排任务。Escape 是关键控制手段：Claude 执行时持续观察，发现方向不对或想改变任务时立即中断并插入新指令。高效使用 Claude 的关键，是判断何时按 Escape 干预、何时让它自行探索完成。隐藏功能：连按两次 Escape 可回到对话早前位置，相当于回滚并重置后续交互。

One advanced usage is running multiple Claude instances simultaneously. Some Anthropic employees and customers run 4 instances, using tmux or multiple tabs to orchestrate tasks. Escape is the key control: continuously observe Claude's execution, and if it goes in the wrong direction or you want to change the task, interrupt immediately and give new instructions. The key to efficient Claude use is judging when to press Escape to intervene and when to let it explore and finish on its own. Hidden feature: pressing Escape twice returns to an earlier point in the conversation, effectively rolling back and resetting subsequent interactions.

## 6\. 模型选择与扩展思考

新功能：在 Claude Code 中输入 `/model` 可查看当前模型；默认可能是 Sonnet，也可切换到 Opus，`/config` 中也能切换。应根据任务选择合适模型，确保当前运行的是最适合自己需求的模型。

New feature: typing `/model` in Claude Code shows the current model; the default might be Sonnet, but you can switch to Opus, also via `/config`. Choose the appropriate model for the task to ensure you're running the model best suited to your needs.

![[笔记同步助手/images/c3a5e2f7d995ee55f69434c0d9119df7_MD5.jpg|模型切换命令]]

模型切换命令

### 扩展思考模式（Thinking）

可让 Claude “think hard” 或使用扩展思考来理解项目。从 Claude 4 起，模型可在工具调用之间继续思考。过去模型不能在工具调用之间思考，而这往往是最需要推理的时刻；Claude 4 改进后可边查看项目文件边持续推理。触发 Claude Code 的“thinking”模式后，会看到浅灰色思考文本；它会调用文件和工具、读取资料，再继续推理，适合排查 bug 或复杂任务时加入“think hard”。

You can ask Claude to "think hard" or use extended thinking to understand the project. Starting with Claude 4, the model can continue thinking between tool calls. Previously, models couldn't think between tool calls, which was often when reasoning was most needed; Claude 4 improves this by allowing continuous reasoning while reviewing project files. When you trigger the "thinking" mode in Claude Code, you'll see light gray thinking text; it will call files and tools, read materials, and continue reasoning, suitable for debugging or complex tasks where you add "think hard".

![[笔记同步助手/images/3c3cb5ecb6586ea5912425eeedce899a_MD5.jpg|扩展思考模式]]

扩展思考模式

## 7\. 编辑器集成与持续关注更新

Claude Code 已集成 VS Code 和 JetBrains，可感知当前编辑器上下文，例如知道正在打开的文件，并据此协助操作。建议持续关注 Anthropic GitHub 上的公开项目 `Claude Code`：可提交 issue，也可查看 changelog；演讲者每周查看一次，以跟进快速发布的新功能。

Claude Code is integrated with VS Code and JetBrains, and can sense the current editor context, for example knowing which file is open, and assist accordingly. It's recommended to follow the public `Claude Code` project on Anthropic's GitHub: you can submit issues, check the changelog; the speaker checks it once a week to keep up with quickly released new features.

![[笔记同步助手/images/258159a797aefff544751ef95f3e5511_MD5.jpg|编辑器集成]]

编辑器集成

## 8\. 多 Claude.md 与高级配置

关于项目内多个 `Claude.md`：同一目录不能有多个，但可在子目录中放置；默认启动时只读取当前工作目录的 `Claude.md`，也可在用户 home 目录设置一个全局版本。Anthropic 曾因 monorepo 顶层启动时读取所有子目录 `Claude.md` 导致上下文爆炸，因此改为默认不自动读取子目录文件；Claude 在搜索项目时若发现相关子目录 `Claude.md`，会被鼓励主动读取。新功能允许在 `Claude.md` 中用 `@` 引用其他文件；如果有一些固定需要加载的说明文件，可在主 `Claude.md` 中显式引用。

Regarding multiple `Claude.md` files in a project: you can't have more than one in the same directory, but you can place them in subdirectories; by default, only the `Claude.md` in the current working directory is read, and you can also set a global version in the user's home directory. Anthropic once caused context explosion by reading all subdirectory `Claude.md` files when starting from the top of a monorepo, so they changed the default to not automatically read subdirectory files; Claude is encouraged to read relevant subdirectory `Claude.md` files when it discovers them during project search. A new feature allows using `@` in `Claude.md` to reference other files; if you have fixed instruction files that need to be loaded, you can explicitly reference them in the main `Claude.md`.

![[笔记同步助手/images/62bfd718699da14a4455394050aa3280_MD5.jpg|多 Claude.md 配置]]

多 Claude.md 配置

### 模型版本对指令遵守的影响

有用户反馈 Claude 不总是遵守 `Claude.md`，例如被要求重构时仍反复添加显而易见的注释。回答指出这部分主要是模型问题：Claude 3.7 即使系统提示中强调不要留注释，模型仍倾向于添加注释。Claude 4 基本改善了过度添加注释的问题，并整体更擅长遵循指令；早期测试者反馈 `Claude.md` 的约束被执行得更严格。切换到新模型后，建议重新审视 `Claude.md`：删除不再需要的旧规则，补充新的项目约束，避免说明冗余或过时。

Some users reported that Claude doesn't always obey `Claude.md`, for example repeatedly adding obvious comments when asked to refactor. The answer noted that this is largely a model issue: Claude 3.7, even with system prompts emphasizing not to leave comments, still tended to add them. Claude 4 basically improved the over-commenting issue and is generally better at following instructions; early testers reported that `Claude.md` constraints are enforced more strictly. After switching to a new model, it's recommended to revisit `Claude.md`: remove old rules that are no longer needed, add new project constraints, and avoid redundant or outdated instructions.

![[笔记同步助手/images/7f8a5d5a79a2ba3774b9054e93bfc12e_MD5.jpg|模型指令遵守对比]]

模型指令遵守对比

## 9\. 多 Agent 共享上下文的实践方案

关于多智能体并行执行时共享上下文：目前团队优先做“简单且有效”的方案，即一个擅长编码的主 agent 完成全部工作，而非复杂多 agent 协作架构。若需要多个 agent 共享上下文，可能的做法是让各 agent 写入共享 Markdown 文件，用它作为沟通和状态同步媒介；演讲者表示自己有时也会这样与 Claude 协作。建议把需要交接给另一个开发者的上下文写入文件，例如 `ticket.md`，说明任务、背景和下一步。然后启动另一个 Claude Code，让它读取 `ticket.md`，把它当作前一位开发者留下的任务说明来继续工作。当前较可行的做法是将状态和上下文持久化到文件中，依赖模型读取文件并理解内容的能力完成衔接。这可能是目前最好的方案；未来产品中或许会提供更原生、更智能的上下文交接方式。

Regarding sharing context when multiple agents execute in parallel: currently the team prioritizes a "simple and effective" approach, i.e., a single main agent that is good at coding completes all work, rather than a complex multi-agent collaboration architecture. If multiple agents need to share context, a possible approach is to have each agent write to a shared Markdown file, using it as a medium for communication and state synchronization; the speaker mentioned that he sometimes collaborates with Claude this way. It's recommended to write the context that needs to be handed over to another developer into a file, for example `ticket.md`, describing the task, background, and next steps. Then start another Claude Code and let it read `ticket.md`, treating it as a task description left by the previous developer to continue. The current feasible approach is to persist state and context into files, relying on the model's ability to read files and understand content to complete the handover. This might be the best solution for now; future products may provide more native and intelligent context handover mechanisms.

![[笔记同步助手/images/1ccc6ea160f7b18c36ac13424cf71cf4_MD5.jpg|文件持久化共享上下文]]

文件持久化共享上下文

## 逐字稿

**00:01** Now, let's talk about best practices.

**00:05** And the first one is not going to be a surprise,

**00:08** but the first one is use Claude.md files.

**00:12** So remember that Claude Code, like I said,

**00:14** is an agent and it has some tools.

**00:17** It has some lightweight instructions in the prompt,

**00:19** but it doesn't really have memory.

**00:21** And so the main way we share state across kind of sessions

**00:25** or across our team when we fire up Claude Code

**00:28** in the same codebase over and over again

**00:31** is this Claude.md file.

**00:32** So when we start Claude, what happens

**00:35** is if there's this Claude.md file in the working directory,

**00:38** it's just plopped into context.

**00:40** It's plopped into the prompt.

**00:41** And basically what it says is, hey,

**00:43** Claude, by the way, these are important instructions

**00:45** the developer left for you.

**00:47** Be sure to pay close attention to this.

**00:49** And there's various places you can put the claude.md file.

**00:52** You can put it in a project and check it in

**00:54** so all your teammates share it.

**00:56** You could put one in your home directory

**00:58** if there's things you just want Claude to always know about,

**01:00** regardless of what you're working on.

**01:02** And the things you put in here are things like, hey, by the way,

**01:05** maybe this is how you run the unit tests.

**01:08** Or just so you know, to make your searching and life easier,

**01:12** here's just an overview of how this project is laid out,

**01:15** where the tests live, what different modules are,

**01:18** things like that.

**01:19** Or here's our style guide, all sorts of things

**01:22** like that to just make Claude's life a bit easier.

**01:24** And you can build these things up over time.

**01:29** The other thing you can do, which is important,

**01:31** is permission management.

**01:33** When you're running Claude Code, there's

**01:34** all sorts of different kind of permission things flying by.

**01:37** Kind of out of the box, what happens when you start our tool

**01:41** is for read actions.

**01:42** If Claude is searching or reading, we just let it go.

**01:46** But once it starts writing or running bash commands

**01:49** or doing things that could change stuff on your machine,

**01:53** potentially, that's when we kick in this UI

**01:56** and it says something like, yes, yes, always allow this,

**01:59** or no, I want to do something else.

**02:03** And using that permission management

**02:05** and being smart about it can help you work faster.

**02:08** So there's something called Auto Accept Mode,

**02:11** where if you're working with Claude Code and you press Shift

**02:13** Tab, Claude will just start working.

**02:16** There's things you can do, like you can configure Claude

**02:18** in the settings where specific commands, like on Bash,

**02:22** Like if you just are tired of saying, yes, run npm run test,

**02:26** you can just always approve that.

**02:28** So fiddling with your permission management

**02:30** is a great way to kind of speed up your workflow.

**02:34** Integration setup.

**02:35** So one thing that is going to help you

**02:37** get the most out of Claude Code is remember

**02:40** that it's great at the terminal.

**02:41** And if there's applications that you use which

**02:44** have kind of a way to access them through CLI,

**02:47** and GitHub is a great example of that,

**02:49** they have a powerful tool called GH,

**02:51** you can basically give more work to Claude Code.

**02:55** And you can do that either by just installing more CLI tools,

**02:59** or you can attach more MCP servers.

**03:02** I would say, just through experience,

**03:04** that if you're using something like a CLI tool that's

**03:08** well-known and well-documented, and you're

**03:10** trying to choose between the CLI tool and just

**03:13** installing it on your machine and grabbing an MCP server,

**03:17** I would recommend using the CLI tool.

**03:20** And then also, if you internally have your own tools,

**03:24** at Anthropic we have something called

**03:26** Koo that does a whole bunch of stuff for us.

**03:28** You can also tell Claude about that,

**03:30** and that's the sort of thing you'd put in claude.md.

**03:34** And then context management.

**03:36** So remember that Claude is an agent.

**03:39** And what it does, it calls these tools.

**03:42** And the context builds up and up over time.

**03:45** And at least for Anthropic, our models

**03:47** have a context window of 200,000 tokens.

**03:49** And you can max this thing out.

**03:51** So you kind of have two options when

**03:53** you're in a long session with Claude, and you're working,

**03:55** and you're going back and forth.

**03:57** You'll see in the bottom right, you'll

**03:58** start to get this little warning that'll say, hey.

**04:01** You're starting to fill up the context window.

**04:03** And kind of depending on what's going on,

**04:04** you have two options.

**04:06** You can run slash clear and just start over,

**04:08** and that clears everything out except for, for instance,

**04:11** Claude.md.

**04:12** Or you can run slash compact.

**04:14** And what will happen is basically it's like a user

**04:17** message is inserted.

**04:19** And it just says something like, hey, I need to go summarize

**04:22** everything we've been up to.

**04:23** I'm going to give this to another developer,

**04:25** and they're going to pick up where I left off.

**04:27** And then that summary is what kind of seeds the next session.

**04:30** And you can go from there.

**04:31** We spend a lot of time tuning this kind of compact

**04:34** functionality so that as you max out the context window

**04:37** and then run compact, you can start back over and keep going.

**04:43** Efficient workflows.

**04:43** What can you do with Claude Code?

**04:45** and how do you get the most out of it.

**04:47** So using planning and to-dos, I talked a little bit

**04:50** about this before.

**04:51** But one of the best things you can

**04:52** do is when you open up Claude Code, instead of saying,

**04:55** hey, I need you to fix this bug, you can say, hey,

**04:58** I have this bug.

**04:59** Can you search around, figure out what's causing it,

**05:01** and just tell me a plan how we're going to fix it?

**05:04** And this can save you a lot of time,

**05:06** because you can verify.

**05:07** You can read Claude's plan, and you can verify

**05:09** what it's going to do.

**05:11** And then the other thing that we have

**05:13** is we have this to-do list feature.

**05:14** So often when Claude's working on a big task,

**05:17** it'll create a to-do list.

**05:19** And if you're kind of paying attention,

**05:21** you can kind of watch this to-do list.

**05:23** And if you see anything kind of weird in there

**05:25** or something that doesn't make sense,

**05:27** that's when you can press escape and say, hey, Claude,

**05:29** let's change the to-do list.

**05:30** I think you're on the wrong path.

**05:32** Smart vibe coding.

**05:34** So it's very tempting and it's very powerful

**05:36** to just let Claude work and press Enter

**05:38** and see what happens at the end.

**05:40** I think there's a few things that can help make this better.

**05:43** And there's, I think, a talk later today about just this

**05:46** for 30 minutes.

**05:47** But doing things like having test-driven development,

**05:50** having Claude make small changes, run the tests,

**05:53** make sure they pass, always having Claude do things

**05:56** like check the TypeScript and the linting,

**05:58** and then commit regularly so that if it's

**06:01** kind of going off the rails, you can always roll back

**06:03** and try again.

**06:05** You can use screenshots to guide and debug.

**06:07** So Claude is built on top of our models, which

**06:10** are multimodal.

**06:11** You can always just grab a screenshot, paste it in.

**06:14** Or if you have a file somewhere that's an image,

**06:16** you can just say, hey, Claude, look at this mock.png,

**06:20** and then build the website for me, or whatever.

**06:23** And then advanced techniques.

**06:25** So as you're getting used to using Claude,

**06:27** what are some things you can think about to kind of push

**06:31** things to the next level?

**06:32** And one of the things we see, both internally and with

**06:35** customers, is when you've started to use this tool

**06:37** for a while, it's going to be very tempting

**06:40** to use multiple Claudes at once.

**06:42** And so I know people at Anthropic and a few customers

**06:45** that run four Claudes at the same time.

**06:47** There's various ways to do this.

**06:49** You can have it in tmux or just different tabs,

**06:52** all sorts of crazy things.

**06:53** So I would challenge you to try getting multiple Claudes running

**06:57** at once and kind of be orchestrating all these things.

**07:00** It's quite fun.

**07:01** I can only do two, but I know people that do four.

**07:05** Use escape.

**07:06** So escape is your best friend.

**07:08** While Claude is working, you can kind of keep an eye

**07:11** on what it's up to.

**07:12** And you can press escape to stop it and interject and say,

**07:15** hey, I think you're going on the wrong path

**07:17** or I want you to do something else.

**07:19** Knowing when the right time to press escape

**07:21** is versus just letting Claude figure it out

**07:24** is key to getting the most out of the tool.

**07:26** And there's a hidden feature.

**07:28** Not too many people know about it.

**07:29** But if you press escape twice, you can actually

**07:31** jump back in your conversation.

**07:33** You can go back and you can kind of reset.

**07:37** Tool expansion and MCP.

**07:39** So this is taking it to the next level.

**07:41** If you feel like with Bash and with the tools that Claude has

**07:44** that it still can't do something,

**07:47** this is when you should start looking at MCP servers.

**07:50** And then headless automation.

**07:51** I think this is a thing we're most excited about,

**07:54** but also we are still trying to wrap our heads around

**07:57** internally, which is how can we use Claude programmatically.

**08:01** We have that in GitHub Actions.

**08:03** We want to figure out other creative places

**08:06** we can start using it.

**08:07** I would challenge you all to do the same.

**08:11** So with that said, I'm going to jump over to my computer,

**08:16** because there's one other best practice, which

**08:18** is it's always good to stay on top of everything that's new.

**08:22** So we're shipping super fast.

**08:25** I'm just going to go over a few things that

**08:26** are new as of today.

**08:29** One thing is when you're in Claude now and you fire it up,

**08:32** you can do slash model.

**08:34** You can see what model you're running on.

**08:36** I'm on default, which happens to be Sonnet.

**08:38** We can jump over to Opus.

**08:40** You can do the same thing in slash config.

**08:43** Switch it here.

**08:46** So that's new.

**08:47** Make sure you're running the model that works for you.

**08:50** There's another thing that's new about these models, which

**08:53** is you can say something like, can you

**08:57** figure out what's in this project?

**08:59** And for a while, we've had this think hard,

**09:02** or extended thinking.

**09:04** Now, this is great, but with our past models,

**09:08** we wouldn't let our model think between tool calls.

**09:10** And that's probably when the thinking matters most.

**09:12** So starting with Claude 4, our models now

**09:16** think between tool calls.

**09:17** And we can watch this happen.

**09:18** So we have Claude in this project.

**09:20** There's a few different files in here.

**09:21** And I'm just going to tell it to think hard and figure out

**09:24** what's in this project.

**09:26** And we can watch Claude start to work.

**09:28** And so the way you know you triggered thinking

**09:30** is you'll see kind of this lighter gray text.

**09:33** And then it'll call some file.

**09:35** It'll call some tools.

**09:36** It'll read some stuff.

**09:37** And then we see some more thinking.

**09:39** And this is awesome.

**09:41** So I encourage you, when you're working on tasks

**09:43** and solving bugs, throw a "think hard" in there.

**09:47** And then the other thing, and you know what?

**09:51** We'll just throw it up real quick,

**09:52** is I have this in VS Code.

**09:55** But of course, this is in JetBrains as well.

**09:57** But we have these new great integrations with VS Code

**10:00** and JetBrains.

**10:02** We can do things like, Claude's going to know what file I'm in.

**10:05** What file am I in?

**10:10** That is not what I meant to say, but Claude's

**10:11** going to figure it out.

**10:14** And you can do things like this.

**10:26** So these are the sort of things I would encourage you

**10:28** to stay on top of.

**10:29** We have a public GitHub project called Claude Code

**10:34** under Anthropic.

**10:35** You can post issues there, but we also

**10:37** post our changelog there.

**10:39** And so I check this once a week and make sure

**10:41** that I'm on top of all the new stuff we're shipping,

**10:43** because even I can't keep up with it.

**10:46** So with that said, we have like four minutes left.

**10:48** I'm happy to answer questions about anything Claude Code

**10:51** related.

**10:51** We have it here.

**10:52** I can live demo some stuff if you're interested.

**10:56** Let's do a few.

**10:57** Let's do him first, and then you.

**10:59** Thanks, real quick. This might be obvious, but multiple claude.md files in a project,

**11:07** I presume that's possible and it just figures it out, or no?

**11:11** So there's a few options. Of course, like in the same directory, you couldn't. But you

**11:20** could have one here and one in a subdirectory. And I think we changed this so that all the

**11:27** subdirectory ones aren't read in,

**11:28** because like Anthropic, we have a monorepo.

**11:31** And people would open it at the top

**11:32** and blow up their context with all the Claude.mds.

**11:36** So we encourage Claude when it's searching around

**11:39** and it discovers Claude.md files in child directories that

**11:43** are relevant to be sure to read them.

**11:46** But by default, it just reads the Claude.md file

**11:49** in the current working directory when you fire it up.

**11:51** And then also you can set one in your home directory.

**11:55** There are things you can do, though.

**11:56** We have this new thing.

**11:58** In your Claude.md, you can start referencing other files.

**12:03** So you could, for instance, do something

**12:06** like this with an at sign.

**12:08** If you have other Claude.md files

**12:10** that you just kind of know you always

**12:11** want to read in, to do something like that.

**12:16** Hi.

**12:17** OK.

**12:17** I have not had luck getting Claude to respect my Claude.md.

**12:23** There's one thing particular where I'll ask it

**12:25** to refactor something, and then it

**12:27** will leave inline comments explaining the what of it is.

**12:31** And it's something that's extremely obvious.

**12:33** And so I'll tell it, go and remove any inline comments

**12:37** that describe the what of what's happening,

**12:38** and then it will remove it, and then immediately do it again

**12:41** in the same pass.

**12:42** So do you have any strategies for dealing with that?

**12:44** So there's kind of two things that fix that.

**12:47** So that was actually kind of a model problem.

**12:49** There's nothing in the prompt.

**12:50** We have actually a lot in the prompt for 3.7 that said,

**12:53** whoa, do not leave comments.

**12:55** And despite that, the model just loves to leave comments.

**12:58** So it doesn't surprise me that your claude.md didn't help

**13:00** much either.

**13:02** I did a lot of work to try to tamp it down

**13:04** from what happens out of the box.

**13:06** So we mostly fixed that in Claude 4.

**13:11** Now there might be some new weird behavior quirks.

**13:13** But the other thing we made better in Claude 4

**13:15** is it's just better at following instructions.

**13:18** And we've gotten a lot of feedback from early testers

**13:20** that all of a sudden, whoa, my Claude.md

**13:23** is being followed way more closely.

**13:26** And it might be a good chance to go look in your Claude.md

**13:28** and decide, do I still need this stuff?

**13:31** Maybe I can take some of it out.

**13:33** Maybe I need to add a few new things.

**13:35** So moving over to the new models might

**13:36** be a good time to take another look at what's in there

**13:39** and see what you need and what maybe can go.

**13:42** For the record, I'm trying to think of something

**13:45** that you might not have thought of.

**13:46** Yes.

**13:47** When doing multi-agent execution and parallelization,

**13:50** can you make it so that for four agents, say,

**13:53** agents two and three use the context from agent one.

**13:56** Maybe agent four uses the context from agent two

**13:58** at a certain point.

**13:59** Yeah.

**14:01** Yeah, et cetera.

**14:02** That's interesting.

**14:03** We're trying to, so kind of like I said at the beginning,

**14:06** we're trying to do the simple thing that works,

**14:08** which is just one agent that's great at coding

**14:10** and does everything.

**14:12** I think we want to figure that out.

**14:14** Probably what's going to happen is if you wanted to do that,

**14:17** you would ask all your agents to probably

**14:19** like write to a shared Markdown file or something like that

**14:23** so they can all kind of like check in and communicate.

**14:26** Sometimes I'll be working with Claude

**14:29** and I'll just say like, hey, I need

**14:31** you to write some stuff in like ticket.md for another developer.

**14:34** And then I'll fire up another Claude Code.

**14:36** I'll be like, hey, read ticket.md.

**14:37** Like another developer left this note for you.

**14:40** Like this is what you're going to work on.

**14:42** So I would think about trying to write that state to a file

**14:45** and then just kind of like count on the model's ability

**14:47** to just read files and make sense of them.

**14:51** It's probably the best you can do today.

**14:53** And maybe we'll figure out clever ways

**14:55** to expose that in the product as something more native.

**15:00** Cool.

**15:03** All right.

**15:04** And with that said, I have some rare Claude Code stickers

**15:08** that I found in my backpack.

**15:09** So come find me.

**15:10** I'll be hanging out over there or something.

**15:12** I'm happy to share them.

**15:14** Thank you.

视频时长 15分14秒 · 消耗 77 积分 · 积分余额 19

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9ed098ab-1df3-42c5-be3a-ff5e3387f4d3?u=https%3A%2F%2Fx.com%2FRaytar%2Fstatus%2F2070219094255599645%3Fs%3D20&s=vtoa)