---
version: "v1"
generated_at: "2026-06-18T15:14:03+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 29
  source_quality_score: 0.83
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 定义

**极差 R** 是正交试验极差分析（又称直观分析法，简称 R 法）中的核心统计量，用于表征某一试验因素在不同水平切换时对响应指标的影响幅度[[S31,S21,S25]]。其定义为：对第 \(j\) 个因素，计算该因素各水平下所有对应试验响应指标的平均值 \( \bar{k}_{j1}, \bar{k}_{j2}, \dots, \bar{k}_{jn} \)，然后取这些平均值中的最大值与最小值之差[[S31,S17,S5]]：

\[
R_j = \max(\bar{k}_{j1}, \bar{k}_{j2}, \dots, \bar{k}_{jn}) - \min(\bar{k}_{j1}, \bar{k}_{j2}, \dots, \bar{k}_{jn})
\]

其中，\( \bar{k}_{jm} \) 是第 \(j\) 个因素在第 \(m\) 个水平下所有对应试验响应指标的算术平均值，其计算过程需先求同一水平下的指标总和 \(K_{jm}\)，再除以该水平下的试验重复次数 \(n\)[[S17,S12,S4]]。符号 R 是正交设计中极差的通用符号，在铸造工艺优化领域广泛使用[[S21,S25]]。

## 基本属性

- **取值范围**：\( [0, +\infty) \)。当 \(R = 0\) 时，表明该因素的各水平对试验指标无统计意义上的显著影响[[S4,S2]]。
- **量纲**：R 的量纲与所分析的试验响应指标量纲一致，不进行额外的无量纲化[[S4,S2]]。
- **水平数不同时的校正**：当正交试验中各因素水平数不相等时，直接比较原始极差 R 会产生偏差，水平数多的因素天生会获得更大的 R 值。此时必须采用折算公式进行校正[[S11,S22]]：
  \[
  R' = d \times \sqrt{r} \times R
  \]
  其中 \(r\) 为该因素对应水平的重复试验次数，\(d\) 为该因素水平数对应的折算系数。只有折算后的 \(R'\) 才可用于公平比较不同水平数因素的作用显著性。

## 极差分析的操作流程

极差分析法的标准流程可分为计算与判断两大模块[[S4,S31,S10]]：

1. **计算环节**：
   - 逐因素计算各水平下的试验指标总和 \(K_{jm}\) 及其平均值 \(\bar{K}_{jm}\)。
   - 计算全部试验响应的总和 \(T\)。
   - 逐因素计算极差 \(R_j = \max(\bar{K}_{jm}) - \min(\bar{K}_{jm})\)。
2. **判断环节**：
   - 按 \(R_j\) 的数值从大到小排序，得到各因素对指标的影响主次顺序。
   - 根据预定的指标优化方向（望大或望小），选取各因素的最优水平，进而组合成初步最优工艺参数方案。
   - 若推导出的最优组合不在已完成的试验组中，必须追加验证试验确认效果[[S4,S10]]。

该流程的完整示意如下图所示。

![正交试验极差分析法（R法）操作流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a69a7b09-1f3e-4d37-940a-770aba806545/resource)

图注：该图源自镁、铝合金熔炼及低压铸造水模拟技术研究，展示了极差分析 R 法的两大步骤——计算 \(K_{jm}\)、\(\bar{K}_{jm}\)、\(R_j\) 以及判断因素主次与最优组合[[S24]]。

## 判定规则与最优水平选择

通过 R 值判定因素重要性的规则是：R 值越大，该因素水平变化造成的响应波动越大，其影响越显著[[S8,S17,S12,S32]]。对所有因素的 R 值降序排列，即为因素影响的主次顺序。

推导最优工艺参数组合的方法为[[S8,S7]]：
- 若指标为**望大特性**（越大越好），选取各因素对应 \(\bar{k}\) 序列中最大值所处的水平；
- 若指标为**望小特性**（越小越好），选取各因素对应 \(\bar{k}\) 序列中最小值所处的水平。

在确定最终参数时，应优先保证 R 值最大的主要因素取得最优水平，次要因素可结合实际成本、工艺可行性等进行合理调整[[S7]]。

## 与方差分析（ANOVA）的区别

极差分析法与方差分析同为正交试验结果的两大分析手段，二者在计算逻辑、指标含义和适用场景上有本质差异[[S31,S32,S15]]：

| 对比维度 | 极差分析（R 法） | 方差分析（ANOVA） |
|---------|----------------|------------------|
| 计算基础 | 仅基于各水平均值的极值差 | 分解总离差平方和为因素离差平方和与误差离差平方和，计算均方和 F 值 |
| 指标含义 | 直接反映因素水平间绝对差异幅度，无统计显著性判断 | F 值是因素均方与误差均方之比，可定量计算各因素的贡献率 |
| 误差处理 | 无法分离试验误差 | 可估计误差大小，并通过 F 检验判定显著性 |
| 适用场景 | 工程快速初筛、教学演示、小样本试验的初步分析 | 正式研究中需给出统计显著结论、排除随机误差干扰的场景 |

## 在压铸工艺优化中的应用

极差分析法在压铸工艺参数优化中应用广泛，以下为若干典型实例。

**5A06 铝合金盒体压铸**：以抗拉强度为指标，三因素三水平正交试验。浇注温度、模具预热温度、压射比压对应的极差 R 分别为 9.14、3.54、11.37，因素主次为：压射比压 > 浇注温度 > 模具预热温度。最优组合为浇注温度 670℃、模具预热温度 200℃、压射比压 120 MPa，该参数下铸件抗拉强度达 307.60 MPa，X 射线探伤无明显缺陷，气密性检验合格率达 95%[[S17,S23,S29,S27]]。

**变速箱壳体压铸**：以缩松缩孔缺陷总分为指标，浇注温度、压射速度、模具预热温度的极差 R 分别为 9.68、14.41、7.25，因素主次为：压射速度 > 浇注温度 > 模具预热温度。优化后铸件缺陷较原始工艺减少 20.22%[[S20]]。

**铝合金水冷板压铸**：同时对卷气量和缩孔缩松进行极差分析。以卷气量为指标时，R 排序为模具温度 > 压射速度 > 浇注温度，最优参数为浇注温度 670℃、模具温度 190℃、压射速度 4 m/s；以缩孔缩松为指标时，R 排序为浇注温度 > 模具温度 > 压射速度，最优参数为浇注温度 660℃、模具温度 210℃、压射速度 4 m/s[[S28]]。

**AZ91-Ce 镁合金压铸**：以缩孔缩松总面积为指标，极差计算结果如下表所示[[S18]]。

| 因素 | \(K_1\) / 均值 | \(K_2\) / 均值 | \(K_3\) / 均值 | 极差 R |
|------|----------------|----------------|----------------|--------|
| 浇注温度 | 0.7656 / 0.2552 | 0.6909 / 0.2303 | 0.8756 / 0.2919 | 0.0624 |
| 压射速度 | 0.7740 / 0.2574 | 0.7399 / 0.2466 | 0.8009 / 0.2670 | 0.0486 |
| 模具预热温度 | 0.7853 / 0.2618 | 0.6912 / 0.2304 | 0.8328 / 0.2776 | 0.0322 |

因素主次顺序为浇注温度 > 压射速度 > 模具预热温度，与 R 值大小完全一致。

下图展示了低压铸造中六个工艺因素的极差随水平变化的趋势，直观反映了不同因素对充填形式的影响程度差异。

![低压铸造正交试验6因素极差随水平变化趋势图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40ac9b55-3547-439a-b568-7c4771de6eea/resource)

图注：该图来自低压及差压铸造理论，纵轴为极差 R，展示 A～F 六个因素的极差随两水平的变化规律，可用于说明极差分析中因素影响强弱的判别[[S6]]。

## 相关术语

- **K 值（同水平响应总和）**：某因素在某一水平下所有对应试验响应指标的累加和。将其除以该水平下的试验次数得到该水平的平均响应值 \(\bar{k}\)[[S31,S12,S4]]。
- **极差分析表**：整合正交试验原始结果、各因素各水平的 K 值、\(\bar{k}\) 值、总响应和 T 以及逐因素 R 值的结构化表格，是极差分析的核心输出载体[[S16,S14]]。
- **主效应图**：以因素水平为横轴、该水平下的平均响应值 \(\bar{k}\) 为纵轴绘制的折线图，可用于直观判断因素的优化方向并对比不同因素的影响幅度[[S19,S9,S13]]。

## 局限性

极差分析法的应用前提为试验数据来自具备“均匀分散、整齐可比”特性的正交试验[[S3]]。其固有局限在于[[S31,S32]]：
- 无法将试验随机误差造成的波动与因素真实水平差异造成的波动分离，因而不能定量估计试验误差的大小；
- 不能通过统计显著性检验判定某因素的影响是否真实存在，所获得的主次排序和最优组合仅为初步近似结果；
- 必须通过追加验证试验来确认最终有效性。

## Sources
- S31: [镁、铝合金熔炼及低压铸造水模拟技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb89af85-55e5-47ce-90ea-65e501b81f6c/resource) (`eb89af85-55e5-47ce-90ea-65e501b81f6c`)
- S21: [基于3D打印的注塑模随形冷却水路优化设计及应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/958b6b42-4197-4ee4-9b28-350b3436e327/resource) (`958b6b42-4197-4ee4-9b28-350b3436e327`)
- S25: [基于Moldex3D的高精度空心杯电机电枢注塑封装工艺仿真优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a72f617b-433d-440b-be68-a5a22652a00d/resource) (`a72f617b-433d-440b-be68-a5a22652a00d`)
- S17: [5A06铝合金盒体压铸成形工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a1a1096-f0f0-4103-a323-052e3d0936c4/resource) (`6a1a1096-f0f0-4103-a323-052e3d0936c4`)
- S5: [直流磁系统的计算与分析 模型·算法·程序](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37be9d0d-560a-4f60-9724-5a62daf87af3/resource) (`37be9d0d-560a-4f60-9724-5a62daf87af3`)
- S12: [直流磁系统的计算与分析 模型·算法·程序](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f54494f-dc52-47cc-964a-8106e6fe472d/resource) (`5f54494f-dc52-47cc-964a-8106e6fe472d`)
- S4: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25e857b4-4f01-4287-a18f-227636c2e169/resource) (`25e857b4-4f01-4287-a18f-227636c2e169`)
- S2: [挤压铸造制备铜_铝双金属构件关键技术及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15d0930e-6059-4c08-a382-0bfc6dab07c1/resource) (`15d0930e-6059-4c08-a382-0bfc6dab07c1`)
- S11: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f192705-f807-46f2-9101-045349a8ad94/resource) (`5f192705-f807-46f2-9101-045349a8ad94`)
- S22: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9dadaff2-84ed-488d-94d1-a2fd7aec00da/resource) (`9dadaff2-84ed-488d-94d1-a2fd7aec00da`)
- S10: [图3.18 极差分析法流程示意](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/574595b5-b385-4f2d-be0e-f96bd6f32322/resource) (`574595b5-b385-4f2d-be0e-f96bd6f32322`)
- S24: [图2.2 极差分析法流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a69a7b09-1f3e-4d37-940a-770aba806545/resource) (`a69a7b09-1f3e-4d37-940a-770aba806545`)
- S8: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42a0e311-1756-47f0-a623-d102a9eb7a94/resource) (`42a0e311-1756-47f0-a623-d102a9eb7a94`)
- S32: [镁合金高铁枕梁的结构设计及成型工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f875601a-9210-48f4-b7c1-3a21726327d4/resource) (`f875601a-9210-48f4-b7c1-3a21726327d4`)
- S7: [挤压铸造成形铝合金飞轮壳构件微观组织与力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42230986-8dcc-4140-8cf0-fc42aa58d1ad/resource) (`42230986-8dcc-4140-8cf0-fc42aa58d1ad`)
- S15: [云母加热器式热流道喷嘴热平衡优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/663a5780-f38d-47cf-a301-94869ee08776/resource) (`663a5780-f38d-47cf-a301-94869ee08776`)
- S23: [TextNode35](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e63aa1c-d976-4eb4-9e50-06706b7f15fc/resource) (`9e63aa1c-d976-4eb4-9e50-06706b7f15fc`)
- S29: [TextNode33](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dea70516-6679-40c7-8c98-9c30af32de8c/resource) (`dea70516-6679-40c7-8c98-9c30af32de8c`)
- S27: [TextNode36](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae03e8b7-7507-4a1d-896d-c9f3bf1929d0/resource) (`ae03e8b7-7507-4a1d-896d-c9f3bf1929d0`)
- S20: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/861830a1-0c69-4417-a567-83047371b719/resource) (`861830a1-0c69-4417-a567-83047371b719`)
- S28: [铝合金水冷板压铸过程数值模拟研究及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfe3aa3f-8550-4fcf-a37e-8d4bbe0f81dd/resource) (`bfe3aa3f-8550-4fcf-a37e-8d4bbe0f81dd`)
- S18: [表4.5 正交试验结果与极差分析表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d2b7c83-e8e0-4da5-a4ef-99af306d1a43/resource) (`6d2b7c83-e8e0-4da5-a4ef-99af306d1a43`)
- S6: [各因素极差随水平的变化图（图1.33）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40ac9b55-3547-439a-b568-7c4771de6eea/resource) (`40ac9b55-3547-439a-b568-7c4771de6eea`)
- S16: [表2 正交试验极差分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67482b61-eca4-46f0-be25-932d6d7cad44/resource) (`67482b61-eca4-46f0-be25-932d6d7cad44`)
- S14: [表5-4 正交试验极差分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63dad3e5-7435-44ec-a6bc-a83ca83e5c42/resource) (`63dad3e5-7435-44ec-a6bc-a83ca83e5c42`)
- S19: [汽车发动机底护板复合材料塑件的成型工艺优化及多尺度联合仿真](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71bd391a-8dca-487e-93de-69777113e9d4/resource) (`71bd391a-8dca-487e-93de-69777113e9d4`)
- S9: [差速器壳体高压压铸工艺模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55ef2a9d-7414-45a4-a64e-7628ff5d565d/resource) (`55ef2a9d-7414-45a4-a64e-7628ff5d565d`)
- S13: [基于熵值法的铝合金缸体低压铸造工艺多目标优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fc53b46-b971-42a8-98d8-0208055348cd/resource) (`5fc53b46-b971-42a8-98d8-0208055348cd`)
- S3: [8699565_正交试验](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ba8f71c-819a-470b-9be7-b7be3812b91d/resource) (`1ba8f71c-819a-470b-9be7-b7be3812b91d`)