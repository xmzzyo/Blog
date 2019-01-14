---
title: Review Deep Learning
tags: []
thumbnail: ''
mathjax: true
date: 2018-06-11 21:20:04
categories:
	- DL
description:
---

## DL Basics

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/58736544.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/40136780.jpg)

### Linear Algebra

#### Scalars

#### Vectors

$\mathbb{R^n}$

#### Matrices

2-D Array

$\mathbb{R^{m\times n}}$

#### Tensors

#### Matrix Transpose

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/18790749.jpg)

$(AB)^T=B^TA^T$

#### Matrix (Dot) Product

#### Identity Matrix

$I_nx=x$

#### Systems of Equations

只有一个解：可逆

#### Matrix Inversion

可逆必要条件：方阵，满秩

#### Norms

$||x||_1=\sum_i|x_i|$

$||x||_ \infty =\max\limits_i|x_i|$

#### Special Matrices and Vectors

正交阵：$A^{-1}=A^T$

#### Eigendecomposition

每一个实对称矩阵都有实，正交特征分解：

$A=Q \land Q^T$

#### SVD

不用是方阵

#### Moore-Penrose Pseudoinverse

？？？

#### Trace

### Probability and Information Theory

#### Computing Marginal Probability with Sum Rule

$P(X=x)=\sum_yP(X=x|Y=y)$

$p(x)=\int p(x,y)dy$

#### Bernoulli Distribution

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/30844542.jpg)

#### Gaussian Distribution

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/15520315.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/60061288.jpg)

## CNN

### 特点

1. Sparse interactions

    不是全链接，稀疏链接

2. Parameter sharing

    整张图片共享一个kernel参数矩阵

3. Equivariant representations

    $f(g(x))=g(f(x))$

    Images: If we move an object in the image, its representation will move the same amount in the output

    Convolution is not equivariant to other operations such as change in scale or rotation

4. Ability to work with inputs of variable size

### Pooling优点

1. Pooling helps the representation become slightly invariant to small translations of the input(we care more about whether a certain feature is present rather than exactly where it is)
2. Since pooling is used for downsampling, it can be used to handle inputs of varying sizes

### Convolution

***输出大小:***

$\frac{N-K}{S}+1$

$N，原图大小(长或者宽)，K，kernel，S，步长$

***Zero Padding***

$\frac{K-1}{2}\ padding可以保留原来的size$

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/48854382.jpg)

## RNN

### LSTM

Challenge of Long-Term Dependencies：梯度消失或爆炸

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-5/19687725.jpg)

LSTM可以解决梯度消失（开忘记门），不能解决梯度爆炸

The influence never disappears unless forget gate is closed

No Gradient vanishing (If forget gate is opened.)

Instead of computing new state as a matrix product with the old state, it rather computes the difference between them.  Expressivity is the same, but gradients are better behaved.

结构：

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-5/27510155.jpg)

### GRU结构

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-5/10544389.jpg)

Exploding is controlled with gradient clipping. Vanishing is controlled with additive interactions (LSTM)

## 正则化和优化

Regularization is any modification made to the learning algorithm with an intention to **lower the generalization error but not the training error**.

### 经典正则化策略

1. Parameter Norm Penalties

> L2 norm penalty can be interpreted as a **MAP Bayesian** 
> **Inference with a Gaussian prior on the weights**.

>L1 norm penalty can be interpreted as a 
>**MAP Bayesian Inference with a Isotropic Laplace Distribution**
>**prior on the weights.**

2. Dataset Augmentation

3. Noise Robustness

> Noise added to weights 
>
> Noise Injection on Outputs. An example is label smoothing.

4. Early Stopping
5. Parameter Sharing
6. Parameter Tying
7. Multitask Learning
8. Bagging
9. Ensemble Models
10. Dropout

> Dropout can intuitively be explained as forcing the model to learn with **missing input and hidden units**.

> Each time we load an example into a minibatch, we randomly sample a different binary mask to apply to all of the input and hidden units in the network.

11. Adversarial Training
> training on adversarially perturbed examples from the training set.

### 优化方法

1. Gradient Descent

   - Batch Gradient Descent

   > Need to compute gradients over the entire training for one update

   - Stochastic Gradient Descent

2. Minibatching

   > Use larger mini-batches

3. Learning Rate Schedule

   > the learning rate is decayed linearly

4. Momentum

   > The Momentum method is a method to accelerate learning using SGD

   梯度：

   ![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/36643891.jpg)

   ![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/25566880.jpg)

5. Nesterov Momentum

   ![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/34867821.jpg)

6. AdaGrad

   ![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/60918544.jpg)

7. RMSProp

   ![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/58611138.jpg)

8. Adam

   ![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/59169403.jpg)

***以上方法比较***

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/44066790.jpg)

9. Batch Normalization

> Let H be a design matrix having activations in any layer for m examples in the mini-batch

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/80725967.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/93754219.jpg)

***优点***
- Improves gradient flow through the network.
- Allows higher learning rates.
- Reduces the strong dependence on initialization.
- Acts as a form of regularization in a funny way, and slightly reduces the need for dropout.

10. Initialization Strategies

> **Initialization should break symmetry (quiz!)**

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-10/57101764.jpg)

## Reinforcement Learning

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/88055126.jpg)

### Model-free learning

1. **Policy-based Approach** Learning an Actor

- Step1: Neural Network as Actor
> Input of neural network: the observation of machine represented as a vector or a matrix

> Output neural network : each action corresponds to a 
> neuron in output layer

- Step 2: goodness of function
> Given an actor $𝜋_𝜃 𝑠$ with network parameter $𝜃$

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/51784666.jpg)


- Step 3: pick the best function
  Policy Gradient

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/892430.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/6836615.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/27246838.jpg)

2. **Value-based Approach** Learning a Critic

> A critic does not determine the action.
>
> Given an actor π, it evaluates the how good the actor is

**Critic**

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/72949772.jpg)

> Monte-Carlo based approach 
>
> The critic watches 𝜋 playing the game

**MC VS. TD**

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/52393914.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/93543592.jpg)

**Q-Learning**

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/9105331.jpg)

3. **Deep Reinforcement Learning** Actor-Critic

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/57243000.jpg)

### Model-based learning

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/16408984.jpg)

**Advantages of Model-Based RL**
![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/19484532.jpg)

![](https://raw.githubusercontent.com/xmzzyo/img/master/backup/18-6-11/43402611.jpg)


