---
title: NLP-Chp8-语法理论
tags: []
thumbnail: ''
mathjax: true
date: 2018-07-14 15:56:27
categories:
	- NLP
description:
---

### 1. 功能合一文法（FUG）

> 采用复杂特征集来描述词、句法规则、语义信息，以及句子的结构功能。
>
> 采用合一运算对复杂特征集进行运算。

设$\alpha$为一个功能描述 FD (Functional Description)，当且仅当$\alpha$可以表示为：$\Bigg( \begin{aligned} f_1=v_1\\ f_2=v_2 \\ \dots\\f_n=v_n\end{aligned}\Bigg)n\ge 1$

其中，$f_i$ 表示特征名， $v_i$ 表示特征值.

可以用复杂特征集描述词汇、规则、句子

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp8-语法理论/57586295.jpg" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp8-语法理论/7285907.jpg" style="zoom:50%;" />

### 2. 词汇功能语法（LFG）

1. 突出词汇的作用，体现“语法结构可以由某些词的意义预示出来”
2. 把功能结构的描述作为语言描述中一个基本的独立层次

**LFG 的两个语法层次结构**

1. 成分结构（Constitute structure, c-结构）
2. 功能结构（Functional structure, f-结构）

**由c-结构经f-描述构造f-结构**

**特点：**

1. 采用复杂特征集表达功能结构
2. 合一运算作为句法-语义分析过程的基本方式
3. 语法信息主要来源于词典中的词汇信息标注
4. 功能结构是无序的

