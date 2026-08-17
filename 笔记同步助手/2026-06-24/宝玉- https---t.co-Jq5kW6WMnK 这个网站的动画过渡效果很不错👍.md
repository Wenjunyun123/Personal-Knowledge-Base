---
author: 宝玉
source: X
url: https://x.com/dotey/status/2069513317693964418?s=20
saved: 2026-06-24 14:12:03
tags:
  - 笔记同步助手
id: 4e6f7773-8af4-457b-908d-be94f1084951
---

🔗 [在 X 查看原文](https://x.com/dotey/status/2069513317693964418)

[transitions.dev](http://transitions.dev) 这个网站的动画过渡效果很不错👍  
还可以安装 Skill，这样 Agent 可以自己为你的网页添加炫酷的动画  
npx skills add jakubantalik/transitions.dev

---

## 💬 评论（10）

> **ShenYi @shenyiLiu**
> 
> 有没有那种生成图片的过度动画

> **阿超聊AI @achao\_talks**
> 
> 现在连动效都能 npx 装成 skill 了…前端这种有标准答案的活儿迟早全被打包掉，收藏了....

> **ShenYi @shenyiLiu**
> 
> 这个太需要了，每次我自己做这种动效都不知道咋描述

> **Iamveektoria.base.eth 🙂‍↔️🌳 ✠ @iamveektoria\_**
> 
> +1

> **AI Mastery Guide @aiseomastery**
> 
> Installing it as a skill so the agent reuses the transitions on its own is way better than copy pasting css every time.

> **Cxxxxx的平行宇宙 @maxiaochiyu**
> 
> 这个好！

> **bitmart92 - 直连通道 🔥 @chinabeijing**
> 
> 这动效丝滑到想给网页做全套大保健

> **nemo @nemoisme**
> 
> 这个动效确实好好看

> **you @youfei0719\_**
> 
> 好舒服好舒服

> **宝玉 @dotey**
> 
> 分享一下我管理 Skills 的方式，偏极客风格，不一定适合所有人，但可以给大家提供一个思路。  
>   
> 一、Skills 只装在项目里，不装全局  
>   
> Agent 的 Skills 可以装在全局（所有项目共享）或者项目内（只有当前项目能用）。我选择只装在项目内，最主要的原因是节约上下文空间。  
>   
> Agent 在工作时有一个上下文窗口，你可以把它想象成 Claude 的工作台——台面大小是有限的。虽然 Skill 默认只会加载名称、描述等摘要信息（不会把完整内容全部摊开），但积少成多——全局装了几十个 Skill，光是这些摘要加在一起也会占掉不少工作台空间。而且一旦 Claude 判断某个 Skill 跟当前任务相关，就会把它的完整内容加载进来，全局 Skill 越多，被误触发的概率也越大，白白浪费空间。  
>   
> 只在项目内安装真正需要的 Skills，工作台上就只摆当前用得到的资料，把宝贵的空间留给更重要的内容，Claude 干活也更高效。  
>   
> 二、用软链接来安装 Skills  
>   
> 这是我管理方式的核心，先解释一下什么是软链接。  
>   
> 你可以把软链接理解成 Windows 的快捷方式——文件本体只有一份，但你可以在很多地方创建快捷方式指向它。改了本体，所有快捷方式指向的内容都会同步变化。  
>   
> 我的具体做法分三步：  
>   
> 第一步：把开源 Skills 项目下载到统一的目录  
>   
> 我在电脑上有一个专门存放 GitHub 项目的文件夹 ～/GitHub，所有下载的开源项目都放在这里面，比如：  
>   
> ～/GitHub/baoyu-skills ← 存放各种 Skills 的开源项目  
> ～/GitHub/baoyu-design ← 另一个开源项目  
>   
> 这个文件夹就像一个仓库，所有 Skills 的原件都保存在这里。  
>   
> 第二步：在自己的项目中创建软链接  
>   
> 假设我有一个写作项目 ～/GitHub/baoyu-writing，里面需要用到好几个 Skills。我不会把 Skills 复制进来，而是创建软链接，让项目指向仓库里的原件：  
>   
> 项目内的路径 → 实际指向的位置（原件）  
> .agents/skills/baoyu-comic → ～/GitHub/baoyu-skills/skills/baoyu-comic  
> .agents/skills/baoyu-design → ～/GitHub/baoyu-design/skills/baoyu-design  
>   
> 第三步：给 Claude Code 建一个入口  
>   
> 最后再创建一个软链接，让 Claude Code 能找到这些 Skills：  
>   
> .claude/skills → .agents/skills  
>   
> 这样 Claude Code 就能顺着这条链找到所有需要的 Skills 了。  
>   
> 三、不用记命令，让 Agent 帮你干  
>   
> 看到这里你可能会想：软链接的命令我记不住怎么办？  
>   
> 完全不用记。直接用自然语言告诉 Codex/Claude Code 你要做什么就行了，比如：  
>   
> \> 帮我把 ～/GitHub/baoyu-skills/skills/baoyu-comic 软链接到 .agents/skills/baoyu-comic  
>   
> 甚至更简单：  
>   
> 帮我把 baoyu-skills 项目里的 baoyu-comic 这个 skill 链接到当前项目  
>   
> Agent 会自动帮你创建软链接，后续的维护、添加、删除也都可以交给它。你只需要说清楚要把哪个 Skill 链到哪，剩下的脏活累活让 Agent 干就好。  
>   
> 四、为什么值得这么折腾？  
>   
> 初次设置确实比直接复制粘贴多花几分钟，但后续维护特别省心，主要有两个好处：  
>   
> 好处一：更新只需一次。因为所有项目都是通过软链接指向同一份原件的，所以当开源项目有更新时，我只需要去 ～/GitHub/baoyu-skills 拉取最新代码，所有用到这个 Skill 的项目就自动变成最新版了。  
>   
> 好处二：修了 bug 可以直接反哺。比如我在写作项目里用漫画 Skill 画漫画时发现了一个问题，直接让 Agent 修复就好。因为是软链接，Agent 修改的其实是仓库里的原件（～/GitHub/baoyu-skills/skills/baoyu-comic），我可以直接把修复提交到开源项目，相当于顺手给开源社区做了贡献。
> 
> ![[笔记同步助手/images/bc68a27ec4e2117ef07274ba132bde25_MD5.jpg]]

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/e9962e60_1782281521254?u=https%3A%2F%2Fx.com%2Fdotey%2Fstatus%2F2069513317693964418)