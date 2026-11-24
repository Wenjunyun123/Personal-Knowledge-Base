# 个人网站 × FDE：执行手册

> 2026-11-24 版。每个工具都读过它的 README / SKILL.md 才写进来；冲突结论基于实际装法和实际体积，不是猜的。

---

## 〇、结论先说：三个设计 skill，只能装两个

| 工具 | 它实际是什么 | 装法 | 体积 | 冲突 |
| --- | --- | --- | --- | --- |
| **Impeccable** | 审稿人。24 个命令（critique / audit / polish / bolder…）+ 62 条**确定性规则**（不调大模型）+ CLI + 编辑时 hook + 浏览器内 live 模式。会写 `PRODUCT.md` / `DESIGN.md` | `npx impeccable install`，重载后 `/impeccable init`（Codex 用 `$impeccable init`） | 主 SKILL 13.7 KB，其余按需加载 | 不建站、自带 0 套设计方向 → **和谁都不抢方向盘** |
| **Hallmark** | 发牌人。50 套"材质主题"，一次发 3 套；新建页面产出**自包含 HTML/CSS**；`/hallmark redesign <path>` 保内容改设计；`/hallmark audit` 只报告；自带 sloplint + 8 个宽度渲染检查 | `npx skills add nutlope/hallmark -g`；渲染检查另需 `npm i -g puppeteer-core` + Chrome | 18.2 KB | 与 Taste Skill **建站阶段互斥** |
| **Taste Skill** 2.5.1 | 发牌人 + 整站系统。先给业务分类（software/gaming/tech/product/service/place），发色板+字体+首屏版式，从 `assets/starter.html` + `system.css` 起站；4 宽度检查 + Stop hook 闸门 | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` | 31 KB（三者最大） | 与 Hallmark **建站阶段互斥** |
| **Uizze**（十条清单里的"Anti UI Slop"） | 不是 skill，是**参考库**：搜真实界面、有 MCP、有 UI Prompt Builder，标语"Show AI what good looks like"。完整功能要登录/付费 | 不用装，当网站用 | — | 无冲突 |
| **MengTo/Skills** | 不是设计系统，是**一堆单项 SKILL.md**：视频→超详细 prompt、整页截图、HTML→交互 prompt、3D、插画 | 按需拷单个文件夹 | 每条很小 | 无冲突，按名字调用 |

**一句话选型**：
- 你要**多页整站 + 现有 Next/React 项目** → 用 **Taste Skill**（它明说支持 React / Next / Vue / Svelte / Astro / Tailwind）。
- 你要**一页作品集 / 想快速看不同"材质"** → 用 **Hallmark**（它生成自包含 HTML/CSS，主题是"材质不是版式"，同一主题两个 prompt 出两个不同页面）。
- **Impeccable 无论选谁都装**，它只评判、微调、生成 `DESIGN.md`，不发牌。

**三种真冲突，别忽略**：
1. **方向盘冲突**：Hallmark 和 Taste 都会"发牌"（一个发主题材质，一个发色板/字体/首屏版式）。两个同时装，agent 可能在一个页面里混两套系统，左右边距、字阶、卡片结构都会打架。
2. **检查器重复**：Impeccable 62 条规则 + Hallmark sloplint + Taste 的 gate 跑的都是"AI 味"，三份报告互相矛盾时你会不知道听谁的。
3. **hook 叠加**：Impeccable 有编辑时设计 hook，Taste 有 Stop 闸门 hook，Hallmark 可选装 edit-time Floor。三个一起开 = 每次改一个文件被拦三次。**只留一个 hook。**

---

## 一、今天只做一件事：把 Impeccable 装上（30 分钟）

```bash
npx impeccable install          # 检测你的编辑器，问项目级还是全局，问要不要装设计 hook → 装
# 重载编辑器
/impeccable init                # 回答几个问题，写出 PRODUCT.md（给谁做、要干什么、约束）
/impeccable document            # 读你现在的代码，把现有视觉系统写成 DESIGN.md
npx impeccable detect .         # 62 条规则扫一遍，输出问题清单
```

- **为什么先装它**：它顺手把 `DESIGN.md` 生成了——我上次让你手写的那份，现在一条命令就有，而且是**从你现有代码里读出来的**，不是拍脑袋。
- **今天不装另外两个**：先把基线量出来，不然你不知道后面换皮到底好了多少。
- Windows 提示：没有 `sh` 的终端用 `impeccable.cmd`；扫描线上页面直接 `npx impeccable detect https://你的域名`（用本机 Chrome 渲染，能查出对比度、字号过小这类源码看不出的问题）。
- 如果它误报你的品牌字体：`npx impeccable ignores add-value overused-font Inter --reason "Brand font"`。

**这一步的产出**：一份按严重度排序的问题清单 + 一份真实的 `DESIGN.md`。这就是你今天"看到的效果"。

---

## 二、第二个装谁：拿你自己的一个页面做对照（各 30 分钟）

别听我说，跑两个对照：

| | Hallmark | Taste Skill |
| --- | --- | --- |
| 跑法 | `/hallmark redesign ./你的页面路径`（保内容、保留接线） | 让它按 starter 重做同一页 |
| 你会得到 | 三种"材质"里挑一种，整页换气质 | 一套色板 + 字体配对 + 首屏版式，整站可用 |
| 多页一致性 | 主题是材质，多页要自己保持一致 | starter + system.css 天生一套系统 |
| 框架友好度 | 新页面是自包含 HTML/CSS，接进 Next 要拆 | 直接支持 Next/React/Tailwind |
| 上下文成本 | 18 KB | 31 KB |
| 额外依赖 | Chrome + puppeteer-core（不给就只跑静态检查） | Node 22+ + Chrome |

**判据只有三条**：① 你的站是单页还是多页；② 现有代码是不是 React/Next；③ 你更缺"气质"还是更缺"系统"。
**试完必须删一个**（项目级只留一个；全局可以都留着，靠名字调用）。

---

## 三、逐条说"哪部分要用、哪部分先别碰"

### Impeccable（24 个命令，个人站只用 7 个）

| 用 | 干什么 | 什么时候 |
| --- | --- | --- |
| `init` | 写 `PRODUCT.md` | 第一天，一次 |
| `document` | 写 `DESIGN.md` | 第一天，一次 |
| `detect`（CLI） | 62 条规则扫 AI 味/对比度/间距 | 每次提交前，可进 CI |
| `critique` | 按可用性启发式打分并排优先级 | 改版前后各一次 |
| `polish` | 上线前最后一轮打磨 | 发布前 |
| `bolder` / `quieter` | 太保守就加强，太吵就收敛 | 看着"说不上哪里不对"时 |
| `typeset` / `layout` | 只修字阶或只修间距 | 当你已经知道问题在这两项 |

先别碰：`live`（要跑 dev server + 会调你的 chat agent，路熟之前别开）、`overdrive`（shader/弹簧/滚动特效，个人站最容易过度）、`onboard`/`adapt`/`harden`（等有真实用户和表单再说）。

### Hallmark（50 套主题，只用 3 套）

- 让它**发 3 套**，你选 1 套，不要翻完 50 套——翻完只会更纠结。
- 主题 ≠ 版式：同一主题写两个 prompt 会出两个不同页面，所以定稿后把选中的主题文件（`references/themes/*`，每个 ≤8 KB）留在项目里当"材质卡"。
- `custom` 模式只在"三套都不像你"时用，它会丢掉主题、只按你的 prompt 找一个"只有你有的点子"。
- `/hallmark audit` 只报告，适合给别人（或给客户）的页面做体检。
- 注意：新页面是**自包含 HTML/CSS**。你要接进 Next，让它先 redesign 现有页面，别让它从零生成整站。

### Taste Skill（31 KB，别全量吃）

- 它按业务类型决定强度：`software/tech/gaming` 才发 shader、滚动场景、3D；`product/service/place` 只给照片+字体。**个人站如果不做技术感，就走后者**，省得满屏 WebGL。
- 真正值钱的是三样：`assets/starter.html`（一屏一节的骨架）、`assets/system.css`（左右边距对齐、固定导航、收尾 footer）、`scripts/gate.mjs`（4 个宽度 + 真实浏览器检查，最多三轮）。
- 不要用它的 3D/插画资产，除非你的站是游戏或技术产品——那是给 tech 页准备的。

### Uizze（不是 skill）

只当"看图说话"的弹药：定方向前搜 2–3 个真实界面，把截图丢给 agent 说"按这个的信息密度和留白改，不要照抄配色"。它给的是**参照**，不是规则——别指望它替你判断。

### MengTo/Skills（按需取一条）

- `video-to-superprompt`：把别人的站录屏 → 转成超详细 prompt（拆解竞品最快的方式）
- `stitched-full-page-capture`：整页长截图，看别人的信息节奏
- `illustration`：需要插画时，14 种 SVG 风格
- 其余 3D / 游戏 / 媒体：与你现在的站无关，别装

---

## 四、三天落地（每天 1 小时）

- **Day 1**：`npx impeccable install` → `/impeccable init` → `/impeccable document` → `npx impeccable detect .`，把清单存成 `baseline.md`。
- **Day 2**：选一个页面（首页或项目页），跑 Hallmark `redesign` 或 Taste 重做，二选一，截图对照，定方向。删掉没选的那个的**项目级**安装。
- **Day 3**：用 Impeccable 的 `critique` 打分 → `typeset`/`layout`/`bolder` 收敛 → `polish` → `detect` 复查，commit。把 `DESIGN.md` 的变更写进去。

**验收**：`detect` 的问题数比 `baseline.md` 少一半；同一页在 1440 / 768 / 390 三个宽度截图没有错位。

---

## 五、网站线其余环节（工具已核对）

| 任务 | 用什么 | 怎么用 |
| --- | --- | --- |
| 讲清一个功能 | [stick-scene](https://github.com/nilbuild/stick-scene) | "读我的项目，给 2 个火柴人场景创意" → 选一个，它逐帧渲染检查重叠 |
| 首屏动效 | [Motion](https://github.com/motiondivision/motion) | 先写"哪个属性、多久、什么触发"，再实现；不许 `transition: all` |
| 3D / 动态区块 | [motionsites.ai](https://motionsites.ai/) | 800+ 提示词，挑 1 个用在 1 处，别全站铺 |
| 文案去 AI 味 | [humanizer-zh](https://github.com/op7418/humanizer-zh) | 所有中文文案过一遍 |
| 字体出处 | [fontinlogo.com](https://fontinlogo.com/) | 查你喜欢的品牌用什么字体 |
| 部署 | Cloudflare Pages + Neon + Resend | 一句话："把项目部署到 Cloudflare Pages，数据库用 Neon" |
| 收费 | Stripe + 服务端裁剪 | 付费内容在服务端裁，前端遮挡等于没做 |

免费额度（原文称，2026-11 快照）：Pages 不限带宽可商用 / Workers 10 万请求每天 / D1 5 GB / R2 10 GB；Neon 免费不限项目数；Supabase 500 MB 库 + 1 GB 存储 + 5 万 MAU；Clerk 5 万 MAU；Resend 100 封/天（需自有域名）。

---

## 六、FDE 线：照抄现成流程

- **官方五课**（飞书，需登录）：第 1 课《7 分钟搞懂什么是 FDE》 https://bytedance.larkoffice.com/file/PAJTbmeZJowrRoxqW51cC60nn5f ｜第 2 课《伙伴 FDE 每天都在做什么》 https://bytedance.larkoffice.com/file/Tnbmbug7zokSMVxze5PcwtnOn7q ｜第 3 课《飞书、豆包产品全景地图》 https://bytedance.larkoffice.com/file/MOWybWSIAo0KCIxx3ktcTN7Jn8c ｜第 4 课《FDE 的一天》 https://bytedance.larkoffice.com/file/W99JbZQWFoed12x7TVAcWLaVnpf ｜第 5 课《需求诊断》 https://bytedance.larkoffice.com/file/YKhDbC6kRo4ntkxysoCcmivqn0O
- **第 5 课当 SOP**：进门前 3 项准备 → 45 分钟问 5 个问题再追问 → 场景打分挑第一个 → 写诊断记录。
- 需求对齐 → [mattpocock/skills](https://github.com/mattpocock/skills) 的 `grill-me`（开工前让它反过来拷问你）
- 行业摸底 → [[笔记同步助手/2026-11-23/如何快速进入一个陌生行业？我把哈佛五力模型拆成 9 个 AI 提示词，3 天摸清任何行业底细|哈佛五力 9 提示词]]
- 交付审查 → [cloudflare/security-audit](https://github.com/cloudflare/security-audit-skill)（新 Agent 专门推翻上一个结论）
- 桌面自动化 → [agent-desktop](https://github.com/vercel-labs/agent-desktop)
- 把网站当客户项目跑一遍的完整参照 → [[笔记同步助手/2026-11-23/从 0 到 1 用 Vibe Coding 构建 OilBook AI 知识库：产品设计、技术选型、内容生产与上线复盘|OilBook 复盘]]

---

## 七、案例线：抄一条记一条

- [[笔记同步助手/2026-11-23/Mian🍜- 本周GitHub神级项目🤯🤯👍 第一名一个月涨了4w6 光是治AI审美的就|Mian 的 GitHub 周榜]]：每周只挑一个，装进项目用一次
- [[笔记同步助手/2026-11-23/用 Codex 或 Claude 制作电影感动画、视频与动态设计：18 个 GitHub 项目工具清单|18 个项目清单]]：做视频时按目标查表
- [[笔记同步助手/2026-11-23/如果你平时用 AI 做设计，这几个网站你一定要看看👇：|8 个设计站]]：没灵感才打开
- 记录三行：解决什么 / 用在哪 / 改了什么。两周没用到就删。

---

## 八、harness 线：让项目可托管

| 层（越下越可靠） | 做法 |
| --- | --- |
| 代码与 API | 让正确用法最自然：目录隔职责、导出面收窄 |
| lint / 类型 / 测试 | 每次纠正 AI，先问"能不能变成一条规则" |
| 运行时验证 | 给 agent 一份"功能映射"清单 + 用 CDP/Playwright 自己点一遍截图 |
| 文字规则 | `AGENTS.md` 只放需要判断力的要求 |

- 禁掉约 99% 的注释：注释不能被执行，还会被 agent 用来给临时补丁辩护。
- 工作台：[Orca](https://github.com/stablyai/orca)、[T3 Code](https://github.com/pingdotgg/t3code)、[[笔记同步助手/2026-11-22/在 Herdr 中用 hc 创建 Pi 子 Agent|Herdr Pi 子 Agent]]
- 额度：[Magpie](https://github.com/yetone/magpie)

---

## 九、AI 视频线：先出片

1. **60 秒讲解片** → [HyperFrames](https://github.com/heygen-com/hyperframes)：写 HTML/CSS/GSAP 导 MP4，19 个按项目顺序排好的 skill
2. **产品演示/动态信息图** → [Remotion](https://github.com/remotion-dev/remotion) + [Remotion Skills](https://github.com/remotion-dev/skills)
3. **落地页小场景** → stick-scene
4. **真人出镜太重** → 先录屏 + 配音；真要做数字人再看[[笔记同步助手/2026-11-23/玩转实时数字人直播 - 免显卡保姆级教程|免显卡教程]]

---

## 十、节奏

周一一个改造（30 分钟能看到差别）／周三一个补课（FDE 一课或一次 lint 化）／周五 30 分钟三问：做完没验收的是哪件、哪个纠正出现第三次、下周删什么。

每两周测一次规范：**换一个全新会话的 agent，只读 `PRODUCT.md` + `DESIGN.md` + `AGENTS.md`，能不能第一次就做对。**

---

## 依据

- [[笔记同步助手/2026-11-20/用 AGENTS.md 约束 Codex，减少前端设计中的 AI Slop]]
- [[笔记同步助手/2026-11-20/别人的代码都是垃圾：如何用 Agent 环境与验证机制支撑单月 3000 个 PR]]
- [[笔记同步助手/2026-10-04/最火AI岗位FDE：月薪5万，都干这些…]]
- [[笔记同步助手/2026-11-21/吴文煜分享的工具 · 方法 · 资料索引]]
- [[笔记同步助手/wiki/topics/AI 前端设计与交付实践路线]]
