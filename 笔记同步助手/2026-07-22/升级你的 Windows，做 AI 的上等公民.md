---
author: vink
source: X
url: https://x.com/i/status/2079475456290816050
saved: 2026-07-22 00:02:19
tags:
  - 笔记同步助手
id: fa58333b-be8c-410a-8200-efcb2aeb4691
---

![[笔记同步助手/images/6c33a7da3723d323db2a7e76dfce2229_MD5.jpg|cover]]

用过 Windows 和 mac 的都知道这两个操作系统在 agent 使用上的体感天差地别

最大的根源在于，windows 的命令行工具powershell 对于 AI 不够友好，因为 AI 大模型训练语料里面的命令行操作大部分都是Linux和macos风格的

导致我们经常在windows 上使用agent 的时候会经常报错，平白无故浪费了token

![[笔记同步助手/images/3c340b26bd5bc3c0e05220b323af6ec4_MD5.jpg]]

这篇文章就教你如何升级自己的 windows 也让我们windows用户感受下mac电脑上使用 agent 的丝滑操作

---

先认清三个名字：

| 名称 | 它是什么 | 启动命令 | 你该怎么用 | | --- | --- | --- | --- | | Windows PowerShell 5.1 | Windows 自带的旧版 Shell | \`powershell\` 或 \`powershell.exe\` | 留给旧模块和系统兼容 | | PowerShell 7 | 建立在现代 .NET 上的新版本 | \`pwsh\` 或 \`pwsh.exe\` | 日常 AI、开发和自动化优先使用 | | Windows Terminal | 装载不同 Shell 的终端窗口 | \`wt\` | 把 PowerShell 7 设为默认配置文件 |

对于我们绝大多数人来说，我们的电脑上安装的都是 Windows PowerShell 5.1，一套 2016 年发布、建立在旧版 .NET Framework 上的命令环境。

PowerShell 5.1 是 Windows 的系统组件，承担着老模块兼容任务。但拿它运行今天的 AI CLI、npm 脚本和新教程，环境摩擦会明显增加。Windows PowerShell 5.1 的多个命令保留了不同的旧式默认编码。文件、管道、日志和外部程序混在一起时，中文内容可能出现乱码，JSON 或配置文件也可能被写成下游工具不接受的编码。

PowerShell 7 把更多默认场景统一到 UTF-8 No BOM。它不能消灭所有编码问题，但能减少一批常见冲突。

因此我们需要把日常终端升级到 PowerShell 7。

首先来检查一下，我们电脑上面的 powershell 到底是那个版本的，win+R 快捷键唤醒运行窗口，然后输入 powershell 打开对应窗口

在powershell里面输入：

\`\`\` $PSVersionTable.PSVersion \`\`\`

![[笔记同步助手/images/49eee6f712f5eba956229f80d1ff53e0_MD5.png]]

可以清楚看到我们目前还是PowerShell 5.1 的版本

---

## 接下来我们将正式安装 PowerShell 7

1️⃣ 检查 WinGet

打开 Windows Terminal、命令提示符或现有 PowerShell，执行：

\`\`\` winget --version \`\`\`

![[笔记同步助手/images/d86b51d96faad53c8d1ef3bcdf5636ae_MD5.png]]

能返回版本号，就可以继续。

如果系统提示找不到 winget，先在 Microsoft Store 更新或安装微软的“应用安装程序（App Installer）

2️⃣ 安装 PowerShell 7

先确认 WinGet 找到的是微软官方包：

\`\`\` winget search --id Microsoft.PowerShell --exact \`\`\`

![[笔记同步助手/images/1b78512f2a5a1df0742cb0fc5c9bf48b_MD5.png]]

然后安装：

\`\`\` winget install --id Microsoft.PowerShell --source winget \`\`\`

![[笔记同步助手/images/2bd95e8618ce7f7b75fcb1608b81fedb_MD5.png]]

安装过程可能弹出用户账户控制窗口。确认发布者与包 ID 后再继续。

已经安装过 PowerShell 7，可以用下面的命令检查并升级：

\`\`\` winget list --id Microsoft.PowerShell --upgrade-available winget upgrade --id Microsoft.PowerShell \`\`\`

3️⃣ 用 pwsh 启动新版本

安装完成后，关闭当前终端窗口，重新打开一个窗口，输入：

\`\`\` pwsh \`\`\`

![[笔记同步助手/images/5d0c2d0bd4d57a6a99aa18098f97079c_MD5.png]]

再检查：

\`\`\` $PSVersionTable.PSVersion $PSVersionTable.PSEdition $PSHOME \`\`\`

可以看三个信号：

-   主版本显示 7。
-   PSEdition 显示 Core。
-   $PSHOME 指向 PowerShell 7 的安装目录，例如 Program Files\\PowerShell\\7 或 WindowsApps 下的 PowerShell 包目录。

如果 pwsh 提示找不到命令，先重启 Windows Terminal、VS Code、Cursor 或正在使用的 AI 客户端。安装程序更新了 PATH，旧进程通常看不到新的环境变量。

仍然找不到时运行：

\`\`\` where.exe pwsh Get-Command pwsh -All \`\`\`

到此为止，PowerShell 7 的安装已经全部搞定了

---

4️⃣ 把 PowerShell 7 设成默认终端

这里以 codex 为例子，直接告诉codex，让其检查

\`\`\` 请执行以下命令，告诉我当前 PowerShell 的版本和可执行文件路径： $PSVersionTable.PSVersion (Get-Process -Id $PID).Path \`\`\`

![[笔记同步助手/images/3967c5d1e0dce0ba3188a2f547bf7ec8_MD5.png]]

如果 Codex 仍然显示 PowerShell 5.1

在你的全局 AGENTS.md 中加入：

\`\`\` ## Windows Shell 规则

\- 当前系统已经安装 PowerShell 7。 - 所有 PowerShell 命令必须使用 \`pwsh.exe\` 执行。 - 不要使用旧版 \`powershell.exe\`。 - 执行 PowerShell 命令时，使用以下形式：

pwsh.exe -NoLogo -NoProfile -Command "<命令>"

\- 第一次执行命令前，先运行：

pwsh.exe -NoLogo -NoProfile -Command "$PSVersionTable.PSVersion"

\- 如果 PowerShell 7 不可用，停止执行并告知用户，不要自动退回 Windows PowerShell 5.1。 \`\`\`

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/60f91ca6_1784649736767?u=https%3A%2F%2Fx.com%2FVinkyu567%2Fstatus%2F2079475456290816050)