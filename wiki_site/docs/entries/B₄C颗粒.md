---
version: "v1"
generated_at: "2026-06-18T14:29:59+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 31
  source_quality_score: 0.87
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

碳化硼颗粒（B₄C颗粒，boron carbide particles，缩写B4C）是一种黑色超硬陶瓷粉末，因其接近金刚石的极高硬度俗称“黑钻石”，是目前铝基复合材料中广泛使用的关键陶瓷增强相之一[[S4,S12,S19]]。在铝基复合材料体系中，B₄C颗粒具有高硬度、低密度和低线膨胀系数的特点，主要用于提高材料的耐磨性、刚性，并降低整体热膨胀系数[[S11,S12,S15]]。

## 材料分类

B₄C颗粒属于**陶瓷颗粒增强体**下的**碳化物增强子类**[[S4,S12]]。其晶体结构为斜方六面体（菱面体/菱形六方），共价键占比高达93.9%[[S4,S16,S19]]。

颗粒可按以下维度进一步分类[[S4,S8,S12,S16]]：
- **粒径分级**：纳米级、亚微米级、微米级
- **纯度分级**：工业磨料级、核屏蔽级、高纯度（≥99%）等级别

## 核心物化属性

### 基本物理性能
| 属性 | 数值 | 出处 |
|------|------|------|
| 密度 | 2.51~2.52 g/cm³ | [[S4,S8,S19]] |
| 熔点 | 2450 ℃ | [[S4,S8,S14,S19]] |
| 莫氏硬度 | 9.3 | [[S4,S8]] |
| 显微硬度 | >30 GPa | [[S19]] |
| 弹性模量 | 450~470 GPa | [[S19]] |

B₄C是仅次于金刚石和立方氮化硼的第三硬超硬材料[[S4,S14,S20]]。其在B-C-N体系超硬材料中占据核心组分之一的位置[[S32]]。下图展示了硼-碳-氮体系超硬材料的组分关系，明确将B₄C列为三大核心超硬组分之一[[S32]]。

![B-C-N体系超硬材料组分关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fea6607d-d08b-4351-b989-f79b4325c227/resource)

### 化学稳定性
- 常温下不与酸、碱发生反应[[S4,S14]]
- 1000 ℃以下可抵抗空气腐蚀[[S4]]
- 在较高温度的氧化气氛中易于氧化[[S4,S14,S20]]
- 不得与热或熔融黑色金属直接接触[[S14,S20]]
- 常规使用温度限定在980 ℃以下[[S14,S20,S22]]

> **证据不足声明**：碳化硼颗粒的热膨胀系数和热导率在现有公开来源中缺乏可信的定量数据，现有文献仅指出其热膨胀系数处于较低水平[[S4,S19]]。

## 润湿性与界面反应

### 润湿性
B₄C颗粒与熔融铝合金之间存在天然的润湿困难问题，这是搅拌铸造等液态工艺面临的核心障碍之一[[S23]]。为改善润湿性，已发展的方法包括：
- **添加K₂TiF₆卤盐**：将B₄C颗粒与K₂TiF₆共同预热后加入铝熔体[[S1]]
- **添加Ti元素**：Ti可在B₄C颗粒表面生成厚度为80~180 nm的Ti-C和Ti-B保护层，有效改善两相润湿性[[S1]]
- **施加高压**：挤压铸造等高压工艺可促进熔体对颗粒的润湿[[S6,S21]]

### 界面反应与抑制
当B₄C颗粒与铝熔体在700 ℃以上长时间接触时，界面处会发生反应生成**Al₄C₃脆性相**，这是有害界面产物，会降低复合材料的界面结合强度[[S25]]。

抑制界面反应的策略包括：在铝熔体中添加Ti元素，利用生成的Ti-C和Ti-B保护层阻断铝与B₄C的直接接触，从而抑制Al₄C₃的生成[[S1]]；以及通过压力浸渗等工艺缩短高温接触时间[[S6]]。

下图为铝基复合材料中表面包覆Zr-Ti富集保护层的B₄C颗粒微观形貌，该保护层可有效避免颗粒与熔融铝发生有害界面反应[[S30]]。

![表面包覆Zr-Ti防护层的B₄C颗粒在铝基复合材料中的微观形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcbe63f5-a17c-4a3a-8006-731e6be74286/resource)

## 制备工艺

### 搅拌铸造
搅拌铸造通过机械作用克服B₄C颗粒与铝熔体之间的润湿阻力，将颗粒分散至基体中，具有成本低、适合大规模量产的优点[[S9,S28]]。

常规搅拌分散工艺参数[[S17]]：
| 参数 | 量值 |
|------|------|
| 搅拌转速 | 300 rpm |
| 熔体温度 | 730±5 ℃ |
| 颗粒纯度 | 95.4% |

搅拌后可直接浇注成型。工业常规添加体积分数为10%~15%[[S1,S17]]。

### 超声辅助分散
利用20 kHz~18 kHz频率超声波引发的空化效应，可在6~10 s的作用时长内破碎B₄C颗粒的团聚体，提升分散均匀度[[S10]]。

### 压力浸渗
在70~100 MPa的外加压力作用下，铝熔体可渗入B₄C颗粒预制体中，有效提升两相润湿性，缩短高温接触时间以降低界面不良反应概率，从而获得高致密度、低孔隙率的复合材料[[S6]]。

### 挤压铸造/压铸
挤压铸造工艺中，高压可促进熔体对颗粒的润湿，快速凝固可细化基体晶粒。随B₄C添加量提升，复合材料晶粒尺寸减小，位错密度升高[[S21]]。

B₄C/AA7075挤压铸造的典型工艺窗口[[S2]]：
| 参数 | 范围 |
|------|------|
| 挤压压力 | 50~150 MPa |
| 熔体温度 | 700~800 ℃ |
| B₄C添加量（质量分数） | 6%~10% |
| 最优力学性能 | 硬度218 VHN，抗拉强度412 MPa |

### 适配的铝合金体系
可用于B₄C增强的铝合金包括铸造铝合金（A356、A357、359等）及变形铝合金（2024、6061、7075等）[[S3]]。

下图为A356-5 vol.% B₄C铸态复合材料抛光后的金相显微组织，清晰展示了铝基体与黑色B₄C增强颗粒的分布状态[[S31]]。

![A356-5vol.% B₄C铸态复合材料抛光态微观组织](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd0f4fc9-b92e-498c-84ad-f03f3a6d4cd1/resource)

## 缺陷与失效机制

### 颗粒团聚与分布不均
B₄C颗粒添加量过高时，易出现颗粒团聚和分布不均的缺陷，引发应力集中，严重时可导致颗粒与铝基体的界面脱粘失效[[S23]]。

### 熔体流动性与充型能力下降
向铝合金熔体中添加B₄C颗粒会提升熔体整体黏度，降低铝合金的流动性，导致充型能力下降，不利于复杂薄壁铸件的完整充型。该效应随B₄C含量提升而加剧[[S23]]。

### 有害界面反应产物
B₄C与铝熔体在700 ℃以上长时间接触会生成Al₄C₃脆性相，降低界面结合强度[[S25]]。

### 高温服役后的微观组织演化
B₄C/Al复合材料在高温老化后，颗粒周围会生成反应层并出现局部聚集相，影响材料韧性。下图为不同老化温度处理后的复合材料微观形貌对比[[S7]]。

![不同老化温度下B₄C增强铝基复合材料的微观形貌特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4003a6d6-1ee9-4b0b-b1c3-d0724a1efbb6/resource)

## 与SiC、Al₂O₃颗粒的对比

三种常用陶瓷增强体的基本性能对比[[S5,S8,S12,S18,S24,S26]]：

| 增强体 | 密度 (g/cm³) | 莫氏硬度 | 熔点 (℃) | 典型应用场景 |
|--------|------------|---------|---------|------------|
| B₄C | 2.519 | 9.3 | 2450 | 核辐射屏蔽、轻质装甲、特殊耐磨件 |
| SiC | 3.21 | 9.2 | 2700 | 通用轻量化耐磨结构件、散热器件 |
| Al₂O₃ | 3.9 | — | 2053 | 中温耐蚀、低成本低载荷场景 |

高体积分数B₄C/Al复合材料的耐磨性能优于等体积分数的SiC/Al复合材料[[S1]]。但B₄C的成本和技术门槛通常高于SiC，因此其应用集中于对轻量化、功能特性（如中子吸收）有特殊要求的场景。

## 应用领域

- **耐磨件/耐磨涂层**：B₄C/Al复合材料在干滑动条件下具有良好的耐磨性能[[S1]]
- **轻质装甲与冲击防护件**：利用B₄C的高硬度和低密度特性[[S19]]
- **核辐射屏蔽材料**：B₄C具有良好的中子吸收能力[[S12]]
- **高强度结构件**：可用于连杆、控制臂、转向节等汽车零部件[[S2]]

## 标准与规范

> **部分证据不足声明**：目前检索范围内未查询到专门针对B₄C颗粒产品的中国GB/T规范或ASTM产品标准。现有标准主要覆盖复合材料的通用力学、热学等性能测试方法（如ASTM复合材料测试系列标准），可用于评价B₄C增强铝基复合材料的性能[[S13,S29]]。专门针对B₄C颗粒产品的独立规范仍属证据不足。

## Sources
- S4: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0722584e-197f-494c-8d7c-228600fb7804/resource) (`0722584e-197f-494c-8d7c-228600fb7804`)
- S12: [低压铸造SiC_Al复合材料铸件的组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/825343c5-f3aa-4370-b6dc-8031b63b0137/resource) (`825343c5-f3aa-4370-b6dc-8031b63b0137`)
- S19: [GNPs强韧化B4C复合材料的制备及性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9e60d02-eb8e-4676-991d-54692986f2d6/resource) (`a9e60d02-eb8e-4676-991d-54692986f2d6`)
- S11: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c0c3a85-4f51-4f08-8dfd-0c2f6b3641ed/resource) (`7c0c3a85-4f51-4f08-8dfd-0c2f6b3641ed`)
- S15: [先进镁合金制备与加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9951b1df-7d9f-47bb-ab05-2db6f359316a/resource) (`9951b1df-7d9f-47bb-ab05-2db6f359316a`)
- S16: [constitution of binary alloys first supplement__9108a2373c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9bbb2a62-2ecc-4d94-a274-95f4000fddff/resource) (`9bbb2a62-2ecc-4d94-a274-95f4000fddff`)
- S8: [常用碳化物的性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48f2d18c-0526-42ff-9442-a7f8f0b5ce2d/resource) (`48f2d18c-0526-42ff-9442-a7f8f0b5ce2d`)
- S14: [实用模具材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96bbce4a-1793-4de2-9171-f28fb00b04af/resource) (`96bbce4a-1793-4de2-9171-f28fb00b04af`)
- S20: [机械工程材料及热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3823e57-1668-4355-88da-3db933fac494/resource) (`b3823e57-1668-4355-88da-3db933fac494`)
- S32: [硼碳氮体系超硬材料化合物关系示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fea6607d-d08b-4351-b989-f79b4325c227/resource) (`fea6607d-d08b-4351-b989-f79b4325c227`)
- S22: [工程材料与热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbc7a8fa-c45c-4cf0-ba2b-7d901303934a/resource) (`bbc7a8fa-c45c-4cf0-ba2b-7d901303934a`)
- S23: [advances in corrosion control of magnesium and its alloys metal matrix composites and protective coatings__a7f032c4ca](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be12dbed-6d07-41c9-9c71-fa9d1207067f/resource) (`be12dbed-6d07-41c9-9c71-fa9d1207067f`)
- S1: [advances in high entropy alloys__48846efcf0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0150a7c4-6e7e-4be1-b866-2ba89154ee4a/resource) (`0150a7c4-6e7e-4be1-b866-2ba89154ee4a`)
- S6: [普通高等教育“十三五”规划教材 特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21456f6a-e38c-4e4c-a538-8956f3296520/resource) (`21456f6a-e38c-4e4c-a538-8956f3296520`)
- S21: [微纳BN颗粒改性铝铜合金材料的多尺度模拟及其在壳体中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bad5e6c6-b512-4c60-a6cc-e6de0985a03b/resource) (`bad5e6c6-b512-4c60-a6cc-e6de0985a03b`)
- S25: [TiCp+TiB2p_铝基复合材料高温力学性能研究及活塞试制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c434211c-ece7-438a-bba4-ae70f79e6757/resource) (`c434211c-ece7-438a-bba4-ae70f79e6757`)
- S30: [图 (b) 显示 B4C 颗粒表面的 Zr-Ti 富集保护层](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcbe63f5-a17c-4a3a-8006-731e6be74286/resource) (`fcbe63f5-a17c-4a3a-8006-731e6be74286`)
- S9: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cf87aa7-7477-4d58-9c83-37a7ce5d719d/resource) (`4cf87aa7-7477-4d58-9c83-37a7ce5d719d`)
- S28: [微纳BN颗粒改性铝铜合金材料的多尺度模拟及其在壳体中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd4afaf8-0cc8-4f79-b062-b9f20afb7657/resource) (`dd4afaf8-0cc8-4f79-b062-b9f20afb7657`)
- S17: [advances in high entropy alloys__48846efcf0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d5379af-331f-4b7e-b33c-3ab86e5c5574/resource) (`9d5379af-331f-4b7e-b33c-3ab86e5c5574`)
- S10: [advances in corrosion control of magnesium and its alloys metal matrix composites and protective coatings__a7f032c4ca](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/528456c9-4d03-41f8-a3c9-1e0848121df1/resource) (`528456c9-4d03-41f8-a3c9-1e0848121df1`)
- S2: [挤压铸造实验设计：压力、温度与 B4C 含量对硬度和抗拉强度的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03fbf99f-534c-4a26-bc0d-db5103e951e2/resource) (`03fbf99f-534c-4a26-bc0d-db5103e951e2`)
- S3: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04cc7bf9-921a-4ab6-b62d-d59f1e82e915/resource) (`04cc7bf9-921a-4ab6-b62d-d59f1e82e915`)
- S31: [A356-5 vol% B4C金属基复合材料（铸锭冶金法，抛光态）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd0f4fc9-b92e-498c-84ad-f03f3a6d4cd1/resource) (`fd0f4fc9-b92e-498c-84ad-f03f3a6d4cd1`)
- S7: [图 11：不同老化温度下复合材料的总吸收能量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4003a6d6-1ee9-4b0b-b1c3-d0724a1efbb6/resource) (`4003a6d6-1ee9-4b0b-b1c3-d0724a1efbb6`)
- S5: [常用颗粒增强体及铝合金基体特性对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1bdd7b63-debe-4782-93c8-433d964b10a2/resource) (`1bdd7b63-debe-4782-93c8-433d964b10a2`)
- S18: [表1-2 常用颗粒增强体热物性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f95b51e-4aa2-44cc-baea-278c6ccfbac5/resource) (`9f95b51e-4aa2-44cc-baea-278c6ccfbac5`)
- S24: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c35bb0cd-13d6-4e05-b3fc-caee672c9313/resource) (`c35bb0cd-13d6-4e05-b3fc-caee672c9313`)
- S26: [advanced materials processing and manufacturing processes__410843daa8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c7cd4524-006b-446c-a87f-e62632f1e71b/resource) (`c7cd4524-006b-446c-a87f-e62632f1e71b`)
- S13: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91f167d6-52f0-40e1-b8b2-20606b9b6fab/resource) (`91f167d6-52f0-40e1-b8b2-20606b9b6fab`)
- S29: [ASTM复合材料相关测试标准列表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e49cbdcd-623b-4f5e-823a-3d2bd0443734/resource) (`e49cbdcd-623b-4f5e-823a-3d2bd0443734`)