Weixin API Mockup
==

微信公众平台目前允许 3 种类型的账号：订阅号、服务号、企业号。我们的目标即是解决上述 3 种账号的开发过程中遇到的困难，后不再分开说明。

## 遇到了什么问题？

开发者必须准备一个能在公开网络上访问的服务器（最好还要有个域名）以及注册并通过微信的一系列认证。这对于开发初始阶段来说得不偿失，你甚至没有 fail fast 的机会。测试号及沙盒的推出稍稍缓解的问题，但仍然有诸多不便。

其次，将纯粹的开发过程与微信的服务器乃至办公室的网速紧紧耦合在一起，这显然是不对的。

我们的目标就是解耦。

## 粉丝在使用微信时有哪几种场景？


