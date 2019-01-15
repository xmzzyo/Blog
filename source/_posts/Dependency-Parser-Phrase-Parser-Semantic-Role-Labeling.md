---
title: Dependency Parser & Phrase Parser & Semantic Role Labeling
tags: []
thumbnail: ''
mathjax: true
date: 2019-01-12 19:50:08
categories:
	- NLP
description:
---

## Dependency Parser

### 《Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations》

applying it to a greedy transition-based parser as well as to a globally optimized graph-based parser

> Modern approaches to dependency parsing can be broadly **categorized into graph-based and transition-based parsers** (Kübler et al., 2009).
>
> Graph-based parsers (McDonald, 2006) treat parsing as a search-based structured prediction problem in which the goal is learning a scoring function over dependency trees such that the correct tree is scored above all other trees. Transition-based parsers (Nivre, 2004; Nivre, 2008) treat parsing as a sequence of actions that produce a parse tree, and a classiﬁer is trained to score the possible actions at each stage of the process and guide the parsing process.

## Joint

### 《Greedy, Joint Syntactic-Semantic Parsing with Stack LSTMs》

> **Stack LSTMs** (Dyer et al., 2015) are LSTMs that allow for stack operations: query, push, and pop. A “stack pointer” is maintained which determines which cell in the LSTM provides the memory and hidden units when computing the new memory cell contents. 

![](https://raw.githubusercontent.com/xmzzyo/img/master/20190112230510.png)



![](https://raw.githubusercontent.com/xmzzyo/img/master/20190112230653.png)

## Semantic

### 《Deep Semantic Role Labeling: What Works and What’s Next》

#### Abstract

> We use a deep highway BiLSTM architecture with constrained decoding
>
>   (1) deep models excel at recovering long-distance dependencies but can still make surprisingly obvious errors, and (2) that there is still room for syntactic parsers to improve these results.

#### Introduction

> Recently break-throughs involving end-to-end deep models for SRL without syntactic input (Zhou and Xu, 2015; Marcheggiani et al., 2017) seem to overturn the long-held belief that syntactic parsing is a prerequisite for this task
>
> Zhou and Xu (2015) treat SRL as a BIO tagging problem and use deep bidirectional LSTMs. 

#### Model

> scoring function with penalization terms:
>
> ![](https://raw.githubusercontent.com/xmzzyo/img/master/img/20190115201522.png)
>
> ![1547554556885](C:\Users\xmz\AppData\Roaming\Typora\typora-user-images\1547554556885.png)
>
> Highway LSTM with four layers. The curved connections represent highway connections, and the plus symbols represent transform gates that control inter-layer information ﬂow.
>
> ![](https://raw.githubusercontent.com/xmzzyo/img/master/img/20190115203401.png)
>
> To **alleviate the vanishing gradient problem** when training deep BiLSTMs, we use gated highway connections
>
> Constrained $A^*​$ Decoding：
>
> SRL Constraints Punyakanok et al. (2008)described a list of **SRL speciﬁc global constraints**:
>
> 1. Unique core roles (U): Each core role (ARG0-ARG5, ARGA) should appear at most once for each predicate.
> 2. Continuation roles (C): A continuation role C-X can exist only when its base role X is realized before it.
> 3. Reference roles (R): A reference role R-X can exist only when its base role X is realized (not necessarily before R-X).
>
> $A^*$ search in this setting ﬁnds the optimal sequence for all sentences and is therefore **equivalent to Viterbi decoding.**

#### Analysis

> performance tends to degrade, for all models, for arguments further from the predicate.
>
> the neural model performance deteriorates less severely on long-range dependencies than traditional syntax-based models
>
> high-quality syntax can still make a large impact on SRL.
>
> off-
> the-shelf neural methods have a remarkable ability to learn long-range dependencies, syntactic constituency structure, and global constraints without coding task-speciﬁc mechanisms for doing so



