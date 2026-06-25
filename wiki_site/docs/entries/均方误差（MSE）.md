---
version: "v1"
generated_at: "2026-06-18T12:35:40+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 24
  source_quality_score: 0.85
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

均方误差（Mean Squared Error，MSE）是回归分析中最基本的预测误差评价指标与损失函数之一[[S11,S17]]。MSE通过计算模型预测值与真实值之间差值的平方的算术平均值，量化了模型整体预测精度，数值越小表示预测误差越小，模型拟合效果越好[[S17]]。在统计估计理论中，MSE也被定义为参数估计误差平方的数学期望，用以衡量估计量在均方意义下的风险[[S6]]。MSE由于具有良好的数学可微性质，广泛作为机器学习回归模型的优化目标函数和性能评价指标[[S7,S29]]。在压铸工艺参数优化、铸件质量与力学性能预测等研究场景中，当采用回归模型进行数值型目标（如凝固时间、温度场、铸件静强度等）的预测时，MSE是最常用的模型训练损失函数和模型评估指标之一[[S1,S14,S11]]。

## 定义与公式

### 离散样本形式

对于包含 $m$ 个样本的数据集，设第 $i$ 个样本的真实目标值为 $y_i$，模型预测值为 $\hat{y}_i$，则均方误差的定义为[[S11,S17,S19]]：

$$MSE = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2$$

该公式为回归模型评估中最通用的离散形式。在文献中，真实值与预测值存在多种符号约定。部分工程论文用 $y_i$ 与 $y_i'$ 分别表示真实值与预测值[[S14]]，部分机器学习文献用 $o_k$ 表示目标输出、$a_k$ 表示模型预测输出[[S14,S31]]，另有统计学文献以 $y_i$ 与 $\hat{y}_i$ 区分观测值与预测值[[S21,S27]]。尽管符号有所差异，其数学含义均为预测残差平方的样本均值。

### 期望定义形式

在贝叶斯估计理论中，均方误差可拓展为连续概率空间上的积分表达。若以 $x$ 表示待估参数，$\hat{x}(y)$ 表示基于观测 $y$ 的估计量，$p(x, y)$ 为联合概率密度函数，则均方误差定义为估计误差平方的数学期望[[S6]]：

$$R_{ms} = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x - \hat{x}(y))^2 \, p(x, y) \, dx \, dy$$

此时最小均方误差（MMSE）估计量等价于给定观测下的条件均值估计，即 $\hat{x}_{ms}(y) = \mathbb{E}[x \mid y]$[[S6,S7]]。

## 核心属性

**取值范围与最优值**：MSE 的取值范围为 $[0, +\infty)$。当且仅当所有样本的预测值与真实值完全一致时，MSE = 0，这是理论上的最优状态[[S11,S17]]。

**对异常值的高度敏感性**：由于MSE公式中将预测残差进行平方运算，较大的单个误差会得到远超原始误差幅度的权重放大。具体而言，若某样本的绝对误差是另一个样本的 $k$ 倍，其对MSE总和的贡献将是后者的 $k^2$ 倍[[S3,S11]]。这意味着少量极端异常样本就会显著拉高整体MSE值，使得模型评估得分可能被少量离群点主导。

**处处可微性**：MSE是参数空间上的二次函数，在整个实数域上处处可微。这一性质使其能够直接适配基于梯度下降的各类机器学习优化算法（如随机梯度下降、Adam等），是回归任务中最常用的可微损失函数之一[[S6,S7]]。

**尺度依赖性**：MSE的数值量级与目标变量的量纲（或量纲的平方）直接绑定。例如，若目标变量以“秒”为单位，MSE的单位是“平方秒”；若以“摄氏度”为单位，则MSE的单位是“平方摄氏度”。这一特性使得不同量纲预测任务之间的MSE无法直接横向对比[[S8]]。

## 与相关度量的对比

回归模型评估通常不依赖单一指标，而是采用MSE、MAE、RMSE和 $R^2$ 等多指标联合评估。各指标的定义与特点对比如下[[S11,S17,S16,S21]]：

| 指标 | 公式 | 对异常值敏感度 | 量纲与目标一致 | 说明 |
|:---|:---|:---|:---|:---|
| **MSE** | $MSE = \frac{1}{m}\sum_{i=1}^{m}(y_i - \hat{y}_i)^2$ | **极高**（平方放大） | 否（平方量纲） | 可微，便于梯度优化 |
| **MAE** | $MAE = \frac{1}{m}\sum_{i=1}^{m}\|y_i - \hat{y}_i\|$ | 低（所有误差等权） | 否（与目标同量纲） | 鲁棒性优于MSE，不易被异常值影响 |
| **RMSE** | $RMSE = \sqrt{\frac{1}{m}\sum_{i=1}^{m}(y_i - \hat{y}_i)^2}$ | **极高** | **是**（与目标同量纲） | 量纲直观，便于工程解释 |
| **$R^2$** | $R^2 = 1 - \frac{\sum_{i=1}^{m}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{m}(y_i - \bar{y})^2} = 1 - \frac{MSE}{Variance}$ | — | 无量纲 | 表示模型解释的方差比例，取值 $[0,1]$，越接近1越好 |

此外，均方对数误差（MSLE）及其衍生指标均方根对数误差（RMSLE）适用于目标变量取值跨度较大的场景（例如房价从数万到数千万），在H2O广义线性回归等框架中可直接输出[[S23]]。

在压铸领域的具体应用中，研究者通常同时报告MSE、MAE、RMSE与 $R^2$ 四项指标，以全面评估模型性能。例如，在铝合金车轮凝固时间预测任务中，BO-XGBoost模型的MSE为4.726，显著低于LSTM模型和原始XGBoost模型，同时在MAE和 $R^2$（0.99以上）上也表现最优，综合表明其预测误差更小、对异常值抑制效果更好、对数据的解释能力更强[[S1]]。

## 在回归问题中的典型应用

### 作为损失函数

在基于梯度优化的回归模型训练中，MSE是最常用的损失函数之一[[S29,S14,S31]]。

**线性回归中的闭式解**：在线性回归场景下，以MSE最小化为目标函数（即最小二乘法），通过对损失函数关于权重 $\mathbf{w}$ 和偏置 $b$ 求偏导并令导数为零，可直接求得全局最优参数的解析解 $\mathbf{W} = (\mathbf{X}^{\mathrm{T}}\mathbf{X})^{-1}\mathbf{X}^{\mathrm{T}}\mathbf{Y}$，无需迭代过程即可完成模型拟合[[S13,S4]]。

**神经网络中的反向传播训练**：在全连接神经网络（多层感知机）的回归训练中，MSE与反向传播算法及梯度下降优化器配合使用。每次迭代中，损失函数值引导网络权重的更新方向，逐步降低预测误差直至模型收敛[[S14,S31]]。在铸造工艺预测的工程场景中，通常将训练迭代轮次设置为3000次即可获得稳定的收敛效果[[S14]]。

经典BP神经网络训练过程中，MSE随训练轮次呈现典型的快速下降后趋于稳定的收敛模式。下图为某BP网络训练过程的MSE变化曲线，训练初期MSE快速下降，在5000轮时达到0.0076348的最佳训练性能（纵轴为对数尺度）[[S9]]。

![经典BP神经网络训练均方误差变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/426c5b5d-10c1-481a-86d8-6a10dd60a12d/resource)

### 作为性能评估指标

MSE作为回归模型的通用评估指标，需与MAE、RMSE、$R^2$ 搭配使用进行多维评估，不可仅依赖单一MSE值判定模型优劣[[S1,S30]]。在压铸相关回归研究中，评估规范通常为：MSE越低说明模型对大误差的抑制效果越好，$R^2$ 越接近1说明模型整体方差解释能力越强[[S1,S17]]。

下表展示了一个典型的模型对比实例——基础BP模型与WOA优化BP模型的回归评价指标对比，WOA-BP模型的所有误差指标均显著优于原始BP模型[[S22]]。

| 模型 | MAE | MSE | RMSE | MAPE |
|:---|:---|:---|:---|:---|
| BP | 较高 | 较高 | 较高 | 较高 |
| WOA-BP | **远小于BP** | **远小于BP** | **远小于BP** | **远小于BP** |

## 压铸领域的关联

### 自动化工艺设计中的回归预测

在铝合金压铸工艺参数优化与铸件质量预测场景中，当采用回归模型对连续物理量进行数值预测时，MSE是核心的模型训练损失函数和评估指标。以下为基于检索证据的典型应用场景：

**压铸工艺数值预测**：在全连接神经网络（ANN）用于预测铸件凝固速度R和Niyama判据的过程中，模型以铸件热模数、浇注温度、铸型温度、换热系数为输入，使用MSE作为损失函数，配合TensorFlow框架进行反向传播训练，迭代3000次后可获得稳定的收敛效果，总体平均百分比预测误差低于10%[[S14,S31]]。

**铝合金车轮凝固时间代理预测**：在基于BO-XGBoost的铝合金车轮凝固时间代理预测模型中，以交叉验证下的MSE为贝叶斯优化目标函数，对模型超参数进行自动调优，再以MSE、MAE、RMSE、$R^2$ 四项指标综合评价模型性能[[S11,S1]]。结果显示BO-XGBoost的MSE为4.726，显著优于LSTM和默认参数XGBoost模型[[S1]]。

**压铸模具温度场预测**：在铝车轮压铸模具温度场的时间序列预测研究中，采用LSTM和LightGBM模型进行回归预测，以MSE、MAE、RMSE、$R^2$ 作为多元评价体系[[S19]]。

### 铸件物理预测的模型评价场景

在熔铸装药顺序凝固温度场快速预测任务中，使用条件生成对抗网络（cGAN）作为温度场图像生成模型，以MSE和MAE作为生成图像质量的定量评估指标。在21~25组测试集中MSE平均值为0.0011，最大值仅0.0018，表明生成温度场分布图与仿真结果高度一致[[S12]]。

> **注意**：上述浇注成型的范畴与高压/低压压铸存在工艺差异，但其中MSE作为图像级别误差评估的用法对压铸领域温度场预测具有方法论参考价值。

### MSE收敛特性与模型对比

下图展示了两类非线性动态系统近似模型（标注为H与V）在在线最小二乘识别过程中MSE随参数k的变化对比曲线。曲线随k增大逐步下降并趋于平稳，且Volterra模型（V）全程MSE低于Hammerstein模型（H），直观体现了MSE作为模型性能对比手段的收敛趋势判别能力[[S26]]。该可视化方法在压铸领域的代理模型超参数寻优与模型选型评估中具有参考意义。

![两种非线性动态系统近似模型的MSE随识别参数k变化对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9e1fd24-dc0b-4dc2-89d8-2b32fdc6ab94/resource)

## 局限性与改进

**异常值敏感性及其应对**：MSE对大误差的平方放大效应使得其极易被少数异常样本主导。在数据集包含离群点的情形下，为最小化MSE，模型拟合会被迫向离群点偏移，从而在正常样本区域产生系统性偏差[[S3,S8]]。常见的改进方案包括[[S8,S10,S24]]：
- 替换为**平均绝对误差（MAE）**，直接基于误差绝对值计算损失，所有误差享有均等权重，不对大误差进行平方放大，鲁棒性显著优于MSE[[S16,S11]]；
- 采用**鲁棒损失函数**，如 $\varepsilon$-不敏感损失函数、Huber损失函数或修剪最小二乘（Least Trimmed Squares, LTS）损失函数。Huber损失在误差较小时保留MSE的二次形式以保持可微优势，在误差超过阈值后切换为线性惩罚模式，有效降低异常值的影响[[S24,S10]]。

**尺度依赖性及其应对**：MSE的数值与目标变量的量纲（或其平方）绑定，不同量纲的预测任务之间不可直接横向对比。缓解该问题的方法是对输入和输出数据执行标准化（Z-score）或归一化（Min-Max）预处理，以消除不同量纲带来的尺度差异[[S8]]。

**压铸文献中的MSE使用现状**：在检索所得的压铸领域相关文献中，MSE普遍作为标准回归评估指标被直接引用，未见针对压铸工艺场景的专门改进MSE变体或行业特定标准的报道。模型评估均遵循通用的多指标联合评估规范[[S1,S17,S19,S14]]。

## Sources
- S11: [数据驱动的铸件凝固时间代理预测模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55da5547-6a70-405d-8d21-69a859178f12/resource) (`55da5547-6a70-405d-8d21-69a859178f12`)
- S17: [铝合金压铸工艺参数不确定性对铸件静强度性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1c59ed2-1005-4b7c-8336-621b0f1dbd85/resource) (`a1c59ed2-1005-4b7c-8336-621b0f1dbd85`)
- S6: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3cdd580e-d449-44f3-8f39-e27db0ec7196/resource) (`3cdd580e-d449-44f3-8f39-e27db0ec7196`)
- S7: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e2d1953-4381-435c-a76b-6e4260e601e6/resource) (`3e2d1953-4381-435c-a76b-6e4260e601e6`)
- S29: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5800428-c9fd-4d28-913f-c77927c01aac/resource) (`f5800428-c9fd-4d28-913f-c77927c01aac`)
- S1: [铝合金压铸工艺参数不确定性对铸件静强度性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1346b5b9-d89c-4a0c-b4a7-86a204bcf392/resource) (`1346b5b9-d89c-4a0c-b4a7-86a204bcf392`)
- S14: [ZL205A合金圆筒状包络构件低压铸造线状偏析形成机理及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76f95034-9fc4-4b04-babe-8271c787697e/resource) (`76f95034-9fc4-4b04-babe-8271c787697e`)
- S19: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7adb42a-3943-4d85-95a0-657df6faf826/resource) (`a7adb42a-3943-4d85-95a0-657df6faf826`)
- S31: [ZL205A合金圆筒状包络构件低压铸造线状偏析形成机理及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd34fe9e-3c45-4317-9ef3-ebff214f7761/resource) (`fd34fe9e-3c45-4317-9ef3-ebff214f7761`)
- S21: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be4c9f59-644a-4a30-9f23-b8407e9b263f/resource) (`be4c9f59-644a-4a30-9f23-b8407e9b263f`)
- S27: [局部近似误差指标定义](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df375e2c-4c50-4cb4-adc8-91f6c3adf6a5/resource) (`df375e2c-4c50-4cb4-adc8-91f6c3adf6a5`)
- S3: [人工智能计算agent基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b57b448-39af-4ba2-ae8a-4506fe28b694/resource) (`2b57b448-39af-4ba2-ae8a-4506fe28b694`)
- S8: [chemical process control cpciv proceedings of the fourth international conference on chemical process control padre i...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ffaaeb1-a30b-4457-aa3d-d33a5a882aac/resource) (`3ffaaeb1-a30b-4457-aa3d-d33a5a882aac`)
- S16: [融合岩性信息的CNN-LSTM-GAT深度网络孔隙压力预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60/resource) (`95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60`)
- S23: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4e8191b-19a0-4a2b-9569-219658c383b4/resource) (`c4e8191b-19a0-4a2b-9569-219658c383b4`)
- S13: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5cd0e5a9-3dcd-484c-904a-d626bad3ac9e/resource) (`5cd0e5a9-3dcd-484c-904a-d626bad3ac9e`)
- S4: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b94a693-9ca6-4b45-aa7e-c85bd0dbeda8/resource) (`2b94a693-9ca6-4b45-aa7e-c85bd0dbeda8`)
- S9: [经典BP神经网络训练均方误差变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/426c5b5d-10c1-481a-86d8-6a10dd60a12d/resource) (`426c5b5d-10c1-481a-86d8-6a10dd60a12d`)
- S30: [融合岩性信息的CNN-LSTM-GAT深度网络孔隙压力预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5e768e7-b316-4a59-b5b6-366fa98c1b1e/resource) (`f5e768e7-b316-4a59-b5b6-366fa98c1b1e`)
- S22: [表6 2种模型预测误差](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4d56d53-1c83-4894-9749-bbbe2aa46083/resource) (`c4d56d53-1c83-4894-9749-bbbe2aa46083`)
- S12: [移动热源作用下熔铸装药顺序凝固温度场快速预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5798ae9c-0a2a-4996-ac54-9943435dcbf6/resource) (`5798ae9c-0a2a-4996-ac54-9943435dcbf6`)
- S26: [Fig.11：广义Hammerstein（H）与参数Volterra（V）模型在线最小二乘识别Wiener模型的MSE随k变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9e1fd24-dc0b-4dc2-89d8-2b32fdc6ab94/resource) (`d9e1fd24-dc0b-4dc2-89d8-2b32fdc6ab94`)
- S10: [advances in statistical monitoring of complex multivariate processes with applications in industrial process control_...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a2534d8-1baa-4c92-a76f-652ba2035c99/resource) (`4a2534d8-1baa-4c92-a76f-652ba2035c99`)
- S24: [神经网络与机器学习英文版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9af827d-f690-442b-b1a6-e3c57840533e/resource) (`c9af827d-f690-442b-b1a6-e3c57840533e`)