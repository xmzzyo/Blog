---
title: Function point based software estimation
tags: []
thumbnail: ''
mathjax: true
date: 2018-09-19 09:49:49
categories:
	- SE
description:
---

### Definition

>software metrics are measurable indication of some quantitative aspects of a software system and they are divided into two functional categories: Product and Process Metrics. Process metrics quantify attributes of the development process and of the development environment. Product metrics are measure of the software product. They provide us with a systematic way to assess quantity based on a set of clearly defined rules. In this study we will concentrate on product metrics i.e. function points.  

>Based onthe FPA method, several methods like Feature Points, Full
>Function Points, Function Weight, Function Bang, Mk IIFunction Points Analysis, COSMIC-FFP and NESMA evolved. 
>
>>A. Zˇivkovicˇ, M. Hericko, T. Kralj, Empirical assessment of methods for software size estimation, Informatica (Ljubljana) 4 (2003) 425–432.



### Traditional labor-intensive method

### UML based

Fetcke et al. proposed four groups of rules based on use cases. Use Case Diagram define the system boundary and mapped into transactional functions. Meanwhile, only entity objects counted as data functions. Aggregation and generalization are respectively treated as data elements types, record element types and ﬁle types referenced.

>Mapping the OO-Jacobson approach into function point analysis
>
>Object-oriented Software Engineering: A Use Case Driven Approach

Takuya UEMURA et al. proposed a series FPA(Function Point Analysis) measurement rules based on UML(Unified Modeling Language) for the design specifications, which produced by Rational Rose, a prevalent CASE tool and widely used in software development organizations. Unlike Fetcke ,  this method used the messages in the sequence diagrams as the system boundary.

> Function-point analysis using design speciﬁcations based on the Uniﬁed Modelling Language

Alesˇ Zˇivkovicˇ et al. proved that the accuracy of estimate increase with three
estimation levels which deﬁned that correspond to the different abstraction levels of the software system. Another contribution is proposing a changed FPA complexity tables based less data elements for transactional functions to achieve the same complexity.

>Automated software size estimation based on function points using UML models

Anie Rose Irawati et al. proposed a system whose input is XMI document resulting from software design documentation derived from UML documents. This system automated calculate the FP measure with the information of Use Case Diagram, Use Case and Class Diagram and association between Use Case and Class Diagram in a faster and easier method without losing accuracy.

>Measuring Software Functionality Using Function Point Method Based On Design Documentation 

A. Chamundeswari et al. proposed a new and enhanced rules to address the ambiguous complexity calculation when a class involved in mixed interactions such as aggregation, association and inheritance without sacrificing estimate accuracy.

> Extended Function Point Approach for Size Estimation of Object-Oriented Software 

Noticed the fact that the process of mapping object-oriented requirements specifications to function points can not be done fully automatically, Vahan Harput et al. proposed primarily of heuristic rules that defined a semi-automatic transformation model. 

>Extending Function Point Analysis to Object-Oriented Requirements Speciﬁcations

All the above methods are based UML, which can provide common language for object-oriented model. And these methods depend on the completeness and accuracy of UML diagrams. Our work takes a different direction and focus on the user stories where can extract function points with nature language methods.

### Goal and Scenario based

### NN based

