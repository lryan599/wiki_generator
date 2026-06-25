---
version: "v1"
generated_at: "2026-06-18T11:27:47+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 17
  source_quality_score: 0.85
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

Softmax函数，中文亦称为**归一化指数函数**，是逻辑函数（Sigmoid）在多维空间上的推广 [[S1,S2]]。它能够将任意K维实数向量映射为一个同维度的概率分布向量，其中每一元素的取值范围在开区间(0,1)内，且所有元素之和严格等于1 [[S1,S2]]。这一性质使得Softmax天然适配多分类任务，成为神经网络输出层为各类别分配概率估计值的标准激活函数 [[S1,S7]]。

## 定义与数学表达

对于一个K维实数输入向量$\mathbf{z} = [z_1, z_2, \dots, z_K]$，Softmax函数对第$j$个分量的输出定义为：

$$g(h_j) = \frac{\mathrm{e}^{h_j}}{\sum_{i=1}^{N}\mathrm{e}^{h_i}} \quad (j = 1, 2, \dots, N)$$

其中$h_j$为输入向量的第$j$个元素，$N$为输入向量的总维度 [[S18,S12]]。该函数为维度同态映射，输入与输出的向量维度严格相等，每个输入分量与一个输出概率一一对应 [[S1]]。

在深度学习中，Softmax的输出$\mathbf{h}_i$可直接作为条件概率$P(Y = i \mid \mathbf{x})$的无偏估计值，构成合法的类别概率分布 [[S12]]。

## 核心属性

1. **输出归一性**：输出向量的每个元素严格落在(0,1)区间内，所有元素之和为1，天然满足概率公理 [[S1,S2]]。
2. **可微性**：Softmax函数在整个实数定义域内处处可微，满足反向传播算法对激活函数的连续可微要求 [[S9]]。这一性质源于其指数运算构成的连续函数形式。
3. **单调性**：Softmax的单分量响应曲线随输入值增大而单调快速上升，直观展示了其非线性映射趋势 [[S14]]。
4. **与argmax的关系**：Softmax是argmax的“软化”版本——argmax产生硬性的最大值选择（输出为独热向量），而Softmax给出每个类别的概率估计，保留更多不确定性信息 [[S1,S2]]。

## 梯度特性与数值稳定性

### 偏导数的雅可比矩阵

作为向量值函数，Softmax函数的完整梯度由其**雅可比矩阵**描述：对于N维输出对N维输入的映射，雅可比矩阵为$N \times N$矩阵，矩阵中每一元素为对应输出分量对输入分量的偏导数 [[S13,S10]]。该雅可比矩阵完整刻画了函数的局部梯度变换关系。

### 多输出梯度推导

单输出Sigmoid函数的导数可通过输出值直接计算，形式为$\sigma'(v) = a \cdot y(1-y)$ [[S17]]；类比这一规律，Softmax的多输出梯度也可由输出分量直接推导，这降低了多输出函数在反向传播中的梯度计算复杂度 [[S17,S11]]。

### 数值稳定性与log-softmax

在工程实践中，直接计算Softmax中的指数项可能因输入值过大而导致数值上溢。工业级实现通常采用**平移不变性技巧**：从每个输入分量中减去输入向量的最大值后再进行指数运算，即：

$$g(h_j) = \frac{\mathrm{e}^{(h_j - h_{\max})}}{\sum_{i=1}^{N}\mathrm{e}^{(h_i - h_{\max})}}$$

此外，主流深度学习框架（如TensorFlow）提供的`tf.nn.softmax_cross_entropy_with_logits`组合API可直接基于模型原始输出logits计算交叉熵损失，避免手动先通过Softmax再计算交叉熵可能引发的数值精度溢出问题 [[S8,S15]]。

## 在分类网络中的角色

### 多分类输出层激活函数

在多分类场景下，Softmax作为神经网络输出层的标准激活函数，为每一个输出分类结果分配独立的概率值，输出结果天然构成合法的类别概率分布 [[S1,S7,S6]]。相比Sigmoid等二分类激活函数，Softmax无需额外后处理即可直接用于多类判别，是工业界处理多分类任务的标准选择 [[S1]]。

### 与交叉熵损失的协同

Softmax与多分类交叉熵（Cross-Entropy）损失函数的组合消除了Sigmoid搭配均方误差损失时存在的梯度消失问题（Sigmoid导数峰值仅为0.25）[[S5,S9]]。在该组合下，反向传播阶段的梯度可直接化简为模型输出概率与真实独热标签值的差值，梯度推导形式简洁、计算效率高，可有效提升神经网络训练的收敛速度 [[S5,S9]]。

### Softmax函数与Softmax回归的关系

**Softmax函数**本身是单一的激活函数运算算子，仅完成实数向量到概率分布的映射操作；而**Softmax回归**（Softmax Regression）是完整的多分类机器学习模型，包含完整的前向映射、损失定义和反向梯度更新流程 [[S1,S2]]。从二分类推广的视角看，Softmax回归是逻辑回归（Logistic Regression）在多分类场景的直接拓展，逻辑回归本质上对应类别数为2时的特殊Softmax回归情形，二者共享基于最大似然估计的参数优化逻辑 [[S1,S5,S3]]。

## 别名与相关术语

| 中文名称 | 英文名称 | 说明 |
|---------|---------|------|
| 归一化指数函数 | Normalized Exponential Function | 数学本质描述 [[S1,S2]] |
| Softmax激活函数 | Softmax Activation | 神经网络语境下的常用称呼 [[S1,S2]] |
| Softmax函数 | Softmax Function | 最通用的名称 [[S1,S2]] |

需注意区分：**Softmax**一词有时也泛指Softmax回归模型（完整分类模型），与本词条所述的单体激活函数存在明确的概念边界 [[S1,S2]]。

## 与铸造领域的关系

在**砂型铸造缺陷预测**等场景中，已有文献明确使用Softmax函数作为神经网络输出层激活函数，用于多分类缺陷预测任务。例如，在基于SMOTE数据预处理的砂型铸造复杂铸件缺陷预测研究中，模型采用ReLU作为隐含层激活函数，采用**Softmax作为输出层激活函数**，结合交叉熵损失和准确率作为性能衡量指标，实现无缺陷、冷隔、气孔、砂眼、缩孔等多类缺陷的概率输出 [[S6,S7]]。

在**压铸件缺陷检测与分割**方面，铝合金压铸件X射线图像内部缺陷智能检测研究中，所提出的多任务分割模型CXMTDS-Net在特征图可视化阶段使用Grad-CAM方法，该方法计算类别预测值对卷积层激活特征图的梯度时，依赖模型末端Softmax层输出的预测值进行反向梯度传播 [[S4]]。这表明Softmax层是压铸缺陷智能检测算法链路的有机组成部分。

**需要指出的是**，目前公开可查的压铸行业技术资料中，未发现关于Softmax函数面向压铸工艺的专属应用说明或独立的理论研究文献；Softmax在压铸场景中主要作为通用机器学习基础组件被相关AI模型调用 [[S7,S4]]。

## 图示

Softmax激活函数的单分量响应曲线直观展示了函数随输入值变化的非线性映射特征：横轴为单个输入神经元的活动值，纵轴为对应的Softmax输出分量，曲线呈现随输入增大而单调快速上升的核心性质 [[S14]]。

![Softmax激活函数单分量响应曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9db94ca5-6ae5-4037-920c-1e46c7963d7c/resource)

## Sources
- S1: [22660782_归一化指数函数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09d674d0-6721-4238-9373-2c284b06243a/resource) (`09d674d0-6721-4238-9373-2c284b06243a`)
- S2: [归一化指数函数（Softmax）基本信息表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16542ce9-b470-4974-a72d-b184ec25aa16/resource) (`16542ce9-b470-4974-a72d-b184ec25aa16`)
- S7: [SMOTE数据预处理算法在砂型铸造复杂铸件缺陷预测中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a9ebf5e-3e36-44df-94a0-708261cae79b/resource) (`3a9ebf5e-3e36-44df-94a0-708261cae79b`)
- S18: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d50d5a07-290c-41be-bb7c-f69853a4efca/resource) (`d50d5a07-290c-41be-bb7c-f69853a4efca`)
- S12: [人工智能中的深度结构学习](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94dd9215-592b-4aae-9f39-a21acf070103/resource) (`94dd9215-592b-4aae-9f39-a21acf070103`)
- S9: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c67fd86-f66a-435f-a847-c6100ee42a9d/resource) (`5c67fd86-f66a-435f-a847-c6100ee42a9d`)
- S14: [Softmax激活函数图像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9db94ca5-6ae5-4037-920c-1e46c7963d7c/resource) (`9db94ca5-6ae5-4037-920c-1e46c7963d7c`)
- S13: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a33a79c-6e2b-4698-8cf4-aeb477f3b982/resource) (`9a33a79c-6e2b-4698-8cf4-aeb477f3b982`)
- S10: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ad64069-36db-4266-a5c8-4c3086894e44/resource) (`6ad64069-36db-4266-a5c8-4c3086894e44`)
- S17: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbf30078-8b34-4a85-a963-291b5f233865/resource) (`cbf30078-8b34-4a85-a963-291b5f233865`)
- S11: [人工智能计算agent基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71e11855-276d-460a-a536-a0db3febbe29/resource) (`71e11855-276d-460a-a536-a0db3febbe29`)
- S8: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fb58fa8-a10d-4c16-b65f-db25df391777/resource) (`3fb58fa8-a10d-4c16-b65f-db25df391777`)
- S15: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba9b24fe-0809-4b10-9140-c5e31157504e/resource) (`ba9b24fe-0809-4b10-9140-c5e31157504e`)
- S6: [SMOTE数据预处理算法在砂型铸造复杂铸件缺陷预测中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/302eea81-7621-4f14-b503-8f100e866db5/resource) (`302eea81-7621-4f14-b503-8f100e866db5`)
- S5: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23accd7e-6eb7-4795-872f-2fcf26605eaa/resource) (`23accd7e-6eb7-4795-872f-2fcf26605eaa`)
- S3: [机器学习中的加速一阶优化算法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a9045df-73c0-4b36-9b46-8ceeb6f03b28/resource) (`1a9045df-73c0-4b36-9b46-8ceeb6f03b28`)
- S4: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2179922c-a9ec-4047-a03d-ad0f8d8eddf2/resource) (`2179922c-a9ec-4047-a03d-ad0f8d8eddf2`)