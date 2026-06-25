---
version: "v1"
generated_at: "2026-06-18T12:59:08+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 40
  source_quality_score: 0.87
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 概述

Al-Mg系铸造合金是铸造铝合金四大核心系列之一（与Al-Si系、Al-Cu系、Al-Zn系并列），以镁为主要合金元素 [[S43,S31]]。该系在铝合金大分类中完全独立于以5xxx系列为代表的变形Al-Mg合金体系，二者在牌号命名规则、成分设计目标与制造工艺路线上存在明确区分 [[S4]]。

Al-Mg系压铸合金的典型性能特征为：室温力学性能好、抗蚀性强，但铸造性能较差，力学性能的波动幅度和壁厚效应都较为显著，长期使用过程中会因时效作用导致塑性下降，压铸件应力腐蚀裂纹的倾向相对较高 [[S29,S21,S18]]。

## 分类与牌号

### 各国标准体系中的定位

各国压铸铝合金标准体系普遍依据主要合金元素进行分类，Al-Mg系在其中均占有独立地位 [[S43]]：

| 标准体系 | Al-Mg系标识规则 | 说明 |
|---------|---------------|------|
| 中国 GB/T 15115 | YL+3××（首位数字3） | 压力铸造铝合金锭，首位数字3对应Al-Mg系 [[S45,S43]] |
| 美国 AA/ANSI | 5xx.x | 首位数字5表示Mg为主要合金元素，后缀.0为铸件、.1/.2为铸锭 [[S4,S32]] |
| 欧洲 EN 1706 | EN AC-5xxxx | 数字牌号首位5统一对应Al-Mg系，如EN AC-51300 [[S44,S20]] |
| 日本 JIS | ADC5、ADC6 | ADC5为Al-Mg系，ADC6为Al-Mg-Mn系 [[S13,S14]] |

### 典型压铸用Al-Mg合金牌号与成分

**AA 520.0**（砂型铸造用高Mg合金）成分范围：Si≤0.25%，Fe≤0.30%，Cu≤0.25%，Mn≤0.15%，Mg 9.5～10.6%，Zn≤0.15%，Ti≤0.25% [[S38]]。

**AA 518.0**（高压铸造专用）成分范围：Si≤0.35%，Fe≤1.8%，Cu≤0.25%，Mn≤0.35%，Mg 7.5～8.5%，Zn≤0.15% [[S38]]。

**AA 515.0**（高压铸造专用）成分范围：Si 0.5～1.0%，Fe≤1.3%，Cu≤0.20%，Mn 0.4～0.6%，Mg 2.5～4.0%，Zn≤0.10% [[S38]]。

Al-Mg系铸造合金存在明确的成分管控规则：若Fe元素质量分数超过0.45%，对应合金中Mg元素的含量不得低于Fe元素质量分数的1/2 [[S50]]。

## 力学性能

### Mg含量对力学性能的影响

高压压铸Al-Mg合金的力学性能与Mg含量密切相关：抗拉强度和屈服强度随Mg含量升高而逐步提升，延伸率在Mg质量分数约6%时达到峰值17.4%，Mg含量进一步增至10%时延伸率降至4.7%，仍优于商用压铸合金A383的3.5% [[S11,S40]]。

![压铸Al-Mg合金力学性能随镁含量变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/695ca6b6-cf74-47f9-a51c-b0649fb25ed5/resource)

### 典型合金与研发牌号的力学性能

| 合金牌号/代号 | 工艺条件 | 屈服强度 (MPa) | 抗拉强度 (MPa) | 伸长率 (%) | 来源 |
|-------------|---------|---------------|---------------|-----------|------|
| Magsimal-59 (AlMg5Si2Mn) | 高真空压铸，铸态 | ~160 | ~300 | 15 | [[S5]] |
| Magsimal-59 (AlMg5Si2Mn) | 高真空压铸，铸态 | >120 | — | >15 | [[S46]] |
| Al-5Mg-0.6Mn | 高压压铸 | >160 | >300 | >10 | [[S5]] |
| 国产AlMg5Si2Mn | 常规压铸态 | — | 324 | 8.31 | [[S46]] |
| A152 (Mg 3%) | 免热处理压铸 | 150 | 265 | 11 | [[S27]] |
| A153 (Mg 4%) | 免热处理压铸 | 170 | 280 | 9 | [[S27]] |
| SJTU-Al-Mg-Si-Mn | 免热处理压铸 | >180 | — | >10 | [[S34]] |
| SJTU-Al-Mg-Cu-Mn | 免热处理压铸 | >180 | >320 | >8 | [[S34]] |

![免热处理压铸SJTU-Al-Mg-Si合金力学性能雷达图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a189047-efb9-4500-b234-32fac4654c5e/resource)

### 壁厚效应

Al-Mg系合金的力学性能壁厚效应显著：厚大部位冷却慢，易产生缩松和晶粒粗大，且在液态停留时间较长，易氧化和与水汽反应而产生晶间氧化与气孔，导致厚壁处力学性能远低于薄壁处 [[S36,S29]]。压铸合金壁厚与强度的关系可用经验公式 S = a·t⁻ⁿ 描述（a、n为经验常数） [[S16]]。

以Magsimal-59为例，壁厚2 mm时伸长率仍高于14%、屈服强度可达200 MPa；当壁厚持续增加时，铸件内部粗大晶粒与缩松缺陷占比上升，强度和塑性同步大幅下降 [[S41,S16]]。

## 铸造性能

### 流动性与充型能力

Al-Mg系压铸合金流动性整体偏弱：合金凝固温度区间宽，Mg易氧化形成夹渣并提高熔体表面张力，导致流动充型能力远低于Al-Si系压铸合金 [[S17,S40]]。Mg含量对流动性影响显著：Mg质量分数在4%～6%时凝固区间最大，铸造性能最差；Mg质量分数提升至9%～10%时充型能力显著提升 [[S36,S17]]。Fe含量的增加可在一定程度上改善流动性 [[S40]]。

### 热裂倾向

Al-Mg系压铸合金整体热裂倾向较高，商用压铸手册评定其热裂抗性等级为较差级别 [[S18,S21,S29]]。热裂形成源于宽凝固温度区间下的糊状凝固特性，凝固末期晶间存在连续低熔点液膜，当凝固收缩产生的拉应力超过液膜的承载极限时发生热撕裂 [[S47,S23]]。

![不同Mg/Zn配比Al-Mg系合金的热裂宏观形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcf4ad69-aff1-4bce-8730-71b0e74e5eb7/resource)

### 缩松与气孔倾向

Al-Mg系合金结晶温度区间宽，呈典型糊状凝固模式，凝固过程中易形成孤立液相区，补缩困难，缩松倾向显著高于常规Al-Si系合金 [[S23]]。Mg元素高温下极易氧化烧损形成氧化渣，若熔体保护不当易导致气孔缺陷占比上升 [[S23,S46]]。生产中通常添加微量Be元素，在熔体表面形成致密BeO氧化膜以减少Mg氧化 [[S46]]。

## 应力腐蚀倾向

Al-Mg系压铸件存在显著的应力腐蚀开裂（SCC）倾向，长期使用过程中伴随自然时效塑性下降，可出现自发开裂 [[S18,S21,S29,S35]]。应力腐蚀敏感性随Mg含量升高而升高：当Mg质量分数超过3%～5%且铸件存在未消除的残余拉应力时，在含Cl⁻环境下发生应力腐蚀开裂的概率显著提升 [[S9]]。

## 工艺参数与缺陷控制

### 高压压铸推荐工艺参数

Al-Mg系高压压铸核心工艺参数推荐控制范围 [[S24,S42,S39]]：

| 参数 | 推荐范围 | 说明 |
|------|---------|------|
| 浇注温度 | 670～700 ℃ | 与模具温度匹配 |
| 模具温度 | 200～250 ℃ | 减小凝固过程温度差 |
| 压射速度 | 2～4 m/s | — |
| 增压压力 | 40～70 MPa | — |
| 留模时间 | 按3 s/mm壁厚设定 | 避免过早脱模或应力无法释放 |

### 热裂防控措施

工业常用Al-Mg系压铸热裂防控策略 [[S46,S24,S39]]：

- **成分层面**：Fe含量控制在0.15%以下，Cu含量低于0.03%，Na和Ca杂质含量均控制在10×10⁻⁶以下。
- **结构层面**：保证铸件壁厚均匀，不同壁厚过渡处圆角半径不小于1 mm，避免十字交叉热节。
- **工艺层面**：合理匹配浇注温度、模具温度、压射压力参数，采用铸造模拟软件预判热节位置并优化浇注排溢系统。

![铸件壁厚设计对比：不均壁厚易引发缩孔，均匀壁厚可抑制缺陷产生](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60816ca5-715b-4d85-af65-0cbdcf539e55/resource)

### 挤压铸造的工艺优势

Al-Mg系合金采用高压直接挤压铸造（液态模锻）工艺可克服其流动性差的短板，消除内部缩松、降低热裂倾向，使α固溶体和β相组织细化，溶质元素固溶度提升，合金塑性提升幅度显著高于其他铝合金系 [[S1,S3]]。挤压铸造工艺可在压力下结晶，细化组织和亚显微结构，提高塑性 [[S3]]。

## 与其他压铸铝合金的对比

### 四大压铸铝合金系核心性能对比

| 对比维度 | Al-Si系 | Al-Si-Mg系 | Al-Mg系 | Al-Zn-Mg系 |
|---------|--------|-----------|---------|-----------|
| 铸造性能 | 最优 | 次之 | 最差 | 一般 |
| 室温强度 | 中 | 中 | 中高 | 最高 |
| 伸长率 | 中 | 中 | 最高 | 中 |
| 耐蚀性 | 良好 | 良好 | 最优（尤其海水） | 差（应力腐蚀倾向高） |
| 阳极氧化适配性 | 差（硅相干扰） | 差（硅相干扰） | 最优 | 一般 |
| 热裂倾向 | 低 | 低 | 高 | 较高 |

Al-Mg系铸造性能最差，Al-Si系综合铸造性能最优 [[S13,S14,S8,S48]]。Al-Mg系耐蚀性远高于其余三类，在海水工况下表现最优 [[S13,S14]]。阳极氧化适配性方面，Al-Mg系可获得均匀光亮的高装饰性氧化膜，而含Si合金系因硬硅相存在难以生成连续均匀的外观氧化膜 [[S48,S8]]。

### 结构化类型对比

| 合金系 | 核心特性 | 适用场景 | 代表牌号 |
|-------|---------|---------|---------|
| Al-Si系 | 结晶温度区间小，流动性好，线收缩系数小 | 大型薄壁、密封要求高的零件 | YL102 |
| Al-Si-Cu系 | 强度、硬度、耐热性高，塑性、耐蚀性下降 | 高强度高硬度要求的汽车/机械零件 | YL112、ADC12 |
| Al-Mg系 | 耐蚀性、阳极氧化性突出，力学强度高，粘模性及热裂倾向大 | 高耐蚀要求、低温服役场景的零件 | YL302 |

[[S49]]

### Al-Mg系的核心选型价值

尽管Al-Mg系压铸合金铸造性能较差，其兼具以下核心优势而仍被选择应用 [[S26,S48,S8]]：

- 所有常规压铸铝合金中最优异的海水耐腐蚀性能
- 最高的断后伸长率
- 优良的切削加工性能
- 阳极氧化后可生成无硅相干扰的均匀高亮装饰性氧化膜

## 工业应用

### 汽车工业

高真空压铸高强韧Al-Mg系合金（如Magsimal-59/AlMg5Si2Mn）已成功应用于汽车结构件制造 [[S47,S10]]：

- Porsche Panamera 减振塔
- BMW 5系 (E60) 减振塔
- 汽车方向盘骨架、后副车架等碰撞安全类结构件

免热处理Al-Mg系压铸合金目前工业应用成熟度与占比相对较低，工艺窗口窄、热裂倾向大，对模具和工艺设计要求远高于Al-Si系 [[S10,S47]]。

### 船舶与海洋工程

Al-Mg系合金因其优异的耐海水腐蚀性能，可用于船壳体、上层结构及海洋工程装备部件的制造 [[S15,S12]]。

### 3C电子领域

用于要求高阳极氧化外观效果的消费电子装饰外壳 [[S12,S13]]。

## Sources
- S43: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce2d13e-413c-4061-9d2d-8e1edc9e49c7/resource) (`dce2d13e-413c-4061-9d2d-8e1edc9e49c7`)
- S31: [工程材料应用技术丛书轻合金及其工程应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6c1c0a2-6e5c-40cf-9a93-9441492b867d/resource) (`a6c1c0a2-6e5c-40cf-9a93-9441492b867d`)
- S4: [aluminum and aluminum alloys introduction and overview__ca28de7c4d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0fc2720d-8de4-4a2b-bf18-e193bfc410e6/resource) (`0fc2720d-8de4-4a2b-bf18-e193bfc410e6`)
- S29: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f728044-844f-4f0e-9fc4-206efa1271c9/resource) (`8f728044-844f-4f0e-9fc4-206efa1271c9`)
- S21: [立式压铸机用压铸模和挤铸模65例设计应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62afe511-56d3-423a-b626-ea71e3060ebc/resource) (`62afe511-56d3-423a-b626-ea71e3060ebc`)
- S18: [卧式压铸机用压铸模69例设计应用评析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5de4ea80-6b4d-4275-86ce-4989556758d2/resource) (`5de4ea80-6b4d-4275-86ce-4989556758d2`)
- S45: [原铝及其合金的熔铸生产问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e09a4c28-6734-41e7-b209-a02e618fb982/resource) (`e09a4c28-6734-41e7-b209-a02e618fb982`)
- S32: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a82c859b-a8a2-48e0-9ea5-4a17a7bec437/resource) (`a82c859b-a8a2-48e0-9ea5-4a17a7bec437`)
- S44: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dfcc7517-86fc-4acd-8a45-8ab0981620f9/resource) (`dfcc7517-86fc-4acd-8a45-8ab0981620f9`)
- S20: [companion guide to the asme boiler and pressure vessel codes volume 1 cr__d22a1f45b3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6203b91b-58c6-46cd-a29b-d3b056125104/resource) (`6203b91b-58c6-46cd-a29b-d3b056125104`)
- S13: [铝与铝合金材料生产技术500问](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/554fa922-5344-4271-bfbb-c0822929ce29/resource) (`554fa922-5344-4271-bfbb-c0822929ce29`)
- S14: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57384ca3-aae6-4bcd-aef8-8721146b1d53/resource) (`57384ca3-aae6-4bcd-aef8-8721146b1d53`)
- S38: [AA标准铸造用铝锭的牌号与化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4551102-0952-40b3-ac50-1bf7463aa78b/resource) (`d4551102-0952-40b3-ac50-1bf7463aa78b`)
- S50: [TextNode79](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6fb6ec9-7b56-4ed2-bef8-5048d1f86d04/resource) (`f6fb6ec9-7b56-4ed2-bef8-5048d1f86d04`)
- S11: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3093af9a-5478-4455-8b66-655aaae5de4b/resource) (`3093af9a-5478-4455-8b66-655aaae5de4b`)
- S40: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d79d6783-251a-4081-b170-88c66be849b4/resource) (`d79d6783-251a-4081-b170-88c66be849b4`)
- S5: [effect of cu addition on microstructures and tensile properties of high__15b7a22a5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13c99d7b-cb80-44b8-9021-45c9211587fb/resource) (`13c99d7b-cb80-44b8-9021-45c9211587fb`)
- S46: [高真空压铸铝合金的研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6671015-f1fb-46ad-b2f7-37b8bb013531/resource) (`e6671015-f1fb-46ad-b2f7-37b8bb013531`)
- S27: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e5d9c75-cd36-46f5-8229-1dbe88768591/resource) (`7e5d9c75-cd36-46f5-8229-1dbe88768591`)
- S34: [新能源汽车用铸造铝合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3e239e5-3d45-4bad-bb8e-3879290cc7bd/resource) (`b3e239e5-3d45-4bad-bb8e-3879290cc7bd`)
- S36: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cdf97ad7-2d86-4491-9337-8052b3cae343/resource) (`cdf97ad7-2d86-4491-9337-8052b3cae343`)
- S16: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b7b663e-684c-4678-a230-bc6ac15dbdc7/resource) (`5b7b663e-684c-4678-a230-bc6ac15dbdc7`)
- S41: [automotive alloys 1999__dbd41f2733](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da8661e3-8fcf-4de5-8ea6-98c739bde7d8/resource) (`da8661e3-8fcf-4de5-8ea6-98c739bde7d8`)
- S17: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c336558-b411-491c-a3a1-f2a085d33544/resource) (`5c336558-b411-491c-a3a1-f2a085d33544`)
- S47: [乘用车白车身铝合金压铸结构件及材料应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8eefccf-1176-412c-9ff2-72476afcedce/resource) (`e8eefccf-1176-412c-9ff2-72476afcedce`)
- S23: [免热处理铝合金大型结构件一体压铸研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/728088b9-8125-4c49-b8a8-72653362f8ec/resource) (`728088b9-8125-4c49-b8a8-72653362f8ec`)
- S35: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b604f172-589a-4f1c-91b9-c94585a5cc20/resource) (`b604f172-589a-4f1c-91b9-c94585a5cc20`)
- S9: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d6f27b1-0ec1-4ac0-b330-e61963df30ff/resource) (`2d6f27b1-0ec1-4ac0-b330-e61963df30ff`)
- S24: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74e1256a-a6f1-442e-858d-2667a2c5fa63/resource) (`74e1256a-a6f1-442e-858d-2667a2c5fa63`)
- S42: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/daa451b2-cd9a-40ae-b091-0cdf7aed38d1/resource) (`daa451b2-cd9a-40ae-b091-0cdf7aed38d1`)
- S39: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d590b819-17e2-4330-aac4-639dfa21e6e2/resource) (`d590b819-17e2-4330-aac4-639dfa21e6e2`)
- S1: [自行车铝合金结构件液态模锻及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0288ebac-42e5-4cf6-8d3c-1145a4fdc674/resource) (`0288ebac-42e5-4cf6-8d3c-1145a4fdc674`)
- S3: [液态模锻与挤压铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ccea6ef-b710-4fd7-bd00-6aa3df06c7fb/resource) (`0ccea6ef-b710-4fd7-bd00-6aa3df06c7fb`)
- S8: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23d65afd-66a9-43d8-8a8a-6469fcd2d3e6/resource) (`23d65afd-66a9-43d8-8a8a-6469fcd2d3e6`)
- S48: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea79ab82-cb6a-4ff5-a6b7-65fc6aecf78b/resource) (`ea79ab82-cb6a-4ff5-a6b7-65fc6aecf78b`)
- S49: [表1-1 各类压铸合金的特点及用途](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eae3df0f-7836-4817-9505-218a1a79b09f/resource) (`eae3df0f-7836-4817-9505-218a1a79b09f`)
- S26: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8aa5ba-8fbf-42f0-a36f-1d784dc2b3d4/resource) (`7b8aa5ba-8fbf-42f0-a36f-1d784dc2b3d4`)
- S10: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e8a5e3c-e794-452e-a49e-e5ef09bd5223/resource) (`2e8a5e3c-e794-452e-a49e-e5ef09bd5223`)
- S15: [铝与铝合金材料生产技术500问](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b50eadb-6e07-4b35-9a4c-689ca53b375b/resource) (`5b50eadb-6e07-4b35-9a4c-689ca53b375b`)
- S12: [表 C.1 压铸铝合金特点及应用举例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/552e31b3-c97a-44e6-b43f-164be4fa76c1/resource) (`552e31b3-c97a-44e6-b43f-164be4fa76c1`)