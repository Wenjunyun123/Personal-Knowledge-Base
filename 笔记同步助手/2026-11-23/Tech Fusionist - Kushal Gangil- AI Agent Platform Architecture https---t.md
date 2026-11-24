---
author: Tech Fusionist | Kushal Gangil
source: X
url: https://x.com/techyoutbe/status/2122771253916508612?s=19
saved: 2026-11-23 22:10:59
tags:
  - 笔记同步助手
id: 2dc7815f-5a16-4554-b1f4-d81f3d941b5f
---

🔗 [在 X 查看原文](https://x.com/techyoutbe/status/2122771253916508612)

AI Agent Platform Architecture [t.co/iDaslmG8WT](https://t.co/iDaslmG8WT)

![](https://pbs.twimg.com/media/HWy05zha0AADDdp.jpg)

---

## 💬 评论（2）

> **跨界漫游 @Willie95163**
> 
> 架构图画得再全，落地还是那几个坑

> **Avi Chawla @\_avichawla**
> 
> Prompt, context, harness & loop engineering, clearly explained!  
>   
> An agent is a while loop with four layers of engineering wrapped around it:  
>   
> \- Prompt engineering  
> \- Context engineering  
> \- Harness engineering  
> \- Loop engineering  
>   
> Each one wraps the last, and the model sits in the middle, so none of them compete with the others. Instead, they just zoom one level further out.  
>   
> \> Prompt engineering:  
>   
> This defines the input the model sees on one call, often composed of a role, instructions, examples, and an output format.  
>   
> The techniques here alter the internal computation and reasoning the model goes through due to the wording it sees:  
>   
> \- Chain-of-thought makes it work in steps before answering  
> \- Few-shot examples define the format and the edge cases  
> \- A JSON schema or XML tags make the output parseable by code  
> \- Self-consistency samples a few chains and takes the majority  
>   
> \> Context engineering:  
>   
> It's everything the model sees on a turn, not just the prompt. That includes the query, retrieved docs, memory, prior turns, and tool outputs from earlier steps.  
>   
> The window is finite and fills up fast, so the engineering work is to rank inputs and cut everything that isn't pulling weight.  
>   
> You do this by:  
>   
> \- Retrieving only the chunks relevant to the query, then reranking them  
> \- Keeping key facts out of the middle, where accuracy drops  
> \- Summarizing old turns, evict stale outputs, push big blobs to files  
>   
> \> Harness engineering:  
>   
> It's the code around the model that defines the tools, parses the calls, retries on failure, and can route work to sub-agents so one handles retrieval and another handles code.  
>   
> A verifier then grades the result by running tests, validating a schema, etc.  
>   
> Prompt and context involve getting one call right. The harness involves everything that has to happen around that call for it to run in a real system.  
>   
> \> Loop engineering:  
>   
> In the usual setup, you manage the outer loop, i.e, you write a prompt, read the turns the agent runs, write the next prompt, and repeat, while catching failures.  
>   
> This layer hands that job to the agent itself. It kicks off on a schedule or an event, and runs many turns with no prompt in between.  
>   
> A loop inherently doesn't know when it's finished. An agent can report that it's done and halt while the tests still fail. So the stop can't be the agent's word, but rather it has to be a real signal, like:  
>   
> \- A turn and token cap to stop stuck runs  
> \- A no-progress detector to catch repeated calls  
> \- A completion check to verify the goal with a separate model or a deterministic test  
>   
> By this layer, you're operating on the whole run, so the engineering moves from writing each prompt to setting the goal and the stop conditions up front and letting it run.  
>   
> A longer run also makes the cost of the layers underneath it grow.  
>   
> When a tool returns a 50K-token response and nothing removes it, the model reads it again on every later call. Over a loop of twenty steps, one response turns into hundreds of thousands of tokens.  
>   
> I wrote a full breakdown of where an agent's tokens actually go and how a harness keeps context flat, using TrueForge, an open-source harness that turns an LLM into a working agent.  
>   
> GitHub repo: [github.com/truefoundry/trueforge](http://github.com/truefoundry/trueforge)  
>   
> (don't forget to star it ⭐ )  
>   
> It covers offloading large tool outputs to files, subagents for context isolation, Code Mode for multi-tool joins, and compaction.  
>   
> It also has a benchmark of three harnesses on the same 14 tasks, where TrueForge reached the same answers on about 40% of the tokens Claude Managed Agents used.  
>   
> You can read my full article below.

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/e33f742c_1795443058015?u=https%3A%2F%2Fx.com%2Ftechyoutbe%2Fstatus%2F2122771253916508612)