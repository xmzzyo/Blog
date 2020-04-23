---
title: Deep Reinforcement Learning for Recommender Systems
tags: [强化学习, 推荐系统]
password: 1aa45ed061f8f41b7292a435ae009b9e44b9d0dbc7b76cac50490f783956e667
thumbnail: ''
mathjax: true
toc: true
date: 2020-04-15 16:36:13
categories:
- RecSys
description:
---

## Model-Based Reinforcement Learning with Adversarial Training for Online Recommendation

> 现有方法关注于Model-free的方法，其需要不断与环境交互，成本大。
> Off-Policy方法使用重要性采样可缓解此问题，但需要大量log数据，不适用于大的action space。
>
> - 需要和user交互，探索unexplored action和state space
> - 代价高-探索过程伤害user满意度，丢失用户
>
> 不同的feedback反应用户的不同兴趣：
>
> - clicks-短期兴趣
> - purchase-长期兴趣（在若干click后发生）

> Model-free 方法不显式建模agent-user的交互。
>
> - value-based方法，如Deep Q-learning，不稳定，不易收敛
> - policy-based方法，如policy gradient，稳定，但由于学习和架构的限制没有实际交互带来data bias；重要性采样可解决data bias，但带来较大variance。

本文根据离线数据构建了用户行为模型，并使用其和agent交互来训练policy（REINFORCE算法）。

- 优点：有效采样、减少离线数据中的噪音
- 缺点：估计的用户行为模型和实际的环境容易有bias、policy经常更新(不一致的推荐)降低用户满意度
- 解决：引入对抗训练(判别器用来判断real or fake 的trajectories)来训练用户行为模型

