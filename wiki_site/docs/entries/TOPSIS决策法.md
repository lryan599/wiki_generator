---
version: "v1"
generated_at: "2026-06-18T13:50:04+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 21
  source_quality_score: 0.83
  freshness_score: 0.87
  evidence_coverage_score: 1.0
---

## 概述

**TOPSIS**（Technique for Order Preference by Similarity to Ideal Solution），中文全称“优劣解距离法”，是一种应用广泛的多属性决策评价方法[[S16,S8]]。其核心逻辑是通过测算各参评方案与正理想解、负理想解的欧氏距离，得到对应方案的相对贴近度，据此判定方案的优劣等级，筛选出同时满足“距离正理想解尽可能近、距离负理想解尽可能远”的最优折中方案[[S20,S3]]。

在压铸及铸造工艺参数优化领域，TOPSIS 通常与多目标优化算法（如 NSGA-II、响应面法等）联合使用，从 Pareto 前沿非支配解集中快速筛选出综合性能最优的工艺参数组合[[S3,S18,S20]]。

## 基本概念与术语

| 术语 | 定义 |
|------|------|
| **正理想解（A⁺）** | 各评价维度下所有参评方案的指标最优值的集合 |
| **负理想解（A⁻）** | 各评价维度下所有参评方案的指标最劣值的集合 |
| **相对贴近度（rᵢ）** | rᵢ = dᵢ⁻ / (dᵢ⁺ + dᵢ⁻)，其中 dᵢ⁺、dᵢ⁻ 分别为方案到正、负理想解的欧氏距离；rᵢ ∈ [0,1]，值越大方案综合表现越优 |

以上定义基于标准 TOPSIS 逻辑[[S3,S20]]。

## 标准算法步骤

TOPSIS 标准化全流程共包含 **7 个步骤**，适用于压铸工艺参数筛选场景[[S3,S17,S20,S18]]：

| 步骤 | 操作 | 公式/说明 |
|------|------|-----------|
| 1 | 构建决策矩阵 | 创建 m 个方案 × n 个指标的原始决策矩阵 X |
| 2 | 向量归一化 | bᵢⱼ = xᵢⱼ / √(∑ xᵢⱼ²)，消除量纲差异 |
| 3 | 加权标准化 | aᵢⱼ = wⱼ × bᵢⱼ，引入指标权重因子 |
| 4 | 确定正/负理想解 | A⁺ 取各维度最大值集合，A⁻ 取各维度最小值集合 |
| 5 | 计算欧氏距离 | dᵢ⁺ = √[∑(aᵢⱼ − A⁺ⱼ)²]，dᵢ⁻ = √[∑(aᵢⱼ − A⁻ⱼ)²] |
| 6 | 计算相对贴近度 | rᵢ = dᵢ⁻ / (dᵢ⁺ + dᵢ⁻) |
| 7 | 排序与择优 | 按 rᵢ 从大到小排序，最大 rᵢ 对应的方案为最优折中解 |

## 多目标优化中的定位

在压铸/铸造多目标优化流程中，TOPSIS 处于 Pareto 前沿生成后的**最终决策环节**。典型流程为：实验设计（BBD等）→ 数值仿真 → 响应面/克里金代理模型建模 → 方差分析 → NSGA-II 算法生成 Pareto 前沿 → **TOPSIS 筛选最优解** → 仿真验证[[S7]]。

以下流程图完整展示了 A356 铝合金缸盖压铸工艺多目标优化全链路，涵盖上述 8 个核心步骤[[S7]]：

![A356铝合金缸盖压铸工艺多目标优化全流程图，集成NSGA-II寻优与TOPSIS最优解筛选步骤](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c070d0e-66d4-4830-9ed2-b59d57aa3c0a/resource)

TOPSIS 方法可以从大量平衡充型温度、压射速度、压射比压、缩孔率、热裂倾向、模具热应力等多维度指标的候选方案中，快速筛选出综合性能最优的工艺参数组合[[S18,S20,S3]]。

## 应用案例

### 案例一：K4169 合金熔模精铸蜗壳

以缩孔体积最小化、凝固时间最大化为双优化目标，采用 NSGA-II 算法（种群规模 30、迭代 200 次）生成 Pareto 前沿后，通过 TOPSIS 筛选得到最优解：缩孔体积 V = 8.6985 cm³，凝固时间 T = 119.2213 s，对应工艺参数为浇注温度 1450 ℃、模壳预热温度 1050 ℃[[S18,S4]]。

### 案例二：A356 铝合金砂型铸造缸盖

以缩松体积与凝固时间为优化目标，结合响应面法与 NSGA-II 算法，经 TOPSIS 筛选的最优工艺组合为：浇注温度 650.25 ℃、模具预热温度 200.32 ℃、浇口横截面宽厚比 1.49、内浇口段宽厚比 2.58、直浇口长径比 2.495。优化后缩松体积降低 9.80%，凝固时间减少 7.25%[[S23,S9]]。

### 案例三：球墨铸铁凸轮轴铸造

以缩孔缩松体积和热裂倾向（HTI 值）的信噪比为双优化目标，基于 RBF 神经网络建模，通过 NSGA-II 生成 20 组非支配解的 Pareto 前沿，采用变异系数法赋权的 TOPSIS 完成多目标决策，获得兼顾降低缩孔缺陷与抑制热裂的最优工艺参数组合[[S12,S20]]。

### 案例四：镁合金半固态流变压铸

结合灰色关联分析（权重 0.4:0.5:0.1）与 TOPSIS 方法对工艺参数组合进行筛选，优化后铸件综合性能提升 25%，工艺稳定性显著提高[[S22]]。

## 与同类方法的比较

TOPSIS 与压铸领域常见的其他多准则决策方法存在以下原理差异[[S8,S10,S11]]：

| 方法 | 核心原理 | 压铸场景适配特点 |
|------|----------|------------------|
| **AHP（层次分析法）** | 指标两两比较判断 | 需人工对数十组工艺质量指标做成对重要度判定，决策成本远高于 TOPSIS |
| **GRA（灰色关联度法）** | 序列关联度排序 | 对压铸指标的非线性关联适配性强，但不同方案的排序区分度显著低于 TOPSIS |
| **VIKOR** | 最大化群体效用、最小化个体遗憾，生成妥协最优解 | 相比 TOPSIS 更适配部分缺陷指标存在刚性不可突破约束的极端优化场景 |

VIKOR 方法的完整执行流程可与 TOPSIS 形成直观对比[[S24]]：

![VIKOR多属性决策方法全流程示意图，支撑TOPSIS与VIKOR的操作逻辑差异对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9f294b4-180c-4826-91cc-3537d3fae93b/resource)

## 适用性与局限性

### 核心优势

- 计算流程完全透明、计算量小易复现，可无缝对接响应面/克里金代理模型 + NSGA-II 等多目标优化算法生成的 Pareto 非支配解集[[S18,S20,S3]]
- 搭配变异系数法、熵权法等客观赋权方法，可降低人工设定指标权重带来的主观偏差[[S20,S3]]

### 主要局限

1. **冗余指标干扰**：采用欧氏距离度量，未考虑各质量指标之间的潜在相关性，容易放大冗余指标对最终排序的干扰[[S20,S3]]
2. **理想解依赖样本极值**：正负理想解的取值完全依赖输入候选解集的极值；当实验样本覆盖范围有限时，所得理想解并非全局最优/最劣值，可能导致排序偏差[[S20,S3]]
3. **低量级缺陷指标权重弱化**：经向量归一化处理后，微量气孔率、微裂纹占比等低量级关键缺陷指标的权重贡献易被大数值的力学性能指标弱化，无法充分突出缺陷类指标的高优先级[[S20,S3]]

## 权重确定方法

TOPSIS 常用权重确定方法分为两类[[S2,S6,S20,S15]]：

| 类别 | 方法 | 说明 |
|------|------|------|
| 客观赋权 | **熵权法** | 基于信息熵原理，指标信息熵越小、离散度越大则权重越高，仅通过原始数据即可直接得到权重 |
| 客观赋权 | **变异系数法** | Vⱼ = σⱼ / ȳⱼ，wⱼ = Vⱼ / ∑Vⱼ；指标数据分布差异越大对应权重越高 |
| 主观赋权 | **专家打分法** | 多名行业专家独立评定各指标重要性，取平均值作为对应指标权重 |

## 常用实现工具

| 工具 | 适用场景与特点 |
|------|----------------|
| **MATLAB** | 工程领域多目标优化场景中应用广泛，可直接通过脚本实现全流程计算[[S1,S13]] |
| **SPSSAU** | 内置成熟的熵权 TOPSIS 功能模块，支持一键完成从数据预处理到结果输出的全流程，无需编写代码[[S13,S10]] |
| **Python** | 通过 numpy、pandas 等库可快速封装 TOPSIS 算法，适配大批量评价对象的计算需求[[S13,S10]] |
| **Excel** | 通过配置单元格公式实现小规模 TOPSIS 计算，适配非编程用户的轻量化评价需求[[S13,S10]] |

## 输出结果示例

熵权 TOPSIS 的典型计算结果如下表所示，包含各评价对象的正理想解距离 D⁺、负理想解距离 D⁻、相对接近度 C 及最终排序。该样例可直接反映 TOPSIS 方法在候选方案综合评价中的应用效果[[S21]]。

| 评价对象 | D⁺ | D⁻ | C（相对接近度） | 排序 |
|:--------:|:--:|:--:|:--------------:|:----:|
| 1 | 0.725 | 0.483 | 0.400 | 9 |
| 2 | 0.616 | 0.593 | 0.491 | 7 |
| 3 | 0.545 | 0.664 | 0.549 | 5 |
| 4 | 0.472 | 0.728 | 0.607 | 3 |
| 5 | 0.648 | 0.561 | 0.464 | 8 |
| 6 | 0.597 | 0.613 | 0.507 | 6 |
| 7 | 0.508 | 0.701 | 0.580 | 4 |
| 8 | 0.414 | 0.795 | 0.658 | 2 |
| 9 | 0.057 | 1.151 | 0.965 | 1 |

评价对象 9 的相对接近度为 0.965，排名第 1，为最优方案[[S21]]。

## Sources
- S16: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/abd76584-eabf-4b8b-83ea-981299f4f94b/resource) (`abd76584-eabf-4b8b-83ea-981299f4f94b`)
- S8: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67441629-a131-4021-8086-5be86be74285/resource) (`67441629-a131-4021-8086-5be86be74285`)
- S20: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c17c336b-df2a-4d56-908f-d6ed81f8b6e0/resource) (`c17c336b-df2a-4d56-908f-d6ed81f8b6e0`)
- S3: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/283e1a39-0158-440a-ac9a-65eac6380721/resource) (`283e1a39-0158-440a-ac9a-65eac6380721`)
- S18: [熔模精铸K4169合金复杂蜗壳薄壁结构件缺陷预测与工艺多目标优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b77a9394-1579-4e5e-8967-8216e87667b2/resource) (`b77a9394-1579-4e5e-8967-8216e87667b2`)
- S17: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0e82776-724f-48ae-b187-d4f2eb2ca0fd/resource) (`b0e82776-724f-48ae-b187-d4f2eb2ca0fd`)
- S7: [图5.1 优化流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c070d0e-66d4-4830-9ed2-b59d57aa3c0a/resource) (`5c070d0e-66d4-4830-9ed2-b59d57aa3c0a`)
- S4: [熔模精铸K4169合金复杂蜗壳薄壁结构件缺陷预测与工艺多目标优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/305ec7bd-613a-48b9-932a-f6aad5ee5f7b/resource) (`305ec7bd-613a-48b9-932a-f6aad5ee5f7b`)
- S23: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb748977-6c48-4506-8bf1-420d7da63d12/resource) (`eb748977-6c48-4506-8bf1-420d7da63d12`)
- S9: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69c506c9-ea39-4693-b493-b70cb0daaac7/resource) (`69c506c9-ea39-4693-b493-b70cb0daaac7`)
- S12: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78bb93f3-ae52-4bcd-9186-5819154bad72/resource) (`78bb93f3-ae52-4bcd-9186-5819154bad72`)
- S22: [镁合金半固态成形流变与模具耦合机制及工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8aee5e5-88de-448f-9073-81f8f11f03cc/resource) (`e8aee5e5-88de-448f-9073-81f8f11f03cc`)
- S10: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6cbc430d-6f2d-4832-91fc-fdbec3c75698/resource) (`6cbc430d-6f2d-4832-91fc-fdbec3c75698`)
- S11: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71cce692-ad70-4afb-8ca2-6b364765223a/resource) (`71cce692-ad70-4afb-8ca2-6b364765223a`)
- S24: [基于EDAS和VIKOR的多属性决策方法流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9f294b4-180c-4826-91cc-3537d3fae93b/resource) (`f9f294b4-180c-4826-91cc-3537d3fae93b`)
- S2: [5616693_熵权法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0fb8431c-d0a7-49c1-879f-085515af94a7/resource) (`0fb8431c-d0a7-49c1-879f-085515af94a7`)
- S6: [6487336_熵值法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5993e649-a492-4340-8502-269be19595b7/resource) (`5993e649-a492-4340-8502-269be19595b7`)
- S15: [城市道路混合交通流分析模型与方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aaadd5ce-fbe7-465f-afc4-7ce6265e2a69/resource) (`aaadd5ce-fbe7-465f-afc4-7ce6265e2a69`)
- S1: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0493ceb9-c64e-4dcf-b21a-eff5ff7dfdb1/resource) (`0493ceb9-c64e-4dcf-b21a-eff5ff7dfdb1`)
- S13: [复合材料构件热压罐成型模具温度场分析与结构优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9314455d-2947-4bd3-a6ff-5fe7b78fe1bd/resource) (`9314455d-2947-4bd3-a6ff-5fe7b78fe1bd`)
- S21: [熵权TOPSIS评价结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ca336a4f-db80-4b0c-9f35-13a8b4960aa7/resource) (`ca336a4f-db80-4b0c-9f35-13a8b4960aa7`)