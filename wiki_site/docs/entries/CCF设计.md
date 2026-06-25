---
version: "v1"
generated_at: "2026-06-18T18:56:54+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 16
  source_quality_score: 0.86
  freshness_score: 0.89
  evidence_coverage_score: 1.0
---

## 概述

面心中心复合设计（Face-centered central composite design，简称 CCF）是中心复合设计（Central Composite Design, CCD）中的一个重要子类，属于响应曲面法（Response Surface Methodology, RSM）框架下专门用于拟合二阶响应模型的实验设计类型。其最显著的结构特征在于：轴向点（星点）直接布置在因子立方体的各个面的中心位置上，轴向距离 α 固定取值为 1[[S1,S10]]。CCF 设计中，所有试验点均完全落在预设的因子立方体可行域内，所有因子仅设置三个水平（低、中、高），无需将轴向点设置在因子范围之外[[S1,S7]]。

## 核心构造与点集组成

CCF 设计的点集由三类试验点组合而成[[S1,S10]]：

-   **角点（Cube / Factorial points）**：2<sup>k</sup> 个全因子角点，布置在因子立方体的所有顶点处，用于估计线性项和交互项[[S2]]；
-   **轴向点（Star / Axial points）**：2k 个面心轴向点，布置在各因子立方体表面的中心，轴向距离 α = 1，用于估计纯二次项[[S1,S2]]；
-   **中心点（Center points）**：1 组重复采样的中心点，通常要求重复 3~5 次，用于估计实验纯误差[[S1,S10]]。

对于 k = 3 个因子的 CCF 设计，总试验次数通常为 15 次，具体包括 8 个全因子角点、6 个面心轴向点以及 1 个中心点，再搭配多次重复的中心点采样[[S6,S1]]。

## 与其他中心复合设计的对比

中心复合设计的不同子类主要由轴向点距设计中心的距离（α）来定义。下表对比了 CCF 与另外两种常见变体——外接中心复合设计（CCC）和内接中心复合设计（CCI）的核心差异[[S1,S10]]：

| 设计类型 | 轴向点位置 | 轴向距离 (α) | 旋转性 | 因子水平数 | 设计空间利用 | 主要优缺点 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CCF** (面心) | 立方体表面 | α = 1 | 不具备 | 3 | 所有点落在可行域内，无需调整因子上下限 | 工程落地难度低，但预测方差在边缘增大[[S3,S4]] |
| **CCC** (外接) | 立方体外 | α > 1 (常取 √k) | 具备 | 5（扩展点超范围） | 轴向点超出初始范围，可能无法在安全区运行 | 预测精度均匀，但要求工艺窗口更宽[[S1,S4]] |
| **CCI** (内接) | 立方体内 | 1/α | 不具备 | 3 | 因子点缩入设计空间内部 | 相比 CCF，预测精度在边界处可能更低[[S1,S10]] |

## 二阶模型与统计分析

利用 CCF 设计所采集的实验数据，通常拟合一个完整的二阶多项式响应曲面模型。该模型的通用表达式为[[S16,S5,S17]]：

$$
y = \beta_0 + \sum \beta_i x_i + \sum \beta_{ij} x_i x_j + \sum \beta_{ii} x_i^2 + \varepsilon
$$

其中，β<sub>0</sub> 为常数项，β<sub>i</sub> 为线性项系数，β<sub>ij</sub> 为交互项系数，β<sub>ii</sub> 为二次项系数，ε 为随机误差项。

模型构建后，需通过方差分析（ANOVA）检验各项的回归显著性，并以 *P* 值判断统计显著性（通常不显著项 *P* > 0.05 予以剔除），以决定系数 *R*<sup>2</sup> 衡量模型对数据变异的解释程度，从而简化并优化模型结构[[S16,S2]]。

## 在压铸工艺优化中的应用

在高压铸造（HPDC）工艺优化领域，CCF 设计被用于构建关键工艺参数与铸件质量特性之间的非线性输入-输出关系[[S9]]。

-   **输入工艺因子**：典型的 CCF 设计可选取四类核心压铸参数，如快压射速度、慢压射向快压射切换点、增压压力以及保压时间[[S9,S8]]。
-   **质量响应指标**：对应的质量响应可包括铸件孔隙率、布氏硬度以及表面粗糙度[[S9]]。
-   **实验执行**：在一项针对 4 个因子的研究中，标准执行流程包含 31 组设计组合，每组进行 3 次重复实验，并额外设置 12 组随机参数组合作为测试样本[[S9,S14]]。通过非线性回归拟合建立模型，并利用测试样本验证，结果显示模型预测值与实际实验值的偏差处于合理区间，可在无额外物理试验的条件下有效预测不同工艺组合下的铸件质量[[S14]]。
-   **现场操作性优势**：由于 CCF 设计的所有因子水平均落在常规压铸工艺的安全操作区间内，无需设置超出生产允许边界的极端参数，这显著降低了压铸车间现场试验的执行难度[[S7]]。

## 局限性与注意事项

CCF 设计的固有局限主要源于其牺牲了旋转性[[S3,S13]]：

-   **不具旋转性**：预测方差不能保持恒定，会随预测点距设计中心距离的变化而改变，导致在因子空间边缘处的预测误差通常高于同等条件下具备旋转性的 CCC 设计[[S3]]。
-   **边界预测精度与模型外推能力有限**：在压铸实践中，由于所有实验点均未超出预设的三水平边界，无法像扩展型 CCD 设计那样通过外推获得工艺窗口极限位置的补充数据。当需要高精度描述工艺窗口边界附近的非线性质量变化规律时，CCF 设计在边界区域的采样点覆盖密度可能不足，导致该区域的模型预测精度有所降低[[S1]]。因此，CCF 模型的外推预测能力有限，不应在需要精确预测极端值（如设计空间角落处）时作为首选[[S7]]。

## 设计点空间分布图示

下图为三因子面心中心复合设计（CCF）的实验点空间分布示意图，清晰展示了位于设计空间中心的中心点、立方体各顶点的因子点以及位于立方体六个表面中心处的星点（轴向点）[[S15,S12]]。

![三因子面心中心复合设计(CCF)实验点空间分布示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d067bd4c-c71b-4e04-8931-33ee6778752f/resource)

## Sources
- S1: [advanced aerospace materials aluminum based and composite structures__94b4d473f2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/004ded91-0fe4-4752-a5d4-ba1e613178d9/resource) (`004ded91-0fe4-4752-a5d4-ba1e613178d9`)
- S10: [advanced aerospace materials aluminum based structures composite structures__1191e65ddf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e977b8a-1f97-45c3-a7e2-f53412d36c9f/resource) (`6e977b8a-1f97-45c3-a7e2-f53412d36c9f`)
- S7: [advanced aerospace materials aluminum based structures composite structures__1191e65ddf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b10d674-b5e5-4ad0-a7c5-b3fd70d9a9f2/resource) (`4b10d674-b5e5-4ad0-a7c5-b3fd70d9a9f2`)
- S2: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f055816-e5b4-420a-9f54-2401da7346c3/resource) (`0f055816-e5b4-420a-9f54-2401da7346c3`)
- S6: [三变量试验组合设计的试验点分布（表7.6）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4398069e-ce19-4cf0-bbb3-18b8e4326ca0/resource) (`4398069e-ce19-4cf0-bbb3-18b8e4326ca0`)
- S3: [an experimental design criterion for minimizing meta model prediction er__269452c1e6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23e047c5-5407-4062-b56c-fcbadcb0e941/resource) (`23e047c5-5407-4062-b56c-fcbadcb0e941`)
- S4: [变模温注塑成型温度场模拟及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/299c7b71-e5b3-42e2-88cb-44a03d24f012/resource) (`299c7b71-e5b3-42e2-88cb-44a03d24f012`)
- S16: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5e458d6-8a44-4649-885f-1b7c24861ddb/resource) (`f5e458d6-8a44-4649-885f-1b7c24861ddb`)
- S5: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3cbc1e2c-0b85-430a-a48a-07aaa7d115d5/resource) (`3cbc1e2c-0b85-430a-a48a-07aaa7d115d5`)
- S17: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd5332bb-3196-4308-b0fc-c8741c08f17f/resource) (`fd5332bb-3196-4308-b0fc-c8741c08f17f`)
- S9: [aip conference proceedings aip international conference on modeling opti__9dbb7b9ee0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6967b44c-57c8-4b2c-8958-41da01f91c35/resource) (`6967b44c-57c8-4b2c-8958-41da01f91c35`)
- S8: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fcb21d2-f06b-418a-9b80-4c7fcd4123cb/resource) (`5fcb21d2-f06b-418a-9b80-4c7fcd4123cb`)
- S14: [aip conference proceedings aip international conference on modeling opti__9dbb7b9ee0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4610021-883b-4c15-8cd9-d7b33544b437/resource) (`c4610021-883b-4c15-8cd9-d7b33544b437`)
- S13: [an experimental design criterion for minimizing meta model prediction er__16f4bc299a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0d3fd60-289b-47c0-9f56-6b51437517f4/resource) (`c0d3fd60-289b-47c0-9f56-6b51437517f4`)
- S15: [Central composite design](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d067bd4c-c71b-4e04-8931-33ee6778752f/resource) (`d067bd4c-c71b-4e04-8931-33ee6778752f`)
- S12: [Central composite design](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a04c5d19-7d2b-40b7-a82a-915fcab09e87/resource) (`a04c5d19-7d2b-40b7-a82a-915fcab09e87`)