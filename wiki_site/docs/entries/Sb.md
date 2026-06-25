---
version: "v1"
generated_at: "2026-06-18T08:58:01+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 41
  source_quality_score: 0.84
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

锑（Antimony，元素符号Sb）在压铸铝合金领域被归类为**长效变质剂**，属于碲-锑类变质剂范畴，主要作用是对Al-Si系合金的共晶硅进行变质调控 [[S39,S44,S24]]。与可获得纤维状共晶硅的Na、Sr类变质剂不同，锑变质后的共晶硅为分枝更密集的板片状或粒状，不具备常规细化初生α-Al晶粒的作用 [[S44,S20,S26]]。锑的变质效果几乎不烧损，不存在常规钠盐类变质剂的快速衰减问题，但其仅在无磷、冷却速度足够快的工况下才能发挥理想变质效果 [[S44,S26]]。

## 基本物理化学性质

单质锑的主要物理参数如下 [[S30]]：

| 性质 | 数值 |
|---|---|
| 熔点 | 630.5 °C |
| 沸点 | 1635 °C |
| 相对密度（水=1） | 6.68 |
| 原子序数 | 51 |
| 相对原子质量 | 121.76 |

锑在铝合金中的固溶度极低。在200~645 °C温度区间内，其固溶度不超过0.1%。少量添加即可形成含1.1%Sb的共晶体，共晶点温度为657 °C。当锑含量超过该阈值后，会生成针状脆性金属间化合物AlSb [[S29]]。

## 工艺作用与协同变质机理

### 单独添加Sb的变质效果

在免固溶处理XA铝合金（Al-Si-Zn-Mg-Cu系）中，仅单独添加Sb元素时，仅能细化共晶硅的尺寸，但无法改变共晶硅的原有形貌——共晶硅仍保持长条状/板片状形态，未能实现完全变质 [[S37]]。

### Sb与La的协同变质效果

Sb与La复合添加可实现显著的协同变质效果：可将未变质的粗糙条状/块状、带明显棱角的共晶硅转变为离散分布的圆润颗粒状，变质后共晶硅的颗粒尺寸约为1.0 μm，最大不超过2.0 μm，共晶硅数量显著提升 [[S37,S22]]。

### AlSb的异质形核争议与澄清

早期研究假说认为，Sb在铝硅合金中以AlSb或Mg₃Sb₂等第二相形式存在。AlSb在657.5 °C条件下形成，凝固过程中可能发挥类似AlP的作用，作为共晶硅的异质形核核心，从而实现共晶硅变质效果 [[S6,S8]]。

然而，通过Bramfitt二维晶格错配度公式计算证实，**AlSb与Si所有低指数平行晶面的二维晶格失配度δ均大于12%，不符合异质形核有效核心的经典判据（δ<12%）**，因此AlSb不能作为共晶硅的异质形核位点 [[S42,S43,S46]]。添加La和Sb后共晶硅数量提升的机制是**生长过程的增殖**，而非异质形核位点增多 [[S42,S46]]。

### Sb-La协同变质的微观机制

Sb-La协同变质的主流理论解释包含以下要点 [[S42,S46,S15]]：

1. **La的杂质诱导孪晶作用**：La的原子半径与Si的比值为1.59，接近Lu和Hellawell提出的杂质诱导孪晶理想半径比值1.646。La通过孪晶凹槽机制（TPRE）和杂质诱导孪晶（IIT）改变共晶硅生长模式，使原共晶体系的小平面/非小平面生长特征转变为非小平面/非小平面生长。

2. **颈缩、溶解与熔断机理**：Sb和La会富集在共晶硅分支的颈部，阻碍Si原子扩散，提高Al-Si体系中Si的平衡溶解度。少量La和Sb还会溶解进入硅晶格中形成低熔点硅固溶体。这两种作用共同促进共晶硅分支颈部发生颈缩、溶解、熔化与熔断，最终实现共晶硅的生长增殖。

3. **晶体结构改变**：TEM观测证实，未添加La和Sb的XA铝合金中共晶硅存在大量平行堆垛层错；添加La和Sb后堆垛层错数量大幅减少，形成取向为[111]的孪晶，共晶硅的堆垛生长方式发生显著改变 [[S22,S3]]。

下图展示了La-Sb协同变质下共晶硅颈部熔化熔断的过程：

![La-Sb协同变质下共晶硅颈部熔化熔断过程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c4d25c5-5b46-4d0d-940f-00c3a730e96e/resource)

*图：La和Sb协同作用下共晶硅分支颈部形态及熔化方向示意图，蓝色箭头指示溶解位置，红色虚线表示发生熔化和熔断的位置* [[S2,S15]]

### 对熔体物性与流动性的影响

添加Sb可显著降低XA铝合金的液态粘度，进而降低熔体正向流动阻力。La单独添加对合金粘度几乎无影响。同时，Sb会小幅提升合金的焓值——在540 °C温度下，含Sb合金的焓比不含Sb的XA合金高67.77 J/g，更高的焓意味着合金保留更多热量、冷却速度更慢，进一步提升流动性 [[S13,S33,S21]]。

**流动性定量实测数据** [[S4]]：

| 合金状态 | 浇注温度 (°C) | 螺旋线流动长度 (mm) |
|---|---|---|
| XA（无Sb, La） | 709 | 557 |
| XA（无Sb, La） | 729 | 925 |
| XA（加Sb, La） | 705 | 1154 |
| XA（加Sb, La） | 724 | 1346（达到模具最大长度） |

添加Sb和La后，705 °C浇注时螺旋线长度即可达到1154 mm，流动性较未添加组提升超45% [[S4]]。

### 对体收缩率的影响

**体收缩率定量实测数据** [[S17]]：

| 合金状态 | 浇注温度 (°C) | 液体收缩率 (%/°C) |
|---|---|---|
| XA（无Sb, La） | 747 | 0.033 |
| XA（加Sb, La） | 747 | 0.028 |
| XA（加Sb, La） | 727 | 0.019 |

Procast模拟结果也显示，相同浇注温度下Sb添加可将体收缩试样上端空隙深度从6.68 mm降至6.56 mm，有效减少铸件缩松生成概率 [[S11,S18]]。

### 对力学性能与断裂模式的影响

Sb与La复合添加的免固溶处理XA铝合金完全适配压铸免热处理要求。铸态下无需进行后续固溶处理，其抗拉强度从变质前的221 MPa提升至232 MPa，延伸率从2.12%提升至3.58%，延伸率提升幅度达68% [[S8,S46,S27]]。合金断裂模式从原有的脆性穿晶解理断裂转变为沿晶韧性和穿晶解理的混合断裂 [[S8,S46]]。

重力铸造下经150 °C×8 h时效处理后，抗拉强度可达264 MPa；压铸条件下添加La和Sb复合变质的XA铝合金油箱支架，铸态抗拉强度约275 MPa、延伸率约8%，经150 °C时效8 h后可实现293 MPa的抗拉强度 [[S10,S27,S31]]。

## 工艺参数与操作条件

### 添加形式与添加量

锑在压铸铝合金熔炼过程中的主流添加形式为Al-Sb中间合金，该中间合金的Sb质量分数为5%~8%。操作简便，不会对坩埚产生侵蚀，引入针孔、夹渣的倾向远低于钠盐变质剂 [[S20,S39]]。严禁将纯Sb直接加入铝液——Sb的相对密度为Al的2.5倍，直接加入会快速沉降生成难熔AlSb化合物沉底，引发严重密度偏析 [[S7]]。

**Sb变质工艺参数汇总** [[S5,S7,S40]]：

| 参数 | 推荐范围/数值 |
|---|---|
| 添加量（亚共晶/共晶Al-Si合金） | 0.1%~0.5%，最优0.2%~0.3% |
| 添加形式 | Al-(5%~8%)Sb中间合金 |
| 变质温度 | 720~780 °C |
| 保温反应时间 | 约20 min |
| 变质有效时长 | 10 h以上，最长可达100 h不失效 |
| 重熔特性 | 经氯盐除气、多次重熔后无明显烧损，仍保留变质效果 |

### 免固溶处理工艺适配性

XA铝合金的铸态组织通过Sb-La复合变质即可获得理想的颗粒状共晶硅，无需进行固溶处理，仅通过人工时效（150 °C×8 h）即可获得目标力学性能，完全适配压铸免热处理要求 [[S27,S45,S46]]。

## 局限性

Sb变质存在以下核心局限 [[S7,S5,S41]]：

1. **密度偏析风险**：Sb相对密度为6.67，是Al的2.5倍，必须采用Al-Sb中间合金方式加入，直接加纯Sb会引发严重偏析。
2. **添加量上限**：Sb添加量超过0.4%后会生成硬脆金属间化合物，导致合金力学性能下降。
3. **对冷却速度高度敏感**：砂型铸造或铸件壁厚超过40~50 mm时冷却速度不足，变质效果大幅衰减，甚至失效。
4. **与Na、Sr不相容**：含有Na、Sr的回炉料不可直接用于Sb变质的合金体系，二者会反应生成Na₃Sb等金属间化合物，完全抵消各自的变质效果，使共晶硅重新粗化 [[S44,S24]]。
5. **磷的干扰**：当P含量超过20×10⁻⁶时，常规添加量范围内的Sb完全无法实现有效变质 [[S9]]。
6. **高温固溶处理变色**：Sb变质铝合金经高温固溶处理后表面会生成含Sb的黑色氧化层，影响铸件表观质量，后续需要抛丸或机加工去除 [[S7]]。

## 与Na、Sr变质剂的多维度对比

| 对比维度 | Na变质 | Sr变质 | Sb变质 |
|---|---|---|---|
| 变质后共晶硅形貌 | 细粒状 | 纤维状 | 细片状/粒状 |
| 推荐添加量 | 0.01%~0.02% | 0.04%~0.06% | 0.2%~0.3% |
| 变质有效时长 | 30~60 min | 6~7 h | 最长100 h以上，重熔不失效 |
| 适配合金体系 | 砂型/慢冷厚壁Al-Si合金 | 亚共晶/共晶Al-Si合金（不可用于过共晶） | 金属型/压铸快冷薄壁亚共晶Al-Si合金 |
| 氯盐除气兼容性 | 不可 | 不可 | 可耐受 |
| 烧损特性 | 严重烧损 | 易烧损 | 几乎无烧损 |
| 对坩埚腐蚀 | 严重 | 轻微 | 无侵蚀 |
| 变质剂类型 | 钠类变质剂 | 钠类变质剂 | 碲-锑类变质剂 |

*表来源* [[S16,S41,S34]]

## XA铝合金应用案例

### 合金背景

XA铝合金是2025年公开发表的学位论文中首次提出的实验型免固溶处理Al-Si-Zn-Mg-Cu系铸造/压铸铝合金，不属于通用标准牌号序列，尚无公开商业化的牌号注册记录 [[S25,S1,S27]]。其公开成分范围为：Si 8.0~9.0 wt.%、Zn 2.5~3.5 wt.%、Mg 1.8~2.3 wt.%、Cu 0.5~0.7 wt.%，同时添加微量Sb、La、Zr作为微合金化元素 [[S27,S45]]。

### 铸造工艺性能与力学性能

- **流动性**：添加Sb和La后，705 °C浇注时螺旋线长度从无添加时的557 mm提升至1154 mm，724 °C时可达1346 mm [[S4]]。
- **体收缩率**：相同浇注温度747 °C下，液体收缩率从0.033%/°C降至0.028%/°C [[S17]]。
- **热裂倾向**：无论是否添加Sb和La，XA铝合金热裂约束试样中均未观察到热裂现象，该合金本身热裂倾向较低 [[S27,S19]]。
- **重力铸造+时效**：抗拉强度264 MPa [[S10]]。
- **压铸铸态**：抗拉强度约275 MPa，延伸率约8% [[S31]]。
- **压铸+时效**：抗拉强度293 MPa [[S31]]。

## 相关标准中对Sb含量的规定

现行可查的主流压铸铝合金相关标准中涉及Sb元素管控的包括 [[S35,S28,S32]]：

- 中国GB 1173-86《铸造铝合金技术条件》
- ISO 3522:1984《铸造铝合金 化学成分和力学性能》
- 美国ASTM B85/B85M《铝合金压铸件》

工业常规管控要求压铸铝合金中Sb作为变质元素的允许添加下限≥0.05%，超过0.5%会作为杂质元素限制含量 [[S28]]。

## Sources
- S39: [原铝及其合金的熔铸生产问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1f86c3a-591b-429d-bc06-a4136a16517e/resource) (`d1f86c3a-591b-429d-bc06-a4136a16517e`)
- S44: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f03f75df-dd74-499c-b0d4-8fa241c37bc2/resource) (`f03f75df-dd74-499c-b0d4-8fa241c37bc2`)
- S24: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8133575e-ab69-4ad3-b5cb-a378ad55b130/resource) (`8133575e-ab69-4ad3-b5cb-a378ad55b130`)
- S20: [铝及铝合金工艺与设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ab657d9-8eb5-4d83-b4e0-f1dbfb71beda/resource) (`6ab657d9-8eb5-4d83-b4e0-f1dbfb71beda`)
- S26: [aluminum and aluminum alloys introduction and overview__ca28de7c4d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84c39fa6-e993-41e9-80b2-f96aa3fdc17e/resource) (`84c39fa6-e993-41e9-80b2-f96aa3fdc17e`)
- S30: [84962_锑](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9fc056cd-935a-4dd4-8916-44a66248e441/resource) (`9fc056cd-935a-4dd4-8916-44a66248e441`)
- S29: [铝合金熔炼理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97367baa-3419-427b-a4e9-45c843ba149d/resource) (`97367baa-3419-427b-a4e9-45c843ba149d`)
- S37: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c187d6e6-9c80-4370-be1f-88502ff90748/resource) (`c187d6e6-9c80-4370-be1f-88502ff90748`)
- S22: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70f677d8-5acb-463f-bfe1-1a10e53911ca/resource) (`70f677d8-5acb-463f-bfe1-1a10e53911ca`)
- S6: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2349dfa3-0ea7-43ac-883d-f605de051abc/resource) (`2349dfa3-0ea7-43ac-883d-f605de051abc`)
- S8: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2822381f-26e3-4f15-a365-2937fba8c9f0/resource) (`2822381f-26e3-4f15-a365-2937fba8c9f0`)
- S42: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d95596fd-86e6-4b43-ba0a-e32d95e04010/resource) (`d95596fd-86e6-4b43-ba0a-e32d95e04010`)
- S43: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1dc5f3f-2626-480c-bf2e-685731b58b69/resource) (`e1dc5f3f-2626-480c-bf2e-685731b58b69`)
- S46: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa3f28cc-4445-4e30-8fcb-5334716bb4f3/resource) (`fa3f28cc-4445-4e30-8fcb-5334716bb4f3`)
- S15: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5657acf2-a183-4cfa-a40d-738122653712/resource) (`5657acf2-a183-4cfa-a40d-738122653712`)
- S3: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/181534b5-53c4-4e60-9f11-805dabc654a0/resource) (`181534b5-53c4-4e60-9f11-805dabc654a0`)
- S2: [La和Sb协同变质处理XA铝合金共晶硅颈部熔化熔断示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c4d25c5-5b46-4d0d-940f-00c3a730e96e/resource) (`0c4d25c5-5b46-4d0d-940f-00c3a730e96e`)
- S13: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/386e35ee-3edf-4abb-9bc1-d8a70d916ddf/resource) (`386e35ee-3edf-4abb-9bc1-d8a70d916ddf`)
- S33: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a67d2118-4cf6-4693-9052-bb9445975310/resource) (`a67d2118-4cf6-4693-9052-bb9445975310`)
- S21: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70a5f420-a16b-4251-8df3-6b57ab1ea522/resource) (`70a5f420-a16b-4251-8df3-6b57ab1ea522`)
- S4: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20c1f396-a0df-4829-b492-b910e999686e/resource) (`20c1f396-a0df-4829-b492-b910e999686e`)
- S17: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ebb5628-8e37-416e-9a8d-7289678bb4d8/resource) (`5ebb5628-8e37-416e-9a8d-7289678bb4d8`)
- S11: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32ad217f-92d1-471a-a728-c5037737b45a/resource) (`32ad217f-92d1-471a-a728-c5037737b45a`)
- S18: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/661fe848-8b6f-44e9-8739-40e8f6ef7724/resource) (`661fe848-8b6f-44e9-8739-40e8f6ef7724`)
- S27: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/868b6659-e040-40c9-9ba4-ad3ab61c8a09/resource) (`868b6659-e040-40c9-9ba4-ad3ab61c8a09`)
- S10: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/322c5213-a46b-43d8-baa5-9551435fa819/resource) (`322c5213-a46b-43d8-baa5-9551435fa819`)
- S31: [图6-31. 压铸添加La和Sb的XA铝合金油箱支架铸件试片力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9fdffcce-656e-4e5b-8fb5-a735051627f1/resource) (`9fdffcce-656e-4e5b-8fb5-a735051627f1`)
- S7: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/260befe1-db1d-4a55-a7d4-ffde008cd6cc/resource) (`260befe1-db1d-4a55-a7d4-ffde008cd6cc`)
- S5: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/228fa49e-7e34-4f24-9a27-2dff1a824ae5/resource) (`228fa49e-7e34-4f24-9a27-2dff1a824ae5`)
- S40: [铝合金材料组织与金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d208403d-5877-46b5-8e2e-f6fe5efdd990/resource) (`d208403d-5877-46b5-8e2e-f6fe5efdd990`)
- S45: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa110dec-959a-459a-ae24-76ef8835aa89/resource) (`fa110dec-959a-459a-ae24-76ef8835aa89`)
- S41: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d8c9e7a9-20eb-400a-9849-0952a2757515/resource) (`d8c9e7a9-20eb-400a-9849-0952a2757515`)
- S9: [图6-17 P, Sr对Sb变质效果的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/303a7562-4167-4231-a2d0-761b45324b24/resource) (`303a7562-4167-4231-a2d0-761b45324b24`)
- S16: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e9aeba5-b37a-4e58-a41e-cacf57d4f2a5/resource) (`5e9aeba5-b37a-4e58-a41e-cacf57d4f2a5`)
- S34: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0ece7f2-6d7b-4e8b-9355-f8bee3c23e42/resource) (`b0ece7f2-6d7b-4e8b-9355-f8bee3c23e42`)
- S25: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8445f69b-d258-4448-b271-9f1e741dad62/resource) (`8445f69b-d258-4448-b271-9f1e741dad62`)
- S1: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03c179cb-825f-4bc6-ae75-315fada997cd/resource) (`03c179cb-825f-4bc6-ae75-315fada997cd`)
- S19: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6643981c-fdeb-4e31-bf48-a1d19c156cfd/resource) (`6643981c-fdeb-4e31-bf48-a1d19c156cfd`)
- S35: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbdfd10d-500b-41dd-bd20-5ac0efd8c501/resource) (`bbdfd10d-500b-41dd-bd20-5ac0efd8c501`)
- S28: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8eda58ac-d805-4f43-942e-22f09c0d3096/resource) (`8eda58ac-d805-4f43-942e-22f09c0d3096`)
- S32: [alloys preparation properties applications__06ebcb5ca6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a40549ba-0de0-447d-b6e5-260f0586309b/resource) (`a40549ba-0de0-447d-b6e5-260f0586309b`)