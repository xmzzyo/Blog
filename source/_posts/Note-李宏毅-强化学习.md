---
title: Note-李宏毅-强化学习
tags: []
thumbnail: ''
mathjax: true
toc: true
date: 2020-03-30 20:31:19
categories:
- DL
- RL
description:
---

## 一、Policy Gradient

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684724410.png" alt="img" style="zoom: 50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684791719.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684803598.png" alt="img" style="zoom:50%;" />

## 二、Proximal Policy Optimization (PPO)

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684834162.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684843415.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684851838.png" alt="img" style="zoom:50%;" />

## 三、Q-Learning

###  1. Introduction

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684887546.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684896040.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684942302.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684951476.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684961521.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586684972617.png" alt="img" style="zoom:50%;" />

### 2. Tips

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685001097.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685013831.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685013831.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685061254.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685084450.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685095275.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685109834.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685122258.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685134188.png" alt="img" style="zoom:50%;" />

### 3. Q-Learning for Continuous Actions

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685157214.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685166572.png" alt="img" style="zoom:50%;" />

## 四、Actor-Critic

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685188338.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685198026.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685208061.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685219738.png" alt="img" style="zoom:50%;" />

> **Asynchronous Advantage Actor-Critic (A3C)**

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685233138.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685264745.png" alt="img" style="zoom:50%;" />

<img src="Note-%E6%9D%8E%E5%AE%8F%E6%AF%85-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/clipboard-1586685276913.png" alt="img" style="zoom:50%;" />



