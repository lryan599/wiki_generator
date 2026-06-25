---
version: "v1"
generated_at: "2026-06-18T16:08:00+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 17
  source_quality_score: 0.85
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

Fleischer公式（Fleischer equation / Fleischer model），即Fleischer固溶强化模型，是固溶强化领域基于溶质-位错弹性交互作用的经典定量理论模型。该模型的核心原始成果由R. L. Fleischer于1963年首次在*Acta Metallurgica*上发表[[S20,S21]]。其基本思路是将固溶原子引起的尺寸错配效应与剪切模量错配效应联合考虑，建立置换固溶体屈服强度增量与溶质浓度的定量关系[[S2,S18]]。

在压铸领域，Fleischer公式被广泛用于估算镁合金和铝合金中固溶强化对屈服强度的贡献，为合金成分设计和工艺优化提供理论依据。

## 模型公式与参数

### 通用表达式

Fleischer固溶强化模型的标准数学表达式为[[S3,S12]]：

$$
\Delta \sigma_{\mathrm{ss}} = \alpha \, M \, \varepsilon_{\mathrm{ss}}^{3/2} \, c^{1/2}
$$

### 参数释义

| 符号 | 物理意义 | 说明 |
|--------|------------|------|
| Δσₛₛ | 固溶强化增量（MPa） | 由溶质原子引起的非热屈服强度分量 |
| α | 经验常数 | 镁合金场景下典型取值为 1/550 [[S3,S12]] |
| M | 泰勒因子（Taylor Factor） | 表征多晶体中滑移系取向的平均统计系数，将单晶临界分切应力与多晶流变应力关联起来 |
| εₛₛ | 组合错配应变 | 尺寸错配与模量错配的联合参数（定义见下） |
| c | 溶质原子浓度 | 以原子分数表示 |

### 组合错配应变 ε_c

Fleischer模型中，关键的组合错配参数 ε_c（即公式中的 εₛₛ）定义如下[[S20,S4]]：

$$
\varepsilon_{c} = \varepsilon - 3\varepsilon_{\mu}
$$

其中：
- **ε**（尺寸错配参数）：溶质与溶剂原子的晶格尺寸相对偏差，即 ε = (1/b)·db/dc，b 为伯氏矢量[[S2,S18]]；
- **ε_μ**（模量差参数）：溶质浓度变化引发的基体剪切模量相对变化率，即 ε_μ = (1/G)·dG/dc，G 为剪切模量[[S2,S20]]。

Fleischer通过在多种铜基合金中绘制 dσ/dc 与 ε_c 的关系曲线，证明了尺寸错配和模量错配共同对固溶强化产生贡献：当溶质与基体的原子尺寸差较大时，两种效应的强化贡献大致各占 50%；而对 Cu-Zn 类合金，尺寸效应仅贡献约 10% 的屈服强度增量[[S20]]。

## 物理机制

Fleischer模型以位错与溶质原子的长程弹性交互作用为理论基础，核心包含以下两类交互作用[[S2,S23]]：

1. **尺寸因子交互作用**（Elastic size factor interaction）  
   最大交互能 Uₘ ≈ Gb³δ，其中 δ = (1/b)·db/dc。该交互作用对刃位错的钉扎作用最强，起因于溶质原子引入的晶格常数变化。

2. **剪切模量交互作用**（Shear modulus interaction）  
   最大交互能 Uₘ ≈ (Gb³/20)·η，其中 η = (1/G)·dG/dc。该交互作用对螺位错的钉扎作用最强，起因于溶质原子改变局部弹性模量。

由于上述两类交互作用均属长程作用，不能被热激活克服，因此Fleischer模型预测的固溶强化增量属于非热分量（athermal component），其值在中温平台区保持稳定[[S2,S18]]。

Fleischer与Hibbard（1963）将固溶强化分为两类[[S13]]：具有立方对称性的对称缺陷为"缓慢强化型"，其 dτ/dc 在 c ≈ 10⁻² 区间较低；应变场具有大四方度的非对称缺陷为"快速强化型"，在 c ≈ 10⁻⁴ 区间的 dτ/dc 约为前者的 10 倍。在稀溶质区间，Fleischer模型的 c^(1/2) 浓度依赖关系可准确描述该强化差异[[S13]]。

不同尺寸的溶质原子在位错周围（尤其是刃位错上下区域）偏聚，引起局部晶格畸变，阻碍位错滑移，这一机制可用以下示意图辅助理解[[S8]]。

![不同尺寸溶质原子在刃位错周围偏聚的示意图，描述Fleischer理论中尺寸错配引发的长程应变场效应](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4558f585-1545-4808-914c-83355909a598/resource)

## 在压铸合金中的应用

### 镁合金应用

在镁合金固溶强化计算中，Fleischer公式的常用参数取值为[[S3]]：

- G = 16.6 GPa（镁基体剪切模量）；
- α = 1/550。

泰勒因子 M 的常用取值因场景而异。密排六方结构镁合金中，M 的通用取值范围为 4~6.5[[S22]]，常见取值包括 4.2[[S15]] 和 4.5[[S5]]。

**应用案例**：

1. **EA43系Mg-Al-RE压铸合金**[[S5,S7]]：针对 Mg-4La-3Al-0.5Mn、Mg-4Ce-3Al-0.5Mn、Mg-4RE-3Al-0.5Mn 三款重力铸造和压铸合金，采用类Fleischer公式（Δσₛₛ = 3.1εGC^(1/2)/700）计算固溶强化贡献，其中 ε 为常数，G 取 16.6 GPa，溶质浓度通过 EDS 实测。所得重力铸造固溶强化贡献分别为 2.24 MPa、1.98 MPa、4.06 MPa，压铸对应值分别为 2.93 MPa、2.26 MPa、3.54 MPa。

2. **真空压铸LA42镁合金**[[S15]]：采用Fleischer扩展形式 σₛₛ = M(38.9)[(ε_b/0.176)² + (ε_SFE/5.67)² − ε_b·ε_SFE/2.98]^(3/2)·cₛ^(1/2)，M 取 4.2，给出不同溶质元素的错配应变 ε_b 实测值：La 为 29.59，Al 为 -11.50，Mn 为 -35.60。计算得到常规压铸与真空压铸固溶强化贡献差值为 2.6 MPa。

3. **Mg-4Al-5RE-xGd系压铸镁合金**[[S16]]：采用符合幂律特征的固溶强化公式 σₛₛ = B·Xⁿ，n 取 2/3，Al 元素固溶强化系数 B 为 197.5 MPa (at.%)^(-2/3)，溶质含量通过 SEM-EDS 面扫实测。

### 铝合金应用

Fleischer模型同样被应用于铝合金的固溶强化分析中[[S4]]。研究表明，在铝合金中尺寸效应是固溶强化的主导来源[[S4,S20]]。

面心立方铝合金固溶强化计算中，通用泰勒因子 M 取值为 3.06[[S19]]。半固态压铸 Al-Zn-Mg-Cu 合金研究中，给出了 7075 等四种铝合金中 Zn、Mg、Cu 三类溶质元素的原子半径、固溶强化系数及单元素固溶强化应力的实测值，可直接用于 Fleischer 固溶强化计算结果比对[[S1]]。

## 与Labusch模型的对比

Fleischer模型与Labusch模型均为固溶强化领域经实验验证的经典弹性交互作用理论，其核心差异在于浓度依赖关系[[S2,S18]]：

| 模型 | 浓度依赖关系 | 提出者及年代 | 说明 |
|------|-------------|-------------|------|
| Fleischer | Δσ ∝ c^(1/2) | Fleischer, 1964 | 假设稀固溶体中位错在随机分布的孤立溶质原子间选择性克服弱障碍；适用于较稀的固溶体和单个溶质障碍物控制的强化机制 |
| Labusch | Δσ ∝ c^(2/3) | Labusch, 1970 | 考虑位错同时与多个溶质障碍物的统计叠加交互作用；适用于中等浓度以及障碍物密集分布的情形 |

在压铸镁合金工程计算中，两种浓度依赖关系的选用视具体合金体系和浓度范围而定。例如 Mg-4Al-5RE-xGd 系中使用 n = 2/3（即Labusch类关系）计算 Al 元素的固溶强化贡献[[S16]]；而多数镁合金Fleischer公式应用则采用 c^(1/2) 关系[[S3,S12]]。

## 局限性与注解

1. **浓度适用范围**：Fleischer模型以稀固溶体假设为基础，c^(1/2) 依赖关系在较稀浓度区间最为有效[[S2]]。Fleischer与Hibbard的分类显示，"快速强化型"缺陷在 c ≈ 10⁻⁴ 区间的准确度良好[[S13]]。

2. **完整性**：Fleischer模型仅计入尺寸错配与模量错配两类长程弹性交互作用，未直接计入化学交互作用（如Suzuki效应）、短程有序效应（SRO效应）等短程作用[[S2,S23]]。对于时效硬化合金，固溶强化仅构成屈服强度的一部分，需配合析出强化、晶界强化等机制的叠加分析[[S3]]。

3. **镁合金参数 α = 1/550 的适用性**：该取值在国内压铸镁合金学术研究中被多次引用和使用[[S3,S12,S15]]，具有特定体系的参数化特征，不宜直接视为Fleischer模型的普适常数。

4. **错配应变 εₛₛ 的确定**：实际应用中，εₛₛ 需结合尺寸差参数 ε 和模量差参数 ε_μ 联合计算。不同溶质-基体体系的 εₛₛ 取值差异较大，如镁合金中 La 为 29.59，Al 为 -11.50，Mn 为 -35.60[[S15]]。缺乏实验数据时，需通过热力学数据或第一性原理计算辅助确定。

## Sources
- S20: [defects in crystalline solids__b78b4ecb9d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc271943-5181-437b-9947-00969eb03c55/resource) (`cc271943-5181-437b-9947-00969eb03c55`)
- S21: [basic mechanical properties and lattice defects of intermetallic compounds__affa85d061](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3de4ef0-7030-4374-a22d-40d8c8e5df0d/resource) (`d3de4ef0-7030-4374-a22d-40d8c8e5df0d`)
- S2: [TextNode8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0bb212cd-607c-47e9-8635-5dc753e50c57/resource) (`0bb212cd-607c-47e9-8635-5dc753e50c57`)
- S18: [alloy and microstructural design__3d0c892f7c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1979b1f-c392-4b47-8ef1-f11ec3cc701f/resource) (`b1979b1f-c392-4b47-8ef1-f11ec3cc701f`)
- S3: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12d4a22d-ed5d-42d8-aa30-2dc448252563/resource) (`12d4a22d-ed5d-42d8-aa30-2dc448252563`)
- S12: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59aa20ab-fdad-4c60-939e-537708e59042/resource) (`59aa20ab-fdad-4c60-939e-537708e59042`)
- S4: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13965e95-8bbc-4672-9a11-8110c57e88af/resource) (`13965e95-8bbc-4672-9a11-8110c57e88af`)
- S23: [alloy and microstructural design__1a336db267](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ead20dc1-1438-4969-8373-eda6f4394aa7/resource) (`ead20dc1-1438-4969-8373-eda6f4394aa7`)
- S13: [TextNode86](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63656e1c-8bd6-40d7-908a-8600b1a92873/resource) (`63656e1c-8bd6-40d7-908a-8600b1a92873`)
- S8: [溶质原子在位错周围聚集的示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4558f585-1545-4808-914c-83355909a598/resource) (`4558f585-1545-4808-914c-83355909a598`)
- S22: [低压铸造镁合金研究现状及展望](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5b047db-4d32-49a7-87ac-afe874ee9def/resource) (`d5b047db-4d32-49a7-87ac-afe874ee9def`)
- S15: [真空压铸对LA42镁合金热导率和力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8411037d-9e6f-4c24-9a29-e9d389aca035/resource) (`8411037d-9e6f-4c24-9a29-e9d389aca035`)
- S5: [稀土成分对EA43合金组织、力学及导热性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e5a2fd6-dd9c-4686-ac22-f934793afd4c/resource) (`1e5a2fd6-dd9c-4686-ac22-f934793afd4c`)
- S7: [稀土成分对EA43合金组织、力学及导热性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40b22c61-f44b-440e-bcce-2f1fca3ee4c4/resource) (`40b22c61-f44b-440e-bcce-2f1fca3ee4c4`)
- S16: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84ca481c-f1b6-4f76-8c9a-2c0b5ff92eb5/resource) (`84ca481c-f1b6-4f76-8c9a-2c0b5ff92eb5`)
- S19: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3912501-633c-4de9-a6e7-dfa524c66718/resource) (`b3912501-633c-4de9-a6e7-dfa524c66718`)
- S1: [表3 合金元素的固溶强化贡献值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/057402ca-93fe-4d38-83e8-b89a1fc27d3f/resource) (`057402ca-93fe-4d38-83e8-b89a1fc27d3f`)