---
title: Joint Models for NLP
tags: []
thumbnail: ''
mathjax: true
date: 2019-01-17 09:39:08
categories:
	- NLP
description:
---

## Motivation

**Joint model**

1. Reduce error propagation
2. Allow information exchange between task

**Challenge**

1. Joint learning
2. Search 

**Solutions**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117094814.png)

## Statistical Models

###Graph-Based Methods

**Traditional solution**
• Score each candidate, select the highest-scored output
• Search-space typically exponential

#### Joint Label Structure

***<u>Joint Learning, Joint Search</u>***

**Joint Segmentation and POS tagging**

**Joint Parsing and NER**

#### Reranking

***<u>Separate Learning, Joint Search</u>***

**Joint Segmentation and POS Tagging**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117101631.png)

**Joint Parsing and SRL**

> Rerank k-best parse trees from a probabilistic parser using an SRL system.

#### Joint Modeling (Multi task)

***<u>Separate Learning, Joint Search</u>***

**Joint Entity and Sentiment**

> Optimize the joint objective function which is defined as a linear combination of the potentials from different predictors with a parameter λ to balance the contribution of these two components: opinion entity identification and opinion relation extraction.
>
> ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117102354.png)

#### Joint Modeling (Single task)

***<u>Joint Learning, Joint Search</u>***

**Joint Segmentation and POS Tagging**

> The decoding algorithm for the joint word segmentor and POS tagger, agendas[i] stores the best sequences that end at i

**Joint Entity Relation Extraction**

> Beam Search

###Transition-Based Methods

**Transition-based Dependency Parsing**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117103723.png)

***A Learning+Search Framework***

**• Advantages**
• Low computation complexity
• Arbitrary non-local features
• Learning-guided-search

**• State-of-the-art accuracies and speeds**
• Constituent parsing
• Dependency parsing
• Word Segmentation
• CCG parsing

**• Enable joint models**
• Address complex search space and use joint features, which have been difficult for traditional models

**Joint Segmentation, Tagging and Normalization**

**Joint Segmentation, POS-tagging and Constituent Parsing**

> Traditional: word-based Chinese parsing
>
> This: character-based Chinese parsing
>
> Chinese words have syntactic structures.

**Joint POS tagging and Dependency Parsing**

**Joint Entity and Relation Extraction** 

## Deep Learning Models

### Neural Transition-based Models

***<u>Joint Learning, Joint Search</u>***

**Joint Entity and Relation Extraction** 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117113620.png)

**Joint Parsing and SRL**

**Joint Word Segmentation, POS Tagging and Dependency Parsing**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117140629.png)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117140757.png)

**Joint Extraction of Entities and Relations**

### Neural Graph-based Models (Multi-task Learning)

***<u>Joint Learning, Separate Search</u>***

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117141801.png)

#### Cross Task

**Identifying beneficial task relations**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Joint Models for NLP/20190117142724.png)

#### Cross Domain

#### Cross Lingual

#### Cross Standard

