---
version: "v1"
generated_at: "2026-06-19T05:00:48+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 42
  source_quality_score: 0.87
  freshness_score: 0.72
  evidence_coverage_score: 1.0
---

## 概述

Ar相变点（Ar transformation temperature）指铁-碳合金在固态范围内冷却时发生相变的实际温度[[S43]]。该术语由法国冶金学家Osmond提出，“Ar”源自法语*arrêt refroidissement*（冷却转变停滞点），与之对应的加热相变点记为“Ac”（*arrêt chauffant*）[[S5,S8,S41]]。

由于实际热处理中冷却并非极缓慢的平衡过程，Ar相变点的数值总是低于铁碳相图上的平衡临界点（A₁、A₃、Acm），冷却速度越大，偏移量（即过冷度）越大[[S32,S40,S29]]。常规热处理手册中引用的Ar相变点数值，普遍是在30～50℃/h的冷却速度下测定的[[S29,S28]]。

Ar相变点在压铸模具钢（如H13/4Cr5MoSiV1/SKD61）的热处理工艺中具有核心地位，直接影响淬火冷却工艺的制定和模具的服役性能[[S13,S34]]。

## 定义与分类

### 基本定义

依据GB/T 5611-2017《铸造术语》，Ar相变点（冷却相变点）的各级定义如下[[S43]]：

- **Ar₁**：奥氏体向珠光体转变的开始温度；
- **Ar₃**：奥氏体开始析出先共析铁素体的温度；
- **Arcm**（标准中记为Arm）：奥氏体开始析出先共析渗碳体的温度。

美国ASTM E44《金属热处理术语标准定义》同样将Ar₁、Ar₃、Arcm纳入国际通用热处理术语体系[[S24]]。

### 与平衡相变点及加热相变点的关系

铁碳相图上的A₁、A₃、Acm是在极缓慢加热/冷却（平衡条件）下测得的临界点。实际生产中，加热和冷却均偏离平衡条件，形成双向滞后[[S15,S20,S50]]：

- 加热相变点Ac₁、Ac₃、Accm **高于**平衡相变点（过热现象）；
- 冷却相变点Ar₁、Ar₃、Arcm **低于**平衡相变点（过冷现象）。

Fe-Fe₃C相图上，Ar₁对应的相变温度区间位于平衡共析线（A₁/PSK线，727℃）的低温侧，Ar₃位于平衡GS线的低温侧，Arcm位于平衡ES线的低温侧[[S52,S15]]。三条Ar相变点连线整体向低温方向偏移。

![Fe-Fe₃C相图上实际加热、平衡、冷却三类相变点的位置对比，展示Ar系列相变点相对平衡相变点的低温偏移](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21d786b6-e801-4672-bc44-4c91615addcb/resource)

### 各类Ar相变点的相变反应

| 相变点 | 对应平衡线 | 冷却相变反应 | 适用钢种 |
|--------|------------|-------------|----------|
| Ar₁ | PSK线（A₁线） | 奥氏体→珠光体共析转变（起始） | 所有铁碳合金 |
| Ar₃ | GS线（A₃线） | 奥氏体→先共析铁素体析出（起始） | 亚共析钢 |
| Arcm | ES线（Acm线） | 奥氏体→先共析二次渗碳体析出（起始） | 过共析钢 |

## 关联概念

研究简报中提及多个关联术语，需与Ar相变点明确区分。

### Ar与Ac（加热相变点）

Ac是实际加热条件下的相变点，Ar是实际冷却条件下的相变点，二者属于同一扩散型相变的正、逆向特征温度，因加热/冷却滞后效应而分别高于和低于平衡相变点[[S15,S20]]。

### Ar与Ms点

Ms点是快速冷却条件下奥氏体向马氏体无扩散型转变的起始温度，属于远低于Ar₁的低温相变区间[[S38,S33]]。Ar相变点对应高温扩散型相变（珠光体、先共析铁素体/渗碳体析出），而Ms点对应低温切变型相变，两者相变机制和转变产物完全不同。

### Ar与As点

As点是加热过程中马氏体向奥氏体逆转变的起始温度，属于逆向相变的特征点，与Ar冷却相变点方向相反，无直接对应关系[[S25]]。

### Ar与奥氏体化温度

奥氏体化温度是将钢加热到Ac₁/Ac₃以上以获得奥氏体组织的加热工艺参数[[S28]]，属于加热过程范畴，与冷却过程中奥氏体分解的Ar系列相变点概念不同。

## 典型压铸模具钢的Ar相变点数据

### H13/4Cr5MoSiV1钢

H13（SKD61）是压铸模最常用的热作模具钢，不同批次和测量条件下Ar相变点存在差异：

| 来源 | Ar₁ / ℃ | Ar₃ / ℃ | Ms / ℃ |
|------|---------|---------|--------|
| 典型实测值一 | 700 | 820 | 335 |
| 典型实测值二 | 775 | 875 | 340 |

### 5%Cr系热作模具钢相变点对比

以下表格收录了三种主流5%铬系热作模具钢的相变点数据，可直接用于不同牌号的热处理工艺参数比对[[S12]]：

| 钢号 | Ac₁ /℃ | Acm (Ac₃) /℃ | Ar₁ /℃ | Ar₃ /℃ | Ms /℃ | Mf /℃ |
|------|---------|---------------|---------|---------|--------|--------|
| 4Cr5MoSiV1 (H13) | 860 | 915 | 775 | 875 | 340 | — |
| 4Cr5MoSiV (H11) | 853 | 912 | 720 | 820 | 310 | — |
| 4Cr5W2VSi | 840 | 900 | 765 | 840 | 285 | — |

## 核心影响因素

### 合金元素

Cr、Mo、V、Si属于缩小奥氏体相区的铁素体稳定化元素，可改变Ar₁、Ar₃温度水平[[S14,S48]]。其中Cr的作用具有特殊性：Cr含量低于7.5%时使A₃点下降（相应Ar₃下降），高于7.5%时使A₃点上升（相应Ar₃上升）[[S9,S4]]。

Cr、Mo、V等碳化物形成元素同时显著降低碳在奥氏体中的扩散速度，减缓冷却过程中铁素体、珠光体的转变为速率，使实际测得的Ar转变温度向低温偏移[[S49,S42]]。Si对碳扩散速度的影响较弱，对Ar相变点的直接作用弱于Cr、Mo、V[[S49]]。

### 原始组织

退火后获得均匀球状珠光体的原始组织，其Ar₁、Ar₃转变起始温度较存在偏析或粗大碳化物的组织更高，转变区间更窄[[S36]]。

### 奥氏体化温度

随奥氏体化加热温度升高，更多合金碳化物溶入奥氏体，奥氏体中碳和合金元素含量提高，使后续冷却过程中的Ar相变点向低温方向偏移[[S11]]。

### 冷却速率

冷却速率提升使Ar相变点向低温方向偏移，相变温度区间拓宽。当冷却速率超过该钢种的临界冷速时，Ar点对应的珠光体/铁素体转变被完全抑制，直接进入马氏体转变区间[[S18,S35]]。

## 测量方法

### 膨胀法

膨胀法是Ar相变点的主流程测定方法之一。采用φ3mm×10mm小试样，以快速膨胀仪真空感应加热至奥氏体区后，程序控制冷却速率，采集不同冷速下试样的膨胀-温度曲线。以体积突变对应特征点确定Ar转变的起始温度、各阶段转变量和终了温度，测定结果可辅助构建CCT曲线[[S18,S35]]。

### 差热分析（DTA）

在程序控温冷却过程中，同步检测待测试样与无热效应参比物之间的温差。试样发生Ar相变时释放的相变潜热使温差曲线出现特征拐点，对应温度即为Ar相变点的特征温度[[S53,S45]]。

### 差示扫描量热法（DSC）

在程序控温冷却过程中，测量输入试样和参比物的补偿热流差随温度的变化。DSC曲线下的面积与相变释放的总热量成正比，可精准定量Ar相变的起始温度、峰值温度和转变热焓，定量精度优于DTA[[S22,S10,S44]]。

### CCT曲线中的标注

在时间-温度半对数坐标系中，Ar₃标注为冷却过程中先共析铁素体析出的起始温度线，Ar₁标注为珠光体相变完全终了的温度线。不同冷却速率曲线与Ar相变线的交点可反映不同冷速下的实际Ar转变温度[[S18,S3]]。

![BH13（H13级热作模具钢）连续冷却转变CCT图，标注Ar₃、Ar₁、Ms、Mf等关键冷却相变点在不同冷速曲线上的位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80ffec13-d8b8-484f-8a1d-23654fa58b89/resource)

## 在压铸模具钢热处理中的应用

### 淬火冷却工艺制定的核心依据

压铸模具钢奥氏体化后的冷却过程，需在Ar₃到Ar₁的相变区间精确控制冷速，其目的为[[S13,S34]]：

- 避免冷却过程中析出铁素体、珠光体等非马氏体的软质相；
- 保证淬火后获得均匀的马氏体组织；
- 显著降低相变应力，减少变形与开裂倾向。

采用匹配Ar相变点的精确控冷工艺，H13类压铸模具钢最终硬度可稳定达到45～52HRC，冲击韧性较未按Ar点匹配冷速的工艺提升30%以上，模具服役寿命可提高2～3倍。该工艺规范已纳入北美压铸协会#207-90标准[[S37,S21]]。

瑞典ASSAB品牌8407（H13改良型）的推荐热处理工艺为1020～1050℃淬火、585～640℃回火，该工艺完全匹配其Ar相变点数值，兼顾高硬度与高热疲劳抗性[[S37]]。

### 分段冷却的工艺逻辑

基于Ar相变点的控冷核心原则是：冷却曲线应尽量避开Ar相变区间内非马氏体产物的形核-长大区域。当冷却速率足够大（超过临界冷速），过冷奥氏体直接进入Ms点以下的马氏体转变区间，可获得全马氏体组织。截面厚大或形状复杂的模具，常在稍高于Ar₁的温度区间进行分级保温，使整体温度均匀后再继续冷却，以降低热应力[[S1]]。

## 与模具缺陷的关系

### 淬火软点

当冷却参数偏离Ar点控制区间，局部区域在Ar₁以上温度长时间停留时，过冷奥氏体部分分解为铁素体、珠光体、屈氏体等非马氏体组织，形成淬火软点，导致模具局部硬度不达标，软点区域成为优先开裂的失效起源位置[[S39]]。

**预防措施**：严格控制原材料碳化物偏析级别；采用合格的预备热处理保证组织均匀；淬火前清理氧化皮和锈斑；加热过程防止氧化脱碳；定期检查和更换淬火冷却介质；大尺寸模具淬火时做往复运动，避免局部粘附气泡降低冷速[[S36]]。

### 淬火开裂

当冷却工艺完全偏离Ar相变控制区间，冷速分布极度不均，Ar点对应相变产生的组织应力与热应力叠加后超过材料断裂强度时，引发淬火开裂，尤其在模具截面厚薄突变、尖角位置开裂风险最高[[S55]]。

**预防措施**：形状复杂、截面差大的模具采用分级淬火或等温淬火；严格控制水淬停留时间；淬火完成后及时回火；需返修淬火的模具预先进行充分的中间退火[[S1]]。

### 残余奥氏体过多

当冷却速率过快，部分过冷奥氏体未在Ar相变区间完成分解即进入马氏体转变温度区间，同时合金元素含量偏高进一步降低Ms、Mf点时，淬火后残余奥氏体含量远超设计要求。这将降低模具硬度、耐磨性和尺寸稳定性，服役过程中残余奥氏体持续转变还会引发局部体积胀大[[S48,S23]]。

**预防措施**：淬火完成后及时进行多次回火；对尺寸精度要求高的模具在冷至室温后补充-60℃～-190℃的冷处理，促进残余奥氏体向马氏体充分转变[[S39,S23]]。

## 术语多义性说明

Ar相变点术语虽主要面向铁碳合金体系，但在非铁合金领域亦存在扩展使用，如铝青铜的相变温度曲线中同样标注冷却相变点Ar与加热相变点Ac以表征滞后特征[[S47]]。在压铸常用语境下，Ar相变点默认指铁碳合金（模具钢）的冷却相变温度。

## Sources
- S43: [GBT+5611（铸造术语）-2017.pdf-dd5ce1f8-c5b9-4d94-87e7-fc40cbfe0347](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d02b8afb-1c7e-4dc0-8098-83c2f0715038/resource) (`d02b8afb-1c7e-4dc0-8098-83c2f0715038`)
- S5: [a hundred years of metallurgy__4ffafa7bed](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/217c72ee-d869-4d8d-87fd-765918f20766/resource) (`217c72ee-d869-4d8d-87fd-765918f20766`)
- S8: [材料加工工程科技英语](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25bc91b3-8444-4336-9958-acaf28e65269/resource) (`25bc91b3-8444-4336-9958-acaf28e65269`)
- S41: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd92d411-f156-42ae-9df4-4136f2923ff2/resource) (`cd92d411-f156-42ae-9df4-4136f2923ff2`)
- S32: [材料加工原理及工艺学无机非金属材料和金属材料分册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a72c5dbc-582d-41bf-839e-e583019bee4e/resource) (`a72c5dbc-582d-41bf-839e-e583019bee4e`)
- S40: [机械制造基础工程材料及热加工工艺基础上册第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc5e7bd0-fe68-460b-a617-c9e468084f09/resource) (`cc5e7bd0-fe68-460b-a617-c9e468084f09`)
- S29: [材料热处理与表面工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91587e55-885b-4e6c-8e73-1623e79ed241/resource) (`91587e55-885b-4e6c-8e73-1623e79ed241`)
- S28: [工程材料与热加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d088d0c-ba22-477d-ae72-a61f139c9865/resource) (`8d088d0c-ba22-477d-ae72-a61f139c9865`)
- S13: [die casting metallurgy__8f9e04f2f0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cd1d4ab-948d-4188-9c67-57fdc59e0ed7/resource) (`4cd1d4ab-948d-4188-9c67-57fdc59e0ed7`)
- S34: [压铸冶金学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab41d148-8313-4489-b1e0-48f2d408946e/resource) (`ab41d148-8313-4489-b1e0-48f2d408946e`)
- S24: [1991 annual book of astm standards section 1 lron and steel products vol__d9cf5303c8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78fa2029-fc3e-4e79-8297-8e6e18264149/resource) (`78fa2029-fc3e-4e79-8297-8e6e18264149`)
- S15: [金属材料及其成形加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/579d0186-b7ca-44af-a989-f7ea9547502e/resource) (`579d0186-b7ca-44af-a989-f7ea9547502e`)
- S20: [机械加工常识第2版含习题册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e9f83c3-a50e-4449-b3ed-6caf23e47c2e/resource) (`5e9f83c3-a50e-4449-b3ed-6caf23e47c2e`)
- S50: [材料加工工程科技英语](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5d8a8a1-c8ab-45db-8952-3736ec79283f/resource) (`e5d8a8a1-c8ab-45db-8952-3736ec79283f`)
- S52: [实用模具材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8394212-0a4e-4dd0-9dbf-1832e4f25407/resource) (`e8394212-0a4e-4dd0-9dbf-1832e4f25407`)
- S38: [an encyclopaedia of metallurgy and materials__c23587647c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bee34e67-8077-4ab7-bd6a-05ec3803491d/resource) (`bee34e67-8077-4ab7-bd6a-05ec3803491d`)
- S33: [an outline of metallurgy__6a9e4daee6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa159f58-2f2b-4c0a-82df-22fe0e828a14/resource) (`aa159f58-2f2b-4c0a-82df-22fe0e828a14`)
- S25: [basic mechanical properties and lattice defects of intermetallic compounds__affa85d061](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/803694a2-47da-4394-9de9-d6d580a6693f/resource) (`803694a2-47da-4394-9de9-d6d580a6693f`)
- S12: [表 3-29：ωCr 为 5% 的铬系三种钢的相变点温度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49333f6b-1eab-4fcb-9e3d-1958329cf948/resource) (`49333f6b-1eab-4fcb-9e3d-1958329cf948`)
- S14: [工程材料学热加工工艺基础学习指导习题](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56e3771f-774b-4fe0-b33d-3fd7d532015a/resource) (`56e3771f-774b-4fe0-b33d-3fd7d532015a`)
- S48: [机械工程材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4b12026-4ba6-4910-b2ed-1dffcbb71258/resource) (`e4b12026-4ba6-4910-b2ed-1dffcbb71258`)
- S9: [工程材料及热加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c06fdd1-fdb7-489e-b5ef-ecf728045c01/resource) (`3c06fdd1-fdb7-489e-b5ef-ecf728045c01`)
- S4: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e070403-4b8e-4b27-aa94-d77b20b3dbed/resource) (`1e070403-4b8e-4b27-aa94-d77b20b3dbed`)
- S49: [普通高等教育机电类规划教材机械工程材料与热加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5adbfb2-4243-482c-9533-5d1e2507f5a2/resource) (`e5adbfb2-4243-482c-9533-5d1e2507f5a2`)
- S42: [机械制造基础上工程材料及热加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf2b6d83-c019-4583-a3f7-d79c9acca6b5/resource) (`cf2b6d83-c019-4583-a3f7-d79c9acca6b5`)
- S36: [模具寿命与材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1b5907b-a1d7-4d92-849a-c6286f37e9b8/resource) (`b1b5907b-a1d7-4d92-849a-c6286f37e9b8`)
- S11: [图4-89 6W6Mo5Cr4V钢淬火温度与马氏体相变点的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4239bfae-02e4-4250-85fb-2a34cc2d4cf3/resource) (`4239bfae-02e4-4250-85fb-2a34cc2d4cf3`)
- S18: [材料热处理与表面工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b293be2-ea94-4645-b7c0-eeaa827f75a1/resource) (`5b293be2-ea94-4645-b7c0-eeaa827f75a1`)
- S35: [材料热处理与表面工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0e28479-3e01-4766-9faf-1a39d649d799/resource) (`b0e28479-3e01-4766-9faf-1a39d649d799`)
- S53: [熔盐电解镁锂合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2a00272-8f79-41b0-b547-b2c07e45df3a/resource) (`f2a00272-8f79-41b0-b547-b2c07e45df3a`)
- S45: [16991063_差示热分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0816f3b-3fdc-40d5-9162-0a772c189e9c/resource) (`e0816f3b-3fdc-40d5-9162-0a772c189e9c`)
- S22: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bb76973-e525-4988-9e33-c212c97d10d7/resource) (`6bb76973-e525-4988-9e33-c212c97d10d7`)
- S10: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40f793de-f672-451f-b97a-e4ad8f245229/resource) (`40f793de-f672-451f-b97a-e4ad8f245229`)
- S44: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d460ecfc-2ce3-4193-91c0-ef576259c999/resource) (`d460ecfc-2ce3-4193-91c0-ef576259c999`)
- S3: [图2-2 H13钢的CCT曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11acaaf8-dba9-4a17-872a-74423a72db6c/resource) (`11acaaf8-dba9-4a17-872a-74423a72db6c`)
- S37: [6149647_8407模具钢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b61405c9-27d0-459b-b9c6-34f9e00e3d70/resource) (`b61405c9-27d0-459b-b9c6-34f9e00e3d70`)
- S21: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63de54f7-1621-42a0-9f9d-622eb1913b6b/resource) (`63de54f7-1621-42a0-9f9d-622eb1913b6b`)
- S1: [模具失效与维护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03431a95-e176-4792-894d-5a12d98e0062/resource) (`03431a95-e176-4792-894d-5a12d98e0062`)
- S39: [工程材料及金属热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c988090e-d8a7-47c6-be12-741547ece7eb/resource) (`c988090e-d8a7-47c6-be12-741547ece7eb`)
- S55: [材料热处理与表面工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc8809a9-03ff-43c2-8aa6-d43126edd752/resource) (`fc8809a9-03ff-43c2-8aa6-d43126edd752`)
- S23: [模具材料应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/706a339f-b3b2-46f6-8d61-32d86b4e18dd/resource) (`706a339f-b3b2-46f6-8d61-32d86b4e18dd`)
- S47: [铝青铜II型的相变温度曲线（Ac、Ar）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4726caa-cb06-4415-9546-df0b40b5022b/resource) (`e4726caa-cb06-4415-9546-df0b40b5022b`)