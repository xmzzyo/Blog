---
title: Note Deep Reinforce Learning
tags: [强化学习]
thumbnail: ''
mathjax: true
toc: true
date: 2020-04-19 19:34:53
categories:
- RL
description:
---

# Deep Reinforcement Learning

> Note from:
> 
> - https://github.com/nndl/nndl.github.io
> - http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html

## 概念

<img src="../asset/Review-Deep-Learning/88055126.jpg" style="zoom:50%;" />

### 定义

> 强化学习（Reinforcement Learning，RL），是指一类从**（与环境）交互中不断学习**的问题以及解决这类问题的方法. 强化学习问题可以描述为一个智能体从与环境的交互中不断学习以完成特定目标（比如取得最大奖励值）. 和深度学习类似，强化学习中的关键问题也是贡献度分配问题，每一个动作并不能直接得到监督信息，需要通过整个模型的最终监督信息（奖励）得到，并且有一定的**延时**性.

**例子：**

- 多臂老虎机（Multi-Armed Bandit Problem）
- 悬崖行走

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420110155864.png" alt="image-20200420110155864" style="zoom:50%;" />

**两个对象：**
1. 智能体（Agent）可以感知外界**环境的状态**（State）和**反馈的奖励**（Reward），并进行**学习和决策**.
2. 环境（Environment）是智能体外部的所有事物，并受智能体**动作**的影响而**改变其状态**，并**反馈**给智能体相应的**奖励**.

**五个基本元素：**
1. 状态s 是对环境的表示，可以是离散的或连续的，其状态空间为$\mathcal{S}$.
2. 动作a 是对智能体的行为，可以是离散的或连续的，其动作空间为$\mathcal{A}$.
3. 策略\pi(a|s) 是**智能体**根据环境状态s 来决定下一步动作a 的函数.
   - 确定性策略：$\pi: \mathcal{S} \to \mathcal{A}$
   - 随机性策略：选择动作的概率分布$\pi(a|s)\triangleq p(a|s)$
   - 一般使用随机性策略. 随机性策略可以更好地探索环境，并具有多样性
4. 状态转移概率$p(s^{'}|s,a)$ 是在**智能体**根据当前状态s做出一个动作s之后，环境在下一个时刻转变为状态$s^{'}$的概率.
5. 即时奖励$r(s,a,s^{'})$是一个标量函数，即智能体根据当前状态s做出动作a之后，环境会反馈给智能体一个奖励，**这个奖励也经常和下一个时刻的状态$s^{'}$有关**.

### 马尔科夫决策过程
**交互序列：**

$$s_0, a_0, s_1, r_1, a_1, ⋯ , s_{t−1}, r_{t−1}, a_{t−1}, s_t, r_t, ⋯ $$

其中$r_t = r(s_{t−1}, a_{t−1}, s_t) $是第t 时刻的即时奖励

**马尔可夫决策过程**（Markov Decision Process，**MDP**）在**马尔可夫**过程中加入一个额外的变量：动作a，即下一个时刻的**状态$s_{t+1}$ 和当前时刻的状态$s_t$ 以及动作$a_t$ 相关(一阶马尔可夫)**，

$p(s_{t+1}|s_t, a_t, ⋯ , s_0, a_0) = p(s_{t+1}|s_t, a_t)$

其中$p(s_{t+1}|s_t, a_t) $为状态转移概率.

给定策略$\pi (a|s)$，马尔可夫决策过程的一个**轨迹（Trajectory）**：

$\tau = s_0, a_0, s_1, \gamma_1, a_1, ⋯ , s_{T−1}, a_{T−1}, s_T , \gamma_T$

其概率为：

$p(\tau) = p(s_0)\prod_{t=0}^{T-1}\pi (a_t|s_t)p(s_{t+1}|s_t, a_t).$

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684724410.png" alt="img" style="zoom: 50%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420112406554.png" alt="image-20200420112406554" style="zoom:50%;" />

### 目标函数

轨迹\tau 一个回合（Episode）或试验（Trial）所收到的累积奖励：

$G(\tau) =\sum_{t=0}^{T-1}\gamma(s_t, a_t, s_{t+1})$

引入一个**折扣率**来**降低远期回报的权重**. 折扣回报（Discounted Return）:

$G(\tau) =\sum_{t=0}^{T-1}\gamma^t\gamma_{t+1}$

**$\gamma \in [0, 1]$ 是折扣率**. 当$\gamma$ 接近于0 时，智能体**更在意短期回报**；而当$\gamma$ 接近于1 时，**长期回报变得更重要**.

**最大化期望回报**（Expected Return）:

$J(\theta) = \mathbb{E}\tau∼p_\theta(\tau)[G(\tau)] = \mathbb{E}\tau∼p_\theta(\tau)[\sum_{t=0}^{T-1}\gamma^t\gamma_{t+1}]$

### 值函数（状态值函数和状态-动作值函数）

#### 状态值函数（V函数）

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420115023853.png" alt="image-20200420115023853" style="zoom:67%;" />

$V^\pi(s)$ 称为状态值函数（State Value Function），表示**从状态s 开始（到结束）**，执行策略\pi 得到的期望总回报

$V^\pi(s) = \mathbb{E}\tau∼p(\tau)[\sum_{t=0}^{T-1}\gamma^t\gamma_{t+1}|\tau_{s_0} = s]$

**贝尔曼方程（Bellman Equation）**（动态规划），表示当前状态的值函数可以通过下个状态的值函数来计算.

**递推公式：**

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420115742034.png" alt="image-20200420115742034" style="zoom:67%;" />

如果给定策略$\pi(a|s)$，状态转移概率$p(s'|s, a)$ 和奖励$\gamma(s, a, s')$，我们就可以通过迭代的方式来计算$V^\pi(s)$. 由于存在折扣率，迭代一定步数后，每个状态的值函数就会固定不变.

#### 状态-动作值函数（Q 函数）

$Q^\pi(s, a) = \mathbb{E}s′∼p(s′|s,a) [\gamma(s, a, s′) + \gamma V^\pi(s′)]$

状态值函数$V^\pi(s)$ 是Q 函数$Q^\pi(s, a)$ **关于动作a 的期望**， 

$V^\pi(s) = \mathbb{E}a∼\pi(a|s)[Q^\pi(s, a)]$

Q函数的贝尔曼方程：

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420120648270.png" alt="image-20200420120648270" style="zoom:67%;" />

值函数的作用→优化：

> 假设在状态s，有一个动作$a^∗ $使得$Q^\pi(s, a^∗) > V^\pi(s)$，说明执行动作$a^∗ $的回报比当前的策略\pi(a|s) 要高，我们就可以调整参数使得策略中执行动作$a^∗ $的概率$p(a^∗|s)$ 增加.

### 深度强化学习

神经网络建模策略$\pi(a|s)$ 和值函数$V^\pi(s), Q^\pi(s, a)$

## 值函数方法（Value/Critic）

> 先随机**初始化一个策略**，计算该策略的值函数，并根据值函数来设置新的策略，然后一直反复迭代直到收敛.
> 
> 基于值函数的策略学习方法中最关键的是如何计算策略\pi 的值函数，有动态规划或蒙特卡罗两种计算方式.

### 动态规划

通过贝尔曼方程来迭代计算其值函数. 这种**模型已知**的强化学习算法也称为**基于模型的强化学习（Model-Based Reinforcement Learning）**算法，这里的**模型**就是指**马尔可夫决策过程**.

**限制：**

1. **要求模型已知**，即要给出马尔可夫决策过程的状态转移概率$p(s'|s, a)$ 和奖励函数$\gamma(s, a, s′)$，这个要求很难满足. 
2. 效率问题，即当状态数量较多时，算法效率比较低.

### 蒙特卡罗方法(MC)

> 基于采样的学习算法也称为模型无关的强化学习（Model-Free Reinforcement Learning）算法.

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684887546.png" alt="img" style="zoom: 33%;" />

#### 方法

Q 函数$Q^\pi(s, a)$ 为初始状态为s，并执行动作a 后所能得到的期望总回报，可以写为:

$Q^\pi(s, a) = \mathbb{E}\tau∼p(\tau)[G(\tau_{s_0}=s,a_0=a)]$

其中$\tau_{s_0}=s,a_0=a$ 表示轨迹$\tau$ 的**起始状态和动作为s, a.**

如果模型未知，Q 函数可以通过采样来进行计算，这就是蒙特卡罗方法.

假设我们进行N 次试验，得到N 个轨迹$\tau(1), \tau(2), ⋯ , \tau(N)$，其总回报分别为$G(\tau^{(1)}), G(^{\tau(2)}), ⋯ , G(\tau^{(N)})$. Q 函数可以近似为

$Q^\pi(s, a) ≈ \hat{Q}^\pi(s, a) = \frac{1}{N}\sum_{n=1}^NG(\tau^{(n)}_{s_0=s,a_0=a})$

在近似估计出Q 函数之后，就可以进行策略改进. 然后在新的策略下重新通过采样来估计Q 函数，并不断重复，直至收敛.

#### Exploitation and Exploration

1. **$\epsilon$-贪心法（$\epsilon$-greedy Method）：**

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420152525225.png" alt="image-20200420152525225" style="zoom:50%;" />

每次选择动作$\pi(s)$ 的概率为$1 − \epsilon + \frac{\epsilon}{|\mathcal{A}|}$，其他动作的概率为 $\frac{\epsilon}{|\mathcal{A}|}$.

2. **Boltzmann 探索：**

   <img src="../asset/Note-Deep-Reinforce-Learning/image-20200420201058499.png" alt="image-20200420201058499" style="zoom:50%;" />

#### 同策略（on-policy）和异策略（off-policy）

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684834162.png" alt="img" style="zoom:50%;" />

**同策略：**

 在蒙特卡罗方法中，如果**采样策略**是$\pi^\epsilon(s)$，即$\epsilon-Greedy$，不断**改进策略也是**$\pi^\epsilon(s)$ **而不是目标策略**$\pi(s)$. 这种**采样与改进策略相同**（即都是$\pi^\epsilon(s)$）的强化学习方法叫做同策略（On-Policy）方法.

**异策略:**

 如果**采样策略**是$\pi^\epsilon(s)$，而**优化目标**是策略$\pi$，可以**通过重要性采样**，**引入重要性权重**来实现对目标策略$\pi$ 的优化这种**采样与改进分别使用不同策略**的强化学习方法叫做异策略（Off-Policy）方法.

### 时序差分学习方法(TD)

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684896040.png" alt="img" style="zoom: 33%;" />

蒙特卡罗方法一般**需要拿到完整的轨迹**，才能对策略进行评估并更新模型，因此效率也比较低.

时序差分学习（Temporal-Difference Learning）方法是蒙特卡罗方法的一种改进，通过**引入动态规划算法**来提高学习效率. 时序差分学习方法是模拟一段轨迹，每行动一步(或者几步)，就利用贝尔曼方程来评估行动前状态的价值. 当时序差分学习方法中每次更新的动作数为最大步数时，就**等价于蒙特卡罗方法**.

将蒙特卡罗方法中Q 函数$\hat{Q}^\pi(s,a) $的估计改为增量计算的方式，假设第N 次试验后值函数$\hat{Q}^\pi_N (s, a)$ 的平均为:

$\hat{Q}^\pi_N (s, a) =\frac{1}{N}\sum_{n=1}^NG(\tau^{(n)}_{s_0=s,a_0=a})$

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420162512079.png" alt="image-20200420162512079" style="zoom:67%;" />

.
值函数$\hat{Q}^\pi(s, a)$ 在**第N 试验后的平均**等于**第N − 1 试验后的平均加上一个增量**. 更一般性地，我们将权重系数$\frac{1}{N}$改为一个比较小的正数$\alpha$.

**Q函数更新：**

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420162942259.png" alt="image-20200420162942259" style="zoom:67%;" />

> 时序差分学习是强化学习的主要学习方法，其关键步骤就是在每次迭代中优化Q 函数来减少现实$\gamma + \gamma Q(s', a')$ 和预期Q(s, a) 的差距.
>
> 时序差分学习方法和蒙特卡罗方法的主要不同为：
>
> 1. 蒙特卡罗方法**需要一条完整的路径**才能知道其总回报，也**不依赖马尔可夫性质**，**较大方差**；
> 2. 而时序差分学习方法只需要一步，其总回报**需要通过马尔可夫性质来进行近似估计**，**小方差，不精确**.
>
> <img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684942302.png" alt="img" style="zoom: 33%;" />

#### SARSA (On-Policy)算法（State Action Reward State Action）

由于Bellman方程：

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420164342490.png" alt="image-20200420164342490" style="zoom:50%;" />

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420164535412.png" alt="image-20200420164535412" style="zoom:67%;" />

更新$\hat{Q}^\pi(s, a)$ 只需要知道当前状态s 和动作a、奖励$\gamma(s, a, s')$、下一步的状态s' 和动作a'.

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420173329436.png" alt="image-20200420173329436" style="zoom:60%;" />

其采样和优化的策略都是$\pi^\epsilon$，**即$\epsilon-Greedy$方法**，所以为**On-Policy算法**.

#### Q-Learning

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420172149723.png" alt="image-20200420172149723" style="zoom: 80%;" />

相当于让Q(s, a) 直接去估计最优状态值函数$Q^*(s, a)$.

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684951476.png" alt="img" style="zoom: 50%;" />

> 与SARSA 算法不同，Q 学习算法**不通过$\pi^\epsilon$，即$\epsilon-Greedy$来选下一步的动作**a′，而是**直接贪婪选最优的Q** 函数，因此更新后的Q 函数是关于策略$\pi$ 的，而不是策略$\pi^\epsilon$ 的.

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420173358958.png" alt="image-20200420173358958" style="zoom:60%;" />

### 深度Q网络

为了在连续的状态和动作空间中计算值函数$Q^\pi(s, a)$，我们可以用一个函数$Q_\phi(s, a)$ 来表示近似计算，称为值函数近似（Value Function Approximation）.

函数$Q_\phi(s, a)$通常是一个参数为$\phi$的函数，比如神经网络，输出为一个实数，称为Q 网络（Q-network）.

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420173950783.png" alt="image-20200420173950783" style="zoom: 60%;" />

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684961521.png" alt="img" style="zoom:40%;" />

目标函数：

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420174244197.png" alt="image-20200420174244197" style="zoom:50%;" />

这个目标函数存在**两个问题：**

1. 目标不稳定，参数学习的目标依赖于参数本身；
2. 样本之间有很强的相关性. 

**深度Q 网络采取两个措施：**

1. 目标网络冻结（Freezing Target Networks），即在一个时间段内固定目标中的参数，来稳定学习目标
2. 经验回放（Experience Replay），即构建一个经验池（Replay Buffer）来去除数据相关性. 经验池是由智能体最近的经历组成的数据集.

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420174609380.png" alt="image-20200420174609380" style="zoom:60%;" />

### 深度Q Learning改进

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685001097.png" alt="img" style="zoom: 33%;" />

<img src="../asset/../asset/Note-Deep-Reinforce-Learning/clipboard-1586685013831.png" alt="img" style="zoom: 33%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685061254.png" alt="img" style="zoom: 33%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685084450.png" alt="img" style="zoom: 33%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685095275.png" alt="img" style="zoom: 33%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685109834.png" alt="img" style="zoom: 33%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685122258.png" alt="img" style="zoom: 33%;" />

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685134188.png" alt="img" style="zoom: 33%;" />

------

**Q Learning连续Action Space**

1. <img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685157214.png" alt="img" style="zoom: 33%;" />
2. Actor-Critic

## 基于策略函数的学习方法（Policy/Actor）

强化学习的目标是学习到一个策略$\pi_\theta(a|s)$ 来最大化期望回报. 

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard.png" alt="img" style="zoom:50%;" />

一种直接的方法是在策略空间直接搜索来得到最佳策略，称为**策略搜索（Policy Search）**.

 策略搜索本质是一个优化问题，可以**分为基于梯度的优化和无梯度优化.** 

策略搜索和基于值函数的方法相比，**策略搜索可以不需要值函数，直接优化策略**. **参数化的策略能够处理连续状态和动作**，可以直接学出**随机性策略**.

### 策略梯度（Policy Gradient）

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684791719.png" alt="img" style="zoom:50%;" />

具体推导——梯度上升**最大化目标函数：**

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420194959326.png" alt="image-20200420194959326" style="zoom:60%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420195216442.png" alt="image-20200420195216442" style="zoom:67%;" />

------

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420195330797.png" alt="image-20200420195330797" style="zoom:50%;" />

------

### Reinforce 算法

结合随机梯度上升算法，可以**每次采集一条轨迹，计算每个时刻的梯度并更新参数**，这称为REINFORCE 算法

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420200630472.png" alt="image-20200420200630472" style="zoom:50%;" />

#### 带基准线的 REINFORCE 算法：

REINFORCE 算法的一个主要缺点是**不同路径之间的方差很大，导致训练不稳定**，这是在高维空间中使用蒙特卡罗方法的通病. 

当Reward一直为正数时，可能会因采样出现问题。假设有三个action，a，b，c采取的结果得到的reward都是正的，这个正有大有小，假设a和c的Reward比较大，b的Reward比较小，经过update之后，还是会让b出现的几率变小，a、c出现的几率变大。但是sampling时，有可能只sample b和c，这样b、c几率都会增加，a没有sample到，即使其Reward较大，其采样到的概率就自动减少。

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420202124429.png" alt="image-20200420202124429" style="zoom:33%;" />

**固定的Baseline：**

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684803598.png" alt="img" style="zoom:50%;" />

**可学习的Baseline：**

为了减小策略梯度的方差，我们引入一个和动作$a_t$无关的基准函数$𝑏(s_t)$，

因为$b (s_t)$和$a_t$无关，<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420202500491.png" alt="image-20200420202500491" style="zoom:63%;" />

为了有效减小方差，$b(s_t)$ 和$G(\tau_t∶T )$ 越相关越好，一个很自然的选择是令$b(s_t)$为值函数$V^{\pi_\theta} (s_t)$. 但是由于值函数未知，我们可以用一个可学习的函数$V_\phi(s_t)$ 来近似值函数，目标函数为

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420205726765.png" alt="image-20200420205726765" style="zoom:67%;" />

采用随机梯度下降法，参数$\phi$的梯度为

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420205813886.png" alt="image-20200420205813886" style="zoom:67%;" />

策略函数参数$\theta$的梯度为

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420205840875.png" alt="image-20200420205840875" style="zoom:67%;" />

### Proximal Policy Optimization (PPO)——(On-Policy&Off-Policy)

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684843415.png" alt="img" style="zoom:50%;" />

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586684851838.png" alt="img" style="zoom:50%;" />

## Actor-Critic算法

> 演员-评论员算法（Actor-Critic Algorithm）是一种**结合策略梯度和时序差分**学习的强化学习方法. 
>
> - 其中Actor是指策略函数$\pi_\theta(a|s)$，即学习一个策略来得到尽量高的回报
> - Critic是指值函数$V_\phi(s)$，对当前策略的值函数进行估计. 
> 
> 借助于值函数，Actor-Critic算法**可以单步更新参数**，不需要等到回合结束才进行更新.

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685188338.png" alt="img" style="zoom:40%;" />

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685208061.png" alt="img" style="zoom:40%;" />

在每步更新中，分别进行策略函数$\pi_\theta(a|s)$ 和值函数$V_\phi(s)$的学习. 

一方面，更新参数$\phi$使得值函数$V_\phi(s_t)$ 接近于估计的真实回报$\hat{G}(\tau_t∶T )$，即

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420204935570.png" alt="image-20200420204935570" style="zoom:67%;" />

另一方面，将值函数$V_\phi(s_t)$作为基线函数来更新参数$\theta$，**减少策略梯度的方差**，即

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420205029432.png" alt="image-20200420205029432" style="zoom: 67%;" />

在每步更新中，演员根据当前的环境状态s 和策略$\pi_\theta(a|s)$ 去执行动作a，环境状态变为s'，并得到即时奖励$\gamma$.

- Critic（值函数$V_\phi(s)$）根据环境给出的真实奖励和之前标准下的打分$(r + \gamma V_\phi(s'))$，来调整自己的打分标准，使得自己的评分更接近环境的真实回报. 

- Actor则跟据Critic的打分，调整自己的策略$\pi_\theta$，争取下次做得更好. 

开始训练时，Actor随机表演，Critic随机打分. 通过不断的学习，Critic的评分越来越准，Actor的动作越来越好.

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420210331909.png" alt="image-20200420210331909" style="zoom: 50%;" />

<img src="../asset/Note-Deep-Reinforce-Learning/image-20200420212938961.png" alt="image-20200420212938961" style="zoom: 33%;" />

## 总结

> 一般而言，基于值函数的方法在策略更新时可能会导致值函数的改变比较大，**对收敛性有一定影响**;而基于策略函数的方法在策略更新时更加更平稳些，但因为策略函数的解空间比较大，**难以进行充分的采样**，导致**方差较大**，并**容易收敛到局部最优解**. Actor-Critic算法通过融合两种方法，取长补短，有着更好的收敛性.

### Model-based learning

<img src="../asset/Review-Deep-Learning/16408984.jpg" style="zoom:50%;" />

**Model-Based优缺点：**

<img src="../asset/Review-Deep-Learning/19484532.jpg" style="zoom: 33%;" />

<img src="../asset/Review-Deep-Learning/43402611.jpg" style="zoom: 25%;" />

### 确定性策略

将策略梯度的思想推广到确定性的策略上，提出了确定性策略梯度（Deterministic Policy Gradient，DPG）算法.

- 好处是方差会变得很小，提高收敛性. 
- 缺点是对环境的探索不足，这可以通过异策略的方法解决. 

利用DQN 来估计值函数，提出深度确定性策略梯度（Deep Deterministic Policy Gradient，DDPG）算法. DDPG 算法可以适合连续的状态和动作空间. 

### 分布式Multi-Agent

因为不同环境中的智能体可以使用不同的探索策略，会导致经验样本之间的相关性较小，所以能够提高学习效率.

**A3C算法（Asynchronous Advantage Actor-Critic）**

<img src="../asset/Note-Deep-Reinforce-Learning/clipboard-1586685233138.png" alt="img" style="zoom:40%;" />

### 部分可观测马尔可夫决策过程（Partially Observable Markov Decision Processes，POMDP）

POMDP 依然具有马尔可夫性质，但是假设智能体无法感知环境的状态s，只能知道部分观测值o和环境信息。

### 逆向强化学习（Inverse Reinforcement Learning，IRL）

在某些情况下，智能体无法从环境得到奖励，只有一组轨迹示例（Demonstration）.比如在自动驾驶中，我们可以得到司机的一组轨迹数据，但并不知道司机在每个时刻得到的即时奖励. 虽然我们可以用监督学习来解决，称为行为克隆. 但行为克隆只是学习司机的行为，并没有深究司机行为的动机.

逆向强化学习（Inverse Reinforcement Learning，IRL）就是指一个不**带奖励的马尔可夫决策过程**，通过给定的一组专家（或教师）的**行为轨迹示例来逆向估计出奖励函数**$\gamma(s, a, s')$ 来**解释专家的行为**，然后再进行强化学习.

### 分层强化学习

指将一个复杂的强化学习问题分解成多个小的、简单的子问题，每个子问题都可以单独用马尔可夫决策过程来建模。