---
author: 技术爬爬虾
source: AI整理 - 视频号
url: https://weixin.qq.com/sph/AXWhful4N4
saved: 2026-08-14 18:06:23
tags:
  - 笔记同步助手
id: ba0e2e1e-0f9f-43d4-bc1f-52dbf33fbd9b
---

作者：技术爬爬虾

来源：技术爬爬虾视频教程《白嫖Cloudflare最优CDN给自己网站加速》

## 一、背景与原理

Cloudflare 提供了免费的 CDN、DDoS 防御、隐藏源站 IP 等大量好用的免费服务。然而 Cloudflare 在国内俗称"减速器"——网站接入 CDN 之后，国内访问速度反而可能变慢。

本教程介绍一种技巧：在搭建网站时，分别为联通、移动、电信、境外配置最优的 CDN 节点，然后根据用户的网络环境，自动选择最优的 CDN 节点提供服务。不花一分钱就能给网站提速，尽情白嫖 Cloudflare 的免费服务，同时避免"减速器"副作用。

### Cloudflare CDN 工作原理

Cloudflare 的 CDN 服务通过遍布全球的数据中心缓存网站的静态资源，例如 JS、CSS、图片和视频。访客请求这些数据时，可以直接从地理位置最近的 CDN 节点读取，加快加载速度并减轻源服务器压力。

## 二、前提条件

整套配置需要以下资源：

-   两个域名：例如主力域名 `tech-shrimp.com` 和辅助域名 `tech-shrimp.top`；
-   一台云服务器：上面用 nginx 发布了一个简单网站；
-   一个 Cloudflare 账号。

## 三、网络拓扑与整体思路

整个访问链路如下：

1.  浏览器请求 `tech-shrimp.com` 主域名；
2.  该域名做了 CNAME，等同于请求 `cdn.tech-shrimp.top`；
3.  对 `cdn.tech-shrimp.top` 做分线路 DNS 解析，将请求分流到各自最优的 Cloudflare CDN 节点；
4.  CDN 节点识别请求头中的 Host 等于 `tech-shrimp.com`，将请求路由到回退源地址 `origin.tech-shrimp.top`；
5.  `origin.tech-shrimp.top` 解析到源服务器 IP，完成回源。

![网络拓扑图：浏览器 → cdn.tech-shrimp.top（线路优选）→ Cloudflare CDN 节点（自定义主机回源）→ origin.tech-shrimp.top → 源服务器](https://relay-1.bijitongbu.site/p/303226f5a7892c50bbb29e19c0c7e19f.jpg)

网络拓扑图：浏览器 → cdn.tech-shrimp.top（线路优选）→ Cloudflare CDN 节点（自定义主机回源）→ origin.tech-shrimp.top → 源服务器

## 四、具体配置步骤

### 第一步：配置 DNS 指向源服务器

进入 Cloudflare 中 `tech-shrimp.top` 的 DNS 记录页面，添加一条 A 记录：

-   类型：A
-   名称：origin
-   IPv4 地址：源服务器的公网 IP
-   代理状态：开启（小黄云）

开启代理后，来自浏览器的数据会先经过 Cloudflare CDN 节点再到达源服务器，从而隐藏真实 IP 并提供免费 DDoS 防御。

![Cloudflare DNS 页面添加 origin.tech-shrimp.top 的 A 记录并开启小黄云代理](https://relay-1.bijitongbu.site/p/4ee2fe37baeeea6f740cca3e455e1f73.jpg)

Cloudflare DNS 页面添加 origin.tech-shrimp.top 的 A 记录并开启小黄云代理

### 第二步：配置自定义主机名（回退源）

由于 `origin.tech-shrimp.top` 只是辅助域名，最终要给用户呈现的是主力域名 `tech-shrimp.com`。这里使用 Cloudflare 的 **Custom Hostnames（自定义主机回源）** 功能。

操作路径：在 `tech-shrimp.top` 域名下，进入 `SSL/TLS → 自定义主机名`。注意：进入该页面需要先绑定支付方式（可使用 PayPal 绑定免费服务）。

添加自定义主机名的步骤：

1.  点击"添加回退源"，回退源地址填写 `origin.tech-shrimp.top`；
2.  点击"添加自定义主机名"，主机名填写主力域名 `tech-shrimp.com`，其余选项保持默认。

添加后会提示需要进行 TXT 记录验证所有权。前往主力域名 `tech-shrimp.com` 的 DNS 页面，添加一条 TXT 记录：

-   类型：TXT
-   名称：`_cf-custom-hostname`（保留 CF 提示的前缀，删掉后面的域名部分）
-   内容：粘贴 Cloudflare 给出的验证值

保存后回到自定义主机名页面刷新，验证状态显示为绿色即表示配置完成。

![Cloudflare SSL/TLS 自定义主机名页面，添加 tech-shrimp.com 作为自定义主机名](https://relay-1.bijitongbu.site/p/18e31cf249c7340385dce8cc2050a2de.jpg)

Cloudflare SSL/TLS 自定义主机名页面，添加 tech-shrimp.com 作为自定义主机名

![在主力域名 DNS 页面添加 TXT 验证记录](https://relay-1.bijitongbu.site/p/8f93fd40bc74633f187d0a39f63129ab.jpg)

在主力域名 DNS 页面添加 TXT 验证记录

![自定义主机名验证状态变为绿色、所有权验证通过](https://relay-1.bijitongbu.site/p/8d225a824186628160e993829ddc1319.jpg)

自定义主机名验证状态变为绿色、所有权验证通过

### 第三步：引入 CDN 子域名做线路分流

再新增一个子域名 `cdn.tech-shrimp.top`，借助对它的解析达成联通、电信、境外等线路的 DNS 解析分流。

配置方法很简单：在 `tech-shrimp.top` 的 DNS 页面添加一条 CNAME 记录：

-   类型：CNAME
-   名称：cdn
-   目标：填写社区整理好的线路优选 CNAME 域名（本质是"抄作业"，社区有不少已配置好的公共优选域名可用）
-   代理状态：**必须关闭小黄云**

完成后，访问 `cdn.tech-shrimp.top` 的流量会自动流经各自最优的 Cloudflare CDN 节点。

![为 cdn.tech-shrimp.top 添加 CNAME 记录指向社区优选域名，并关闭小黄云](https://relay-1.bijitongbu.site/p/01af3284eca2885f52863dad9a18b248.jpg)

为 cdn.tech-shrimp.top 添加 CNAME 记录指向社区优选域名，并关闭小黄云

### 第四步：将主域名 CNAME 到 CDN 子域名

回到主力域名 `tech-shrimp.com` 的 DNS 页面，添加一条 CNAME 记录：

-   类型：CNAME
-   名称：@
-   目标：`cdn.tech-shrimp.top`
-   代理状态：**必须关闭小黄云**（这是关键，否则会被 Cloudflare 再次代理，与线路优选逻辑冲突）

至此所有配置完成。

![为主域名 tech-shrimp.com 添加 CNAME 指向 cdn.tech-shrimp.top，且关闭小黄云](https://relay-1.bijitongbu.site/p/0bb5ba122fa34f7f57f5bc880b21ebc8.jpg)

为主域名 tech-shrimp.com 添加 CNAME 指向 cdn.tech-shrimp.top，且关闭小黄云

## 五、效果测试

访问 `https://tech-shrimp.com` 进行测速对比：

-   **直连测速**：平均响应约 191 ms，且出现响应超时；
-   **使用优选 CDN 节点后**：平均响应降到约 127 ms，无响应超时。

作为对照，作者还配置了一个开启小黄云的子域名 `test.tech-shrimp.com`（未做线路优选）：测试时下载出现 22 次访问失败，主要出口节点仅有两个（104.x 和 172.x 的 Cloudflare IP），节点资源少且固定，遇到节点不佳时失败率高。

而做了优选的主力域名 `tech-shrimp.com` 出口节点明显增多，按各家运营商线路做了优选，访问失败极少。

![优选 CDN 后的测速结果：127 ms、无超时](https://relay-1.bijitongbu.site/p/0ddcc561ac25a031b738f9d5e0d15fdb.jpg)

优选 CDN 后的测速结果：127 ms、无超时

![未做优选的 test.tech-shrimp.com 下载测试，22 次失败、出口节点仅两个](https://relay-1.bijitongbu.site/p/747bac4520ff70af7a8387b4fb485d7f.jpg)

未做优选的 test.tech-shrimp.com 下载测试，22 次失败、出口节点仅两个

![做了优选的主力域名下载测试：出口节点丰富，仅极少数失败](https://relay-1.bijitongbu.site/p/80cc568129f094df51a6abe1aa57fb7f.jpg)

做了优选的主力域名下载测试：出口节点丰富，仅极少数失败

## 六、要点回顾

-   需要一个辅助域名做回源（origin）和一个子域名做线路优选（cdn）；
-   主域名通过 CNAME 指向 CDN 子域名（关闭代理），由 CDN 子域名借助社区优选 CNAME 完成线路分流；
-   CDN 节点通过 Custom Hostnames 把 Host 头是主域名的请求回源到 origin 域名；
-   所有"小黄云"代理状态要按角色开关：origin 开启，主域名与 cdn 子域名关闭。

## 全文整理

Cloudflare 有免费的 CDN、DDoS 防御、隐藏源站 IP 等一大堆好用的免费服务。不过 Cloudflare 在国内俗称"减速器"，网站用上 CDN 之后，国内访问速度反而会变慢。今天爬爬虾介绍一个技巧：在搭建网站的时候，根据用户的网络环境自动选择最优的 CDN 节点进行服务，不花一分钱给自己的网站提速，尽情白嫖 Cloudflare 的免费服务，而不用担心网站变慢的副作用。

正式教程开始之前，先介绍一下原理。Cloudflare 的 CDN 服务通过遍布全球的数据中心缓存客户网站的静态资源，比如 JS 文件、CSS、图像和视频。网站访客请求这些数据时，可以直接从地理位置最近的 CDN 节点读取，加快网站加载速度并减少服务器压力。下面来看如何给自己的网站配置最优 CDN 线路。

这套操作的前提是必须有两个域名。以我自己为例，我有两个域名，一个是 techtromp.com 这个主力域名，还有一个是 techshrimp.top 这个辅助域名。我还有一台云服务器，上面用 Nginx 发布了一个很简单的网站。

第一步，在 Cloudflare 里配置 DNS。这里将域名 origin.techshrimp.top 解析到我的网站，并打开小黄云，这样 Cloudflare 的 CDN 就开启了。来自浏览器的请求会先经过 Cloudflare 的 CDN 节点，再到达我的服务器，从而隐藏真实 IP 并提供免费的 DDoS 防御。

由于 origin.techshrimp.top 只是辅助域名，我希望最终给用户呈现的是主力域名。此处使用了 Cloudflare 的自定义主机名回源服务，简单来说就是给 Cloudflare 的 CDN 节点增加一条配置：当 CDN 节点收到网络请求，如果其中的 header 的 host 值等同于我配置的自定义主机名（本例中是 techtromp.com），则将请求路由到回退源地址，也就是让 origin.techshrimp.top 等同于我的服务器。

第二步，实现 CDN 节点的线路优选，也就是让联通、电信、境外都配置各自最优的 CDN 节点。这里需要再引入一个子域名 cdn.techshrimp.top，借助对它的解析实现联通、电信、境外等线路的 DNS 解析分流。配置起来也很简单，只需要把它 CNAME 到一个已经配置好线路分流的域名即可。这是一种抄作业的做法，但简单好用。社区里有不少已经配置好的公共优选 CNAME 域名地址，本次教程使用的是其中一个。这样访问 cdn.techshrimp.top 的流量都会自动流经各自最优的 CDN 节点。

最后，再添加一条 CNAME，将 techtromp.com 这个主域名与 cdn.techshrimp.top 关联起来，这样就大功告成了。

再看一下网络拓扑：浏览器请求 techtromp.com 域名，由于做了 CNAME，等同于请求 cdn.techshrimp.top；这里使用了分线路解析，分流至最优的 Cloudflare CDN 节点；CDN 节点配置了自定义主机名回源，发现请求的地址是 techtromp.com，那就应该路由到回源地址，也就是 origin.techshrimp.top；最后 origin.techshrimp.top 指向我的服务器。至此整个网络流程结束。

我们马上进入实战环节，也会穿插这个流程图进行讲解。

第一步：回退源地址指向我的服务器。这是我用 Nginx 发布的一个小网站，里面东西很简单，一个标题加三张图片。这个网站发布到我的服务器上，这是它的公网 IP。

第二步：将域名托管到 Cloudflare。这里是 techshrimp.top 这个域名，点进去以后给它配置 DNS。点击"DNS 记录"，点击"添加记录"：类型 A，前缀 origin，IPv4 地址填服务器的 IP 地址。注意把代理状态开启，也就是显示小黄云，那就完成了。

第三步：自定义主机回退源。还是 techshrimp.top 这个域名，点击这里的 SSL/TLS，点击"自定义主机名"。这里需要绑定一个支付方式才能进入这个页面，我选择的是 PayPal 的方式。绑定好以后选择免费服务。进入这个页面以后，开始添加回退源，就是刚才配置的 DNS origin.techshrimp.top，点击"添加回退源"。然后点击"添加自定义主机名"，这里填写主力域名 techtromp.com，下面默认，直接点击"添加自定义主机名"。这里主机名状态显示错误，展开后发现需要验证这个域名的所有权。

新开一个窗口进入第二个域名 techtromp.com 进行配置，点击"DNS 记录"。按照要求填写一条 TXT 类型的记录，把值复制过来。点击"添加记录"，类型选择 TXT，把后面域名这一段删掉只留主机名，内容部分粘贴刚才的值，点击保存，这就配置完成了。再回到刚才的页面点击刷新，显示出绿色，两边都有效，那就配置完成了。

第四步：再引入一个新域名 cdn.techshrimp.top，借助它实现 DNS 线路分流。进入 techshrimp.top 域名的 DNS 记录，点击"添加记录"，类型选择 CNAME，名称填写 cdn，目标使用社区解析好的地址并复制过来。这里注意一定要把小黄云关闭，点击保存。

第五步：设置 CNAME。回到 Cloudflare，进入主力域名 techtromp.com，点击"DNS 记录"，点击"添加记录"，类型选择 CNAME，名称填 @，目标填写 cdn.techshrimp.top。这一步的重点是把小黄云关掉。好，大功告成，至此所有配置都完成了。

试着访问一下 [https://techtromp.com。在测速网站上直连的平均速度大约是](https://techtromp.com%E3%80%82%E5%9C%A8%E6%B5%8B%E9%80%9F%E7%BD%91%E7%AB%99%E4%B8%8A%E7%9B%B4%E8%BF%9E%E7%9A%84%E5%B9%B3%E5%9D%87%E9%80%9F%E5%BA%A6%E5%A4%A7%E7%BA%A6%E6%98%AF) 191 毫秒，还有一个响应超时。再试一下使用优选 CDN 节点后的速度，提高到 127 毫秒，没有响应超时。

这里我配置了一个子域名 test.techshrimp.com，使用它开启了小黄云连接到我的服务器，没有做线路优选。先带着协议测一下下载速度，结果 22 个访问失败，主要出口节点只有两个，104 的和 172 的，Cloudflare 给分配的就是这两个节点。如果这两个节点情况不好，就很容易造成失败。

再看一下做了优选以后的效果，也就是我的主力域名。它的出口节点变多了，根据各自的运营商线路都做了优选，这里访问失败只有一个福建泉州了，听说福建泉州已经开始推进 IP 白名单。

这里是技术扒爬虾，我会定期分享一些有趣实用的编程项目，分享一些提升效率的黑科技软件。今天的视频就到这里，感谢大家，我们下期再见。

视频时长 7分26秒 · 消耗 38 积分 · 积分余额 851

AI整理设置可以[点此调整](https://my.bijitongbu.site/settings)

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c3a21926-b0b2-40a7-98be-38aee5740eb8?u=https%3A%2F%2Fweixin.qq.com%2Fsph%2FAXWhful4N4&s=vtoa)