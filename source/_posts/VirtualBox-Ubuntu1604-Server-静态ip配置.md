---
title: VirtualBox Ubuntu1604 Server 静态ip配置
tags: []
thumbnail: '1.png'
mathjax: true
date: 2018-02-07 20:03:56
categories:
	- Linux
description:
---

### 1 安装ssh

> sudo apt-get install openssh-server

### 2 启动ssh

> service sshd start

检查：

> ps -e | grep sshd

### 3 配置桥接网卡

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/VirtualBox-Ubuntu1604-Server-静态ip配置/50708098.jpg)

网络连接方式：

- Bridged networking 桥接模式

- Network Address Translation (NAT) 网络地址转发

- Host-only networking 仅主机

- Internal networking 内部网络

### 4 配置静态ip

> sudo vim /etc/networking/interface

```shell
auto enp0s8
iface enp0s8 inet static
address 192.168.1.11
netmask 255.255.255.0
```
ip地址要和本机在同一网段：
![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/VirtualBox-Ubuntu1604-Server-静态ip配置/66215780.jpg)

```shell
xmz@userver:~$ ifconfig
enp0s3    Link encap:Ethernet  HWaddr 08:00:27:a0:92:86
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fea0:9286/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:6 errors:0 dropped:0 overruns:0 frame:0
          TX packets:15 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1480 (1.4 KB)  TX bytes:1722 (1.7 KB)

enp0s8    Link encap:Ethernet  HWaddr 08:00:27:b6:50:e2
          inet addr:192.168.1.11  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:feb6:50e2/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:153 errors:0 dropped:0 overruns:0 frame:0
          TX packets:134 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:14614 (14.6 KB)  TX bytes:20699 (20.6 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:160 errors:0 dropped:0 overruns:0 frame:0
          TX packets:160 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:11840 (11.8 KB)  TX bytes:11840 (11.8 KB)

```

重启网络：

> sudo /etc/init.d/networking restart