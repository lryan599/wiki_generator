---
version: "v1"
generated_at: "2026-06-18T12:42:43+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 26
  source_quality_score: 0.83
  freshness_score: 0.98
  evidence_coverage_score: 1.0
---

## 概述

长短期记忆网络（Long Short-Term Memory, LSTM）是Hochreiter和Schmidhuber于1997年提出的一种改进型循环神经网络（RNN），其核心设计是在隐藏层中引入记忆单元与门控机制，有效解决传统RNN在长序列处理时的梯度消失/梯度爆炸问题，实现长期时序依赖的稳定学习[[S28,S10,S34]]。在压铸技术领域，生产过程（如模具温度变化、压射速度曲线、工艺参数时序演变）本质上属于高维、强时滞特性的时间序列建模问题，LSTM凭借其对长时依赖的捕捉能力，正成为压铸过程质量预测、工艺参数优化与过程数字孪生建模的重要智能算法[[S14,S34,S5]]。

## LSTM的定义与基本原理

### 结构组成

LSTM单元由遗忘门、输入门和输出门三个门控组件构成，通过门控逻辑控制信息在单元内的流入、保留与流出[[S1,S16,S25]]。

- **遗忘门**：接收上一时刻隐藏状态 \(h_{t-1}\) 和当前输入 \(x_t\)，经Sigmoid激活输出0~1之间的控制值 \(f_t\)，决定上一时刻细胞状态 \(c_{t-1}\) 中哪些信息应被遗忘。  
- **输入门**：同样由Sigmoid产生控制信号 \(i_t\)，结合tanh生成的候选状态 \(\tilde{c}_t\)，共同决定将多少新信息写入当前细胞状态 \(c_t\)。  
- **输出门**：由Sigmoid生成 \(o_t\)，对经过tanh处理的当前细胞状态进行门控，得到当前隐藏状态 \(h_t\)，作为该时间步的输出。

细胞状态的更新规则为 \(c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t\)（\(\odot\) 为逐元素乘法），该机制使得细胞状态可以在主通道上仅通过少量逐元素乘加运算直接传递，大幅降低长序列反向传播时的梯度指数衰减，实现对长时关联信息的有效记忆[[S16,S1,S25]]。

### 与标准RNN的对比

传统RNN的隐藏层仅通过简单线性变换和激活函数传递序列状态，在铸造过程等需要回溯超长时间窗口的场景下，因链式求导引起梯度消失，导致无法学习远距离依赖[[S14,S18,S16]]。LSTM替代RNN隐藏层后，以门控方式控制信息流动，在压铸模具温度场超长序列预测等任务中表现出显著优势[[S16,S7]]。

![LSTM单元内部结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1b8de28-b323-4a18-a606-7f092065091c/resource)

**图1.** 长短期记忆网络单元标准结构示意图，展示遗忘门、输入门、输出门以及σ、tanh激活函数的关系[[S30]]。

![普通RNN单元与LSTM单元结构对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/130e20b5-7e9d-49e5-a468-b86257593709/resource)

**图2.** 普通RNN单元（a）与LSTM单元（b）结构对比，体现门控机制的引入[[S7]]。

## 在压铸中的典型应用

### 模具温度场时序预测

压铸模具温度具有明显的冷却传热延时特性和工艺-温度的历史映射关系，是典型的长序列预测场景。燕山大学的研究针对铝合金车轮低压铸造，提出了经滑动窗口技术改进的LSTM模型，以及在此基础上集成卷积层（CNN）的CNN-LSTM模型[[S5,S14]]。在仿真数据环境下，单纯滑动窗口LSTM的MAE可达0.0007，表现出极高的拟合精度；但转入现场实测数据后，因噪声扰动，LSTM出现“顶峰波动”现象，无法准确预测温度曲线拐点，MAE升至0.0356，鲁棒性不足[[S3,S22]]。在相同实测数据上，CNN-LSTM模型的MAE小于0.033、MSE小于0.0015，决定系数R²稳定在0.98左右，相比纯滑动窗口LSTM，MAE下降22%、MSE下降39%，并通过将迭代预测时长控制在10秒以内避免了累积误差，实现了模具温度的在线预判[[S3,S9,S15]]。

面向薄壁结构件的压铸模温预测研究进一步在LSTM的基础上引入双向结构和注意力机制，构建了BiLSTM-attention-FWA模型，实验对比表明其预测精度最稳定，误差最小，优于基础LSTM[[S31,S19]]。

### 工艺参数预测与优化

盐城工学院针对铝合金汽车离合器壳体真空压铸场景，构建了CNN-LSTM混合预测模型[[S2,S10]]。研究以实际压铸机记录的50组有效生产数据为样本，通过最小-最大归一化处理后，建立浇注温度、模具温度、快压射速度、慢压射速度、真空度5项关键工艺参数与铸件残余熔体模数之间的非线性映射[[S26,S35]]。模型预测的最优参数组合为浇注温度680℃、模具初始温度210℃、快压射速度5.5m/s、慢压射速度0.6m/s、真空度30KPa，经数值模拟验证，铸件无明显缩孔、卷气等内部缺陷[[S26]]。该案例中使用的CNN-LSTM网络参数配置如表1所示，LSTM层输入通道数为32、输出维度为50[[S33]]。

**表1. CNN-LSTM压铸参数预测模型网络参数配置**

| 网络层 | 输入通道数 | 输出通道数 | 核大小 | 步长 |
|--------|------------|------------|--------|------|
| 卷积层1 | 1 | 32 | 3 | 1 |
| 卷积层2 | 32 | 64 | 3 | 1 |
| 池化层 | 64 | 64 | 2 | 2 |
| LSTM层 | 32 | 50 | - | - |
| 全连接层 | 50 | 1 | - | - |

### 压射系统动态建模与参数映射

针对2800kN锁模力压铸机的压射系统，有研究将LSTM用于学习插装阀阀芯位移与压射速度之间的时序映射关系[[S34]]。利用磁栅式传感器采集的510组压射速度曲线，经sym8小波软阈值去噪预处理后，输入LSTM进行训练，所建模型在测试集上的均方根误差RMSE低至0.336%，相关系数R²=0.998，平均预测误差仅0.11%；而传统理论公式模型的平均误差高达-17.36%，充分体现了LSTM在压铸动态系统时序建模中的高精度优势[[S13,S17]]。

## 模型性能对比

在铝车轮低压铸造模具温度长的预测任务中，研究人员将LSTM、CNN-LSTM、LSTM-ATTENTION、CNN-LSTM-ATTENTION、经滑动窗口改进的LightGBM等多种模型分别在仿真和实测数据集上进行对比[[S22]]。各模型的主要性能表现汇总于表2。

**表2. 铝车轮低压铸造模具温度预测模型性能对比**

| 模型 | 数据集类型 | MAE | MSE | R² | 特点 |
|------|------------|-----|-----|----|------|
| LSTM（滑动窗口） | 仿真 | 0.0007 | - | - | 精度最高，但实测差[[S22]] |
| LSTM（滑动窗口） | 实测 | 0.0356 | - | - | 顶峰波动，鲁棒性差[[S3]] |
| CNN-LSTM | 实测 | <0.033 | <0.0015 | ≈0.98 | 鲁棒性强，性能最优[[S9,S3]] |
| LSTM-ATTENTION | 仿真 | - | - | - | 响应速度快一倍，但精准度低[[S22]] |
| CNN-LSTM-ATTENTION | 仿真 | - | - | - | 训练时间仅为CNN-LSTM的40%，达其90%精度[[S15]] |
| CNN-LSTM-ATTENTION | 实测 | - | - | - | 效果低于普通CNN-LSTM，不适用工业现场[[S15]] |
| LightGBM（滑动窗口） | 实测 | 0.1564 | 0.0204 | 0.89 | 较普通LightGBM MAE下降3%，MSE下降33%，但响应慢[[S3]] |

综合对比表明，在包含实际噪声的压铸实测数据环境下，结合CNN与LSTM的混合模型相较于纯LSTM能够更好地捕捉局部特征，弥补单一模型在拐点预测和噪声鲁棒性上的不足[[S3,S22]]。注意力机制在仿真条件下可提升训练效率，但在高拟合度实测场景中则导致训练难度增大，预测效果反而下降[[S15]]。

## 局限性与实际挑战

尽管LSTM在压铸建模中展现出良好的预测性能，但在实际工业部署中仍面临若干限制：

- **小样本过拟合风险**：压铸现场数据采集成本高、标注困难，多数研究仅能获取几十至几百组有效样本，导致LSTM在有限数据下极易过拟合，削弱泛化能力[[S23]]。  
- **计算开销与实时性**：LSTM网络结构复杂，参数量大，在边缘设备上难以满足压铸现场毫秒级的实时推理需求[[S27,S14]]。  
- **可解释性不足**：LSTM作为黑箱深度序列模型，其门控参数与权重难以与压铸工艺机理（如浇注温度与缺陷形成的物理关系）直接对应，给工艺人员的决策追溯带来困难[[S8]]。

这些挑战推动了在压铸领域中CNN-LSTM、BiLSTM-Attention等改进模型的研究，以期在高精度与工程可行性之间取得平衡。

## Sources
- S28: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a3caf88-9985-46d1-9095-b16bce13e579/resource) (`9a3caf88-9985-46d1-9095-b16bce13e579`)
- S10: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1da6be75-a76d-47ad-80aa-0a61525d6a3f/resource) (`1da6be75-a76d-47ad-80aa-0a61525d6a3f`)
- S34: [基于时间序列数据驱动的压铸机压射系统机理模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9080f10-0ae7-498f-bbf6-2954eae4f048/resource) (`f9080f10-0ae7-498f-bbf6-2954eae4f048`)
- S14: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/33bba657-4755-4bf9-a533-ca9fbf38f287/resource) (`33bba657-4755-4bf9-a533-ca9fbf38f287`)
- S5: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f2f8d33-211e-4bc6-bf7b-fbe19c0997ec/resource) (`0f2f8d33-211e-4bc6-bf7b-fbe19c0997ec`)
- S1: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02a97747-1ac7-4fbc-8b57-1784e100eb3a/resource) (`02a97747-1ac7-4fbc-8b57-1784e100eb3a`)
- S16: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42e11ee8-8c46-41d9-9638-346255be04ff/resource) (`42e11ee8-8c46-41d9-9638-346255be04ff`)
- S25: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/876c3e06-3d81-4352-b0cc-51eedee623e9/resource) (`876c3e06-3d81-4352-b0cc-51eedee623e9`)
- S18: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57601dee-6e97-449e-b9e0-d056fdf3b861/resource) (`57601dee-6e97-449e-b9e0-d056fdf3b861`)
- S7: [图3-4 普通RNN和LSTM的cell对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/130e20b5-7e9d-49e5-a468-b86257593709/resource) (`130e20b5-7e9d-49e5-a468-b86257593709`)
- S30: [图3.1 LSTM网络单元结构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1b8de28-b323-4a18-a606-7f092065091c/resource) (`d1b8de28-b323-4a18-a606-7f092065091c`)
- S3: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07989892-001d-4ef5-bbb2-be926ccd0c70/resource) (`07989892-001d-4ef5-bbb2-be926ccd0c70`)
- S22: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69bb2271-36b4-42bb-b535-4178743b65e1/resource) (`69bb2271-36b4-42bb-b535-4178743b65e1`)
- S9: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b919417-90ed-48db-89ab-a20dcbfbe23f/resource) (`1b919417-90ed-48db-89ab-a20dcbfbe23f`)
- S15: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38e163bc-89bc-40e4-acca-ca7209185d18/resource) (`38e163bc-89bc-40e4-acca-ca7209185d18`)
- S31: [图3.9 3种模型的预测精度对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ee15b54e-6035-4124-b573-d7de070cf7a0/resource) (`ee15b54e-6035-4124-b573-d7de070cf7a0`)
- S19: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/579a830d-3267-4d71-8744-7ccb62753c62/resource) (`579a830d-3267-4d71-8744-7ccb62753c62`)
- S2: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02b55975-6f8d-4217-bf6c-6220a32e5879/resource) (`02b55975-6f8d-4217-bf6c-6220a32e5879`)
- S26: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/889c321f-892b-44f2-a6ff-80972afa4a27/resource) (`889c321f-892b-44f2-a6ff-80972afa4a27`)
- S35: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9bd1032-29cc-4459-8429-223fc50a2bf1/resource) (`f9bd1032-29cc-4459-8429-223fc50a2bf1`)
- S33: [表5.1 基于CNN与LSTM压铸参数训练网络参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f17461da-3790-4a8a-a242-6e5eafad689e/resource) (`f17461da-3790-4a8a-a242-6e5eafad689e`)
- S13: [基于时间序列数据驱动的压铸机压射系统机理模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2dd8ff51-e6e9-49b9-b70d-0b772e41227c/resource) (`2dd8ff51-e6e9-49b9-b70d-0b772e41227c`)
- S17: [基于时间序列数据驱动的压铸机压射系统机理模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/575ffc7d-ed1d-4350-81f3-cc0168bf93e6/resource) (`575ffc7d-ed1d-4350-81f3-cc0168bf93e6`)
- S23: [致密砂岩储层孔隙度预测一般方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78f6fbbf-79d5-4b07-85fd-b0384f7aaf78/resource) (`78f6fbbf-79d5-4b07-85fd-b0384f7aaf78`)
- S27: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96ab7148-5a63-4dd4-8605-1eac8d337b6f/resource) (`96ab7148-5a63-4dd4-8605-1eac8d337b6f`)
- S8: [大话自动化从蒸汽机到人工智能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13ee4d35-73d1-4ade-a84e-ca7ba3d90773/resource) (`13ee4d35-73d1-4ade-a84e-ca7ba3d90773`)