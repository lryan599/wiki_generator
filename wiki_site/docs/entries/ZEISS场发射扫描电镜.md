---
version: "v1"
generated_at: "2026-06-18T12:54:59+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 23
  source_quality_score: 0.83
  freshness_score: 0.93
  evidence_coverage_score: 1.0
---

## 概述

ZEISS场发射扫描电镜，标准型号为ZEISS SUPRA 55（亦见于文献中略作“SUPRA55”[[S11,S16]]），是由德国卡尔·蔡司（Carl Zeiss）制造的肖特基热场发射扫描电子显微镜[[S19,S4]]。该设备在压铸材料研究中被广泛使用，可完成压铸铝合金/镁合金等试样的微观组织形貌观测、断口形貌表征、微区成分分析及EBSD晶粒取向分析等工作[[S18,S16,S23]]。

不同于冷场发射（CFE）电子枪仅可搭载能谱仪（EDS），ZEISS SUPRA 55作为热场发射扫描电镜，可同时加装能谱仪与波谱仪（WDS）[[S19]]。

## 与钨灯丝SEM的性能差异

ZEISS SUPRA 55与传统钨灯丝热发射扫描电镜的核心性能差异源于电子枪类型。以下表格对比了不同类别SEM电子枪的典型特性[[S8]]：

| 电子枪类型 | 发射源尺寸 | 束能量展宽 | 20 keV下典型束流 | 20keV下典型束亮度（A/cm²·sr） |
|:----------|:----------|:----------|:----------------|:--------------------------|
| 钨热发射           | 较大 | — | — | — |
| LaB₆热发射        | — | — | — | — |
| 冷阴极场发射        | 极小 | — | — | — |
| **肖特基发射（热场发射）** | **小** | — | **较高** | **显著高于钨灯丝型号** |

传统钨灯丝热发射SEM的发射源直径较大，样品表面电子束斑直径通常为5~7nm，分辨率较低；而ZEISS SUPRA 55作为肖特基热场发射SEM，其电子源尺寸更小、束流密度更高，成像分辨率远优于传统钨灯丝扫描电镜[[S8,S19]]。热场发射阴极尖端的工作温度约1800℃[[S19]]。

## 主要技术规格与结构

### 电子枪类型

ZEISS SUPRA 55采用肖特基热场发射电子枪（Schottky emitter），属于热场发射（Thermal Field Emission, TFE）类型[[S19]]。这一设计可提供较大的电子束流，解决了冷场发射因尖端发射总电流小而导致无法搭载波谱仪的问题[[S19]]。

### 探测器与成像模式

研究所见操作实例中，ZEISS SUPRA 55至少具备以下成像模式与信号采集能力：

- **二次电子（SE）模式**：二次电子像主要反映试样表面形貌[[S3,S6,S14]]
- **背散射电子模式**：可显示元素分布状态及不同相成分区域的轮廓[[S4,S10]]
- **In-lens SE、SE2**：常见二次电子探测器类型[[S3,S6]]

### EDS能谱仪集成

ZEISS SUPRA 55原厂/市面主流集成的配套能谱仪（EDS）为牛津仪器（Oxford Instruments）系列，典型配套型号为Oxford IE 300×型X射线能谱仪[[S4,S17]]。该组合支持对试样开展点扫描、线扫描和面扫描元素成分分析[[S11,S24,S1]]。

### EBSD功能

ZEISS SUPRA 55可集成背散射电子衍射（EBSD）功能，用于晶粒取向分析研究[[S16,S17]]。

## 在压铸领域的典型应用

### 第二相形貌与分布分析（显微组织观测）

ZEISS SUPRA 55广泛用于压铸铝合金、锌合金、镁合金的第二相形貌与分布的微观表征[[S23,S18,S22]]。

**试样制备方法**（以ADC12压铸铝合金为例）：

1. 取样后依次使用400目至2000目的不同粒度水砂纸逐级研磨[[S13,S6]]
2. 机械抛光至镜面[[S13,S6]]
3. 采用Keller试剂腐蚀5~10 s（或采用4%硝酸酒精腐蚀约5 s）[[S13,S6,S14]]
4. 超声波清洗并吹干后上机观测[[S13]]

**典型压铸铝合金第二相形貌示例**：

免热处理压铸Al-Zn-Si-Cu合金的FESEM显微组织图像清晰展示了纤维状共晶Si以及晶界富Zn相的典型形貌分布[[S20]]。

![免热处理压铸Al-Zn-Si-Cu合金典型第二相SEM形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3b0c8b4-adc8-439a-8e77-e3a1ceb0a076/resource)

*图：免热处理压铸Al-Zn-Si-Cu合金FESEM显微组织图像（标尺10μm），可见纤维状共晶Si及晶界富Zn相*[[S20]]

**缺陷周围基体组织观测**：

Al-Si-Cu合金压铸件缺陷周围基体组织的二次电子SE2模式SEM图像（放大200倍，加速电压20 kV，与ZEISS SUPRA 55常用操作参数匹配）可用于展示缺陷周边弥散分布的细小第二相颗粒特征[[S3]]。

![Al-Si-Cu压铸件缺陷周边基体组织200倍二次电子SEM形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14382318-eafd-478d-a73b-60cd6aa5b21e/resource)

*图：Al-Si-Cu压铸件缺陷周围基体组织的二次电子SEM图像（×200，20 kV）*[[S3]]

### EDS元素分析

#### 点扫描（Point Analysis）

EDS点扫描可对压铸铝合金/锌合金中不同微区第二相的元素原子百分比进行定量测试，从而精准判定相组成[[S2,S25]]。例如，可区分Al₂CuMg（S相）、Al₂Cu等压铸铝合金中常见的第二相类型[[S2,S25]]。下表示例为2195铝锂合金中各能谱点的原子含量及对应判定的第二相类型[[S25]]：

| 能谱点 | Al (at.%) | Cu (at.%) | Mg (at.%) | 判定第二相 |
|:------|:----------|:----------|:----------|:----------|
| 以实测为准 | — | — | — | 可区分残余第二相类型 |

*注：表中数值因不同检测点位而异，完整的原子含量及相判定见原始文献，此处仅展示数据结构的定性形式*[[S25]]

#### 线扫描（Line Scan）

EDS线扫描可沿压铸合金试样上预设的扫描路径，连续采集不同位置的元素信号强度（如Mg、Al、Si、Ca、Ce、Mn等），直观展示第二相与基体相界面处的元素浓度梯度变化，实现压铸凝固过程中溶质偏析行为的定量表征[[S24,S9]]。

#### 面扫描（Elemental Mapping）

EDS面扫描可在较大视场范围内全域采集观测区域内各元素的分布特征，直观呈现Zn、稀土等合金元素在压铸合金晶界第二相上的整体富集分布规律[[S1,S21]]，用于分析压铸过程中的元素偏聚行为。

### 拉伸断口形貌观察

ZEISS SUPRA 55广泛用于压铸合金拉伸断口的微观形貌表征[[S23,S22,S15]]。

**断口保护基本要求**[[S10,S15,S5]]：

- 试样拉断后**严禁用手触摸断口表面**，**严禁将两个匹配断口互相对接**，以避免人为划痕和磨损污染
- 应立即使用无水乙醇或丙酮进行超声波清洗
- 完全干燥后尽快上机观测；长期在空气中放置会导致断口表面氧化、积灰，破坏原始形貌特征

## 操作要点与局限性

### 导电性要求与样品处理

扫描电镜对试样的基本要求是导电[[S10]]：

- 对于导电良好的压铸金属样品，标准金相抛光和浸蚀处理即可直接观测
- 非导电样品（如压铸陶瓷涂层、非金属夹杂类试样）需在表面喷镀导电层[[S10]]
  - **喷金**：适配低倍率形貌观察
  - **喷碳**：适配后续需要EDS定量成分分析的场合，以避免金元素的特征X射线对压铸合金中待测轻元素的检测造成干扰[[S10,S19]]

### 磁性样品注意事项

（本维基目前暂未收入磁性样品相关的ZEISS SUPRA 55专门实验数据。）

### 维护要求与常见问题

- 热场（肖特基）发射电子枪的阴极寿命较冷场发射低，需注意灯丝的定期更换[[S19]]
- 成像过程中的**像散校正**是日常操作维护的常见操作项，需由经过培训的操作人员执行

## 相关标准与方法

压铸材料研究中使用ZEISS SUPRA 55开展扫描电镜及能谱分析时，常参考或引用的主要标准与方法包括：

- GB/T 16594 — 扫描电镜分析相关通用标准（此处按发现逻辑对应引入，该标准属中国国家标准扫描电镜分析领域常引文件）
- ISO 22493 — 扫描电镜分析相关国际标准（同上）
- GB/T 228.1—2021《金属材料 拉伸试验 第1部分：室温试验方法》 — 拉伸试样的切取与测试标准[[S23,S13,S15,S22]]

*注：上述标准在本研究获取的发现材料中被相关文献间接引用或与试验方法关联，具体条款适用性应以原始标准文本为准。*

## Sources
- S11: [挤压铸造成形铝合金飞轮壳构件微观组织与力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a0e6c45-222e-43a8-bc85-87b62a0cbc14/resource) (`6a0e6c45-222e-43a8-bc85-87b62a0cbc14`)
- S16: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae1fec2d-24c7-4ed8-bdec-c6334de35663/resource) (`ae1fec2d-24c7-4ed8-bdec-c6334de35663`)
- S19: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c1494015-43e6-430f-bde5-7a168cef5eb4/resource) (`c1494015-43e6-430f-bde5-7a168cef5eb4`)
- S4: [激光熔覆CoCrFeNiMoNb_WC复合涂层及高温服役性能的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1609858e-e5d8-4558-9a81-a1fdd9850ab1/resource) (`1609858e-e5d8-4558-9a81-a1fdd9850ab1`)
- S18: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5b00e1f-b5e3-469e-8c6b-db709057485e/resource) (`b5b00e1f-b5e3-469e-8c6b-db709057485e`)
- S23: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1a343be-d9ad-447f-aaf0-d0b66811a4bf/resource) (`f1a343be-d9ad-447f-aaf0-d0b66811a4bf`)
- S8: [扫描电子显微镜（SEM）不同类型电子枪的典型特性参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a96f289-f264-4dba-af69-9744d2440603/resource) (`5a96f289-f264-4dba-af69-9744d2440603`)
- S3: [缺陷周围基体组织的二次电子(SEM)图像（图4.8(a)）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14382318-eafd-478d-a73b-60cd6aa5b21e/resource) (`14382318-eafd-478d-a73b-60cd6aa5b21e`)
- S6: [T6热处理对高压压铸ADC12铝合金微观结构和性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e699368-32a3-4d41-bee3-26c246828c08/resource) (`4e699368-32a3-4d41-bee3-26c246828c08`)
- S14: [稀土成分对EA43合金组织、力学及导热性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97ebefde-c09c-4e8a-b1f6-9dc281bc0004/resource) (`97ebefde-c09c-4e8a-b1f6-9dc281bc0004`)
- S10: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65433de1-7a72-4349-a969-11157c68a775/resource) (`65433de1-7a72-4349-a969-11157c68a775`)
- S17: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af6575f5-f86d-4a37-890e-bf4c967552c8/resource) (`af6575f5-f86d-4a37-890e-bf4c967552c8`)
- S24: [图4.5 普通重力铸造Mg-9Al-2Si-0.5Ca-0.2Ce-0.2Mn合金的扫描电子图像与能谱线扫分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6b57004-03cc-4526-9b70-dd0676e44970/resource) (`f6b57004-03cc-4526-9b70-dd0676e44970`)
- S1: [图3.1(f) Mg-Zr中间合金的EDS面扫描结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b64d519-2da6-4061-af2e-060c357df89a/resource) (`0b64d519-2da6-4061-af2e-060c357df89a`)
- S22: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e09979af-dc3a-41ea-87aa-1f1926fcce4d/resource) (`e09979af-dc3a-41ea-87aa-1f1926fcce4d`)
- S13: [T6热处理对高压压铸ADC12铝合金微观结构和性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81b29e9c-8f38-4542-aa74-d81f10055288/resource) (`81b29e9c-8f38-4542-aa74-d81f10055288`)
- S20: [压铸Al-Zn-Si-Cu合金的扫描电镜显微组织图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3b0c8b4-adc8-439a-8e77-e3a1ceb0a076/resource) (`c3b0c8b4-adc8-439a-8e77-e3a1ceb0a076`)
- S2: [典型航空铝合金塑性成形与蠕变时效成形的工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0dfdae15-07e1-4803-8aa1-9d2f04f4ee6c/resource) (`0dfdae15-07e1-4803-8aa1-9d2f04f4ee6c`)
- S25: [表4-3 图4-7中各点能谱分析结果(at.%)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fec35f41-5788-4389-9de2-0d5162062537/resource) (`fec35f41-5788-4389-9de2-0d5162062537`)
- S9: [Fig.4.23 传统铸态(CC)与受控扩散凝固(CDS)样品的SEM表面形貌及EDS线扫分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62e5baf6-5bf8-4b98-ba33-f3218c952cda/resource) (`62e5baf6-5bf8-4b98-ba33-f3218c952cda`)
- S21: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9077ae0-1d20-48d4-802c-3dd0174b0164/resource) (`c9077ae0-1d20-48d4-802c-3dd0174b0164`)
- S15: [5A06铝合金盒体压铸成形工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ef09786-25f7-4486-b9db-0aacf0e64af6/resource) (`9ef09786-25f7-4486-b9db-0aacf0e64af6`)
- S5: [5202785_断口分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c4723ff-1d2b-4a9f-a69a-bcd87e8bf5c5/resource) (`2c4723ff-1d2b-4a9f-a69a-bcd87e8bf5c5`)