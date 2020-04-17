---
title: Chp1-绪论
tags: []
thumbnail: '1-1.png'
mathjax: true
date: 2018-02-01 12:23:09
categories:
	- NLP
description:
---

### 1.1 问题的提出

### 1.2 基本概念

- 计算语言学(Computational Linguistics) 

> 通过建立形式化的计算模型来分析、理解和生成自然语言的学科，是人工智能和语言学的分支学科。计算语言学是典型的交叉学科，其研究常常涉及计算机科学、语言学、数学等多个学科的知识。与内容接近的学科自然语言处理相比较，计算语言学更加侧重基础理论和方法的研究。 

- 自然语言理解(Natural Language Understanding, NLU) 

> 自然语言理解是探索人类自身语言能力和语言思维活动的本质， 研究模仿人类语言认知过程的自然语言处理方法和实现技术的一门学科。 它是人工智能早期研究的领域之一， 是一门在语言学、 计算机科学、认知科学、 信息论和数学等多学科基础上形成的交叉学科。 

- 自然语言处理(Natural Language Processing, NLP) 

> 自然语言处理是研究如何利用计算机技术对语言文本（句子、篇章或话语等）进行处理和加工的一门学科，研究内容包括对词法、句法、语义和语用等信息的识别、分类、提取、转换和生成等各种处理方法和实现技术。 

- 三个不同的语系

> - 屈折语(fusional language/ inflectional language): 用词的形态变化表示语法关系，如英语、法语等。
> - 黏着语(agglutinative language): 词内有专门表示语法意义的附加成分，词根或词干与附加成分的结合不紧密，如日语、韩语、土耳其语等。
> - 孤立语(analytic language)(分析语, isolatinglanguage): 形态变化少，语法关系靠词序和虚词表示，如汉语。 

- 人类语言技术(Human Language Technology, HLT)
- 自然语言理解 (Natural Language Understanding, NLU) 
- 计算语言学 (Computational Linguistics, CL) 

### 1.3 HLT的产生与发展

### 1.4 研究内容

- 机器翻译 (Machine translation, MT) 
- 信息检索 (Information retrieval) 
- 自动文摘 (Automatic summarization / Automatic abstracting) 
- 问答系统 (Question-answering system)
- 信息过滤 (Information filtering)
- 信息抽取 (Information extraction)
- 文档分类 (Document categorization)

### 1.5 基本问题和主要困难

#### 问题：

1. 形态学 (Morphology) 问题

   > 单词的识别/ 汉语的分词问题。 


2. 语法学 (Syntax) 问题 

   > 研究句子结构成分之间的相互关系和组成句子序列的规则 。
   > 为什么一句话可以这么说也可以那么说？ 

3. 语义学 (Semantics) 问题 

   > 研究如何从一个语句中词的意义，以及这些词在该语句中句法结构中的作用来推导出该语句的意义。 

4. 语用学(Pragmatics) 问题 

   > 研究在不同上下文中语句的应用，以及上下文
   > 对语句理解所产生的影响。 

5. 语音学(Phonetics) 问题 

   > 研究语音特性、语音描述、分类及转写方法等 

#### 困难：

1. 大量歧义(ambiguity)现象 

   - 词法歧义（分词歧义）

   - 词性歧义（不同词性，不同意义）

   - 结构歧义（断句歧义）

     <img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/NLP-Chp1-绪论/20190114112451.png" style="zoom:50%;" />

   - 语义歧义（一词多义）

   - 语音歧义 

   - 多音字及韵律等歧义 

2. 大量未知语言现象 

   - 新词、人名、地名、术语等 
   - 新含义 
   - 新用法和新句型等 

### 1.6 基本研究方法

1. 理性主义 

   > 基于规则的分析方法建立符号处理系统 
   >
   > 知识库 ＋ 推理系统 -> NLP 系统 
   >
   > 理论基础： Chomsky 的文法理论 

   1. 对英语句子进行词法分析、句法结构分析
   2. 利用转换规则将英语句子结构转换成汉语句子结构
   3. 根据转换后的句子结构， 利用词典和生成规则生成翻译的结果句子

2. 经验主义 

   > 基于大规模真实语料(语言数据)建立计算方法 
   >
   > 语料库 ＋ 统计模型 -> NLP 系统 
   >
   > 理论基础：统计学、信息论、机器学习 

   - 贝叶斯公式

### 1.7 研究现状

