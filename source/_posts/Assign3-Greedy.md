---
title: Assign3-Greedy
mathjax: true
date: 2018-01-25 09:00:09
tags:
categories:
	- Algorithms
thumbnail: 3-1.png
---

### 1 Greedy Algorithm 

首先要求度之和要为偶数，否则不能形成图。每次要进行降序排列，贪婪选择度最大的节点v，记录其度为k，k不能大于节点数，否则两个节点之间肯定有多余edge，不能构成图。然后将这个最大度节点去掉，再将接下来的k个最大的数${d_1\sim d_k}$减一，若v与这些节点相连，我们可以看作去掉v后并将与v连接的edge去掉导致这些节点度减一，若不相连，对于不相连点$v_a$，去掉与其相连的edge\ $v_av_b$，去掉v与其他不是${d_1\sim d_k}$的节点之间的edge\ $vv_c$，连接$vv_a$和$v_bv_c$，度的集合不变，与原问题等价。若其中一个节点的度出现负数，则说明不能形成图。每次循环形成一个子问题，若子问题不能形成图，则原问题也不能形成图，循环到最后可以判断能否形成图。

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign3-Greedy/20190114110942.png)

算法循环n次，每次要进行排序以及数组遍历，因此时间复杂度为$O(n^2\log n)$。

### 2 Greedy Algorithm 

让$f_i$大的先执行。

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign3-Greedy/20190114111018.png)

时间复杂度$O(n\log n)$

### 3 Greedy Algorithm 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign3-Greedy/20190114111040.png)

贪婪选择第一个匹配的字符作为S和T相同的部分，这个相同字符在S中位置是i，在T中是j。形成在S中$i\sim len(s)$和T中$j\sim len(t)$中是否存在相同子序列的子问题。

遍历S和T字符串，贪婪选择第一个S和T相同的字符，并认为它们是S和T相同的部分。假设我们已经得到S字符串后len(s)-1个字符的匹配，并且在T中的匹配位置是k，因此只用在S中的1-k中寻找第一个字符相同的位置即可，因此可以贪婪选择第一个遇到的，求解子问题的过程同理。

算法只用遍历S和T字符串，因此时间复杂度为$O(n)$。

### 4 Greedy Algorithm 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign3-Greedy/20190114111053.png)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign3-Greedy/20190114111102.png)

算法只用排序和遍历数组，因此时间复杂度为$O(n\log n)$。