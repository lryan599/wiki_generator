---
version: "v1"
generated_at: "2026-06-18T14:36:47+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 24
  source_quality_score: 0.84
  freshness_score: 0.91
  evidence_coverage_score: 1.0
---

## 概述

均方根误差（Root Mean Square Error，RMSE），亦称均方根误差，是统计回归模型中最常用的基础评估指标之一，用于量化回归模型整体预测精度 [[S17,S3,S9]]。RMSE由均方误差（MSE）开平方得来，取值与原始实测数据处于同一量纲，在压铸领域的工艺参数预测、力学性能预测、缺陷检测等机器学习模型评估中被普遍采用 [[S18,S5,S11,S9]]。

## 定义

在回归预测任务中，设真实观测值序列为 $y_i$，对应模型预测值序列为 $\hat{y}_i$，参与计算的样本总数为 $n$，则**样本均方根误差**的标准数学表达式为 [[S3,S16,S18,S28]]：

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

简而言之，RMSE即均方误差（MSE）的算术平方根：
$$RMSE = \sqrt{MSE}$$

在统计推断场景中，总体的均方根误差公式分母采用总体观测值总数 $N$；用于无偏估计总体标准差的样本标准差公式则为 $s = \sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}$，分母为 $n-1$，与常规样本RMSE的自由度处理存在差异，二者在统计目的和适用场景上需加以区分 [[S15,S30,S6]]。

## 类别归属与核心判据

RMSE属于回归模型误差评价指标范畴，是监督学习回归任务中最为通用的性能度量之一 [[S17,S3,S9]]。其核心判据如下：

- **取值范围**：$[0, +\infty)$，数值越小表示模型预测精度越高，越小越优 [[S13,S8,S28]]。
- **量纲特性**：与原始数据保持一致，可直接对应物理场景下的预测偏差量级，例如压铸温度场预测的RMSE以℃为单位，孔隙体积预测的RMSE以cc为单位 [[S18,S12,S9,S11]]。
- **对异常值的敏感度**：因继承MSE的平方计算特性，对大误差赋予更高权重，相较平均绝对误差（MAE）对离群值更为敏感 [[S2,S18,S3]]。

## 计算步骤

RMSE的标准计算步骤如下 [[S3,S2,S16]]：

1. 获取所有待评估样本的真实值序列 $y_i$ 和预测值序列 $\hat{y}_i$，确认二者长度一致；
2. 逐样本计算差值 $y_i - \hat{y}_i$，并对差值求平方，得到平方误差序列；
3. 对所有平方误差求和后除以样本总数 $n$，得到均方误差 $MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$；
4. 对MSE取非负算术平方根，得到最终结果 $RMSE = \sqrt{MSE}$。

## 与MSE、MAE、R²的对比

下表归纳了回归问题四个核心评价指标的差异 [[S18,S3,S16,S14]]：

| 指标 | 计算公式 | 量纲 | 异常值敏感度 | 取值范围 | 适用场景 |
|------|---------|------|------------|--------|--------|
| MSE | $\frac{1}{n}\sum(y_i - \hat{y}_i)^2$ | 原始量纲的平方 | 高 | $[0,+\infty)$ | 需要压制大误差的任务 |
| RMSE | $\sqrt{\frac{1}{n}\sum(y_i - \hat{y}_i)^2}$ | 与原始数据同量纲 | 高 | $[0,+\infty)$ | 连续数据预测精度直观评估 |
| MAE | $\frac{1}{n}\sum|y_i - \hat{y}_i|$ | 与原始数据同量纲 | 低 | $[0,+\infty)$ | 直接反映预测与真实值的平均偏差 |
| R² | $1 - \frac{\sum(y_i-\hat{y}_i)^2}{\sum(y_i-\bar{y})^2}$ | 无量纲比值 | — | $[0,1]$ | 评估模型对因变量方差的解释比例 |

## 在压铸领域的具体应用

压铸领域目前虽无公开行业标准强制规定RMSE的使用要求，但所有已公开发表的压铸回归预测学术研究均将RMSE作为核心模型精度评价指标之一，已形成广泛的行业使用共识 [[S5,S11,S9]]。

### 工艺参数预测

针对AL365铝合金压铸咖啡机顶盖的模具热疲劳应力预测任务，采用量子粒子群算法改进的Kriging（QPSO-Kriging）模型相比原始Kriging模型，RMSE降低了82.3207%，预测残差区间由[-2,10]显著缩小至[-2,1] [[S7]]。

在铝合金轮毂低压压铸凝固时间预测中，基于贝叶斯优化的XGBoost（BO-XGBoost）模型相较基础XGBoost模型在RMSE指标上表现更优，内推与外推场景下预测可靠性更高 [[S5,S26]]。

### 铸件力学性能预测

基于发动机缸体高压压铸生产数据，采用人工神经网络（ANN）建立的铸件极限抗拉强度（UTS）预测模型，在所有对比模型中RMSE值最低，优于随机森林、支持向量机以及XGBoost模型 [[S29]]。

### 孔隙率与缺陷预测

在压力铸造气孔体积与缩孔缩松体积预测中，BP神经网络的预测RMSE值显著优于RBF神经网络。其中BP模型对气孔体积预测的RMSE仅为0.088cc，远低于RBF模型的对应指标，且两类模型的预测相对误差均低于5%，可满足压铸工程允许的误差范围 [[S11,S24,S22]]。

### 尺寸精度预测

针对铝合金低压压铸充型率预测，BP神经网络的RMSE值低于RBF神经网络，二者相对误差分别为0.75%与2.14%，均可满足充型尺寸预测的工程精度要求 [[S11]]。

### 模具温度场预测

在铝车轮压铸模具温度场预测任务中，RMSE被选为与MSE、MAE、R²并列的核心评价指标，用于对比LSTM模型与LightGBM模型的连续数据预测精度。RMSE在此场景下单位与实测温度保持一致，可直接反映预测温度与真实温度的偏离幅度 [[S9]]。

![不同检测点数量下三种压铸模具温度场预测模型的RMSE对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1507082a-1fac-4348-887a-65543674ef34/resource)  
图：LR、SVR和DNN模型在不同检测点数量下的温度场重构RMSE（单位：℃），DNN模型RMSE整体更低且随检测点增多进一步降低 [[S4]]。

## 局限性

1. **对异常值极为敏感**：RMSE对预测误差取平方以放大大误差权重。在压铸数据集中，若存在少量离群异常检测点数据，会导致RMSE数值显著拉高，掩盖大部分样本的真实预测精度水平 [[S18]]。

2. **量纲依赖，无法跨任务直接比较**：RMSE的单位与被预测物理量完全一致且无归一化处理，无法在不同量纲的预测任务间横向对比优劣。例如，不能直接比较抗拉强度预测的RMSE（单位MPa）与孔隙体积预测的RMSE（单位cc）的大小 [[S18]]。

3. **不能直接反映相对误差**：RMSE仅表示绝对误差的统计平均，无法体现误差相对于实测值的比例。例如，某铝合金铸件抗拉强度实测值为320MPa、预测偏差8MPa，与另一小尺寸铸件实测值80MPa、偏差同样为8MPa的情景相比，二者绝对误差相同而相对误差相差4倍，单凭RMSE数值无法对此加以区分 [[S1]]。

![SIR粒子滤波器均方根误差随粒子数量变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0b8b82f-1f7a-4972-8e9e-60aead840c0a/resource)  
图：SIR粒子滤波器的RMSE随粒子数量增加（0至500）显著下降，粒子数量超过100后趋于稳定——该曲线可用于类比理解RMSE随模型参数或样本容量变化的收敛行为 [[S20]]。

## Sources
- S17: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c049691-10fd-4c6c-80de-14b2d0d74dbf/resource) (`9c049691-10fd-4c6c-80de-14b2d0d74dbf`)
- S3: [锻造时压力机应变场与模具温度场的数字重构研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03c45709-9489-4d34-ad3a-86ce4dc38ae0/resource) (`03c45709-9489-4d34-ad3a-86ce4dc38ae0`)
- S9: [基于机器学习的铝车轮压铸模具温度场预测方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e35315c-8af5-4be5-ba8f-2f3f731509a9/resource) (`3e35315c-8af5-4be5-ba8f-2f3f731509a9`)
- S18: [铝合金压铸工艺参数不确定性对铸件静强度性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1c59ed2-1005-4b7c-8336-621b0f1dbd85/resource) (`a1c59ed2-1005-4b7c-8336-621b0f1dbd85`)
- S5: [数据驱动的铸件凝固时间代理预测模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22825d58-f6e9-44e7-9ff3-8a982c3e072c/resource) (`22825d58-f6e9-44e7-9ff3-8a982c3e072c`)
- S11: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53fd911b-f391-4c08-b585-c56ccc269668/resource) (`53fd911b-f391-4c08-b585-c56ccc269668`)
- S16: [融合岩性信息的CNN-LSTM-GAT深度网络孔隙压力预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60/resource) (`95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60`)
- S28: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4ca1b6d-1239-415c-8c8c-d7a3d4fca6f2/resource) (`e4ca1b6d-1239-415c-8c8c-d7a3d4fca6f2`)
- S15: [表7.6-1 样本和总体之间的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8fa6518b-bd08-4946-bab1-d21c80cc7082/resource) (`8fa6518b-bd08-4946-bab1-d21c80cc7082`)
- S30: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f45f9470-629d-4c11-a807-a2110958c989/resource) (`f45f9470-629d-4c11-a807-a2110958c989`)
- S6: [材料加工过程控制技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24ab135d-19ad-4357-94d9-1fba85dab082/resource) (`24ab135d-19ad-4357-94d9-1fba85dab082`)
- S13: [压力铸造成型工艺参数优化数学模型研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68adbd40-9f10-46f2-8f88-6b924a7dd869/resource) (`68adbd40-9f10-46f2-8f88-6b924a7dd869`)
- S8: [不锈钢Y型三通管熔模铸造浇注方案设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39aa64a7-ce1a-482a-8d52-5bb6d40c41f8/resource) (`39aa64a7-ce1a-482a-8d52-5bb6d40c41f8`)
- S12: [数据驱动的铸件凝固时间代理预测模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55da5547-6a70-405d-8d21-69a859178f12/resource) (`55da5547-6a70-405d-8d21-69a859178f12`)
- S2: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03b7028f-505d-42e2-afae-143562132b19/resource) (`03b7028f-505d-42e2-afae-143562132b19`)
- S14: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d8076ce-1394-4f6d-bf23-31e938c348cf/resource) (`8d8076ce-1394-4f6d-bf23-31e938c348cf`)
- S7: [压力铸造成型工艺参数优化数学模型研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/294efda0-d5e7-4b4a-a055-6a3103c104f1/resource) (`294efda0-d5e7-4b4a-a055-6a3103c104f1`)
- S26: [数据驱动的铸件凝固时间代理预测模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2c2e21f-07f8-474d-9091-4020d829938a/resource) (`e2c2e21f-07f8-474d-9091-4020d829938a`)
- S29: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1efdcdf-dae8-4b97-a943-8b66fe85d23d/resource) (`f1efdcdf-dae8-4b97-a943-8b66fe85d23d`)
- S24: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0c69004-dc73-4af2-9887-15599bf01d0d/resource) (`e0c69004-dc73-4af2-9887-15599bf01d0d`)
- S22: [表3-2 压力铸造训练集数据的预测缺陷数值对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc65ebcf-0a99-4c22-8a65-3ef407dad10e/resource) (`cc65ebcf-0a99-4c22-8a65-3ef407dad10e`)
- S4: [表4-9 LR、SVR和DNN模型在不同检测点数量下的RMSE(°C)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1507082a-1fac-4348-887a-65543674ef34/resource) (`1507082a-1fac-4348-887a-65543674ef34`)
- S1: [移动热源作用下熔铸装药顺序凝固温度场快速预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01fa6d42-a1da-44d6-872c-e2b2b28c3b10/resource) (`01fa6d42-a1da-44d6-872c-e2b2b28c3b10`)
- S20: [图14.8 SIR粒子滤波器的均方误差平方根（RMSE）随粒子数量的变化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0b8b82f-1f7a-4972-8e9e-60aead840c0a/resource) (`c0b8b82f-1f7a-4972-8e9e-60aead840c0a`)