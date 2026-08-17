---
author: そう｜Claude Codeで始めるAI自動化
source: X
url: https://x.com/so_ainsight/status/2069281811168198760?s=20
saved: 2026-06-24 20:56:57
tags:
  - 笔记同步助手
id: 4c2790c0-b8e8-45f2-8cdf-4508f111f8e7
---

🔗 [在 X 查看原文](https://x.com/so_ainsight/status/2069281811168198760)

今週GitHubで急上昇したAIリポジトリ10選：  
  
1\. headroom  
LLMに渡す前にログ・ファイル・RAGチャンクを圧縮し、トークン消費を60〜95%削減するツール。ライブラリ・プロキシ・MCPサーバーの3つの形で組み込める。  
[github.com/chopratejas/headroom](https://github.com/chopratejas/headroom)  
  
2\. Agent-Reach  
Twitter・Reddit・YouTube・GitHubなど主要プラットフォームをAIエージェントに横断検索させるツール。APIキー不要でCLI1本から動く。  
[github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)  
  
3\. agent-skills（addyosmani）  
コーディングエージェント向けの本番品質スキルセット。AIアシスタントを実務レベルで動かすための土台。  
[github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)  
  
4\. SkillSpector（NVIDIA）  
AIエージェントスキルの脆弱性・悪意あるパターン・セキュリティリスクを検出するスキャナー。NVIDIAが公開したエージェント安全対策ツール。  
[github.com/NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)  
  
5\. codebase-memory-mcp  
コードベースを永続的な知識グラフとしてインデックス化するMCPサーバー。158言語に対応し、依存ゼロの単一バイナリで動く。  
[github.com/DeusData/codebase-memory-m…](https://github.com/DeusData/codebase-memory-mcp)  
  
6\. OpenMontage  
AIコーディングアシスタントを動画制作の環境に変えるオープンソースシステム。12本のパイプラインと52種のツールを搭載する。  
[github.com/calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)  
  
7\. PaddleOCR  
PDFや画像を、AIが扱いやすい構造化データに変換する軽量OCRツールキット。100言語以上に対応し、LLMへの入力前処理に使える。  
[github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)  
  
8\. agentsview  
Claude Code・Codexなど20以上のコーディングエージェントのセッション履歴・トークン使用量・インサイトを、ローカルで検索・分析できるツール。  
[github.com/kenn-io/agentsview](https://github.com/kenn-io/agentsview)  
  
9\. LMCache  
LLMのKVキャッシュを高速化する専用レイヤー。同じコンテキストの再計算を省き、推論コストと遅延を下げる。  
[github.com/LMCache/LMCache](https://github.com/LMCache/LMCache)  
  
10\. flue（withastro）  
自律エージェントを構築・実行するためのTypeScript製ハーネスフレームワーク。セッション・ツール・スキルに加え、安全な実行のためのサンドボックスを備える。  
[github.com/withastro/flue](https://github.com/withastro/flue)

![[笔记同步助手/images/f8ca665a7d5926883d0d314b7d813c01_MD5.jpg]]

![[笔记同步助手/images/67a05f0ba75f5351c56b6ad4b593b0d2_MD5.jpg]]

![[笔记同步助手/images/300a85c1d32acc4b7e4fbbe77720c265_MD5.jpg]]

![[笔记同步助手/images/d42ff0f69fdf4762418f476f32a1dc46_MD5.jpg]]

---

**🧵 作者续推（1）**

> **2/** この投稿が参考になったら、 @so\_ainsight をフォロー。  
> いいね、リポストもよろしく。

---

## 💬 评论（16）

> **Sergey Cherkashin @VonderVuflya**
> 
> 翻訳ツールで書いているので、不自然だったらすみません🙏 とても参考になるまとめでした！  
>   
> 私も近いレイヤーのものを作っています →  
> Yggdrasil：AIコーディングエージェント向けの、ローカル＆依存ゼロな永続メモリです。お目に留まれば嬉しいです🌳  
> [github.com/VonderVuflya/Yggdrasil](http://github.com/VonderVuflya/Yggdrasil)

> **Gerard Sans | Axiom 🇬🇧 @gerardsans**
> 
> Meme:

> **Mustafa Bozkaya @InfoMBozkaya**
> 
> 🚀 Bu hafta yükselen AI repo'ları süper özetlemişsin!  
>   
> Gerçek zamanlı ve momentum bazlı GitHub trending'leri takip etmek için \*\*[trendshift.io/\*\*](https://trendshift.io/**) sitesini şiddetle tavsiye ederim.  
>   
> Bu tarz özetler için harika bir kaynak 👌  
>   
> #AITools #GitHub

> **Ryu @ai\_ryu\_fukugyo**
> 
> headroomみたいにLLMへ渡す前で削る発想、俺もログ要約の自動化で一番効きました！重複行とエラースタックだけ先に整えると、コストだけでなく回答ブレも減りました！

> **Yoseph Gratika I.P. @yosephgratika**
> 
> Codegraph also reduce the token amount in my use case, mainly I'm using grokbuild + codex 🙌

> **Manh Hung ✨ @manhhung\_ai**
> 
> headroomの60〜95%削減、かなり幅あるけどRAGの種類でブレそう。どの前提で上限寄り出る想定なんだろう？

> **abel @aaaiautg**
> 
> headroom 这个思路有意思，在 context window 阶段之前做压缩比单纯依赖 long context 更实际。RAG chunk 的压缩质量直接影响 retrieval 效果，好奇它的压缩率和 recall 的 tradeoff 是怎么做的。你们 workflow 里怎么处理 token budget？

> **Yann Ribemont @YannRibemont**
> 
> unroll

> **macintoxic @macintoxic**
> 
> unroll

> **Czerian.eth  ⟠ ✪ 𝕏  @\_lazygoku**
> 
> unroll

> **HSIAO YUAN @lliu54827**
> 
> headroomが気になった。  
> ClaudeにK線データ食わせると毎回トークン膨らんで、自分でトリミングしてたけど60〜95%削減できるなら試す価値ある。  
> 8ヶ月毎日Claude使ってて一番悩むのがコンテキスト管理で、RAGに逃げる前に前処理層のほうが結果よかった。  
> codebase-memory-mcpも面白そう。

> **Steven Cheng @stevencheng**
> 
> headroom’s token savings are huge.

> **21 @DJ\_Reddz**
> 
> This is gold thank you for sharing

> **GPTaku @GPTaku**
> 
> Lazycodex with Insane search

> **安叫兽|Bird🕊️ 🔶 BNB @ajs6888**
> 
> headroom 省 token 这块有点香

> **Raiman @0xRaiman**
> 
> Thanks

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/4861d506_1782305815256?u=https%3A%2F%2Fx.com%2Fso_ainsight%2Fstatus%2F2069281811168198760)