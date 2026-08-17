# Phistory - AI 代理系统提示追踪工具

> 追踪流行编码代理 CLI（如 Claude Code、Codex、Kimi、opencode、OpenClaw、Hermes 和 Pi）的系统提示变化

## 📌 项目概述

**Phistory** 是一个自动归档工具，用于追踪和比较不同 AI 编码代理的系统提示（System Prompt）随时间的变化。它通过捕获每个代理版本的提示快照，帮助开发者理解代理设计如何通过提示、工具、策略和运行时指令进行迭代。

**在线查看器：** [phistory.cc](https://phistory.cc/)

## 🎯 核心用途

### 1. 追踪代理设计演变
- 观察 Anthropic、OpenAI 等代理构建者如何迭代系统提示
- 发现新工具、权限检查、模型默认值和用户确认规则的添加时间
- 比较不同 CLI 如何构建代理行为、工具使用和开发者约束

### 2. 研究与调试支持
- 在文章、研究笔记、审计或调试报告中引用稳定的提示快照
- 分析代理行为变化背后的设计决策

## 🔧 工作原理

对于每个支持的版本，Phistory 执行以下流程：

1. **安装** 精确的 CLI 包
2. **运行** 一次通过 `claude-tap`（无需调用真实模型提供商）
3. **捕获** 承载提示的 HTTP 请求
4. **存储** 结果到 `captures/<agent>/<version>/` 目录，包含：
   - `prompt.md` - 系统提示内容
   - `trace.jsonl` - 追踪数据
   - `meta.json` - 元数据

对于最近的 Claude Code 版本，还会提取静态提示字符串并存储为：
- `static-prompts.md`
- `static-prompts.json`
- `static-candidates.json`

**自动化：** GitHub Actions 每小时检查支持的 CLI 版本，当新版本出现时自动提交新的快照。

## 📊 支持的代理

| 代理 | 包名 | 最新版本 | 捕获数量 | 最后捕获时间 |
|:---:|:---|:---|:---:|:---|
| **Claude Code** | `@anthropic-ai/claude-code` | 2.1.186 | 347 | 2026-06-22 |
| **Codex CLI** | `@openai/codex` | 0.142.0 | 57 | 2026-06-22 |
| **Hermes Agent** | `hermes-agent` | v2026.6.19 | 16 | 2026-06-19 |
| **Kimi CLI** | `MoonshotAI/kimi-cli` | 1.48.0 | 20 | 2026-06-22 |
| **OpenClaw** | `openclaw` | 2026.6.9 | 65 | 2026-06-21 |
| **opencode** | `opencode-ai` | 1.17.9 | 75 | 2026-06-21 |
| **Pi** | `@earendil-works/pi-coding-agent` | 0.79.10 | 24 | 2026-06-22 |

## 🚀 本地开发

### 环境准备

```bash
# 安装锁定的开发环境
uv sync --all-groups
```

### 常用命令

```bash
# 捕获最新的支持代理版本
uv run phistory capture --latest --agents claude-code,codex,openclaw,hermes,kimi,opencode,pi

# 捕获特定代理的历史版本范围
uv run phistory backfill claude-code --from 2.1.113 --to latest

# 重建最近 10 个捕获的 Claude Code 版本的静态提示文件
uv run phistory extract-static claude-code --latest-captured 10

# 重新生成 README.md、README_zh.md、docs/captures.md 和 captures/index.json
uv run phistory render-index

# 重新生成静态网页查看器 index.html
uv run phistory render-site
```

## 💡 使用场景

### 对于 AI 开发者
- **追踪行业趋势**：了解主要代理构建者的提示设计演变
- **借鉴最佳实践**：分析不同代理的工具和策略设计
- **调试参考**：当代理行为变化时，查看提示变化找到原因

### 对于研究人员
- **系统研究**：分析 AI 代理设计模式的演变
- **论文引用**：引用特定版本的提示快照作为研究证据
- **比较分析**：对比不同代理的提示设计策略

### 对于普通用户
- **了解变化**：知道你的 AI 工具更新了哪些重要功能
- **选择参考**：通过提示设计了解不同代理的特点

## 🔍 项目结构

```
phistory/
├── captures/           # 捕获的提示快照
│   ├── claude-code/   # Claude Code 版本
│   ├── codex/         # Codex CLI 版本
│   ├── hermes/        # Hermes Agent 版本
│   ├── kimi/          # Kimi CLI 版本
│   ├── openclaw/      # OpenClaw 版本
│   ├── opencode/      # opencode 版本
│   └── pi/            # Pi 版本
├── phistory/          # 主程序代码
├── tests/             # 测试文件
├── docs/              # 文档
├── index.html         # 静态网页查看器
└── pyproject.toml     # Python 项目配置
```

## 📈 项目数据

- **Stars**: 28
- **Forks**: 5
- **主要语言**: Python (51.8%), HTML (48.2%)
- **创建时间**: 2026-05-21
- **最后更新**: 2026-05-24

## 🔗 相关资源

- **GitHub 仓库**: [WEIFENG2333/phistory](https://github.com/WEIFENG2333/phistory)
- **在线查看器**: [phistory.cc](https://phistory.cc/)
- **依赖工具**: [claude-tap](https://github.com/liaohch3/claude-tap) - 用于捕获系统提示

## 🎓 学习价值

### 技术学习
1. **Python 自动化**：学习如何使用 Python 进行自动化捕获和处理
2. **GitHub Actions**：了解如何设置定时任务和自动化工作流
3. **Web 开发**：查看静态网站生成和提示比较界面的实现

### AI 领域学习
1. **系统提示设计**：了解 AI 代理的系统提示结构和设计原则
2. **代理架构**：通过提示变化理解代理架构的演变
3. **工具集成**：学习 AI 代理如何集成和管理工具

## 📝 个人使用笔记

### 安装步骤
```bash
# 1. 克隆仓库
git clone https://github.com/WEIFENG2333/phistory.git
cd phistory

# 2. 安装依赖
uv sync --all-groups

# 3. 运行捕获
uv run phistory capture --latest
```

### 常见问题
- **网络问题**：确保网络连接正常，能够访问 GitHub
- **依赖问题**：使用 `uv sync` 而不是 `pip install`
- **版本兼容**：确保 Python 版本符合要求

## 🚀 未来探索

- [ ] 尝试本地运行捕获命令
- [ ] 分析特定代理的提示变化历史
- [ ] 比较不同代理的工具设计模式
- [ ] 了解系统提示的最佳实践

---

**更新时间**: 2026-06-23  
**项目版本**: 最新（main 分支）  
**本地位置**: `E:\DATA\github-kb\Personal-Knowledge-Base\Personal-Knowledge-Base\phistory`