---
version: "v1"
generated_at: "2026-06-19T09:27:14+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 34
  source_quality_score: 0.89
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

## 概述

AFS平均细度（AFS Grain Fineness Number，简称AFS GFN），又称AFS细度数、AFS细度或原砂细度，是铸造行业表征造型用砂（尤其是硅砂）平均粒度分布的核心参数。该参数由美国铸造学会（American Foundry Society，简称AFS）最早制定并推广，现已纳入多项国家标准和行业规范。AFS平均细度通过标准筛分法测得，其数值与单位质量去泥砂粒的理论总表面积大致成正比，广泛用于型砂、芯砂及各类铸造颗粒材料的粒度选型和质量控制。[[S4,S32,S30]]

## 定义与物理意义

AFS平均细度是原砂经标准筛析后，通过计算得出的一个等效平均粒度指标。其物理意义为：假设砂样中所有颗粒尺寸完全均一，且全部砂粒恰好能通过某一理论筛号，则该筛号即为该砂样的AFS平均细度。这一等效砂粒的总表面积与实际砂样砂粒的总表面积相等，因此AFS平均细度数值大致与单位质量原砂（扣除泥分）的总表面积成正比。[[S4,S12,S32]]  

AFS平均细度数值越大，代表砂样整体颗粒越细。工业铸造场景中常用型砂的AFS细度值通常分布在40—220区间内。[[S6,S30]]  

## 测试标准与设备

AFS平均细度测试方法最早由美国铸造学会制定，后纳入中国国家标准GB/T 9442—1998《铸造用硅砂》。配套标准筛符合ASTM E11系列（含1970版）金属丝试验筛规范，国内等效筛具符合JB/T 9155铸造用试验筛要求，筛孔尺寸序列与AFS官方标准基本对齐。[[S28,S15,S20,S7]]

AFS标准筛序列具有严格的比例关系：相邻两级筛子的筛孔尺寸比值为√2（即1.414），相邻两级筛孔面积比值为2。整套筛组包含从6号粗筛到270号细筛的全套筛具，底部配置物料收集底盘，常规推荐筛具规格为直径203 mm（8英寸），单筛高度25–50 mm。[[S28,S19]]

测试前需先按照标准流程去除砂样中粒径小于20 μm的AFS泥分，将烘干后的无泥砂样放入叠放完成的全套筛组中，通过筛砂机振动12–15 min，然后称量每级筛上的残留砂质量，代入公式完成计算。[[S20,S5,S34]]

国内等效标准中，铸造用试验筛的筛号与筛孔尺寸对应关系见下表。[[S20]]

| 筛号 | 筛孔尺寸（mm） |
|------|----------------|
| 6    | 3.35           |
| 12   | 1.70           |
| 20   | 0.850          |
| 30   | 0.600          |
| 40   | 0.425          |
| 50   | 0.300          |
| 70   | 0.212          |
| 100  | 0.150          |
| 140  | 0.106          |
| 200  | 0.075          |
| 270  | 0.053          |

## 计算公式与计算方法

AFS平均细度的标准加权计算公式为：

**AFS平均细度 = \(\dfrac{\displaystyle\sum_{}^{} (P_n \cdot X_n)}{\displaystyle\sum_{}^{} P_n}\)**

式中：\(P_n\) 为 n 号筛上停留砂粒质量占砂样总质量的百分数，\(X_n\) 为 n 号筛对应的细度因数（乘数）。[[S33,S14,S6,S2,S7,S30]]

各筛号对应的细度因数由标准规定，常用筛号的细度因数如下（以国内标准GB/T 9442为例）。[[S7,S11,S15]]

| 筛号 | 细度因数 |
|------|----------|
| 6    | 3        |
| 12   | 5        |
| 20   | 10       |
| 30   | 20       |
| 40   | 30       |
| 50   | 40       |
| 70   | 50       |
| 100  | 70       |
| 140  | 100      |
| 200  | 140      |
| 270  | 200      |

## 计算实例

### 实例一：铸造原砂

以国内常用铸造硅砂测试为例，各筛层砂粒乘积总和为4663.4，各筛停留砂粒质量分数总和为98.88，计算所得AFS平均细度为47.2，按数值修约规则取整后为47。[[S33,S37]]

| 筛号 | 停留量（质量分数%） | 乘数 | 乘积  |
|------|---------------------|------|-------|
| 6    | —                   | 3    | —     |
| 12   | —                   | 5    | —     |
| 20   | —                   | 10   | —     |
| 30   | 1.60                | 20   | 32.0  |
| 40   | 8.10                | 30   | 243.0 |
| 50   | 33.80               | 40   | 1352.0|
| 70   | 32.10               | 50   | 1605.0|
| 100  | 16.50               | 70   | 1155.0|
| 140  | 6.78                | 100  | 678.0 |
| 200  | —                   | 140  | —     |
| 270  | —                   | 200  | —     |
| 底盘 | —                   | —    | —     |
| **总和** | **98.88**       | —    | **4663.4** |

计算：AFS平均细度 = 4663.4 ÷ 98.88 = 47.2，取整为 **47**。

### 实例二：天然粘结砂

以含5.9 g泥分的天然粘结砂测试为例，各筛层停留砂粒乘积总和为15.243，各筛停留砂粒质量分数总和为88.2，最终计算所得AFS平均细度为173。[[S4,S22]]

计算：AFS平均细度 = 15.243 ÷ 88.2 = **173**。

## 粗细分级与典型数值区间

根据筛孔尺寸与AFS细度中值的对应关系，铸造行业将型砂划分为粗砂、中砂、细砂三类。下表给出了典型筛号组对应的AFS中值。[[S21]]

| 砂类 | 主要筛号组 | AFS细度中值 | 适用场景 |
|------|------------|-------------|----------|
| 粗砂 | 30/50      | 30          | 大型铸件、高透气性要求 |
| 中砂 | 50/100     | 50          | 通用铸件、平衡透气性与表面质量 |
| 细砂 | 70/140     | 70          | 小型铸件、高表面光洁度要求 |

AFS平均细度中值约为该组砂前筛号的数值（例如50/100筛号组的AFS中值为50）。当实际AFS值低于中值时，表明该组砂中前部筛号上的粗砂较多；反之，则后部筛号上的细砂较多。[[S21]]

## 与工艺性能的关系

### 透气性

AFS平均细度直接影响型砂的透气性。其他条件不变时，AFS数值越小（砂粒越粗），砂粒间孔隙尺寸越大，透气性越高。但相同AFS细度下，粒度分布差异对透气性有显著影响：单筛分布砂的透气性可达7.5 cm²/(Pa·min)，而两筛镶嵌分布砂的透气性仅约4.7 cm²/(Pa·min)，差距近一倍。[[S24]]

### 铸件表面质量与金属液渗透

AFS数值越高（砂粒越细），紧实后砂型表面孔隙尺寸越小，金属液越难渗入砂粒间隙，铸件表面粗糙度越低、光洁度越高。但AFS数值过高会导致砂粒总表面积过大，型砂透气性显著下降，易产生气孔类缺陷。[[S1,S17]]  

在铸铁湿型砂生产中，当AFS细度小于50且透气性大于180时，铸件发生机械粘砂的置信度可达0.8；将型砂AFS细度调整至55–70区间可有效降低粘砂缺陷概率。[[S3]]

### 紧实率

型砂紧实率间接受AFS细度影响。细砂（高AFS值）的总比表面积更大，在相同含水量条件下更易通过紧实过程获得均匀的砂型密度。常规生产中将湿型砂紧实率控制在43%–47%区间时，可匹配不同AFS细度型砂的最佳综合性能。[[S25]]

## 不同铸造工艺的选型区间

| 铸造工艺 | 推荐AFS细度区间 | 选型依据 |
|----------|-----------------|----------|
| 消失模铸造干砂 | 25–45 | 高排气性要求，防止模样热解残留物逸出受阻；过细则阻碍排气，过粗则金属液渗透 [[S24,S13]] |
| 覆膜砂砂芯（重力/低压铸造） | 50–65 | 保证排气性同时保障树脂与砂粒接触面积，使24h冷芯强度达峰值 [[S18,S13]] |
| 铸铁湿型砂（防粘砂） | 55–70 | 有效降低粘砂缺陷概率 [[S3]] |
| 高压铸造（特殊可溃散砂芯） | 高于低压覆膜砂区间 | 抵消高压充型时的金属液渗透压力，防止砂粒被冲入型腔 [[S17]] |

AFS平均细度与砂粒流动性在一定范围内存在关联。以3D打印砂型用砂为例，高硅砂（AFS 53.14）流动性为15 s，陶瓷砂（AFS 52.94）流动性为14 s，再生砂（AFS 56.12）流动性为14 s，各砂种在相近AFS水平下表现出较好的流动性。[[S29]]  

![三种砂的AFS细度与流动性检测结果柱状图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a387ad64-faec-4016-8182-cb7e44877870/resource)  

## 局限性

AFS平均细度作为一种单一平均值参数，存在以下固有限制：

1. **不能反映粒度分布宽度**：粒度分布完全不同的两种型砂可以得到完全相同的AFS细度值，但二者的透气性、粘结剂需求量、强度等工艺性能可能存在显著差异。[[S4,S15,S9,S30]]
2. **基于理想球形假设**：计算逻辑基于所有砂粒为理想球形的假设。当面对异形颗粒、筛分过程中未破碎的团聚型砂粒、或表面包覆粘结剂层的再生旧砂颗粒时，测试结果会出现明显偏差，无法准确对应砂样的真实比表面积和粒度分布参数。[[S26,S31]]

## 与其他粒度指标的配合使用

为弥补AFS平均细度的局限性，铸造行业常引入其他粒度表征参数配合使用。德国铸造学会定义了两个补充指标：  

- **中间粒径（MK）**：对应砂样50%累积通过量的筛孔直径，表示砂粒的平均粒径。  
- **均匀度（GG）**：4/3 MK粒径的砂质量通过量减去2/3 MK粒径的砂质量通过量的差值，用于表征粒度分布的均匀程度。[[S33]]

现行铸造标准（如GB/T 9442—1998）要求供货方在提供AFS平均细度的同时，必须提供完整的粒度分布全曲线作为补充验收依据，从而实现不同工况下型砂性能的精准调控。[[S33]]

## 在国内标准体系中的应用

在国内铸造用砂标准中，AFS平均细度已纳入产品牌号的标准化命名体系：

- **铸造用硅砂牌号（ZGS）**：AFS平均细度作为牌号核心组成字段之一，与SiO₂分级代号、主要粒度组成首尾筛号及平均细度偏差分级代号共同构成完整牌号。[[S8]]
- **铸造用覆膜砂牌号（FMS）**：AFS平均细度作为第三级字段标注，与常温抗弯强度分级、灼烧减量分级并列构成牌号结构。[[S10]]

## 与再生工艺的关系

湿法再生工艺中，水砂比的变化会对再生砂的AFS细度产生微弱影响。以湿法再生试验数据为例，当水砂体积比从0.5:1提升至3:1时，再生砂含泥量从0.92%逐步下降至0.70%，对应的AFS细度从49逐步升高至50。这表明水洗除泥过程会略微提升AFS细度值，但影响幅度有限。[[S23]]

| 水砂体积比 | 含泥量（%） | AFS细度 |
|------------|------------|---------|
| 0.5:1      | 0.92       | 49      |
| 1.0:1      | 0.85       | 49      |
| 2.0:1      | 0.75       | 50      |
| 3.0:1      | 0.70       | 50      |

## 可视化参考

型砂粒度分布与累积百分比曲线是表征AFS细度与全粒度分布对应关系的常用可视化手段。该曲线以筛号为横轴，以质量百分比为纵轴，包含单筛残留量分布折线和累积通过率曲线，可直观展示砂样在不同筛号上的颗粒富集情况，并与AFS平均值相互印证。[[S36]]  

![型砂粒度分布与累积百分比曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f72df72f-0fed-4ff2-8187-f8efc12dbf67/resource)

## Sources
- S4: [造型材料试验手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14048931-5d92-467e-b9e7-6b935c6276c1/resource) (`14048931-5d92-467e-b9e7-6b935c6276c1`)
- S32: [GBT+5611（铸造术语）-2017.pdf-dd5ce1f8-c5b9-4d94-87e7-fc40cbfe0347](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4c7a7e4-00f0-4b81-a861-d39fa03eff02/resource) (`d4c7a7e4-00f0-4b81-a861-d39fa03eff02`)
- S30: [制造技术 第1卷 铸造、成形和焊接 英文版 原书第3版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8ea4f00-32c3-423a-a942-283135c312cd/resource) (`a8ea4f00-32c3-423a-a942-283135c312cd`)
- S12: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5adab31d-4429-434f-9c7d-4345abd7d5f2/resource) (`5adab31d-4429-434f-9c7d-4345abd7d5f2`)
- S6: [材料加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/29082743-9eeb-4e74-b67d-b4aff4193906/resource) (`29082743-9eeb-4e74-b67d-b4aff4193906`)
- S28: [造型材料试验手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f53e32b-f1f6-456d-bc0e-42b0670da7c6/resource) (`9f53e32b-f1f6-456d-bc0e-42b0670da7c6`)
- S15: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fd1afe2-1f34-45f4-9b57-95ab9da43e78/resource) (`6fd1afe2-1f34-45f4-9b57-95ab9da43e78`)
- S20: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/849b8a7f-269b-44a2-bfc7-07414a5be205/resource) (`849b8a7f-269b-44a2-bfc7-07414a5be205`)
- S7: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/291b1960-2b50-42a8-9510-7430931e818f/resource) (`291b1960-2b50-42a8-9510-7430931e818f`)
- S19: [1991 annual book of astm standards section 2 nonferrous metal products v__3abfaf437d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/838fb6c0-89d4-48a4-8084-d60812f3907d/resource) (`838fb6c0-89d4-48a4-8084-d60812f3907d`)
- S5: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26e98bc9-ce6c-478f-9c2d-cec3a8b03f6e/resource) (`26e98bc9-ce6c-478f-9c2d-cec3a8b03f6e`)
- S34: [制造技术—铸造、成形和焊接（英文·原书第2版）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e32da17c-a6b1-432c-90a7-3a490d5fb47f/resource) (`e32da17c-a6b1-432c-90a7-3a490d5fb47f`)
- S33: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e06d90c0-32bd-4b42-af85-58d7dc08d7a3/resource) (`e06d90c0-32bd-4b42-af85-58d7dc08d7a3`)
- S14: [金属材料液态成型实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/600d0256-81dc-4ca3-b282-25571f08b785/resource) (`600d0256-81dc-4ca3-b282-25571f08b785`)
- S2: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b2504d1-0c06-47ea-b600-81db132ac880/resource) (`0b2504d1-0c06-47ea-b600-81db132ac880`)
- S11: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55efd3f8-f299-48db-90a4-55a1afb4e012/resource) (`55efd3f8-f299-48db-90a4-55a1afb4e012`)
- S37: [原砂的平均细度计算实例表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb7018b7-052a-4349-b9c8-9ec8ff8afea1/resource) (`fb7018b7-052a-4349-b9c8-9ec8ff8afea1`)
- S22: [表 4.2 AFS 细度典型计算示例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/905abda7-e44b-4d26-9a09-61b3013cfadd/resource) (`905abda7-e44b-4d26-9a09-61b3013cfadd`)
- S21: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ba3ec52-89d4-4841-9f35-da1bdf27e790/resource) (`8ba3ec52-89d4-4841-9f35-da1bdf27e790`)
- S24: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90a31a70-49cf-4fe2-bb3e-ff7223e33d8d/resource) (`90a31a70-49cf-4fe2-bb3e-ff7223e33d8d`)
- S1: [实用铸造技术问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0940f3cf-0ec1-4b83-8286-4f8e71ccd5e1/resource) (`0940f3cf-0ec1-4b83-8286-4f8e71ccd5e1`)
- S17: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/778484df-5ba5-4e13-a23f-a660f27a0405/resource) (`778484df-5ba5-4e13-a23f-a660f27a0405`)
- S3: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1192d942-68c9-4eb7-a24e-0ccc2af0815d/resource) (`1192d942-68c9-4eb7-a24e-0ccc2af0815d`)
- S25: [金属液态成型原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94da6a0a-b6f4-4b5e-821a-3d2123661565/resource) (`94da6a0a-b6f4-4b5e-821a-3d2123661565`)
- S13: [5352135_原砂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5adddb90-2271-4947-a65b-0dd88ae0812d/resource) (`5adddb90-2271-4947-a65b-0dd88ae0812d`)
- S18: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/798a386e-85b8-4c36-b198-43dd0f2e9e84/resource) (`798a386e-85b8-4c36-b198-43dd0f2e9e84`)
- S29: [图3-1 三种砂粒度AFS和流动性检测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a387ad64-faec-4016-8182-cb7e44877870/resource) (`a387ad64-faec-4016-8182-cb7e44877870`)
- S9: [制造技术—铸造、成形和焊接（英文·原书第2版）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46f596b5-f744-40f2-b6da-aeeb38fbb60c/resource) (`46f596b5-f744-40f2-b6da-aeeb38fbb60c`)
- S26: [造型材料试验手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9521ee7b-73d8-446f-a811-cbade8de4255/resource) (`9521ee7b-73d8-446f-a811-cbade8de4255`)
- S31: [造型材料试验手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bdbf3cee-a82a-44e4-8dbd-cb2cb14c337a/resource) (`bdbf3cee-a82a-44e4-8dbd-cb2cb14c337a`)
- S8: [图3-3 铸造用硅砂牌号表示](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/463c1d41-e34a-4490-b4be-9ec3e4c95507/resource) (`463c1d41-e34a-4490-b4be-9ec3e4c95507`)
- S10: [铸造用覆膜砂的牌号表示方法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4c298b41-c758-4cbd-bc87-a2013926b541/resource) (`4c298b41-c758-4cbd-bc87-a2013926b541`)
- S23: [表6.2 不同水砂体积比对再生砂的粒度分布及含泥量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90a06811-9d3f-42db-9141-e8bb47148198/resource) (`90a06811-9d3f-42db-9141-e8bb47148198`)
- S36: [型砂粒度分布与累积百分比曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f72df72f-0fed-4ff2-8187-f8efc12dbf67/resource) (`f72df72f-0fed-4ff2-8187-f8efc12dbf67`)