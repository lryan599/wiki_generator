---
version: "v1"
generated_at: "2026-06-18T19:12:50+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 19
  source_quality_score: 0.82
  freshness_score: 0.92
  evidence_coverage_score: 1.0
---

## 定义与公式

准确率（Accuracy, 缩写为 A）是监督学习分类模型的核心性能指标之一，用于衡量模型对所有测试样本的整体分类正确程度。其定义为“预测正确的样本数占全部测试样本总数的比例”，标准的数学表达式为

\[
A = \frac{TP + TN}{TP + TN + FP + FN}
\]

其中：
- \(TP\)（真阳性）：真实为正类且被模型预测为正类的样本数；
- \(TN\)（真阴性）：真实为负类且被模型预测为负类的样本数；
- \(FP\)（假阳性）：真实为负类但被模型预测为正类的样本数；
- \(FN\)（假阴性）：真实为正类但被模型预测为负类的样本数。

分母 \(TP+TN+FP+FN\) 即为参与评估的全部样本数，准确率取值在 0~1 之间（或 0%~100%），数值越高代表模型整体分类能力越强 [[S17,S2,S10,S20]]。

在压铸缺陷预测的具体工程文献中，该指标也常被等价地写成

\[
\text{准确率} = \frac{N_{\text{true}}}{N_{\text{total}}}
\]

其中 \(N_{\text{true}}\) 为预测正确的样本数，\(N_{\text{total}}\) 为所有参与统计的测试样本数 [[S20]]。

## 别名与英文术语

- **英文术语**：Accuracy，国际通用。在机器学习领域的主流开源工具（如 scikit‑learn）中，该指标已被标准化实现为 `accuracy_score` [[S19]]。
- **中文别名**：“正确率”“总体准确率”以及“A 正确”等在工业数据异常检测和铸造/材料相关的算法评估文献中均有使用。其中“正确率”在质量评价场景中常与“准确率”互换；“A 正确”多出现在以字母 A 作为指标代称的铸造、挤压铸造等领域文献中 [[S12,S2]]。
- **缩写**：行业惯例以单字母 **A** 作为标准缩写，并与 **P**（精确率）、**R**（召回率）并列作为分类模型的核心评价指标 [[S17]]。

## 混淆矩阵与可视化

准确率是从混淆矩阵（Confusion matrix）直接派生的二级评估指标，而混淆矩阵则记录了 TP、TN、FP、FN 四个基础统计量。混淆矩阵又称误差矩阵，适用于二分类与多分类任务，在压铸缺陷分类场景中广泛使用 [[S10,S24]]。

以压铸变速箱壳体质量预测为例，图 1 展示了典型的多分类混淆矩阵热力图，对角线给出了各类别的正确预测数量，可直接用于推导模型整体的分类准确率 [[S29,S18]]。

![压铸变速箱壳体质量预测模型训练样本的混淆矩阵](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcfdf34b-655c-4927-905a-38ebec666d7c/resource)

在铝铸件自动 X 射线检测中，TP（正确检出缺陷）与 FP（误判为非缺陷）的判定通常需要参考预测框与真实标注框的重合程度（IoU≥0.5 时视为 TP）。图 2 给出了标注有多个缺陷区域及置信度的检测结果，直观反映了准确率计算中 TP/FP 的统计来源 [[S28,S26]]。

![铝合金压铸件X射线缺陷检测标注示例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5624880-5ddb-45d3-8dce-ef4343e43234/resource)

## 在压铸缺陷预测中的应用

准确率在压铸缺陷预测中主要用于表征模型的整体预测能力，是评价遗传神经网络、随机森林、深度学习等模型性能的基础指标 [[S20,S11,S3,S8]]。

- **工艺参数优化与质量预测**：基于遗传神经网络构建的变速箱壳体压铸质量预测模型，优化后整体预测准确率达到 96%，其中对无缺陷与完全不合格两类样本的预测准确率甚至可达 100%，满足了工业场景中“不允许将合格件误判为不合格，亦不允许将不合格件误判为合格”的质量控制要求 [[S3,S11]]。
- **缺陷分类与智能检测**：在镁合金压铸件数据集中，随机森林模型在原始非平衡数据上的总准确率高达 93.67%，但仅以此指标评价会出现严重误判（见下节）[[S6,S20]]。在砂型铸造缺陷预测中，经 SMOTE 均衡处理后，神经网络模型的测试集准确率可稳定提升至 97.91% 左右 [[S27,S8]]。
- **目标检测场景的术语差异**：需要特别指出，在部分压铸件 X 射线目标检测文献中，“准确率”一词被用于表示 \(TP/(TP+FP)\)，即通常所说的 **精确率（Precision）**，而非本词条讨论的全局分类准确率。此时该指标主要反映模型的误检水平，数值越高代表误检率越低 [[S26]]。因此阅读压铸缺陷检测文献时须注意上下文区分。

## 与其他评价指标的关系

准确率只反映整体的正确分类比例，无法体现各类别的个体表现。因此，在压铸缺陷预测中，它通常与精确率、召回率、F1 分数、特异度以及 ROC‑AUC 等指标配合使用，构成多维度的评估体系。表 1 给出了二分类场景下各指标的简要对比 [[S17,S2,S20]]。

| 指标 | 定义公式 | 关注点 |
|------|----------|--------|
| 准确率 (Accuracy) | \((TP+TN)/(TP+TN+FP+FN)\) | 整体预测正确的比例 |
| 精确率 (Precision) | \(TP/(TP+FP)\) | 预测为缺陷的样本中真正的缺陷比例 |
| 召回率/真阳性率 (Recall/TPR) | \(TP/(TP+FN)\) | 真实缺陷中被成功检出的比例 |
| 特异度 (Specificity) | \(TN/(TN+FP)\) | 正常样本中被正确判为正常的比例 |
| F1 分数 (F1‑score) | \(2\times P\times R/(P+R)\) | 精确率与召回率的调和均值 |
| AUC | ROC 曲线下面积 | 模型综合性能的稳健性 |

## 类别不平衡下的局限性

在压铸实际生产中，无缺陷的良品数量往往远多于气孔、缩松、裂纹等各类缺陷样本，形成典型的“长尾分布”数据集 [[S6,S8]]。此时仅凭高准确率可能产生严重误导：

- **镁合金压铸件实例**：某数据集中良品样本高达 39 132 条，而同时出现三种缺陷的极端不良样本仅 34 条。随机森林模型在该原始分布上的总准确率达到 93.67%，AUC 为 0.9708，看似性能优异；但三类缺陷的召回率（真正率）分别低至 48.35%、31.94% 和 18.18%，平均真正率（ATPR）仅 49.47%，大量缺陷件被错误地归为良品，存在严重的漏检安全风险 [[S6]]。
- **不平衡对抗措施**：采用降采样与 SMOTE 过采样结合的方法对数据分布进行均衡化后，同一模型的整体准确率虽小幅下降至 89.54%，但 AUC 提高至 0.9838，ATPR 大幅提升至 87.65%，占总样本仅 0.1% 的极端少数缺陷样本的检出率也超过 90%，完全满足了工业质检对缺陷“零漏判”的严格要求 [[S6]]。
- **训练过程的收敛表现**：在不平衡数据上，模型准确率随迭代次数会出现剧烈震荡，无法实现正常的严格递增收敛；而经过均衡预处理后，准确率曲线呈平滑单调上升，最终测试集准确率可达 97.91% 左右 [[S8,S27]]。

因此，压铸领域的研究与工业实践普遍推荐采用 **准确率 + 平均真正率（ATPR）+ AUC** 的多指标组合评估方案，以避免单一准确率带来的评估误导 [[S20,S6]]。

## 派生指标

- **平均真正率（Average True Positive Rate, ATPR）**：对各个类别分别计算真正率（召回率）后取算术平均，被视作体现“平衡准确率”思想的核心指标。在类别严重不均衡时，它比全局准确率更能反映模型对各类别缺陷的平均检出能力 [[S20,S6]]。
- **AP（平均准确率，Average Precision）**：在目标检测任务中，基于精确率‑召回率曲线下面积计算的单类检测精度，常用于压铸件 X 射线缺陷检测中的气孔、缩孔识别 [[S26]]。
- **Top‑k 准确率**：当模型输出多个候选类别时，验证真实标签是否出现在概率最高的 k 个预测结果中，适用于部分多标签工艺参数推荐的评价场景，在本领域文献中偶有使用。

## 相关标准与规范

准确率的计算本身属于统计学与机器学习的通用方法，但在压铸领域，其前提——缺陷标注的可靠性——有赖于一系列检测与验收标准。以下标准为铸造件内部缺陷的定义、检测和评定提供了合规性基础，从而保证了准确率计算的基准一致 [[S5,S15]]：

- **ISO 9916:1991**（铝合金和镁合金铸件液体渗透检测）统一规定了缺陷迹痕的严重程度等级；
- **GB/T 29070‑2012**（工业 CT 铸件检测）为无损检测操作提供了规范；
- **ASTM E2862**（针对命中/未命中数据的概率检测分析）给出了 POD 统计评估的标准方法，为缺陷检出性能评价提供了统计框架。

在铝铸件自动 X 射线检测中，常采用真阳性率（TPP）和假阳性率（FPP）作为辅助指标，理想状态为 TPP=100%、FPP=0%；对于直径≥2.5 mm 的气孔类缺陷，TPP 可以实现 100% [[S7]]。

## Sources
- S17: [基于YOLO算法的激光粉末床熔融成形层形貌分类识别与成形质量预测研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80d9fc2b-8cb5-4122-9f30-b8517e2b4053/resource) (`80d9fc2b-8cb5-4122-9f30-b8517e2b4053`)
- S2: [基于砂铸生产大数据的铸件缺陷质量分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/068871bf-f635-4152-acca-6de2c007edc3/resource) (`068871bf-f635-4152-acca-6de2c007edc3`)
- S10: [10087822_混淆矩阵](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ba570e3-371b-40c6-9baf-1422ec1e6926/resource) (`4ba570e3-371b-40c6-9baf-1422ec1e6926`)
- S20: [基于数据驱动的镁合金压铸件质量智能预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b9eda0f6-e27b-4508-b787-d8abea2b3bf4/resource) (`b9eda0f6-e27b-4508-b787-d8abea2b3bf4`)
- S19: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9b72cf8-b5b6-4ab8-bc00-adaf10e515be/resource) (`a9b72cf8-b5b6-4ab8-bc00-adaf10e515be`)
- S12: [融合领域知识和集成模型的挤压铸造工艺数据正确性检测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65c8294e-bbbb-4979-a34f-5f92ceea9ab5/resource) (`65c8294e-bbbb-4979-a34f-5f92ceea9ab5`)
- S24: [混淆矩阵基本信息表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf481751-9a0e-4e96-b916-7e2b9ccdcd3d/resource) (`cf481751-9a0e-4e96-b916-7e2b9ccdcd3d`)
- S29: [(b) 训练样本的混淆矩阵](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcfdf34b-655c-4927-905a-38ebec666d7c/resource) (`fcfdf34b-655c-4927-905a-38ebec666d7c`)
- S18: [图4.12 质量预测模型训练结果与预测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3c3da1f-38f2-4673-8ca5-ecf7d7af3e11/resource) (`a3c3da1f-38f2-4673-8ca5-ecf7d7af3e11`)
- S28: [铝合金压铸件X射线图像缺陷检测标注图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5624880-5ddb-45d3-8dce-ef4343e43234/resource) (`f5624880-5ddb-45d3-8dce-ef4343e43234`)
- S26: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb8d5146-ff5e-4653-acc7-76497d4e932b/resource) (`eb8d5146-ff5e-4653-acc7-76497d4e932b`)
- S11: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51e1e422-1a7d-4f25-8458-5072fb4a1cbe/resource) (`51e1e422-1a7d-4f25-8458-5072fb4a1cbe`)
- S3: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/174f1bb5-d3f4-4e4d-9736-5b2826a750f6/resource) (`174f1bb5-d3f4-4e4d-9736-5b2826a750f6`)
- S8: [SMOTE数据预处理算法在砂型铸造复杂铸件缺陷预测中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a9ebf5e-3e36-44df-94a0-708261cae79b/resource) (`3a9ebf5e-3e36-44df-94a0-708261cae79b`)
- S6: [基于数据驱动的镁合金压铸件质量智能预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c5849d8-8363-464f-87db-4d6d6cae64dc/resource) (`1c5849d8-8363-464f-87db-4d6d6cae64dc`)
- S27: [SMOTE数据预处理算法在砂型铸造复杂铸件缺陷预测中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efa52087-a618-49f5-b2ab-ea506ad2d509/resource) (`efa52087-a618-49f5-b2ab-ea506ad2d509`)
- S5: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1bd7673c-fb5e-425e-8792-02e8d1923db2/resource) (`1bd7673c-fb5e-425e-8792-02e8d1923db2`)
- S15: [0289_9aa0a01a8e7813ea_Nondestructive_testing](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7df7d760-f737-40d4-ae8d-79c42520bf0b/resource) (`7df7d760-f737-40d4-ae8d-79c42520bf0b`)
- S7: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c2cc11e-f927-48c0-8f64-1401d1c4e31f/resource) (`2c2cc11e-f927-48c0-8f64-1401d1c4e31f`)