---
version: "v1"
generated_at: "2026-06-18T10:59:33+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 30
  source_quality_score: 0.86
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述

一氧化碳（Carbon monoxide，化学式 CO）是压铸及铝合金铸造过程中常见的工艺气体组分之一。在铝合金压铸场景下，CO 主要来源于燃料不完全燃烧、有机物热分解及 CO₂ 与铝液反应，其在铝合金中几乎无溶解度，属于典型的卷入性气孔气相来源。

## 基本性质

一氧化碳为无色、无臭、无味的气体，分子量为 28.0101，熔点为 -205 ℃，沸点为 -191.5 ℃。其在水中溶解度极低，20 ℃ 时仅为 0.002838 g，但可溶于乙醇、苯等有机溶剂 [[S30]]。

*《新编铸造技术数据手册》*进一步收录了 CO 的标准状态物理性质参数，包括密度、燃点及空气中燃烧临界浓度等完整物性数据，可为安全管控提供参考 [[S35]]。

## 压铸中 CO 的生成机制

### 熔炼阶段来源

在压铸熔炼阶段，含碳燃料（如天然气、煤气）在氧气供给不足条件下发生不完全燃烧是 CO 的核心生成路径之一。CO 作为炉气的常规组分会存在于熔炼设备内部 [[S23]]。若燃料燃烧不充分，炉气中 CO 含量将显著上升。

### 型腔内来源

CO₂ 与高温铝液接触可直接反应生成 CO，这是型腔内 CO 的重要来源之一 [[S18]]。完整的反应式为：

**3CO₂ + 2Al → Al₂O₃ + 3CO↑**

在 1023 K 温度下，该反应的标准吉布斯自由能 ΔG° 为 -387.74 kJ/mol，说明热力学层面可自发进行 [[S24,S5]]。

### 涂料与粘结剂分解

压铸用模具涂层及脱模剂中所含的有机粘结剂组分，在高温铝液接触受热时发生热分解，可直接生成 CO、CO₂ 和烃类等挥发性气体。若涂层透气性不足或压铸模型腔排气不畅，生成的 CO 无法及时溢出，将滞留于金属液与涂层（或型壁）界面，形成气孔缺陷 [[S10]]。

综合而言，铝合金压铸场景下 CO 的主要生成途径包括：熔炼过程燃料不完全燃烧、脱模剂中碳质组分高温不完全氧化、型腔残留有机物热解产生 [[S39,S12]]。

### 各生成路径汇总

| 生成路径 | 具体来源 | 关键条件 |
|----------|----------|----------|
| 燃料不完全燃烧 | 熔炼炉中碳氢燃料氧化不足 | 空燃比偏低，氧气供给不足 |
| CO₂ 与 Al 液反应 | 型腔内裹挟的 CO₂ 气体接触铝液 | 高温（1023 K 以上即可自发） |
| 有机粘结剂/脱模剂热解 | 模具涂料、树脂砂粘结剂等受热分解 | 铝液高温接触，涂层透气性不足 |

## 与铝液的反应行为

### 常温至常规浇注温度区间

在常规 800 ℃（约 1073 K）以下温度区间内，CO 对熔融铝几乎没有作用，不会发生明显反应 [[S27]]。

### 高温条件下的反应行为

当温度升高至 1200 ℃（约 1473 K）以上时，CO 才会被铝液少量吸收，仅生成极微量的碳或碳化铝（Al₄C₃），且碳化铝产物仅在铝液被加热到 1500 ℃ 以上的试样中可被检测到 [[S27,S18]]。

### 1200 K 条件下的分子动力学模拟结果

分子动力学模拟进一步揭示了 CO 与铝在 1200 K 条件下的行为：将 CO 分子置于铝晶体表面加热至 1200 K 使铝完全熔化后，CO 分子与铝表面的距离从初始的 0.201 nm 增大至 0.466 nm，存在明显的脱离铝表面逸出的趋势，不会生成 Al₄C₃ 等反应产物 [[S5,S30,S27]]。

> 因此，1200 K 下 CO 几乎无法直接与熔融铝发生反应，会以气体形式逸出 [[S30]]。

### 热力学背景数据

*《中国材料工程大典 第18卷》*收录的铝液与各类气体反应热力学参数表，明确列出了 CO、CO₂ 等气体与铝液反应的平衡常数 Kp、标准状态自由能变化值及适用温度范围，可作为进一步定量分析的权威参考 [[S17]]。

不同温度（700 K 至 1200 K）、不同总压条件下 CO 的平衡分压与摩尔分数数据表明：CO 生成类吸热反应随温度升高产物占比增大，随压力升高产物占比降低 [[S21]]。

## CO 与铝合金中其他气体的对比

### 溶解性差异

在铝合金压铸场景下，不同气相组分的溶解行为存在本质差异 [[S33]]：

| 气体种类 | 在铝合金中的溶解性 | 缺陷类型归属 |
|----------|-------------------|-------------|
| H₂ | 可大量溶解，凝固时超过 95% 的溶解氢析出 | 析出型气孔（弥散性气孔） |
| N₂ | 几乎不能溶解 | 卷入性气孔 |
| CO | 几乎不能溶解 | 卷入性气孔 |
| CO₂ | 几乎不能溶解 | 卷入性气孔（可伴生 Al₂O₃ 夹杂） |
| CH₄ | 几乎不能溶解 | 卷入性气孔 |

CO 在铝合金中溶解度极低，几乎无法以溶解态进入铝基体，属于非析出型气体。被铝合金液裹挟后在凝固阶段滞留即可形成气孔，区别于铝合金中占气体总含量 70% 以上的溶解析出型氢气孔 [[S4,S33]]。

### 生成路径对比

| 气体种类 | 铝合金压铸全流程中的典型生成路径 |
|----------|-------------------------------|
| H₂ | 铝液与水汽反应、炉料油污/锈蚀分解析出 |
| N₂ | 充型过程卷入空气、炉内气氛带入 |
| CO | 含碳燃料不完全燃烧、铸型内碳氧反应 |
| CO₂ | 燃料完全燃烧、碳酸盐热分解 |
| CH₄ | 脱模剂、型砂粘结剂、燃料等有机物高温分解 |

## 对铸件质量的影响

### 气孔形成微观机制

CO 完全以分子态游离于铝液充型卷入的气相中，属于典型卷入性气孔的组成成分 [[S33]]。在压铸充型湍流条件下，型腔内的 H₂、N₂、CO、CH₄ 等气体会发生碰撞合并，共同形成体积更大的气泡，无法顺利上浮排出时同步滞留在铸件内部，协同提升气孔形成概率 [[S34]]。

### 气孔宏观特征

CO 滞留引发的铝合金气孔多分布在铸件近表面或皮下区域，形貌为梨形、椭圆形的非弥散型孔洞，孔壁光洁度高，和细小分散的析出型氢气孔存在明确区分特征 [[S20,S8]]。

以下图像展示了铝合金铸件加工后外表面的宏观气孔形貌，可作为 CO 引发的暴露型气孔的典型配图 [[S29]]：

![图2-64 铝合金铸件气孔缺陷示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4d5ec76-5358-4f5e-9883-cfd296cb10e3/resource)

另一幅相同来源的缺陷示意图可进一步用于气孔外观特征的对比识别 [[S36]]：

![图2-64 气孔缺陷示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef54884e-0fa6-4dbc-9c66-8c2f39243a20/resource)

### 对力学性能与气密性的影响

CO 引发的铸件气孔会减小有效承载面积，在气孔周边诱发应力集中，直接劣化铸件力学性能；同时气孔率升高会显著降低铸件的气密性指标 [[S8]]。

## CO 在铸造气体缺陷分类体系中的位置

CO 在铝合金中几乎无溶解度，无法以原子态固溶于铝熔体，完全不存在从铝液中随温度降低析出形成气孔的可能，**因此 CO 完全不属于析出型气孔来源** [[S33]]。

与反应型气孔的边界为：反应型气孔由铝液与铸型/介质直接化学反应原位生成，而压铸场景下的 CO 大部分来自充型过程卷入的游离气相，少部分来自型内碳与残余氧的次级反应，本质上不属于金属与介质直接反应生成的典型反应型气孔，**因此 CO 明确归类为卷入性气孔类缺陷的气相来源** [[S33,S22]]。

## 控制与缓解措施

### 熔炼环节控制

调整铝合金熔炼炉的空燃比，保证燃料完全充分燃烧，可将炉气中 CO 的生成量控制在极低水平，同步避免铝合金额外氧化 [[S38]]。

### 涂料与脱模剂选择

选用低有机物含量的压铸脱模剂或型腔涂料，可减少高温下有机物不完全分解产生的 CO 等气体总量，从源头降低型腔内的 CO 分压 [[S26]]。

### 排气系统优化

优化压铸模具排气系统，在分型面上开设深度为 0.005～0.010 英寸（约 0.13～0.25 mm）、宽度约 12.7 mm 的排气槽，可将型腔内裹挟的 CO 等气体顺利排出，大幅降低气孔缺陷生成概率 [[S6]]。

### 真空压铸

应用真空压铸工艺，在压射前对型腔执行抽真空预处理，可大幅降低型腔初始总气体含量，同步抽走腔体内残留的 CO 组分，显著降低铸件整体气孔率、提升致密度 [[S3]]。不同成形工艺气孔率差异可佐证低湍流/加压类成形工艺降低含 CO 卷入类缺陷的效果 [[S2]]。

## 检测与监测

压铸生产中可采用便携式燃烧效率监控仪，将带热电偶的采样探头插入熔炼炉烟道，直接抽取炉气检测 CO 含量，同步计算燃烧效率，指导空燃比调整，实现 CO 生成量的实时监测 [[S38]]。

依据 GB/T 37365—2019 压铸单元性能检测标准，压铸场景使用的压力传感器检测精度可达 ±0.1%、位移传感器检测精度可达 ±0.5%，可通过型腔压力分布、气体状态参数间接评估 CO 等气体的卷入风险 [[S16]]。

## 工业卫生与安全

CO 对人体具有强烈毒性，在铸造车间空气中 CO 的最高容许浓度不得超过 0.003 mL/L。熔化工部作为 CO 主要产生区域，必须设置可靠的局部吸风装置和废气净化设备，保障作业人员安全 [[S31,S1]]。

铝合金压铸生产需符合 JB/T 11735—2014《铝合金锌合金压铸生产安全技术要求》、GB 30078—2013《变形铝及铝合金铸锭安全生产规范》相关要求，其中明确熔化区域通风布局必须保证操作人员处于洁净空气侧，废气从压铸机上方最短路径排向吸气负压区，减少 CO 等有害气体在作业区的积聚 [[S19,S25]]。

## Sources
- S30: [163473_一氧化碳](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8f0babb-4c13-422a-a3b3-fda7e9f3eead/resource) (`a8f0babb-4c13-422a-a3b3-fda7e9f3eead`)
- S35: [一氧化碳的物理性质表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ee7d7cad-470c-4137-b4fc-7ec70d0354d2/resource) (`ee7d7cad-470c-4137-b4fc-7ec70d0354d2`)
- S23: [有色金属熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/862bcc39-c639-45a2-90b6-61a8bff75f79/resource) (`862bcc39-c639-45a2-90b6-61a8bff75f79`)
- S18: [有色金属熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/581167a0-b910-4b10-8eee-c9d3f23b45c9/resource) (`581167a0-b910-4b10-8eee-c9d3f23b45c9`)
- S24: [阳极气体传质对铝液中氧化铝夹杂形成影响机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a030c4e-3f9e-4f18-a52f-063456943849/resource) (`8a030c4e-3f9e-4f18-a52f-063456943849`)
- S5: [阳极气体传质对铝液中氧化铝夹杂形成影响机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/165061ec-617f-453f-b314-07473d97dda3/resource) (`165061ec-617f-453f-b314-07473d97dda3`)
- S10: [砂型铸造中涂料性能对铸件表面质量的影响机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27db8886-29a6-48ef-9e35-0e80099efdc5/resource) (`27db8886-29a6-48ef-9e35-0e80099efdc5`)
- S39: [实用有色合金铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9bf03cf-b406-45df-b08a-9b6f60444f41/resource) (`f9bf03cf-b406-45df-b08a-9b6f60444f41`)
- S12: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c29b170-25d4-43fa-9e86-bbed20b92d82/resource) (`2c29b170-25d4-43fa-9e86-bbed20b92d82`)
- S27: [aluminium teil a lieferung 2__65e70861fb](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9cf0c718-6ae3-4e84-a96c-9f41344437a8/resource) (`9cf0c718-6ae3-4e84-a96c-9f41344437a8`)
- S17: [表2.3-16 铝液和各种气体反应时的平衡常数和标准状态自由能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51368e12-c1fe-46ab-b243-7afff00de027/resource) (`51368e12-c1fe-46ab-b243-7afff00de027`)
- S21: [表 3-2 不同温度与总压下 CO 平衡分压及摩尔分数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7271a6cc-bc64-4a9d-8163-32da20f01b55/resource) (`7271a6cc-bc64-4a9d-8163-32da20f01b55`)
- S33: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4263141-0f30-4936-b3bd-c2eabdb99d3e/resource) (`b4263141-0f30-4936-b3bd-c2eabdb99d3e`)
- S4: [铝及铝合金熔铸工操作指南](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/119c1e9c-4969-4e14-997c-e44b7c167c4f/resource) (`119c1e9c-4969-4e14-997c-e44b7c167c4f`)
- S34: [castings principles the new metallurgy of cast metals__9ac1d4f9a8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf71e1ed-f45c-49f0-a6a3-51c85cc7c499/resource) (`cf71e1ed-f45c-49f0-a6a3-51c85cc7c499`)
- S20: [皮下气孔示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6713a6a6-40cc-4ed9-bff3-f848109383b2/resource) (`6713a6a6-40cc-4ed9-bff3-f848109383b2`)
- S8: [8128055_缩孔](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24c35ab8-9800-4f02-a072-2d528ae182cc/resource) (`24c35ab8-9800-4f02-a072-2d528ae182cc`)
- S29: [图2-64 铝合金铸件气孔缺陷示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4d5ec76-5358-4f5e-9883-cfd296cb10e3/resource) (`a4d5ec76-5358-4f5e-9883-cfd296cb10e3`)
- S36: [图2-64 气孔缺陷示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef54884e-0fa6-4dbc-9c66-8c2f39243a20/resource) (`ef54884e-0fa6-4dbc-9c66-8c2f39243a20`)
- S22: [casting copper base alloys__d5182d5c2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7cdb39b2-da52-4878-adaf-34f3e29e0ecf/resource) (`7cdb39b2-da52-4878-adaf-34f3e29e0ecf`)
- S38: [压铸冶金学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f91aef14-2f11-4a3f-b3bc-43c0978b483b/resource) (`f91aef14-2f11-4a3f-b3bc-43c0978b483b`)
- S26: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c8cbdad-d9e3-4790-9376-10b8ac6665ce/resource) (`9c8cbdad-d9e3-4790-9376-10b8ac6665ce`)
- S6: [basic engineering metallurgy__96f2179710](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18603377-7dc2-4223-a5e8-28e9e85d8879/resource) (`18603377-7dc2-4223-a5e8-28e9e85d8879`)
- S3: [压力铸造译文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d053e07-eed3-4f7e-82b0-984f9351399d/resource) (`0d053e07-eed3-4f7e-82b0-984f9351399d`)
- S2: [图5.4不同工艺气孔含量量化统计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/05d81a11-28e1-405a-b8db-e958c9fd4cee/resource) (`05d81a11-28e1-405a-b8db-e958c9fd4cee`)
- S16: [表 A.2 控制精度检测项目及检测仪器、量具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d218aa2-c1be-4f52-8c6e-ec5d88ea6685/resource) (`4d218aa2-c1be-4f52-8c6e-ec5d88ea6685`)
- S31: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab3e03a7-2d53-4f2e-8987-538eee32befd/resource) (`ab3e03a7-2d53-4f2e-8987-538eee32befd`)
- S1: [有色金属合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/010bb1e6-d926-4dd4-b644-9779563b6da3/resource) (`010bb1e6-d926-4dd4-b644-9779563b6da3`)
- S19: [压铸一体机常见的安全隐患](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/66dc9779-e090-461d-ab5e-0cc7b8f0a091/resource) (`66dc9779-e090-461d-ab5e-0cc7b8f0a091`)
- S25: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9408f1f3-dbc9-4314-b31d-7de574cf9ed2/resource) (`9408f1f3-dbc9-4314-b31d-7de574cf9ed2`)