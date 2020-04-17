---
title: NLP-Chp7-词法分析与词性标注
tags: []
thumbnail: ''
mathjax: true
date: 2018-07-11 15:02:56
categories:
	- NLP
description:
---

### 1. 概 述

### 2. 英语的形态分析

**基本任务**

1. 单词识别
2. 形态还原

### 3. 汉语自动分词概要

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/25160701.jpg" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/47244199.jpg" style="zoom:50%;" />

**汉语自动分词中的主要问题**

1. 汉语分词规范问题
2. 歧义切分字段处理

### 4. 分词与词性标注结果评价方法

**两种测试**

1. 封闭测试/ 开放测试
2. 专项测试/ 总体测试

**评价指标**

1. 正确率(Correct ratio/Precision, P ): 测试结果中正确切分或标注的个数占系统所有输出结果的比例。假设系统输出N 个，其中，正确的结果为n个，那么，$P=\frac{n}{N}$

2. 召回率(找回率) (Recall ratio, R ): 测试结果中正确结果的个数占标准答案总数的比例。假设系统输出N 个结果,其中，正确的结果为 n个，而标准答案的个数为M 个，那么，$R=\frac{n}{M}$

   两种标记： $R_{OOV}$ 指集外词的召回率；$R_{IV}$ 指集内词的召回率。

3. F-测度值(F-Measure): 正确率与找回率的综合值。$F_1=\frac{2\times P \times R}{P+R}$

   <img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/92352949.jpg" style="zoom:50%;" />

   <img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/27224070.jpg" style="zoom:50%;" />

### 5. 自动分词基本算法

1. 有词典切分/ 无词典切分
2. 基于规则的方法/ 基于统计的方法

**最大匹配法** (Maximum Matching, MM)－有词典切分，机械切分

1. 正向最大匹配算法 (Forward MM, FMM)

   <img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/55890904.jpg" style="zoom:50%;" />

2. 逆向最大匹配算法 (Backward MM, BMM)

3. 双向最大匹配算法 (Bi-directional MM)

**最少分词法(最短路径法)**

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/4582013.jpg" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/38190288.jpg" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/18416684.jpg" style="zoom:50%;" />

**基于语言模型的分词方法**

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/53420317.jpg" style="zoom:50%;" />

**基于HMM的分词方法**

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp7-词法分析与词性标注/83713994.jpg" style="zoom:50%;" />

**由字构词 (基于字标注)的分词方法**

> 基本思想：将分词过程看作是字的分类问题。该方法认为，每个字在构造一个特定的词语时都占据着一个确定的构词位置(即词位)。假定每个字只有4个词位：词首(B)、词中(M)、词尾(E)和单独成词(S)，那么，每个字归属一特定的词位。
>
> 该方法的重要优势在于，它能够平衡地看待词表词和未登录词的识别问题，文本中的词表词和未登录词都是用统一的字标注过程来实现的。

**生成式方法与区分式方法的结合**

大部分基于词的分词方法采用的是生成式模型(n-gram)

> 假设 o 是观察值，q 是模型。如果对p(o|q)进行建模,就是生成式模型。其基本思想是：首先建立样本的概率密度模型，再利用模型进行推理预测。要求已知样本无穷多或者尽可能地多。该方法一般建立在统计学和 Bayes 理论的基础之上。

而基于字的分词方法采用区分式模型(B,M,S,E)

> 如果对条件概率(后验概率) p(q|o)进行建模，就是判别式模型。基本思想是：有限样本条件下建立判别函数，不考虑样本的产生模型，直接研究预测模型。表性理论为统计学习理论。

**基于字的区分模型有利于处理集外词，而基于词的生成模型更多地考虑了词汇之间以及词汇内部字与字之间的依存关系。**因此，可以将两者的优势结合起来。

### 6. 未登录词识别

### 7. 词性标注方法

基于规则的词性标注方法
基于统计模型的词性标注方法
规则和统计方法相结合的词性标注方法
基于有限状态变换机的词性标注方法
基于神经网络的词性标注方法