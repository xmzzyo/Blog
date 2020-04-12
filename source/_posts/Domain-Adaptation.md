---
title: Domain Adaptation
tags: []
thumbnail: ''
mathjax: true
toc: true
date: 2020-03-30 18:37:17
categories:
- DL
description:
---

## Domain Adaptation 不同分类方式

1. 是否有监督

- 半监督适应性算法（Semi-supervised Adaptation）：基于Covariate Shift的方法和基于共享表示（shared representation）学习的方法。

- 监督适应性算法（Supervised Adaptation）：基于特征的方法（Feature-Based Approaches）和基于参数的方法（Parameter-Based Approach）。

2. Shallow Domain Adaptation：

- 基于Instance，加不同权重矫正样本偏差
- 基于feature，common feature space
- 基于迭代，训练中不断加入带标签伪数据修改模型

