---
version: "v1"
generated_at: "2026-06-18T12:07:03+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 36
  source_quality_score: 0.84
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

## 概述

决定系数（Coefficient of Determination），通常记为 R²，是回归分析中衡量模型拟合优度的核心统计指标，在压铸及相关铸造领域广泛用于工艺参数–质量特性建模、机器学习铸件质量预测模型以及数值仿真模型的性能评价。该指标表示因变量总变差中能够被回归模型（自变量）解释的比例，属于无量纲的相对评价指标 [[S1, S10, S37]]。

标准的 R² 数学定义为：

\[
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = \frac{SS_{\text{reg}}}{SS_{\text{tot}}}
\]

> **别名：** 拟合优度、决定系数 R2、Coefficient of Determination (R²)。

---

## 定义与数学原理

### 三个平方和的关系

在回归分析中，因变量的总波动可以通过三个平方和及其恒等关系来分解 [[S1, S10, S15]]：

- **总平方和** \(SS_{\text{tot}}\)（SST）：所有样本观测值与观测值均值之差的平方和，反映因变量整体的总波动；
- **回归平方和** \(SS_{\text{reg}}\)（SSR）：所有样本模型预测值与观测值均值之差的平方和，反映自变量线性关系对因变量波动的解释部分；
- **残差平方和** \(SS_{\text{res}}\)（SSE）：所有样本观测值与对应模型预测值之差的平方和，反映模型无法解释的剩余波动。

三者之间满足以下恒等关系：

\[
SS_{\text{tot}} = SS_{\text{reg}} + SS_{\text{res}} \qquad \text{【[[S1, S10, S15]]】}
\]

### R² 的计算公式

R² 本质上是回归平方和在总平方和中所占的比例，其两种等价表达形式如下 [[S10, S14, S27]]：

\[
R^{2} = \frac{U}{L_{yy}} = \frac{SS_{\text{reg}}}{SS_{\text{tot}}}
\]

\[
R^{2} = 1 - \frac{\sum (y_i - \hat{y}_i)^{2}}{\sum (y_i - \bar{y})^{2}} = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\]

式中：\(y_i\) 为第 \(i\) 个样本的实测值；\(\hat{y}_i\) 为对应的模型预测值；\(\bar{y}\) 为所有实测值的均值。

---

## 取值范围与解读

### 常规取值范围

R² 在常规场景下的取值范围为 **[0, 1]**：越接近 1，代表回归模型对因变量总变差的解释比例越高，模型拟合效果越好；R² = 1 表示所有样本点完全落在拟合直线上，无任何残差 [[S1, S4, S17]]。

### 出现负值的特殊场景

当残差平方和 \(SS_{\text{res}}\) 大于总平方和 \(SS_{\text{tot}}\) 时，R² 计算结果为负值，代表当前回归模型的预测效果甚至差于直接使用因变量样本均值进行预测。典型引发负值 R² 的场景包括 [[S1]]：

- 无截距项的线性回归；
- 严重欠拟合的模型；
- 利用训练集外的样本外推时模型失效。

### R² = 1 的理想拟合图示

下图展示了所有数据点完全落在最佳拟合直线上、相关系数 R = 1 的理想线性回归效果，直接对应 R² = 1 的拟合情形 [[S34]]。

![线性回归分析图：所有数据点完全落在拟合直线上，相关系数 R=1，对应 R²=1 的理想拟合效果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d863fd86-b01d-4edd-8201-b6bac38762d1/resource)

---

## 相关指标与扩展

### 多重 R² 与调整 R²

**多重 R²（多元确定系数）** 表示多元回归场景下因变量的总变差中能够被全部自变量共同解释的比例。其主要局限性在于，随新增自变量的加入会单调递增并趋向于 1——即使新增自变量与因变量无关，R² 仍会升高，导致对模型实际拟合能力的高估 [[S9]]。

为修正这一偏差，引入 **调整 R²（Adjusted R²）**：在基础 R² 的计算逻辑中引入自变量数量的惩罚项，消除普通 R² 随自变量增加而单调升高的偏差，能够更客观地评估多元回归模型的真实拟合精度。调整 R² 越接近 1，表示模型拟合精度越高 [[S12, S17, S22]]。

### 预测 R²

**预测 R²（Predicted R²）** 是基于测试集或交叉验证数据集计算得到的决定系数，用于评估回归模型的泛化预测能力。当调整 R² 与预测 R² 之间的差值小于 0.2 时，通常表明模型预测值与实测值的吻合程度良好，过拟合风险低 [[S17, S32]]。

### 三类 R² 指标对比

以下数据来自工艺建模中的回归模型汇总表，直观展示了普通 R²（94.50%）、调整 R²（85.34%）、预测 R² 在实际工程报告中的典型数值关系 [[S16]]：

| 指标 | 数值 | 工程含义 |
|------|------|----------|
| 普通 R² | 94.50% | 训练数据上的拟合优度 |
| 调整 R² | 85.34% | 惩罚自变量数量后的拟合精度 |
| 预测 R² | 对应数值 | 模型泛化预测能力评估 |

### R² 与 RMSE、MAE 的差异对比

R² 与均方根误差（RMSE）、平均绝对误差（MAE）是回归模型评价中常见的三类互补指标 [[S1, S33, S36]]：

| 指标 | 类型 | 特点 |
|------|------|------|
| **R²** | 无量纲相对指标 | 反映模型对因变量方差的解释比例，越接近 1 越好 |
| **RMSE** | 与因变量同量纲的绝对指标 | 直接度量预测偏差幅度，对较大偏差的敏感度较高 |
| **MAE** | 与因变量同量纲的绝对指标 | 对异常值的敏感度低于 RMSE |

工程评估中推荐三者同时使用，以从不同维度综合判断模型性能。

---

## 压铸领域的应用场景

### 工艺参数–质量特性回归模型

R² 在高压压铸领域最经典的应用是评估基于响应面法构建的工艺参数–质量特性非线性回归模型的拟合精度。典型的输入变量包括快压射速度、增压压力、持压时间、模具温度、浇注温度等；输出质量特性则覆盖气孔率、表面粗糙度、硬度、缩松率、力学性能等 [[S12, S21, S40]]。

### 机器学习质量预测模型评价

随着智能铸造技术的推广，R² 被广泛用于验证各类机器学习质量预测模型的泛化性能，涉及的算法包括人工神经网络（ANN）、自适应神经模糊推理系统（ANFIS）、支持向量机（SVM）、随机森林（RF）、XGBoost、CNN-LSTM 等。预测目标涵盖铸件气孔缺陷率、抗拉强度、模具温度场、铸造过程参数等 [[S2, S7, S18, S26]]。

### 数值仿真与经验公式的验证

R² 同样应用于评估压铸数值仿真输出与实验实测结果的匹配程度，典型场景包括 [[S11, S37]]：

- 压铸金属–模具界面换热系数（HTC）拟合；
- 经验公式对铸件凝固时间、充型过程参数的预测精度判定。

### 以 R² 为优化目标的模型开发

在工程优化中，R² 可直接作为优化算法的适应度函数。例如，将 R² 作为粒子群算法（PSO）优化 BP 神经网络权值和阈值的适应度函数，在压铸翘曲变形预测场景下，优化后的模型 R² 可从 0.765 提升至 0.951，显著降低预测误差 [[S5]]。

### 压铸领域 R² 可接受阈值参考

不同压铸建模场景下，行业普遍采用的 R² 最低可接受阈值分布如下 [[S2, S17, S20, S21]]：

| 场景类型 | 典型 R² 要求 |
|----------|--------------|
| 高精度二阶响应面工艺质量回归模型 | R² ≥ 0.95 |
| 普通数据驱动压铸质量预测模型（训练集） | R² ≥ 0.73 ~ 0.75 |
| CNN-LSTM 模具温度场深度学习时序预测 | R² ≈ 0.98 |
| 模型独立测试集验证 | 预测 R² ≥ 0.88 以保证工程实用精度 |

压铸领域工程实践中同时建议：当 R² 与调整 R² 差值小于 0.2，且预测 R² ≥ 0.88 时，可判定模型信噪比充足、预测精度符合工程要求 [[S17, S19]]。

### 可视化：实测值–预测值散点图

在压铸论文中，实测值–预测值散点图是展示 R² 物理意义的通用可视化方法：全部样本点越贴近 45° 参考直线，R² 值越高、模型预测性能越优异 [[S35, S39]]。

---

## 局限性与注意事项

### 对异常值高度敏感

R² 的计算基于残差平方和，对数据集内的异常值极为敏感——单个极端离群样本点即可显著改变 R² 数值，令其无法稳定反映整体样本的拟合质量 [[S13, S38]]。

### 无法评价非线性关系

R² 仅能评估变量间的线性相关程度。当变量之间存在显著的非线性关联时，R² 可能输出极低的数值，从而错误地判定二者不存在相关性，对非线性关系的解释能力存在本质局限性 [[S10, S13]]。

### 随自变量增加自然膨胀

R² 数值随回归模型中新增自变量的数量单调上升——即便新增自变量与目标因变量完全无关，R² 也会趋向于 1。因此，高 R² 不能作为模型无过拟合的判定依据 [[S9, S31]]。

### 变量变换引发虚假增高

当因变量经过对数替换、平方根变换等非线性变换后开展回归计算时，R² 会出现虚假性增高的现象。此时输出的高 R² 不能代表原始变量维度上的真实模型拟合质量 [[S9]]。

### 无法区分系统误差与随机误差

高 R² 仅代表模型整体解释了大部分观测方差，无法直接区分残差中的系统误差成分与随机误差成分，也不能证明回归模型是无偏的——部分存在隐蔽系统性偏差的回归模型仍然可以输出很高的 R² 数值 [[S3, S13]]。

### 压铸高噪声数据环境下的误判风险

压铸生产过程的实测数据普遍存在传感器采集噪声和工艺随机波动带来的高噪声特性。单独使用 R² 作为压铸预测模型的唯一评价指标极易发生误判：部分仅在训练集上获得高 R² 的压铸预测模型，在未知实测生产样本上的泛化性能可能极差 [[S6, S28]]。

### 压铸领域推荐联合诊断方法

为规避上述局限，压铸领域的工程实践推荐以下联合诊断流程 [[S3, S8]]：

1. **多指标联合使用**：同时报告普通 R²、调整 R²、预测 R²、RMSE 和 MAE；
2. **残差诊断**：绘制残差正态概率图、残差–拟合值散点图、残差时序图以检验残差的随机性与正态性；
3. **异常判定准则**：当 R² 与调整 R² 的差值大于 0.2，或残差分布出现明显的非随机趋势时，可判定模型存在系统性缺陷，不宜直接投入生产使用。

下图以材料力学试验中的极端异常值实例直观展示了单个离群点对回归拟合结果的颠覆性影响，与 R² 对异常值敏感这一局限性紧密相关 [[S30]]。

![疲劳 Zn 双晶试样旋转应变随距晶界距离变化的散点曲线图：晶界左侧存在一个明显异常值，直观说明单个极端异常点可严重干扰回归拟合与 R² 计算](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4bf1e12-39a4-48c6-9377-3c1aa54e7f14/resource)

## Sources
- S1: [锻造时压力机应变场与模具温度场的数字重构研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03c45709-9489-4d34-ad3a-86ce4dc38ae0/resource) (`03c45709-9489-4d34-ad3a-86ce4dc38ae0`)
- S10: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cc63b8b-043e-40af-98e3-c409fd882f57/resource) (`2cc63b8b-043e-40af-98e3-c409fd882f57`)
- S37: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4ca1b6d-1239-415c-8c8c-d7a3d4fca6f2/resource) (`e4ca1b6d-1239-415c-8c8c-d7a3d4fca6f2`)
- S15: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52c6d6ef-ba5f-4f4e-8dd4-b941007afed2/resource) (`52c6d6ef-ba5f-4f4e-8dd4-b941007afed2`)
- S14: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f7318a2-394e-4d4b-a270-a5a688acbf68/resource) (`4f7318a2-394e-4d4b-a270-a5a688acbf68`)
- S27: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d8076ce-1394-4f6d-bf23-31e938c348cf/resource) (`8d8076ce-1394-4f6d-bf23-31e938c348cf`)
- S4: [锻造时压力机应变场与模具温度场的数字重构研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1158892b-fb21-409d-92e6-f40b02e14608/resource) (`1158892b-fb21-409d-92e6-f40b02e14608`)
- S17: [铝合金三通阀体金属型重力铸造数值模拟与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/550242b2-ace6-47da-b005-4c354c9f19d3/resource) (`550242b2-ace6-47da-b005-4c354c9f19d3`)
- S34: [线性回归分析图，含数据点、最佳拟合线，相关系数R=1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d863fd86-b01d-4edd-8201-b6bac38762d1/resource) (`d863fd86-b01d-4edd-8201-b6bac38762d1`)
- S9: [植物病害流行 数学分析和模型建立](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/256c6d4b-9a9f-4b65-8d04-87b539f8e994/resource) (`256c6d4b-9a9f-4b65-8d04-87b539f8e994`)
- S12: [典型盘型铸件熔模铸造工艺设计与优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b4d45d9-e844-4513-9dfd-98c04e9ad686/resource) (`3b4d45d9-e844-4513-9dfd-98c04e9ad686`)
- S22: [基于响应曲面法的工业安全帽多目标注塑工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/791e5e66-05b3-443d-b8a8-ebc1360fbfb9/resource) (`791e5e66-05b3-443d-b8a8-ebc1360fbfb9`)
- S32: [11042494_回归方程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba45f33c-c988-4e7d-a63f-f12c1d713db7/resource) (`ba45f33c-c988-4e7d-a63f-f12c1d713db7`)
- S16: [表5-3 公式（5-3）预测模型汇总](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53300813-f1c0-489e-bea6-a1a1154771e3/resource) (`53300813-f1c0-489e-bea6-a1a1154771e3`)
- S33: [advanced materials in engineering applications__0b40dace28](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce992b2f-60e8-4a03-b914-2572c8d17008/resource) (`ce992b2f-60e8-4a03-b914-2572c8d17008`)
- S36: [alloys and composites corrosion and mechanical properties__573c8b2ba2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e37745bd-c511-4b99-a917-e8139dfc70ba/resource) (`e37745bd-c511-4b99-a917-e8139dfc70ba`)
- S21: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78f0565b-8ee3-4d9a-b60a-df8d0973afc7/resource) (`78f0565b-8ee3-4d9a-b60a-df8d0973afc7`)
- S40: [aip conference proceedings aip international conference on modeling opti__9dbb7b9ee0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efc07a83-2d43-43f2-b842-bbd550fdeb2d/resource) (`efc07a83-2d43-43f2-b842-bbd550fdeb2d`)
- S2: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07989892-001d-4ef5-bbb2-be926ccd0c70/resource) (`07989892-001d-4ef5-bbb2-be926ccd0c70`)
- S7: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22f7f147-1331-4c2a-9d83-ede652b5d302/resource) (`22f7f147-1331-4c2a-9d83-ede652b5d302`)
- S18: [an adaptive neuro fuzzy inference system anfis model for high pressure d__ae645d3dcf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a34900b-bf1e-4604-9a49-7409e69e37ca/resource) (`6a34900b-bf1e-4604-9a49-7409e69e37ca`)
- S26: [基于PSO-SVM的Q区山西组致密砂岩储层物性参数预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a18d749-b112-48b0-9149-807b8c1a24b5/resource) (`8a18d749-b112-48b0-9149-807b8c1a24b5`)
- S11: [determination of the heat transfer coefficient at the metal die interfac__3400c99740](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f84de20-e7fb-4ebc-a6a4-55f0caa0719f/resource) (`2f84de20-e7fb-4ebc-a6a4-55f0caa0719f`)
- S5: [汽车散热器水室成型的数值分析及优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/17b2e5fb-4b4b-445f-a3bb-b2f646fe3d5d/resource) (`17b2e5fb-4b4b-445f-a3bb-b2f646fe3d5d`)
- S20: [图5-4 RLHS、正交设计（OD）、中心复合设计（CCD）不同样本量构建的数据集上，各机器学习模型的决定系数R²](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77be67c8-d2cd-4f2e-a0a4-cc75766bda7d/resource) (`77be67c8-d2cd-4f2e-a0a4-cc75766bda7d`)
- S19: [表 4 缩松缩孔预测模型可信度分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c474d8b-a28e-4eea-bcb2-3330e593ee76/resource) (`6c474d8b-a28e-4eea-bcb2-3330e593ee76`)
- S35: [(b) 实际-预测拟合图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1613cee-e381-4af4-81f7-2c8d11a41c87/resource) (`e1613cee-e381-4af4-81f7-2c8d11a41c87`)
- S39: [图4-2 总凝固时间回归分析：实际-预测拟合图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed23a76a-da1f-4672-b4e6-eab34b44f346/resource) (`ed23a76a-da1f-4672-b4e6-eab34b44f346`)
- S13: [植物病害流行 数学分析和模型建立](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b33aa15-2427-4e7f-a3d8-29c038f7a5e6/resource) (`4b33aa15-2427-4e7f-a3d8-29c038f7a5e6`)
- S38: [advances in statistical monitoring of complex multivariate processes with applications in industrial process control_...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e888a390-466e-4609-8ce3-6ff18a491f33/resource) (`e888a390-466e-4609-8ce3-6ff18a491f33`)
- S31: [大尺寸铝合金轮毂低压铸造凝固模拟及结构强度的仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ac33f4e5-9e5c-4521-b609-f89354e0f922/resource) (`ac33f4e5-9e5c-4521-b609-f89354e0f922`)
- S3: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0bb6c3d9-0ab5-486e-9145-e311e5eb9d10/resource) (`0bb6c3d9-0ab5-486e-9145-e311e5eb9d10`)
- S6: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b919417-90ed-48db-89ab-a20dcbfbe23f/resource) (`1b919417-90ed-48db-89ab-a20dcbfbe23f`)
- S28: [铝合金压铸工艺参数不确定性对铸件静强度性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91f2d11e-f275-4e47-b3c8-2a8c40b0f3d8/resource) (`91f2d11e-f275-4e47-b3c8-2a8c40b0f3d8`)
- S8: [压铸模具型芯寿命改善研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24186f61-2cdf-41df-a9b9-05f597c96474/resource) (`24186f61-2cdf-41df-a9b9-05f597c96474`)
- S30: [Fig.8: Rotation strain vs. distance from grain boundary for fatigued Zn bicrystal sample T1R](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4bf1e12-39a4-48c6-9377-3c1aa54e7f14/resource) (`a4bf1e12-39a4-48c6-9377-3c1aa54e7f14`)