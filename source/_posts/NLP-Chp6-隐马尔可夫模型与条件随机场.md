---
title: NLP-Chp6-隐马尔可夫模型与条件随机场
tags: []
thumbnail: ''
mathjax: true
date: 2018-07-09 08:53:45
categories:
	- NLP
description:
---

**NLP中概率图模型的演变**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp6-隐马尔可夫模型与条件随机场/20559589.jpg)

### 1. 马尔可夫模型

> 马尔可夫模型(Markov Model):
>
> 如果在特定情况下，系统在时间 t 的状态只与其在时间 t-1 的状态相关，则该系统构成一个离散的一阶马尔可夫链：$p(q_t = S_j | q_{t-1} =Si ,q_{t-2} =Sk , \dots) =p(q_t = S_j | q_{t-1}=S_i )$
>
> 如果只考虑公式独立于时间 t 的随机过程，即所谓的不动性假设，状态与时间无关，那么$p(q_t = S_j | q_{t-1}=S_i )=a_{ij}$
>
> $s.t. a_{ij}>0\ \sum\limits_{j=1}^Na_{ij}=1$
>
> 马尔可夫模型又可视为随机的有限状态自动机 

### 2. 隐马尔可夫模型

> 该模型是一个双重随机过程，我们不知道具体的状态序列，只知道状态转移的概率，即模型的状态转换过程是不可观察的（隐蔽的），而可观察事件的随机过程是隐蔽状态转换过程的随机函数

> 三个问题：
>
> (1)在给定模型$\mu=(A, B, \pi)$ 和观察序列 $O＝O_1O_2 …O_T$的情况下，怎样快速计算概率 $p(O|\mu)$？
> (2)在给定模型 $\mu=(A, B, \pi)$和观察序列 $O＝O_1O_2 …O_T$的情况下，如何选择在一定意义下“最优”的状态序列 $Q = q_1 q_2 … q_T$，使得该状态序列“最好地解释”观察序列？
> (3)给定一个观察序列$O＝O_1O_2 …O_T$ ，如何根据最大似然估计来求模型的参数值？即如何调节模型的参数，使得$p(O|\mu)$ 最大？

### 3. 前向算法

**快速计算观察序列概率$p(O|\mu)$**

**动态规划**

**前向变量**

$\alpha_t(i)=p(O_1O_2O_3\dots O_t,q_t=S_i|\mu)$

> 先输出序列，后状态转移，前面一段

$P(O|\mu)=\sum\limits_{S_i}p(O_1O_2O_3\dots O_t,q_t=S_i|\mu)=\sum\limits_{i=1}^N\alpha_T(i)$

**递推式：时间t+1：**

$\alpha_{t+1}=[\sum\limits_{i=1}^N\alpha_t(i)a_{ij}]\times b_j(O_{t+1})$

> N个状态

**初始化：**

$\alpha_1(i)=\pi_ib_i(O_1)$

**结束：**

$P(O|\mu)=\sum_{i=1}^N\alpha_T(i)$

**时间复杂度：**

$O(N^2T)$

### 4. 后向算法

**后向变量**

$\beta_t(i)=p(O_{t+1}O_{t+2}O_{t+3}\dots O_T,q_t=S_i|\mu)$

> 先状态转移，再输出序列，后面一段

**归纳顺序：**

$\beta_T(x),\beta_{T-1}(x),\beta_{T-2}(x)\dots\beta_1(x)$

**初始化：**

$\beta_T(i)=1$

**递推公式：**

$\beta_t(i)=\sum\limits_{j=1}^Na_{ij}b_j(O_{t+1})\beta_{t+1}(j)$

> N个状态

**输出结果：**

$p(O|\mu)=\sum\limits_{i=1}^N\beta_1(i)\pi_1b_1(O_1)$

**时间复杂度：**

$O(N^2T)$

### 5. Viterbi 搜索算法

**如何发现“最优”状态序列能够“最好地解释”观察序列**

$\gamma_t(i)=p(q_t=S_i|O,\mu)=\frac{p(q_t=S_i,O|\mu)}{p(O|\mu)}$

$p(a_t=S_i,O|\mu)=\alpha_t(i)\times\beta_t(i)$

**每一个状态单独最优不一定使整体的状态序列最优**

**Viterbi 变量 $\delta_t(i)$是在时间 t 时，模型沿着某一条路径到达 $S_i$，输出观察序列$ O＝O_1O_2 …O_t$ 的最大概率为：**

$\delta_t(i)=\max\limits_{q_1,q_2\dots q_{t-1}}p(q_1,q_2,\dots,q_t=S_i,O_1,O_2,\dots,O_t|\mu)$

**递推公式：**

$\delta_{t+1}(i)=\max\limits_j[\delta_t(j)a_{ji}]\times b_i(O_{t+1})$

**初始化：**

$\delta_1(i)=\pi_ib_i(O1)$

$\psi_t(j)=\arg\max\limits_j[\delta_t(j)a_{ji}]\times b_i(O_{t+1})$

**回溯得到路径**

**时间复杂度：**

$O(N^2T)$

### 6. 参数学习

**前向后向算法**

**在时间t状态为$S_j$，在时间t+1状态为$S_i$概率为：**

$\varepsilon_t(i, j)=\frac{\alpha_t\times a_{ij}b_j(O_{t+1})\times \beta_{t+1}(j)}{\sum_{i=1}^N\sum_{j=1}^N\alpha_t\times a_{ij}b_j(O_{t+1})\times \beta_{t+1}(j)}$

**给定模型$\mu$和观察序列$ O＝O_1O_2 …O_t$ ，在时间 t位于状态$ S_i$ 的概率为：**

$\gamma_t(i)=\sum_{j=1}^N\varepsilon_t(i,j)$

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp6-隐马尔可夫模型与条件随机场/65577340.jpg)

### 7. HMM应用举例

分词和词性标注问题：

1. 分词：概率最大的输出序列，$P(O|\mu)$
2. 词性标注：最优状态序列，$P(Q|O,\mu)$

### 8. CRFs及其应用

**定义：**

> 设 G=(V, E) 为一个无向图，V为结点集合，E为无向边的集合，$Y = \{Y_v | v\in V\}$，即V中每个结点对应于一个随机变量 $Y_v$, 其取值范围为可能的标记集合 {y}。如果以观察序列X为条件，每个随机变量 $Y_v$都满足以下马尔可夫特性：
>
> $p(Y_v|X,Y_w,w\neq v)=p(Y_v|X,Y_w,w\sim v)$
>
> 其中，$w\sim v $表示两个结点在图中是邻近结点。那么，(X, Y) 为一个条件随机场。

**在给定观察序列X 时，某个特定标记序列Y的概率可以定义为：**

$exp(\sum_j\lambda_jt_j(y_{i-1},y_i,X,i)+\sum_k\mu_ks_k(y_i,X,i))$

其中，$t_j(y_{i-1},y_i,X,i)$是转移函数，$s_k(y_i,X,i)$是状态函数

**特征函数可以统一表示为：**

$F_j(Y,X)=\sum_{i=1}^nf_i(y_{i-1},y_i,X,i)$

**条件随机场定义的条件概率可以由下式给出:**

$p(Y|X,\lambda)=\frac{1}{Z(x)}exp(\sum_j\lambda_jF_j(Y,X))$

**三个问题：**

1. 特征选取
2. 参数训练
3. 解码

**应用举例：**

由字构词(基于字标注)的分词方法

>一般情况下，每个字只有4个词位：词首(B)、词中(M)、词尾(E)和单独成词(S) 。

**解码：**

> 条件随机场解码的过程就是根据模型求解的过程，可以由维特比 (Viterbi)算法完成。维特比算法是一个动态规划算法，动态规划要求局部路径也是最优路径的一部分