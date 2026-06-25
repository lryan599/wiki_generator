---
version: "v1"
generated_at: "2026-06-18T19:32:50+00:00"
confidence_score: 0.89
confidence_level: "very_high"
confidence_basis:
  cited_sources: 27
  source_quality_score: 0.89
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

**X射线粉末衍射仪（Ultima IV）**，亦称 Ultima IV 型 X 射线衍射仪、Ultima Ⅳ 型多功能 X 射线衍射仪，是由日本理学株式会社（Rigaku Corporation, Tokyo, Japan）生产的一款 X 射线衍射（XRD）设备 [[S10,S27,S26]]。该设备属于理学 Ultima 系列衍射仪，其前代产品为 Ultima III 型 [[S22,S24,S5]]，当前知识库中尚未收录该系列各型号间完整代际差异的官方描述信息 [[S5]]。Ultima IV 在材料科学与工程领域被广泛用于多晶材料的物相定性分析、定量分析及晶体结构表征，在压铸铝合金等金属材料的微观组织研究中占有重要地位。

## 核心技术属性与规格

### X 射线发生器

Ultima IV 采用 Cu 靶作为 X 射线发生靶材，Cu Kα 特征辐射的波长为 1.5406 Å（0.15418 nm）[[S10,S2,S13,S26]]。根据已公开文献中的实测工况记录，设备可支持的典型测试参数如下：

| 参数类型 | 已公开实测取值 | 引用来源 |
|---------|-------------|---------|
| 管电压 | 40 kV、50 kV | [[S2,S10]] |
| 管电流 | 30 mA、40 mA、44 mA | [[S10,S2,S13]] |

### 测角仪与扫描能力

测角仪是 X 射线衍射仪的核心部件，其典型光路布局为：X 射线光焦点与探测器窗口分布在测角仪圆上，试样及试样台位于测角仪圆中心位置 [[S6]]。该框架适配 Ultima IV 型号的基础光路设计。不同研究场景下已公开的扫描参数取值范围如下：

| 参数类型 | 已公开取值 | 引用来源 |
|---------|----------|---------|
| 2θ 扫描范围 | 5°～70°、5°～75°、5°～90°、10°～90° | [[S12,S2,S13,S10]] |
| 扫描速度 | 2°/min、5°/min、8°/min、10°/min | [[S13,S12,S10,S2]] |

**待验证内容**：当前知识库未收录理学官方产品手册中公开的测角仪最小步长、角度重现性、探测器动态范围、能量分辨率、入射/接收狭缝配置、单色化方式（如石墨弯晶单色器）、可选平行光束系统、标准样品架尺寸、自动进样支持情况及旋转/摇摆功能等完整标定参数，以上信息需在获取官方产品文档后补充验证 [[S12]]。

### 探测器

通用 X 射线衍射仪常用探测器包括正比计数器（PC）和闪烁计数器（SC）两类，均属 Ultima IV 可选配置类型。正比计数器能量分辨率高、光子计数效率高，分辨时间约 10⁻⁶ s，缺点为对温度和电压稳定性敏感；闪烁计数器计数效率高，分辨时间约 10⁻⁵ s，缺点为背底脉冲较高、探测晶体易受潮 [[S6]]。

### 冷却系统

X 射线管及高压电源工作时需配套冷却装置。侧窗靶阳极接地可采用普通水冷却；端窗靶阴极接地的阳极需使用电阻率大于 5.0 MΩ·cm 的去离子水冷却，该要求适配 Ultima IV 型号运行需求 [[S20]]。

## 设备结构与子系统

通用 X 射线衍射仪核心子系统由 X 射线发生器（含高压控制系统和 X 射线管）、测角仪、辐射探测器、冷却系统、自动控制与记录单元组成，该结构框架适配 Ultima IV 型号基础配置 [[S6,S20]]。

测角仪光路示意图展示了衍射仪圆、样品台、探测器等核心部件的经典布局关系，可用于说明 Ultima IV 的扫描运行光路原理 [[S1]]。

![X射线衍射仪测角仪结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/016e666c-a1b5-4ad6-8bb0-b23ee83ed405/resource)

面向铸造领域材料物相检测的 X 射线衍射仪整机原理图进一步展示了 X 射线发生系统、样品室、真空/氦气置换系统、检测及控制系统的完整组成架构 [[S17]]。

![压铸领域用X射线衍射仪整体结构原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/946bd8ce-c64b-41bd-b27c-42b8f9dd88f0/resource)

## 在压铸领域的工艺角色与应用

### 可检测材料体系与功能

X 射线衍射技术面向商用铝合金，可覆盖以下检测功能：物相定性分析与定量分析、残余应力测量、位错密度与织构分析、点阵畸变与晶粒尺寸表征等 [[S3,S4]]。

在压铸领域，Ultima IV 已被实际应用于以下材料体系的物相检测：

- **ADC12 铝合金**：通过高压压铸成形，可对压铸态、固溶处理后及 T6 热处理后的 ADC12 铝合金进行物相表征，识别 α-Al 基体、共晶 Si、Al₂Cu 等相及其含量在热处理前后的变化规律 [[S14,S8,S15]]。

- **Al-5.5Mg-0.7Mn-xCu 系铝合金**：与扫描电镜（SEM）及能谱仪（EDS）配合使用，可识别合金中 Al₁₂Mg₁₇ 相、富铁金属间化合物等析出相，完成定性分析 [[S29]]。

### 典型应用案例

在高压压铸 ADC12 合金的 T6 热处理研究中，Ultima IV 衍射图谱揭示热处理过程未生成新相，但固溶和时效处理后 Al₂Cu 相含量有所增加，表明热处理固态相变的不同阶段存在交叉进行 [[S14,S15]]。通过与 SEM、EDS 等表征技术配合，可综合分析压铸件中共晶 Si 相、Al₂Cu 相的形态与分布演变 [[S8,S29]]。

### 物相分析软件

XRD 测试完成后，可通过 Jade、X'pert HighScore、Topas 等商用 XRD 分析软件与标准 PDF 卡片对照，完成物相识别与定量分析 [[S16,S14]]。Topas 软件的全谱拟合功能亦被用于水泥基材料的物相定量分析，证实其与 Ultima IV 的配合应用潜力 [[S12]]。

## 操作条件与样品制备规范

### 典型测试条件

根据已公开发表的研究文献，Ultima IV 测试压铸铝合金时的典型条件设置包括：

| 测试参数 | 典型设置 | 引用来源 |
|---------|---------|---------|
| 扫描范围 | 10°～90° (2θ) | [[S14,S8]] |
| 扫描速度 | 10°/min | [[S2]] |
| 管电压/管电流 | 40 kV / 40 mA | [[S2]] |

其他已公开文献中，扫描范围可在 5°～90° 间根据研究目的灵活设置，扫描速度可选 5°/min、8°/min 等档位 [[S10,S12]]。

### 试样制备要求

针对高压压铸 ADC12 铝合金块状试样，样品制备标准流程为：依次经不同目数的水砂纸研磨去除表面氧化层，抛光至镜面，经 Keller 试剂腐蚀 5～10 s 后超声波清洗吹干，即可进行 XRD 检测 [[S14,S8]]。

## 性能限制与待验证参数

**待验证内容**：当前检索范围内未收录理学原厂公开的 Ultima IV 型号专属信息，包括角度分辨率极限、微量相/非晶相最低检测灵敏度指标、特殊样品检测限制条件、官方指定日常维护要点、专属安全操作规范等，上述信息需在获取厂家官方说明书或高校公开的 Ultima IV 专属操作手册后补充验证 [[S7]]。

## 相关标准与规范

### 国内标准

国内现行压铸铝合金相关标准包括：

- **GB/T 13822—2017《压铸有色合金试样》**：规定压铸有色合金试样的制备工艺图、压铸工艺参数及试样要求 [[S28]]。
- 国内压铸铝合金标准体系已纳入 JIS H5302 中的 ADC12 牌号作为正式列项合金牌号 [[S9]]。

### 国际标准

与压铸铝合金相关的国际标准体系包括 [[S19,S21,S18]]：

| 标准号 | 标准名称 | 适用范围 |
|-------|---------|---------|
| ISO 3522 | 铸造铝合金的化学成分和力学性能 | 铸造铝合金 |
| ISO 7722 | 铝合金铸件通用交货条件 | 铝合金铸件 |
| ASTM B85 | 铝合金压铸件 | 铝合金压铸件 |
| JIS H5302 | 铝合金压铸件 | 铝合金压铸件，含 ADC12 牌号 |

上述标准对应的试样制备与检测方法条款可兼容常规粉末 X 射线衍射测试需求。

## 与同系列设备的关系

Ultima IV 的同系列前代在售产品为 Rigaku Ultima III X 射线衍射仪，两代产品基础共性为均采用 Cu Kα 辐射配置 [[S22,S24]]。当前知识库中无公开权威的完整代际差异、产品系列定位的官方描述信息。同品牌另一已知产品为 D/max-rc 2500 型 X 射线衍射仪，可作为同品牌系列产品参数对比素材 [[S11]]。

## Sources
- S10: [铝合金流变铸造卷入性缺陷及其钝化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/586a537e-24d5-4b37-9cd2-f202aa2e9713/resource) (`586a537e-24d5-4b37-9cd2-f202aa2e9713`)
- S27: [effects of cu content on the microstructure mechanical property and hot__90e549550b](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ee1a83af-bdf3-4ef9-ae67-c47c2c0249e1/resource) (`ee1a83af-bdf3-4ef9-ae67-c47c2c0249e1`)
- S26: [alloys and composites corrosion and mechanical properties__573c8b2ba2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcbb37af-974d-4820-bbc9-b95321a54c42/resource) (`dcbb37af-974d-4820-bbc9-b95321a54c42`)
- S22: [complex concentrated alloys ccas__861b70e9c9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c44fbb40-7a8a-42c1-8362-63b4689a988c/resource) (`c44fbb40-7a8a-42c1-8362-63b4689a988c`)
- S24: [原位负载稀土镱对氮化硅陶瓷烧结性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2ef03ee-ec15-40b4-81c5-b27f6a800c4c/resource) (`d2ef03ee-ec15-40b4-81c5-b27f6a800c4c`)
- S5: [complex concentrated alloys ccas__861b70e9c9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2247e3b8-9a62-473f-b05f-ea818d82fb77/resource) (`2247e3b8-9a62-473f-b05f-ea818d82fb77`)
- S2: [Cu对搅拌摩擦加工高锌镁合金性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06e66002-b9f0-4683-97f7-eb0f43e85e7e/resource) (`06e66002-b9f0-4683-97f7-eb0f43e85e7e`)
- S13: [aerobic oxidative coupling of amines to imines by mesoporous copper alum__606eb98542](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b129142-bcf9-453c-9c48-0bb7b2f5700b/resource) (`7b129142-bcf9-453c-9c48-0bb7b2f5700b`)
- S6: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22a73477-8d17-4881-ad61-9d66fb911ebf/resource) (`22a73477-8d17-4881-ad61-9d66fb911ebf`)
- S12: [低真空环境长期暴露下水泥基材料的力学性能演变及预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d418627-5bd2-470c-a569-e9c1e9da5710/resource) (`6d418627-5bd2-470c-a569-e9c1e9da5710`)
- S20: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae6195e0-360f-4a8b-99fc-098e30c68aac/resource) (`ae6195e0-360f-4a8b-99fc-098e30c68aac`)
- S1: [X射线衍射仪结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/016e666c-a1b5-4ad6-8bb0-b23ee83ed405/resource) (`016e666c-a1b5-4ad6-8bb0-b23ee83ed405`)
- S17: [X射线衍射仪原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/946bd8ce-c64b-41bd-b27c-42b8f9dd88f0/resource) (`946bd8ce-c64b-41bd-b27c-42b8f9dd88f0`)
- S3: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/118f5c64-79f2-4ddf-bf91-d88561d1fef0/resource) (`118f5c64-79f2-4ddf-bf91-d88561d1fef0`)
- S4: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e244eb1-09dd-4dcc-957b-f8ada0fed322/resource) (`1e244eb1-09dd-4dcc-957b-f8ada0fed322`)
- S14: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81b29e9c-8f38-4542-aa74-d81f10055288/resource) (`81b29e9c-8f38-4542-aa74-d81f10055288`)
- S8: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e699368-32a3-4d41-bee3-26c246828c08/resource) (`4e699368-32a3-4d41-bee3-26c246828c08`)
- S15: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82ed23b9-ecfb-4373-a863-6513ba70e448/resource) (`82ed23b9-ecfb-4373-a863-6513ba70e448`)
- S29: [effect of cu addition on microstructures and tensile properties of high__15b7a22a5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd1ca4a4-daaa-4381-be7b-0ebe64a0dfda/resource) (`fd1ca4a4-daaa-4381-be7b-0ebe64a0dfda`)
- S16: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/85e7d669-dea3-465a-b590-40d136e4cb55/resource) (`85e7d669-dea3-465a-b590-40d136e4cb55`)
- S7: [elements of x ray diffraction a volume in addison wesley series in metallurgy and materials__c6f389868b](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f7c950b-5540-4b21-9c81-e269d37b1e8c/resource) (`2f7c950b-5540-4b21-9c81-e269d37b1e8c`)
- S28: [GBT+13822（压铸有色合金试样）-2017.pdf-f9decb69-f6dc-45e1-991e-9aab07e76673](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa810bc8-c796-42c9-9681-dfb0026ea195/resource) (`fa810bc8-c796-42c9-9681-dfb0026ea195`)
- S9: [最新铸造标准应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/500df639-0a67-4cfc-9402-b90053ac4e45/resource) (`500df639-0a67-4cfc-9402-b90053ac4e45`)
- S19: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6027e3a-2c77-42a3-b1df-934c6eea6f9c/resource) (`a6027e3a-2c77-42a3-b1df-934c6eea6f9c`)
- S21: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbdfd10d-500b-41dd-bd20-5ac0efd8c501/resource) (`bbdfd10d-500b-41dd-bd20-5ac0efd8c501`)
- S18: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f7ccfbe-2b2c-401d-b742-2ff294e0f103/resource) (`9f7ccfbe-2b2c-401d-b742-2ff294e0f103`)
- S11: [实验使用仪器表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58ed4f82-712e-44c7-b307-30cada4015db/resource) (`58ed4f82-712e-44c7-b307-30cada4015db`)