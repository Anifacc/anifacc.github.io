---
layout: post
title: VPS-Shadowsocks-雅各的天梯
categories:
- Toolkit
---

本GOV的Internet不是 real internet, 而是巨大的 local net, net 内自干五们无处不在, 愤青也无处不在. 信息是被Blocked, and filtered. 本ID 必须要突破出去.

废话说了这么多, 其实就是想科学上网, 获得更多丰富资源. 之前用的红杏, 后来被封. 用 __Lantern__ 到昨日, 虽然有每月500M的限制, 用完之后, 其实还是可以继续使用, 就是连接网速慢些, 忍无可忍. 还是使用付费使用吧.

从月光博客搜索到可以买个VPS, 搭配Shadowsocks来科学上网. 于是乎Google, 看了很多关于VPS+Shadowsocks搭建科学上网的资料,胡乱中,不知使用哪一个, 于是乎, 一直没有买（行动）, 只是在阅读其他人的资料. 杂七杂八看了一堆, 被搞迷糊, 就 __心想__ 这是有点难度的. 直到行动后, 我发现根本不是那么回事. 如同编程, __只有开始编程, 才能编程.__ 莫要花费其余时间看其他教程, 自己不去编程.

又扯淡些许, 进入真题. __Bandwagon Host VPS__ 搭建科学上网之梯.

---

## Action

一开始, 本ID是不知道选用哪家VPS, 就花了好多时间看性价比高的商家, 后来就选了 [Bandwagon Host][1]$19.99的10G - PROMO套餐, 对于搭建梯子,是够用了, 而且还可以支付宝支付呢(因为VISA卡已被剪掉,无法注册Paypel). 本ID的目的目前只是为了搭建梯子, 因为便宜的套餐没有了, 就选择上面的套餐.  

- 先注册账户, 尽量提供真实信息. 
- 选择适合你的套餐
- 购买支付, (国内就Aipay方便, 有Paypel也可以)
- 点击 __services__ 进入 __My Services__, 再点击所购买套餐的 __KiwiVM Control Panel__ 进入控制面板, 在这个里面直接可以进行[shadowsocks的设置][2]：

1 进入 __Root shell - advanced__, update下系统(默认的是Centos 6 x86), 在空白框内键入:

    yum update

之后点击 __Execute__;

2 进行shadowsocks一键安装, 选择控制面板内最下方 __KiwiVM Extras__下的 __Shadowsocks Server__, 点击 __Install Shadowsocks Sever__, 完成后, __go back__, 之后就有 Shadowsocks server controls 信息, 根据IP, 填入Shadowsocks客户端中, 在页面内, 还有对应系统的下载地址, 直接下载Shadowsocks极其方便, 真是极其方便.     

3 下载&[设置 Shadowsocks 客户端][2].  
4 完成.

---

## 后记

其实使用 [Bandwagon Host VPS][1]搭建梯子极其容易, 买下后, 其控制系统中就有Shadowsocks服务端, 只需下载客户端, 进行设计就OK了.  现在想来, 15分钟的时间, 本ID居然花了3h46mins左右时间, 只需 __6.6%__ 的时间 真是醉了. 

So. __WHY__?

因为本ID把它想难了, 实际上行动起来, 根本就不难的.

所以, 先 __行动起来吧__.

---

## 其他


图文详解请参考[搬瓦工搭建SS与VPN教程-紫杉倒影][2], 本ID就是按着这个教程来的, 只进行到可以科学上网, 其他加速啥的, 尚未设置. 

多人共享使用, 请参考[多人共享][3].

---

    Beta 1.0   
    Anifacc   
    2017-03-25 21:25:08
    58mins

---

[1]:    https://bandwagonhost.com/aff.php?aff=14368
[2]:    https://www.carlstedt.cn/archives/876
[3]:    http://itcoding.tk/2016/06/04/fuckGFW01/#0x05-%E5%A4%9A%E4%BA%BA%E5%85%B1%E4%BA%AB