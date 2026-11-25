# life/ 生活数据化

> 目标：每天的生活点滴留下可回溯的记录，AI 能直接读、直接分析、直接给建议。
> 原则：**不加新 App、不加服务器、不加第四套同步。** 全部塞进已有的 Obsidian 仓库，靠你现成的 GitHub 同步跑。

---

## 一、为什么是这个架构

你现在已经有的三件事，恰恰是这套系统的全部基建：

| 你已有的 | 在本系统里的角色 |
| --- | --- |
| Obsidian（三端同步 + GitHub） | **唯一的数据库和唯一的传输管道** |
| `obsidian-git` 自动 commit | 手机写的 → 自动进 GitHub → 电脑拉下来 |
| AI 能读本地文件夹 | **不需要"接入 API"，AI 读文件就是最强的分析入口** |

所以缺的从来不是工具，是两件事：**一个统一格式**，和**一个 15 秒能完成的录入入口**。

---

## 二、数据流

```
手机（快捷指令 / 微信 / 系统健康）
        │  写入一行文本
        ▼
life/inbox/2026-11-25.md      ← 人能看懂，Obsidian 原生支持追加
        │  obsidian-git 自动 commit → GitHub
        ▼
电脑 ~/Personal-Knowledge-Base/life/inbox/
        │  python scripts/life.py ingest
        ▼
life/data/2026-11.jsonl       ← 机器格式，append-only，一行一条
        │
        ├─→ life.py week     → 周报到 life/reports/（给你看）
        └─→ AI 直接读        → 分析、找相关性、给决策
```

**为什么中间隔一层 inbox**：手机端只能可靠地追加 Markdown（Obsidian URI 天生支持），但 Markdown 不是机器格式。所以手机上写"人话"，电脑上转成 JSONL。转换由脚本做，你永远不用手碰 JSON。

---

## 三、录入渠道（按摩擦力从低到高）

### 1. 手机快捷指令 → Obsidian URI（主力，15 秒）

一行 `obsidian://new` URL 就能往当天 inbox 追加：

```
obsidian://new?vault=Personal-Knowledge-Base&file=life/inbox/2026-11-25&append=true&content=<URL编码后的一行>
```

- **iOS**：快捷指令 App → 新建"记一下" → 「从菜单中选取」（体重/饮食/睡眠/情绪/消费/学习）→ 「要求输入」（数字或文字）→ 「文本」拼出行 → 「打开 URL」。再把它加到**锁屏小组件 / 背面轻点 / 主屏**。
- **Android**：MacroDroid 或 HTTP Shortcuts 组一个"打开 URL"动作，或者 Termux 直接 `echo >> path`。

### 2. 微信 → 现有笔记同步助手（你已经会了）

刷到什么、想到什么，发给同步助手 → 进 `笔记同步助手/YYYY-MM-DD/`。
**这类是"素材"，不是"指标"**，别混进 life 的 data 里——两者用途不同，混了 AI 分析会失焦。

### 3. 系统自动源（日/周批量，不占你注意力）

| 数据 | 来源 | 落地方式 |
| --- | --- | --- |
| 睡眠 / 步数 / 心率 / 体重 | iOS「健康」/ Android「Health Connect」 | iOS 用 **Health Auto Export** 导出，Android 用 Health Sync；每周导一次到 `life/import/` |
| 消费 | 支付宝 / 微信账单 | 每月导出 CSV → `life/import/` |
| 时间去向 | 手机「屏幕使用时间」/ 数字健康 | 每周截图丢进 `life/import/`，AI 读图 |
| 体重（若不自动） | 智能秤 App | 秤完顺手快捷指令记一条，10 秒 |

### 4. 饮食：别指望全自动

现实是：拍照 → AI 估算热量，误差 20%+；手动记 → 一周就放弃。**建议做法**：

- 只记"**值得记的那顿**"和"**破例的那次**"，不记每一口。
- 快捷指令选一个"饮食"菜单项 → 输入一句话（"牛肉面 + 拿铁"）→ 结束。
- 每周让 AI 结合体重趋势反推：真正影响你的是哪 2–3 个习惯，而不是每天多少卡。

---

## 四、inbox 行格式（唯一需要记的规则）

```
- HH:MM | 领域 | 数值 | 备注
```

例：

```
- 07:20 | 体重 | 72.4 kg | 起床后空腹
- 12:30 | 饮食 | 牛肉面+拿铁 | 外食
- 23:10 | 睡眠 | 6.5 h | 1:20 才睡
- 21:00 | 情绪 | 7/10 | 投完 3 家
- 20:40 | 学习 | 90 min 前端 | 做完个人站首页
```

规则只有三条：

1. 竖线分隔，四段，**字段顺序不能变**（备注可空）。
2. 数值那一段可以带单位，也可以带多个数字。
3. 领域名尽量复用已有词，别每天发明新词（见 `schema.md`）。

---

## 五、每天怎么用

| 时机 | 动作 | 耗时 |
| --- | --- | --- |
| 随发生随记 | 锁屏快捷指令 → 选领域 → 填 → 完成 | 15 秒 |
| 睡前 | 一条「睡眠」「情绪」 | 30 秒 |
| 周末在电脑上 | `python life/scripts/life.py ingest && python life/scripts/life.py week` | 1 分钟 |
| 每周一次 | 把 `life/reports/` 最新周报丢给 AI，问"这周有哪 3 个发现、下周该做哪 1 个实验" | 5 分钟 |

---

## 六、三条硬规矩（违反必死）

1. **只采集 3 个指标起步。** 推荐：体重、睡眠、情绪。三个月后数据有形状了再加。一次上十个域，两周后你就不记了。
2. **不做看板。** 不要 Grafana、不要 InfluxDB、不要仪表盘。等到你有 3 个月连续数据、且真的每周在看周报，再考虑可视化。
3. **append-only。** 永远不改历史记录。记错了就再记一条"修正"。

---

## 七、这台机器上的入口

| 用途 | 命令 |
| --- | --- |
| 解析手机写进 inbox 的内容 | `python life/scripts/life.py ingest` |
| 电脑上顺手记一条 | `python life/scripts/life.py add 体重 72.4 kg --note 空腹` |
| 看今天 | `python life/scripts/life.py today` |
| 生成周报 | `python life/scripts/life.py week` |
| 检查哪天断记 | `python life/scripts/life.py check` |
