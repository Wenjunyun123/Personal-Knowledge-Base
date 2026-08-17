---
author: meng shao
source: X
url: https://x.com/i/status/2077335188666044426
saved: 2026-07-16 01:15:22
tags:
  - 笔记同步助手
id: 22d870c7-3f15-43d1-b808-8114a8ea2158
---

🔗 [在 X 查看原文](https://x.com/shao__meng/status/2077335188666044426)

推荐 @MengTo 为设计师和开发者们开源的 Skills  
  
MengTo 是 @designcodeio 和 [aura.build](http://aura.build) 创始人，在设计和开发结合方面有非常深的积累，他的分享必须关注起来，这个开源项目把设计指令、工作流、风格系统、抓取与调试经验都沉淀成了「四大类、75 个 Skills」  
[github.com/MengTo/Skills](https://github.com/MengTo/Skills)  
  
1\. Codex workflows - 10 个  
可复用的 Agent 操作流程（抓取、转 prompt、性能剖析、内容生产）  
video-to-superprompt、stitched-full-page-capture、html-to-interaction-prompts、daily-ui-inspiration-capture、optimize-web-animations、performance-profiling  
  
2\. Media - 2 个  
按用途/裁切/比例挑选高质量图片素材  
aura-asset-images、unsplash-asset-images  
  
3\. UI - 1 个  
“像设计系统一样写 prompt”的方法论  
design-first-ui-prompting  
  
4\. Web design - 62 个  
落地页结构、动效系统、WebGL/3D、CSS 处理、布局系统、视觉风格  
landing-page、pricing-page、gsap、threejs、tailwindcss、animation-on-scroll、globe-gl、cobejs、vantajs、progressive-blur、css-border-gradient、各种 dark/glass/skeuomorphic 风格包 ...  
  
旗舰工作流：从参考视频到一键 HTML  
1\. video-to-superprompt —— 输入一段参考视频（设计稿/落地页/动画录屏），用 ffprobe+ffmpeg 抽帧，按“故事 / 布局 / 运动 / 视觉 / 技术重建 / 可访问性”六层分析，输出一个长到不看原视频也能重建的 paste-ready prompt，明确点名 GSAP ScrollTrigger、Lenis、Three.js、video.currentTime scrubbing 等具体机制。  
2\. html-to-interaction-prompts —— 把已有 HTML 页面（如 Aura Build 产物）拆成“单段/单动画/单按钮/单 hover/单 WebGL 效果”的可复用 prompt 文章。  
3\. stitched-full-page-capture —— 解决 Framer 等懒加载/滚动动画站点 fullPage 截图发白的痛点：滚动预热 → 视口分步截图 → 垂直拼接 → 用拼接图重切 section crop，并写回 manifest。配套 Playwright + ffmpeg 脚本。  
4\. daily-ui-inspiration-capture —— 把“浏览 + 抓取 + 参考研究 + prompt 生成”组合成每日自动循环，产出 prompt pack。  
  
两个值得细读的 Skill 范式  
1\. design-first-ui-prompting 给出了一套固定 prompt 骨架：GOAL → FORMAT → LAYOUT → TYPE SYSTEM → COLOR+MATERIAL → IMAGERY → COPY → CONSTRAINTS → NEGATIVE PROMPT，并强调三个关键技巧：  
· “Variants > rerolls”：先锁定布局+层级+文案，再每次只改一个变量（角度/强调色/卡片排布/背景调子）。  
· 2-pass 字体工作流：模型常拼错字时，先无字生成留出文字安全区，再回 Figma 排版。  
· Constraints card：用 FONT / STYLE / MODE 三行小面板像 mini style guide 一样锚定输出。  
2\. landing-page 则示范了一个“设计 + 转化 + SEO”三合一 SOP：先收集页面目的/受众/证据/约束，再给核心结构（首屏 5 要素 → 中段论证 → 底部异议处理），列出 4 种布局选型、6 条高转化策略、headline/CTA 文案模板、逐节迭代顺序、SEO/AEO 清单和常见坑——典型地体现了“Skill = 操作规程”的写法。

![[笔记同步助手/images/3162fba7e84984a9587239f18b15334a_MD5.jpg]]

---

## 💬 评论（2）

> **晚晚 @An\_yhl**
> 
> 这个仓库够设计开发吃一阵了

> **meng shao @shao\_\_meng**
> 
> 😅 现在 Tibo 一发推，就代表着要「RESET」了？  
>   
> Tibo 自己也打趣：你们是不是觉得我又要通知 reset 了，不是，我只是来刷刷推，看看对 ChatGPT Work 和 Codex 的反馈！  
>   
> 所以，朋友们，懂了吗？  
> 有任何使用 ChatGPT Work 和 Codex 的反馈都可以在 Tibo 的帖子下回复。  
>   
> 有可能！你发现的问题，会给大家带来一次 RESET 😃

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/2ea3f4d7_1784135720488?u=https%3A%2F%2Fx.com%2Fshao__meng%2Fstatus%2F2077335188666044426)