---
version: "v1"
generated_at: "2026-06-21T06:05:26+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 46
  source_quality_score: 0.84
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

AlSi10Mg是一种以铝为基体、硅和镁为主要合金元素的亚共晶铝硅镁系铸造/压铸铝合金，典型成分为约90% Al、9% Si、1% Mg，允许含少量铁、铜、锌等杂质元素，兼具优异的铸造性能、力学性能与耐腐蚀性[[S31,S29]]。该合金属于4xxx系Al-Si合金，Si含量约10%，低于铝硅合金共晶点（约12.6%Si），属于亚共晶成分范畴[[S42,S40,S28,S56]]。AlSi10Mg同时是增材制造领域应用最广泛的主流铝合金牌号之一，符合ASTM F3318标准要求[[S29]]。

在中国压铸铝合金标准体系中，GB/T 15115-2009中YZAlSi10Mg（代号YL104）与AlSi10Mg牌号核心成分特征高度匹配[[S45,S51]]。按EN 1706标准，EN AC-43400（AlSi10Mg(Fe)）对应于AlSi10Mg牌号；ASME规范中亦确认EN AC-43000对应AlSi10Mg[[S27,S23]]。

## 牌号命名

国际标准中，铸造铝合金牌号由基体金属元素符号与合金元素符号及其名义百分含量组成。AlSi10Mg牌号表示：基体为Al，合金元素Si的名义含量为10%，Mg的名义含量小于1%[[S18]]。

![AlSi10Mg国际标准牌号构成示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73c84eed-b279-46af-8029-436ae95a7298/resource)

## 化学成分

AlSi10Mg合金的化学成分在不同标准体系下存在一定差异。以下列出GB/T 15115-2009中YZAlSi10Mg（YL104）与EN 1706中EN AC-43400的化学成分要求对比。

| 元素 | GB/T 15115-2009 YZAlSi10Mg (YL104)[[S45]] | EN 1706 EN AC-43400 (AlSi10Mg(Fe))[[S23]] |
|------|-------------------------------------------|-------------------------------------------|
| Si | 8.0~10.0 | 9.0~11.0 |
| Cu | ≤0.3 | ≤0.08 |
| Mn | 0.2~0.5 | ≤0.55 |
| Mg | 0.17~0.30 | 0.20~0.50 |
| Fe | ≤1.0 | 0.45~0.9 |
| Zn | ≤0.3 | ≤0.15 |
| Pb | ≤0.05 | ≤0.15 |
| Sn | ≤0.01 | ≤0.05 |
| Ni | — | ≤0.15 |
| Ti | — | ≤0.15 |
| Al | 余量 | 余量 |

Mg元素在合金中形成Mg₂Si析出相，是实现热处理强化的关键[[S29]]。Si元素可显著提升熔体流动性、降低热裂倾向与线收缩率[[S3]]。

## 物理性能

AlSi10Mg合金实测物理性能参数如下表所示，该数据为压铸工艺数值模拟的官方实测数据源[[S26]]。

| 参数 | 数值 | 单位 |
|------|------|------|
| 密度 | 2.68 | g/cm³ |
| 热膨胀系数（20~100℃） | 21.7 | 10⁻⁶/K |
| 比热容 | 0.753 | KJ/(Kg·K) |
| 室温热导率 | 147 | W/(m·K) |
| 熔化潜热 | 470 | KJ/Kg |
| 固相线温度 | 570 | ℃ |
| 液相线温度 | 602 | ℃ |

## 力学性能

### 传统铸造/热处理态

金属型铸造态AlSi10Mg合金经T6热处理后的实测性能[[S14]]：

| 性能指标 | 数值 |
|----------|------|
| 硬度 | 86~104 kgf/mm² |
| 0.2%残余屈服强度 | ≈250 N/mm² |
| 延伸率 | ≈10% |
| 电阻率（T6态） | 44.2 nΩ·m |

### SLM成形态与复合材料对比

SLM优化工艺制备的(Al₂O₃+SiC)混杂增强AlSi10Mg基复合材料，在扫描速度700 mm/s、扫描间距70 μm条件下达到最高致密度95.57%，对应抗拉强度为413 MPa，比同工艺制备的纯SLM成形AlSi10Mg合金的抗拉强度高4.5%[[S10]]。该最优复合材料试样延伸率为5.41%，最大屈服强度可达270 MPa（对应扫描速度900 mm/s）[[S10]]。

## 工艺特性

### 压铸工艺

AlSi10Mg作为Si含量约10%的亚共晶铝硅合金，高占比Si元素可显著提升熔体流动性、降低热裂倾向与线收缩率，压铸工艺适配性优异[[S24,S25]]。

**铸造性能优势**[[S6,S39]]：
- 线收缩率处于0.5%~0.6%区间，显著低于低硅铝合金，可减少压铸模具型面补偿余量，降低缩松缩孔发生概率
- 结晶温度区间约50℃，属于窄结晶间隔范畴

**浇注温度**：AlSi10Mg适配的常规浇注温度区间为630℃~660℃[[S57]]。温度过高会增大合金氧化、吸气概率，加剧对H13压铸模具的热冲击与粘模倾向；温度过低易产生冷隔、填充不良缺陷[[S57,S47]]。

**界面反应控制**：将合金中Fe元素含量控制在合理区间可显著降低粘模倾向，避免合金与H13压铸模具表面发生互扩散形成粘附层[[S3,S38,S52]]。

### SLM增材制造工艺

#### 粉末特性

气雾化制备的AlSi10Mg合金SLM专用粉末典型粒度分布为15~53 μm，平均粒径约42 μm，粉末球形度良好，仅少量粉末表面附着卫星颗粒，常规铺粉作业流动性优异[[S54,S13,S21]]。

#### 工艺参数窗口

已公开的SLM成形AlSi10Mg合金通用工艺参数范围[[S49,S43,S7]]：

| 工艺参数 | 数值范围 |
|----------|----------|
| 激光功率 | 160~200 W |
| 扫描速度 | 1000~1200 mm/s |
| 扫描间距 | 70~80 μm |
| 铺粉层厚 | 20~30 μm |
| 基板预热温度 | 80℃~100℃ |

采用相邻层扫描位相差67°的zigzag扫描策略时，可获得致密度99.5%以上的成形件[[S7]]。最优体能量密度区间通常为42.4~63 J/mm³，参数匹配合理时成形件致密度最高可达99.9%[[S13,S30]]。

#### 后处理

- **T6热处理**：SLM成形AlSi10Mg合金经T6热处理后，析出Mg₂Si强化相可实现力学性能调控，同时可消除部分内应力[[S41]]。时效温度升高时，合金抗拉强度、屈服强度先升高后降低，延伸率持续下降[[S35]]；固溶处理后停放时间延长，抗拉强度、屈服强度先小幅降低后趋于平稳[[S5]]。
- **热等静压（HIP）**：可有效闭合内部残余孔隙，降低整体孔隙率，提升延伸率；但过高的保温保压参数会导致共晶Si相粗化，引起抗拉强度小幅下降[[S36]]。

## SLM成形缺陷机理

AlSi10Mg合金存在三个核心本征特性直接影响SLM成形质量：对激光入射能量的吸收率仅为9%，热导率高达237 W/(m·K)，铝元素高温下极易与氧发生反应[[S46,S4,S37]]，是SLM过程中各类冶金缺陷高发的内在诱因。

### 球化

球化分为两类[[S37,S16]]：
- **大尺寸球化**：由熔体与基体润湿性不足、激光能量输入不足导致，在表面张力作用下液态金属包裹未熔粉末形成大球体
- **小尺寸球化**：由熔池不稳定引发的液滴飞溅生成，最终会造成铺粉不均、内部孔隙甚至刮刀损坏

### 孔洞

孔隙来源可划分为三种类型[[S16]]：
1. **未熔合孔洞**：激光能量不足导致的层间冶金结合不良，形状不规则，多出现在层间界面处或相邻熔道搭接位置
2. **凝固缩孔**：液态金属熔化量不足导致的收缩孔
3. **气孔**：粉末间隙气体、保护气卷入以及析出气体形成，形态多为规则球形

![SLM成形AlSi10Mg合金中的氢气孔与缩孔形貌对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/66679899-2748-45b8-9e92-d89a8c222492/resource)

### 氧化夹杂

氧化夹杂生成量随温度升高呈指数上升，可由公式 lg[O]ₘₐₓ = -6320/T + 2.734 计算平衡氧溶解度[[S1,S16]]。即使惰性保护氛围中仅残留0.1%的氧，也会生成Al₂O₃等多边形硬质夹杂物，劣化层间结合性能、降低致密度甚至诱发裂纹。夹杂和气孔可从几何形状上区分：气孔通常为球形，夹杂为多边形[[S16]]。

![SLM成形AlSi10Mg合金表面的氧化夹杂形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d960ac11-52b5-4741-9b33-4705899edcfe/resource)

### 裂纹

SLM成形过程中循环快速加热冷却引发的高温度梯度会持续积累热应力，当应力超过局部材料强度时就会诱发微裂纹，属于热应力型缺陷[[S37]]。

## 应用领域

AlSi10Mg合金凭借轻质高强、导热性能优异、可实现极复杂构型近净成形的特性，在以下领域有明确工业应用[[S33]]：

- **航空航天**：空客公司采用SLM工艺制备A350XWB机型的垂直尾翼AlSi10Mg支架，有效降低部件质量、缩减制造成本；该合金也大量用于SLM成形带随形冷却通道的航空结构支架[[S9,S33,S15]]
- **汽车制造**：用于制备轻量化薄壁结构件、减震部件、集成化散热壳体，依托其优异的流动充型性能和SLM工艺可一体成形复杂内部流道的优势[[S31,S29,S33]]
- **核工程**：适配特种复杂结构部件制备需求，可一体成形传统工艺难以加工的特殊构型内部冷却通道构件[[S33]]

## 关联材料对比

AlSi10Mg在四类典型Al-Si系合金中处于独特定位[[S9]]：

| 对比合金 | 特性差异 |
|----------|----------|
| AlSi7Mg | Si含量约7%，热裂倾向显著更高，需要完整T6热处理才能达到目标力学性能，整体成形窗口更窄[[S9,S20,S32]] |
| AlSi12 | Si含量10%~13%，接近共晶点，流动充型性能极佳，在传统压铸中应用广泛，但合金塑性、强度较低，在SLM领域的结构件应用占比远低于AlSi10Mg[[S20,S9]] |
| AlSi10MnMg | 在AlSi10Mg基础上添加约1%Mn元素，专为高真空薄壁压铸工艺开发，可通过调整Mn/Fe比值抑制针状富Fe相提升延伸率，但无法使用再生铝制备、成本较高，SLM增材制造适配性差[[S22,S50]] |

AlSi10Mg的核心优势：热裂倾向远低于AlSi7Mg，力学强度和可热处理强化性能优于AlSi12，可同时适配传统常压压铸和SLM等增材制造工艺，成形窗口最宽，兼顾制造成本和成形灵活性[[S9]]。

## Sources
- S31: [0230_23bb365dd533025d_AlSi10Mg](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9872230c-c0fb-416b-92ae-142614a7c746/resource) (`9872230c-c0fb-416b-92ae-142614a7c746`)
- S29: [0230_23bb365dd533025d_AlSi10Mg](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93fb1c44-9d05-4b09-afa9-288ae40c26d7/resource) (`93fb1c44-9d05-4b09-afa9-288ae40c26d7`)
- S42: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4bb5ba6-7e9a-481d-a943-6c68370e0fea/resource) (`b4bb5ba6-7e9a-481d-a943-6c68370e0fea`)
- S40: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aafece40-ed3f-4b9a-b68e-2b661a27ff9f/resource) (`aafece40-ed3f-4b9a-b68e-2b661a27ff9f`)
- S28: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/901f4416-2f24-4e85-b8d3-e9cded9122f8/resource) (`901f4416-2f24-4e85-b8d3-e9cded9122f8`)
- S56: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f459d633-53b4-4aa0-aaee-2cb55ba6d609/resource) (`f459d633-53b4-4aa0-aaee-2cb55ba6d609`)
- S45: [GB/T 15115—2009 压铸铝合金化学成分和力学性能表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bff2de31-aa7c-4fc4-942f-16e2c7c2142f/resource) (`bff2de31-aa7c-4fc4-942f-16e2c7c2142f`)
- S51: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce2d13e-413c-4061-9d2d-8e1edc9e49c7/resource) (`dce2d13e-413c-4061-9d2d-8e1edc9e49c7`)
- S27: [2019 asme boiler and pressure vessel code code cases boilers and pressure vessels__656b4c05d7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ad78415-95dc-4629-ba70-a1dd546fcb93/resource) (`8ad78415-95dc-4629-ba70-a1dd546fcb93`)
- S23: [欧盟标准压铸铝合金（EN1706:1998）的化学成分与力学性能指标](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c0353d9-a077-4754-99de-3e60f2568186/resource) (`7c0353d9-a077-4754-99de-3e60f2568186`)
- S18: [铸造铝合金牌号表示方法示例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73c84eed-b279-46af-8029-436ae95a7298/resource) (`73c84eed-b279-46af-8029-436ae95a7298`)
- S3: [铝合金减震塔压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10989aed-8f07-493d-a9c2-40ee2039e6e2/resource) (`10989aed-8f07-493d-a9c2-40ee2039e6e2`)
- S26: [表2-9 AlSi10Mg铝合金的热物性系数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89e6b3b1-04b1-4bb9-add7-a95faf08b905/resource) (`89e6b3b1-04b1-4bb9-add7-a95faf08b905`)
- S14: [铝合金结构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49e27be5-a64e-461e-be32-a8839bef22a5/resource) (`49e27be5-a64e-461e-be32-a8839bef22a5`)
- S10: [TextNode55](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28e18130-1a9b-40bc-8614-25fb2ec6e829/resource) (`28e18130-1a9b-40bc-8614-25fb2ec6e829`)
- S24: [Al-Si二元合金成分与铸造性能关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7cf1a282-1721-418b-964e-16e56baceb54/resource) (`7cf1a282-1721-418b-964e-16e56baceb54`)
- S25: [图 硅的质量分数对二元合金铸造性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82002201-fbe1-41e5-b4b8-acd324b06bfd/resource) (`82002201-fbe1-41e5-b4b8-acd324b06bfd`)
- S6: [车身真空高压压铸技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/17057928-a5e6-46ea-afc3-7dfe199f82df/resource) (`17057928-a5e6-46ea-afc3-7dfe199f82df`)
- S39: [图3.13(a) Al-9.8Si-2.6Mg-0.35Cu与A356合金收缩率随温度变化对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a44ce872-b090-42c0-abf0-066ee7c2a773/resource) (`a44ce872-b090-42c0-abf0-066ee7c2a773`)
- S57: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9be54da-d0a3-4681-893e-ad62ffa8b38f/resource) (`f9be54da-d0a3-4681-893e-ad62ffa8b38f`)
- S47: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d82f2e87-f3aa-44de-941a-e19a8d470a16/resource) (`d82f2e87-f3aa-44de-941a-e19a8d470a16`)
- S38: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a236297a-4f14-406a-8a61-a559a8b04c85/resource) (`a236297a-4f14-406a-8a61-a559a8b04c85`)
- S52: [压铸工艺及设备模具实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0cf11fb-a883-41c3-8766-a667e94234d3/resource) (`e0cf11fb-a883-41c3-8766-a667e94234d3`)
- S54: [工艺参数对铝合金点阵结构SLM成形表面质量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed95403b-7c78-483b-a901-ca5e6c28ac70/resource) (`ed95403b-7c78-483b-a901-ca5e6c28ac70`)
- S13: [工艺参数对铝合金点阵结构SLM成形表面质量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/442d57fd-07f4-48ed-9f42-f0c6e093357a/resource) (`442d57fd-07f4-48ed-9f42-f0c6e093357a`)
- S21: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78af0f9f-8d56-4496-a485-77fe7758fec5/resource) (`78af0f9f-8d56-4496-a485-77fe7758fec5`)
- S49: [表2.3 SLM成形AlSi10Mg合金工艺参数范围](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dbefc750-1fad-4ebd-902f-6c8bc08289cc/resource) (`dbefc750-1fad-4ebd-902f-6c8bc08289cc`)
- S43: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4bc67ec-6527-4925-9d23-0ff4b9876704/resource) (`b4bc67ec-6527-4925-9d23-0ff4b9876704`)
- S7: [TextNode28](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c94dd48-642f-4706-8b01-8679bab2c5b7/resource) (`1c94dd48-642f-4706-8b01-8679bab2c5b7`)
- S30: [工艺参数对铝合金点阵结构SLM成形表面质量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94f0c160-438d-476c-adbb-a75f383469ce/resource) (`94f0c160-438d-476c-adbb-a75f383469ce`)
- S41: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0b6d80a-3e50-45c3-a687-f15b8b9a98ad/resource) (`b0b6d80a-3e50-45c3-a687-f15b8b9a98ad`)
- S35: [硬铝时效温度对力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c476253-3cd5-4b28-ba3f-1d0fe2403f4d/resource) (`9c476253-3cd5-4b28-ba3f-1d0fe2403f4d`)
- S5: [图7-95 人工时效前的放置时间对力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13c0d0db-ad22-4660-b10f-14a4b86165b7/resource) (`13c0d0db-ad22-4660-b10f-14a4b86165b7`)
- S36: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9cb97511-8614-499b-b3a4-df6dcb0350d3/resource) (`9cb97511-8614-499b-b3a4-df6dcb0350d3`)
- S46: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cce35f1e-6e05-4047-9096-39f6a47d7a63/resource) (`cce35f1e-6e05-4047-9096-39f6a47d7a63`)
- S4: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/115a9018-e4fa-44e2-8956-cfb95cb00ede/resource) (`115a9018-e4fa-44e2-8956-cfb95cb00ede`)
- S37: [激光选区熔化成形铝合金的缺陷及控制方法研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9fff7c79-22c4-4434-8931-671b34467ea3/resource) (`9fff7c79-22c4-4434-8931-671b34467ea3`)
- S16: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f51ab8d-ab37-4323-9ded-7d8473be2b0a/resource) (`4f51ab8d-ab37-4323-9ded-7d8473be2b0a`)
- S1: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0551da2d-e207-43b3-8d56-7dc687917926/resource) (`0551da2d-e207-43b3-8d56-7dc687917926`)
- S33: [介观尺度下AlSi10Mg合金选区激光熔化过程数值模拟和实验研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/998aa947-4113-4497-bb33-7be2c7e8df85/resource) (`998aa947-4113-4497-bb33-7be2c7e8df85`)
- S9: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24140644-16fa-4c63-8699-c937c1c7c8b1/resource) (`24140644-16fa-4c63-8699-c937c1c7c8b1`)
- S15: [铝合金（AlSi10Mg）激光打印耦合流场模拟仿真](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b5652ed-e655-4533-8f95-c3da02980501/resource) (`4b5652ed-e655-4533-8f95-c3da02980501`)
- S20: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/763e6026-6d04-4838-bcc4-3e0fb6c7cfeb/resource) (`763e6026-6d04-4838-bcc4-3e0fb6c7cfeb`)
- S32: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9950e34e-48df-459a-bd8b-9b81f7228038/resource) (`9950e34e-48df-459a-bd8b-9b81f7228038`)
- S22: [高真空压铸铝合金的研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b3abf52-f943-4583-adc9-ab962b591d00/resource) (`7b3abf52-f943-4583-adc9-ab962b591d00`)
- S50: [压铸AlSi10MnMg铝合金中铸态缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcb0f541-2392-4d84-bd22-00d6d584de8d/resource) (`dcb0f541-2392-4d84-bd22-00d6d584de8d`)