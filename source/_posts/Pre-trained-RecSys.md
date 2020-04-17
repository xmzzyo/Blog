---
title: Pre-trained RecSys
tags: []
thumbnail: ''
mathjax: true
date: 2019-01-30 17:04:30
categories:
	- 推荐系统
description:
---

## Pre-train BERT Model for RecSys

### 1.Dataset statistics

| Dataset       | #users | #items | avg_action/user | avg_action/item | #action |
| ------------- | ------ | ------ | --------------- | --------------- | ------- |
| Book          | 603668 | 367982 | 14.7            | 24.2            | 8898041 |
| Movies_and_TV | 123960 | 50052  | 8.7             | 21.7            | 1084572 |
| Digital_Music | 5541   | 3568   | 11.7            | 18.1            | 64706   |

使用数据量较小的[Digital_Music](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Digital_Music_5.json.gz)进行训练。

### 2.训练过程

#### 数据预处理

统计每个用户的action，过滤掉出现次数少于5的user、item，并按**unixReviewTime**排序

**sequence长度统计：**

| max  | min  | average | median | std  |
| ---- | ---- | ------- | ------ | ---- |
| 578  | 5    | 11.7    | 7      | 18.2 |

**split sequence:**

根据time span分割：

1. 固定间隔：

   两个连续action的时间间隔大于max_time_interval，就分割

   [Real-time Personalization using Embeddings for Search Ranking at Airbnb](https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb)中，30分钟无click，就划为一个session

2. 按子序列最大间隔分割：

   每次挑选序列时间间隔最大的action进行分割，直到每个子序列长度小于max_length

第2种方法分割的时间间隔比较adaptive，并且可以约束max_length，暂时使用第2种方法分割sequence来进行Next Sentence Prediction

#### 训练

**Requirements：**

[pytorch-pretrained-BERT](https://github.com/huggingface/pytorch-pretrained-BERT)

> ```powershell
> pip install pytorch-pretrained-bert
> ```

**参数：**

|                         | BERT base | Ours |
| ----------------------- | --------- | ---- |
| hidden_size             | 768       | 512  |
| num_hidden_layers       | 12        | 8    |
| num_attention_heads     | 12        | 8    |
| intermediate_size       | 3076      | 1024 |
| max_position_embeddings | 512       | 128  |

在Digital_Music数据集上训练3个epoch，每个epoch训练所有sample，batch_size为32

训练时间为1h，电脑配置为i5低压CPU(主频1.6GHZ)，8G内存，无GPU

没有GPU训练经验，，估计在当前参数(Ours)下，Book数据集(Digital_Music的一百多倍大小)在16G内存，GPU上2-3天能训练3个epoch？（Book数据集是[Amazon](http://jmcauley.ucsd.edu/data/amazon/index.html)里面最大的数据集，其他类别数据集应该能在更短时间内训练完）

BERT文章中使用BooksCorpus(800M words)、WikiPedia(2500M words)，一共3.3billion，batch_size为256，40个epoch，16个TPU，训练时间为4天

[加速训练技巧](https://github.com/huggingface/pytorch-pretrained-BERT#Training-large-models-introduction,-tools-and-examples)  [Google Colab](https://colab.research.google.com/notebooks/tpu.ipynb) 免费TPU(需翻墙，打不开)

[代码 GitHub](https://github.com/xmzzyo/BERT4RS)

#### 获取item representation

加载训练好的pytorch_model.bin，输入以“|||”分隔的序列，获取all_encoder_layers以及pooled_output

all_encoder_layers[-4:]后四层hidden state concat 作为 feature（Top layers一般效果较好）

*存在问题：随机生成序列，获取item representation，计算item的余弦相似度都是0.99（可能是训练样本太少，参数量太大，epoch小？）*

### 3.TODO

1. Position Embedding:

   推荐系统中的sequence不只含有序列位置信息，还有时间间隔信息

   BERT中的Position Embedding为：

   ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Pre-trained-RecSys/20190130221850.png)

   只含有位置信息，应该加入时间间隔信息 [Context-aware Sequential Recommendation](https://arxiv.org/abs/1609.05787)

   Position Embedding + Time Interval Embedding 

2. 冷启动:

   item冷启动类似于OOV问题。加入其它信息？(product description etc.)；OOV的解决方法？

   user冷启动

3. 训练domain specific parameter:

   长短期依赖：[Long and Short-Term Recommendations with Recurrent Neural Networks](http://iridia.ulb.ac.be/~rdevooght/papers/UMAP__Long_and_short_term_with_RNN.pdf)

   - 短期兴趣：音乐、视频

   - 长期兴趣：读书

4. item聚类

   NLP中的vocab数量有限(几万-几十万)，推荐系统中的item数量较大，使用BERT训练参数量太大

   可以根据item信息(description，review text etc.)使用LDA，或者对user-item矩阵进行矩阵分解等方法对item进行聚类，即不学习item representation，学习cluster representation

   Benefit:

   - 减少计算量，加速训练

   - 增加泛化能力？

   - 多样化推荐
     - 不对item进行推荐，对cluster进行推荐

5. 可解释性

   Self Attention 可视化 [Self-Attentive Sequential Recommendation](https://cseweb.ucsd.edu/~jmcauley/pdfs/icdm18.pdf)



