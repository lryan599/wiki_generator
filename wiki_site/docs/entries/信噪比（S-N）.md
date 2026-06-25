---
version: "v1"
generated_at: "2026-06-21T05:55:06+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 24
  source_quality_score: 0.84
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

在田口质量工程（Taguchi Method）的语境下，信噪比是衡量产品品质特性对外界噪声因素（不可控干扰）抗扰能力的核心统计指标[[S16,S22]]。它与电子通信领域基于电信号功率比值定义的物理信噪比属于两个独立的应用体系，两者的物理意义与适用场景存在本质差异[[S16,S22]]。

田口方法中的信噪比源出于质量损失函数（Quality Loss Function）的数学推导，其统计本质为「信号功率」与「噪声功率」的比值，一般形式可表示为 **η = S/N = μ²/σ²**，其中 **μ** 为多次试验所测品质特性的均值，**σ²** 为品质特性的总体方差[[S22,S16]]。信噪比的法定计量单位为分贝（dB），其对数变换形式使得它成为无量纲的统计评价指标，旨在统一衡量品质特性的均值水平与波动程度[[S14,S15]]。

在压铸与低压铸造工艺优化中，信噪比通常被直接用作实验设计的响应变量。其值越大，表示该组工艺参数组合下的铸件品质越稳定，对不可控噪声因素的敏感度越低[[S19,S6]]。

## 三类信噪比特性分类

田口方法依据品质特性的优化目标方向，将信噪比计算划分为望小特性、望大特性与望目特性三种类型[[S16,S22]]。

### 望小特性

适用于品质特性取值为非负、理论最优值为零的场景——即特性值越小越好[[S16,S24]]。在压铸语境中，缩孔体积、缩松体积、孔隙率、气孔率、翘曲量、内应力等缺陷指标均采用望小特性信噪比进行评估[[S4,S19,S21,S15]]。

标准公式为[[S16,S24,S15,S21,S4,S19]]：

\[
S/N = -10 \log\left(\frac{1}{n}\sum_{i=1}^{n} y_i^2\right)
\]

其中，\(y_i\) 为第 \(i\) 次试验的缺陷量化值（如缩孔体积、孔隙率等），\(n\) 为该组试验的总次数。S/N 值越高，表明该组工艺条件下缺陷指标的平均值越小，同时各次试验结果的离散程度越低[[S19,S4]]。该公式已在多本工程教材、压铸工艺优化研究及商用品质工程软件（如 Minitab）中得到交叉验证[[S16,S24,S15,S14,S21,S12]]。

![Minitab分析田口设计选项窗口，展示望小、望目、望大三类信噪比的标准实现公式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8b225e9c-21a5-461a-8616-6d809d5ec65c/resource)

图：Minitab 软件「分析田口设计」选项界面，直观呈现望小特性的标准公式 η = −10×Log₁₀(ΣY²/n)，与教材中的解析表达式完全一致[[S12]]。

### 望大特性

适用于品质特性取值为正、理论最优值尽可能大的场景[[S16,S25]]。在压铸中常见于铸件致密度、力学强度、产品服役寿命、合格率等需要最大化的品质指标。

标准公式为[[S16,S25,S24]]：

\[
S/N_{\max} = -10 \log\left(\frac{1}{n}\sum_{i=1}^{n}\frac{1}{y_i^2}\right)
\]

### 望目特性

适用于品质特性存在固定标称目标值、优化目标为响应值尽可能接近该目标值同时最小化波动的场景[[S16]]。压铸中典型的应用是尺寸精度控制、特定流量或压力参数的目标值优化。

标准公式为[[S16]]：

\[
S/N_{\text{obj}} = 10 \log\left(\frac{\mu^2}{\sigma^2}\right)
\]

其中 \(\mu\) 为 \(n\) 次试验的均值，\(\sigma^2\) 为总体方差。

## 铸件缺陷作为望小特性的量化方法

在压铸及低压铸造工艺优化中，缩孔、缩松、气孔、卷气等内部缺陷是评估铸件品质的核心指标。这些缺陷的体积、面积比或孔隙率均为非负量，且越小表明铸件致密性越好，因此天然适用于望小特性信噪比进行稳健性分析[[S19,S4,S21]]。

使用 ProCAST 等铸造仿真软件时，通常通过后处理模块统计铸件 Total Shrinkage Porosity 超过某一阈值（如 3%）以上的体积（记为 \(V_{\text{缩}}\)），作为各组试验的品质特性响应值[[S4,S5]]。将该值代入望小特性 S/N 公式，计算得到的信噪比越大，表示该组工艺条件下的缩松缩孔体积均值越低，对噪声因素的抗干扰能力越强[[S21,S5]]。

![低压铸造水龙头铸件缩孔缺陷实物图，直观展示为何将此类缺陷设为越小越好的望小指标](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0543596b-b9ed-4aa3-a071-f8a890dd494c/resource)

图：低压铸造生产的水龙头铸件缩孔缺陷形态。此类内部缺陷的体积或孔隙率是压铸望小特性 S/N 分析的典型品质指标[[S2]]。

## 压铸工艺优化中的信噪比应用流程

### 标准实验设计与分析步骤

田口信噪比在压铸工艺优化中的典型应用流程包括以下环节[[S9,S6,S14]]：

1. 确定品质特性与目标类型（如缩孔体积→望小特性，致密度→望大特性）
2. 选定可控因子及其水平（浇注温度、模具温度、充型速度、保压压力与时间等）
3. 选择正交表（如 L₉、L₁₆、L₂₇ 等）安排试验方案
4. 如考虑噪声因素影响，进一步构建内表（无噪声理想工况）与外表（叠加噪声实际工况）[[S6,S7]]
5. 通过仿真或实物试验获取各组的品质特性响应值
6. 计算各组 S/N 值并进行极差分析与方差分析
7. 绘制信噪比主效应图，确定各因子最优水平组合
8. 验证最优组合的预测改善效果

Minitab 等商用软件提供集成化的田口设计分析功能，可同时分析信噪比与均值的主效应，为工艺优化提供高效的统计支持[[S1]]。

![Minitab田口设计图形配置界面，展示同时勾选"信噪比"与"均值"选项的分析流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/050d5aae-352a-456d-aa94-0e7ebf4fd550/resource)

图：Minitab 软件田口设计图形选项配置界面，勾选「信噪比」与「均值」即可生成因子主效应分析图[[S1]]。

### 典型实验数据案例

下表为 A360 铝合金冷却盖板压铸工艺优化中三个核心工艺参数各水平下的缩孔缩松体积信噪比均值，可用于判断各因子对铸件品质稳定性的影响权重[[S8]]。

| 水平 | 浇注温度 (A) | 模具预热温度 (B) | 快压射速度 (C) |
|------|--------------|-----------------|---------------|
| 1 | （信噪比均值，dB） | （信噪比均值，dB） | （信噪比均值，dB） |
| 2 | （信噪比均值，dB） | （信噪比均值，dB） | （信噪比均值，dB） |
| 3 | （信噪比均值，dB） | （信噪比均值，dB） | （信噪比均值，dB） |
| 极差 (Delta) | 1.2027 | 0.6552 | 0.1942 |
| 排序 | 1 | 2 | 3 |

表：A360 铝合金冷却盖板压铸工艺信噪比均值及极差[[S8]]。极差越大，该因子对品质稳定性（R1 指标）的影响越显著。该案例中影响排序为浇注温度 > 模具预热温度 > 快压射速度[[S14,S8]]。

另一项铸铝电机转子压铸研究采用 L₁₆ 正交表，以慢压-快压转换点、压射速度、铝液温度、模具温度四个因子进行试验，记录了 16 组缩松缩孔体积的信噪比（dB）实测值，用于极差分析与因子影响主次排序[[S18]]。

### 典型优化效果

在基于望小 S/N 的压铸工艺优化实践中，已有多项研究证实了该方法在降低铸件缺陷方面的显著效果。一项针对铝合金压铸的 L₁₆ 正交试验表明，按信噪比最大原则优选的工艺参数组合可将孔隙率均值从优化前的约 0.486% 降至约 0.25%，降幅约为 48%；对应的工艺成本损耗降幅可达 71%[[S5,S11]]。

## 可控因子与噪声因素

### 可控因子

压铸及低压铸造场景下可主动调控的工艺变量包括[[S6,S14,S9,S4]]：

- 浇注温度（金属液温度）
- 模具预热温度
- 充型压力 / 充型速度 / 压射速度（慢压射、快压射分阶段）
- 保压压力与保压时间
- 慢/快压射距离转换点

### 不可控噪声因素

实际铸造生产中难以完全精确控制的噪声因素包括[[S6,S7,S14,S9]]：

- 人工操作随机波动
- 环境温度变化
- 供电电路波动
- 设备长期运行精度漂移
- 原材料的批次差异

### 内外表设计原理

为量化噪声因素对铸件品质的影响，田口方法采用内外表实验设计[[S6,S7]]。内表反映在指定工艺参数组合且无噪声影响下的理想品质情况；外表反映在内表各样本点上叠加噪声干扰后表现出的实际品质情况。通过计算各组试验的 S/N 值，可以有效评价不同参数组合对外界噪声的稳健性，进而筛选出抗干扰能力最强的工艺参数组合[[S6,S19]]。

## 与品质损失函数的关系

田口信噪比与田口二次品质损失函数存在严格的数学推导关联[[S13,S17,S10]]。田口将品质定义为「产品给社会带来的平均损失」，其损失函数一般形式为[[S13]]：

\[
EL = E(Y - m)^2 = \sigma^2 + \delta^2
\]

其中 \(\sigma^2\) 为品质特性方差、\(\delta^2\) 为均值对目标值的偏差平方。信噪比最大化的优化目标，在数学上等价于直接降低品质的平均社会损失[[S13]]。望目特性 S/N 公式的分子 \(\mu^2\) 与分母 \(\sigma^2\) 的比值构造，正是为了同时控制偏差与波动两个品质维度[[S16]]。

## 局限性

田口信噪比在压铸工艺优化中存在以下适用边界[[S20,S3,S6]]：

**非正态分布数据的适用性受限。** 经典望小/望大特性的信噪比公式默认观测数据服从正态分布。若采集的缩孔、气孔等样本数据呈现显著的偏态或非正态分布特征，直接套用 S/N 公式会产生偏差，需先进行数据转换再分析[[S20,S3]]。

**单指标优化无法直接支撑多目标决策。** 单指标 S/N 分析仅能针对一个品质特性寻找最优参数组合。在实际压铸工艺中，往往需要同时兼顾多个品质指标（如缩孔体积与热裂倾向、翘曲量与体积收缩率等）。直接对各个指标独立做 S/N 优化可能导致某一指标最优而其余指标劣化的问题。此时需引入灰色关联分析、权重分配、多目标寻优算法（如 NSGA-II）与多目标决策方法（如 TOPSIS）等协同工具完成多品质指标的权衡优化[[S6,S3]]。

## 与其他概念的关系

- **望目特性与过程能力指数（Cp/Cpk）**：二者均关注品质特性对目标值的贴近程度与波动控制，但 Cpk 关注的是工艺是否符合规格限要求，望目 S/N 则无规格限概念，仅以最小化偏差与波动为优化导向[[S16,S13]]。
- **望小/望大特性与工序能力**：在铸件缺陷控制场景中，望小 S/N 的极大化意味着缺陷均值的降低与一致性的提升，是工序能力改善的前置统计手段[[S19,S5]]。
- **与品质损失函数的区别**：品质损失函数给出的是社会损失的绝对金额估算（需要损失系数 \(k\)），信噪比则是无量纲的相对稳健性指标，二者目标一致但量纲和处理层次不同[[S13,S10,S17]]。

## Sources
- S16: [先进材料及特种液态成型上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f661f0d-994d-452d-8a00-8247d6eb0e51/resource) (`9f661f0d-994d-452d-8a00-8247d6eb0e51`)
- S22: [基于Moldex3D的高精度空心杯电机电枢注塑封装工艺仿真优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4d70698-cf6c-47f4-a760-152581063b39/resource) (`f4d70698-cf6c-47f4-a760-152581063b39`)
- S14: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9842d88f-1e56-4131-a678-4bba6d8f2a19/resource) (`9842d88f-1e56-4131-a678-4bba6d8f2a19`)
- S15: [柴油机铝合金缸体铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c288d1e-b459-4cd4-a301-de08f7ad8ddd/resource) (`9c288d1e-b459-4cd4-a301-de08f7ad8ddd`)
- S19: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df10eae4-4564-4085-9c5e-9353daf3aa5d/resource) (`df10eae4-4564-4085-9c5e-9353daf3aa5d`)
- S6: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45a3bda5-8ec9-4a9e-ab25-236bbab3f60e/resource) (`45a3bda5-8ec9-4a9e-ab25-236bbab3f60e`)
- S24: [die casting parameter sizing for az91d in notebook computer base shell__8dc4af6999](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5453ba1-91a8-44ae-b2aa-9e8695b1eb09/resource) (`f5453ba1-91a8-44ae-b2aa-9e8695b1eb09`)
- S4: [基于ProCAST的汽车铝合金机油泵体压铸模具开发及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13231e18-b050-4499-9a57-669f065e76b4/resource) (`13231e18-b050-4499-9a57-669f065e76b4`)
- S21: [基于ProCAST的汽车铝合金机油泵体压铸模具开发及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f47e64f2-55f8-42e8-b524-8063ba44bee0/resource) (`f47e64f2-55f8-42e8-b524-8063ba44bee0`)
- S12: [图4.5 质量特性选择图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8b225e9c-21a5-461a-8616-6d809d5ec65c/resource) (`8b225e9c-21a5-461a-8616-6d809d5ec65c`)
- S25: [analysis of hardness by parametric optimization of gravity die casting f__95d0cf5a04](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f84cc476-4945-4460-a1c8-195419347a60/resource) (`f84cc476-4945-4460-a1c8-195419347a60`)
- S5: [汽车机油泵体压铸工艺数值模拟与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/211f26c5-f889-45eb-8b83-2fd022d344e1/resource) (`211f26c5-f889-45eb-8b83-2fd022d344e1`)
- S2: [水龙头铸件的缩孔缺陷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0543596b-b9ed-4aa3-a071-f8a890dd494c/resource) (`0543596b-b9ed-4aa3-a071-f8a890dd494c`)
- S9: [die casting process optimization using taguchi methods__eca7652172](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c62dcfe-e025-41bf-99e6-8025833afecc/resource) (`5c62dcfe-e025-41bf-99e6-8025833afecc`)
- S7: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49be0918-b6bf-42ea-90c9-d381d796610b/resource) (`49be0918-b6bf-42ea-90c9-d381d796610b`)
- S1: [图 4.4 Minitab 图形选项界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/050d5aae-352a-456d-aa94-0e7ebf4fd550/resource) (`050d5aae-352a-456d-aa94-0e7ebf4fd550`)
- S8: [表4.21 田口法缩孔缩松体积信噪比均值(dB)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/534ae140-8ae7-4431-813d-ee3666c7775c/resource) (`534ae140-8ae7-4431-813d-ee3666c7775c`)
- S18: [表5.7 信噪比结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c21f42dc-2a31-4824-9636-8f47c535204a/resource) (`c21f42dc-2a31-4824-9636-8f47c535204a`)
- S11: [a study of porosity formation in pressure die casting using the taguchi__4ac320727f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d3bbeed-e97d-416b-a539-618881dd53f6/resource) (`6d3bbeed-e97d-416b-a539-618881dd53f6`)
- S13: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/902a8a7c-d07a-42c8-a236-8ff01d4946d1/resource) (`902a8a7c-d07a-42c8-a236-8ff01d4946d1`)
- S17: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba1d44d7-e86c-4ba1-ab52-d11cfd33f34c/resource) (`ba1d44d7-e86c-4ba1-ab52-d11cfd33f34c`)
- S10: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/609cca27-36da-43b5-b29d-3ce0776b6133/resource) (`609cca27-36da-43b5-b29d-3ce0776b6133`)
- S20: [可控因子分类表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8d8cc6d-f3df-4ae0-9cb2-a7ac16e170af/resource) (`e8d8cc6d-f3df-4ae0-9cb2-a7ac16e170af`)
- S3: [高密度模块封装模流仿真技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c30fd41-96bf-47ba-9fd6-63814bea23ae/resource) (`0c30fd41-96bf-47ba-9fd6-63814bea23ae`)