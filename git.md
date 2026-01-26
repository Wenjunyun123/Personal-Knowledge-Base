# Git 工作流程 - 笔记提交指南

> 每次完成笔记后的标准 Git 提交流程

## 📋 完整流程（推荐）

```bash
# 1️⃣ 查看当前状态 - 了解有哪些变更
git status

# 2️⃣ 查看具体变更内容 - 确认修改了什么
git diff              # 查看未暂存的变更
git diff --staged     # 查看已暂存的变更

# 3️⃣ 添加文件到暂存区
# 方式1: 添加所有变更（包括删除的文件）
git add -A

# 方式2: 添加特定文件或文件夹
git add "文件路径/文件名.md"
git add "文件夹名/"

# 方式3: 添加所有修改和新文件，不包含删除的文件
git add .

# 4️⃣ 提交变更 - 写清晰的提交信息
git commit -m "feat: 添加XX笔记内容"

# 5️⃣ 推送到远程仓库
git push origin main

# 6️⃣ 确认推送成功
git status
```

---

## 🎯 提交信息规范（Conventional Commits）

使用前缀明确提交类型：

| 前缀 | 说明 | 示例 |
|:---:|:---|:---|
| `feat:` | 新功能 | `feat: 添加深度学习简介笔记` |
| `fix:` | 修复问题 | `fix: 修正公式错误` |
| `docs:` | 文档更新 | `docs: 更新README` |
| `style:` | 格式调整 | `style: 统一代码格式` |
| `refactor:` | 重构 | `refactor: 优化代码结构` |
| `chore:` | 杂项 | `chore: 更新依赖` |

### 提交信息格式

```bash
# ✅ 好的提交信息
git commit -m "feat: 添加PyTorch张量操作笔记"
git commit -m "fix: 修正神经网络公式错误"
git commit -m "docs: 更新学习路线图"

# ❌ 不好的提交信息
git commit -m "update"
git commit -m "fix bug"
git commit -m "a"
```

---

## 🚀 快速工作流（常用命令）

### 添加单个新笔记

```bash
git add "机器学习-ML/新笔记.md"
git commit -m "feat: 添加新笔记"
git push origin main
```

### 添加整个文件夹的新笔记

```bash
git add "深度学习-DL/"
git commit -m "feat: 添加深度学习day01-day06笔记"
git push origin main
```

### 修改已有笔记

```bash
git add -A
git commit -m "fix: 修正线性回归公式错误"
git push origin main
```

---

## 🔍 常用 Git 命令

### 查看类

```bash
git status              # 查看工作区状态
git log                 # 查看提交历史
git log --oneline       # 简洁查看历史
git diff                # 查看未暂存的修改
git diff --staged       # 查看已暂存的修改
git log --graph         # 图形化显示分支历史
```

### 撤销类（谨慎使用）

```bash
# 撤销未暂存的修改
git checkout -- 文件名.md

# 撤销已暂存的修改
git reset HEAD 文件名.md

# 撤销最后一次提交（保留修改）
git reset --soft HEAD~1

# 撤销最后一次提交（丢弃修改）
git reset --hard HEAD~1

# 回退到指定提交（丢弃之后的所有修改）
git reset --hard <commit-hash>
```

### 分支类

```bash
git branch              # 查看本地分支
git branch -a           # 查看所有分支
git checkout -b 新分支名  # 创建并切换到新分支
git checkout 分支名      # 切换分支
git merge 分支名        # 合并分支
git branch -d 分支名     # 删除已合并的分支
```

---

## ⚠️ 常见问题解决

### 问题1: Push 失败（远程有新提交）

```bash
# 先拉取远程最新代码
git pull origin main

# 如果有冲突，解决冲突后再提交
git add .
git commit -m "解决合并冲突"
git push origin main
```

### 问题2: 提交信息写错了

```bash
# 修改最后一次提交信息（未推送）
git commit --amend

# 修改已推送的提交信息（需要强制推送）
git commit --amend
git push -f origin main  # ⚠️ 强制推送，谨慎使用
```

### 问题3: 添加了错误的文件

```bash
# 取消暂存
git reset HEAD 错误文件.md

# 如果已提交，回退
git reset --soft HEAD~1
git reset HEAD 错误文件.md
```

### 问题4: 想要修改之前的提交

```bash
# 交互式变基（修改最近的3个提交）
git rebase -i HEAD~3

# 在编辑器中将 pick 改为 edit，保存后修改
git add .
git rebase --continue
```

---

## 📝 推荐的工作习惯

### ✅ DO（建议做的）

1. **每次完成一个主题就提交一次**
   - 不要攒一堆笔记一次性提交
   - 每个提交应该是一个完整的逻辑单元

2. **写清晰的提交信息**
   - 使用前缀（feat/fix/docs等）
   - 简短描述做了什么
   - 如有必要，添加详细说明

3. **Push 前检查 status**
   ```bash
   git status  # 确认要提交的文件
   git diff    # 查看具体变更
   ```

4. **定期拉取远程更新**
   ```bash
   git pull origin main
   ```

5. **使用 `.gitignore` 忽略临时文件**
   ```
   # 忽略临时文件
   .DS_Store
   Thumbs.db
   *.tmp
   *.bak
   ```

### ❌ DON'T（避免做的）

1. **不要提交敏感信息**
   - 密码、密钥、个人信息

2. **不要忽略冲突**
   - 遇到冲突要仔细解决
   - 不要随意使用强制推送

3. **不要频繁修改历史提交**
   - 修改已推送的历史会造成问题
   - 新手慎用 `git push -f`

4. **不要在主分支上做实验**
   - 重要操作前创建备份分支

---

## 🎓 实战示例场景

### 场景1: 完成一门课程的所有笔记

```bash
# 完成第1节笔记
git add "机器学习-ML/一、机器学习概述.md"
git commit -m "feat: 添加机器学习概述笔记"
git push origin main

# 完成第2节笔记
git add "机器学习-ML/二、KNN算法.md"
git commit -m "feat: 添加KNN算法笔记"
git push origin main

# ...以此类推
```

### 场景2: 修正多个笔记中的错误

```bash
# 修正完成后，一次性提交
git add -A
git commit -m "fix: 修正多处公式错误"
git push origin main
```

### 场景3: 添加新文件夹和多个笔记

```bash
# 添加整个深度学习文件夹
git add "深度学习-DL/"
git commit -m "feat: 添加深度学习day01-day06笔记"
git push origin main
```

### 场景4: 修改文件夹结构

```bash
# 移动文件后，查看状态
git status

# 添加所有变更（包括移动）
git add -A
git commit -m "refactor: 重新组织文件夹结构"
git push origin main
```

---

## 📚 快速参考卡片

```
完整流程（背诵）：
git status → git add -A → git commit -m "type: message" → git push origin main

查看状态：git status
查看历史：git log --oneline
撤销修改：git checkout -- file
撤销暂存：git reset HEAD file
强制推送：git push -f origin main（慎用！）
```

---

## 🔧 Git 配置

### 设置用户信息（仅需一次）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### 设置默认分支名称

```bash
git config --global init.defaultBranch main
```

### 查看配置

```bash
git config --list
```

---

## 💡 进阶技巧

### 1. 使用别名简化命令

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD'
git config --global alias.last 'log -1 HEAD'
```

### 2. 彩色输出

```bash
git config --global color.ui true
```

### 3. 自动推送

```bash
# 推送到所有跟踪的分支
git push
```

---

## 🎯 最佳实践总结

| 习惯 | 原因 |
|:---|:---|
| **频繁提交** | 减少冲突，便于回滚 |
| **清晰信息** | 便于追溯和理解 |
| **推送前检查** | 避免错误提交 |
| **定期拉取** | 保持代码同步 |
| **善用分支** | 隔离实验性改动 |

---

**🚀 记住：提交是为了自己，而不是为了别人。**
**良好的 Git 习惯会让你受益终生！**
