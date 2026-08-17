# 知识库变更日志

> 本文件只在末尾追加。记录日期、资料范围、新建页、更新页、验证证据与待人工确认事项。

## 2026-08-10 — 初始化三层知识库并完成首篇入库

- 资料范围：[[笔记同步助手/2026-08-10/用 Codex + Obsidian 搭建自生长的个人知识库实战]]。
- 原文 SHA-256：`5BC9D613481CB207226E3B2DD954EB5F03958500527D5103B8D025EBFBEB3C72`。
- 初始盘点：27 个日期目录、143 个 Markdown 文件、369 个 `images/` 附件；本次未移动或改写这些历史 Raw。
- 新建 Schema：`AGENTS.md`、`index.md`、`log.md`、`workflows/` 与只读校验脚本。
- 新建来源摘要：[[笔记同步助手/wiki/sources/用 Codex + Obsidian 搭建自生长的个人知识库实战]]。
- 新建概念页：[[笔记同步助手/wiki/concepts/LLM Wiki]]、[[笔记同步助手/wiki/concepts/Raw-Wiki-Schema 三层架构]]、[[笔记同步助手/wiki/concepts/增量知识维护]]。
- 新建实体页：[[笔记同步助手/wiki/entities/Codex]]、[[笔记同步助手/wiki/entities/Obsidian]]。
- 新建主题页：[[笔记同步助手/wiki/topics/AI 辅助个人知识管理]]。
- 待人工确认：是否调整同步助手的未来输出路径、是否启用 Git 版本管理、下一批优先入库主题。

## 2026-08-10 — 初始化项目级本地 Git

- Git 根目录：`笔记同步助手/`，未覆盖父级 Obsidian Vault 或其他知识项目。
- 初始分支：`main`。
- 当前状态：空仓库，尚无提交，未配置远程仓库。

## 2026-08-10 — 纠正 Git 根目录判断

- 上一条记录中的项目级空 Git 仓库是错误初始化，现已删除其 `.git` 元数据；笔记内容未删除。
- 已确认现有 GitHub checkout 位于 `Personal-Knowledge-Base/Personal-Knowledge-Base/`，远程为 `Wenjunyun123/Personal-Knowledge-Base.git`。
- 父级 Obsidian Vault `Personal-Knowledge-Base/` 目前不是 Git 根；是否把现有 checkout 对齐到父级目录仍待人工确认。

## 2026-08-11 — 将现有 Git checkout 展平到 Vault 根目录

- 迁移前备份：`E:\DATA\github-kb\.codex-backups\Personal-Knowledge-Base-inner-before-flatten-20260811-115915`；3145 个文件、359733311 字节与源一致。
- Git 根目录已从内层 `Personal-Knowledge-Base/Personal-Knowledge-Base/` 对齐到父级 Vault `Personal-Knowledge-Base/`，旧内层目录已清空并移除。
- 保留 origin `https://github.com/Wenjunyun123/Personal-Knowledge-Base.git`、分支 `main`、HEAD `514ade62f4132ae5b1fefd4ce4d3ebf98f10b27e` 和原 Git index。
- `.claude/claudian-settings.json` 保留父级当前版本；内层旧版本归档为 `.claude/claudian-settings.inner-before-flatten-20260811.json`；4 个 session 文件已合并。
- 未创建提交、未暂存、未推送；现有四个深度学习笔记的未提交内容哈希与迁移前备份一致。
- 知识库结构、完整路径双链和指定原文 SHA-256 校验通过。
- `.gitignore` 已排除新的 `.claude/sessions/` 文件、迁移归档 settings、同步助手备份目录和 `nul`；已有 4 个 session 元数据文件此前已经被 Git 跟踪，本次未擅自从索引移除。
