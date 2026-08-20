---
author: Lonely
source: X
url: https://x.com/Lonely__MH/status/2090110302969081899
saved: 2026-08-20 13:05:26
tags:
  - 笔记同步助手
id: f3714a57-04b8-400e-96f0-7558bfd33c07
---

🔗 [在 X 查看原文](https://x.com/Lonely__MH/status/2090110302969081899)

🎉好消息！ 8G 内存 Mac 也能部署 Qwen 3.8-27B 了！  
  
@UnslothAI 刚刚整了个大活，发布了基于 Qwen3.8-27B 的 Dynamic 3.0 超级量化版本！  
  
以往 27B 这种体量的多模态大模型，至少需要 30G 以上的显存/内存才能勉强带得动  
  
但这次，通过极致的 1-bit / 2-bit 量化（UD-IQ1\_M / UD-IQ2\_S），模型体积直接被压缩到了 6G～8GB 左右！  
  
虽然是极限压缩，但它依然保留了多模态能力，还自带思维链深度思考！  
  
运行方式👇🏻  
  
1\. 羊驼 Ollama 一键运行（适合小白）  
\---  
ollama run [hf.co/unsloth/Qwen3.8-27B-GGUF:UD-IQ2…](http://hf.co/unsloth/Qwen3.8-27B-GGUF:UD-IQ2_S)  
\---  
  
2\. llama.cpp 终端运行（推荐极客）  
\---  
brew install llama.cpp llama cli -hf unsloth/Qwen3.8-27B-GGUF:UD-IQ2\_S  
\---

![[笔记同步助手/images/8593b2f7f03ff5b6b9c19abffc417f27_MD5.jpg]]

---

**🧵 作者续推（2）**

> **2/** @UnslothAI 传送门👉🏻  
> [huggingface.co/unsloth/Qwen3.8-27B-GG…](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)

> **3/** 🚀MacBook Pro M1 16G内存，实测 bit-2 部署  
>   
> 👇  
>   
> [x.com/lonely\_\_mh/status/2090287811106…](https://x.com/lonely__mh/status/2090287811106906313?s=46&t=rV0Jfn54zxsvYDMyr_vq-w)

---

## 💬 评论（25）

> **雪瑜 @xueyu1125**
> 
> 这个我前两天跑过了没有太大意义，只有4token/s的速度，和玩具一样  
>   
> [x.com/xueyu1125/status/20895979871694…](https://x.com/xueyu1125/status/2089597987169476760?s=20)

> **Wei佳 @LiuweijiaVip**
> 
> 逆天的版本1bit

> **mousepotato @iluciddreaming**
> 
> 低于4bit的能用吗

> **CatKingAC @CatKingAC**
> 
> 跑出来的效果如何

> **老杨啊 | AI产品商业化 @yhslgg**
> 
> 会不会出现，老式打印机的速度。

> **Steven Cheng @stevencheng**
> 
> 这压缩率有点狠，推理速度咋样？

> **AzureFox @YiFox31923**
> 
> 试了一下，跑不动，电脑差点卡死

> **Abhi @Abhi\_Flex**
> 
> How much of the performance is retained?

> **晚晚 @An\_yhl**
> 
> 8G 能跑是能跑，就怕速度先把人劝退😂

> **Ethereal Haven @EtherealHavenn**
> 
> dùng LM Studio có được ko

> **Chris Flores @chrisflores\_us**
> 
> So just so I’m reading this correctly…  
>   
> My spare MacBook Pro M1 8GB can run this?

> **Henry | Ye @HenryY54001**
> 
> 保留了多模态能力，保留了多少？

> **精神科王主任 @wang\_psy01**
> 
> 8G 内存都能跑 27B 了，电脑：我还能再战；内存：你礼貌吗。

> **hoanggxyuuki @h4x0rcCG**
> 
> It can run tool calling ?

> **Loïc Saillant @dev\_loic**
> 
> ce genre de post me hype enormement mais je me demande (noob question) à quoi ça sert ? Le modèle peut certes tourner sur un device avec de petites capacités mais est-ce que ça en fait une alternative efficace à un abo openai or anthropic ? Hormis le côté private

> **winbbry @winbbry**
> 
> 所以8G的 4060也能跑对吗？

> **Adenfly @lyzdenda**
> 
> 有人测试了吗？卡出翔了没？

> **Banana @Marcuscai88**
> 
> 你试过了吗

> **ihatechris @ihate\_chris**
> 
> wow we’ve come a long way in like 8 months

> **AI Mastery Guide @aiseomastery**
> 
> 30GB down to 6GB, that's insane compression

> **小黄人爱炒币 @every99999**
> 
> 还能用吗？ 不会被量化成弱智了吧

> **owen @cngaohui**
> 
> 8g的速度怎么样？有人测试过吗？

> **Alan Y. @AlanY\_dpxwz**
> 
> 1bit量化纯傻逼，跑是能跑，我5070 laptop都能跑出30token/s的decode，但天天死循环，tool call都干不好

> **赖叔 | LaiShu.ai @hiheimu**
> 
> 不太清楚这种极限压缩会有什么适用的场景  
>   
> 都是极客玩家的挑战吗  
>   
> 8G大部分都是个人玩家的选择  
> 但凡想上生产环境、正常使用不都得来个16G以上的配置  
>   
> 而且压缩后的能力是否在线也是值得商榷的  
> 所以我是想不出这种方案有什么 pmf  
>   
> 有人开智吗

> **来用兵-纸上用兵 @davidsouza676**
> 
> 8G Mac：我以前没得选，现在想跑27B  
>   
> 就是不知道模型先思考完，还是风扇先起飞啊哈 [t.co/yrj7Orvh9R](https://t.co/yrj7Orvh9R)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/84047e5d_1787202325326?u=https%3A%2F%2Fx.com%2FLonely__MH%2Fstatus%2F2090110302969081899)