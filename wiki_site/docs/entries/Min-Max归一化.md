---
version: "v1"
generated_at: "2026-06-18T12:23:59+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 18
  source_quality_score: 0.84
  freshness_score: 0.92
  evidence_coverage_score: 1.0
---

## 概述

最小-最大归一化（Min-Max Normalization），亦称离差标准化（Rescaling）、Min-Max Scaling，是一种广泛应用于数据预处理领域的特征缩放技术[[S12,S2,S17]]。该方法通过对原始数据进行线性变换，将不同特征的值统一映射到相同的数值区间内，从而消除因量纲或尺度差异带来的分析偏差[[S10,S12]]。在压铸工艺数据分析中，该技术常用于预处理浇注温度、压射速度、模具温度、流量等多维度异构参数，为后续机器学习建模提供尺度一致的输入数据[[S3,S4,S20]]。

## 定义与公式

最小-最大归一化的标准数学计算公式为[[S13,S3,S12,S10,S7]]：

$$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$

各变量含义如下[[S13,S12,S17]]：
- $X_{\text{norm}}$：归一化后的输出数值
- $X$：对应特征的原始输入数值
- $X_{\min}$：该特征在全部样本中的最小值
- $X_{\max}$：该特征在全部样本中的最大值

该公式通过计算原始值与最小值的偏差占整体数据范围的比例，完成线性缩放映射[[S17,S19,S10]]。

## 核心属性

### 输出范围

在默认配置下，最小-最大归一化将所有原始特征值线性映射到[0, 1]的闭区间内，缩放后的输出值不会超出该范围[[S12,S2,S3,S10]]。

### 线性缩放特性

该方法属于纯线性变换，不会改变原始数据的相对分布形态，也不会影响数据点之间的大小排序关系，仅对原始数值进行等比例的线性缩放[[S17,S19,S10]]。

### 对异常值的敏感性

最小-最大归一化的计算完全依赖于数据集的全局最小值$X_{\min}$和最大值$X_{\max}$[[S3,S2]]。当数据集中存在显著的极端异常值时，这些极值会严重偏离正常数据范围，导致归一化结果整体失真。因此，归一化操作必须放在异常值处理流程之后执行[[S3]]。

## 局限性

### 异常值敏感

当数据集中出现极端异常值，使得$X_{\min}$与$X_{\max}$被显著拉大或缩小，会严重扭曲整个数据集的归一化结果[[S3]]。使用该方法前必须先完成异常值剔除处理[[S3,S9]]。

### 新样本溢出风险

当新增测试样本的数值超出原始训练集预设的$X_{\min}$和$X_{\max}$范围时，归一化计算结果可能超出[0, 1]区间，无法保证所有特征仍处于统一的缩放范围，进而影响后续模型稳定性[[S5]]。

### 适用条件

该方法更适合特征上下限预先已知、数据集内离群值数量少且数据分布相对均匀的场景[[S2,S3]]。非正态分布的数据集使用该方法的效果通常优于Z-score标准化方案[[S3]]。

## 与相关归一化方法的比较

| 方法 | 公式 | 输出范围 | 对异常值敏感性 | 适用条件 | 来源 |
|------|------|----------|----------------|----------|------|
| Min-Max归一化（离差标准化） | $X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$ | [0, 1] | 高 | 数据分布相对均匀、离群值少、非正态分布 | [[S2,S3,S12]] |
| Z-score标准化（0均值标准化） | $y = \frac{x - \mu}{\sigma}$ | 均值为0、方差为1 | 中等 | 数据近似服从高斯分布 | [[S12,S7]] |
| Robust缩放 | 基于中位数和四分位距 | 无固定区间 | 低 | 存在大量异常值的数据集 | [[S18]] |

Z-score标准化要求原始数据的分布近似服从高斯分布，否则归一化处理效果不理想[[S12]]。Robust缩放基于中位数和四分位距进行特征变换，不受极端异常值的大幅干扰，对离群点的鲁棒性远高于Min-Max归一化[[S18]]。

## 压铸领域的典型应用

Min-Max归一化在压铸数据分析中主要应用于需要将不同单位的工艺参数统一到同一尺度的建模场景[[S3]]。

**铝车轮低压铸造模具温度场预测**：在模具温度场预测中，由于采集到的冷却流量、冷却风流量、保温炉温度等实测工艺数据呈现非正态分布，研究选择Min-Max归一化作为预处理方案，将91000余条仿真样本和28000余条实测样本全部缩放至[0, 1]区间，该操作在空值填补和异常值剔除之后进行[[S3,S13]]。

![铝车轮低压铸造工艺部分实测数据频数分布直方图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7dba6031-5f2f-426e-a177-2b0a471d3a21/resource)

实测数据的频数分布直方图（上图）可用于解释为何选定Min-Max归一化：当压铸实测数据呈非正态分布时，采用该方法较Z-score标准化更为适配[[S14]]。

**变速箱壳体压铸质量预测**：该场景中将浇注温度、慢/快压射速度、模具预热温度等工艺参数通过MATLAB的`mapminmax`函数缩放到[0, 1]区间，避免参数数量级差异导致BP神经网络训练结果偏差。预测输出后通过反归一化得到最终质量分类结果[[S4]]。

**铝合金汽车离合器壳体真空压铸工艺参数预测**：对筛选出的5个关键工艺特征采用Min-Max归一化处理，消除尺度差异后将数据输入CNN-LSTM机器学习模型，以提升预测精度和泛化能力[[S20]]。

**薄壁结构件压铸开模温度预测**：在BiLSTM-Attention-FWA预测模型构建中，Min-Max归一化用于预处理合模温度、冷却水温、冷却时间、管道与模具间距、压射时间等多维度生产数据，使其适配sigmoid激活函数的输入要求，避免数值较小的输入因子权重被错误缩小。预测结果经反归一化公式还原为真实开模温度值[[S9,S15]]。

反归一化的数学表达式为[[S15]]：

$$x = x_i' (x_{\max} - x_{\min}) + x_{\min}$$

其中$x$是反归一化后的最终预测结果，$x_{\max}$和$x_{\min}$是序列中的最大、最小值，$x_i'$是归一化后的预测值。

## 实现参考

### scikit-learn标准实现步骤

在Python的scikit-learn库中，可使用`MinMaxScaler`类实现Min-Max归一化[[S10,S1,S16,S6]]：

1. 从`sklearn.preprocessing`模块导入`MinMaxScaler`类；
2. 实例化缩放器对象；
3. 调用`fit()`方法遍历输入数据集，逐维度统计并计算各特征的$X_{\min}$和$X_{\max}$极值；
4. 调用`transform()`方法对每个原始样本代入归一化公式进行线性变换，得到[0, 1]区间的缩放结果；
5. 可直接调用`fit_transform()`方法一次性完成极值拟合与数据缩放两个操作。

### MATLAB实现参考

在MATLAB环境中，可使用`mapminmax`函数实现归一化[[S4]]：

```matlab
[p_train, ps_input] = mapminmax(P_train, 0, 1);
p_test = mapminmax('apply', P_test, ps_input);
```

其中`P_train`与`P_test`分别为训练集和测试集的输入数据；`p_train`与`p_test`为归一化后的结果；`ps_input`为保存的归一化结构体，用于对新数据执行相同的缩放。

## Sources
- S12: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75c925e4-0f65-4d38-98ed-68f8b39459db/resource) (`75c925e4-0f65-4d38-98ed-68f8b39459db`)
- S2: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1da6be75-a76d-47ad-80aa-0a61525d6a3f/resource) (`1da6be75-a76d-47ad-80aa-0a61525d6a3f`)
- S17: [考虑螺旋离心泵水力性能及铸造成型的多目标优化设计研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad6933aa-6fba-4b0e-b0a7-f819a18396f6/resource) (`ad6933aa-6fba-4b0e-b0a7-f819a18396f6`)
- S10: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6588f311-79e7-4899-9871-71ff31d3012f/resource) (`6588f311-79e7-4899-9871-71ff31d3012f`)
- S3: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2439d336-a625-47b7-970c-53052b637be3/resource) (`2439d336-a625-47b7-970c-53052b637be3`)
- S4: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ed94a10-afa5-4c16-b317-e0f210d3b438/resource) (`2ed94a10-afa5-4c16-b317-e0f210d3b438`)
- S20: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9bd1032-29cc-4459-8429-223fc50a2bf1/resource) (`f9bd1032-29cc-4459-8429-223fc50a2bf1`)
- S13: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7901efd2-b154-45e1-9433-6bef156ce2ed/resource) (`7901efd2-b154-45e1-9433-6bef156ce2ed`)
- S7: [automation for food engineering food quality quantization and process co__658da4cafc](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a701d05-b4fe-48b3-9cda-2b65113559f6/resource) (`3a701d05-b4fe-48b3-9cda-2b65113559f6`)
- S19: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8ffbed1-8d2b-4768-bc13-5e974a1063c3/resource) (`f8ffbed1-8d2b-4768-bc13-5e974a1063c3`)
- S9: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/583a0f67-c798-49e0-a240-463f14c36e09/resource) (`583a0f67-c798-49e0-a240-463f14c36e09`)
- S5: [a multiple objective decisionmaking approach for assessing simultaneous__b40edcb5cb](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f4e9376-35e6-41fc-97ee-06ccc93cbcf3/resource) (`2f4e9376-35e6-41fc-97ee-06ccc93cbcf3`)
- S18: [advances in statistical monitoring of complex multivariate processes with applications in industrial process control_...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e888a390-466e-4609-8ce3-6ff18a491f33/resource) (`e888a390-466e-4609-8ce3-6ff18a491f33`)
- S14: [图5-7 部分实测数据频数分布直方图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7dba6031-5f2f-426e-a177-2b0a471d3a21/resource) (`7dba6031-5f2f-426e-a177-2b0a471d3a21`)
- S15: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9eae2a19-8cc6-4814-b808-bfd9400e8711/resource) (`9eae2a19-8cc6-4814-b808-bfd9400e8711`)
- S1: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19d6f46e-ea0f-47b2-8893-3134e895e08f/resource) (`19d6f46e-ea0f-47b2-8893-3134e895e08f`)
- S16: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3fbf1ee-3988-4508-88b3-130c7fec5f43/resource) (`a3fbf1ee-3988-4508-88b3-130c7fec5f43`)
- S6: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/307ad6bb-9535-4acf-9277-16a20f7969d6/resource) (`307ad6bb-9535-4acf-9277-16a20f7969d6`)