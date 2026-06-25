---
version: "v1"
generated_at: "2026-06-18T14:13:37+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 26
  source_quality_score: 0.86
  freshness_score: 0.78
  evidence_coverage_score: 1.0
---

## 概述

Mg-Al二元相图（Mg-Al binary phase diagram）是镁铝二元体系在近平衡条件下各相随温度和成分变化关系的图形化表达，属于压铸镁合金工艺设计的基础热力学参考。该体系全部稳定相包含：富镁端终端固溶体α-Mg（hcp结构）、富铝端终端固溶体α-Al（fcc结构），以及金属间化合物β-Mg₁₇Al₁₂（立方晶系，富镁侧特征相）和Al₃Mg₂（即Mg₂Al₃，富铝端化合物），部分权威相图评估资料还记录了亚稳中间相ε-Al₃₀Mg₂₃ [[S20,S12,S21]]。

对于以AZ91为代表的商用压铸Mg-Al-Zn系镁合金，Mg-Al二元相图是分析其平衡凝固特性、确定半固态成形温度窗口及制定热处理工艺的核心依据。该相图经同行评审的权威评估版本收录于ASM《Binary Alloy Phase Diagrams》第二卷第129–131页 [[S2,S24]]。

## 核心相图特征

### 基本端点与相区

纯镁熔点为650 ℃，纯铝熔点为660.452 ℃，分别构成相图两端的基础标定点 [[S6]]。全组分相图上，自富镁端至富铝端依次分布L（液相）、(Mg)固溶体、(Al)固溶体，以及中间化合物Al₁₂Mg₁₇（即Mg₁₇Al₁₂）、Al₃Mg₂各相区 [[S17,S12]]。

### 富镁侧关键反应与参数

镁侧发生的主要共晶反应为：

**L → α-Mg + Mg₁₇Al₁₂**

共晶温度为437 ℃，对应Al质量分数约12.7% [[S12,S9,S21]]。在共晶温度下，Mg在α-Mg中的极限固溶度为12.7 wt.%；随温度降低固溶度显著下降，至室温时仅约2 wt.% [[S9,S21]]。

### 富铝侧关键反应与参数

铝侧共晶反应为：

**L → α-Al + Al₃Mg₂（即Mg₂Al₃）**

共晶反应温度在449–450 ℃范围内，对应Mg质量分数约33%（原子分数约38 at.%） [[S26,S27,S16,S18]]。共晶温度下Mg在α-Al中的最大固溶度为17.4 wt.%，室温下则降至1.4%–1.9%以下 [[S27,S18,S7]]。富铝端主要中间相Mg₅Al₈（即Mg₂Al₃）为六方晶格结构的脆性金属间化合物，高含量时会降低合金的工业加工性能 [[S27,S18]]。

### 关键温度与成分汇总

| 参数项 | 数值/描述 | 来源 |
|---|---|---|
| 纯Mg熔点 | 650 ℃ | [[S6]] |
| 纯Al熔点 | 660.452 ℃ | [[S6]] |
| 镁侧共晶反应 | L → α-Mg + Mg₁₇Al₁₂ | [[S12,S21]] |
| 镁侧共晶温度 | 437 ℃ | [[S12,S9]] |
| 镁侧共晶Al含量 | ~12.7 wt.% | [[S9,S21]] |
| Mg在α-Mg中最大固溶度 | 12.7 wt.%（436–437 ℃） | [[S9,S21]] |
| Mg在α-Mg中室温固溶度 | ~2 wt.% | [[S9]] |
| 铝侧共晶反应 | L → α-Al + Al₃Mg₂ | [[S16,S27]] |
| 铝侧共晶温度 | 449–450 ℃ | [[S26,S27,S16]] |
| 铝侧共晶Mg含量 | ~33 wt.%（~38 at.%） | [[S27,S16]] |
| Mg在α-Al中最大固溶度 | 17.4 wt.%（共晶温度） | [[S27,S7]] |
| Mg在α-Al中室温固溶度 | 1.4–1.9 wt.% | [[S27,S18]] |
| Mg₁₇Al₁₂相自身熔点 | 458 ℃ | [[S28]] |

### 相图图示

图a493f163-1638-4819-a1fa-7cb203d0e927为Mg-Al全组分二元平衡相图，横轴为Mg质量百分比（0–100%），纵轴为温度（℃，范围100–700 ℃），标注了L液相区、(Al)固相区、(Mg)固相区以及中间相Al₃Mg₂、Al₁₂Mg₁₇的全部相区边界，明确标注纯铝熔点660 ℃、纯镁熔点650 ℃、富铝端共晶温度450 ℃、富镁端共晶温度437 ℃等核心相变点，可直接用于支撑AZ91镁合金凝固特性及相组成分析 [[S12]]。

![Mg-Al二元平衡相图（标注各相区及关键温度点）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a493f163-1638-4819-a1fa-7cb203d0e927/resource)

> 来源：压铸AZ91-Ce镁合金微观组织及力学性能研究，图3.1 Mg-Al二元相图 [[S12]]。

## AZ91合金与平衡固相线/液相线

AZ91名义成分为Mg-9Al-1Zn，在二元简化下可视为Mg-9Al。依据多个权威来源数据，AZ91合金在平衡条件下的关键温度参数如下：

| 参数项 | 数值 | 备注 | 来源 |
|---|---|---|---|
| 平衡液相线温度 | 595–602 ℃ | 多源数据交叉验证 | [[S4,S13,S14]] |
| 平衡固相线温度 | 470–485 ℃ | Pandat计算值/手册数据 | [[S13,S4,S14]] |
| 非平衡凝固完全结束温度 | 414 ℃ | DSC实测 | [[S13]] |
| Mg-Al二元实测固相线 | 约420–430 ℃ | 一次DSC放热峰起始/终止 | [[S13,S10]] |

> **关于用户提示505 ℃的说明**：用户在描述提示中提及AZ91成分区域初熔点约505 ℃。该数值出现在一篇关于热压工艺的研究报告中，文中在使用Mg-Al二元相图分析时引用了这一初熔点温度 [[S19]]。然而，该值明显高于多源权威数据所指向的AZ91平衡固相线温度范围（470–485 ℃） [[S4,S13,S14]]，也与DSC热分析中一次放热（液-固相变）所对应的470 ℃附近温度不符 [[S13]]。因此，建议以470–485 ℃作为AZ91在平衡条件下的固相线参考区间，505 ℃仅作为特定文献中引用的近似或虚拟初熔点对待，不宜作为通用热力学依据。

## 工艺关联：热压温度与致密度控制

Mg-Al二元相图可为AZ91基镁合金的粉末冶金/热压工艺提供温度选择的相变依据。研究表明，在真空热压制备AZ91基复合材料过程中，致密度随热压温度的升高呈现先升后降的规律 [[S19]]：

- 热压温度为500 ℃时，AZB59W1复合材料致密度可达最大值98.8%；
- 热压温度低于430 ℃时，合金基体呈颗粒状，变形能力不足，界面组织较疏松，易出现未熔合孔隙导致致密度偏低；
- 热压温度超过520 ℃时，材料内部出现较多液相并从模具缝隙渗出，破坏基体分布均匀性，反而降低致密度 [[S19]]。

此温度窗口的确定依赖于Mg-Al二元相图所提供的固相线附近相变行为参考：在固相线温度以下，合金以固态变形与扩散实现致密化；超过固相线后液相的出现虽然可能改善润湿和填充，但过量液相溢出将导致成分偏析和致密度下降。

## 工艺关联：半固态压铸温度窗口

半固态压铸温度窗口的确定同样可依托Mg-Al二元相图。对Cp/AZ91D复合材料的研究表明，最佳半固态温度为600 ℃，该温度下可获得满足成形要求的固液两相比例：

- 温度低于600 ℃时，原子扩散速率弱，液相数量不足，初生α-Mg相球化率低，充型阻力显著上升且易产生未熔合缺陷；
- 温度达到600 ℃时，半固态固液两相达到平衡状态，液相比例适中，初生α-Mg相呈球化趋势；
- 温度超过600 ℃并继续升高（如610 ℃）时，初生α-Mg晶粒出现粗化与合并，液相数量过多，部分初生相熔化导致颗粒悬浮于液相中，严重影响后续触变成形的组织均匀性与性能 [[S23,S5]]。

## 局限性与适用边界

### 平衡相图与非平衡凝固的差异

Mg-Al二元相图所记录的为近平衡凝固条件下的相变特征，与压铸生产中的非平衡凝固工况存在显著偏离：

- **固相线与液相线偏移**：快速冷却条件下，固相线向低温侧偏移、液相线向高温侧偏移，结晶温度区间相比平衡态显著扩大 [[S11,S3,S1]]；
- **共晶点移动**：加压速冷条件下，镁侧共晶点向富镁低铝方向移动，铝在镁中的最大固溶度相比平衡态显著降低 [[S22,S11]]；
- **固溶度极限下降**：冷却速度大于1.67 ℃/s时，铝在镁中的平衡最大固溶度12.7%可降至仅0.2% [[S11]]；
- **非平衡共晶组织增多**：极快冷却导致剩余液相量增加，非平衡共晶（离异共晶β-Mg₁₇Al₁₂）占比相比平衡态大幅提升 [[S1,S11]]。

### 合金元素对二元相图的偏移

AZ91合金中含有约1 wt.%的Zn及少量Mn等合金元素。Zn基本固溶于α-Mg和β-Mg₁₇Al₁₂相中，对平衡Mg-Al二元相图相变点的直接偏移幅度很小 [[S25]]。然而，在压铸快冷和加压的双重作用下，实测数据表明：

- AZ91非平衡固相线可从二元平衡共晶温度的437 ℃区域降至约404.2 ℃ [[S10]]；
- 在115 MPa压力下，AZ91合金液相线温度相比二元平衡值额外升高约7.58 ℃ [[S11]]。

### 适用边界总结

Mg-Al二元相图仅适用于冷却速率极低、压力接近常压的近平衡凝固工况。当冷却速度超过10 ℃/s、压力达到数十MPa以上的高压压铸或挤压铸造条件下，不可直接套用平衡相图的固相线、液相线及共晶点位置，必须结合实测非平衡相变温度进行修正，以避免出现工艺温度设定偏差所引发的晶粒粗化、欠充型、液相溢出等生产缺陷 [[S11,S1]]。

## 配图补充：平衡与非平衡状态图对比

图de40887e-7428-4ef4-8b45-921349bd0408直观展示了平衡Mg-Al状态图与加压速冷非平衡工况下的相边界差异：共晶点向富镁低铝方向移动，铝在镁中的最大固溶度相比平衡态显著降低，液相线随压力升高向高温侧偏移，图中还标注了ZM5合金的相区位置，可直接用于支撑挤压铸造、高压压铸等带压凝固场景的相变参数修正说明 [[S22]]。

![加压和速冷对Mg-Al状态图的影响（平衡与非平衡对比）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de40887e-7428-4ef4-8b45-921349bd0408/resource)

> 来源：挤压铸造，加压和速冷对镁-铝状态图的影响 [[S22]]。

## Sources
- S20: [application of phase diagrams in metallurgy vol 2__6d6dee20cd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d45b5e6a-d953-4838-809a-9ea5c70aaf80/resource) (`d45b5e6a-d953-4838-809a-9ea5c70aaf80`)
- S12: [图3.1 Mg-Al二元相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a493f163-1638-4819-a1fa-7cb203d0e927/resource) (`a493f163-1638-4819-a1fa-7cb203d0e927`)
- S21: [Mg-Al平衡相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d941598a-33fe-48e4-b875-66dd9edca2f4/resource) (`d941598a-33fe-48e4-b875-66dd9edca2f4`)
- S2: [TextNode328](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10cf2eb2-b9b5-43d2-b333-154cce3c09f5/resource) (`10cf2eb2-b9b5-43d2-b333-154cce3c09f5`)
- S24: [binary alloy phase diagrams__4d8db6f6f7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec5d76d5-15f5-48a9-a2a3-8b914acd476e/resource) (`ec5d76d5-15f5-48a9-a2a3-8b914acd476e`)
- S6: [Melting and Boiling Points of the Elements](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51e67732-a66d-4d21-95fb-780853acce6f/resource) (`51e67732-a66d-4d21-95fb-780853acce6f`)
- S17: [图 4.7 Mg-Al 二元相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/beca6970-1ebd-4209-af56-a237962d1431/resource) (`beca6970-1ebd-4209-af56-a237962d1431`)
- S9: [低压铸造镁合金研究现状及展望](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6726d07a-1630-442e-b2f0-ea00f6534692/resource) (`6726d07a-1630-442e-b2f0-ea00f6534692`)
- S26: [铝镁二元合金相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eeddd725-b079-4530-bf46-22324e5ce3b6/resource) (`eeddd725-b079-4530-bf46-22324e5ce3b6`)
- S27: [铝及铝合金的熔炼与铸锭](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb66719e-49dd-4c45-b8a3-38ea3cdf11e0/resource) (`fb66719e-49dd-4c45-b8a3-38ea3cdf11e0`)
- S16: [Al-Mg二元合金相图反应参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd253470-2bc3-47de-b0f0-fb392c5df12e/resource) (`bd253470-2bc3-47de-b0f0-fb392c5df12e`)
- S18: [铝及铝合金的熔炼与铸锭](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c68958fb-6b67-4dec-86ae-bdeb3e7be833/resource) (`c68958fb-6b67-4dec-86ae-bdeb3e7be833`)
- S7: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5949badf-dd84-4753-ab02-53f3e7b1676c/resource) (`5949badf-dd84-4753-ab02-53f3e7b1676c`)
- S28: [压铸耐热镁合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdbd6255-e48d-4f13-98c7-6b5c548bc78d/resource) (`fdbd6255-e48d-4f13-98c7-6b5c548bc78d`)
- S4: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47faecb2-2242-4160-8c36-efbe81d4b732/resource) (`47faecb2-2242-4160-8c36-efbe81d4b732`)
- S13: [AZ91D镁合金构件铸造残余应力有限元模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a72f606f-0bcb-4e7b-9cb9-c9195fef5e11/resource) (`a72f606f-0bcb-4e7b-9cb9-c9195fef5e11`)
- S14: [AZ91D镁合金构件铸造残余应力有限元模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1d43a14-1dea-4d03-b804-cd36e1b963d3/resource) (`b1d43a14-1dea-4d03-b804-cd36e1b963d3`)
- S10: [characterization of magnesium automotive components produced by super va__b8e1b095ec](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77b27e1c-57c2-4673-9476-02c703a52c20/resource) (`77b27e1c-57c2-4673-9476-02c703a52c20`)
- S19: [高硼含量的B4C_W_AZ91复合材料的制备与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d32d4853-b98f-4509-b846-5fa24cf40407/resource) (`d32d4853-b98f-4509-b846-5fa24cf40407`)
- S23: [Cp_AZ91D复合材料的制备与性能表征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9a8e808-0f1c-47fe-9135-2d31ebbeb167/resource) (`e9a8e808-0f1c-47fe-9135-2d31ebbeb167`)
- S5: [Cp_AZ91D复合材料的制备与性能表征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4dba8387-fb33-4d77-af74-22894ca06020/resource) (`4dba8387-fb33-4d77-af74-22894ca06020`)
- S11: [液态模锻与挤压铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7fbe0d7d-c9dc-4d8a-b522-3fff9266936b/resource) (`7fbe0d7d-c9dc-4d8a-b522-3fff9266936b`)
- S3: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3bd9aff3-24be-47ba-af75-be840c97844a/resource) (`3bd9aff3-24be-47ba-af75-be840c97844a`)
- S1: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/100e29c7-407a-47bd-b790-160919e84ed4/resource) (`100e29c7-407a-47bd-b790-160919e84ed4`)
- S22: [加压和速冷对镁-铝状态图的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de40887e-7428-4ef4-8b45-921349bd0408/resource) (`de40887e-7428-4ef4-8b45-921349bd0408`)
- S25: [die casting metallurgy__8f9e04f2f0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed1b2e70-2bfa-4010-b5da-9b0432dc6fa2/resource) (`ed1b2e70-2bfa-4010-b5da-9b0432dc6fa2`)