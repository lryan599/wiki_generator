---
version: "v1"
generated_at: "2026-06-18T16:08:42+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 38
  source_quality_score: 0.84
  freshness_score: 0.89
  evidence_coverage_score: 1.0
---

## 定义与术语

在增材制造、选择性激光熔化（SLM）及粉末冶金相关文献中，“AlSi10Mg原粉”或“AlSi10Mg原始粉末”特指由气雾化等工艺直接制备、未经过任何成形热历史或循环使用的铝硅镁合金粉末，是实验研究中默认的初始基准原料[[S26,S17,S14]]。该术语与“AlSi10Mg粉末”、“AlSi10Mg virgin powder”、“AlSi10Mg raw powder”在首次使用场景下完全等价，其核心区别对象为经过多次熔融/回收的再生粉（recycled powder）[[S14,S1]]。工业级产品的名义纯度通常大于99.9%[[S14]]。

## 材料分类与牌号

AlSi10Mg属于4xxx系近共晶Al-Si合金，在铝合金粉床激光熔融（PBF-LB）增材制造领域拥有明确的标准定位。ASTM F3318《增材制造——成品性能——粉床熔融AlSi10Mg规范》专门针对该合金的粉末与成形件成分做出规定[[S23]]。在压铸领域，DIN EN 1706标准体系下对应的铸件牌号为EN AC 43400 AlSi10Mg(Fe)（Si 9–11%，Fe ≤0.55%）[[S9,S37,S38]]。中国标准GB/T 15115–2024《压铸铝合金》亦覆盖该类合金的分类规则[[S3]]。需指出，上述铸造牌号是针对熔融浇注的锭材或铸件，而非原粉本身，但两者的基础合金成分高度重叠。

## 化学成分

AlSi10Mg原粉的化学成分必须满足特定标准或供应商规范。综合ASTM F3318及同行研究，其主要元素及允许的杂质含量如下[[S4,S23,S32]]：

| 元素 | 典型含量 / 区间（wt%） | 常见上限（wt%） | 说明 |
|------|------------------------|------------------|------|
| Al   | 余量                   | —                | 基体元素 |
| Si   | 9.0–11.0               | —                | 接近共晶点，显著降低热裂倾向 |
| Mg   | 0.20–0.45 (部分规范至0.6) | —             | 与Si形成Mg₂Si强化相 |
| Fe   | ≤0.50                  | ≤0.55（铸件标准）| 杂质，过高易形成脆性β-AlFeSi相 |
| Mn   | ≤0.40                  | —                | 改善Fe相形态 |
| Ti   | ≤0.15                  | —                | 晶粒细化剂 |
| Cu   | ≤0.05                  | —                | 杂质 |
| 其他元素总和 | —                | ≤0.15            | — |

> 注：实际工业批次会根据激光吸收率、铺展性等微调；例如某一实测批次为 Al-10.1Si-0.4Mg-0.3Fe（wt%）[[S32]]。

## 粉末核心属性

### 粒径分布

AlSi10Mg原粉通常按应用场景划分为不同粒度区间，同一批气雾化粉末经过筛分离后可得典型规格[[S19]]：

| 粒度级 | D10 (μm) | D50 (μm) | D90 (μm) | 霍尔流速 (s/50g) |
|--------|----------|----------|----------|-------------------|
| 细粉（15–53 μm） | 24.4 | 37.1 | 58.3 | 无法测出（颗粒间摩擦过大）|
| 粗粉（53–105 μm）| 49.1 | 70.7 | 114.6 | 90 |

在SLM/LPBF工艺中，最常使用的规格为细粉级（15–53 μm或20–63 μm），以保证薄层铺展（典型层厚20–40 μm）和均匀的激光能量吸收[[S29]]。文献中出现的“平均粒径约26.4 μm”属于特定复合材料实验所选用的具体批次，并非通用工业规格[[S29]]。

### 颗粒形貌与物理性能

气雾化AlSi10Mg原粉的典型形貌与工艺性能如下：

| 指标                     | 典型值 / 范围                      | 来源 |
|--------------------------|-----------------------------------|------|
| 球形度                   | ≥90%                              | [[S27,S34,S35]] |
| 卫星粉占比               | <8%                               | [[S27,S34]] |
| 空心粉占比               | <3%                               | [[S27,S34]] |
| 松装密度                 | 1.1–1.4 g/cm³                     | [[S19]] |
| 振实密度                 | 1.4–1.7 g/cm³                     | [[S19]] |
| 霍尔流动性               | 30–90 s/50g（粗粉可测；细粉不可测）| [[S19]] |

形貌典型图像如下。

![气雾化法制备AlSi10Mg原粉的扫描电子显微镜形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccf4520b-9117-41da-8a22-d949c07a4594/resource)  
*图1：气雾化AlSi10Mg原粉的SEM形貌（圆球形，无明显卫星粉）[[S34]]*

![AlSi10Mg合金粉末SEM形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae68b77c-8945-4343-ab4e-df49f204a5da/resource)  
*图2：同一粉末的进一步放大SEM图像，可见少量卫星粉附着，整体保持高球形度[[S27]]*

### 物相组成

气雾化制备的AlSi10Mg原粉物相主要为α-Al固溶体基体、共晶Si相，以及少量Mg₂Si析出相[[S23,S40]]。X射线衍射图谱中，α-Al衍射峰强度远高于Si相，表明粉末以铝固溶体为主。

## 原粉与回收粉的差异

明确区分“原粉”与“回收/再生粉”在增材制造中至关重要。可量化差异主要体现在以下几项[[S24,S1,S8]]：

| 对比维度       | 原粉（virgin powder）                         | 多次循环使用的回收粉                     |
|----------------|-----------------------------------------------|------------------------------------------|
| 氧含量         | 初始约800 μg/g                                | 可上升至1900 μg/g                       |
| 颗粒形貌       | 高球形度，表面光洁，卫星粉少                    | 形变加剧，表面氧化层增厚                  |
| 粒度分布       | 正态分布、集中                                  | 分布偏移，细小碎片增多                    |
| 成形件Si析出相 | 细小、弥散                                    | 平均尺寸增大，时效>6h后粗化为片状，延伸率下降 |

回收粉的循环使用会导致成形件力学性能下降，特别是塑性损失，因此航空等高端应用场景对粉末循环次数有严格限制[[S14]]。

## 与压铸工艺的关联

常规高压压铸（HPDC）直接用于生产结构件的主流Al-Si-Mg系合金为AlSi10MnMg（Fe≤0.25%，含Mn抑制粘模），而非AlSi10Mg[[S2,S7]]。现有公开研究中未见 AlSi10Mg 原粉直接作为半固态压铸触变成形前驱体或粉末压铸原材料的规模化工业应用[[S28]]。

**AlSi10Mg原粉在压铸技术中的间接角色是作为金属增材制造的专用原料，用于制造压铸模具的核心功能部件——随形冷却镶块。** AlSi10Mg因其低热裂倾向和高导热性能，特别适合激光粉床熔融（LPBF/SLM）一体成形传统机加工无法实现的复杂内部冷却水道，从而提升模腔温度均匀性、降低局部热疲劳开裂风险并缩短压铸循环周期[[S23,S10,S5]]。模具使用寿命和冷却效率的改善直接作用于压铸生产，因此AlSi10Mg原粉是压铸模具制造的关键使能材料之一[[S22,S39]]。

此外，使用AlSi10Mg合金（ASTM或EN标准铸态）作为铸件材料时，真空压铸工艺已用于生产油底壳等汽车零部件[[S15]]。但此类铸件使用的是熔融浇注的铝液，并非粉末形态的“原粉”。

## 在实验研究中的角色

AlSi10Mg原粉是SLM/LPBF工艺参数开发与复合材料研究中使用最广泛的基准基体粉末[[S21]]。大量公开研究选择平均粒径约26 μm的球形气雾化AlSi10Mg粉，此粒径区间与常规SLM铺粉层厚（20–40 μm）高度适配，且能保证粉床铺展流动性好、激光能量吸收率稳定，避免因细粉团聚造成的打印缺陷[[S29]]。

作为“实验基体粉末”，其典型用途包括：  
- 纯基体穿孔或块体样件的SLM工艺参数优化；  
- 制备颗粒增强铝基复合材料（加入SiC、TiC、TiB₂、Al₂O₃、WC、碳纳米管、石墨烯等增强相）[[S21,S25,S41]]；  
- 与纯AlSi10Mg基体对比，评估增强复合材料的力学性能和热物理性能（如密度、热导率）[[S31]]。

例如，3 wt%纳米WC增强AlSi10Mg复合材料的抗拉强度可达464.1 MPa；而(TiB₂+TiC)双相混杂增强组分则使抗拉强度突破552.4 MPa且延伸率保持12%[[S21,S41]]。

## 安全性与存储

AlSi10Mg属铝基合金粉末，具有可燃性和爆炸风险：  
- 未涂层的铝粉属于危险货物43013类（UN 1396），遇湿易发生反应释放氢气，存在氧化自燃风险[[S33]]。  
- 悬浮粉尘云的爆炸下限为20–60 g/m³，粒径低于100 μm的粉末极易形成悬浮爆炸工况[[S43]]。  
- 工程上，在存储或使用前需将粉末置于120 ℃真空烘箱中烘干2 h，以去除表面吸附的游离水分，防止水分引发的氧化、气孔和安全隐患[[S13]]。

## 相关性能与热处理响应

虽然本条目关注的是“原粉”本身的属性，但由该粉末经SLM打印后获得的AlSi10Mg固体材料具备以下可热处理特性，间接反映了该合金体系的潜力：  
- 随固溶温度升高（450 ℃→550 ℃），成形件的拉伸强度和屈服强度降低，而延伸率显著提高，300 ℃退火时延伸率可达约13%[[S6,S12]]。  
- 标准T6处理（525 ℃固溶6 h+165 ℃人工时效7 h）后，共晶Si网发生粗化断裂，Mg₂Si相析出，塑性上升但强度较未热处理态下降[[S6,S11]]。  
- 经350 ℃及以上温度热处理后，共晶Si球化，Si从基体中析出，晶界逐渐消失，热导率随热处理温度升高而明显提升[[S30]]。  
- 铝基体表面的自氧化层及Si、Mg元素共同赋予AlSi10Mg良好的耐腐蚀性，使其适应海洋和航空航天等严苛环境[[S22]]。

## Sources
- S26: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9d5c759-829f-4e5b-836d-b93c53cef85b/resource) (`a9d5c759-829f-4e5b-836d-b93c53cef85b`)
- S17: [b0490 introduction to powder metallurgy__a36c9d0447](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73fb6f83-5fa5-4723-a246-e9a904e61912/resource) (`73fb6f83-5fa5-4723-a246-e9a904e61912`)
- S14: [additive manufacturing of metal alloys 1 processes raw materials and numerical simulation__200a158ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/573461b8-012e-4d0d-89fa-864491dabe21/resource) (`573461b8-012e-4d0d-89fa-864491dabe21`)
- S1: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03200d99-d096-4bcc-9e2b-edb022f495c8/resource) (`03200d99-d096-4bcc-9e2b-edb022f495c8`)
- S23: [0230_23bb365dd533025d_AlSi10Mg](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9872230c-c0fb-416b-92ae-142614a7c746/resource) (`9872230c-c0fb-416b-92ae-142614a7c746`)
- S9: [advances in processing and mechanical behavior in lightweight metals and alloys__ec5cc90182](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f6f4d20-ea6b-4fbf-b243-9eec70c8587b/resource) (`1f6f4d20-ea6b-4fbf-b243-9eec70c8587b`)
- S37: [表1 AlSi10Mg(Fe)_EN1706 (Cu≤0.3%) 化学成分及力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de2d65f1-37a0-49cd-a38a-bdc9f606da6c/resource) (`de2d65f1-37a0-49cd-a38a-bdc9f606da6c`)
- S38: [EN标准铸造铝合金的牌号与化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/def86e94-250a-4193-8625-1382e1ec83a9/resource) (`def86e94-250a-4193-8625-1382e1ec83a9`)
- S3: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/072272e1-f319-400f-9748-5a402ac4bb2a/resource) (`072272e1-f319-400f-9748-5a402ac4bb2a`)
- S4: [表2-1 AlSi10Mg粉末元素成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0876de89-d3a5-4215-9858-3af3ee681ae8/resource) (`0876de89-d3a5-4215-9858-3af3ee681ae8`)
- S32: [表2-2 AlSi10Mg合金粉末的化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0d0f1d9-d19b-417c-92ed-9c314d547d1e/resource) (`c0d0f1d9-d19b-417c-92ed-9c314d547d1e`)
- S19: [铝合金零件激光熔化沉积修复工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82d0dd69-d5dd-438d-a596-617dbc6a54ab/resource) (`82d0dd69-d5dd-438d-a596-617dbc6a54ab`)
- S29: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4bc67ec-6527-4925-9d23-0ff4b9876704/resource) (`b4bc67ec-6527-4925-9d23-0ff4b9876704`)
- S27: [图2.2 AlSi10Mg合金粉末形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae68b77c-8945-4343-ab4e-df49f204a5da/resource) (`ae68b77c-8945-4343-ab4e-df49f204a5da`)
- S34: [图5-1(d) 实验所用AlSi10Mg原粉的SEM形貌图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccf4520b-9117-41da-8a22-d949c07a4594/resource) (`ccf4520b-9117-41da-8a22-d949c07a4594`)
- S35: [15~53 μm粒径的AlSi10Mg合金粉末微观形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd245ed6-dc8a-4154-b821-cb46d3a4d0f7/resource) (`cd245ed6-dc8a-4154-b821-cb46d3a4d0f7`)
- S40: [图2.3 AlSi10Mg合金粉末的物相组成](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9ad350d-b07a-4196-8293-034a6a33bef6/resource) (`e9ad350d-b07a-4196-8293-034a6a33bef6`)
- S24: [additive manufacturing of metal alloys 1 processes raw materials and numerical simulation__200a158ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c32ea5c-cfe5-4a5d-958b-6c9473f2dc7d/resource) (`9c32ea5c-cfe5-4a5d-958b-6c9473f2dc7d`)
- S8: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a27f242-e40a-4e87-9a86-91a5192970f1/resource) (`1a27f242-e40a-4e87-9a86-91a5192970f1`)
- S2: [effect of microstructure and casting defects on the mechanical propertie__7978147656](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04118443-5a6a-4d2a-98e4-3cca5d9fa8ab/resource) (`04118443-5a6a-4d2a-98e4-3cca5d9fa8ab`)
- S7: [effect of microstructure and casting defects on the mechanical propertie__7978147656](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16c1ed73-bd29-47cc-acb6-048b6c3417b9/resource) (`16c1ed73-bd29-47cc-acb6-048b6c3417b9`)
- S28: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b036045d-1475-4f48-a042-bb9ffc59f4e6/resource) (`b036045d-1475-4f48-a042-bb9ffc59f4e6`)
- S10: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24140644-16fa-4c63-8699-c937c1c7c8b1/resource) (`24140644-16fa-4c63-8699-c937c1c7c8b1`)
- S5: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/115a9018-e4fa-44e2-8956-cfb95cb00ede/resource) (`115a9018-e4fa-44e2-8956-cfb95cb00ede`)
- S22: [0230_23bb365dd533025d_AlSi10Mg](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93fb1c44-9d05-4b09-afa9-288ae40c26d7/resource) (`93fb1c44-9d05-4b09-afa9-288ae40c26d7`)
- S39: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0aed05f-d5bb-471d-b9e3-dbb600e9fff1/resource) (`e0aed05f-d5bb-471d-b9e3-dbb600e9fff1`)
- S15: [油底壳压铸模结构示意图（图1-7）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6abd8d84-077f-45ce-a0fb-f4fbbeb017eb/resource) (`6abd8d84-077f-45ce-a0fb-f4fbbeb017eb`)
- S21: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/901f4416-2f24-4e85-b8d3-e9cded9122f8/resource) (`901f4416-2f24-4e85-b8d3-e9cded9122f8`)
- S25: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9cb97511-8614-499b-b3a4-df6dcb0350d3/resource) (`9cb97511-8614-499b-b3a4-df6dcb0350d3`)
- S41: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea448237-8428-4408-bc72-500f5788cc40/resource) (`ea448237-8428-4408-bc72-500f5788cc40`)
- S31: [图3-7 (c) (Al₂O₃+SiC)/AlSi10Mg的密度参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfe7e10f-3b91-4495-9aab-c1a3279bbfcb/resource) (`bfe7e10f-3b91-4495-9aab-c1a3279bbfcb`)
- S33: [铝合金粉材生产技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3ac94a4-fc85-436e-abcc-538f1419a22d/resource) (`c3ac94a4-fc85-436e-abcc-538f1419a22d`)
- S43: [铝与铝合金材料生产技术500问](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f70b9433-c5a1-4a4d-8499-a6476ab8903e/resource) (`f70b9433-c5a1-4a4d-8499-a6476ab8903e`)
- S13: [工艺参数对铝合金点阵结构SLM成形表面质量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/442d57fd-07f4-48ed-9f42-f0c6e093357a/resource) (`442d57fd-07f4-48ed-9f42-f0c6e093357a`)
- S6: [铝合金选择性激光熔化成形工艺控制与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13ca4ee0-dd2f-43d1-982f-993bb0e52e79/resource) (`13ca4ee0-dd2f-43d1-982f-993bb0e52e79`)
- S12: [图5.7 SLM成形AlSi10Mg合金不同退火温度下的力学性能，柱状图代表拉伸强度，蓝色球体代表延伸率](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37e1ed0f-0438-476c-97ce-3b6a4f0abd65/resource) (`37e1ed0f-0438-476c-97ce-3b6a4f0abd65`)
- S11: [effects of laser treatment on surface characterization and mechanical properties of alloys__0bf692855d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24879c4b-c63a-4921-89c3-6bcd9e579ee2/resource) (`24879c4b-c63a-4921-89c3-6bcd9e579ee2`)
- S30: [effect of heat treatment on thermal conductivity of aluminum die casting__4d37683de3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf4741f4-8e7b-4342-9eea-5126693b8997/resource) (`bf4741f4-8e7b-4342-9eea-5126693b8997`)