---
author: GitHubDaily
source: X
url: https://x.com/i/status/2040007843638845711
saved: 2026-07-25 21:31:16
tags:
  - 笔记同步助手
id: eba8f786-1898-44bb-afe0-ce7d0027f3c9
---

🔗 [在 X 查看原文](https://x.com/GitHub_Daily/status/2040007843638845711)

AI 短剧赛道爆火，自己想动手时，却发现剧本拆分、角色设计、生图、生视频这些环节，需要在好几个工具之间来回切换，极其消耗精力。  
  
偶然在 GitHub 看到 ArcReel 这个开源项目，把从小说到成片的整个流程串成了一条自动化流水线，全程由 AI 智能体驱动。  
  
只需上传小说内容，AI 便自动完成剧本生成、角色设计、分镜绘制、视频片段生成，最后合成完整视频，基本不用手动干预。  
  
GitHub：[github.com/ArcReel/ArcReel](http://github.com/ArcReel/ArcReel)  
  
它会先生成角色设计图，后续所有画面都参考这张图，保证同一个角色在不同镜头里长得一样。  
  
图片和视频生成支持 Gemini、Grok、OpenAI 等主流模型供应商，同时支持随时切换。  
  
做完的视频片段还能一键导出成剪映草稿，方便二次编辑调整。  
  
可通过 Docker 快速部署使用，如果你也想制作 AI 短剧，又不太想折腾，可以试下这个工具。

![[笔记同步助手/images/314659b8943e9d10de11ae58fee894cb_MD5.jpg]]

---

## 💬 评论（12）

> **牛魔王🔶OP\_CAT @Btcniumowang**
> 
> 这个workflow太丝滑了

> **HAI Labs（人本智能实验室） @Meta360DAO**
> 
> 目前各大自媒体平台AI短剧如火如荼，如果你也想制作AI短剧，你可以试试这几个项目  
>   
> 一、魔因漫创 Moyin Creator  
> 🎬 AI 影视生产级工具 · 支持 Seedance 2.0 · 剧本到成片全流程批量化  
> 魔因漫创 是一款面向 AI 影视创作者的生产级工具。五大板块环环相扣，覆盖从剧本到成片的完整创作链路：  
> 📝 剧本 → 🎭 角色 → 🌄 场景 → 🎬 导演 → ⭐ S级（Seedance 2.0）  
> 每一步的产出自动流入下一步，无需手动搅合。支持多种主流 AI 大模型，适合短剧、动漫番剧、预告片等场景的批量化生产。  
> 功能特性  
> ⭐ S级板块 — Seedance 2.0 多模态创作 SkyReels-V4 多模态创作  
> ​多镜头合并叙事视频生成​：将多个分镜分组合并生成连贯叙事视频  
> 支持 @Image / @Video / @Audio 多模态引用（角色参考图、场景图、首帧图自动收集）  
> 智能提示词构建：自动三层融合（动作 + 镜头语言 + 对白唇形同步）  
> 首帧图网格拼接（N×N 策略）  
> Seedance 2.0 参数约束自动校验（≤9图 + ≤3视频 + ≤3音频，prompt≤5000字符）  
> 地址：[github.com/MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator)  
>   
> 二、waoowaoo AI 影视 Studio  
> 一款基于 AI 技术的短剧/漫画视频制作工具，支持从小说文本自动生成分镜、角色、场景，并制作成完整视频。  
> 功能特性  
> 🎬 AI 剧本分析 — 自动解析小说，提取角色、场景、剧情  
> 🎨 角色 & 场景生成 — AI 生成一致性人物和场景图片  
> 📽️ 分镜视频制作 — 自动生成分镜头并合成视频  
> 🎙️ AI 配音 — 多角色语音合成  
> 🌐 多语言支持 — 中文 / 英文界面，右上角一键切换  
> 地址：[github.com/saturndec/waoowaoo](https://github.com/saturndec/waoowaoo)  
>   
> 三、Jellyfish AI短剧工厂 / AI Short Drama Studio  
> 一站式 AI 生成短剧（竖屏短剧 / 微短剧）的生产工具  
> 从剧本输入 → 智能分镜 → 角色/场景/道具一致性管理 → AI 视频生成 → 后期剪辑 → 一键导出成片  
> ✨ 核心价值  
> ​极致一致性​：全局种子 + 统一风格 + 资产复用，解决 AI 生成最痛的“人物/场景漂移”问题  
> ​工业化生产流程​：从文学剧本到可拍摄分镜，再到视频片段，一条龙闭环  
> ​可视化 & 可控​：所见即所得的分镜编辑器 + 精细的镜头语言控制 + 实时预览  
> ​资产复用体系​：角色/场景/道具/服装/提示词模板全生命周期管理  
> 🎯 适用场景  
> 短剧/微短剧内容创作者  
> AI 影视工作室批量生产  
> 个人创作者想低成本试水竖屏短剧  
> 教育/培训机构制作教学短视频  
> 品牌/电商制作带剧情的产品宣传短片  
> 地址：[github.com/Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish)  
>   
> 四、BigBanana AI Director (AI 漫剧工场)  
>   
> BigBanana AI Director是一个一站式 AI短剧，AI漫剧,AI导演平台，面向创作者，实现从灵感到成片的高效生产。 它摇弃了传统的“抽卡式”生成，采用 "Script-to-Asset-to-Keyframe" 的工业化工作流。实现 “一句话生成完整短剧，从剧本到成片全自动化”，同时精准控制角色一致性、场景连续性与镜头运动。  
>   
> [github.com/shuyu-labs/BigBanana-AI-Di…](https://github.com/shuyu-labs/BigBanana-AI-Director)

> **Ren Hoshino @Ren\_Hoshino\_4**
> 
> 阿里有个lumenx也很不错[github.com/alibaba/lumenx](https://github.com/alibaba/lumenx)

> **Upulse @upulseapp**
> 
> 这种把各环节串成自动化流水线的思路挺实用。很多创作者不是缺单点工具，是缺能把工作流打通的方案。

> **心靈閱讀 @Hammertvfun**
> 
> 火山方舟 中國台灣無法註冊使用 有解嗎？

> **Upulse @upulseapp**
> 
> AI 工作流整合越来越成熟了。从文字到成片，中间环节越少，创作者能把更多精力放在内容创意上而不是技术细节上。

> **tang | AI Product Maker @justic\_hot**
> 
> 角色一致性是 AI 短剧最头疼的问题，先生成设计图让后续镜头参考这个思路是对的。  
>   
> 不过实测下来（我自己做 AI 视频工具的时候踩过这个坑），就算有参考图，生图模型在不同姿势和光线下还是会漂移。真正的瓶颈不在单个环节，在环节之间的交接——前一步输出的格式和下一步期望的输入总是对不上。

> **Charlie Bear 小熊風 @SomeCharlieBear**
> 
> 看起来很不错

> **⭐️ @xfr11111**
> 
> 你好，我是小白，能学吗

> **何夕2077 (个板马版) @justlikemaki**
> 
> 从小说到成片一条管线拉通，关键看中间每一步的可控性——角色一致性、镜头语言、配音节奏这些能做到多细。跑通 demo 不难，量产才见真章。

> **白也来咯 @wangzihui383992**
> 
> 😎

> **Melinda Butts @butts55568**
> 
> 算力是硬伤

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/aa6fd306_1784986274942?u=https%3A%2F%2Fx.com%2FGitHub_Daily%2Fstatus%2F2040007843638845711)