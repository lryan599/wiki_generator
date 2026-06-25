---
version: "v1"
generated_at: "2026-06-18T13:21:46+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 41
  source_quality_score: 0.84
  freshness_score: 0.92
  evidence_coverage_score: 1.0
---

## 1 定义与技术特征

**Al-Si系免热处理压铸铝合金**是指通过合金成分设计与高压铸造工艺优化，使合金在铸态（F态）自然冷却条件下即可达到目标力学性能，无需额外进行固溶、淬火或完整T6/T7时效处理的Al-Si基压铸铝合金体系[[S44,S28]]。其强化机制以细晶强化、固溶强化和凝固析出第二相强化为主，区别于传统可热处理Al-Si铸造铝合金依赖Mg₂Si等析出相的沉淀强化作用路径[[S44]]。

该类合金的免热处理核心判定标准包含三点[[S19,S44]]：

1. 合金中Mg、Cu等时效强化元素的含量显著低于常规可热处理Al-Si系压铸铝合金，从而大幅降低时效硬化效应；
2. 铸态下屈服强度可达80~220 MPa，延伸率为8%~15%，满足汽车结构件的力学性能要求；
3. 经过完整T6/T7热处理后，合金性能提升幅度极低，部分牌号甚至不发生明显变化。

与常规可热处理Al-Si铸造铝合金（如A356、A201）的本质区别在于：后者必须通过“固溶+时效”热处理才能达标，仅靠铸态F状态无法满足使用要求；而免热处理合金无需该工序即可直接在铸态下实现高性能，从而规避大型薄壁压铸件在热处理后易发生变形、表面起泡和报废率升高的问题[[S27]]。

## 2 分类与子体系

当前主流的Al-Si系免热处理压铸铝合金可划分为以下子体系[[S31,S2]]：

| 子体系 | 典型代表牌号 | 特征 |
|--------|-------------|------|
| Al-Si-Mg系 | Silafont-36 (EN AC-43500 / AlSi10MnMg)、Silafont-38 | 低Fe含量，通过Sr变质细化共晶Si、Mn球化富铁相，铸态可满足车身结构件要求 |
| Al-Si-Mg-Mn系 | Aural-2、Aural-3、Aural-5 | Fe含量上限0.2%，Mn约0.5%，Mg含量进一步优化 |
| 低Mg/无Mg添加过渡族元素系 | Castasil-37 (AlSi9MnMoZr) | Mg质量分数上限控制在0.06%以下，通过添加Mo、Zr实现固溶与细晶强化 |
| Al-Si-X定制化多元系 | JDA1系列、特斯拉自研合金 | 根据应用需求定制Si、Cu、Mn及微合金元素配比 |

在国内外标准体系中的对应情况：EN 1706收录了Silafont-36对应的EN AB-43500低铁Al-Si-Mg-Mn牌号；ASTM B179和ASTM B85收录了对应AlSi10MgMn等可铸态直接使用的Al-Si系压铸铝合金；JIS H5202、JIS H5302中的ADC3SF等低铁高延伸Al-Si压铸牌号可归入免热处理范畴；GB/T 15115在近年更新版本中已补充部分免热处理合金牌号[[S22,S37,S35]]。

## 3 合金化机理与微观组织

### 3.1 主要合金元素的成分窗口与作用机理

常用牌号Al-Si系免热处理压铸合金的核心元素质量分数范围如表所示（基于[S3]）：

- **Si**：通常在4.0~11.5 wt%范围内调控，Si含量提升可改善合金流动性，同时增加共晶Si面积分数，细化α-Al晶粒[[S12]]。
- **Mg**：质量分数一般不超过0.5 wt%。Mg在凝固初期生成Mg₂Si强化相，以细小颗粒形式均匀分布于基体与晶界处，可大幅强化α-Al基体。但当Mg含量过高时，会沿晶界析出网状Al₃Mg₂相，引发热裂风险并显著降低合金塑性[[S4,S30]]。
- **Cu**：适宜添加区间为0.5~1.5 wt%，可通过过饱和固溶和纳米级GP区析出实现自然时效强化。当Cu含量超过1.5 wt%时，会沿晶界生成粗大网状Al₂Cu相，显著降低合金的热裂抗性与耐蚀性[[S15,S20]]。

### 3.2 微合金元素的作用

- **Sr变质共晶Si**：Sr原子选择性吸附在共晶硅孪晶凹谷处，阻碍硅原子沿原方向堆垛，迫使共晶硅从粗大板片状转变为纤维状/蠕虫状。免热处理压铸合金中Sr的最优添加区间为0.01~0.1 wt%，过量Sr会降低熔体流动性和引发缩松缩孔缺陷[[S16,S4]]。
- **Ti/B细化α-Al**：Al-5Ti-1B等细化剂生成高熔点TiB₂异质形核核心，可显著增加α-Al的形核数量，将晶粒尺寸降低70%以上，提升合金强韧性并减少铸件缺陷[[S34,S4]]。
- **Mn/Fe协同优化**：Mn原子替换Fe原子，将针状硬脆β-Al₅FeSi相转变为汉字状/多边形状的α-Al₁₅(Fe,Mn)₃Si₂相。Mn/Fe质量比的最优调控区间为0.6~0.8，该比例下α相占比可超过85%，合金伸长率显著提升[[S30,S9]]。
- **V、Zr、Mo过渡族元素**：在无Mg体系免热处理Al-Si合金中，可生成高温稳定的细小弥散金属间化合物（如Al₃Zr相），在压铸快速凝固后有效钉扎晶界、抑制再结晶，实现细晶弥散强化，无需依赖Mg₂Si析出强化即可获得较高铸态强度与热稳定性[[S19,S14]]。

### 3.3 铸态微观组织特征

免热处理Al-Si压铸合金的典型铸态组织为：尺寸细小圆润的等轴α-Al晶粒、分布于晶界处的网状变质共晶硅、以及弥散分布的改性富铁相。合金中粗大平衡析出相占比极低，与常规需热处理Al-Si合金铸态下粗大α-Al枝晶和板片状未变质共晶硅的组织形态存在显著差异[[S12,S44]]。通过Mn/Fe协同调控可有效抑制硬脆β-Fe相，使富铁相呈均匀弥散分布[[S17,S24]]。

![免热处理Al-Si压铸合金高Si含量样本的低倍SEM图像，显示富铁相呈均匀弥散分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/462b951c-2bd8-4b7c-9f9a-3fa58290f586/resource)

图：高压铸造免热处理Al-Si合金高Si含量样本的低倍SEM图像（×50 μm），显示富铁相呈均匀弥散分布[[S17]]。

### 3.4 相图基础

- **Al-Si二元相图**：共晶成分Si含量为11.7%，共晶温度577℃，共晶温度下Si在α-Al中的最大固溶度为1.65%，室温下固溶度降至约0.05%[[S6,S23]]。
- **Al-Mg₂Si伪二元相图**：共晶温度595℃，共晶点对应的Mg₂Si质量分数为13%，共晶温度下Mg₂Si在α-Al中的最大固溶度为1.85%，室温下固溶度趋近于0[[S42,S50]]。

## 4 工艺适应性

### 4.1 高压铸造工艺参数窗口

针对一体化压铸（Gigacasting）场景的Al-Si免热处理铝合金推荐标准工艺参数窗口范围：浇注温度680~730℃，模具初始/工作温度推荐180~250℃，内浇口压射速度范围18~35 m/s，压射比压50~70 MPa，高真空配置下型腔真空度可控制在50~100 mbar[[S27,S18]]。某款一体化后车体CAE仿真验证所用的免热处理Al-Si合金典型工艺参数为：浇注温度690℃、真空度50 mbar、增压压力28 MPa、模具初始温度180℃[[S43]]。

### 4.2 铸造缺陷控制

Al-Si免热处理压铸铝合金通过定向成分调控手段（将Mg元素质量分数控制在0.06%以下、添加0.3%~0.8%的Mn实现抗粘模，配合Zr、Mo等元素细晶强化），相比传统常规压铸合金可显著降低热裂倾向，抑制粘模缺陷生成；配合高真空系统可有效降低型腔内卷气带来的气孔缺陷发生率，适配无后续热处理的工艺要求[[S21,S1,S47]]。

## 5 铸态力学性能

### 5.1 典型牌号性能基准

| 牌号 | 铸态屈服强度 Rp₀.₂ (MPa) | 铸态抗拉强度 Rm (MPa) | 铸态延伸率 A (%) | 备注 |
|------|--------------------------|----------------------|------------------|------|
| 美铝 C611 | 123 | 268 | 16.2 | Si含量4%~7%，折弯角达45°，已用于奥迪A8全铝车身[[S19,S38]] |
| Castasil-37 | 120~140 | 240~260 | 9~12 | Mg≤0.06%，Mo/Zr复合强化[[S19,S38,S21]] |
| 特斯拉自研合金 | 130~150 | 280~295 | 10~16 | Si约8.5%，Cu约0.79%[[S13,S48,S49]] |
| 国内自研（JDA1等） | ≥150 | ≥280 | ≥10 | 多企业已开发，部分已小批量交付[[S13]] |

Aural 5M可在保证强度的前提下提升塑性，适配后续涂装烘烤硬化要求，其力学表现与A356-T6、A357-T6热处理合金相当，显著优于传统压铸合金A380、ADC12的常规性能[[S21,S19,S33]]。

### 5.2 壁厚与取样位置对性能的影响

不同壁厚下的Al-Si免热处理铝合金性能存在波动：3 mm薄壁标准试样的综合力学性能优于大尺寸结构件本体取样；近浇口位置试样的屈服强度和抗拉强度整体高于远浇口位置取样；大尺寸一体压铸构件的实际本体性能普遍低于实验室标准试棒的检测结果[[S51,S26]]。

## 6 应用领域

### 6.1 汽车轻量化结构件

全球已量产的代表性Al-Si免热处理铝合金一体化压铸应用案例[[S1,S11,S21,S25,S48]]：

- **特斯拉Model Y全铝后地板**：采用自研Al-Si系免热处理合金，将原70余个分散零件合并为单件成型，制造成本降低约40%，单部件生产节拍从传统热处理工艺的1~2小时缩短至3~5分钟[[S11,S36]]；
- **奥迪A8后纵梁**（Castasil-37）、**捷豹XJ A柱及减震塔**、**大众辉腾车门内板**等均采用对应牌号的商用免热处理Al-Si合金量产。

### 6.2 其他领域应用

可用于5G通信基座、消费电子壳体等对铸态性能和无变形要求较高的部件；部分航空航天非承力结构件也开始试用该类合金以降低后续热处理工序成本[[S11,S40]]。

## 7 优势与局限性

### 7.1 核心优势

取消T6热处理的Al-Si免热处理压铸工艺具有显著的综合效益[[S11,S36,S21,S44]]：

- **成本降低**：特斯拉上海工厂一体化压铸后地板制造成本相比传统分零件制造工艺降低约40%；
- **生产节拍加快**：单部件生产节拍从传统热处理工艺的1~2小时缩短至3~5分钟；
- **能耗与碳排放降低**：单条大型T6热处理生产线每年可减少CO₂排放达4500 Mt；
- **规避变形与表面缺陷**：完全避免大尺寸构件热处理带来的鼓泡、变形及后续整形高废品率问题。

### 7.2 现存局限性

当前公开的技术局限性包括[[S33,S40]]：

- 合金成分窗口窄，对Fe、Cu等杂质元素的含量波动敏感；
- 部分服役场景下疲劳强度、冲击韧性仍低于同级别热处理合金；
- 针对该类合金的配套焊接、结构胶粘接工艺适配标准尚未完全普及。

## 8 相关概念对比

免热处理Al-Si压铸铝合金与传统压铸/铸造铝合金在成分体系和工艺路径上的区别：传统压铸铝合金（如A380、ADC12）含较高的Fe（0.8~1.1 wt%）以利于脱模，但存在大量硬脆β-Al₅FeSi相，延伸率较低；可热处理Al-Si铸造合金（如A356-T6、A357-T6）依赖固溶+时效实现强化，工序复杂且大件易变形；免热处理Al-Si压铸铝合金则通过低Fe设计、Mn/Fe比调控、Sr变质及微量过渡族元素添加，另辟蹊径地在铸态下实现强度与塑性的协同[[S7,S31,S19]]。

## Sources
- S44: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be1dd337-4dff-4c78-aa1a-3287dc92e4fd/resource) (`be1dd337-4dff-4c78-aa1a-3287dc92e4fd`)
- S28: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ae3463d-f591-4e2b-aa72-e3210bf09929/resource) (`7ae3463d-f591-4e2b-aa72-e3210bf09929`)
- S19: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a13ff66-c55b-43cc-bcc2-5e8b2253b5ee/resource) (`5a13ff66-c55b-43cc-bcc2-5e8b2253b5ee`)
- S27: [一体压铸用免热处理铝合金自主研发及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7348ad90-aa1e-481a-bedb-cd53f0309b54/resource) (`7348ad90-aa1e-481a-bedb-cd53f0309b54`)
- S31: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cce15c9-13d6-4bc3-a83e-75c736157c17/resource) (`8cce15c9-13d6-4bc3-a83e-75c736157c17`)
- S2: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07f6a7c3-735f-457a-88fe-8eeca3cac19d/resource) (`07f6a7c3-735f-457a-88fe-8eeca3cac19d`)
- S22: [国内外主要压铸铝合金代号对照表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5d305b43-8398-47c9-b57f-3c34e060447f/resource) (`5d305b43-8398-47c9-b57f-3c34e060447f`)
- S37: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c31a640-f143-4c34-903f-cbc5961ad1a7/resource) (`9c31a640-f143-4c34-903f-cbc5961ad1a7`)
- S35: [压铸成型技术及模具 设计与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98314b3b-610f-46ea-8ccd-e346c2ee439b/resource) (`98314b3b-610f-46ea-8ccd-e346c2ee439b`)
- S12: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25d0c53b-ac2c-4a85-af0c-997a356144b1/resource) (`25d0c53b-ac2c-4a85-af0c-997a356144b1`)
- S4: [免热处理铝合金大型结构件一体压铸研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c1004b7-01a2-4339-a254-ca757edab5a1/resource) (`0c1004b7-01a2-4339-a254-ca757edab5a1`)
- S30: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82013eee-6b17-4059-9384-bca4ce09589a/resource) (`82013eee-6b17-4059-9384-bca4ce09589a`)
- S15: [effect of chemical compositions on tensile behaviors of high pressure di__7b422b5dd4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/310a3757-4d62-40da-ae55-4d2a2f8f77fb/resource) (`310a3757-4d62-40da-ae55-4d2a2f8f77fb`)
- S20: [铝合金一体化压铸技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a415112-0cbb-43fd-93a2-bfcda9ab952f/resource) (`5a415112-0cbb-43fd-93a2-bfcda9ab952f`)
- S16: [免热处理压铸Al-9Si合金成分与工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42bec4d4-a4fa-4c58-94db-eb53f2ae9f1c/resource) (`42bec4d4-a4fa-4c58-94db-eb53f2ae9f1c`)
- S34: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92439c5e-0b77-4e95-8e11-cec24d720160/resource) (`92439c5e-0b77-4e95-8e11-cec24d720160`)
- S9: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1887da90-1c56-42b2-b2ae-dc394a575fc9/resource) (`1887da90-1c56-42b2-b2ae-dc394a575fc9`)
- S14: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d614a31-79f7-4f47-905d-2c5c1696c6da/resource) (`2d614a31-79f7-4f47-905d-2c5c1696c6da`)
- S17: [图3.3(d) 免热处理压铸Al-Si合金富铁相低倍SEM照片](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/462b951c-2bd8-4b7c-9f9a-3fa58290f586/resource) (`462b951c-2bd8-4b7c-9f9a-3fa58290f586`)
- S24: [免热处理压铸Al-Si合金低倍SEM照片（Si含量9-10wt.%）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/651eccee-32b5-4080-8f77-c404a7c26a6a/resource) (`651eccee-32b5-4080-8f77-c404a7c26a6a`)
- S6: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/122c965c-5fe3-4ccd-b89e-7f6a622451f9/resource) (`122c965c-5fe3-4ccd-b89e-7f6a622451f9`)
- S23: [铝合金材料组织与金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f31f98e-d804-442a-be13-98d0f6e4f2d6/resource) (`5f31f98e-d804-442a-be13-98d0f6e4f2d6`)
- S42: [有色合金铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b9892749-b9af-4c62-a38d-f939044ae571/resource) (`b9892749-b9af-4c62-a38d-f939044ae571`)
- S50: [自生颗粒增强铝基复合材料汽缸套的制备技术及其应用研究__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3b7cccb-023e-447e-afec-714c95f7d2ef/resource) (`e3b7cccb-023e-447e-afec-714c95f7d2ef`)
- S18: [表 9-6 压铸试样工艺参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/544b3fe6-da4f-423f-9d6e-626dd5122cfd/resource) (`544b3fe6-da4f-423f-9d6e-626dd5122cfd`)
- S43: [表一 CAE 模拟工艺参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bab5a516-80f5-4be1-87e5-117c44549974/resource) (`bab5a516-80f5-4be1-87e5-117c44549974`)
- S21: [乘用车白车身铝合金压铸结构件及材料应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5af52160-8b71-4e9a-a625-2febfaa9c292/resource) (`5af52160-8b71-4e9a-a625-2febfaa9c292`)
- S1: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/007fb056-27aa-42a5-8f73-c308a2a9ec14/resource) (`007fb056-27aa-42a5-8f73-c308a2a9ec14`)
- S47: [免热处理压铸Al-9Si合金成分与工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce144ac9-a4ec-4e15-8004-09eb28d2337c/resource) (`ce144ac9-a4ec-4e15-8004-09eb28d2337c`)
- S38: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a02050cf-086e-4071-ad7f-87b05b503352/resource) (`a02050cf-086e-4071-ad7f-87b05b503352`)
- S13: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2617b3fb-b636-4458-9d6e-0f47e2795799/resource) (`2617b3fb-b636-4458-9d6e-0f47e2795799`)
- S48: [0019_27e5403754fcdd48_Giga_Press](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0c3f674-c3d1-484a-bd56-fa6edf101f0c/resource) (`d0c3f674-c3d1-484a-bd56-fa6edf101f0c`)
- S49: [0019_27e5403754fcdd48_Giga_Press](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da0b39e8-ff53-453c-af6d-30c72776a67c/resource) (`da0b39e8-ff53-453c-af6d-30c72776a67c`)
- S33: [一体化压铸免热处理铝合金研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9034930d-7153-462b-b9f1-c65ff2cc7b64/resource) (`9034930d-7153-462b-b9f1-c65ff2cc7b64`)
- S51: [图4.11 零件和3mm试片力学性能对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5695aca-4857-4517-b458-2e9a745e132a/resource) (`e5695aca-4857-4517-b458-2e9a745e132a`)
- S26: [表4.14 拉伸试样尺寸及拉伸性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/708a0180-dabe-4ecc-94d7-d1c77baa92d6/resource) (`708a0180-dabe-4ecc-94d7-d1c77baa92d6`)
- S11: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21f22368-55a4-4f77-9ad3-d04fab832912/resource) (`21f22368-55a4-4f77-9ad3-d04fab832912`)
- S25: [0019_27e5403754fcdd48_Giga_Press](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6badc09a-febd-48d9-b443-5ef83cfd69f4/resource) (`6badc09a-febd-48d9-b443-5ef83cfd69f4`)
- S36: [ageless aluminum cerium based alloys in high volume die casting for impr__882de99c2e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9918d4a5-bb2a-404c-96f2-0a3773721dd4/resource) (`9918d4a5-bb2a-404c-96f2-0a3773721dd4`)
- S40: [乘用车白车身铝合金压铸结构件及材料应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6775f77-b490-47a4-aa81-d41afa62c1cc/resource) (`a6775f77-b490-47a4-aa81-d41afa62c1cc`)
- S7: [effect of microstructure and casting defects on the mechanical propertie__7978147656](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16c1ed73-bd29-47cc-acb6-048b6c3417b9/resource) (`16c1ed73-bd29-47cc-acb6-048b6c3417b9`)