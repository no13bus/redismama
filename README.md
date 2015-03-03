redismama
=========

another redis monitor 

** 原理
- pubnub的优点是多个客户端是实时同步的，信息都是一致的，不会出现客户端得到信息的先后的问题
- 利用pubnub的功能，本地执行脚本（脚本内间隔一段时间publish数据） supervisor管理，