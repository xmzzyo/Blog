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

### Simple and Accurate Dependency Parsing Using Bidirectional LSTM Feature Representations

applying it to a greedy transition-based parser as well as to a globally optimized graph-based parser

> Modern approaches to dependency parsing can be broadly categorized into graph-based and transition-based parsers (Kübler et al., 2009).
>
> Graph-based parsers (McDonald, 2006) treat parsing as a search-based structured prediction problem in which the goal is learning a scoring function over dependency trees such that the correct tree is scored above all other trees. Transition-based parsers (Nivre, 2004; Nivre, 2008) treat parsing as a sequence of actions that produce a parse tree, and a classiﬁer is trained to score the possible actions at each stage of the process and guide the parsing process.

## Joint

### Greedy, Joint Syntactic-Semantic Parsing with Stack LSTMs

> **Stack LSTMs** (Dyer et al., 2015) are LSTMs that allow for stack operations: query, push, and pop. A “stack pointer” is maintained which determines which cell in the LSTM provides the memory and hidden units when computing the new memory cell contents. 

![](https://raw.githubusercontent.com/xmzzyo/img/master/20190112230510.png)



![](https://raw.githubusercontent.com/xmzzyo/img/master/20190112230653.png)

