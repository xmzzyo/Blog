---
title: NLP-Chp9-句法分析
tags: []
thumbnail: ''
mathjax: true
date: 2018-07-14 20:01:29
categories:
	- NLP
description:
---

### 1. 概述

**类型：**

1. 短语结构分析(Phrase parsing)
   - 完全句法分析(Full parsing)
   - 局部句法分析(Partial parsing)
2. 依存句法分析(Dependency parsing)

### 2. 短语结构分析

英语中的结构歧义随介词短语组合个数的增加而不断加深的，这个组合个数我们称之为开塔兰数，$C_N=\Bigg( \begin{aligned}2n \\ n\end{aligned}\Bigg)\frac{1}{n+1}=\frac{(2n)!}{(n!)^2(n+1)}$

**基本方法和开源的句法分析器：**

1. 基于CFG规则的分析方法：

   线图分析法(chart parsing) 
   CYK 算法
   Earley (厄尔利)算法
   LR 算法 / Tomita 算法 … …

   - Top-down: Depth-first/ Breadth-first
   - Bottom-up

2. 基于 PCFG 的分析方法 PCFG: Probabilistic Context-Free Grammar

### 3. 线图分析法

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/66788476.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/32594558.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/29679548.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/77759849.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/48133533.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/57488942.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/8184354.jpg)

**Chart算法的时间复杂度为：**
$O(Kn^3)$ (K 为一常数, n是句子长度)

### 4. CYK分析算法

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/46208169.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/28024299.jpg)



![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/79891438.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/14010626.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/77743394.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/43168851.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/57532977.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/26327949.jpg)

### 5. 概率上下文无关文法（PCFG）

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/71881730.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-15/10801535.jpg)

### 6. 依存句法分析

> 在依存语法理论中，“依存”就是指词与词之间支配与被支配的关系，这种关系不是对等的，而是有方向的。

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-16/31324242.jpg)

**对依存图和依存树的形式约束为：**

1. 单一父结点(single headed)
2. 连通(connective)
3. 无环(acyclic)
4. 可投射(projective)

> 由此来保证句子的依存分析结果是一棵有“根(root) ”的树结构。

**建立一个依存句法分析器一般需要完成以下三部分工作：**

1. 依存句法结构描述
2. 分析算法设计与实现
3. 文法规则或参数学习

**目前依存句法结构描述一般采用有向图方法或依存树方法，所采用的句法分析算法可大致归为以下4类：**

1. 生成式的分析方法(generative parsing)
2. 判别式的分析方法(discriminative parsing)
3. 决策式的(确定性的)分析方法(deterministic parsing)
4. 基于约束满足的分析方法(constraint satisfaction parsing) 

### 7. 依存句法分析器性能评价

1. 无标记依存正确率(unlabeled attachment score, UA)：

   > 所有词中找到其正确支配词的词所占的百分比，没有找到支配词的词(即根结点)也算在内。

2. 带标记依存正确率(labeled attachment score, LA)：

   > 所有词中找到其正确支配词并且依存关系类型也标注正确的词所占的百分比，根结点也算在内。

3. 依存正确率(dependency accuracy, DA)：

   > 所有非根结点词中找到其正确支配词的词所占的百分比。

4. 根正确率(root accuracy, RA)：有两种定义方式：

- 正确根结点的个数与句子个数的比值；

- 另一种是所有句子中找到正确根结点的句子所占的百分比。

  对单根结点语言或句子来说，二者是等价的。

5. 完全匹配率(complete match, CM)：所有句子中无标记依存结构完全正确的句子所占的百分比。

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-16/1559529.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-16/67633229.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-17/61531300.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-7-17/95529832.jpg)

