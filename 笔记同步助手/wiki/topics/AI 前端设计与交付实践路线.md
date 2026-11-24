---
title: "AI 前端设计与交付实践路线"
type: topic
aliases:
  - AI 前端
  - AI Slop
  - AI 写前端
tags:
  - knowledge-base/topic
  - 前端
  - AI编程
  - 设计
sources:
  - "[[笔记同步助手/2026-11-20/用 AGENTS.md 约束 Codex，减少前端设计中的 AI Slop]]"
  - "[[笔记同步助手/2026-11-19/Google 开源 Modern Web Guidance：让 AI 前端代码从 56% 提升至 88%]]"
  - "[[笔记同步助手/2026-11-23/10 个能把 AI 味压下去的技能：]]"
  - "[[笔记同步助手/2026-11-23/Mian🍜- 本周GitHub神级项目🤯🤯👍 第一名一个月涨了4w6 光是治AI审美的就]]"
  - "[[笔记同步助手/2026-11-23/从 0 到 1 用 Vibe Coding 构建 OilBook AI 知识库：产品设计、技术选型、内容生产与上线复盘]]"
  - "[[笔记同步助手/2026-11-20/别人的代码都是垃圾：如何用 Agent 环境与验证机制支撑单月 3000 个 PR]]"
created: 2026-11-24
updated: 2026-11-24
status: growing
---

# AI 前端设计与交付实践路线

## 范围

本页综合 2026-10-02 至 2026-11-23 期间由「笔记同步助手」入库的 59 篇笔记（10 月 11 篇、11 月 48 篇；其中 3 篇是同步助手索引页）。其中约 30 篇与 AI 辅助前端设计、AI 编码治理、动效与上线直接相关，是本页的取用范围。

未纳入：AI 视频/剪辑/数字人、Agent 框架横向评测、职场沟通、搜索与网络工具、AI 论文清单。它们与本路线弱相关，仍留在 Raw。

## 当前综合：四层结构

这批笔记表面上很杂（工具清单、团队实践、单人复盘），但收敛到同一件事上：**AI 做前端，瓶颈不在生成能力，而在"judgment（审美判断）+ 上下文 + 约束"三件事没人给它**。可以拆成四层，越往下越确定、也越该先建。

| 层 | 解决什么 | 代表材料 | 确定性 |
| --- | --- | --- | --- |
| L4 产出层 | 动效、视频、上线 | HyperFrames、Remotion、Motion、stick-scene、Cloudflare/Neon/Resend | 低 |
| L3 工程层 | 让错误写法写不出来 | lint、类型、架构边界、运行时验证、形式化 | 高 |
| L2 上下文层 | 设计系统、竞品、产品隐喻 | MengTo/Skills 150 组件、MCP 接设计系统、`DESIGN.md` | 中 |
| L1 审美层 | 认出并去掉 "AI 味" | Impeccable、Taste Skill、Hallmark、Anti UI Slop | 中 |

一处来源间的**真实分歧**：露西/何笠这类清单派认为"装 2–3 个 skill 就能把 AI 味压下去"；Lauren Tan（Grok 团队）一派认为文字规则与 skill 文件是**最不可靠**的一层，已知问题必须沉淀为 lint、类型、架构约束。我的综合是两条路并行但分工明确：**审美属于判断力，写不成 lint，只能靠 skill + 设计系统 + 人看图；正确性属于工程，必须靠确定性检查**，用 skill 去治 `useEffect` 滥用只会反复失败。

## 一条可执行的路线（6 周，每周一个可验收产物）

前置：已有可跑的前端项目（否则第 0 周先让 AI 起一个 Next.js 骨架，见 OilBook 的技术选型）。

**第 0 周｜立规矩（半天）**
- 动作：在项目 `AGENTS.md` 里写入"禁止项"而非"注意事项"——不加无意义的次要标签、辅助说明、描述性文字和冗余微文案；不把内部设计理由写进面向用户的设置项（小石的四条）。
- 动作：生成 `DESIGN.md`（字体、色板、间距、圆角、动效时长、断点），此后所有页面改动以此为据（OilBook 的做法）。
- 动作：只装 2 个审美 skill，推荐 Impeccable（62 条规则扫 AI 味）+ Taste Skill。不要 10 个全上（原帖也这么说）。
- 验收：让 AI 改现有设置页，产出里不出现"关闭设置窗口后仍可使用"这类小字；出现即回写 `AGENTS.md`。

**第 1 周｜喂上下文（1 周）**
- 动作：把组件库/设计系统接进对话（MCP 或直接把真实代码喂进去），而不是让它临时发挥——这是"转化率翻倍"案例的核心结论：**关键不在提示词，在上下文**。
- 动作：拆 3 个竞品（文案结构 + 视觉 token），再让它按产品隐喻出 3 套视觉方向，选一套（OilBook：现代博客 / 杂志小册 / 古典书本）。
- 验收：同一个需求，AI 首轮产出的颜色、字体、间距不需要你手改。

**第 2–3 周｜建护栏（2 周）**
- 动作：把上周纠正过 AI 的每一处，翻译成可复现的检查——ESLint 规则、TS 类型、目录级导入禁令（例：`electron-main` 与 `electron-renderer` 互不导入），而不是再加一行注释。
- 动作：加运行时验证。让 agent 自己起服务、用 CDP/Playwright 点一遍、截图；先给一份"功能映射"清单（应用有哪些功能、在哪个位置），否则它会猜"左边那个东西"。
- 动作：禁掉 99% 的注释（Lauren Tan 团队做法），避免 agent 用注释为临时补丁辩护。
- 验收：一个 PR 里附带截图/测试结果，而不是只有 diff；同类错误第二次出现时已被 lint 拦住。

**第 4 周｜动效（1 周）**
- 动作：首屏锁一段真动画。技术选型：网站内交互用 Motion；要导出视频用 Remotion + Remotion Skills 或 HyperFrames（HTML/CSS/GSAP 渲成 MP4）；要"讲清一个功能"的轻量方案用 stick-scene 的火柴人场景。
- 验收：落地页首屏有一段能在真浏览器里跑的动画，且没有布局抖动（CLS）与掉帧；做不出来就退回静态图，不要堆截图。

**第 5 周｜上线闭环（1 周）**
- 动作：前端 Cloudflare Pages（可商用、不限带宽）→ 后端 Workers 或 Supabase → 数据库 Neon（免费不限项目数）/ D1 / Turso → 存储 R2 → 认证 Supabase Auth 或 Clerk → 邮件 Resend（需自有域名）→ 支付 Stripe。
- 动作：付费内容**必须服务端鉴权裁剪**，前端遮挡等于没做。
- 验收：真实域名可访问，注册/收信/付款三条链路自己完整走一遍。

**第 6 周｜写回规范（半天）**
- 动作：把 6 周里所有纠正写回 `AGENTS.md` / `DESIGN.md` / lint 规则。这是"自生长"的部分：每次纠正都变成下次的默认。

## 可用资源清单

链接均为 2026-11-24 实际解析/探测结果（原笔记中的 `t.co` 短链已还原）。

**L1 审美治理（先装 2 个，别全装）**

| 资源 | 用途 | 链接 |
| --- | --- | --- |
| Impeccable | 62 条规则扫 AI 味（Inter 字体、紫蓝渐变、卡片套卡片）；`bolder`/`quieter` 调语气 | https://github.com/pbakaus/impeccable ｜ https://impeccable.style/ |
| Taste Skill | 给 AI 设计品味，按公司官网标准排版，多断点真浏览器检查 | https://github.com/Leonxlnx/taste-skill |
| Hallmark | 50 套设计主题（纸张/字体/配色/质感），可 `hallmark redesign` 只换设计不动内容 | https://github.com/nutlope/hallmark |
| Anti UI Slop | 反 UI 套路 skill | https://uizze.com/ |
| Emil Kowalski Skills | 设计工程实践（动画、交互细节） | https://github.com/emilkowalski/skills |
| Vercel Web Design Guidelines | 前端设计规则 skill 集合 | https://github.com/vercel-labs/agent-skills |
| Anthropic Frontend Design | 官方 frontend-design skill | https://github.com/anthropics/skills |
| Make Interfaces Feel Better | 交互手感改进 | https://github.com/jakubkrehel/make-interfaces-feel-better |
| UI UX Pro Max | UI/UX 综合 skill | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| Stageshow（Benji Taylor） | 演示/展示类 skill | https://github.com/benjitaylor/skills |
| humanizer-zh | 中文文案去 AI 味 | https://github.com/op7418/humanizer-zh |

**L2 上下文与设计系统**

| 资源 | 用途 | 链接 |
| --- | --- | --- |
| MengTo/Skills | 公开的设计 Skills，含 150 组件设计系统（搜索/天气/日程/支付/农业数据等界面） | https://github.com/MengTo/Skills |
| Modern Web Guidance（Google 开源） | 给 AI 换"现代前端教材"，原文称前端能力 56%→88% | 原文未附链接，待补（见「待核实」） |
| 灵感站 · 获奖网页 | 收录获奖级网页设计 | https://godly.website/ |
| 灵感站 · 落地页 | 落地页灵感 | https://land-book.com/ （探测 403，站点存在） |
| 灵感站 · 移动端动效 | 移动 UI 动画灵感 | https://60fps.design/ |
| 灵感站 · 顶级落地页 | 落地页合集 | https://landdding.com/ |
| 灵感站 · 设计图库 | 网页设计灵感图库 | https://recent.design/ |
| 灵感站 · 品牌字体 | 查大品牌 Logo 背后的字体 | https://fontinlogo.com/ |
| 3D/动态区块提示词 | 800+ 3D 网站与动态区块提示词，复制给 Claude 直接生成 | https://motionsites.ai/ ｜ https://studio.motionsites.ai/ |
| 动效灵感 | 动态设计书签库 | https://designbookmark.com/motion |

**L3 工程护栏与验证**

| 资源 | 用途 | 链接 |
| --- | --- | --- |
| mattpocock/skills | TypeScript 名师日常在用的技能集，`grill-me` 会先反问你需求 | https://github.com/mattpocock/skills |
| Cloudflare security-audit | 多 Agent 分头找漏洞，再派新 Agent 推翻结论，报告分已确认/待验证/已排除 | https://github.com/cloudflare/security-audit-skill |
| agent-desktop（Vercel Labs） | 让 AI 按元素编号操作桌面软件，不靠截图认图 | https://github.com/vercel-labs/agent-desktop |
| Chrome WebMCP | 网站主动注册工具，AI 直接调用 JS 能力，替代模拟点击 | 原文无链接（见「待核实」） |
| DeepSeek Harness | 缓存已确定步骤，原文称 token 降 87.93%、成功率 +14% | 原文无链接 |
| fast-anything | 自动定位性能瓶颈并重写关键代码 | 原文无链接 |
| Obscura | 面向自动化/Agent 的开源浏览器 | 原文无链接 |

**L4 动效、视频与上线**

| 资源 | 用途 | 链接 |
| --- | --- | --- |
| HyperFrames（HeyGen） | 用 HTML/CSS/GSAP 写画面，导出 MP4，19 个按项目顺序排列的 skill | https://github.com/heygen-com/hyperframes |
| Remotion | 用 React 做视频与动态信息图 | https://github.com/remotion-dev/remotion |
| Remotion Skills | 教 agent 正确使用 Remotion | https://github.com/remotion-dev/skills |
| Motion（原 Framer Motion） | 网站内布局过渡与弹簧动画 | https://github.com/motiondivision/motion |
| Motion Canvas | 代码驱动的动画讲解 | https://github.com/motion-canvas/motion-canvas |
| stick-scene | 一句话让 agent 画会动的火柴人小场景，用于落地页讲功能 | https://github.com/nilbuild/stick-scene |
| Blender Skills | 把 Blender 工作流转成 agent 可用的 skill | https://github.com/EL4CTEO/blender-skills |
| GSAP / Three.js / ComfyUI / Blender MCP | 网页动画、三维场景、节点式生图、AI 操控 Blender | 见「18 个项目清单」原文 |
| Cloudflare Pages / Workers / D1 / R2 | 前端托管（可商用、不限带宽）、10 万请求/天、5 GB 库、10 GB 存储 | https://pages.cloudflare.com/ ｜ https://workers.cloudflare.com/ |
| Neon | 云端 Postgres，免费不限项目数（多产品共用首选） | https://neon.tech/ |
| Supabase | 后端 + Postgres 500 MB + 存储 1 GB + Auth 5 万 MAU | https://supabase.com/ |
| Clerk | 认证，5 万 MAU | https://clerk.com/ |
| Resend | 邮件，100 封/天，需自有域名 | https://resend.com/ |
| Stripe | 收款与订阅 | https://stripe.com/ |

**学习方法**

| 资源 | 用途 | 链接 |
| --- | --- | --- |
| Anthropic《Claude Code 实践》PDF | 原文称"最便宜的 AI 教材"：上传给模型→中文总结→拆成 3 个可落地步骤，约 30 分钟 | 原文无链接（见「待核实」） |
| Shay「10 周入门法」 | 只留一条主线、先"扔"再"抓"、建一个 Lab 文件夹、按周丈量 | [[笔记同步助手/2026-10-07/用 10 周在一个领域真正入门：Shay 的「周生活」突破法]] |
| 哈佛五力 9 提示词 | 查（AI 调研）→ 问（找人）→ 试（自己走一遍）→ 下判断 | [[笔记同步助手/2026-11-23/如何快速进入一个陌生行业？我把哈佛五力模型拆成 9 个 AI 提示词，3 天摸清任何行业底细]] |
| Magpie / Multica | 多渠道反代统一端点；Agent 小队编排 | https://github.com/yetone/magpie ｜ https://github.com/multica-ai/multica |

## 分歧与限制

- **数字都来自原作者口述，未独立核验**：56%→88%（Modern Web Guidance）、5.17 倍渲染提速、单月 3000 PR / 团队 11000 PR / 回滚率 0.5%、token 降 87.93%、转化率翻倍。本页只记录"该来源称"，不作为事实断言。
- **时效性强**：GitHub 周榜排名、star 数、免费额度（500 MB / 5 GB / 5 万 MAU / 100 封/天）均为 2026-11 快照，落地前需按官网当前条款复核。
- **审美工具高度重叠**：Impeccable / Taste / Hallmark / Anti UI Slop 解决同一类问题，同时装会互相冲突并大量吃上下文，装 2 个即可。
- **两条路线的优先级不同**：清单派把 skill 当解药，Lauren Tan 派把 skill 放在最不可靠层。本页取"审美靠 skill、正确性靠 lint/架构"的分工，而非二选一。
- **左侧缺失**：这批笔记几乎全部来自 X / 抖音 / 视频号转述，一手文档（Google 的 Modern Web Guidance、Anthropic 的 PDF）都没有链接，本页无法追到原始出处。

## 相关页面

- [[笔记同步助手/wiki/topics/AI 辅助个人知识管理]]
- [[笔记同步助手/wiki/concepts/增量知识维护]]
- [[笔记同步助手/wiki/concepts/LLM Wiki]]
- [[笔记同步助手/wiki/entities/Codex]]

## 来源

- [[笔记同步助手/2026-10-05/AI写的代码到底能不能信？Bob大叔用确定性工具取代逐行检查]]
- [[笔记同步助手/2026-10-07/用 10 周在一个领域真正入门：Shay 的「周生活」突破法]]
- [[笔记同步助手/2026-10-12/谷歌开发者大会收获：用 HTML in Canvas 把 HyperFrames 渲染提速 5.17 倍]]
- [[笔记同步助手/2026-10-15/2026 独立开发者零成本上线全家桶：从前端托管到邮件服务]]
- [[笔记同步助手/2026-11-01/Agno 智能体开发框架：从个人 Agent 到 AgentOS 的快速构建方案]]
- [[笔记同步助手/2026-11-02/Karpathy 用 Claude Code 打造 HackerTube：从社区推荐中自动筛选优质视频]]
- [[笔记同步助手/2026-11-03/Chrome 推出 WebMCP：浏览器自动化从模拟点击转向直接调用网页工具]]
- [[笔记同步助手/2026-11-17/Grok 团队如何用 AI 编程提升交付效率：代码治理、规则约束与自动化验证]]
- [[笔记同步助手/2026-11-19/2026 独立开发者零成本上线工具栈：前端、后端、数据库与邮件服务]]
- [[笔记同步助手/2026-11-19/Anthropic 员工使用 Claude Code 的实践指南：30 分钟整理出可落地的 AI 学习步骤]]
- [[笔记同步助手/2026-11-19/DeepSeek Harness：缓存已确定步骤，Token 消耗降低 87.93%，任务成功率提升 14%]]
- [[笔记同步助手/2026-11-19/Diagram Design：用 AI 将长文本一键转化为专业可视化图表]]
- [[笔记同步助手/2026-11-19/Google 开源 Modern Web Guidance：让 AI 前端代码从 56% 提升至 88%]]
- [[笔记同步助手/2026-11-19/Obscura：专为自动化任务与 AI 代理设计的开源浏览器]]
- [[笔记同步助手/2026-11-19/OpenFilm：用 HTML-CSS 构建并微调视频画面]]
- [[笔记同步助手/2026-11-20/别人的代码都是垃圾：如何用 Agent 环境与验证机制支撑单月 3000 个 PR]]
- [[笔记同步助手/2026-11-20/用 AGENTS.md 约束 Codex，减少前端设计中的 AI Slop]]
- [[笔记同步助手/2026-11-21/吴文煜分享的工具 · 方法 · 资料索引]]
- [[笔记同步助手/2026-11-22/在 Herdr 中用 hc 创建 Pi 子 Agent]]
- [[笔记同步助手/2026-11-23/10 个能把 AI 味压下去的技能：]]
- [[笔记同步助手/2026-11-23/7 skills para que tu agente de IA anime interfaces como un pro]]
- [[笔记同步助手/2026-11-23/AI 时代的六边形能力模型：普通人如何保持不可替代性]]
- [[笔记同步助手/2026-11-23/GitHubDaily- 做产品落地页时，想放一段动画讲清楚功能，找设计师太贵，自己又不会画，最后只能堆几]]
- [[笔记同步助手/2026-11-23/Mian🍜- 本周GitHub神级项目🤯🤯👍 第一名一个月涨了4w6 光是治AI审美的就]]
- [[笔记同步助手/2026-11-23/Un diseñador dice que duplicó la conversión de 3 SaaS rediseñando su web con Cla]]
- [[笔记同步助手/2026-11-23/fast-anything：自动定位性能瓶颈，重写关键代码实现性能跃升]]
- [[笔记同步助手/2026-11-23/从 0 到 1 用 Vibe Coding 构建 OilBook AI 知识库：产品设计、技术选型、内容生产与上线复盘]]
- [[笔记同步助手/2026-11-23/如果你平时用 AI 做设计，这几个网站你一定要看看👇：]]
- [[笔记同步助手/2026-11-23/如何快速进入一个陌生行业？我把哈佛五力模型拆成 9 个 AI 提示词，3 天摸清任何行业底细]]
- [[笔记同步助手/2026-11-23/用 Codex 或 Claude 制作电影感动画、视频与动态设计：18 个 GitHub 项目工具清单]]

## 待核实

- [ ] Google `Modern Web Guidance` 的仓库地址与 56%→88% 的评测口径。
- [ ] Anthropic《Claude Code 实践》PDF 的官方地址。
- [ ] Diagram Design、OpenFilm、GSAP/Three.js/Blender MCP/ComfyUI 的具体仓库（原文仅口述，无链接）。
- [ ] Chrome WebMCP 的规范状态（原文称"Chrome 推出"，未见版本号）。
- [ ] 免费额度条款是否仍与 2026-11 笔记一致（Cloudflare / Supabase / Neon / Clerk / Resend）。
- [ ] 是否要为这批笔记补建 `wiki/sources/` 来源摘要页；当前本页直接链接 Raw 原文。
