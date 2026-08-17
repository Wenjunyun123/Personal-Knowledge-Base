---
author: 成峰
source: 微信公众号
url: https://mp.weixin.qq.com/s?__biz=MzU3MjU5Mzc2Nw==&mid=2247489933&idx=1&sn=b56e3b3fedcc3b29cad259ebc1446c9b&chksm=fd9b702b7257392992f89a5518e33a67ef2bdca88b494828fbc58467ed8502e58b257548daa2&mpshare=1&scene=1&srcid=06245ZbIMbdfAJclTcsnKbBf&sharer_shareinfo=904d90c2239523e83865ef316da4588e&sharer_shareinfo_first=904d90c2239523e83865ef316da4588e#rd
saved: 2026-06-24 12:42:52
tags:
  - 笔记同步助手
id: dcffea01-b6a9-4bbf-8ed3-33ed03b57ccc
---

公众号名称：AI产品自由

作者名称：成峰

发布时间：2026-06-22 07:20

我之前做过一个 2000+ Star 的剪辑 Skills。

> ![[笔记同步助手/images/ff4e06bb2d9828bd8730cd0f79fb2057_MD5.png]]

这次接上 Codex，大升级！加上了复杂的动画效果。  
已经帮我跑出好几条千赞视频。

> ![[笔记同步助手/images/8d80b4b9c2e349f2f5a2f2d2bb7b6a6b_MD5.jpg]]

先看结果：

![[笔记同步助手/images/1dc43f0e13db616102c27f6c1fa93865_MD5.jpg]]

> 📹 此处为视频内容（vid: wxv\_4571421040303882240）（上图为封面），未能直接提取，请前往原文查看：[在公众号原文中观看](https://mp.weixin.qq.com/s?__biz=MzU3MjU5Mzc2Nw==&mid=2247489933&idx=1&sn=b56e3b3fedcc3b29cad259ebc1446c9b&chksm=fd9b702b7257392992f89a5518e33a67ef2bdca88b494828fbc58467ed8502e58b257548daa2&mpshare=1&scene=1&srcid=06245ZbIMbdfAJclTcsnKbBf&sharer_shareinfo=904d90c2239523e83865ef316da4588e&sharer_shareinfo_first=904d90c2239523e83865ef316da4588e#rd)

我近期的视频，都是用这个流程去跑的。

以前做视频，要先打开剪映。

现在装好 Skills，把视频和文字稿丢给 Agent，它就能把整条片子往下跑。

# 我是怎么做的呢？

## 1.让 Agent 安装剪辑 Skills

打开 Claude Code 或 Codex，发给他这个提示词：

> 帮我安装或更新 `chengfeng-videocut-skills` 这个剪辑 Skills。
> 
> 安装命令是 `npx chengfeng-videocut-skills install`。

Agent 会先跟你确认，然后自己去跑安装。装好以后，本地就能调用这套剪辑 Skills。

这套skills，我把所有的经验，都放到里面了。

安装好了以后，效果如下图：

> ![[笔记同步助手/images/1238519e560f56130c12ae881cd79492_MD5.png]]

## 2.生成剪后视频和字幕

第二步，先把原始口播整理成基础素材包。

> ![[笔记同步助手/images/fe5f760cc1b36b384ac72b70d402d8e1_MD5.jpg]]

我们把口播视频和文字稿交给 `剪口播` Skills，就能拿到剪后视频和字幕文件。

下面具体看怎么做。

口播视频不用复杂录。我一般直接对着文字稿念一遍。

> ![[笔记同步助手/images/1ca38835b6395fcaab63151d4a925f86_MD5.jpg]]

如果中间涉及到具体操作，就切换画面，把操作过程录进去。

> ![[笔记同步助手/images/a00944b25b4cf9207d1221cc5865aba7_MD5.png]]

这些都准备好以后，就可以交给 `剪口播` Skill。

直接在项目里输入斜杠命令：

```
/剪口播  + 视频地址 + 口播稿地址
```

它会开始处理你给它的视频和文字稿。

> ![[笔记同步助手/images/d630aa035c5ede8d383eecd1c497c5e8_MD5.png]]

接到命令后，Agent 会先生成审核页。

> ![[笔记同步助手/images/24ea870a4f34ffccbf874a8ed36c27a3_MD5.jpg]]

Agent 会把停顿、口误、重说先整理出来。我要做的，就是确认这些删除项是否对。

确认没问题后，我点“执行剪辑”。

这一步跑完后，Agent 直接输出“剪后视频”和“字幕文件”。

> ![[笔记同步助手/images/4e0606bb38642776336b5eddfb7eabb5_MD5.png]]

得到的字幕，和剪后视频，在时间上是对齐的。

到这里，基础素材包就准备好了：

```
剪后口播视频
对齐字幕文件
```

## 3.按字幕生成分镜页面

素材包准备好以后，在项目里输入斜杠命令，唤醒这个 Skill：

```
/口播成片
```

> ![[笔记同步助手/images/d6b4b4c3e5fe4ae03a8149a28a02a931_MD5.png]]

Agent 生成一个 HTML 分镜核对页。

如下图：

> ![[笔记同步助手/images/2b984459bc237915b996ac94428a3821_MD5.jpg]]

左边是 Agent 生成的画面，右边是字幕、画面任务、素材来源和镜头动作。

这个 Skill 在分镜页里实际做三件事：

> ![[笔记同步助手/images/4195729bdbe52f113da90646d8f5ddfe_MD5.jpg]]

它会先按字幕时间轴拆段，再根据每一段内容选择画面来源。

每一句话，到底保留原视频，还是换成截图、产品页面、结果页，或者做一个 HTML 动画，Agent 都会在这里一步处理掉。

如果这一段讲的是录屏操作，Agent 就会保留原视频片段。下面这个画面，就是保留原视频里的页面效果。

> ![[笔记同步助手/images/1e024549a4d1a7c8c40c4de98f6e0ab3_MD5.jpg]]

如果这一段更适合用截图、产品页面或结果页来解释，Agent 就会切到对应素材。比如下面这个页面，直接展示了 Agent 的回答。

> ![[笔记同步助手/images/9b369475532870ac19d7493e518bd60f_MD5.png]]

在前面的两个素材基础之上，它还可以做非常丰富的动画。比如下面的这一个动画，就是背后有一张素材图，我又让他在这个素材图上，去画了一些动画。

> ![[笔记同步助手/images/aa1955235fe8972450d583697e82cfec_MD5.gif]]

我试了几个动画方案，现在用下来 rough.js 效果最好。

它画逻辑图和标注比较顺手，圈重点、画箭头的效果也更接近手绘批注。

如果某一段不满意，直接告诉 Codex 第几段哪里不对。改起来也非常快。

比如直接说：

```
05 这一段动画改一下。
箭头指向标题，圈出右侧结果。
```

Codex 的 Computer Use 可以打开这个页面，看左边画面和右边口播，再回去改 HTML 画面或标注。这个更自动化。

我的动作从“自己排分镜”，变成“看分镜，提修改一键”。

## 4.检查时间线预览

分镜页面确认后，就可以进入预览。

继续说：

> ![[笔记同步助手/images/942f25a5b3cb49020ca14f72bcf1b55b_MD5.png]]

然后 Agent 就会给出来一个预览页面。

左边是视频预览；底部是进度条，附带文字说明；右边展示口播内容。

> ![[笔记同步助手/images/497edc597175643ec41fdc9c3d8b2c60_MD5.jpg]]

时间线预览会按字幕时间点排动画。字幕说到哪里，动画就出现在哪里，这比自己在剪辑软件里对时间线省很多事。

> ![[笔记同步助手/images/38a0f87ba9052cef510b9c7b001e99e4_MD5.jpg]]

这里看的是“这些画面放回整条视频以后，出现得对不对”。

如果视频出错，比如：

```
画面没有提前出现
原视频被误换成 HTML
截图用错
文字挡住画面
节奏不是跟着口播走
```

反馈不用写长文，直接按片段说：

> 01保留原视频。
> 
> 02图出现太早
> 
> 03画面太满，删掉下面两行字。

这一步确认以后，才进入最终合成。

## 5.合成 MP4

前面的这个视频预览确认了以后，我们就可以让它合成了。

> ![[笔记同步助手/images/c098e12366e40260ae5a0b775608ec63_MD5.png]]

Agent 会用 HyperFrames 负责把它变成可以渲染的视频动画工程。

> ![[笔记同步助手/images/fcae87f24d625ff9ebad54965198dba5_MD5.png]]

HyperFrames 对 Agent 很友好，因为它可以把 HTML 动画变成视频。只要画面能用 HTML 做出来，就能进入这条合成流程。

过几分钟我们就可以看到最后的动画了。

导入字幕和视频到剪辑工具里面，检查一下有没有一些细节有错。

> ![[笔记同步助手/images/12acbe7c7a9e437d11d2cd2c0f90b5a5_MD5.jpg]]

# 剪辑Agent，正在逐步替代传统剪辑

以前，视频生产围绕时间线展开。

现在，视频生产开始围绕工作流展开。

剪辑 Agent 正在替代传统剪辑里的操作层，把视频生产变成一条可以持续复用的自动化流程。

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/d3decd77_1782276171139?u=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU3MjU5Mzc2Nw%3D%3D%26mid%3D2247489933%26idx%3D1%26sn%3Db56e3b3fedcc3b29cad259ebc1446c9b%26chksm%3Dfd9b702b7257392992f89a5518e33a67ef2bdca88b494828fbc58467ed8502e58b257548daa2%26mpshare%3D1%26scene%3D1%26srcid%3D06245ZbIMbdfAJclTcsnKbBf%26sharer_shareinfo%3D904d90c2239523e83865ef316da4588e%26sharer_shareinfo_first%3D904d90c2239523e83865ef316da4588e%23rd&s=obsidian)