# 个人网站 × FDE：执行手册（每一步都配好工具）

> 原则：**不从头造，先抄跑通的**。每个动作都写到"打开哪个、粘什么话、几分钟后看到什么"。
> 起点 2026-11-24。你库里的 59 篇收藏，这里只挑能立刻上手的，其余留在 `wiki/topics/AI 前端设计与交付实践路线.md` 当备查。

---

## 一、今天 90 分钟：三个动作，立刻看到差别

### 动作 1（30 分钟）· 先给你现在的站做一次"AI 味体检"

- **用什么**：[Impeccable](https://github.com/pbakaus/impeccable)（62 条规则，不用大模型就能扫出 AI 味）
- **怎么用**：把仓库链接丢给 Codex/Claude，粘这句：

  > 读这个仓库的 README，把它装成当前项目的 skill。装完扫描这个项目所有页面文件，按严重程度列出 AI 味问题，每条给出文件位置和改法。不要直接改代码。

- **看到什么**：一份清单——Inter 字体、紫到蓝渐变、卡片套卡片、灰色小字说明。这份清单就是你后面所有改动的靶子。
- **为什么它有效**：它认的是"套路"而不是"风格"，所以不会把你改成另一个模板。

### 动作 2（30 分钟）· 用现成设计主题套一次，看清差距

- **用什么**：[Hallmark](https://github.com/nutlope/hallmark)（50 套设计主题：纸张、字体、配色、质感全配好）
- **怎么用**：粘这句：

  > 读 README 装成 skill。然后对我首页执行 hallmark redesign：内容一个字不动，只换设计。做完在真实浏览器里用桌面/平板/手机三种宽度各截一张图给我。

- **看到什么**：同一份内容、三种设计并排。你会立刻知道"高大上"差在哪——通常是留白和字阶，不是特效。
- **顺手**：[Anti UI Slop](https://uizze.com/) 和 [Taste Skill](https://github.com/Leonxlnx/taste-skill) 二选一存着，别三个一起装（会互相打架、吃满上下文）。

### 动作 3（30 分钟）· 找 3 个能抄的对象，不是 10 个

- **用什么**：[godly.website](https://godly.website/)（获奖级网页）、[land-book.com](https://land-book.com/)（落地页）、[60fps.design](https://60fps.design/)（移动端动效）
- **怎么用**：只存 3 张首屏截图，每张写一行：**第一句话说什么 / 字阶几档 / 动效出现在哪**。
- **看到什么**：3 行可执行的参数，而不是"感觉很好看"。

---

## 二、网站线：每个任务对应哪个工具

| 任务 | 用什么 | 怎么用（一句话） | 验收 |
| --- | --- | --- | --- |
| 定视觉方向 | [Taste Skill](https://github.com/Leonxlnx/taste-skill)、[MengTo/Skills](https://github.com/MengTo/Skills)（150 组件设计系统） | 让它按"博客 / 杂志 / 档案 / 工作台"四个隐喻各出一套，你选一个 | 三套方向结构不同，不是三个配色 |
| 去 AI 味（结构） | Impeccable + `AGENTS.md` 禁令 | 把"不加辅助说明、描述性文字、冗余微文案"写进 `AGENTS.md` | 界面不再出现"点击了解更多"类小字 |
| 去 AI 味（文案） | [humanizer-zh](https://github.com/op7418/humanizer-zh) | 所有中文文案过一遍 | 读起来不像说明书 |
| 高端感（3D/动态区块） | [motionsites.ai](https://motionsites.ai/)（800+ 3D 与动态区块提示词）、[designbookmark](https://designbookmark.com/motion) | 挑一个提示词，丢给 Claude 直接生成一个区块 | 只用在 1 个地方，别全站铺 |
| 首屏动效 | [Motion](https://github.com/motiondivision/motion)（原 Framer Motion） | 先写"什么时候动、动多久、动哪个属性"，再让 AI 实现 | CLS 不抖、不卡 |
| 讲清一个功能 | [stick-scene](https://github.com/nilbuild/stick-scene) | "读我的项目，给 2 个火柴人场景创意，我选一个" | 一个功能演成一个小动作 |
| 品牌字体溯源 | [fontinlogo.com](https://fontinlogo.com/) | 查你喜欢的品牌用的字体 | 字体有出处，不是默认 Inter |
| 上线 | [Cloudflare Pages](https://pages.cloudflare.com/) + [Neon](https://neon.tech/) + [Resend](https://resend.com/) + [Clerk](https://clerk.com/) | 一句话："把我的项目部署到 Cloudflare Pages，数据库用 Neon" | 真实域名可访问，push 即上线 |
| 收费 | Stripe + 服务端鉴权 | 付费内容必须在服务端裁剪，前端遮挡等于没做 | 未登录拿不到正文 |

**一个真实参照**（照着它的技术选型抄）：[[笔记同步助手/2026-11-23/从 0 到 1 用 Vibe Coding 构建 OilBook AI 知识库：产品设计、技术选型、内容生产与上线复盘|OilBook 复盘]] —— Next.js + Neon + 本地 Markdown（不上 CMS）+ Vercel + Cloudflare DNS + Resend + Stripe。它把"哪些决策该先定"讲清楚了。

**免费额度别记，直接抄这张单**（原文称，2026-11 快照）：Cloudflare Pages 不限带宽可商用 / Workers 10 万请求每天 / D1 5 GB / R2 10 GB；Neon 免费不限项目数（多产品首选）；Supabase 500 MB 库 + 1 GB 存储 + 5 万 MAU；Clerk 5 万 MAU；Resend 100 封每天（需自有域名）。

---

## 三、FDE 线：直接照抄别人的流程，不用自己发明

### 3.1 先看官方五课（有人已经把流程拆好了）

- 第 1 课《7 分钟搞懂什么是 FDE》 https://bytedance.larkoffice.com/file/PAJTbmeZJowrRoxqW51cC60nn5f
- 第 2 课《伙伴 FDE 每天都在做什么》 https://bytedance.larkoffice.com/file/Tnbmbug7zokSMVxze5PcwtnOn7q
- 第 3 课《飞书、豆包 产品全景地图》 https://bytedance.larkoffice.com/file/MOWybWSIAo0KCIxx3ktcTN7Jn8c
- 第 4 课《FDE 的一天》 https://bytedance.larkoffice.com/file/W99JbZQWFoed12x7TVAcWLaVnpf
- 第 5 课《需求诊断》 https://bytedance.larkoffice.com/file/YKhDbC6kRo4ntkxysoCcmivqn0O

**第 5 课直接当 SOP 用**：进门前 3 项准备 → 45 分钟访谈问 5 个问题再追问 → 候选场景打分挑第一个 → 写一份诊断记录。一句话："先诊断，后开药"。

### 3.2 把网站当客户项目练一遍（这是最快的 FDE 训练）

| FDE 环节 | 用什么 | 怎么用 |
| --- | --- | --- |
| 需求对齐 | [mattpocock/skills](https://github.com/mattpocock/skills) 里的 `grill-me` | 开工前让 AI 反过来一条条拷问你到底要什么，对齐了再动手 |
| 行业/竞品摸底 | 哈佛五力 9 提示词（[[笔记同步助手/2026-11-23/如何快速进入一个陌生行业？我把哈佛五力模型拆成 9 个 AI 提示词，3 天摸清任何行业底细|笔记]]） | 查（AI 调研）→ 问（找人）→ 试（自己走一遍）→ 下判断 |
| 一页方案 | 无工具，30 分钟手写 | 背景 / 目标 / 方案 / 取舍 / 风险，五段 |
| 两天出 demo | Hallmark + OilBook 架构 | 别做新产品，先改现有页 + 接一个真数据源 |
| 交付审查 | [cloudflare/security-audit](https://github.com/cloudflare/security-audit-skill) | 派新 Agent 专门推翻上一个 Agent 的结论 |
| 自动化交付 | [agent-desktop](https://github.com/vercel-labs/agent-desktop) | 按元素编号操作软件，不靠截图认图 |
| 复用抽象 | 写进你的 Skill 库 | 每单结束问：这次哪一步下单选能直接复用 |

**FDE 的真相**（你收藏的那篇访谈）：沟通占七成、开发占三成。所以别把时间全花在学框架上，把"45 分钟问到真需求"和"一页方案"练熟，比会第三个框架值钱。

---

## 四、案例线：从"收藏"改成"抄一条记一条"

- **入口 1**：[[笔记同步助手/2026-11-23/Mian🍜- 本周GitHub神级项目🤯🤯👍 第一名一个月涨了4w6 光是治AI审美的就|Mian 的 GitHub 周榜]] —— 每周只挑一个，装进项目，用一次。
- **入口 2**：[[笔记同步助手/2026-11-23/用 Codex 或 Claude 制作电影感动画、视频与动态设计：18 个 GitHub 项目工具清单|18 个项目清单]] —— 做视频时按目标查表（宣传片/讲解/录屏/三维/动效）。
- **入口 3**：[[笔记同步助手/2026-11-23/如果你平时用 AI 做设计，这几个网站你一定要看看👇：|8 个设计站]] —— 没灵感时才打开，别当日常刷。

**记录格式只有三行**：它解决什么 / 我在哪用了 / 我改了什么。连续两周没被用到的，删掉。

---

## 五、harness 线：让项目"可托管"，而不是每次重新解释

| 层（越下越可靠） | 用什么 | 怎么做 |
| --- | --- | --- |
| 代码与 API 设计 | 架构边界 | 让正确用法成为最自然的用法（比如把主进程/渲染进程拆成两个目录，禁止互导） |
| lint / 类型 / 测试 | ESLint + TS + 导入禁令 | 每次纠正 AI，先问"能不能变成一条规则"，不能才写进 `AGENTS.md` |
| 运行时验证 | Playwright / CDP + 功能映射 | 给 agent 一份"应用有哪些功能、在哪个位置"的清单，它才不会瞎猜 |
| 文字规则 | `AGENTS.md` / skill | 只放需要判断力的要求，不放已知错误 |

- **禁注释**：团队级做法是禁掉约 99% 的注释——注释不能被执行，还会成为 agent 给临时补丁辩护的借口。
- **多 Agent 工作台**：[Orca](https://github.com/stablyai/orca)（一个 Agent 一个工作区）、[T3 Code](https://github.com/pingdotgg/t3code)（手机批准下一步）、[[笔记同步助手/2026-11-22/在 Herdr 中用 hc 创建 Pi 子 Agent|Herdr Pi 子 Agent]]
- **额度与反代**：[Magpie](https://github.com/yetone/magpie)（多渠道聚成一个本地端点）
- **省 token**：DeepSeek Harness 思路——把已确定的步骤缓存掉，别每次重跑

---

## 六、AI 视频线：最短路径，先出片再学软件

1. **60 秒讲解片** → [HyperFrames](https://github.com/heygen-com/hyperframes)：写 HTML/CSS/GSAP，直接导 MP4。先写 6 句脚本，再让它生成画面。
2. **产品演示/动态信息图** → [Remotion](https://github.com/remotion-dev/remotion) + [Remotion Skills](https://github.com/remotion-dev/skills)（给 Codex/Claude 的现成技能）。
3. **落地页小场景** → [stick-scene](https://github.com/nilbuild/stick-scene)。
4. **长文转图** → Diagram Design（原文称近 6 万 star，具体仓库待补）。
5. **真人出镜太重** → 先不做数字人，用录屏 + 配音；真要做，看[[笔记同步助手/2026-11-23/玩转实时数字人直播 - 免显卡保姆级教程|免显卡教程]]。

---

## 七、节奏：每周只做三件

- **周一**：一个改造（用上面某个工具，30 分钟能看到差别）
- **周三**：一个补课（FDE 五课其中一课 / 一次 lint 化）
- **周五 30 分钟复盘**：① 做完了但没验收的是哪件 ② 哪个纠正这周出现第三次（第三次 → 变成规则）③ 下周删掉什么

每两周问一次：**换一个全新会话的 agent 只读 `AGENTS.md` + `DESIGN.md`，能不能第一次就做对？** 做不对是规范的问题，不是模型的问题。

---

## 八、本手册的依据

- [[笔记同步助手/2026-11-20/用 AGENTS.md 约束 Codex，减少前端设计中的 AI Slop]]
- [[笔记同步助手/2026-11-23/从 0 到 1 用 Vibe Coding 构建 OilBook AI 知识库：产品设计、技术选型、内容生产与上线复盘]]
- [[笔记同步助手/2026-11-20/别人的代码都是垃圾：如何用 Agent 环境与验证机制支撑单月 3000 个 PR]]
- [[笔记同步助手/2026-10-04/最火AI岗位FDE：月薪5万，都干这些…]]
- [[笔记同步助手/2026-11-21/吴文煜分享的工具 · 方法 · 资料索引]]
- [[笔记同步助手/wiki/topics/AI 前端设计与交付实践路线]]
