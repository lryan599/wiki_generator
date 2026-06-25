---
version: "v1"
generated_at: "2026-06-18T13:06:17+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.87
  freshness_score: 0.78
  evidence_coverage_score: 1.0
---

## 概述

硅（Silicon，元素符号 Si，原子序数 14）是压铸铝合金中用量最大、影响最核心的合金元素。在常规添加实践中，硅常以纯硅或铝硅中间合金的形式引入铝熔体[[S13, S22]]。Al-Si 合金是压铸生产中应用最广泛的合金体系，硅元素在该体系中对流动性、凝固收缩、热裂倾向、力学性能及物理性能均产生深刻影响。

**关于别名“铆接性能”**：现有研究表明，硅含量不直接决定合金的铆接性能，“铆接性能”与硅含量之间不存在直接的因果关系。硅含量升高主要通过降低合金延伸率（塑性）间接影响铆接过程中产生的裂纹密度，该别名相关表述存在不严谨歧义[[S5, S21]]。

![硅元素符号圆形标识](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10cef0bd-8120-4766-a40f-d9da63f163f0/resource)

图1 硅（Si）元素符号标识图，用于压铸铝合金中 Si 元素的基础属性展示[[S3]]。

## 基础属性

| 属性 | 数值 / 说明 |
|------|------------|
| 元素符号 | Si |
| 原子序数 | 14 |
| 熔点 | 1414 ℃ |
| 沸点 | 2355 ℃ |
| 密度 | 2.34 g/cm³ |
| 在 Al 中最大固溶度（577 ℃） | 1.65 wt% |
| 在 Al 中室温固溶度 | 约 0.05 wt% |
| 常规添加形式 | 纯硅、铝硅中间合金 |
| 凝固潜热 | 约为同体积铝的 4.5 倍 |
| 推荐添加范围（压铸铝合金） | 4～13 wt% |
| 线膨胀系数相对铝 | 约为铝的 1/3～1/4 |

来源：[[S44, S13, S22, S6, S17, S43]]

## 分类与含量规范

### 按硅含量分类

按中国标准术语，铝硅合金的官方分类如下[[S20, S30, S45]]：

| 类别 | 硅含量范围 | 凝固组织特征 |
|------|----------|-------------|
| 亚共晶铝硅合金 | < 12 wt% | α-Al 初晶 + 共晶(α-Al + Si) |
| 共晶铝硅合金 | ≈ 12 wt%（理论共晶点 12.6 wt%） | 全共晶组织(α-Al + Si) |
| 过共晶铝硅合金 | > 12 wt% | 初生 Si + 共晶(α-Al + Si) |

### 典型压铸铝合金牌号硅含量

| 标准体系 | 牌号 | 硅含量 (wt%) | 所属系列 |
|---------|------|-------------|---------|
| JIS H5302 | ADC12 | 9.6～12.0 | Al-Si-Cu |
| ASTM B85 | A380 | 7.5～9.5 | Al-Si-Cu |
| ASTM | A356.0 | 6.5～7.5 | Al-Si-Mg |
| GB/T 15115-2024 | YL113 | 9.6～12.0 | Al-Si-Cu |

来源：[[S2, S15, S41]]

### 压铸铝合金牌号中硅含量标注规则

在中国国家标准中，牌号采用“YZ+基体元素符号+合金元素符号及名义百分含量”的方式命名。以 YZAlSi10Mg 为例：YZ 表示压铸合金，Al 为基体铝元素，Si10 表示硅（Si）且名义质量分数为 10%，Mg 为镁元素[[S34, S31]]。

![压铸铝合金牌号表示方法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0a42b3d-9adb-4bfa-9972-b262f6f160d9/resource)

图2 压铸铝合金牌号表示方法示意图，以 YZAlSi10Mg 为例标注各符号含义，可直观理解牌号中硅含量标注规则[[S34, S31]]。

## 工艺作用与铸造性能

### 对流动性的影响

硅是改善压铸铝合金流动性的核心元素。其作用机制包括[[S22, S25]]：

- 高凝固潜热：硅的凝固潜热约为同体积铝的 4.5 倍，可明显延长熔体可流动时间；
- 凝固温度区间变窄：随硅含量增加，合金凝固温度区间逐步收窄，有利于保持熔体充型能力。

流动性随硅含量变化的非线性规律如下：

- 硅含量在约 5 wt% 时流动性出现最低值[[S25, S19]]；
- 硅含量在 7～18 wt% 区间内可获得优良流动性[[S19, S6]]；
- 共晶成分（平衡态 12.6 wt% Si）附近合金流动性显著提升；
- 在压铸非平衡凝固条件下，Al-Si 合金共晶点向高硅侧偏移，流动性峰值对应的硅含量可移至 14～18 wt% 区间，峰值可达平衡共晶成分的 1.3 倍以上[[S25, S14, S32]]。

定量示例：高压铸造条件下，亚共晶 Al-Si 合金在相同过热度（液相线+80 ℃）条件下，硅含量从 7 wt% 提升至 10 wt% 时，6 mm×2 mm 截面流道中流动距离由 507 mm 增至 603 mm，提升幅度达 19.3%；硅含量超过 9 wt% 后流动性提升幅度趋于饱和[[S18]]。

704 ℃ 与 760 ℃ 两种典型压铸温度下，AFS 螺旋流动长度随硅含量升高先增大后减小，流动性峰值出现在硅含量 15%～19% 区间，更高浇注温度可整体提升流动能力[[S36]]。

![硅含量对压铸铝合金流动性的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4920a3a-fa93-4403-8895-011433d78cf9/resource)

图3 硅含量对压铸铝合金流动性的影响（AFS 试验螺旋长度），展示 704 ℃ 和 760 ℃ 两种浇注温度条件下的变化趋势[[S36]]。

### 对凝固收缩的影响

硅在凝固过程中发生体积膨胀，可补偿铝基体的部分凝固收缩。Al-Si 合金的体积凝固收缩率随硅含量升高呈线性下降趋势，当硅质量分数达到 25% 时体积收缩率降至接近零，该特性应用于制备低变形、高精度的压铸零件[[S43, S22, S6]]。

### 对热裂倾向的影响

靠近共晶点（硅含量约 11%～13%）的 Al-Si 合金凝固温度区间极窄，补缩性能优异，热裂倾向最低，适合压铸薄壁复杂铸件[[S23, S26]]。

### 对脱模性能的影响

硅可提升铝合金对铁基模具表面的润湿性，降低合金与模具界面的粘附倾向。配合合理的铁含量控制，可有效改善脱模性能[[S11]]。

### 对热膨胀系数的影响

硅的线膨胀系数仅为铝的 1/3～1/4。随合金硅含量升高，压铸铝合金整体热膨胀系数显著降低，铸件尺寸稳定性大幅提升[[S22, S43]]。

## 硅元素在压铸铝合金中的综合作用简表

| 作用方向 | 影响趋势 |
|---------|---------|
| 充型流动性 | 硅含量 7～18 wt% 区间优良，峰值在约 14.5～18 wt%（非平衡） |
| 凝固体积收缩率 | 随硅含量升高线性下降，25 wt% Si 时趋于零 |
| 热裂倾向 | 近共晶点（约 11～13 wt% Si）最低 |
| 热膨胀系数 | 随硅含量升高显著降低 |
| 硬度 | 随硅含量增加而提高 |
| 强度（UTS、YS） | 亚共晶区间含量增加可提高，但过量时可能与塑性同步劣化 |
| 延伸率（塑性） | 随硅含量升高持续下降 |

来源：[[S17, S22, S43, S23, S35]]

## 微观组织与相组成

### 共晶硅的形貌与演化

在未变质的铸态 Al-Si 合金中，共晶硅以粗大的不规则层片状或针状形态分布于 α-Al 基体中。这种形貌会产生显著应力集中效应，降低合金塑性[[S35, S12, S39]]。

采用 Na、Sr 等元素对合金进行变质处理后，共晶硅可从粗大片状转变为细小的纤维状。该过程的主要机制为孪晶凹谷（TPRE）或界面台阶生长机制：变质原子被吸附在硅的生长前沿，抑制原有粗晶生长方向，诱导大量孪晶生成，使硅相形貌细化[[S40]]。

### 压铸条件的特殊效应

高压压铸的快速冷却条件可使共晶硅无需添加变质元素即可获得细小的纤维状共晶组织，避免了粗针状硅相引发的应力集中问题[[S29]]。

### 热处理后共晶硅的球化行为

压铸 Al-Si 合金经 520～540 ℃ 固溶保温处理后，共晶硅在高曲率、颈缩、缺陷位置优先熔断，随保温时间延长逐步演变为近球形颗粒，完成球化过程。保温温度超过 540 ℃ 后硅相尺寸出现粗化长大现象[[S28]]。

### 过共晶合金的初生硅细化

过共晶 Al-Si 合金中初生硅相呈粗大多角块状。添加 P 元素可有效细化初生硅颗粒，而 Na、Sr 等变质剂仅能细化共晶硅，无法同时作用于初生硅。采用 P+Sr 复合的双重变质工艺可实现两类硅相的同时细化[[S37, S24]]。

### 与其他元素的化合物形成

- **Mg₂Si 相**：Al-Si 合金中 Mg 元素与 Si 元素可反应生成 Mg₂Si 金属间化合物。该相可通过固溶处理溶入铝基体，后续时效析出弥散分布的细小颗粒，实现合金基体强化[[S23, S7, S8]]。
- **(Al,Si)₃(Zr,Ti) 相**：Si 可与 Al、Zr、Ti 形成复合相，存在于特定微合金化成分设计中。

## 力学性能影响

Si 含量对 Al-Si 合金力学性能的影响不仅取决于含量本身，更与实际硅颗粒的分布和形貌密切相关[[S43]]。

硅含量升高时：
- 硬度、抗拉强度有所提升（硬质共晶硅相的强化贡献）；
- 延伸率持续下降。

以高压压铸免热处理亚共晶 Al-Si 合金系统研究为例：当硅含量从 7 wt% 增至 10 wt%，共晶硅面积分数由 25.8% 增至 51.2%，布氏硬度提升 14%，抗拉强度提升 8.3%，延伸率由 15.59% 降至 13.33%。延伸率的下降机制在于共晶硅由近球形颗粒向高长径比针状结构转变，引发更显著的应力集中效应[[S35]]。

室温与 300 ℃ 高温延伸率均随硅含量升高而下降，但对应相同硅含量时高温延伸率远高于室温值[[S1]]。

## 物理性能影响

| 物理性能 | 硅含量影响 |
|---------|----------|
| 线膨胀系数 | 从纯 Al 的 25×10⁻⁶ K⁻¹ 降至（加入 10% Si 时）约 20×10⁻⁶ K⁻¹，40% Si 时约 12×10⁻⁶ K⁻¹ |
| 凝固体积收缩率 | 随硅含量升高线性降低，25% Si 时趋于零 |
| 液相线温度 | 随硅含量增加而降低，共晶点最低约 577 ℃ |

来源：[[S43, S22]]

## 与其他元素交互作用

### 协同强化作用

Si 与 Mg 形成的 **Mg₂Si 相**是压铸铝合金中最主要的时效强化相，通过固溶+时效处理可显著提升合金强度[[S23, S7, S8]]。

### 对铁相分布的影响

随硅含量增加，合金中富铁相团簇化倾向受到抑制，呈现逐步分散趋势，这一结构演变理论上有利于延伸率的保持。但在实际合金中，共晶硅形貌的恶化主导了延伸率的下行[[S35]]。

### 在 Al-Mg 系合金中

向 Al-Mg 合金中添加硅可以改善其流动性，但同时会降低合金的延展性和缺口韧性，且不会带来明显的强度增益[[S43]]。

## 特殊应用与极限含量

### 高硅含量（≥16 wt%）用于活塞等零件

含硅量 ≥16 wt% 的过共晶铝硅合金具有优良的热稳定性和耐磨性，广泛用于铸造汽车发动机活塞[[S20]]。高硅含量使合金热膨胀系数显著降低、凝固收缩率趋近于零，从而保障活塞在高温工况下的尺寸稳定性[[S22]]。

### 极低硅含量区间

常规 Al-Si 铸造合金集中在 4～10 wt% Si 区间。该区间处于纯铝高流动性与非平衡共晶高流动性之间的中间地带，流动性表现平平[[S32]]。

### 铆接适配性优化区间

针对 SPR 自冲铆接结构件，综合材料强韧性、工艺可行性及连接可靠性，硅含量优化区间推荐为 **8.0～8.5 wt%**。该区间可兼顾力学性能（UTS ≥ 269 MPa、YS ≥ 118 MPa、延伸率 ≥ 14%）和铆接裂纹密度（控制在 4.0 ± 0.5 条的范围内）[[S5]]。

## 缺陷相关

- **过量硅的脆性相问题**：高硅铝合金中可能出现游离硅的硬质点，硅含量越高游离硅越多，增大机加工难度，且结晶时硅的析出倾向增大[[S13, S22]]。
- **铆接裂纹**：随硅含量增加，延伸率下降，铆接过程中应力集中导致裂纹密度上升。在 SP R自冲铆接测试中，硅含量从 7 wt% 增至 10 wt% 时，铆接裂纹密度由 3.0 ± 0.8 条增至 5.3 ± 1.2 条，增幅约 70%[[S5]]。

## 测试与表征

硅含量的测定在工业生产中通常采用光谱分析法。组织表征方面，光学显微镜（OM）和扫描电子显微镜（SEM）配合能谱分析（EDS）是观察共晶硅形貌、统计硅相面积分数、分析相组成的主要手段[[S21]]。

## 相关标准概览

| 标准代号 | 标准名称 / 范围 | 涉及典型牌号及硅含量 |
|---------|---------------|-------------------|
| GB/T 15115-2024 | 压铸铝合金 | YL113: 9.6～12.0 wt% |
| GB/T 15114-2023 | 铝合金压铸件 | 各牌号按 GB/T 15115 执行 |
| JIS H5302 | 铝合金压铸件 | ADC12: 9.6～12.0 wt% |
| ASTM B85 | 铝合金压铸件 | A380: 7.5～9.5 wt% |

来源：[[S2, S15, S41]]

## 成分优化推荐区间汇总

| 性能目标 | 推荐硅含量区间 | 关键考量 |
|---------|-------------|---------|
| 最佳充型流动性 | 接近 12.6 wt%（平衡共晶点，非平衡条件下≤14.5 wt%） | 流动性与补缩性能最优 |
| 高强度 + 铆接适配 | 8.0～8.5 wt% | 平衡 UTS、YS、延伸率、铆接裂纹密度 |
| 高耐磨、低热膨胀（活塞类） | ≥ 16 wt%（过共晶范围） | 尺寸稳定性、耐磨性优先 |

来源：[[S5, S20, S22, S25]]

## Sources
- S13: [有色金属压力铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b2ce23e-3718-47ac-978d-880fa4035e15/resource) (`4b2ce23e-3718-47ac-978d-880fa4035e15`)
- S22: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79fae38c-ae3b-4e7c-bd54-8e139b8983aa/resource) (`79fae38c-ae3b-4e7c-bd54-8e139b8983aa`)
- S5: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c5835bd-bc09-413c-9d7f-700ad6652f9e/resource) (`1c5835bd-bc09-413c-9d7f-700ad6652f9e`)
- S21: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c04fbe6-31e0-4b21-b1a0-ba383eaba1a2/resource) (`6c04fbe6-31e0-4b21-b1a0-ba383eaba1a2`)
- S3: [标注硅元素符号（Si）的圆形标识](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10cef0bd-8120-4766-a40f-d9da63f163f0/resource) (`10cef0bd-8120-4766-a40f-d9da63f163f0`)
- S44: [硅元素理化性质与分类数据表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f22b44af-7e2b-4d5f-a3b2-604f306e2a6c/resource) (`f22b44af-7e2b-4d5f-a3b2-604f306e2a6c`)
- S6: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d0e8bd4-b74c-46f0-8331-b4fbf84d6451/resource) (`1d0e8bd4-b74c-46f0-8331-b4fbf84d6451`)
- S17: [压铸铝合金主要添加元素含量及作用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60581534-2e3a-41ef-a4af-8817f5755396/resource) (`60581534-2e3a-41ef-a4af-8817f5755396`)
- S43: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea79ab82-cb6a-4ff5-a6b7-65fc6aecf78b/resource) (`ea79ab82-cb6a-4ff5-a6b7-65fc6aecf78b`)
- S20: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65aa0475-7435-40f4-ada2-945ac5143fda/resource) (`65aa0475-7435-40f4-ada2-945ac5143fda`)
- S30: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a17bfeeb-5bf5-41bd-a79e-d20066b46a17/resource) (`a17bfeeb-5bf5-41bd-a79e-d20066b46a17`)
- S45: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f459d633-53b4-4aa0-aaee-2cb55ba6d609/resource) (`f459d633-53b4-4aa0-aaee-2cb55ba6d609`)
- S2: [压铸用铝合金（JIS H5302-1976）种类与化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ee060ab-a2c3-40b1-812e-a78bc8f1536b/resource) (`0ee060ab-a2c3-40b1-812e-a78bc8f1536b`)
- S15: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S41: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce2d13e-413c-4061-9d2d-8e1edc9e49c7/resource) (`dce2d13e-413c-4061-9d2d-8e1edc9e49c7`)
- S34: [压铸铝合金牌号表示方法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0a42b3d-9adb-4bfa-9972-b262f6f160d9/resource) (`b0a42b3d-9adb-4bfa-9972-b262f6f160d9`)
- S31: [压铸铝合金牌号表示方法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8dd5e55-9d71-459a-9142-84839ecfb018/resource) (`a8dd5e55-9d71-459a-9142-84839ecfb018`)
- S25: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87d463e0-6ba5-4abc-9bc1-d1190399a95e/resource) (`87d463e0-6ba5-4abc-9bc1-d1190399a95e`)
- S19: [aluminium cast house technology theory practice__d10cf55c8c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/644824fa-6118-4d4a-aed6-1e484debb4a7/resource) (`644824fa-6118-4d4a-aed6-1e484debb4a7`)
- S14: [castings principles the new metallurgy of cast metals__9ac1d4f9a8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ed9f3d4-414f-4b84-8542-6f6bb2fbd023/resource) (`4ed9f3d4-414f-4b84-8542-6f6bb2fbd023`)
- S32: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b01b935b-704e-4455-a1d5-df1d2e184eec/resource) (`b01b935b-704e-4455-a1d5-df1d2e184eec`)
- S18: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6153ef42-c0a4-4f88-861c-c2de2ace692d/resource) (`6153ef42-c0a4-4f88-861c-c2de2ace692d`)
- S36: [硅含量对压铸铝合金流动性的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4920a3a-fa93-4403-8895-011433d78cf9/resource) (`b4920a3a-fa93-4403-8895-011433d78cf9`)
- S23: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b589232-953f-4f25-9cd9-43a77e38bc68/resource) (`7b589232-953f-4f25-9cd9-43a77e38bc68`)
- S26: [压铸实用技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/915fbf85-45a0-46a3-8cd1-1262ed6e33ba/resource) (`915fbf85-45a0-46a3-8cd1-1262ed6e33ba`)
- S11: [金属压铸工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4998c79b-4d82-4e49-aceb-adfeeb8ef3ad/resource) (`4998c79b-4d82-4e49-aceb-adfeeb8ef3ad`)
- S35: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4554040-2ee7-45b4-a677-b29ea426106c/resource) (`b4554040-2ee7-45b4-a677-b29ea426106c`)
- S12: [稀土在铝合金中的行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b245337-0e9e-4f20-b653-b396d6ebc45f/resource) (`4b245337-0e9e-4f20-b653-b396d6ebc45f`)
- S39: [an introduction to the solidification of metals__01fcbbd421](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d95448ea-a9ad-4dd0-ad79-965faee9f084/resource) (`d95448ea-a9ad-4dd0-ad79-965faee9f084`)
- S40: [aluminium cast house technology viii__22bdc9a7f6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da2b6355-b6d3-4f56-8dce-329754ecabc1/resource) (`da2b6355-b6d3-4f56-8dce-329754ecabc1`)
- S29: [comparative study on the microstructures and hardness of the alsi106cumg__b188063cb6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98b7d086-b910-4e3d-bf5d-6468057b5e89/resource) (`98b7d086-b910-4e3d-bf5d-6468057b5e89`)
- S28: [不同成形方式及热处理对A356铝合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9789a856-63ea-446d-b0eb-d9fc50d0b631/resource) (`9789a856-63ea-446d-b0eb-d9fc50d0b631`)
- S37: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c079dae7-9cbc-4333-add7-1b2dcef6a4b8/resource) (`c079dae7-9cbc-4333-add7-1b2dcef6a4b8`)
- S24: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c12f445-b57b-4e00-ae1c-d57a8ae6b9d1/resource) (`7c12f445-b57b-4e00-ae1c-d57a8ae6b9d1`)
- S7: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20ca9094-e3a1-492d-a1a6-60cee243e7ed/resource) (`20ca9094-e3a1-492d-a1a6-60cee243e7ed`)
- S8: [工程材料及热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/226f1b60-d122-4c61-a6a3-15cc35bbdd10/resource) (`226f1b60-d122-4c61-a6a3-15cc35bbdd10`)
- S1: [Al-Si合金伸长率随硅含量变化关系图，含室温和300℃数据及不同研究对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/030f1f18-26fc-41aa-b757-0ca600d7c625/resource) (`030f1f18-26fc-41aa-b757-0ca600d7c625`)