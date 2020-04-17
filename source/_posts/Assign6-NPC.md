---
title: Assign6-NPC
mathjax: true
date: 2018-01-26 15:57:42
tags:
categories:
	- Algorithms
thumbnail: 6-2.jpg
---

### 1 Integer Programming

首先，对于给定的$A,x,b$，可以在多项式时间内验证$Ax\geq b$，因此它是NP问题。
对于一个$3-SAT$问题，对于$x_i$，构造$x_i$，对于$\neg x_i$，构造$(1-x_i)$，比如其中一个子句实例为$\neg x_1 \vee x_2 \vee x_3$，我们构造约束条件：$(1-x_1)+x_2+x_3 \geq 1$。我们可以根据给定的$3-SAT$问题构造对应的线性规划实例。
当子句成立，则其中至少有一个项为$True$，对应的约束也成立。
 因此我们可以得到$3-SAT \leq_P IntegerProgramming$，其是NPC问题。

### 2 Mine-sweeper

对于给定的图$G$、地雷位置，我们对于标注$m$的结点，判断其相连结点是否有$m$个地雷，这一过程在多项式时间内可以完成，因此它是NP问题。
构造结点C，置label为3，对于每个变量$x_i$，设置两个项$x_i,\neg x_i$，连接C与对应的项，比如对于$\neg x_1 \vee x_2 \vee x_3$，连接$C和x_1,x_2,\neg x_3$，并且连接C和两个额外的结点$s\ s'$作为“补充”。
具体图如下：
![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign6-NPC/20190114111714.png)
对于一个assignment，如果$x_i=True$，则将对应结点置1，否则置0，若$C_i$中的项为TRUE的小于3个，可以把$s_i\ s_i'$中的一个或两个置1作为“添头”。
若子句中至少有一个为TRUE，则子句成立，结点周围也可以连接3个地雷。
 $3-SAT \leq_P MineSweeper$，其是NPC问题。

### 3 Half-3SAT

对于给定的Half-3SAT问题和变量的赋值，我们可以在多项式时间内判断其是否满足Half-3SAT，因此它是NP问题。
给定一个3-SAT问题，对于Half-3SAT，我们构建三组子句，第一部分和原3-SAT一样，子句个数为m；第二部分个数为m，设置为永真，比如$x_1 \vee x_2 \vee \neg x_2$；第三部分为2m个相同的子句，为永真或者永假。
若原3-SAT问题有解，第一部分的m个子句为真，第二部分有m个为真，第三部分永假，则可以满足Half-3SAT问题。
若原3-SAT问题无解，则不能满足为真的子句占一半。
$3-SAT \leq_P Half3SAT$，其是NPC问题。

