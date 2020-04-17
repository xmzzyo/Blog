---
title: Assign5-MaxFlow
mathjax: true
date: 2018-01-24 09:43:51
tags:
categories:
	- Algorithms
thumbnail: 5-1.png
---

### 1 Load balance

#### 1.1 Basic idea of your algorithm

​	假设有n个任务，m个计算机。我们构造网络如下：设置一个源点与各个任务相连，每条边的容量是1，任务与其对应的计算机节点相连，容量是1，节点汇入汇点，初始容量为$load=m$。我们对这个网络求最大流，如果$maxflow==n$，则说明这个任务分配是合法的。然后对$load$减半，求最大流判断是否存在合法任务分配，若存在则继续减半寻找更小的$maxload$，若不存在，则在$\frac{load}{2} \sim load$中找，这样通过二分寻找最小的$maxload$。

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111417.png)

伪代码：

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111439.png)

#### 1.2 Prove the correctness of your algorithm

当最大流等于任务总数时，此网络表示一个合法分配，通过二分法可以不断缩小范围寻找最小的$maxload$。因此本算法正确。

#### 1.3 Analyse the complexity of your algorithm

Dinic算法时间复杂度为$(N^2M)$，N是结点数，M是边数。N=m+n+2，M=m+n+2*n

### 2 Matrix 

#### 2.1 Basic idea of your algorithm

​	我们设$r_1,r_2...r_n$为行节点，$c_1,c_2...c_m$为列节点。构造网络为源节点与每个行节点相连，边的容量为对应行节点的行之和，将每个列节点与汇点相连，边的容量为对应列节点的列之和，行节点与所有列节点相连，容量为1。

​	 求最大流，若网络中行节点i与列节点j之间有流通过，即$flow=1$，则$matrix[i][j]=1$。

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111447.png)

伪代码：

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111457.png)

#### 2.2 Prove the correctness of your algorithm 

矩阵上每个元素最大为1，因此构造列节点和行节点之间边的容量为1，求解最大流，即最大流等于所有元素之和，满足行之和、列之和的条件。因此算法正确。

#### 2.3 Analyse the complexity of your algorithm

结点数N为$n + m +2$，边数M为$n \times m$，时间复杂度为$O(N^2M)$。

### 3 Unique Cut

#### 3.1 Basic idea of your algorithm

我们首先对网络求最大流，在剩余图中通过DFS分别寻找源s所能到达的节点集合S，和能到达汇点t的集合T，若全集减去S即为T，则说明该网络有唯一划分。

伪代码：

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111507.png)

#### 3.2 Prove the correctness of your algorithm

> 判断最小割的唯一性，由图的割的性质可以知道，割可以将图分为两部分，如果将割边都隔断，两部分依然为连通图。而对于一个图，最大流对应这最小割，最小割中的边都是满流的，也就是在剩余网络中是不连通的，我们使用求解最大流之后的剩余网络，如果去掉割边之后两部分子图分别连通，则割唯一，否则不唯一。 

最小割为找到的S和T之间的边。假设有节点v，若s到v的边不满流，v到t的边不满流，则v既可以划分给S，也可以划分给T，则最小割不是唯一的。若v既不属于S，也不属于T，则S、T不能到达v，即S、T到v的边都是满流的，我们沿着$S\sim v$划分或者$v \sim T$划分都可以，则最小割不是唯一的。

#### 3.3 Analyse the complexity of your algorithm

求最大流时间复杂度为$O(M^2N)$，DFS是$O(M+N)$ 。

### 4 Problem Reduction 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111521.png)

从左上角到右下角，然后从右下角再到左上角的最小花费等价于从左上角到右下角走两次的最小花费。因
此，相当于流为2的最小费用流 。

> 时间复杂度$O(VE)$

时间复杂度为$O(MNC)$ ，C=1，因此为$O(MN)$ 。

### 5 Network Cost 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111534.png)

capacity是n，就可以转换成n个等差序列和，每条边容量为1。

若flow=1，走1a;

若flow=2，走1a+3a;

.......

伪代码：

```c
build_graph(){
for edge(s,t,w){
  for (int i = 1; i <= w; i++){
		addedge(s,t,1,a(2i‐1));//同时添加反向边，反向边费用取相反数，流量为0
  		}
	}
} 
ans = min_cost_max_flow(s,t); 
```

> 时间复杂度$O(fVE)，E=\sum w_i$ 。

边数从M->fM，f是流的大小，时间复杂度为$O(fMN)$ 。

### 6 Maximum Cohesiveness 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111546.png)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111557.png)

> ***证明在  E:\研一课件\算法\《网络流作业第六题的粗劣证明》***

### 7 Maximum flow 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign5-MaxFlow/20190114111607.png)

对于割$Cut=\{A,B\}$ ，$u \in A,v \in B,e=(u,v)，l_e=1$ ，否则$l_e=0$ 。对偶问题是最小割问题。 
