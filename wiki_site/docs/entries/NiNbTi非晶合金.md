---
version: "v1"
generated_at: "2026-06-18T16:50:08+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 22
  source_quality_score: 0.86
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

NiNbTi非晶合金是一种镍基三元过渡族金属非晶（金属玻璃），属于Ni基块体非晶的研究分支。通过调控Ni、Nb、Ti三组元的原子比例，可在特定成分区间内获得较高的非晶形成能力（GFA），从而通过急冷工艺制备出完全的玻璃态合金[[S8]]。该非晶合金近年来在铝合金熔体处理领域展现出独特的应用价值：以极低添加量引入铝熔体后，可在高温下原位晶化生成纳米晶，作为异质形核质点实现对铝基体组织的显著细化[[S20]]。

## 分类与体系归属

NiNbTi非晶合金属于镍基三元过渡族金属非晶体系，与非晶薄带、锆基块体非晶、铁基软磁非晶等分支并列，属于金属玻璃材料家族的一员[[S8]]。其基体元素Ni与非晶形成关键组元Nb、Ti的组合，使其兼具较高的非晶形成能力和在铝熔体中独特的反应潜力。二元Nb-Ni非晶体系即已展现出优良的非晶形成能力，第三组元Ti的加入可进一步拓展其非晶形成成分区间[[S5,S1]]。

## 成分与非晶形成能力

### 名义成分

NiNbTi非晶合金为三元体系，通过Ni-Nb-Ti三元素的原子尺寸匹配与非晶形成热力学条件耦合获得非晶态。具体最优非晶成分区间需通过非晶化驱动力（ADF）计算和实验验证确定，但现有研究已证实该体系可在一定成分范围内通过急冷实现完全非晶化[[S8]]。

### 非晶形成能力指标

非晶合金的非晶形成能力核心评价指标包括以下四项：

| 评价指标 | 符号 | 定义 |
|----------|------|------|
| 约化玻璃转变温度 | *T*<sub>rg</sub> = *T*<sub>g</sub> / *T*<sub>m</sub> | 玻璃转变温度与熔点之比 |
| 临界冷却速率 | *R*<sub>c</sub> (K/s) | 抑制晶态相析出所需最低冷却速率 |
| 临界最大铸造成形直径 | *D*<sub>c</sub> (mm) | 铜模铸造法可获得的完全非晶态最大直径 |
| 非晶化驱动力 | ADF | 固态溶体与玻璃态之间的能量差 |

其中体系的非晶化驱动力与可获得的最大块体非晶尺寸呈正相关关系[[S19,S27]]。已有测试数据表明，二元Ni<sub>60</sub>Nb<sub>40</sub>非晶合金的临界冷却速率仅为10² K/s，远低于多数非晶体系所需的10⁵~10⁶ K/s[[S5]]。

## 结构与热特征

### XRD无定形特征

完全非晶态的NiNbTi合金在X射线衍射分析中不存在尖锐的晶态布拉格衍射峰，仅在2θ=30°~50°区间呈现单一宽化的漫散射"馒头峰"，这一特征是判断合金是否形成非晶态的核心标识[[S4,S7]]。

### 热分析特征温度

非晶合金在差示扫描量热（DSC）升温过程中呈现以下关键热事件[[S14,S26]]：

- **玻璃转变温度 *T*<sub>g</sub>**：非晶固态向过冷液态转变的特征温度，在DSC曲线上表现为吸热台阶。
- **晶化起始温度 *T*<sub>x</sub>**：过冷液态发生晶化相变的起始温度，在DSC曲线上表现为放热峰的起始点。
- **过冷液相区宽度 Δ*T*<sub>x</sub>** = *T*<sub>x</sub> - *T*<sub>g</sub>：该温度区间内非晶合金可发生超塑性流变而不发生晶化。

DSC测试通用规范参考：样品量10~15 mg，氩气氛围保护，测温范围303~1273 K，可选升温速率10/15/20/25 K/min，使用Netzsch STA449C型设备[[S9]]。

### DSC/XRD联合表征参考图

典型非晶合金的联合表征如图所示：DSC曲线展现玻璃转变吸热特征和晶化放热峰，内嵌XRD图谱在2θ≈38°附近呈现非晶材料特有的漫散射包，无尖锐晶相衍射峰。此联合表征范式完全适用于NiNbTi非晶合金的鉴定[[S2]]。

![典型非晶合金联合表征：DSC热流-温度曲线与非晶特征XRD漫散射图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0628d3e0-0994-4d97-960a-8e8d1c1f2b76/resource)

## 高温晶化行为

NiNbTi非晶合金在高温铝熔体中可发生晶化反应，析出NiTi(B2)纳米晶相。纳米晶在原位生成后弥散分布于熔体内，与铝合金中关键相构成有利的共格关系[[S20]]。

**晶化析出相**：NiTi(B2)纳米晶。

**晶格错配度**：
- NiTi(B2)与α-Al基体：< 10%
- NiTi(B2)与共晶硅：< 10%
- NiTi(B2)与Mg₂Si析出相：< 10%

这一低错配度特征使晶化生成的NiTi(B2)纳米晶可作为α-Al、共晶硅和Mg₂Si三相的异质形核核心[[S20]]。

## 在铝合金中的作用机制

### 异质形核细化机制

NiNbTi非晶合金添加到铝合金熔体后，首先在高温下发生晶化生成NiTi(B2)纳米晶。由于这些纳米晶与α-Al基体、共晶硅和Mg₂Si析出相之间的晶格错配度均低于10%，三者均可在纳米晶表面以低能垒方式实现异质形核[[S20]]。这一机制不同于传统Al-Ti-B细化剂仅利用TiB₂颗粒作为形核质点的方式，NiTi(B2)纳米晶对硅相和析出相也具有直接形核能力。

### 细化效果实验数据

以下数据来源于Al-7Si-0.3Mg合金中添加**0.05 wt.%** NiNbTi非晶的对比实验[[S20]]：

| 微观组织特征 | 未添加NiNbTi | 添加0.05 wt.% NiNbTi | 细化效果 |
|-------------|-------------|---------------------|---------|
| α-Al晶粒平均尺寸 (μm) | 1610 | 205 | 细化87.3% |
| 共晶硅平均尺寸 (μm) | 26.6 | 12.6 | 细化52.6% |
| 共晶硅长径比 | 3.8 | 2.2 | 降低42.1% |
| 共晶硅形貌 | 长针状 | 短棒状 | 形态明显改善 |

### 时效析出与力学性能提升

NiTi(B2)纳米晶在时效热处理过程中同样促进β-Mg₂Si相的形核。由于NiTi相与铝基体之间热膨胀系数的差异，水淬期间在纳米晶附近产生大量位错；同时NiTi相在93.5°C时经历奥氏体→马氏体转变，固态相变亦产生大量位错。这些位错为合金元素提供更多扩散通道和析出相形核位点[[S6]]。

调控后Mg₂Si相和β''析出相的细化效果及力学性能对比[[S6]]：

| 性能指标 | 未添加NiNbTi | 添加0.05 wt.% NiNbTi | 提升幅度 |
|---------|-------------|---------------------|---------|
| β-Mg₂Si相平均尺寸 | — | — | 细化31.9% |
| β''析出相平均尺寸 | — | — | 细化47.6% |
| 室温疲劳强度 (MPa) | 92 | 112 | 提高21.7% |
| 120 MPa应力幅疲劳寿命 | 基准值 | ~5倍提升 | 大幅延长 |

> 测试条件：*R* = -1，*f* = 60 Hz，室温[[S6]]

### 枝晶细化示意图

晶粒细化后铝合金枝晶尺寸显著减小、形核数量大幅提升。图中展示的细化枝晶形貌可用于辅助理解NiNbTi非晶通过异质形核提升枝晶形核数量的作用机制[[S13]]。

![晶粒细化对枝晶搭接点的影响——细化晶粒的枝晶形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/508d5477-fbbd-4df1-99fc-d8f0a5bcd5d4/resource)

## 工艺条件

### 适用铝合金体系

当前有明确实验证据支撑的应用体系为**Al-7Si-0.3Mg**亚共晶铸造铝合金（类似A356体系）[[S20]]。该体系含硅相和Mg₂Si析出相，NiTi(B2)纳米晶对两者的细化均表现出色。

### 添加量与添加形态

已验证的有效添加量为0.05 wt.%（质量分数），以NiNbTi非晶合金形式加入铝熔体[[S20]]。相比商用Al-Ti-B细化剂常规添加量0.5~4 kg/吨熔体，NiNbTi非晶的用量处于极低水平[[S22]]。添加方式为非晶合金在高温铝熔体中原位晶化生成纳米晶，无需预先制备晶态中间合金。

## 自身性质与局限性

### 热稳定性和服役限制

非晶态合金属于热力学亚稳结构，其核心应用局限体现在两方面[[S24,S10,S3]]：
- **厚度限制**：常规急冷制备工艺下可获得的产品厚度受到严格限制，无法直接制备大尺寸块体构件。
- **晶化倾向**：受热后存在自发晶化的倾向，高温下长期服役时性能稳定性不足。这一特性意味着NiNbTi非晶在铝熔体处理场景中的功能恰好依赖于其受热晶化，作为非晶晶化型细化剂使用。

### 相图相容性

Al-Nb-Ti三元体系中存在稳定的三元化合物NbTiAl₃（名义成分41.8% Nb、21.7% Ti），该相可与Al基体以及TiAl₃、NbAl₃相平衡共存[[S12,S28]]。这一相图关系为NiNbTi非晶合金中Nb和Ti元素在铝熔体中的相容性提供了热力学支撑，避免了异质元素添加时形成有害界面相的风险。

### 非晶合金强度性能参考

块体非晶合金作为一类材料，其杨氏模量-拉伸强度关系显著优于钛合金、铝合金和不锈钢等传统晶态材料，高强度和良好的成形性为其作为特种添加剂提供了基础性能支撑[[S23]]。

![块体非晶合金与传统金属材料的杨氏模量-拉伸性能对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0ff5f14-75e7-4adb-a4cb-318514d7cef2/resource)

## 与常见细化剂的区别与联系

### Al-Ti-B系晶粒细化剂

商用Al-Ti-B系细化剂通过引入TiB₂颗粒作为异质形核核心和Ti溶质作为生长抑制因子起效，是目前应用最广泛的铝合金晶粒细化方案[[S18]]。但与NiNbTi非晶相比存在以下差异：

- **中毒效应**：Al-Ti-B在含Si、Zr等合金元素的铝熔体中存在细化剂毒化现象，导致形核能力下降[[S18,S22]]。Si、Zr等元素可替代Ti并偏聚于TiB₂颗粒表面，增大其与α-Al的晶格错配度。
- **衰退现象**：TiB₂颗粒在长时间保温后易发生沉降聚集，细化效率随保温时间延长而衰退[[S22]]。
- **细化对象单一**：Al-Ti-B主要细化α-Al晶粒，对共晶硅和析出相的细化作用有限；NiNbTi非晶晶化生成的NiTi(B2)纳米晶对α-Al、共晶硅和Mg₂Si三相均具有形核作用[[S20]]。
- **添加量差异**：Al-Ti-B常规添加量为0.5~4 kg/吨熔体[[S22]]，而NiNbTi非晶仅需0.05 wt.%（即0.5 kg/吨）。

### Nb对铝硅合金的细化效应

已有研究证实，单独向铝硅合金中添加铌（Nb）即可产生显著的晶粒细化效果[[S12]]。NiNbTi非晶中Nb元素的存在可能通过晶化后形成的含Nb相或Nb与Ti的协同作用进一步增强细化性能。

## Sources
- S8: [alloys and intermetallic compounds from modeling to engineering__edf223cde2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3518294f-90f1-4370-bb33-b7723df40d9e/resource) (`3518294f-90f1-4370-bb33-b7723df40d9e`)
- S20: [TextNode153](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/975e4e57-3075-462f-9b09-996368271175/resource) (`975e4e57-3075-462f-9b09-996368271175`)
- S5: [几种金属及合金的临界冷却速度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13a49ee3-f14c-4c40-bc1b-cbd56629a2cc/resource) (`13a49ee3-f14c-4c40-bc1b-cbd56629a2cc`)
- S1: [application of phase diagrams in metallurgy vol 2__6d6dee20cd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04e2213b-f1e3-4d9a-9f4b-0f3ff5d6d14d/resource) (`04e2213b-f1e3-4d9a-9f4b-0f3ff5d6d14d`)
- S19: [alloys and intermetallic compounds from modeling to engineering__edf223cde2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/925be478-8e9e-4c5b-b57f-6740ea135544/resource) (`925be478-8e9e-4c5b-b57f-6740ea135544`)
- S27: [alloys and intermetallic compounds from modeling to engineering__edf223cde2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4936edb-d62b-4eab-9b51-bf80c8024e63/resource) (`e4936edb-d62b-4eab-9b51-bf80c8024e63`)
- S4: [非晶合金药型罩压力铸造过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0bc57c33-5967-457a-a5fa-d8742e6c9345/resource) (`0bc57c33-5967-457a-a5fa-d8742e6c9345`)
- S7: [基于熔体注射成形工艺制备镁基非晶合金及其组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/335953cf-96de-4f09-8bc8-51753d434242/resource) (`335953cf-96de-4f09-8bc8-51753d434242`)
- S14: [微纳材料及加工前沿方向研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/526d6469-4489-4c63-99ad-d1dab02f36cb/resource) (`526d6469-4489-4c63-99ad-d1dab02f36cb`)
- S26: [微纳材料及加工前沿方向研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1d3c64d-60c1-4bac-a165-7b8e2164bdff/resource) (`e1d3c64d-60c1-4bac-a165-7b8e2164bdff`)
- S9: [铸型材质对锆基块体非晶合金性能的影响及铸造成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3799a1be-756c-4ff8-a275-de3c3e2a5ac0/resource) (`3799a1be-756c-4ff8-a275-de3c3e2a5ac0`)
- S2: [Al₈₆Ni₈Y₆ 260μm带材的DSC与XRD表征图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0628d3e0-0994-4d97-960a-8e8d1c1f2b76/resource) (`0628d3e0-0994-4d97-960a-8e8d1c1f2b76`)
- S6: [TextNode154](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ae7efe5-2b5f-48cb-8b14-52c2b2226303/resource) (`2ae7efe5-2b5f-48cb-8b14-52c2b2226303`)
- S13: [图1-4 b) 晶粒细化对枝晶搭接点的影响（细化晶粒的枝晶形貌）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/508d5477-fbbd-4df1-99fc-d8f0a5bcd5d4/resource) (`508d5477-fbbd-4df1-99fc-d8f0a5bcd5d4`)
- S22: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9e46e3e-91d4-4a90-9190-35167bdd9508/resource) (`a9e46e3e-91d4-4a90-9190-35167bdd9508`)
- S24: [普通高等教育机电类规划教材机械工程材料与热加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7c517ad-2582-49af-b47b-f752c57fe8d7/resource) (`b7c517ad-2582-49af-b47b-f752c57fe8d7`)
- S10: [机械工程材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b58db1e-74dd-4d76-bf59-522503137173/resource) (`3b58db1e-74dd-4d76-bf59-522503137173`)
- S3: [工程材料与热加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/073898d3-cabb-4aa8-9dfa-9f07a2b785cb/resource) (`073898d3-cabb-4aa8-9dfa-9f07a2b785cb`)
- S12: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4fdbffeb-024e-44b8-aad5-34349ecaa791/resource) (`4fdbffeb-024e-44b8-aad5-34349ecaa791`)
- S28: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb43821b-98be-4c2f-974b-730fcf627d8e/resource) (`eb43821b-98be-4c2f-974b-730fcf627d8e`)
- S23: [非晶合金与不同材料的弹性极限及强度对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0ff5f14-75e7-4adb-a4cb-318514d7cef2/resource) (`b0ff5f14-75e7-4adb-a4cb-318514d7cef2`)
- S18: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9248261c-3c9e-423e-89d6-f231f47f022e/resource) (`9248261c-3c9e-423e-89d6-f231f47f022e`)