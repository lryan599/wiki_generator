---
version: "v1"
generated_at: "2026-06-18T12:42:24+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 15
  source_quality_score: 0.84
  freshness_score: 0.87
  evidence_coverage_score: 1.0
---

## 平均绝对误差（MAE）

### 概述
平均绝对误差（Mean Absolute Error，MAE）是回归类任务中广泛使用的预测精度度量指标，用于量化模型预测值与真实观测值之间的平均偏差幅度。其基本定义为所有样本的预测偏差绝对值之和的算术平均值，结果越小表明模型的预测效果越好[[S1]][[S5]][[S10]][[S6]]。在材料加工与铸造（含压铸）领域，MAE 已成为工艺参数预测、温度场重构及缺陷预报等机器学习建模中的标准评价指标之一[[S4]][[S12]]。

### 数学定义
MAE 的标准数学表达式为：
$$
\mathrm{MAE} = \frac{1}{n} \sum_{i=1}^{n} \left| y_i - \hat{y}_i \right|
$$
其中，\(n\) 为样本总数，\(y_i\) 为第 \(i\) 个样本的真实测量值，\(\hat{y}_i\) 为对应的模型预测值[[S1]][[S5]][[S10]]。在压铸文献中，常采用等价形式 \(\mathrm{MAE} = \frac{1}{n} \sum_{i=1}^{n} |Y_i - \hat{Y}_i|\)[[S4]][[S12]]。

### 主要属性
1. **量纲一致性**  
   MAE 的量纲与原始观测变量完全一致，无需额外转换即可直接解读为实际物理量的平均偏离水平，避免了平方或开方运算引入的单位失真问题[[S12]][[S6]]。

2. **对异常值的鲁棒性**  
   与均方误差（MSE）不同，MAE 对所有偏差采用线性等权平均，对极端偏离的异常样本不敏感。MSE 通过平方运算会对大偏差施加二次放大的影响，而 MAE 的线性权重使其在数据存在离群值时具有显著更强的稳健性[[S3]]。

3. **高可解释性**  
   MAE 输出数值直接表示预测值相对于真实值的平均偏移幅度，解读门槛极低，适用于工业场景下向非技术人员公示预测精度[[S11]][[S6]]。

### 与其他误差指标的关系与对比
在回归模型评价中，MAE 常与 MSE、RMSE、MAPE 等指标配合使用。下表汇总了各指标的计算公式与主要特性[[S10]][[S6]][[S12]]。

| 指标 | 公式 | 量纲 | 核心特性 | 适用场景 |
|------|------|------|----------|----------|
| 平均绝对误差 (MAE) | \(\frac{1}{n}\sum \|y_i - \hat{y}_i\|\) | 同原始变量 | 对异常值鲁棒，可解释性强；在零误差点不可导 | 对极端异常值不敏感的工程预测任务，需直观解读平均误差的工业评估 |
| 均方误差 (MSE) | \(\frac{1}{n}\sum (y_i - \hat{y}_i)^2\) | 原始变量平方 | 数学可导性好，适合梯度优化；对离群点极敏感 | 需重点抑制大偏差的回归任务，深度学习梯度训练 |
| 均方根误差 (RMSE) | \(\sqrt{\frac{1}{n}\sum (y_i - \hat{y}_i)^2}\) | 同原始变量 | 兼顾大偏差惩罚与量纲一致性；仍对异常值较敏感 | 跨数据集预测精度横向对比，量化整体偏离严重程度 |
| 平均绝对百分比误差 (MAPE) | \(\frac{100\%}{n}\sum \|\frac{y_i - \hat{y}_i}{y_i}\|\) | 无量纲（百分比） | 消除量级和单位影响；真实值趋零时无定义 | 不同量级预测结果的相对误差对比，百分比精度要求明确的场景 |

MAE 的优势在于对异常值的稳健性和直接的可读性，而劣势是其在零误差处的不可导特性限制了梯度优化中的稳定性[[S10]][[S6]]。在铸造与材料领域的实际研究中，常同时报告 MAE、MSE、RMSE 与决定系数 \(R^2\)，以从不同侧面评价模型性能[[S4]][[S12]]。

### 压铸领域中的应用场景
MAE 在压铸相关预测建模中获得了多方面的应用：

- **模具温度场预测**  
  在基于机器学习的铝车轮低压铸造模具温度场预测研究中，MAE 被作为四项核心评价指标之一（与 MSE、RMSE、\(R^2\) 并列），用于衡量模型预测温度与实际采集温度的偏差[[S4]][[S12]]。

- **铸件缺陷预测**  
  在压力铸造工艺仿真中，通过 BP 和 RBF 神经网络预测充型率、气孔体积、缩孔缩松体积，分别给出训练集和测试集的 MAE 与 RMSE 值，结果表明 BP 模型的 MAE 整体小于 RBF 模型，验证了 MAE 在缺陷预测模型筛选中的有效性[[S13]][[S17]]。

- **工艺参数与力学性能预测**  
  调压铸造工艺的代理模型中，使用 MAE 与 \(R^2\) 评估不同数据集下的预测精度，如训练集 MAE=0.195 MPa、测试集 MAE=4.7021 MPa，直观反映模型泛化能力[[S7]][[S18]]。在铝合金压铸工艺参数不确定性对静强度性能影响的研究中，通过对比内推与外推方案下的 MAE、MSE、RMSE 等指标，为模型适用性提供了多角度判据[[S9]][[S15]]。

### 局限性
尽管 MAE 具有良好的鲁棒性和可解释性，其梯度优化存在固有困难：当预测值恰好等于真实值（即绝对误差为零）时，损失函数在该点不可导，无法直接获得有效梯度。工程实践中通常约定此点的导数为零，使参数停止更新，以此规避迭代异常[[S8]]。此外，在压铸数据可能呈现偏态分布或包含强离群值的情况下，虽然 MAE 较 MSE 更为稳健，但仍需配合其他指标（如 RMSE、\(R^2\)）进行综合判断，以避免单一指标对误差结构反映的片面性[[S4]][[S12]]。

### 图示案例
图 1 为铝合金压铸工艺研究中不同预测方案（内推与外推）下的四项评价指标对比柱状图，其中包含 MAE。该图直观展示了 MAE 与 MSE、RMSE 在同一试验条件下的数值差异，有助于理解在压铸建模中采用多指标联合评估的必要性[[S9]]。

![图1 铝合金压铸预测模型内推与外推方案的误差指标对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90cebbe1-fae5-4de9-b3ac-cf89424198d7/resource)

## Sources
- S1: [材料加工过程控制技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24ab135d-19ad-4357-94d9-1fba85dab082/resource) (`24ab135d-19ad-4357-94d9-1fba85dab082`)
- S5: [移动热源作用下熔铸装药顺序凝固温度场快速预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5798ae9c-0a2a-4996-ac54-9943435dcbf6/resource) (`5798ae9c-0a2a-4996-ac54-9943435dcbf6`)
- S10: [融合岩性信息的CNN-LSTM-GAT深度网络孔隙压力预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60/resource) (`95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60`)
- S6: [城市道路混合交通流分析模型与方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/634b9f49-eca6-4061-a3cb-9698d3d24403/resource) (`634b9f49-eca6-4061-a3cb-9698d3d24403`)
- S4: [TextNode25](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e35315c-8af5-4be5-ba8f-2f3f731509a9/resource) (`3e35315c-8af5-4be5-ba8f-2f3f731509a9`)
- S12: [TextNode24](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7adb42a-3943-4d85-95a0-657df6faf826/resource) (`a7adb42a-3943-4d85-95a0-657df6faf826`)
- S3: [人工智能计算agent基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b57b448-39af-4ba2-ae8a-4506fe28b694/resource) (`2b57b448-39af-4ba2-ae8a-4506fe28b694`)
- S11: [预测结果分析的误差指标](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a53d0ade-5d5f-42ca-aa53-d60310a02cab/resource) (`a53d0ade-5d5f-42ca-aa53-d60310a02cab`)
- S13: [表3-2 压力铸造训练集数据的预测缺陷数值对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc65ebcf-0a99-4c22-8a65-3ef407dad10e/resource) (`cc65ebcf-0a99-4c22-8a65-3ef407dad10e`)
- S17: [表3-4 压力铸造测试集数据的预测缺陷数值对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd8183aa-4ec2-4d89-bd20-7a8d71b3a8a8/resource) (`fd8183aa-4ec2-4d89-bd20-7a8d71b3a8a8`)
- S7: [代理模型预测值与真实值的散点对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bc4ce11-1f36-462b-aede-964a1f9b6a5d/resource) (`6bc4ce11-1f36-462b-aede-964a1f9b6a5d`)
- S18: [Fig.5-8(c) 初始EL预测模型的训练集与测试集性能对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ffba9f03-56b8-472c-a4b6-3d4bc0cc3e54/resource) (`ffba9f03-56b8-472c-a4b6-3d4bc0cc3e54`)
- S9: [图3-10 不同方案中的预测评价指标](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90cebbe1-fae5-4de9-b3ac-cf89424198d7/resource) (`90cebbe1-fae5-4de9-b3ac-cf89424198d7`)
- S15: [图15 不同方案中的预测评价指标](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9379a7e-2c5d-4281-bf4d-02c95b916ca6/resource) (`d9379a7e-2c5d-4281-bf4d-02c95b916ca6`)
- S8: [人工智能计算agent基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72639fd0-80df-42a0-87f0-ea41bbaa4953/resource) (`72639fd0-80df-42a0-87f0-ea41bbaa4953`)