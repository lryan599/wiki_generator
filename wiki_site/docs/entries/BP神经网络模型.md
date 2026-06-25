---
version: "v1"
generated_at: "2026-06-18T16:59:14+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 44
  source_quality_score: 0.84
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

BP神经网络（Back Propagation Neural Network，BPNN）在压铸领域是一种基于误差反向传播机制的多层前馈网络，其核心机制为信号沿正向传递到输出层，计算预测值与真实值的误差后，将误差反向逐层传递，沿损失函数梯度反方向迭代更新各层神经元的连接权值与阈值，最小化预测误差从而完成训练[[S39,S19,S2]]。

在压铸工艺中，BP神经网络主要作为预测、优化和控制的建模手段，被应用于多个彼此独立的子场景，如工艺参数预测、铸件缺陷预测、质量分级分类、设备状态监测和能耗预测等。这些场景下的BP网络并非单一固定的模型实例，而是面向不同任务独立构建的预测模型[[S3,S39]]。理论上，一个三层BP网络可在给定任意精度内逼近任意连续映射，因此具备强大的函数逼近与非线性映射能力，能够适配压铸工艺参数到铸件质量之间的复杂非线性关系[[S39,S3]]。

## 基本原理与拓扑结构

BP神经网络由输入层、隐藏层和输出层三部分组成。单个BP神经元由多输入分支、加权求和单元、阈值偏置和激活函数四个基本功能模块组成，是压铸领域各类预测分类模型的基础计算单元[[S7,S45]]。

![压铸BP神经网络基本计算单元结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d8cc810c-a4c6-4dee-b1ab-6921129542d4/resource)

图注：BP神经元基础结构示意图，展示输入支路、加权求和模块、带阈值的激活函数模块及输出端口[[S45,S7]]。

压铸建模场景下，BP神经网络普遍采用输入层-单一隐藏层-输出层的三层拓扑结构。理论证明，该结构可实现任意连续非线性函数的精确映射，完全满足绝大多数压铸质量预测、工艺优化场景的精度需求；仅少数复杂高维度压铸建模场景会采用双隐藏层结构[[S39,S31]]。

![压铸场景BP神经网络训练全流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4208d2b-9d6e-4ac2-8e0a-15b8d6db88c3/resource)

图注：面向压铸场景的BP模型完整训练流程，从参数初始化、导入压铸工艺参数与铸件质量样本到误差判断、迭代更新权值直至输出训练结果[[S48]]。

## 在压铸中的主要应用场景

不同应用场景下的BP神经网络模型在输入变量、输出目标、网络结构上各有不同，无法融合为单一描述。以下五类应用场景在压铸领域已形成典型实践：

### 压铸工艺参数预测与优化

面向高压压铸的工艺参数正向预测，典型实践为将浇注温度、模具预热温度、压射速度作为输入，预测充型时间、充型流态，可替代传统试模流程帮助无经验的压铸工艺人员快速确定合理参数组合，降低试错成本[[S29,S44]]。

代表性的早期研究为Yarlagadda等人在1999年开发的通用压力压铸工艺参数预测模型，采用Levenberg-Marquardt算法为训练算法，输入参数包含铸件重量、熔炼温度、型腔温度、注射压力，输出参数为注射时间。经28类不同工程压铸件工业实测数据验证，整体预测误差低于5%，其中25个隐含神经元配置下最低预测误差仅为1.1765%[[S29,S38,S47]]。邹凤山等国内学者开发的压铸内浇口速度与填充时间多输入多输出BP神经网络模型，通过总结大量压铸行业实践经验训练，可直接根据铸件结构、合金属属属性等输入参数输出内浇口速度与填充时间的最优推荐值[[S44,S37]]。

以下为BP神经网络与数值模拟在压铸工艺参数预测任务上的结果对比实例：

**表：BP神经网络与数值模拟的压铸工艺预测结果对比**[[S30]]

| 序号 | 浇注温度(℃) | 模具温度(℃) | 加压速度(m/s) | 充型时间(s)-数值模拟 | 充型时间(s)-BP预测 | 温度差(℃)-数值模拟 | 温度差(℃)-BP预测 |
|------|-------------|-------------|---------------|--------------------|-----------------|-----------------|--------------|
| 1    | 680         | 200         | 2.0           | 0.082             | 0.080           | 18.5            | 17.3         |
| 2    | 700         | 250         | 2.5           | 0.069             | 0.071           | 14.2            | 15.1         |
| 3    | 720         | 300         | 3.0           | 0.058             | 0.060           | 11.0            | 11.8         |
| 4    | 740         | 350         | 3.5           | 0.050             | 0.048           | 9.3             | 8.7          |
| 5    | 760         | 400         | 4.0           | 0.043             | 0.045           | 7.8             | 8.5          |

该对比表直观验证了BP模型在压铸工艺参数映射任务上的有效性，大部分工况的充型时间、型腔温度差预测误差在工程可接受范围内[[S30]]。

### 压铸典型缺陷预测

面向压铸缺陷的预测已形成较成熟的应用范式，已验证的预测对象包含气孔、缩松缩孔、冷隔三类常见压铸缺陷。对比实验表明，面向压铸场景训练的BP网络对上述缺陷体积的预测精度优于RBF神经网络，平均预测误差低于5%，可实现缺陷的事前预判[[S26,S8,S32]]。

在压力铸造缺陷预测测试集的公开实验中，BP神经网络对充型率、气孔体积、缩孔缩松体积的预测MAE、RMSE指标均优于RBF神经网络，BP预测结果与实测值的吻合度更高[[S46,S49,S33]]。其中，在冷隔缺陷的识别上，BP网络的预测准确率可达100%[[S46]]；常规缩孔率预测偏差可控制在0.36%以内[[S8]]。

### 铸件质量分级分类

典型实践为面向铝合金变速箱壳体压铸的三级质量分类：将铸件标注为"无缺陷质量良好""存在少量缺陷不影响使用质量合格""存在严重缺陷不可用质量不合格"三类，以4项核心压铸工艺参数（浇注温度、快/慢压射速度、模具预热温度）作为输入，BP模型可实现150组实测样本的分类准确率满足工业使用要求[[S16]]。

### 压铸机设备状态监测与故障诊断

基于BP网络建立压铸机液压系统运行参数与故障映射关系，可有效识别压铸机液压泵异常磨损等常见故障，替代传统人工巡检实现设备异常的事前预警，降低非计划停机时长[[S14,S1]]。

### 压铸生产能耗与生产效率预测

面向压铸全流程的能耗建模，将熔炼、保温、压射、冷却各工序的运行参数作为输入，BP模型可精准预测单批次铸件生产能耗与生产节拍，支撑压铸车间能效优化调度[[S42]]。

## 典型模型结构与参数配置

### 常用输入输出变量

压铸建模场景下BP模型涉及的变量集合因应用场景不同而有所差异，以下是基于文献归纳的典型配置：

**表：压铸场景BP网络典型输入输出变量**[[S31,S29,S23,S9,S5,S10]]

| 类别 | 变量 | 说明 |
|------|------|------|
| **输入变量-核心工艺参数** | 压射速度（慢压射/快压射） | 直接影响金属液充型行为 |
| | 模具预热温度 | 影响凝固顺序与铸件表面质量 |
| | 浇注温度（合金温度） | 决定合金流动性与凝固收缩 |
| | 保压压力/保压时间 | 影响铸件致密度与缩孔形成 |
| **输入变量-扩展参数** | 合金牌号/化学成分 | 如ADC12、AlSi9Cu3等 |
| | 模具设计参数 | 内浇口结构参数、溢流槽体积等 |
| | 铸件重量/几何特征 | 影响热容量与凝固时间 |
| **输出变量-缺陷相关** | 气孔/缩孔尺寸及分布 | 缺陷量化指标 |
| | 冷隔/充不足等缺陷类型 | 分类输出或缺陷严重度 |
| | 充型率/缩孔率 | 表征填充质量与内部致密度 |
| **输出变量-质量相关** | 铸件质量分级（良好/合格/不合格） | 分类输出 |
| | 力学性能参数 | 如极限抗拉强度、伸长率等 |

此外，在特定场景中也有研究以铝合金化学元素成分为输入，预测压铸后成品的力学性能，整体预测误差为3.65%，满足压铸工业的工程应用精度[[S13]]。

### 网络结构参数与激活函数

压铸场景下标准BP神经网络采用三层架构即可满足绝大多数非线性映射需求[[S39,S43]]。激活函数的最常用组合为：隐藏层选择Sigmoid类函数（tansig/log-sigmoid），输出层选择纯线性purelin函数，该组合的训练收敛速度与预测精度适配压铸工艺参数到铸件质量的映射特性[[S5,S20,S22]]。

隐藏层神经元数量的确定是模型设计的关键环节。压铸领域通用的经验公式主要有两类：

- **第一类公式**：M = √(n+m) + a，其中M为隐藏层节点数，n为输入层节点数，m为输出层节点数，a为取值1~10之间的整数[[S20,S31]]。
- **第二类公式**（Kolmogorov定理）：n₂ = 2n₁ + 1，其中n₂为隐藏层节点数，n₁为输入层节点数[[S31]]。

工程应用中通常先通过经验公式确定节点数范围，再遍历对比不同节点配置的模型均方误差，选择误差最小的最优节点数[[S20,S31]]。以铝合金变速箱壳体质量预测场景为例，不同隐藏层节点数的10次独立训练实验结果如下：

**表：不同隐含层节点数对应的模型误差**[[S28]]

| 节点数 | 10次独立实验平均误差 |
|--------|----------------------|
| 4      | 0.043               |
| 5      | 0.038               |
| 6      | **0.031** （最优）    |
| 7      | 0.042               |
| 8      | 0.055               |
| 9      | 0.061               |
| 10     | 0.071               |
| 11     | 0.098               |
| 12     | 0.121               |
| 13     | 0.155               |

可见平均误差与隐藏层节点数呈非线性关系，随节点数增加呈先降后升的变化规律[[S31,S22]]。

压铸领域工程实践中的典型BP模型默认参数配置可参考下表：

**表：压铸场景典型BP模型参数配置**[[S35]]

| 参数项 | 典型取值 |
|--------|---------|
| 拓扑结构 | 输入层-单隐藏层-输出层 |
| 激活函数组合 | 隐藏层tansig + 输出层purelin |
| 训练算法 | trainlm (Levenberg-Marquardt) |
| 学习率 | 0.05 |
| 最大迭代次数 | 5000 |
| 目标训练误差 | 1×10⁻⁴ |

### 训练算法

压铸建模领域最常用的BP神经网络训练算法为Levenberg-Marquardt算法（LM，对应Matlab平台的trainlm函数）。该算法相比普通梯度下降类变体拥有更快的收敛速度与更高的预测精度，适配压铸非线性拟合场景[[S29,S20,S22]]。次常用的训练算法为引入动量因子与自适应学习率的traingdx梯度下降变体[[S22]]。

## 数据采集与预处理

### 训练数据来源

压铸场景下BP模型训练数据的三类主流来源[[S16,S32,S29]]：

1. **压铸工艺实验实测数据**：通过压铸机PLC、车间传感器、人工质检记录采集得到；
2. **工厂批量生产历史数据库**：来自压铸车间长期批量生产积累的历史工艺参数与对应质量记录；
3. **铸造CAE仿真模拟输出数据**：通过Moldflow、ProCAST等压铸仿真软件批量生成不同工艺参数下的充型、凝固结果作为补充样本。

### 数据预处理流程

压铸领域BP模型训练数据的通用预处理步骤[[S16,S27,S34,S40]]：

1. **缺失值与异常值处理**：完成缺失值填充/删除，采用3σ准则或箱线图剔除异常无效数据；
2. **数据标准化**：对非正态分布的压铸工艺参数采用Min-Max离差标准化，将所有变量映射到[0,1]区间，消除不同参数间的量纲差异；
3. **特征筛选**：通过相关性分析剔除共线性冗余特征，仅保留对铸件质量影响显著的核心输入参数。在工业实践中，通过相关性分析可将75个工艺参数精简为13个关键变量[[S34]]。

### 训练样本量要求

针对中小型铝合金压铸件的质量预测、缺陷分类任务，实际生产验证的最小有效训练样本量不低于100~150组，即可保证模型泛化能力满足工业精度要求[[S16]]。例如，面向铝合金变速箱壳体的三级质量分类模型采用力劲集团DCC1600吨卧式冷室压铸设备采集的150组实际生产数据进行训练[[S16,S11]]。

## 模型评估与性能对比

### 评估指标

压铸领域BP模型预测性能的主流评估指标包含平均绝对误差(MAE)、均方根误差(RMSE)、相对误差(RE)、均方误差(MSE)、决定系数R²，分别用于量化预测结果与实测值的偏差程度与整体拟合效果[[S46,S49]]。

### 典型准确率范围

压铸领域BP神经网络典型预测准确率范围区间为88%~97%，其中对铸件裂纹类缺陷的整体预测准确率最高可达96.9%，对冷隔类缺陷的识别准确率可达100%，常规缩孔率预测偏差可控制在0.36%以内[[S15,S8,S46]]。

### 与RBF神经网络的对比

在压力铸造缺陷预测任务中，针对充型率预测、缩孔缩松体积预测两类任务，BP神经网络的预测值比RBF神经网络更贴近实测原始值。在大样本量实验组数场景下，RBF神经网络预测偏差显著高于BP神经网络[[S26,S46]]。BP网络模型的平均绝对误差和均方根误差均小于RBF网络模型，表明BP网络对随机数据的预测效果更好，提取的非线性关系更准确，具有更好的泛化性[[S46]]。

## 局限性与改进模型

### 标准BP神经网络的局限性

压铸用标准BP神经网络存在公认固有局限性[[S43,S41,S6]]：

1. **易陷入局部最优解**：由于BP算法采用梯度下降方法，在权重调整过程中可能收敛到局部最优而非全局最优，从而影响预测精度；
2. **泛化能力高度依赖数据**：训练数据规模不足或质量不高时，过拟合风险显著提升；
3. **训练收敛速度慢**：无优化的经典BP在部分压铸样本集训练中耗时可达56秒，甚至出现训练发散、无法达到预设目标误差的问题。

### 过拟合的工程化处理方法

压铸场景下应对过拟合的工程化方法包括[[S43,S31,S17]]：

1. 扩充实际压铸生产与CAE仿真生成的标注样本数据集；
2. 设置合理的训练误差阈值提前终止训练；
3. 在经验公式给出的合理范围内选择最优隐藏层节点数，避免节点冗余；
4. 引入遗传算法、粒子群算法等全局优化算法预训练网络初始权值与阈值，减少过拟合概率。

### 遗传算法优化模型（GA-BP）

GA-BP混合模型在压铸领域已有较广泛的验证应用，可解决原始BP的局部最优缺陷。

面向ADC12铝合金汽车变速箱壳体的GA-BP质量预测模型以浇注温度、快/慢压射速度、模具预热温度为输入，以缩松缩孔缺陷率、质量合格等级为输出，使用力劲集团DCC1600吨卧式冷室压铸设备采集150组实际生产数据训练。经遗传算法优化后，相比标准BP预测精度可提升4.07%，训练总耗时从56秒大幅缩短至2秒，最终预测结果相对误差可控制在±2%以内，可有效降低铸件缺陷返工率[[S14,S41,S12]]。

### 粒子群算法优化模型（PSO-BP）

在压铸/精密铸造场景下，PSO-BP混合模型相比GA-BP收敛速度更快：粒子群算法的适应度在第40代之后趋于稳定，而遗传算法需要到第55代后才趋于稳定；粒子群算法优化的最终适应度显著低于遗传算法，预测误差更小。在复杂薄壁铸件缩孔缩松缺陷与力学性能预测场景中，PSO-BP的表现优于GA-BP[[S17]]。

## 典型应用案例

### 案例一：铝合金变速箱壳体质量预测

面向Al-Si系ADC12铝合金汽车变速箱壳体（典型汽车结构压铸件），基于遗传算法优化的BP神经网络质量预测模型，输入参数包含浇注温度、快/慢压射速度、模具预热温度等核心压铸工艺参数，输出参数为铸件缩松缩孔缺陷率、质量合格等级（三级分类：良好/合格/不合格）。使用力劲集团DCC1600吨卧式冷室压铸设备采集150组实际生产数据训练，模型泛化能力较标准BP神经网络提升，可实现压铸质量的事前预测，降低试模返工率[[S14,S11,S21]]。

### 案例二：压铸工艺参数通用预测系统

Yarlagadda等人1999年开发的面向通用压力压铸工艺的BP神经网络工艺参数预测模型，采用Levenberg-Marquardt算法，输入参数包含铸件重量、熔炼温度、型腔温度、注射压力，输出参数为注射时间。经28类不同工程压铸件工业实测数据验证，整体预测误差低于5%，其中25个隐含神经元配置下最低预测误差仅为1.1765%。该系统的意义在于：新手无需压铸领域专业经验即可使用该系统快速完成压铸工艺参数初选[[S29,S38,S47]]。

### 案例三：压铸铝合金力学性能预测

C. Munoz-Ibanez等人开发的压铸铝合金性能预测BP神经网络模型，以铝合金化学元素成分为输入参数，输出压铸后成品的力学性能，整体预测误差为3.65%，满足压铸工业的工程应用精度要求[[S13]]。

## Sources
- S39: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4e91d3a-69f4-48bb-9e12-3e72f8397365/resource) (`b4e91d3a-69f4-48bb-9e12-3e72f8397365`)
- S19: [基于深度学习的42CrMo八角锭铸造参数预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bb0fca8-54f6-42b9-972e-0520d43bea0c/resource) (`4bb0fca8-54f6-42b9-972e-0520d43bea0c`)
- S2: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04b8a138-5d37-4d38-ad63-05beffddd490/resource) (`04b8a138-5d37-4d38-ad63-05beffddd490`)
- S3: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/05208a83-a0d1-41a0-87db-9fdf1535227e/resource) (`05208a83-a0d1-41a0-87db-9fdf1535227e`)
- S7: [图2.3 BP神经元](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19b12193-4980-482f-9f2d-740ac962c7f2/resource) (`19b12193-4980-482f-9f2d-740ac962c7f2`)
- S45: [BP神经元模型结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d8cc810c-a4c6-4dee-b1ab-6921129542d4/resource) (`d8cc810c-a4c6-4dee-b1ab-6921129542d4`)
- S31: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/896531f0-2010-4dec-be1c-1ad94a26cdcf/resource) (`896531f0-2010-4dec-be1c-1ad94a26cdcf`)
- S48: [图4.2 BP神经网络训练流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4208d2b-9d6e-4ac2-8e0a-15b8d6db88c3/resource) (`f4208d2b-9d6e-4ac2-8e0a-15b8d6db88c3`)
- S29: [a neural network system for the prediction of process parameters in pres__ec0b04f9b1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c35e8bd-c47c-4067-8308-e6b005327b02/resource) (`7c35e8bd-c47c-4067-8308-e6b005327b02`)
- S44: [凝固界面换热系数反求及铝合金薄壁件压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d26cce2d-43a8-495f-a265-08d0d31d8ba0/resource) (`d26cce2d-43a8-495f-a265-08d0d31d8ba0`)
- S38: [a neural network system for the prediction of process parameters in pres__ec0b04f9b1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab5a92f9-5f8a-40fe-a1ca-c5612f1e7626/resource) (`ab5a92f9-5f8a-40fe-a1ca-c5612f1e7626`)
- S47: [Table 5: Predicted vs. Actual Injection Times for Various Engineering Components](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e38ec28c-e2a7-4cb4-8b83-8a9735d18bcb/resource) (`e38ec28c-e2a7-4cb4-8b83-8a9735d18bcb`)
- S37: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a97ca1fc-c3a6-4712-bcdb-cafad0d34a9b/resource) (`a97ca1fc-c3a6-4712-bcdb-cafad0d34a9b`)
- S30: [表5.8 BP神经网络预测的结果与数值模拟结果的比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8542af9e-64c1-468d-9a47-b0f9f8f06e6e/resource) (`8542af9e-64c1-468d-9a47-b0f9f8f06e6e`)
- S26: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/741d3c6e-d647-40bb-8ccb-f775d1bc2540/resource) (`741d3c6e-d647-40bb-8ccb-f775d1bc2540`)
- S8: [基于消失模铸造的面齿轮成型方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d3d65ce-813f-474f-ad0b-b8de8eabb86f/resource) (`1d3d65ce-813f-474f-ad0b-b8de8eabb86f`)
- S32: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9326b199-fb61-4d0b-b97a-af36c68be60b/resource) (`9326b199-fb61-4d0b-b97a-af36c68be60b`)
- S46: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0c69004-dc73-4af2-9887-15599bf01d0d/resource) (`e0c69004-dc73-4af2-9887-15599bf01d0d`)
- S49: [表3-4 压力铸造测试集数据的预测缺陷数值对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd8183aa-4ec2-4d89-bd20-7a8d71b3a8a8/resource) (`fd8183aa-4ec2-4d89-bd20-7a8d71b3a8a8`)
- S33: [充型率原始值与预测值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95b8df22-3445-4cdf-8711-3f02e434139f/resource) (`95b8df22-3445-4cdf-8711-3f02e434139f`)
- S16: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ed94a10-afa5-4c16-b317-e0f210d3b438/resource) (`2ed94a10-afa5-4c16-b317-e0f210d3b438`)
- S14: [TextNode12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/281a7fe1-20e9-4365-90af-a2517e6ed8f1/resource) (`281a7fe1-20e9-4365-90af-a2517e6ed8f1`)
- S1: [a big data analytics platform for smart factories in small and medium si__61e084bf85](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02a27e43-c97a-4c12-9d11-8c5e2b4eee78/resource) (`02a27e43-c97a-4c12-9d11-8c5e2b4eee78`)
- S42: [an iot based framework for energy monitoring and analysis of die casting__e91d993e60](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c96bc80e-c513-4291-9f88-2a86f1abf08c/resource) (`c96bc80e-c513-4291-9f88-2a86f1abf08c`)
- S23: [an adaptive neuro fuzzy inference system anfis model for high pressure d__ae645d3dcf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/627c1199-55b0-4a3c-803c-1ed818a2bd55/resource) (`627c1199-55b0-4a3c-803c-1ed818a2bd55`)
- S9: [die casting process control__e0210f9156](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d4dc79d-42d1-4c8f-a1d6-7b78981a5ba5/resource) (`1d4dc79d-42d1-4c8f-a1d6-7b78981a5ba5`)
- S5: [基于GA-BP神经网络的电机铸铝转子压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10687d7e-af74-4497-8353-e2747d5ed90b/resource) (`10687d7e-af74-4497-8353-e2747d5ed90b`)
- S10: [a big data analytics platform for smart factories in small and medium si__61e084bf85](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fbded09-c09c-44ee-b567-b42e1606c5ee/resource) (`1fbded09-c09c-44ee-b567-b42e1606c5ee`)
- S13: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24fbd963-9bb1-4d35-98bb-56523717d527/resource) (`24fbd963-9bb1-4d35-98bb-56523717d527`)
- S43: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc66ba1f-0609-44d6-a796-97890634a596/resource) (`cc66ba1f-0609-44d6-a796-97890634a596`)
- S20: [城轨车辆铝合金铸造牵引梁材料与成型工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4be3db93-5c08-4198-afd2-bcd5b054e6ac/resource) (`4be3db93-5c08-4198-afd2-bcd5b054e6ac`)
- S22: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6144dd13-1eae-4d2a-8d57-50913083f1ef/resource) (`6144dd13-1eae-4d2a-8d57-50913083f1ef`)
- S28: [表4.2 不同隐含层节点数模型误差](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b556973-d9a5-44bd-accf-00ad0b5b6d8d/resource) (`7b556973-d9a5-44bd-accf-00ad0b5b6d8d`)
- S35: [表5.1 BP神经网络结构参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4db908f-631e-4874-8dca-edc3c5f787da/resource) (`a4db908f-631e-4874-8dca-edc3c5f787da`)
- S27: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75c925e4-0f65-4d38-98ed-68f8b39459db/resource) (`75c925e4-0f65-4d38-98ed-68f8b39459db`)
- S34: [a big data analytics platform for smart factories in small and medium si__61e084bf85](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97f929cf-dc1b-471f-a2cc-df886baa81b5/resource) (`97f929cf-dc1b-471f-a2cc-df886baa81b5`)
- S40: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbe6d03f-9afa-4f15-a64e-6948738c0b94/resource) (`bbe6d03f-9afa-4f15-a64e-6948738c0b94`)
- S11: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fc4906b-77ed-4eb2-b66d-8a0815f91851/resource) (`1fc4906b-77ed-4eb2-b66d-8a0815f91851`)
- S15: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d1b6c54-3cce-4ed6-a1ad-ba83b2b1cf80/resource) (`2d1b6c54-3cce-4ed6-a1ad-ba83b2b1cf80`)
- S41: [基于Moldex3D的高精度空心杯电机电枢注塑封装工艺仿真优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be87252c-5e51-4754-ae63-81f719bbad93/resource) (`be87252c-5e51-4754-ae63-81f719bbad93`)
- S6: [国防科工委十五规划教材材料加工工艺过程的检测与控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18999e21-69b7-41d4-bf31-aa5b567d7e45/resource) (`18999e21-69b7-41d4-bf31-aa5b567d7e45`)
- S17: [复杂薄壁不锈钢轴承座熔模铸造仿真优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3511ec98-d0f5-4136-8a1b-a3adb9bbb27c/resource) (`3511ec98-d0f5-4136-8a1b-a3adb9bbb27c`)
- S12: [基于GA-BP神经网络的电机铸铝转子压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/244f34f2-2caf-4372-9c97-8a6671c2a6e0/resource) (`244f34f2-2caf-4372-9c97-8a6671c2a6e0`)
- S21: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58917021-cb0a-4f9d-831c-755723eab021/resource) (`58917021-cb0a-4f9d-831c-755723eab021`)