---
version: "v1"
generated_at: "2026-06-18T19:41:20+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 45
  source_quality_score: 0.85
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

CF8是ASTM A351标准中规定的一种奥氏体铸造不锈钢，属于铁-铬-镍系耐腐蚀铸钢。其ACI牌号命名规则中，首字母“C”表示耐腐蚀用途，数字“8”代表碳的最大百分含量为0.08%。CF8对应的UNS统一编号为J92600，通常被称为铸造304不锈钢，等效对应中国GB/T 2100标准中的06Cr19Ni10铸钢牌号[[S1,S39,S40]]。该材料广泛用于制造泵体、阀体、三通管件等承压耐腐蚀零部件[[S29,S25]]。

## 定义与分类

CF8属于耐腐蚀类（C类）奥氏体铸钢，是CF系列铸造不锈钢的最基础牌号之一[[S40]]。在ASTM标准体系下，CF8出现在A351、A743、A744等多个标准中，涵盖通用耐腐蚀用途、严重工况及承压零件用铸件[[S1]]。

与锻件相比，CF8是304不锈钢的铸造对应牌号。在ACI命名体系中，第二位字母“F”定位了该合金在Fe-Cr-Ni三元相图中镍和铬含量的近似位置。CF8的后续变体牌号通过附加字母标识特殊元素：如CF8M添加钼（Mo），CF8C添加铌（Nb）[[S40]]。

## 化学成分

CF8的标准化学成分按ASTM标准规定如下表所示。

| 元素 | C | Mn | Si | P | S | Cr | Ni | Mo |
|------|-----|------|-----|------|-----|------|------|-----|
| 质量分数 (%) | ≤0.08 | ≤1.5 | ≤2.0 | ≤0.040 | ≤0.040 | 18.0~21.0 | 8.0~11.0 | ≤0.50 |

*表：CF8化学成分限值（质量分数，%）[[S47,S8,S12]]*

铬是提供不锈钢耐腐蚀性的核心元素，能够在材料表面形成钝化氧化膜；镍的加入使合金获得奥氏体基体组织，保证优良的力学性能和工艺性能[[S6]]。

## 力学性能与物理性能

### 力学性能

CF8在室温下的最低力学性能要求如下表所示：

| 性能指标 | 最低要求值 |
|---------|-----------|
| 抗拉强度 | 485 MPa（70 ksi） |
| 0.2%条件屈服强度 | 205 MPa（30 ksi） |
| 断后伸长率（2英寸标距） | 35% |

*表：CF8室温最低力学性能[[S11,S48,S9]]*

### 物理性能

CF8（等效牌号ZG07Cr19Ni10）的室温密度为7.93 g/cm³。密度随温度升高而逐步降低，在约1400°C的固液相变区间出现明显突变，这一密度-温度曲线可直接用于铸造工艺模拟参数设置[[S39,S3]]。

CF8奥氏体不锈钢的另一关键物理特性是其线收缩率约为3.0%~3.2%，这一较高线收缩值是导致铸件热裂倾向的重要材料因素[[S19]]。

### 高温服役限制

CF8铸态组织中的δ铁素体相（体积分数约15%~20%）在300°C~400°C长期服役时，会发生调幅分解，形成富铁α相和富铬α'相的纳米级调制结构，同时析出G相复杂硅化物。这一相变过程导致材料的冲击韧性大幅下降，可降至初始值的约15%，形成严重的热老化脆化。ASME标准规定此类CF3A、CF8A等控铁素体CF铸件用于承压部件时，建议长期最高使用温度不超过425°C [[S35,S26]]。

### 微观组织特征

![CF8/CF8M铸态不锈钢热老化后的金相显微组织](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/247a11a2-f285-4f2a-b518-1c35e65a5ad5/resource)

*注：CF8/CF8M铸态不锈钢经热老化后析出的细密第二相颗粒，可用于说明长期高温服役后材料相变与力学性能退化的关联[[S14]]。*

## 铸造工艺

### 适用铸造方法

CF8主流适用砂型铸造和熔模铸造（失蜡铸造）工艺，工业生产中大量用于泵体、阀体等承压耐腐蚀零部件的制造[[S29,S25]]。CF8不适用于常规压力铸造，原因在于：其液相线温度在1500°C以上，高铬、镍含量的合金液易与压铸模具发生粘模反应，且高温钢液易冲蚀、熔损普通压铸钢模；同时，奥氏体不锈钢流动性较差，常规压铸的高压充型模式下难以获得高质量铸件[[S38,S6]]。

### 浇注温度区间

CF8的浇注温度根据铸造方法有所不同：

| 铸造方法 | 浇注温度区间 |
|---------|-------------|
| 砂型铸造 | 1530°C~1590°C |
| 常规熔模铸造 | 1600°C~1620°C |
| 复杂薄壁件熔模铸造 | 1670°C~1700°C（适当提高） |

*表：CF8常用浇注温度区间[[S49,S39]]*

浇注温度过低会导致金属液流动性不足，产生冷隔、浇不足等缺陷；适当提高浇注温度可改善流动性，但过高温度会增加氧化铬夹渣的产生倾向[[S6]]。

### 浇注系统设计要点

CF8浇注系统设计的关键原则包括：

1. **底注优先**：推荐采用底注式浇注系统，金属液自液面下平稳注入铸型，避免钢液在充型过程中飞溅氧化，形成氧化铬夹渣。大尺寸CF8铸件采用顶注易导致氧化物薄膜卷入，形成晶间弱化缺陷[[S45]]。顶注工艺仅适用于尺寸较小、结构简单的薄壁铸件。

2. **密封式浇注系统**：铬镍不锈钢的浇注系统截面面积通常比碳钢铸件大30%~50%，以补偿其较差的流动性[[S19]]。

3. **冒口设计**：CF8冒口的模数不低于铸件热节模数的1.2倍，整体冒口尺寸比同重量碳钢铸件的冒口大20%左右。优先选用保温冒口以提升补缩效率[[S6,S24]]。部分文献指出，CF8铸件的冒口尺寸需比碳钢件大30%~50%，方可保证顺序凝固和充分补缩[[S19,S30]]。

4. **冷铁协同**：在不易设置冒口的部位（如壁厚较厚的凸出处、壁与筋的交接处）合理布置冷铁，以实现顺序凝固[[S24]]。

### 凝固特性

CF8属于奥氏体不锈钢，凝固过程体积收缩率显著高于普通碳钢。热节分散位置易形成孤立液相区，缩孔缩松倾向性明显。必须通过冒口与冷铁的协同作用实现顺序凝固，使缩孔缺陷转移至冒口区域内，才能获得致密无缺陷的承压铸件[[S6]]。

## 热处理制度

CF8奥氏体不锈钢采用固溶热处理（也称固溶化处理）作为标准热处理制度。处理工艺为：将铸件加热至1050°C~1150°C区间充分保温，随后快速水冷淬火[[S46,S32]]。

固溶处理的核心作用是将铸态组织中沿晶界析出的Cr₂₃C₆碳化物充分溶解进入奥氏体基体，快速冷却后获得室温下的单相过饱和奥氏体组织，消除敏化风险，从而最大化保证材料的耐腐蚀性能、塑性和冲击韧性[[S50,S27]]。

## 缺陷机制与防控

CF8铸造奥氏体不锈钢在实际生产中常面临以下典型缺陷：

### 气孔

CF8钢液浇注过程中，铬元素易氧化生成氧化铬膜。浇注过程卷入的氢气及卷入性气体无法及时上浮逸出，易形成皮下气孔或分散分布的气孔缺陷。随着钢液温度降低，氢溶解度大幅下降，也可导致氢析出形成气孔[[S10,S41,S19]]。

**防控**：提高浇注温度、缩短浇注时间以减少金属液氧化和气体吸收；采用底注式浇注系统，使金属液平稳充型，避免气体卷入[[S6,S45]]。

### 缩孔与缩松

CF8体收缩大，凝固过程中若补缩不足，热节位置极易形成缩孔和缩松缺陷[[S19]]。

**防控**：冒口尺寸需比碳钢铸件大30%~50%，通过冒口与冷铁的协同作用实现顺序凝固[[S19,S30]]。对于阀体等结构复杂、热节分散的铸件，可采用ProCAST等数值模拟工具优化补缩工艺，确保缩松缺陷迁移至浇注系统部位[[S21,S13]]。

### 热裂

CF8线收缩率约为3.0%~3.2%，高温强度低。凝固末期接近固相线时，枝晶间残留液膜受收缩应力约束被拉裂，形成沿晶界扩展的曲折氧化态裂纹。热裂常出现在铸件拐角、截面突变处及热节区域[[S19,S20,S43]]。

**防控**：改善型（芯）砂的退让性以减小收缩阻力；合理设计铸件结构，避免截面突变；优化浇注系统，实现平稳充型和适宜的温度分布[[S19,S20]]。

![铸件冷却收缩应力分布与典型热裂位置示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56439f8e-6f91-482f-b2f6-eff2ce58f7a3/resource)

*注：铸造工艺示意图展示铸件冷却过程的收缩应力方向与热裂产生位置，可用于阀体类铸件热裂防控说明[[S22]]。*

### 夹杂

CF8钢液中的氧化物（Cr₂O₃为主）、熔渣、炉衬侵蚀剥落杂质、型壳冲蚀脱落的耐火材料颗粒易混入铸件形成非金属夹杂，降低铸件的韧性和承压能力，成为应力集中源[[S10,S33]]。

**防控**：熔炼时采用适当的脱氧处理和镇静时间；浇注系统中设置陶瓷过滤器；采用底注式浇注以减少氧化物卷入[[S10,S45]]。

### 阀体类铸件的质量检测

CF8阀体类承压铸件通常存在壁厚不均、热节分散的结构特点。内部缺陷需通过射线探伤检测，表面缺陷需采用渗透探伤排查，以确保承压工况下无超标缺陷泄漏风险[[S13,S51]]。

## C1113-S阀体铸造工艺优化

C1113-S阀体是CF8（304不锈钢）材质的典型承压铸件，单件质量6.41 kg，外部轮廓168×233×154 mm [[S39]]。

### 原始工艺问题

原始铸造工艺采用通用冒口顶注式浇注，存在两处对称孤立热节无法有效补缩的问题，导致铸件产生缩松、渗漏缺陷[[S15]]。

### 优化方案

某核心期刊报道的优化方案采用均衡凝固技术，具体措施如下[[S15,S44,S16]]：

1. **浇注姿态调整**：将铸件沿直通管中轴线旋转90°后重新设计浇注系统，使热节分布于铸件上方，调节凝固顺序。
2. **分区分段补缩**：针对两处对称热节（热节1、热节2，模数均为4 mm），设置圆柱形冒口分别单独补缩；针对两处邻近热节（热节3模数6.3 mm、热节4模数4.83 mm），采用腰圆形冒口共同补缩。
3. **工艺参数优化**：最优工艺参数为浇注温度1640°C、型壳预热温度1100°C、浇注时间10 s。浇注结束后将热壳底部浸水激冷5 s加速冷却，避免热量过分集中。

采用优化方案后，铸件经渗透检测无缩松、裂纹等缺陷，表面质量与承压性能达标，验证了均衡凝固技术在304不锈钢复杂铸件生产中的应用价值[[S16,S44]]。

![C1113-S阀体铸件三维模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4229377-0f98-4635-b4c0-5d51a2aaa563/resource)

*注：C1113-S阀体铸件三维模型图，材质为CF8（304不锈钢），用于初始浇注系统铸造仿真的前处理[[S36]]。*

## 焊接性能

CF8属于可焊性较好的奥氏体铸造不锈钢。焊接时推荐匹配AWS 308填充金属[[S17]]。由于CF8含碳量≤0.08%，焊接热影响区存在敏化析出Cr₂₃C₆碳化物导致晶间腐蚀的风险。如焊后不进行整体固溶退火处理，应优先选择超低碳填充金属以降低敏化倾向[[S2]]。

奥氏体不锈钢焊接接头在长期高温服役时存在焊缝金属蠕变断裂强度低于母材、蠕变塑性显著偏低的“冶金缺口”效应，需在焊缝布置设计时限制局部高应变区域[[S28]]。

## 应用与关联材料

### 典型应用

CF8广泛用于常规非强腐蚀工况下的承压耐腐蚀零部件，主要应用领域包括[[S48,S25,S29]]：

- 泵阀行业：泵体、阀体及配套管件
- 化工、石油行业：耐腐蚀流体输送部件
- 食品、医药行业：卫生级设备零部件
- 核电行业：辅助管道系统部件

### 与类似牌号对比

CF8（铸造304）、CF8M（铸造316）、CF3（铸造304L）、CF3M（铸造316L）是CF系列铸造奥氏体不锈钢的四个核心牌号，其主要差异对比如下：

| 对比项 | CF8 | CF8M | CF3 | CF3M |
|-------|-----|------|-----|------|
| 碳含量（%） | ≤0.08 | ≤0.08 | ≤0.03 | ≤0.03 |
| 钼添加 | 无 | 2%~3% Mo | 无 | 2%~3% Mo |
| 最低抗拉强度（MPa） | 485 | 485 | 485 | 485 |
| 最低屈服强度（MPa） | 205 | 205 | 205 | 205 |
| 最低伸长率（%） | 35 | 30 | 35 | 30 |
| 耐蚀特点 | 常规耐腐蚀 | 含Mo，耐氯离子点蚀和硫酸腐蚀 | 超低碳，抗敏化（耐晶间腐蚀） | 超低碳+含Mo，耐强腐蚀、海洋及酸性介质 |
| 典型应用 | 常规阀体、泵体承压件 | 中等腐蚀工况化工流体输送件 | 需焊接的抗敏化构件 | 强腐蚀海洋、酸性介质工况部件 |
| 相对成本 | 最低 | 较高 | 中等 | 最高 |

*表：CF8与CF8M、CF3、CF3M的对比[[S48,S7,S37,S18]]*

在沸腾65%硝酸环境中，固溶态的CF3（低碳）耐腐蚀性优于CF8 [[S7]]。CF8M和CF3M因含钼元素，在含氯离子和硫酸等腐蚀性介质中表现显著优于无钼的CF8和CF3 [[S37]]。

## Sources
- S1: [1991 annual book of astm standards section 1 lron and steel products vol__d9cf5303c8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/010ff58b-e5bd-424a-9e95-89281506f964/resource) (`010ff58b-e5bd-424a-9e95-89281506f964`)
- S39: [基于选区激光烧结的阀体快速铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0176460-fb2c-416e-ae28-b0e7729526d4/resource) (`c0176460-fb2c-416e-ae28-b0e7729526d4`)
- S40: [最新铸造标准应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd23a758-cde6-47c4-9bf8-cee0442d2db1/resource) (`cd23a758-cde6-47c4-9bf8-cee0442d2db1`)
- S29: [SPFH590高强钢异形三通管胀压复合成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/788500dc-6afe-44de-8843-ce80f9693479/resource) (`788500dc-6afe-44de-8843-ce80f9693479`)
- S25: [不锈钢泵体的熔模铸造工艺设计及参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f661786-a02c-4040-9476-8079d868edbd/resource) (`5f661786-a02c-4040-9476-8079d868edbd`)
- S47: [表1 CF8化学成分（质量分数，%）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0ce1433-c379-4c16-8ea7-70a8d8bf9cc2/resource) (`f0ce1433-c379-4c16-8ea7-70a8d8bf9cc2`)
- S8: [Table 1: Chemical Composition Requirements for Various Stainless Steel Castings](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12fdba06-18c7-4c9b-b8a4-24a3038ab454/resource) (`12fdba06-18c7-4c9b-b8a4-24a3038ab454`)
- S12: [承压用奥氏体钢的牌号和化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/195e4ae9-7743-466e-a28d-13af2d3281c3/resource) (`195e4ae9-7743-466e-a28d-13af2d3281c3`)
- S6: [自吸式泵体铸件铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0bf1e318-d615-42eb-a4fc-5d8dcc5046d6/resource) (`0bf1e318-d615-42eb-a4fc-5d8dcc5046d6`)
- S11: [0022_599b6a52d8cf0648_Steel_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/17ae44b3-71d1-44b9-b309-7fe059d98ea0/resource) (`17ae44b3-71d1-44b9-b309-7fe059d98ea0`)
- S48: [CF 系列及类似不锈钢铸件机械性能要求表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3c92ed0-cf2c-4701-8996-2fa091468176/resource) (`f3c92ed0-cf2c-4701-8996-2fa091468176`)
- S9: [美国高温用奥氏体不锈钢的力学性能表（ASTM A351/A351M）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15bde081-c050-4f7b-9b1c-8b9b25f03c52/resource) (`15bde081-c050-4f7b-9b1c-8b9b25f03c52`)
- S3: [图2.1 ZG07Cr19Ni10铸钢密度曲线; Fig.2.1 Density curve of ZG07Cr19Ni10 cast steel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/089be944-ac23-406d-957d-2bf5551ea2d4/resource) (`089be944-ac23-406d-957d-2bf5551ea2d4`)
- S19: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/463be8dd-b333-48ed-a280-b7786478d756/resource) (`463be8dd-b333-48ed-a280-b7786478d756`)
- S35: [characterization of defects in materials symposium held december 1 2 198__8187998853](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3de5868-93ed-44f3-b338-aaee1515bdc3/resource) (`a3de5868-93ed-44f3-b338-aaee1515bdc3`)
- S26: [最新铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/714109a1-8906-4c4f-9da6-e670311d2939/resource) (`714109a1-8906-4c4f-9da6-e670311d2939`)
- S14: [Micrograph of aged cast stainless steel microstructure](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/247a11a2-f285-4f2a-b518-1c35e65a5ad5/resource) (`247a11a2-f285-4f2a-b518-1c35e65a5ad5`)
- S38: [0006_dfbb858b59ef68e8_冒口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8905c0e-9d98-4325-aeda-db4a6f9ecd03/resource) (`b8905c0e-9d98-4325-aeda-db4a6f9ecd03`)
- S49: [自吸式泵体铸件铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f659498a-f5dc-48b2-99a6-fb353d124cec/resource) (`f659498a-f5dc-48b2-99a6-fb353d124cec`)
- S45: [钢铸件的浇注系统](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb06831a-4975-4479-bccc-c74eb7b1dd48/resource) (`eb06831a-4975-4479-bccc-c74eb7b1dd48`)
- S24: [自吸式泵体铸件铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a233fde-0734-4c20-8f65-a6bba16fc058/resource) (`5a233fde-0734-4c20-8f65-a6bba16fc058`)
- S30: [不锈钢泵体初始铸造工艺方案2缩孔缩松缺陷模拟位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/797b8b35-8a85-4cb6-809c-8a0d1bef1c89/resource) (`797b8b35-8a85-4cb6-809c-8a0d1bef1c89`)
- S46: [10918801_固溶处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f037d593-8f11-4752-b75f-1800f81274a1/resource) (`f037d593-8f11-4752-b75f-1800f81274a1`)
- S32: [10918801_固溶处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90ae36ed-9210-4506-8d3c-b0c9bc426892/resource) (`90ae36ed-9210-4506-8d3c-b0c9bc426892`)
- S50: [basic engineering metallurgy__96f2179710](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f92c9409-91cc-4f87-a78e-c286f7a4e22e/resource) (`f92c9409-91cc-4f87-a78e-c286f7a4e22e`)
- S27: [10918801_固溶处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7691cd4e-2cf2-449b-8678-4c48a4ded415/resource) (`7691cd4e-2cf2-449b-8678-4c48a4ded415`)
- S10: [0001_8a205c06e73297bc_铸造缺陷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16e689ae-a21c-4020-9565-8499333d1034/resource) (`16e689ae-a21c-4020-9565-8499333d1034`)
- S41: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d7ec28fb-a054-4ac1-87ed-9a26340d6bf2/resource) (`d7ec28fb-a054-4ac1-87ed-9a26340d6bf2`)
- S21: [a k3=1.6 时模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53215d88-6063-48f2-aa7e-8f63b1eace07/resource) (`53215d88-6063-48f2-aa7e-8f63b1eace07`)
- S13: [885807_液态成形](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ed983ef-9c55-4244-b093-64f7abdb88f5/resource) (`1ed983ef-9c55-4244-b093-64f7abdb88f5`)
- S20: [热加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49af83ad-0788-45d4-80da-5c51fa9bf178/resource) (`49af83ad-0788-45d4-80da-5c51fa9bf178`)
- S43: [金属液态成型原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e201192f-2136-4c45-a5cc-2f6239aeaf81/resource) (`e201192f-2136-4c45-a5cc-2f6239aeaf81`)
- S22: [Fig.5.27 Hot tear in castings](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56439f8e-6f91-482f-b2f6-eff2ce58f7a3/resource) (`56439f8e-6f91-482f-b2f6-eff2ce58f7a3`)
- S33: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91e3dba9-4ff9-4c47-bf7d-9dd22b83f3d7/resource) (`91e3dba9-4ff9-4c47-bf7d-9dd22b83f3d7`)
- S51: [不锈钢泵体的熔模铸造工艺设计及参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd6d4b50-ef92-4306-b369-cd1b13d79481/resource) (`fd6d4b50-ef92-4306-b369-cd1b13d79481`)
- S15: [基于选区激光烧结的阀体快速铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26d86d74-ffc2-4c7c-99e9-7ef214aa0d88/resource) (`26d86d74-ffc2-4c7c-99e9-7ef214aa0d88`)
- S44: [基于选区激光烧结的阀体快速铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6e1e388-98ed-4216-9075-21dfd633f76b/resource) (`e6e1e388-98ed-4216-9075-21dfd633f76b`)
- S16: [基于选区激光烧结的阀体快速铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a7edf9d-e0a1-486d-8efd-8bac68d15f4a/resource) (`2a7edf9d-e0a1-486d-8efd-8bac68d15f4a`)
- S36: [C1113-S阀体铸件三维模型图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4229377-0f98-4635-b4c0-5d51a2aaa563/resource) (`b4229377-0f98-4635-b4c0-5d51a2aaa563`)
- S17: [推荐用于铸造不锈钢的填充金属（AWS 代号）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ae52221-cd9b-405b-ae44-b777d8bde1d7/resource) (`3ae52221-cd9b-405b-ae44-b777d8bde1d7`)
- S2: [an introduction to metallurgy__dd8d7db1a2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/043e3517-e6ff-46d0-8d26-79ea616d7ab1/resource) (`043e3517-e6ff-46d0-8d26-79ea616d7ab1`)
- S28: [companion guide to the asme boiler and pressure vessel codes volume 1 cr__d22a1f45b3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76bbfe9d-eee8-4ede-851b-e3a041b00ac7/resource) (`76bbfe9d-eee8-4ede-851b-e3a041b00ac7`)
- S7: [不同铁素体含量的CF系列合金在沸腾65%硝酸中的腐蚀速率表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d305cde-b902-4649-ab99-8aa7e12f9ac0/resource) (`0d305cde-b902-4649-ab99-8aa7e12f9ac0`)
- S37: [不同铁素体含量的CF系列合金在沸腾65%硝酸中的平均腐蚀速率](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b48722d5-1ff5-49c5-ba25-1efe99e37c1d/resource) (`b48722d5-1ff5-49c5-ba25-1efe99e37c1d`)
- S18: [Table 2: Tensile, Yield, Elongation, and Reduction of Area Requirements for Various Steel Grades Used in Castings](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42c4f51f-9df2-49fc-81d4-656b2c9b5714/resource) (`42c4f51f-9df2-49fc-81d4-656b2c9b5714`)