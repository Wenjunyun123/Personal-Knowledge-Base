---
author: 宝玉
source: X
url: https://x.com/dotey/status/2069632132431929651?s=20
saved: 2026-06-24 20:54:13
tags:
  - 笔记同步助手
id: 4754fca7-0011-4f81-a3ee-a7ef9a5a08d1
---

🔗 [在 X 查看原文](https://x.com/dotey/status/2069632132431929651)

分享一下我管理 Skills 的方式，偏极客风格，不一定适合所有人，但可以给大家提供一个思路。  
  
一、Skills 只装在项目里，不装全局  
  
Agent 的 Skills 可以装在全局（所有项目共享）或者项目内（只有当前项目能用）。我选择只装在项目内，最主要的原因是节约上下文空间。  
  
Agent 在工作时有一个上下文窗口，你可以把它想象成 Claude 的工作台——台面大小是有限的。虽然 Skill 默认只会加载名称、描述等摘要信息（不会把完整内容全部摊开），但积少成多——全局装了几十个 Skill，光是这些摘要加在一起也会占掉不少工作台空间。而且一旦 Claude 判断某个 Skill 跟当前任务相关，就会把它的完整内容加载进来，全局 Skill 越多，被误触发的概率也越大，白白浪费空间。  
  
只在项目内安装真正需要的 Skills，工作台上就只摆当前用得到的资料，把宝贵的空间留给更重要的内容，Claude 干活也更高效。  
  
二、用软链接来安装 Skills  
  
这是我管理方式的核心，先解释一下什么是软链接。  
  
你可以把软链接理解成 Windows 的快捷方式——文件本体只有一份，但你可以在很多地方创建快捷方式指向它。改了本体，所有快捷方式指向的内容都会同步变化。  
  
我的具体做法分三步：  
  
第一步：把开源 Skills 项目下载到统一的目录  
  
我在电脑上有一个专门存放 GitHub 项目的文件夹 ～/GitHub，所有下载的开源项目都放在这里面，比如：  
  
～/GitHub/baoyu-skills ← 存放各种 Skills 的开源项目  
～/GitHub/baoyu-design ← 另一个开源项目  
  
这个文件夹就像一个仓库，所有 Skills 的原件都保存在这里。  
  
第二步：在自己的项目中创建软链接  
  
假设我有一个写作项目 ～/GitHub/baoyu-writing，里面需要用到好几个 Skills。我不会把 Skills 复制进来，而是创建软链接，让项目指向仓库里的原件：  
  
项目内的路径 → 实际指向的位置（原件）  
.agents/skills/baoyu-comic → ～/GitHub/baoyu-skills/skills/baoyu-comic  
.agents/skills/baoyu-design → ～/GitHub/baoyu-design/skills/baoyu-design  
  
第三步：给 Claude Code 建一个入口  
  
最后再创建一个软链接，让 Claude Code 能找到这些 Skills：  
  
.claude/skills → .agents/skills  
  
这样 Claude Code 就能顺着这条链找到所有需要的 Skills 了。  
  
三、不用记命令，让 Agent 帮你干  
  
看到这里你可能会想：软链接的命令我记不住怎么办？  
  
完全不用记。直接用自然语言告诉 Codex/Claude Code 你要做什么就行了，比如：  
  
\> 帮我把 ～/GitHub/baoyu-skills/skills/baoyu-comic 软链接到 .agents/skills/baoyu-comic  
  
甚至更简单：  
  
帮我把 baoyu-skills 项目里的 baoyu-comic 这个 skill 链接到当前项目  
  
Agent 会自动帮你创建软链接，后续的维护、添加、删除也都可以交给它。你只需要说清楚要把哪个 Skill 链到哪，剩下的脏活累活让 Agent 干就好。  
  
四、为什么值得这么折腾？  
  
初次设置确实比直接复制粘贴多花几分钟，但后续维护特别省心，主要有两个好处：  
  
好处一：更新只需一次。因为所有项目都是通过软链接指向同一份原件的，所以当开源项目有更新时，我只需要去 ～/GitHub/baoyu-skills 拉取最新代码，所有用到这个 Skill 的项目就自动变成最新版了。  
  
好处二：修了 bug 可以直接反哺。比如我在写作项目里用漫画 Skill 画漫画时发现了一个问题，直接让 Agent 修复就好。因为是软链接，Agent 修改的其实是仓库里的原件（～/GitHub/baoyu-skills/skills/baoyu-comic），我可以直接把修复提交到开源项目，相当于顺手给开源社区做了贡献。

![[笔记同步助手/images/bc68a27ec4e2117ef07274ba132bde25_MD5.jpg]]

---

**🧵 作者续推（1）**

> **2/** Skills 的更新就跟着 git 走最好，通常都是开源项目，哪怕不是开源的也可以用私有 git repo 管理起来，需要更新去对应项目 git pull 一下，需要特定版本就去 git checkout。  
> 这事你也不用自己做，可以在 Codex/CC 里面搞个定时任务，自动做  
> [x.com/linghucong/status/2069674665476…](https://x.com/linghucong/status/2069674665476501935?s=20)

---

## 💬 评论（31）

> **LinearUncle @LinearUncle**
> 
> skills 只放在项目内的话，有一些日常频次比较高的工作流怎么办？  
> 例如：twitter /youtube视频->字幕文字稿->AI 问答  
> z-library 下载书籍  
> iPhone“提醒事项”增删改查  
> 等等一些常见的日常任务，是放到一个项目里吗？每次去那个固定项目里操作？感觉有点麻烦

> **Feiteng @FeitengLi**
> 
> 宝玉老师的skill 我是装全局的，而且跨工具共享， Claude code Codex 都必须有

> **zhili @zhili669029**
> 
> 多 agent 情况下这样管理确实方便。不过这样安装 skill 的时候可能稍微麻烦点，需要让 agent 先下载到 github 目录，然后创建软连接。否则 直接使用 npx add 这种指令就直接给装到 skill全局目录下了

> **Kid @singkid9527**
> 
> 学习了。我一开始也是学的宝玉老师，Skills 放 Github 项目里，在软连接到 各种 Agent。  
>   
> 接下来就是慢慢习惯项目级 Skill 的用法。

> **K. @Kainative**
> 
> 已经在本地配置了。Skill 的原件只留一份，其他地方全用"快捷方式"指过去。之前我把同一个 skill 复制进十个项目，就有了十份副本，然后用着用改 bug修复也烂在那个项目里回不到原件，更回不到开源社区。软链接就把这个问题从根上掐掉：原件只有一份在仓库里，所有项目都是指过去不是搬过来，很有效。

> **天然 @juyiBaib**
> 
> 基于项目+软链接这个思路好,全局太多skill,哪怕只是元数据,占的上下文也多

> **vink @Vinkyu567**
> 
> 宝玉老师，我就是这样建立一个中央skill仓库，然后cc和codex都是通过软链接来管理的  
> [x.com/Vinkyu567/status/20688960901670…](https://x.com/Vinkyu567/status/2068896090167074906)

> **JZ @\_junzhen**
> 
> [github.com/orca-studio/ghq-skills/](https://github.com/orca-studio/ghq-skills/)  
>   
> 我选择从 统一管理源仓库的 x-motemen/ghq 加个 skills 子命令来管 ～.～

> **狐狸布布 @baibaida**
> 
> 项目级隔离这点太对了 全局装久了根本想不起来哪个还在用 跟收藏夹吃灰一个道理

> **别处理 @zhengsihua\_dev**
> 
> +1，不过我还没有细致到项目级别的skill管理，目前是所有安装的skill全部软链到全局skill目录下了，后续可以优化成项目管理的方式，学到了

> **树影 @TreeShadow\_1**
> 
> 在不同的项目里软链skills，如果不同项目的输入输出的路径可能不一样，宝玉老师有什么建议，是使用配置文件来解决还是有其他更便捷的方案。

> **阿超聊AI @achao\_talks**
> 
> 这套正好能治 LinearUncle 那个浆糊:把 .codex/skills、.claude/skills 都软链到同一个 skills 源,几个 agent，就共享一份,改一处全同步,不用各写各的了😂

> **祖平 | AI 实战派 @ping\_zu8939**
> 
> 这套软链方案我很受用，想追一个协作场景：单人多项目时”改一次处处更新”是纯优点，但多人协作时，别人 clone 你的项目拿到的是个指向你本地 ～/GitHub 的死链。你是怎么处理的——是约定大家仓库结构一致，还是关键 skill 干脆复制进项目、只对自己常改的用软链？我一直在”复用”和”可移植”之间摇摆。

> **严毅 @yo\_yan14480**
> 
> 这个管理方法很合理，学习了。我现在是建了一个放所有skills的库，但没有软连接和全局、项目的详细区分，要用这个思路再改改

> **Michael Chan @Michael55366361**
> 
> 软链接的方法就是跟宝佬学的，现在管理起来很方便👍

> **linghucong @linghucong**
> 
> skills的更新也是个问题，有什么好的方案么？

> **Steven Cheng @stevencheng**
> 
> 软链接确实省心。我还会加个.gitignore，避免把源文件误提交到项目仓库里。

> **xiaobeiLin(小北) @linxiaobei888**
> 
> skill一多，超过一定的token，剩下的cc和codex都会丢弃掉，所以有些Skill不知不觉就永远不会被触发

> **Xiaowen @ixiaowenz**
> 
> 我也是这么干的，专项专用，我有一个装 SKILL 和测试调试 SKILL 的项目，靠软连接提供给工作区项目。

> **nemo\_biubiubiu @nemo\_biubiubiu**
> 
> [skill.xn--shnpx-vj0ms2fi4jiv1d](http://skill.sh用的那种npx) skills package manager呢？

> **刚劲 @gltrade100**
> 
> 软链接的思路太妙了，更新和修复自动同步到所有项目，省去了手动维护的繁琐，极客范儿十足👍

> **Jacky无限生长 @jacky\_infinite**
> 
> 大佬的偏技术流，我是直接交给cc Switch管理的，也能实现软连接，skill放项目这点学到了，我目前精简了很多，但还是全局加载的。

> **不辞远 @sharebravery**
> 
> 使用ccswitch管理会更方便

> **奇怪的猫 @WanWu77058**
> 
> 极客式管理 Skills 的思路很实用，尤其是用软链接统一维护版本，既省上下文又方便回传修复。不过“让 Agent 自动创建软链接”这一步，如果指令描述不够精确，反而可能引入路径错误或循环依赖风险。建议先在小范围项目手动验证链路稳定性，再全量依赖 Agent 操作，毕竟工具再智能，清晰的底层逻辑才是高效的关键。

> **琬琬，♥处男免费♥ @Shawn127346**
> 
> 🥦

> **book or technique @liu360567**
> 
> 这个软链接的思路太优雅了啊  
> 终于不用被这几个 agent 的路径折磨疯了哈

> **book or technique @liu360567**
> 
> We need a package manager for this.  
> Like npm but for agent skills.  
> Who is going to build it?

> **雨蕊🌸寻固炮🌸点击主页 @VeronicaBi7712**
> 
> 🤝

> **chenglong 523 @Chenglong523**
> 
> 宝玉老师，我去买您的书了，但是好像全都是预售的，没有现货。京东、淘宝、拼多多都看了，好像都没有现货。我还是从京东上下单等着呢，京东上还是靠谱的，其他地儿我怕买到的是盗版的

> **卡牌大师崔斯特 @cuisitekp**
> 
> 项目内装skills确实省上下文 全局装多了agent容易跑偏

> **灵灵七 @min\_zhen07**
> 
> 宝玉老师干货！这套组合拳完美解决多 Agent 技能混乱问题，学到了👍

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/9ed2b0b4_1782305650495?u=https%3A%2F%2Fx.com%2Fdotey%2Fstatus%2F2069632132431929651)