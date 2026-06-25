---
version: "v1"
generated_at: "2026-06-18T17:50:13+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 46
  source_quality_score: 0.86
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 概述

霍尔-佩奇（Hall-Petch）晶粒细化强化理论是多晶金属材料力学性能领域最重要、应用最为广泛的理论之一。该理论阐明多晶材料的屈服强度与平均晶粒尺寸之间的定量关系——晶粒越细小，材料屈服强度越高。该理论于20世纪50年代初由E. O. Hall和N. J. Petch基于大量实验数据与位错塞积模型归纳提出[[S32,S5,S16]]，现已成为材料科学与工程领域细晶强化机制的核心定量表达。

## 定义与核心公式

霍尔-佩奇关系指出，多晶金属的屈服强度（σ_y）随平均晶粒直径（d）的减小而增大，其标准数学表达为[[S54,S33,S19,S36]]：

**σ_y = σ₀ + k · d^(-1/2)**

式中：
- **σ_y**：材料屈服强度（MPa）
- **σ₀**：位错在晶格内滑动所受的固有摩擦阻力（亦称派纳力），数值上相当于单晶体（无晶界）的屈服强度[[S12,S16]]；其值随材料成分与温度变化而改变
- **k**：晶界应力集中常数（亦称晶格障碍强度系数、Hall-Petch斜率），表征位错在晶界处塞积并触发相邻晶粒滑移的难易程度[[S54,S28,S5]]；k值与晶界结构、材料晶体类型直接相关
- **d**：平均晶粒直径（μm或mm）

公式表明σ_y与d^(-1/2)呈线性关系。指数-1/2是经过大量权威教材与实验数据验证的通用标准形式[[S33,S45,S36]]。此外，该关系可扩展至不同应变条件下的流动应力描述：σ_ε = σ_0ε + k_ε · l^(-1/2) [[S36]]。

## 微观机制

### 位错塞积模型

霍尔-佩奇关系的理论基础是位错塞积模型。在一个晶粒内，某滑移系的施密特因子较大时，位错源率先开动，位错沿滑移面运动至晶界处受阻[[S54,S29,S41]]。由于晶界两侧的晶粒取向不同、原子排列混乱，位错无法直接穿越晶界，遂在晶界前发生塞积[[S29,S3,S41]]。

位错塞积的力学特征如下[[S11,S2,S15,S18]]：

- 位错在障碍物（晶界）前形成分布梯度——越靠近障碍物，位错排列越密集
- 塞积群尖端对障碍物产生的有效集中应力是外加切应力的n倍（n为塞积位错总数），满足τ_有效 = n·τ_外加
- 塞积位错总数n与外加切应力τ、位错源至障碍物距离L、剪切模量μ及柏氏矢量b相关

### 公式推导逻辑

将位错塞积长度等效为晶粒直径d，则塞积尖端产生的高应力将触发相邻晶粒内的位错源开动。通过应力条件σ_d = (σ - σ_i)(d/r)^(1/2)整理，即可得到霍尔-佩奇屈服强度公式σ_y = σ_i + k_y · d^(-1/2) [[S31,S41,S53]]。其中k_y为材料常数，表征位错滑移越过晶界的难度。

晶粒细化提升强度的核心原理有两方面[[S56,S25,S29]]：
1. 晶粒细化大幅增加单位体积内的晶界总面积，强化晶界对位错运动的总阻碍作用
2. 细晶组织中参与塑性变形的晶粒数量增多，变形分布更均匀，应力集中程度降低，材料的韧性同步提升

![单滑移面内位错在障碍物前的塞积分布示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc4d61ef-3ffd-4692-bbf3-8546b037c90c/resource)

图：位错在障碍物前的塞积示意图，AB为滑移面，P为障碍物，位错在切应力τ作用下沿滑移面运动并在障碍物前形成从障碍物向远端逐渐稀疏分布的塞积群[[S40]]。

![刃型位错在障碍物前的塞积位置分布示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db7a7742-a559-4e2c-b8dc-69e076442cc5/resource)

图：刃型位错在障碍物前的塞积结构，位错从远离障碍物处向最靠近障碍物处逐渐加密，塞积尖端位错排列最密集[[S47]]。

## 铝合金中的霍尔-佩奇参数

### 典型Hall-Petch常数值

Armstrong等人1962年汇总的经典室温Hall-Petch常数表提供了包含面心立方铝合金在内的各类金属材料实测参数[[S13]]，该表作为铝合金霍尔-佩奇定量计算的权威参考数据被广泛引用。

铝合金专属参数的公开实验数据如下表所示：

| 材料 | k值 | σ₀说明 | 来源 |
|------|------|--------|------|
| 纯铝 | 0.065~0.12 MPa·√m | — | [[S44]] |
| Al-1050铝合金（小应变~0.2%） | ~25 MPa·μm^(1/2) | — | [[S17]] |
| Al-1050铝合金（应变~7%） | ~7 MPa·μm^(1/2) | — | [[S17]] |
| 超高纯铝（>99.99%） | 40~50 MPa·μm^(1/2) | — | [[S17]] |
| 免热处理压铸铝合金 | ~68 MPa·μm^(1/2) | σᵢ为纯铝强度 | [[S25]] |

铝合金的Hall-Petch斜率k整体远低于钢铁材料（约为钢铁的五分之一），因此在常规晶粒尺度下，晶粒细化对铝合金的强化效果弱于钢[[S44,S52]]。然而，当晶粒细化至微米级时，仍可获得可观的强度提升[[S25,S52,S44]]。

### k值对温度的依赖性

随环境温度升高，铝合金的Hall-Petch常数k值呈现逐步下降的变化规律[[S35]]。这是由于高温下晶界扩散滑移效应增强，逐步弱化了霍尔-佩奇强化效果[[S30]]。

## 压铸工艺中的应用

### 细晶强化在压铸场景的作用规律

晶粒平均尺寸越小，材料屈服强度越高；同时细晶粒可将外力分摊到更多晶粒上，降低局部应力集中，使塑性变形更均匀，从而在提升强度的同时同步改善塑性[[S51,S10]]。这一特性明显区别于砂型铸造晶粒粗大带来的变形不均与性能偏低问题。

### 压铸与砂型/重力铸造的晶粒特征对比

重力铸造合金的平均晶粒尺寸约390 μm，而高压压铸合金依靠高压辅助快速凝固的作用，平均晶粒尺寸仅约12 μm[[S51]]。压铸件晶粒分布更均匀，晶界占比大幅提升，细晶强化效应远高于常规砂铸工艺，最终实现强度与塑性的协同提升[[S51]]。

![A356铝合金砂型铸造件晶粒尺寸分布3D热图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb67ff08-aa7d-4b9d-a516-2508179bfa87/resource)

图：A356砂型铸造件全件晶粒尺寸分布云图，晶粒尺寸数值范围为0.01375~0.25739 cm，直观展现砂型铸造内部晶粒尺寸极不均匀的特征，可与压铸工艺的全件细晶粒分布均匀性形成对比[[S43]]。

### 壁厚效应与冷却速率

压铸工艺中，铸件壁厚是影响晶粒尺寸的核心因素。薄壁区域冷却速率快，晶粒细化效果显著。A356铝合金半固态压铸件的薄壁区域可获得近球形、轮廓圆滑的α-Al超细化等轴晶组织[[S21]]。

![A356半固态压铸件薄壁区域显微组织](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b48e7e7-0764-4bba-adf0-889a6491118e/resource)

图：A356铝合金半固态压铸件薄壁区域的微观组织，α-Al晶粒为近球形且轮廓圆滑，呈现薄壁快冷压铸工艺获得的超细化等轴晶结构（标尺100μm）[[S21]]。

冷却速率对A356铝合金性能的影响已被实验证实：冷却速率提升使二次枝晶臂间距显著降低，抗拉强度、屈服强度、断后伸长率均同步大幅提升，同时缩短后续热处理耗时[[S39]]。

### 晶粒细化工艺对压铸A356类合金的强化效果

| 工艺条件 | α-Al晶粒特征 | 抗拉强度 | 屈服强度 | 断后伸长率 | 来源 |
|----------|-------------|---------|---------|-----------|------|
| 未添加细化剂（压铸） | 粗大树枝状 | 276.1 MPa | — | 7.4% | [[S26]] |
| 添加0.25%Al-5Ti-1B（压铸） | 细小颗粒状/近球形 | 295.6 MPa（+7.1%） | — | 8.5%（+14.9%） | [[S26,S49]] |
| 半固态压铸A356 | 平均尺寸49μm | 提升19% | 提升15% | 提升107% | [[S39]] |

对于近A356成分的免热处理压铸铝合金（Si约9.84%），采用Al-5Ti-1B晶粒细化剂时，TiB₂颗粒作为稳定异质形核核心，可将粗大树枝状α-Al晶粒逐步转变为细小颗粒状/近球状晶粒。该体系下Ti-B合金最佳添加量为0.25%，添加量超过此值后继续增加不会进一步增强晶粒细化效果[[S27,S49,S26]]。添加0.25%细化剂后，压铸铝合金液流动长度增加10.9%，抗拉强度提高7.1%，断后伸长率提高14.9%[[S26,S49]]。

普通压铸件的常规晶粒尺寸通常处于1μm至100μm的微米级区间，常规服役温度多为-40℃至200℃，完全处于霍尔-佩奇效应的有效适用区间内。因此细晶强化工艺可稳定用于提升压铸件的屈服强度[[S24]]。

## 与其他强化机制的对比

铝合金中常见的强化机制包括细晶强化、固溶强化、析出（时效）强化和位错强化（加工硬化），各机制的原理与特点如下表所示[[S7,S22,S34,S6,S50,S8,S56,S3]]：

| 强化机制 | 核心原理 | 关键公式 | 特点 |
|---------|---------|---------|------|
| 细晶强化（Hall-Petch） | 晶界阻碍位错运动，细化晶粒增加晶界面积 | σ_y = σ₀ + k·d^(-1/2) | 唯一可同时提高强度与塑性的方法 |
| 固溶强化 | 溶质原子引发晶格畸变，与位错交互作用形成溶质气团钉扎位错 | Δσ_ss ∝ C^(2/3)（C为溶质浓度） | 提升强度同时保留良好塑性 |
| 析出（时效）强化 | 纳米级第二相粒子阻碍位错运动（切过或绕过机制） | 奥罗万机制 | 铝合金室温最高强度的强化手段 |
| 位错强化（加工硬化） | 塑性变形使位错密度大增，位错缠结阻碍后续滑移 | Δσ = α·G·b·ρ^(1/2) | 不可热处理强化合金的核心强化方式 |

### 协同作用

四种强化机制之间存在显著的协同效应[[S31,S29,S50]]：

- 细晶化为析出相提供更多晶界形核位点，调控时效析出动力学
- 固溶型晶粒细化元素（如Ti）可同时实现固溶强化与晶粒细化双重效果
- 预冷变形引入的高位错密度可同时贡献位错强化，并加速后续时效析出进程，大幅提升合金总强度

### 潜在竞争

在实际应用中需注意各强化机制之间的竞争关系[[S29,S50,S22]]：

- 过度细化晶粒可能导致析出相沿晶界连续分布形成无析出带，诱发晶间脆性，降低合金塑性
- 固溶元素含量超过固溶度阈值时会形成粗大非平衡第二相，反而削弱固溶强化效果
- 过高变形量引入的位错缠结会严重降低合金塑性与后续可加工性

## 适用性与局限性

### 常规适用范围

霍尔-佩奇关系的稳定适用晶粒尺寸范围为微米级（约1μm至数毫米的粗晶区间）[[S54,S9]]。在该区间内，基于位错的变形机制主导材料的塑性变形行为，晶粒细化可稳定提升屈服强度。当晶粒尺寸由100μm细化至1μm时，金属均匀变形量可提升3~5倍[[S9]]。

### 反霍尔-佩奇效应

当晶粒尺寸降低至纳米级（通常<10~20 nm）时，标准霍尔-佩奇关系出现失效，材料强度随晶粒进一步细化反而下降，这一反常现象称为**反霍尔-佩奇（Inverse Hall-Petch）效应**[[S14,S30]]。该效应已在纳米晶Cu、Pd、Ni-P及部分纳米铝合金体系中被实验观测到[[S14,S30]]。

反霍尔-佩奇效应的产生原因包括[[S14,S30]]：

- 晶粒小至无法容纳一个以上位错时，基于位错塞积的推导假设不再成立，Hall-Petch关系失效
- 晶粒极小时，晶界处任何弛豫过程均可使强度下降
- 晶粒尺寸趋近于零时，材料向非晶态转变，晶界强化效应完全消失

解释反霍尔-佩奇效应的主要模型包括：晶界蠕变模型、临界晶粒尺寸模型、改进的位错网模型和三晶粒结点模型，纳米晶材料的界面缺陷结构、界面过剩体积与界面过剩能也对该效应产生显著影响[[S14,S30]]。

反霍尔-佩奇效应的核心微观机制涉及扩散控制的晶界滑移、晶界蠕变、界面黏滞流动、晶界运动与旋转等[[S14,S30]]。

### 高温下的适用性变化

随温度升高至超过室温后，晶界扩散滑移效应逐渐增强，逐步弱化霍尔-佩奇强化效果[[S30]]。当温度达到扩散蠕变激活阈值后，材料硬度与强度随晶粒尺寸减小反而降低的趋势进一步凸显[[S30]]。然而，对于压铸铝合金而言，常规服役温度范围（-40℃至200℃）完全处于霍尔-佩奇效应的有效适用区间，且晶粒尺寸（1μm至100μm）也属于微米级常规区间，因此细晶强化可稳定发挥作用[[S24]]。

## 关联词条

与该理论紧密相关的技术与概念领域包括：

- **合金元素与细化工艺**：Sr变质处理、Ti-B晶粒细化剂（如Al-5Ti-1B）、异质形核
- **压铸工艺参数**：冷却速率控制、模具温度、充型压力——直接影响铸件晶粒尺寸
- **力学性能测试**：屈服强度、抗拉强度、断后伸长率、硬度
- **微观组织特征**：晶粒尺寸、二次枝晶臂间距（SDAS）、晶界面积
- **其他强化机制**：固溶强化、析出强化、位错强化——与细晶强化协同或竞争[[S25,S10,S51]]

## Sources
- S32: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c435213-1498-473e-9af5-7ac769277e1a/resource) (`9c435213-1498-473e-9af5-7ac769277e1a`)
- S5: [elements of physical metallurgy__5d4ee92381](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0cdf5efb-9c4d-4ac2-b30e-46f5811a0ee4/resource) (`0cdf5efb-9c4d-4ac2-b30e-46f5811a0ee4`)
- S16: [金属塑性成形理论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a14a547-931c-4e2e-a688-4e7f031394ae/resource) (`5a14a547-931c-4e2e-a688-4e7f031394ae`)
- S54: [热处理对Mg-10Gd-1.9Y-1Zn-0.5Zr铸造镁合金显微组织和力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5544c2f-7c61-46f2-a1c1-665624d2280e/resource) (`f5544c2f-7c61-46f2-a1c1-665624d2280e`)
- S33: [机械制造基础工程材料及热加工工艺基础上册第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a119e6bf-cb7f-4522-8b79-2e828d66c818/resource) (`a119e6bf-cb7f-4522-8b79-2e828d66c818`)
- S19: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7885322d-546b-47fd-a4a9-2b3c0134abde/resource) (`7885322d-546b-47fd-a4a9-2b3c0134abde`)
- S36: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad56cf71-c880-4935-b341-c7b4d73ddaef/resource) (`ad56cf71-c880-4935-b341-c7b4d73ddaef`)
- S12: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c8ec14a-cc7a-401b-89b4-0addfb5c4db1/resource) (`3c8ec14a-cc7a-401b-89b4-0addfb5c4db1`)
- S28: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9285cb31-736c-46ed-88fb-e18dd0d8d45a/resource) (`9285cb31-736c-46ed-88fb-e18dd0d8d45a`)
- S45: [机械制造基础上工程材料及热加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cdd70eb3-44e1-4428-a17b-43176e8df4f1/resource) (`cdd70eb3-44e1-4428-a17b-43176e8df4f1`)
- S29: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95450627-d690-4be0-823e-e6a389883db7/resource) (`95450627-d690-4be0-823e-e6a389883db7`)
- S41: [crystals defects and microstructures modeling across scales__f611fb073e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3108866-da94-4982-8072-8306ce6e1c61/resource) (`c3108866-da94-4982-8072-8306ce6e1c61`)
- S3: [铝合金压铸成型缺陷控制的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/043ac051-3ff3-4f41-8489-901bcddd0fc2/resource) (`043ac051-3ff3-4f41-8489-901bcddd0fc2`)
- S11: [crystals defects and microstructures modeling across scales__8a1f86ad1c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/381113e2-700b-40ca-93c3-6c6954ff5a79/resource) (`381113e2-700b-40ca-93c3-6c6954ff5a79`)
- S2: [细晶镁合金制备方法及组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0181d6be-6ef9-4380-ba6e-5e98fa040668/resource) (`0181d6be-6ef9-4380-ba6e-5e98fa040668`)
- S15: [金属热塑性成形基础理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49a22e3e-2b78-45a3-b5f4-14a4b79d7dfd/resource) (`49a22e3e-2b78-45a3-b5f4-14a4b79d7dfd`)
- S18: [jinshusuxingchengxingyuanli金属塑性成形原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bd59a55-17fc-4222-b60e-3ba866434b40/resource) (`6bd59a55-17fc-4222-b60e-3ba866434b40`)
- S31: [an introduction to metallurgy__70fe3feda9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a5586bc-a0e1-48d8-9086-355ea17a8f4a/resource) (`9a5586bc-a0e1-48d8-9086-355ea17a8f4a`)
- S53: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f518ad3c-5094-4334-86ad-2186500b40a9/resource) (`f518ad3c-5094-4334-86ad-2186500b40a9`)
- S56: [工程材料及金属热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8b71ce3-5b5e-44d7-8d49-be665cf48c35/resource) (`f8b71ce3-5b5e-44d7-8d49-be665cf48c35`)
- S25: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e14aec4-d528-4be3-b1ae-538358e23e29/resource) (`8e14aec4-d528-4be3-b1ae-538358e23e29`)
- S40: [位错在障碍前的塞积示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc4d61ef-3ffd-4692-bbf3-8546b037c90c/resource) (`bc4d61ef-3ffd-4692-bbf3-8546b037c90c`)
- S47: [刃型位错在障碍前的塞积示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db7a7742-a559-4e2c-b8dc-69e076442cc5/resource) (`db7a7742-a559-4e2c-b8dc-69e076442cc5`)
- S13: [表6-3 室温下Hall-Petch关系的常数数值（Armstrong等人，1962）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/426895f4-0102-48cf-a3cd-614ccafc7ff5/resource) (`426895f4-0102-48cf-a3cd-614ccafc7ff5`)
- S44: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccf750f7-e6d1-4de4-a4ab-6829a8a251c4/resource) (`ccf750f7-e6d1-4de4-a4ab-6829a8a251c4`)
- S17: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ddc64c9-d286-4c4c-9800-bd52ad76030b/resource) (`5ddc64c9-d286-4c4c-9800-bd52ad76030b`)
- S52: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3d55d34-f407-4cf7-8f5d-b435b763791c/resource) (`f3d55d34-f407-4cf7-8f5d-b435b763791c`)
- S35: [Hall-Petch常数ky随温度的变化（Al）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ac30810e-0c64-4e6d-bb41-48024073a558/resource) (`ac30810e-0c64-4e6d-bb41-48024073a558`)
- S30: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99389931-064c-4258-a9ae-f090a466d5b5/resource) (`99389931-064c-4258-a9ae-f090a466d5b5`)
- S51: [稀土成分对EA43合金组织、力学及导热性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0eacf8f-b082-49f3-8b0f-fa5d0a007e70/resource) (`f0eacf8f-b082-49f3-8b0f-fa5d0a007e70`)
- S10: [9694803_细晶强化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cfb290b-5634-496a-9b54-51a7a2e39f3a/resource) (`2cfb290b-5634-496a-9b54-51a7a2e39f3a`)
- S43: [(b) A356铝合金铸件晶粒尺寸分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb67ff08-aa7d-4b9d-a516-2508179bfa87/resource) (`cb67ff08-aa7d-4b9d-a516-2508179bfa87`)
- S21: [半固态压铸件薄壁处显微组织图（图5-9(d)）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b48e7e7-0764-4bba-adf0-889a6491118e/resource) (`7b48e7e7-0764-4bba-adf0-889a6491118e`)
- S39: [3D打印砂型对A356铝合金铸造工艺及铸件性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6983acb-135f-4430-8ab7-3f04314ed496/resource) (`b6983acb-135f-4430-8ab7-3f04314ed496`)
- S26: [TextNode4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90481912-16bf-4ac7-8a27-67c1dc93dd91/resource) (`90481912-16bf-4ac7-8a27-67c1dc93dd91`)
- S49: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e7e37bd4-100e-4953-960d-bb1207d16864/resource) (`e7e37bd4-100e-4953-960d-bb1207d16864`)
- S27: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91bbf8c3-52fb-41d9-98f4-3e6831aec0b4/resource) (`91bbf8c3-52fb-41d9-98f4-3e6831aec0b4`)
- S24: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cdd164d-d074-417c-bae9-60ae3a797650/resource) (`8cdd164d-d074-417c-bae9-60ae3a797650`)
- S7: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2169defe-1b11-474b-abde-bd148286f839/resource) (`2169defe-1b11-474b-abde-bd148286f839`)
- S22: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/805ad2ad-2943-4573-af4f-b2c9d9f60339/resource) (`805ad2ad-2943-4573-af4f-b2c9d9f60339`)
- S34: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a99b1346-a6a4-4ae1-80aa-f63ec5963f4c/resource) (`a99b1346-a6a4-4ae1-80aa-f63ec5963f4c`)
- S6: [铝合金和钛合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/158e1008-c8c6-473e-9581-d21c7067361c/resource) (`158e1008-c8c6-473e-9581-d21c7067361c`)
- S50: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e90051e0-0609-4bf9-a500-a57151cc1757/resource) (`e90051e0-0609-4bf9-a500-a57151cc1757`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28064e86-8216-45f8-a3f4-3869ee6d080d/resource) (`28064e86-8216-45f8-a3f4-3869ee6d080d`)
- S9: [5340005_变形量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a8c9435-922f-4fde-acba-4a8f9e63674c/resource) (`2a8c9435-922f-4fde-acba-4a8f9e63674c`)
- S14: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43083b23-5d12-4b4f-994f-e0e7d2819819/resource) (`43083b23-5d12-4b4f-994f-e0e7d2819819`)