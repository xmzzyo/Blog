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

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/58736544.jpg)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/40136780.jpg)

### Linear Algebra

#### Scalars

#### Vectors

$\mathbb{R^n}$

#### Matrices

2-D Array

$\mathbb{R^{m\times n}}$

#### Tensors

#### Matrix Transpose

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/18790749.jpg" style="zoom:50%;" />

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

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/30844542.jpg" style="zoom:50%;" />

#### Gaussian Distribution

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/15520315.jpg" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/60061288.jpg" style="zoom:50%;" />

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

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/48854382.jpg" style="zoom:50%;" />

## RNN

### LSTM

Challenge of Long-Term Dependencies：梯度消失或爆炸

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/19687725.jpg" style="zoom:50%;" />

LSTM可以解决梯度消失（开忘记门），不能解决梯度爆炸

The influence never disappears unless forget gate is closed

No Gradient vanishing (If forget gate is opened.)

Instead of computing new state as a matrix product with the old state, it rather computes the difference between them.  Expressivity is the same, but gradients are better behaved.

结构：

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/27510155.jpg" style="zoom:50%;" />

### GRU结构

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/10544389.jpg" style="zoom:50%;" />

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

   ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/36643891.jpg)

   ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/25566880.jpg)

5. Nesterov Momentum

   <img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/34867821.jpg" style="zoom:50%;" />

6. AdaGrad

   ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/60918544.jpg)

7. RMSProp

   ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/58611138.jpg)

8. Adam

   ![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/59169403.jpg)

***以上方法比较***

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/44066790.jpg)

9. Batch Normalization

> Let H be a design matrix having activations in any layer for m examples in the mini-batch

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/80725967.jpg" style="zoom:50%;" />

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/93754219.jpg)

***优点***
- Improves gradient flow through the network.
- Allows higher learning rates.
- Reduces the strong dependence on initialization.
- Acts as a form of regularization in a funny way, and slightly reduces the need for dropout.

10. Initialization Strategies

> **Initialization should break symmetry (quiz!)**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/57101764.jpg)

## Reinforcement Learning

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/88055126.jpg" style="zoom:50%;" />

### Model-free learning

1. **Policy-based Approach** Learning an Actor

- Step1: Neural Network as Actor
> Input of neural network: the observation of machine represented as a vector or a matrix

> Output neural network : each action corresponds to a 
> neuron in output layer

- Step 2: goodness of function
> Given an actor $𝜋_𝜃 𝑠$ with network parameter $𝜃$

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/51784666.jpg)


- Step 3: pick the best function
  Policy Gradient

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/892430.jpg)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/6836615.jpg)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/27246838.jpg)

2. **Value-based Approach** Learning a Critic

> A critic does not determine the action.
>
> Given an actor π, it evaluates the how good the actor is

**Critic**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/72949772.jpg)

> Monte-Carlo based approach 
>
> The critic watches 𝜋 playing the game

**MC VS. TD**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/52393914.jpg)

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/93543592.jpg)

**Q-Learning**

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/9105331.jpg)

3. **Deep Reinforcement Learning** Actor-Critic

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/57243000.jpg" style="zoom:50%;" />

### Model-based learning

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/16408984.jpg" style="zoom:50%;" />

**Advantages of Model-Based RL**
<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/19484532.jpg" style="zoom: 33%;" />

<img src="https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Review-Deep-Learning/43402611.jpg" style="zoom: 33%;" />


