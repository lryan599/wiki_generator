---
version: "v1"
generated_at: "2026-06-18T20:33:46+00:00"
confidence_score: 0.84
confidence_level: "high"
confidence_basis:
  cited_sources: 49
  source_quality_score: 0.86
  freshness_score: 0.73
  evidence_coverage_score: 1.0
---

## 概述

V法铸造的正式中文名称为真空密封造型法，因英文“Vacuum”首字母得名，简称V法（V-process），亦称负压造型法、减压造型法，在工程资料中也常以V法造型、V法工艺、V法铸造等名称出现，术语指向完全一致[[S23,S47,S10]]。该工艺1971年由日本学者提出，是利用无粘结剂干砂在真空负压条件下紧实成型，无需添加水分或粘结剂即可获得稳定铸型的特种铸造技术，被誉为第三代物理硬化造型方法[[S35,S10,S23]]。V法属于砂型铸造范畴，不同于高压压铸，现有证据未记录V法与压铸融合的变体工艺[[S7,S16]]。

### 工艺原理与流程

V法铸造的核心机理为物理紧实：在带抽气室的砂箱内填充不含粘结剂的干砂，上下两面均覆盖塑料薄膜密封，真空泵抽出砂箱内空气使铸型内外形成约-0.04~-0.06 MPa的压差，砂粒在压差作用下相互挤压摩擦，维持铸型足够强度直至铸件完全凝固；释放真空后干砂自然溃散，铸件可轻松取出[[S23,S10,S9]]。浇注过程中EVA薄膜接触高温金属液即气化分解，但其密封作用随即由金属液自身和耐火涂料层取代，铸型在浇注及凝固全程维持负压状态，不发生塌型[[S11,S38,S51]]。

V法铸造全流程为辅料+干砂+真空覆膜输入，依次经制芯、造下箱、造上箱、涂料涂刷烘干、合箱、浇注、落砂、清理后取出成品铸件，配套闭环旧砂处理单元完成除尘、冷却后循环回用干砂[[S44]]。

![带旧砂闭环循环的完整V法铸造生产工艺流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed1b8116-da61-4422-b48a-5c559f4c7efe/resource)

V法造型的各道关键工序要求如下：

| 工序环节 | 技术要求与操作要点 | 主要来源 |
|---|---|---|
| 覆膜成型 | 将0.05~0.10 mm EVA薄膜加热至80~120℃软化，模板通过抽气孔抽真空使薄膜紧密贴附模样轮廓，深凹部位需增设抽气孔 | [[S35,S10,S22,S49]] |
| 刷涂料 | 在薄膜表面喷涂快干耐火涂料，要求对薄膜有良好润湿性与附着力，常温或≤50℃快速干燥，不含与薄膜反应组分，浇注后可从铸件表面完整剥离 | [[S8,S42,S10]] |
| 加砂与振动紧实 | 采用100~200目干硅砂，雨淋式均匀加砂，控制振动加速度1.2~1.5g，以水平振动为主，砂型硬度可达85~92 | [[S37,S49,S53,S10]] |
| 覆背膜·抽真空硬化 | 砂面刮平后覆盖密封薄膜，接通砂箱抽气建立约-400~-500 mmHg真空，干砂迅速硬化定型 | [[S53,S10]] |
| 起模 | 释放模板侧真空，保持砂箱侧真空，顶箱平稳起模，拔模斜度仅0°~-1°，无需敲击或振动模样 | [[S10,S53,S19]] |
| 合箱 | 检查修理铸型，下芯、安放冷铁，清理散砂，精准对位合箱并锁固砂箱，保持真空管路接通 | [[S10,S19]] |
| 浇注 | 铸型维持负压，浇注速度较常规砂型更快，先慢后快再慢，避免金属液飞溅冲毁薄膜；推荐底注或倾斜4°~12°浇注防止气孔 | [[S53,S10,S49,S39]] |
| 保压 | 浇注完毕后持续维持负压直至铸件完全凝固，防止铸型失稳 | [[S23,S19]] |
| 落砂 | 铸件完全凝固冷却后解除真空，干砂自然溃散，铸件轻易取出；干砂仅需过筛冷却至50℃以下即可回用，旧砂回用率≥95% | [[S10,S19,S31]] |

V法造型分步工序可概括为模型准备→薄膜加热软化→真空吸附成型→喷刷涂料→放置砂箱→加砂振动紧实→上表面覆膜抽真空→上下箱起模→合箱、放置浇口杯浇注→脱箱落砂→铸件后处理[[S14]]。

![V法造型分步工序流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59c06050-b1a9-462b-b78a-aac36a6656a1/resource)

### 关键设备与工具

V法生产线核心装备包括真空泵系统、砂箱、薄膜加热装置、振动紧实台、模板与覆膜机构及砂处理系统等，可配置单机式、台车移动式、梭动式、转台式等多种布局[[S31,S25,S6]]。

- **真空泵系统**：主流配置为水环密封真空泵，可耐受少量砂粒混入，稳定真空度可达约600 mmHg；常用型号包括SK-6、SK-12、SK-20、SK-30、SK-43，也可采用水环泵加罗茨泵组合降低能耗[[S1,S9,S37]]。  
- **砂箱**：采用四周抽气结构；标准尺寸有1200×1000×250 mm、2000×1600×300 mm、3300×1200×650 mm，可按需定制[[S9,S37]]。  
- **薄膜加热装置**：可选用回转式电加热器、热空气加热器或煤气辐射加热器，要求全区域加热均匀、温度可控；薄膜加热合格可凭肉眼判断——薄膜失去不透明度且中部自然下垂[[S35,S12]]。  
- **振动紧实台**：常见载重量2t、4t、6t，仅需一维上下方向振动，可兼用于消失模生产[[S9,S50]]。  
- **模板**：开设大量通气孔与中空负压箱连通，以利薄膜吸附；成型困难区域适当增加通气孔[[S35,S10]]。  
- **砂处理系统**：闭环循环，流程为造型砂斗→加砂造型→开箱→格子板→振动输送→提升入斗→磁选→过筛→沸腾冷却→提升入库，旧砂回用率达95%以上[[S31,S21]]。

![V法铸造闭环砂处理工艺循环流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c30ad3e-f5f7-43d9-8995-2a02460b3b09/resource)

### 关键工艺参数

| 参数项 | 数值范围 / 说明 | 主要来源 |
|---|---|---|
| 型砂真空度 | 主流推荐-0.04~-0.06 MPa（约-400~-500 mmHg）；生产中可稳定维持约-66500 Pa（-500 mmHg） | [[S9,S31,S37,S10,S53]] |
| 覆膜真空度 | 模板覆膜阶段控制-0.03~-0.04 MPa | [[S28]] |
| 浇注时真空度 | 维持在-0.05~-0.06 MPa | [[S28]] |
| 薄膜（EVA）加热温度 | 80~120℃，EVA最适延展温度95~115℃ | [[S10,S12,S22]] |
| 薄膜厚度（覆膜用EVA） | 0.05~0.10 mm；另有一来源给出覆膜推荐0.07~0.10 mm，通用总范围0.03~0.25 mm | [[S35,S22,S48,S45,S5]] |
| 型砂粒度（AFS范围） | 推荐100~200目（AFS约70~200），常用70/140或100/200目硅砂；高硅砂AFS 53.14、流动性15s | [[S37,S12,S18,S27]] |
| 振动加速度 | 1.2~1.5g | [[S49]] |
| 旧砂回用砂温 | ≤50℃ | [[S31,S34]] |
| 铸铁浇注温度 | 1300~1400℃ | [[S37]] |
| 铸件保压时间（壁厚15~20mm） | 浇注后保压≥5min | [[S37]] |

### 原材料

**型砂**：V法适用高耐火度干砂，包括石英砂、锆砂、铬矿砂、橄榄石砂；低熔点有色金属也可用钢丸或铁丸替代以加快冷却。石英砂因性价比高、来源充足应用最广；锆砂和铬矿砂耐火度更高且可避免硅尘[[S18,S42,S12]]。型砂粒度通常较普通砂型细，以便获得光滑表面并防机械粘砂[[S18]]。

**密封薄膜**：主流选用EVA（乙烯-醋酸乙烯共聚物）薄膜，其醋酸乙烯酯含量14%~19%，吹塑法制备，具有成型性好、热塑应力小、方向性低、发气量小且无毒等优点[[S20,S22]]。密封背部的薄膜不要求成型性，可选用较薄、较低规格的EVA薄膜[[S12,S22]]。

**涂料**：V法涂料喷涂于EVA薄膜表面，需常温或低温（≤50℃）快干、不流淌，对薄膜有良好润湿与附着力，干燥后形成坚固层，浇注后可成薄壳自行从铸件表面剥离；不得含有与塑料薄膜发生化学反应的组分，浇注前必须彻底干透[[S8,S42]]。

### 主要优点与局限性

**优点**[[S10,S19,S11,S37,S35]]

- 铸件尺寸精度高、表面光洁，表面粗糙度Ra较常规砂型提升约60%，可铸造壁厚仅3 mm的薄壁铸件，飞边毛刺少；
- 型砂不含粘结剂、水分及附加物，无需混砂，旧砂回用率≥95%，无大量废砂外排，有害废气产生量少，作业环境友好；
- 造型设备投入较湿砂型造型低约30%，配套动力消耗仅为湿砂型的60%；
- 拔模斜度0°~-1°，起模容易，砂型硬度85~92；
- 相比呋喃树脂砂工艺，每吨铸件直接生产成本更低，且无需额外投入粘结剂采购、废砂高温处置及尾气治理成本[[S2,S43]]。

**局限性**[[S19,S42]]

- 受EVA薄膜延伸率限制，不适用于形状过于复杂、深内腔占比过高的铸件；
- 不宜用于3 mm以下的极薄壁高充型要求铸件及大批量微型铸件的自动化高速流水线，其生产率低于传统高压湿砂造型线；
- 塑料薄膜覆膜成型及抽气管连接等环节部分仍需手工操作，机械化与自动化程度有待提升；
- 国内尚无V法造型装置系列技术参数标准，设备配套性有待统一。

### 典型应用

V法铸造广泛适用于工程机械配重/压铁、高锰钢衬板与筛板等耐磨件、泵阀壳体、出口工程机械转动体类结构件、矿车轮、大型薄壁铸铁平板、汽车后桥等[[S37,S11,S38,S30,S41]]。尤其适合对碳含量敏感的ZG20、ZG25、ZG30类低碳铸钢件，可避免消失模EPS气化带来的增碳缺陷[[S50,S41]]。生产实例显示，V法制造出口美国转动体类工程机械配件时，铸件内部无缩孔缩松等缺陷，外观质量优良，加工尺寸完全符合图纸要求[[S55,S28]]。

### 与消失模铸造的关系

**共通点**：V法铸造与消失模铸造均为无粘结剂干砂作为型砂、以真空泵抽气建立负压紧实铸型的物理造型工艺，两者可共用大部分核心装备，如水环式真空泵系统、震实台、落砂装置及旧砂处理线[[S50,S9,S29]]。中小厂家可根据铸件特征灵活搭配使用两种工艺以提高设备利用率[[S50,S29]]。

**核心差异**[[S4,S29,S33,S41]]

| 对比维度 | V法铸造 | 消失模铸造 |
|---|---|---|
| 铸型性质 | 空腔铸型——取模后获得型腔 | 实腔铸型——泡沫白模直接埋入砂内作为型腔 |
| 模型 | 可重复使用的金属或木质模板（带抽气箱与抽气孔） | 一次性EPS泡沫塑料白模 |
| 分型方式 | 上下箱水平分型，可下芯、放置冷铁 | 一箱式或组串浇注，无需取模 |
| 密封薄膜使用 | 上下箱型腔侧覆EVA膜，背部覆密封膜（薄膜消耗多于消失模） | 砂箱顶部覆密封膜 |
| 涂料 | 快干醇基涂料，喷/刷涂覆于EVA薄膜 | 涂料与泡沫匹配，通常水基浸/刷 |
| 典型缺陷 | 气孔、披缝、塌箱 | EPS气化引起的积碳、增碳、黑渣、皱皮 |

**适用场景选择**：V法更适配大面积薄壁铸件及低碳铸钢件，以减少批产白模消耗并避免增碳；消失模则更适合大批量、便于组串生产的高锰钢、中高碳合金钢铸件[[S41,S50]]。

在工艺体系分类中，V法可被纳入“干砂+负压”造型范畴，属于消失模铸造体系中的一个分支（以真空负压干砂造型为特征的第三代技术）[[S32,S33]]。

### 常见缺陷及对策

| 缺陷类型 | 产生原因 | 对策措施 | 主要来源 |
|---|---|---|---|
| 塌箱 | 金属液喷溅烧损密封薄膜；浇注断流；初始真空度不足；顶注时气体不易排出；砂粒摩擦系数偏低 | 箱口覆干砂保护薄膜；浇口杯持续充满不断流；大件采用底注；采用硅砂提升摩擦系数；适当提高初始真空度 | [[S17,S52]] |
| 表面粘砂 | 真空度过高；浇注温度过高；耐火涂层厚度不足或分布不均；型砂粒度过大 | 控制真空度于推荐范围；降低浇注温度；均匀增加涂层厚度；选用合适粒度型砂 | [[S40]] |
| 气孔 | 浇注速度过快，薄膜瞬时汽化气体无法及时逸出；浇注紊流卷入空气 | 平稳浇注避免紊流；适当提升涂层透气性；必要时倾斜4°~12°浇注降低液面上升速度；壁厚15~20 mm时浇注后保压≥5 min | [[S39,S37]] |
| 薄膜烧损 | 浇注热辐射提前大面积烧损密封薄膜，局部失压导致干砂溃散缺肉 | 确保金属液前沿推进速度大于薄膜受辐射烧损速度，避免局部大片薄膜提前气化 | [[S11,S38]] |

### 标准与规范

公开检索范围内未发现针对V法铸造独立的专项国际标准（如ASTM、ISO体系）。适用于常规铸造材料验收及质量体系的通用标准通常可沿用至V法铸件[[S15,S24]]。国内目前亦尚无V法造型装置系列技术参数的国家或行业专项标准[[S42]]。

## Sources
- S23: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70bcae51-2504-4734-a73d-b399ac2c7195/resource) (`70bcae51-2504-4734-a73d-b399ac2c7195`)
- S47: [0016_79b7208f6837dee4_砂铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef24af21-926c-4682-a1a5-18d31c060045/resource) (`ef24af21-926c-4682-a1a5-18d31c060045`)
- S10: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42e983dc-ed71-43a7-8061-1da853162205/resource) (`42e983dc-ed71-43a7-8061-1da853162205`)
- S35: [金属液态成型原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd1178b7-9141-4695-bd1a-80294de36013/resource) (`cd1178b7-9141-4695-bd1a-80294de36013`)
- S7: [5354165_真空压铸](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d8f5e8f-8b0c-4155-a0cf-736bd61f8a05/resource) (`2d8f5e8f-8b0c-4155-a0cf-736bd61f8a05`)
- S16: [7113892_压铸](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f5be48e-c793-4c53-9711-1b8a0c3e5a58/resource) (`5f5be48e-c793-4c53-9711-1b8a0c3e5a58`)
- S9: [TextNode57](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39ad6f60-7211-40ec-8db0-f74aa0011163/resource) (`39ad6f60-7211-40ec-8db0-f74aa0011163`)
- S11: [V法铸造工艺生产出口美国转动体试制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4370e72e-51f2-40e2-92f1-ae6bb52a786d/resource) (`4370e72e-51f2-40e2-92f1-ae6bb52a786d`)
- S38: [Ⅴ法铸造生产出口美国转动体试制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcd1454c-0e9a-4ab7-9473-cbd0f3a307b2/resource) (`dcd1454c-0e9a-4ab7-9473-cbd0f3a307b2`)
- S51: [V法铸造生产出口美国转动体试制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f32ec07a-85e2-45f7-8f77-f1816fc0bf24/resource) (`f32ec07a-85e2-45f7-8f77-f1816fc0bf24`)
- S44: [图1-2 (b) “V”法铸造工艺流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed1b8116-da61-4422-b48a-5c559f4c7efe/resource) (`ed1b8116-da61-4422-b48a-5c559f4c7efe`)
- S22: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6deacaf2-686b-4300-9c1c-253603c934f7/resource) (`6deacaf2-686b-4300-9c1c-253603c934f7`)
- S49: [特种铸造工学基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0ae1a60-217b-4bc8-afb6-24e96b643af9/resource) (`f0ae1a60-217b-4bc8-afb6-24e96b643af9`)
- S8: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/337d1b63-5ffb-43b8-98d9-98011125a3c9/resource) (`337d1b63-5ffb-43b8-98d9-98011125a3c9`)
- S42: [金属液态成型原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e72761fc-e46c-45f5-84f2-1ffe56ba1036/resource) (`e72761fc-e46c-45f5-84f2-1ffe56ba1036`)
- S37: [2885316_V法铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dccf3581-5dd3-4ee0-9f51-136adfb44878/resource) (`dccf3581-5dd3-4ee0-9f51-136adfb44878`)
- S53: [出国参观考察报告 西德、日本高压造型技术在铸纲中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9809706-e73b-4e07-823c-8149ab6eab94/resource) (`f9809706-e73b-4e07-823c-8149ab6eab94`)
- S19: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63272b21-7c94-4d1b-9585-afb8e053ce0a/resource) (`63272b21-7c94-4d1b-9585-afb8e053ce0a`)
- S39: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3ba3e55-4134-4af9-a8f0-37dd52b6bccc/resource) (`e3ba3e55-4134-4af9-a8f0-37dd52b6bccc`)
- S31: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6f28b6d-2b08-47da-a686-277ba78a8f7f/resource) (`b6f28b6d-2b08-47da-a686-277ba78a8f7f`)
- S14: [V法铸造工艺流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59c06050-b1a9-462b-b78a-aac36a6656a1/resource) (`59c06050-b1a9-462b-b78a-aac36a6656a1`)
- S25: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9774c8f8-3960-44a0-99b9-2e90a99357f6/resource) (`9774c8f8-3960-44a0-99b9-2e90a99357f6`)
- S6: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/207c79d0-862b-4eae-9599-d9b0d4d5a19e/resource) (`207c79d0-862b-4eae-9599-d9b0d4d5a19e`)
- S1: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f1e5ca5-946f-415f-b5c1-db942a71c68d/resource) (`0f1e5ca5-946f-415f-b5c1-db942a71c68d`)
- S12: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4fa49cd1-eecf-43d3-99d2-6b6ef7676f5c/resource) (`4fa49cd1-eecf-43d3-99d2-6b6ef7676f5c`)
- S50: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f26891cd-f34e-45d2-9d86-f9ea2f42948b/resource) (`f26891cd-f34e-45d2-9d86-f9ea2f42948b`)
- S21: [V法铸造砂处理工艺流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c30ad3e-f5f7-43d9-8995-2a02460b3b09/resource) (`6c30ad3e-f5f7-43d9-8995-2a02460b3b09`)
- S28: [Ⅴ法铸造生产出口美国转动体试制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3aaf503-8195-4503-b49c-3f41b8fd5126/resource) (`a3aaf503-8195-4503-b49c-3f41b8fd5126`)
- S48: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f03660ac-b4f5-4ef2-997f-338147ef3f19/resource) (`f03660ac-b4f5-4ef2-997f-338147ef3f19`)
- S45: [casting buyers guide for buyers designers engineers specifiers producers__71cb07c367](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed3aed66-ce7a-4978-bf2f-34d3cbb06d5e/resource) (`ed3aed66-ce7a-4978-bf2f-34d3cbb06d5e`)
- S5: [EVA塑料薄膜的物理性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2053bb0f-010b-4c73-83a1-347d82b0b797/resource) (`2053bb0f-010b-4c73-83a1-347d82b0b797`)
- S18: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62271643-3e0f-4fab-bcfa-458aa18eb1f6/resource) (`62271643-3e0f-4fab-bcfa-458aa18eb1f6`)
- S27: [图3-1 三种砂粒度AFS和流动性检测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a387ad64-faec-4016-8182-cb7e44877870/resource) (`a387ad64-faec-4016-8182-cb7e44877870`)
- S34: [特种铸造工学基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf741798-3c08-4276-bd81-ff6c2381e55e/resource) (`bf741798-3c08-4276-bd81-ff6c2381e55e`)
- S20: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b9ac965-b26c-4354-83c2-df180e55a366/resource) (`6b9ac965-b26c-4354-83c2-df180e55a366`)
- S2: [V-process与Furan工艺每吨铸件成本对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1778b9eb-9d92-41bf-8c46-f88ab9e4081b/resource) (`1778b9eb-9d92-41bf-8c46-f88ab9e4081b`)
- S43: [engineering equipment for foundries proceedings of the seminar on engine__879d587d16](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e95cafd4-5d88-42bb-b2ca-d2b0c782c715/resource) (`e95cafd4-5d88-42bb-b2ca-d2b0c782c715`)
- S30: [负压实型铸造及铸件质量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad0045aa-3090-4dc7-989f-04c83e881b7a/resource) (`ad0045aa-3090-4dc7-989f-04c83e881b7a`)
- S41: [TextNode56](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e579ed3c-b350-4e6d-acca-2b0084c82092/resource) (`e579ed3c-b350-4e6d-acca-2b0084c82092`)
- S55: [图四：转动体零件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd765c7d-1ce8-41fb-a5f7-262d2f6311e2/resource) (`fd765c7d-1ce8-41fb-a5f7-262d2f6311e2`)
- S29: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5679d5f-ae23-4be7-8c7a-7d15d2199bd4/resource) (`a5679d5f-ae23-4be7-8c7a-7d15d2199bd4`)
- S4: [消失模铸造与V法铸造工艺特性比较表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d510c13-4626-4e8f-98d1-7da0a9eb812c/resource) (`1d510c13-4626-4e8f-98d1-7da0a9eb812c`)
- S33: [消失模铸造及实型铸造技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf54c9ed-3be5-419a-8c90-2ac004b9af1a/resource) (`bf54c9ed-3be5-419a-8c90-2ac004b9af1a`)
- S32: [消失模铸造分类及工艺特点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bee503ce-1efc-4d50-88d4-8bc5b0871902/resource) (`bee503ce-1efc-4d50-88d4-8bc5b0871902`)
- S17: [普通高等教育“十三五”规划教材 特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/615d773e-e666-46fa-babc-b5bc565c0680/resource) (`615d773e-e666-46fa-babc-b5bc565c0680`)
- S52: [负压实型铸造及铸件质量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f70ea717-d8cc-41da-92c8-0bec35a47c04/resource) (`f70ea717-d8cc-41da-92c8-0bec35a47c04`)
- S40: [金属液态成型原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e434f580-96c7-4d75-910b-765c1dde2c22/resource) (`e434f580-96c7-4d75-910b-765c1dde2c22`)
- S15: [asme b1629 2012 wrought copper and wrought copper alloy solder joint drainage fittings dwv__b615ad273b](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5efa4ca8-bdd0-4fc7-9eef-8a7e5c289a91/resource) (`5efa4ca8-bdd0-4fc7-9eef-8a7e5c289a91`)
- S24: [asme b1622 2012 wrought copper and copper alloy solder joint pressure fittings__caea384876](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73220c2e-6915-4126-bcd4-f31a165bc247/resource) (`73220c2e-6915-4126-bcd4-f31a165bc247`)