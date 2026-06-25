---
version: "v1"
generated_at: "2026-06-18T13:46:54+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 17
  source_quality_score: 0.82
  freshness_score: 0.98
  evidence_coverage_score: 1.0
---

## 概述

CNN‑LSTM 是将卷积神经网络（Convolutional Neural Network，CNN）与长短期记忆网络（Long Short‑Term Memory，LSTM）融合而成的混合深度学习模型，专门面向序列数据的分析与预测[[S4]]。其核心设计思路是：利用 CNN 分支自动提取输入数据的局部空间特征，再通过 LSTM 分支捕获时间维度的长程依赖关系，从而兼具两类网络的优势，有效降低时序建模的计算复杂度、缓解过拟合风险，并适配不同长度的时序输入[[S4]]。

在英文文献中，该模型常被称为 **CNN‑LSTM hybrid network** 或 **Convolutional‑LSTM network**。在压铸领域，CNN‑LSTM 已被应用于工艺参数预测、模具温度场时序预测等工业场景[[S4,S12]]。

---

## 工作原理与架构

### 1D‑CNN 的序列特征提取

CNN‑LSTM 中的 CNN 部分通常采用一维卷积神经网络（1D‑CNN），其输入张量形状为 `[batch_size, sequence_length, num_features]`。卷积核沿序列的时间步方向滑动，通过尺寸为 `[kernel_size, num_features]` 的卷积运算提取时间序列的局部模式（如短时波动、局部趋势），输出特征具备平移不变性，可将原始序列转化为结构化的局部特征序列，供后续模块使用[[S18,S20]]。

![图：CNN基本结构示意图，展示包含输入层、卷积层、池化层、全连接层与输出层的经典架构，常作为CNN-LSTM中空间特征提取模块的基础组成](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d11017e8-68f9-45a5-97e6-c0174431f114/resource)

### LSTM 的时序建模

LSTM 是针对传统 RNN 优化而来的循环网络结构。通过引入记忆单元和遗忘门、输入门、输出门三门控机制，LSTM 可缓解长序列建模中的梯度消失/梯度爆炸问题，能基于当前输入与历史记忆状态动态调整信息的保留与丢弃策略，从而稳定学习时序长程依赖[[S4,S15]]。

### CNN 与 LSTM 的连接方式

CNN 输出与 LSTM 输入之间主要有两种连接方案[[S10]]：

- **方案一：全局池化层连接** — 通过池化层完成特征降维后输入 LSTM，优势是降低后续模块的计算量，但存在部分特征细节损失。
- **方案二：Flatten 层连接** — 将 CNN 输出的高维特征直接展平后输入 LSTM，可完整保留所有提取的特征信息，适用于对特征完整性要求高的场景（如压铸模具温度场的准确预测）。

![图：基于Pooling层连接的CNN-LSTM通用时序预测架构示意图，展示输入层、卷积层、Pooling层、LSTM层、输出层的逐层连接方式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28968bb7-a9d9-4c06-8eb2-b14a3e3f72ba/resource)

---

## 与 ConvLSTM 的区分

1D CNN‑LSTM 与 ConvLSTM 是两类差异化的时序混合模型[[S18]]：

| 对比维度 | 1D CNN‑LSTM | ConvLSTM |
|---------|------------|----------|
| 架构类型 | 串行级联架构 | 卷积极成在 LSTM 单元内部 |
| 特征提取方式 | CNN 独立完成局部特征提取后输出至 LSTM | 卷积嵌入门控计算流程，同步完成空间与时序联合建模 |
| 适用数据场景 | 纯一维时间序列（工业时序监测、过程参数预测） | 同时具备空间维度和时间维度的数据（连续帧图像预测、时空序列） |

---

## 关键超参数

基于压铸工业场景的贝叶斯超参数寻优结果，CNN‑LSTM 的超参数常规取值区间如下[[S17]]：

| 超参数 | 常规取值区间 | 说明 |
|--------|------------|------|
| 卷积核尺寸（kernel_size） | 2～10 | 控制 CNN 提取局部特征的窗口大小 |
| 卷积过滤器数量（filters） | 8～64 | 决定卷积层输出的特征图通道数 |
| LSTM 单元数量（units） | 10～30 | 控制时序建模的记忆容量 |
| 丢弃率（dropout_rate） | 0.01～0.6 | 仿真低噪声场景建议 ≤0.1；实测高噪声场景建议 ≥0.04[[S17]] |

---

## 典型实现环境与数据预处理

CNN‑LSTM 的典型工业实现环境为 **Python 3.9 + TensorFlow 2.0**，可通过 Keras 层接口快速搭建卷积层、池化层、LSTM 层与全连接层的堆叠结构[[S5]]。

面向时序数据的通用预处理流程包括五个核心环节[[S4,S13]]：

1. **数据清洗**：剔除异常值、填充缺失值、去除重复数据。
2. **数据归一化**：通过最小‑最大归一化（Min‑Max Normalization）将所有特征缩放至统一尺度，常用映射区间为 `[0, 1]`[[S4]]。
3. **特征筛选**：采用过滤法、包裹法或嵌入法筛选高相关特征，降低特征冗余。
4. **滑动窗口重构**：将原始时序数据转换为指定窗口长度的输入‑输出训练对，以适配模型输入张量格式。
5. **数据集划分**：采用随机划分或交叉验证，生成训练集、验证集与测试集。

---

## 压铸领域的典型应用

### 铝合金汽车离合器壳体真空压铸工艺参数预测

在该应用中，数据来源于力劲压铸机实际生产的 50 组有效数据。模型以浇注温度、模具初始温度、快压射速度、慢压射速度、真空度 5 个核心特征为输入，以铸件最小残余熔体模数为优化目标[[S14,S19]]。数据集按 50 组训练、6 组验证、4 组测试划分。

训练过程中，前 50 轮损失波动较大，迭代至 60 轮时训练集与验证集损失曲线收敛且趋于一致，达到理想训练状态[[S19]]。最终得到的最优参数组合为：浇注温度 680 ℃、模具初始温度 210 ℃、快压射速度 5.5 m/s、慢压射速度 0.6 m/s、真空度 30 kPa。该参数下铸件经 X 射线探伤、气密性检测与金相分析验证，无气孔、缩孔、裂纹等缺陷[[S19,S23]]。

![图：CNN-LSTM压铸工艺参数预测模型拓扑结构图，输入包括残余熔体模数、浇注温度、模具温度、快压射速度、慢压射速度、真空度等压铸核心参数，经模型处理后输出预测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37a98b3d-973e-43f3-ba27-8b8467914783/resource)

下表为该场景下 CNN‑LSTM 模型的网络参数配置[[S26]]：

| 网络层 | 输入通道数 | 输出通道数 | 核大小 | 步长 |
|--------|----------|----------|--------|-----|
| 第一层卷积 | 1 | 16 | 1 | 1 |
| 第二层卷积 | 16 | 32 | 1 | 1 |
| 池化层 | 32 | 32 | 2 | 2 |
| LSTM 层 | 32 | 50 | — | — |
| 全连接层 | 50 | 1 | — | — |

### 铝合金车轮低压压铸模具温度场时序预测

该应用构建了有限元仿真连续工艺运行温度数据与低压压铸车间实机采集数据组成的双通道数据集，目标是解决压铸过程多变量耦合与温度场时间延迟问题，适配超长序列预测需求[[S12,S24]]。

经贝叶斯优化对 7 类不同时序模型的横向对比，CNN‑LSTM 相比纯时间窗口 LSTM 模型，平均绝对误差（MAE）降低 22%，均方误差（MSE）降低 39%，典型测点预测 R² 可达 0.9784，MSE 低至 0.0013[[S12,S16]]。在仿真场景下，仅消耗约 40% 的训练时间即可达到纯 LSTM 模型 90% 的预测精度[[S12]]。

---

## 性能对比

### 与传统机器学习及纯 LSTM 模型的对比

| 对比对象 | 关键性能差异 | 结论 |
|---------|------------|------|
| 时间窗口 LSTM | 实测模具温度预测中 MAE 下降 22%，MSE 下降 39%[[S3,S12]]；不会出现纯 LSTM 在工业噪声下的“顶峰波动”拐点预测失效问题，鲁棒性显著提升[[S1,S3]] | CNN‑LSTM 在压铸时序预测中的精度与鲁棒性均优于纯 LSTM |
| 改进型滑动窗口 LightGBM（传统机器学习树模型） | 实测压铸模具温度预测中 MAE 从 0.1564 降至 <0.033（降幅 >74%），MSE 从 0.0204 降至 <0.0015（降幅 >92%）[[S3]] | CNN‑LSTM 预测精度显著高于主流传统机器学习模型 |
| 正交试验法（传统工艺选参方法） | CNN‑LSTM 仅需少量训练样本即可构建工艺参数与质量指标的非线性映射关系，选参效率大幅提升，避免人工试错误差与时间浪费[[S19,S23]] | CNN‑LSTM 显著提高工艺参数优化效率 |

---

## 优势与局限

### 核心优势

- **多尺度特征融合**：融合 CNN 局部空间特征提取能力与 LSTM 长时序依赖捕捉能力[[S4]]。
- **抗过拟合**：CNN 的降维作用减少模型参数规模，降低过拟合风险[[S4]]。
- **输入长度灵活**：可适配不同长度的压铸时序输入数据[[S4]]。
- **超长序列预测能力**：在压铸工业传感器超长序列预测场景下表现出高准确性、快速响应与强鲁棒性[[S12]]。

### 适用边界与局限性

- **长时预测的精度衰减**：在压铸场景下，仅对 10 秒以内的迭代预测可保持高精度；预测时长超过 15 秒时，评价指标会快速下降，引入累积误差[[S1]]。
- **注意力机制变体并非通用方案**：额外添加注意力机制的 CNN‑LSTM‑ATTENTION 结构在仿真场景下仅需 40% 的训练时间即可达到标准 CNN‑LSTM 的 90% 精度，但在含工业噪声的实测压铸数据集上预测效果反而下降[[S1,S12]]。
- **调参复杂度较高**：相比传统机器学习模型，CNN‑LSTM 的超参数调优复杂度更高，在小样本压铸数据集上易出现过拟合[[S12]]。

## Sources
- S4: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1da6be75-a76d-47ad-80aa-0a61525d6a3f/resource) (`1da6be75-a76d-47ad-80aa-0a61525d6a3f`)
- S12: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38e163bc-89bc-40e4-acca-ca7209185d18/resource) (`38e163bc-89bc-40e4-acca-ca7209185d18`)
- S18: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/887766a6-e225-497b-a88b-4e0c146bd105/resource) (`887766a6-e225-497b-a88b-4e0c146bd105`)
- S20: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92a93a6a-6497-4010-8fd6-2677baea1eb7/resource) (`92a93a6a-6497-4010-8fd6-2677baea1eb7`)
- S15: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42e11ee8-8c46-41d9-9638-346255be04ff/resource) (`42e11ee8-8c46-41d9-9638-346255be04ff`)
- S10: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35b71734-628d-4a77-8682-055a5e4ecb00/resource) (`35b71734-628d-4a77-8682-055a5e4ecb00`)
- S17: [表5-5 CNN-LSTM模型参数范围与最优参数组合](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86283c10-0f40-4c94-856a-4897eb7d5de8/resource) (`86283c10-0f40-4c94-856a-4897eb7d5de8`)
- S5: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e97bc65-7ee7-4917-b6b6-08d6de4da935/resource) (`1e97bc65-7ee7-4917-b6b6-08d6de4da935`)
- S13: [automation for food engineering food quality quantization and process co__658da4cafc](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a701d05-b4fe-48b3-9cda-2b65113559f6/resource) (`3a701d05-b4fe-48b3-9cda-2b65113559f6`)
- S14: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a9797e1-ccc1-45fc-8e44-9039d3041a3e/resource) (`3a9797e1-ccc1-45fc-8e44-9039d3041a3e`)
- S19: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/889c321f-892b-44f2-a6ff-80972afa4a27/resource) (`889c321f-892b-44f2-a6ff-80972afa4a27`)
- S23: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e50b20b3-6775-498e-9d34-373dae431391/resource) (`e50b20b3-6775-498e-9d34-373dae431391`)
- S26: [表5.1 基于CNN与LSTM压铸参数训练网络参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f17461da-3790-4a8a-a242-6e5eafad689e/resource) (`f17461da-3790-4a8a-a242-6e5eafad689e`)
- S24: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6622e26-2956-456b-90ca-a219ef87be83/resource) (`e6622e26-2956-456b-90ca-a219ef87be83`)
- S16: [图5-17 温度场预测2中TC12预测与实测温度曲线对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82ca5e8e-f67b-4a87-ac10-c1b5c3c45fb8/resource) (`82ca5e8e-f67b-4a87-ac10-c1b5c3c45fb8`)
- S3: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b919417-90ed-48db-89ab-a20dcbfbe23f/resource) (`1b919417-90ed-48db-89ab-a20dcbfbe23f`)
- S1: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07989892-001d-4ef5-bbb2-be926ccd0c70/resource) (`07989892-001d-4ef5-bbb2-be926ccd0c70`)