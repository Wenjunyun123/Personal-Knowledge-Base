---
author: 美研芒格君
source: X
url: https://x.com/Kay2289123/status/2125915733100245346?a=7NRTPrmwb2C3INmtrSM&s=19
saved: 2026-11-26 23:17:56
tags:
  - 笔记同步助手
id: 52e69578-08fa-4762-ae83-85ab667a7d5f
---

🔗 [在 X 查看原文](https://x.com/Kay2289123/status/2125915733100245346)

如果你有很强烈的学习能力，想进 AI 行业，做高薪方向，该学什么？  
  
我真心建议你学 AI 推理工程，可以从下面的步骤来。  
  
1\. 先挑一个方向钻进去。 GPU 编程（比如 CUDA）、模型优化、量化、分布式推理，都可以选。  
• 可以先看 GPU 的线程和内存是怎么组织的。NVIDIA《CUDA 编程指南》 [docs.nvidia.com/cuda/cuda-programming…](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html)  
  
2\. 把基础学透。 一个请求进来，GPU 跑了哪些计算？模型怎么一个 token 一个 token 地生成答案？  
• 可以跟着 Karpathy 写一个小 GPT，重点看它怎么预测下一个 token。 [youtube.com/watch](https://www.youtube.com/watch?v=kCc8FmEb1nY)  
  
3\. 上手 PyTorch、Triton、vLLM 和 TensorRT-LLM。 试着把模型部署成一个能接真实请求的推理服务。  
• 服务部署可以先从跑通一个 API 开始。vLLM 官方教程 [docs.vllm.ai/en/stable/getting\_starte…](https://docs.vllm.ai/en/stable/getting_started/quickstart/#online-serving)  
  
4\. 做 3 到 5 个项目。 试着压低推理成本、缩短回复延迟，或者让同样的 GPU 扛住更多请求。  
• 举个例子，拿一个开源模型做量化，用同一套问题对照测试，看看省了多少显存，回答表现有没有变化。  
• 也可以先跑通一版小型推理引擎，再动手改一处调度或缓存。Nano-vLLM [github.com/GeeeekExplorer/nano-vllm](https://github.com/GeeeekExplorer/nano-vllm)  
  
5\. 每个项目都跑 benchmark。 固定 GPU 和测试条件，记录每张卡的吞吐、延迟和每百万 token 的成本。  
• 举个例子，假设同一张卡跑同一批请求，输出从每秒 100 个 token 提到 130 个，吞吐就是多了 30%。也把首 token 延迟和回答质量记下来。  
• 可以照着文档跑一次压测。vLLM Benchmark CLI [docs.vllm.ai/en/stable/benchmarking/c…](https://docs.vllm.ai/en/stable/benchmarking/cli/)  
  
6\. 列出 50 家你真想去的公司。 AI 创业公司、GPU 云厂商、专门做推理的团队都可以。  
• 可以先从公司目录里找做推理和 GPU 云的团队。YC 基础设施公司目录 [ycombinator.com/companies/industry/in…](https://www.ycombinator.com/companies/industry/infrastructure)  
  
7\. 看看这些公司的系统卡在哪儿。 从工程博客或公开 issue 里挑一个具体问题，做个能复现、能对比的项目。  
• 举个例子，如果一个文档问答服务反复把同一份长文放进提示词，可以用公开文档搭个 demo，测测复用这段前缀能不能缩短首 token 延迟。  
• 可以看看实际团队怎么用缓存路由减少排队和长尾延迟。Modal 与 Sakana AI 的上线复盘 [modal.com/blog/sakana-case-study](https://modal.com/blog/sakana-case-study)  
  
8\. 直接联系创始人或工程负责人。 给他们看项目、代码和测试结果，然后问问有没有实习机会。  
• 消息可以这样写，「看到你们工程博客提到长文档请求慢，我用公开数据做了个小实验。这里是代码和测试结果，请问团队有推理方向的实习机会吗？」  
• 可以参考 YC 对第一封联系邮件的建议。 [ycombinator.com/blog/advice-for-job-s…](https://www.ycombinator.com/blog/advice-for-job-seekers-on-resumes-and-standing-out)  
  
9\. 花 12 到 18 个月扎扎实实做一线工程。 亲手部署、看监控、排查故障，搞清楚 AI 系统在线上到底怎么跑。  
• 可以看推理服务怎么部署到 Kubernetes、怎么路由请求、怎么做监控。vLLM Production Stack [github.com/vllm-project/production-st…](https://github.com/vllm-project/production-stack#step-by-step-tutorials)  
  
10\. 有了这些经验，再考虑自己出来做。 可以做推理服务，帮别的团队做性能优化咨询，或者做 GPU 基础设施。  
• 可以先学怎么判断一个创业点子有没有真实需求。YC《如何找到创业点子》 [ycombinator.com/library/8g-how-to-get…](https://www.ycombinator.com/library/8g-how-to-get-startup-ideas)  
  
模型会越来越聪明。要让更多人用上它，每次调用得够便宜，用户等回复的时间得够短，流量上来时服务还得扛得住。  
  
谁能把这些问题解决，谁就有机会在 AI 产业里做成一门大生意。

---

## 💬 评论（16）

> **Charles在路上 @Charles77xixi**
> 
> 其实有点晚了，国内目前相关就业市场在急剧收缩

> **zrqgood @zrqgood9068**
> 
> 补一条更省时间的走法：方向定下来后先跑通一条最小端到端链路，拿一个 7B 模型，把量化前后、批大小、并发这三组变量各测一遍吞吐、首字延迟和显存占用，自己画成曲线。比通读编程指南更快建立判断，因为面试问的多是某次线上延迟怎么压下来，而不是能不能背出线程模型。

> **青衫渡月 @lizhang525474**
> 
> 转行的人上 CUDA，门槛是不是太高了？

> **Young | AI & Markets 🚀 @LeslieYoung1114**
> 
> 推理工程现在确实是离钱最近的岗位🤣

> **大喵CS、转码、预科班(十年讲师，能够教你学会编程) @damiaoedux**
> 
> 学cuda？先把计算机组成原理，操作系统还有c语言啃下来

> **0xAzr @AzrianoY1**
> 
> 自学的话，普通显卡够练手吗？

> **Hoki 🇨🇦 @HokiFuqi**
> 
> CUDA这关就劝退一大半人 🫠

> **涵涵 @hanhan010101**
> 
> “如果你有很强烈的学习能力”NVIDIA这类架构改动的意义不在benchmark，在成本结构：同样的推理量，单位成本能压多少。说白了，算力扩张的边际成本是递增的：先买卡，再供电，再散热，每一层都比上一层更难批。迁移成本谁承担？客户愿意为性能多付多少？

> **jimerrors @JMkernt**
> 
> 第5条最实在，数字说话

> **哨兵B哥 @SentryB\_**
> 
> 难怪开价高。AI 应用公司毛利比传统 SaaS 低一大截，账上最大一块成本就是推理，推理成本砍掉两成，下轮融资讲毛利都有底气了

> **阿强（讨伐claude版） @BruceJia1**
> 
> 先啃透CUDA内存层级，比堆框架收益大得多。

> **王纯纯 @chun\_wang35417**
> 
> 现在入场就是去当分母吧

> **黑衣执事 @hackdeacon**
> 
> 学推理

> **Kane @konjinensi**
> 
> 我最近在学习并实施部署一个pytorch的人车船飞类模型，按照最小完整走一遍流程，对我来说非常振奋。感谢博主分享知识。

> **rudje @thronill**
> 
> 标记一下

> **重建巴别塔 @BeyondGodC**
> 
> AI如果发展的好的话，应该什么都不用学

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/efdd41fc_1795706275748?u=https%3A%2F%2Fx.com%2FKay2289123%2Fstatus%2F2125915733100245346)