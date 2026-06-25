---
version: "v1"
generated_at: "2026-06-18T11:38:47+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 53
  source_quality_score: 0.85
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

ADC12 是日本工业标准（JIS）体系下的压铸专用铝合金牌号，全称 Aluminum-Alloy Die Castings，俗称“12号铝料”[[S25,S58]]，执行 JIS H5302《铝合金压铸件》标准[[S25]]。ADC12 属于 Al-Si-Cu 系近共晶压铸铝合金，其 Si 含量接近 Al-Si 二元共晶点，液相线和固相线温度较低，流动性优异，广泛用于压铸成型[[S36,S25]]。

压铸用铝合金与砂型/金属型铸造铝合金的关键区别在于对 Fe 杂质含量允许较宽——ADC 前缀统一代表压铸用合金（区别于 AC 前缀的砂型/金属型铸造合金），较高的允许含 Fe 量可降低高压压铸过程中的粘模倾向[[S16]]。

## 化学成分

ADC12 标准化学成分执行 JIS H5302:2000 版本，具体成分范围如下[[S38,S5,S25]]：

| 元素 | 含量（质量分数 %） |
|---|---|
| Si | 9.6～12.0 |
| Cu | 1.5～3.5 |
| Fe | ≤1.3 |
| Mg | ≤0.3 |
| Zn | ≤1.0 |
| Mn | ≤0.5 |
| Ni | ≤0.5 |
| Sn | ≤0.2 |
| 其他单种杂质 | ≤0.05 |
| 杂质总和 | ≤0.2 |
| Al | 余量 |

**实际生产中的成分控制**：Fe 含量通常控制在 0.9% 以下（低于 0.6% 时压铸粘模倾向显著增加）。以原生铝配制的 ADC12 实际 Fe 含量约为 0.6%，Zn 含量约为 0.3%[[S25]]。

**高纯度与变体牌号**：
- JIS H2118:2000 标准定义的高纯度锭子 AD12.2 对应于低铁级 ADC12，Fe 含量控制于 0.3～0.6%，其余微量元素控制水平远低于普通级[[S2]]。
- ADC12Z 为高锌变体，除 Zn 允许上限提高至 3.0% 外，其余主元素和杂质范围与 ADC12 一致[[S38,S2]]。

## 物理性能

ADC12 典型物理性能参数汇总如下：

| 性能参数 | 数值 | 单位 |
|---|---|---|
| 密度 | 约2.5（仿真参考值）[[S8,S30]] | g/cm³ |
| 液相线温度 | 580 | ℃ |
| 固相线温度 | 515 | ℃ |
| 凝固温度区间 | 65 | ℃ |
| 比热容 | 0.965 | kJ/(kg·K) |
| 熔化潜热 | 390（或526）[[S8,S11]] | kJ/kg |
| 热导率（常温） | 96.2～100[[S8,S36]] | W/(m·K) |

**温度-密度关系**：ADC12 密度随温度升高整体单调下降，在 500 ℃ 后下降速率明显加快，该趋势数据来源于 JmatPro 热力学计算，可直接用于模流仿真的温度-密度映射[[S4,S26]]。

**温度-表面张力关系**：在 565～680 ℃ 范围内，ADC12 表面张力随温度升高逐步增大，超过 650 ℃ 后趋于平缓，覆盖压铸充型典型温度范围[[S24]]。

**热膨胀系数**：ADC12 在不同温度下的实测热膨胀系数如下[[S18,S53]]：

| 温度（℃） | 热膨胀系数（×10⁻⁶/℃） |
|---|---|
| 550 | 25.3 |
| 500 | 24.8 |
| 450 | 24.3 |
| 400 | 23.8 |
| 室温 | 定义为 0 |

## 力学性能

**压铸态力学性能**：ADC12 常规高压铸造状态下典型力学性能范围如下[[S45,S56]]：

| 性能参数 | 典型范围 |
|---|---|
| 抗拉强度 | 228～296 MPa |
| 屈服强度 | 140～170 MPa |
| 布氏硬度 | 70～95 HB |
| 断后伸长率 | 1～3% |

实际性能数值因成分差异和生产工艺不同存在一定波动[[S45,S56]]。

**真空压铸对性能的提升**：当压铸型腔真空度从常压降低至 10 kPa 时，与普通常压压铸件相比，抗拉强度提升约 10%，屈服强度提升约 25%，延伸率提升约 36%，布氏硬度提升约 12%，铸件内部气致缺陷显著减少，组织从粗大树枝晶转为细小近等轴晶[[S55]]。

**T6 热处理后性能**：经 510 ℃ × 1 h 固溶处理 + 200 ℃ × 6 h 人工时效后，硬度可提升至 128 HBW，固溶态抗拉强度可达 233 MPa[[S20,S34]]。

## 热物性与仿真参数

ADC12 在模流仿真中的关键热物性参数如下[[S11]]：

| 参数 | 数值 | 单位 |
|---|---|---|
| 液相线 | 853（580） | K（℃） |
| 固相线 | 795（515） | K（℃） |
| 结晶潜热 | 526 | kJ/kg |
| 合金液相传热系数 | 161 | W/(m²·K) |
| 合金固相传热系数 | 81.6 | W/(m²·K) |

Anycasting 软件中 ADC12 默认仿真前处理参数为[[S57]]：比热容 0.229998 cal/g·℃，热导率 0.219728 cal/s·cm·℃，动态粘度 0.0108 P，热膨胀系数 2.1e-5 /℃，凝固体积收缩率 7.14%，临界凝固比率 0.7，570 ℃ 时表面张力 685 dyne/cm。仿真支持密度、热导率、焓等物性作为温度函数的定义方式，以适配高精度凝固分析需求[[S9]]。

## 凝固特性与 DTA 分析

DTA 差热分析结果显示：在氩气保护、5 ℃/min 加热速率条件下，ADC12 合金从 539 ℃ 开始熔化，578 ℃ 完全熔化，凝固起始温度为 590 ℃，固液相线温度区间为 539～590 ℃[[S44,S17]]。需要指出的是，该 DTA 实测区间（539～590 ℃）与常见的参考值（515～580 ℃）存在一定差异，此差异可能来源于测试条件与材料成分的不同。

## 金相组织与物相组成

重力铸造态 ADC12 原始显微组织主要由树枝状 α-Al 相和针片状共晶 Si 相组成[[S51]]。XRD 分析显示铸件组织由 Al、Si、Al₂Cu 等相组成；由于 Cu 含量较高，在凝固末期发生 L → α-Al + Si + Al₂Cu 共晶反应[[S17]]。

ADC12 压铸铝合金的典型 XRD 图谱显示了 Al、Si、Al₂Cu、Al₃Fe₂Si 四种组成相的特征衍射峰位置[[S10]]，直观反映了该合金的物相组成特征。

![ADC12压铸铝合金XRD图谱，标注Al、Si、Al₂Cu、Al₃Fe₂Si相的特征衍射峰](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e7ec919-1be1-490e-b4cb-9ddb850b6db4/resource)

## 铸造与工艺性能

### 流动性
ADC12 为近共晶 Al-Si 合金，液相线与固相线温度较低，常规流动性优异，适合复杂薄壁件压铸成型[[S36]]。

### 热裂倾向与收缩
普通熔配 ADC12 热裂倾向性极低，常规工况下不会产生热裂纹；添加微量 La 元素细化晶粒可进一步降低其热裂敏感性[[S33,S3]]。自由线收缩率处于压铸铝合金常规区间，与同类合金无显著差异[[S33]]。

### 切削性能
ADC12 切削性能中等偏优，可满足常规切削加工要求，加工难度低于 ADC5、ADC6 等高镁系压铸铝合金[[S41,S35]]。在 JIS 标准压铸铝合金性能评级中属于切削性良好的牌号。

### 耐腐蚀性能
普通高压铸造 ADC12 在 5% NaCl 溶液中的腐蚀速率约为 180 mg/(cm²·d)；型腔绝对压力为 10 kPa 的真空压铸可将腐蚀速率降至约 60.5 mg/(cm²·d)，仅为普通试样的 34%[[S15]]。经单位换算后，常规 ADC12 在对应盐雾工况下的腐蚀速率约为 0.3358 mm/a[[S13,S49]]。含 1.5～3.5% Cu 对耐腐蚀性能有一定不利影响[[S23]]。

### 推荐压铸工艺参数

| 参数 | 推荐范围 | 说明 |
|---|---|---|
| 浇注温度 | 660～720 ℃（基准 670 ℃） | 比液相线高 20～30 ℃[[S23,S46,S28]] |
| 模具温度 | 150～220 ℃ | 超低速压铸最优为 150 ℃[[S30,S7]] |
| 低速压射速度 | 0.15～0.25 m/s | 防止压室内空气卷入[[S7]] |
| 高速压射速度 | 2～6 m/s | 低于 2.0 m/s 薄壁件充型不完全[[S7,S36,S43]] |
| 内浇口速度 | 30～70 m/s | [[S36]] |
| 铸造比压 | 65～90 MPa | 典型量产 65 MPa 以上、80 MPa[[S7,S50,S54]] |

## 流变硬化行为与仿真模型

针对 2 mm 厚 ADC12 免热处理压铸铝合金板材的室温准静态拉伸工况（拉伸速度 1.2 mm/min，等效塑性应变外推至 0.5），三种经典硬化模型的标定参数如下[[S21]]：

| 模型 | 参数 | 数值 |
|---|---|---|
| Swift | B | 1196.68 |
|  | ε₀ | 0.0002 |
|  | n | 0.38052 |
| Ludwik | C | 111 |
|  | ε₁ | 2907.9 |
|  | m | 0.706 |
| Hockett-Sherby | σ_at | 3200 |
|  | σ₀ | 3089 |
|  | K | 0.994 |
|  | n | 0.7138 |

Swift、Ludwik、Hockett-Sherby 三种模型均能高精度拟合 ADC12 压铸铝合金的硬化曲线，该材料无明显缩颈现象。其中 Ludwik 硬化准则的拟合趋势相对更优，被推荐用于该材料的塑性行为预测，对应仿真断裂应变误差可控制在 8% 以内，可用于整车碰撞仿真分析[[S21,S29]]。

应变硬化贡献比随温度升高单调下降，在 300 ℃ 时降至 0[[S6]]，表明高温下 ADC12 的应变硬化能力显著衰减。

## 主要局限性

1. **导热率限制**：ADC12 常温热导率仅为约 100 W/(m·K)，无法满足当前 5G 基站散热器普遍要求的 ≥160 W/(m·K) 门槛，因此不能直接用于对高导热有严格要求的 5G 散热器壳体[[S36,S14]]。

2. **粘模风险**：Fe 含量低于 0.6% 时压铸粘模倾向显著提升[[S25]]。

3. **耐腐蚀性能**：成分中 1.5～3.5% 的 Cu 会降低合金耐腐蚀性能[[S23]]。

4. **气孔与缩松缺陷**：常规压铸件内部易存在气孔、缩松缺陷，限制了直接 T6 热处理工艺的应用[[S23,S47]]。

5. **抛丸起皮**：成分异常（如 Si≥11.5%、Fe≥1.2% 等）或工艺不当时，抛丸处理易出现起皮缺陷[[S47]]。

6. **高导热对比**：ADC3 的切削性和耐蚀性均优于 ADC12，导热性能更高；ADC6 耐腐蚀性比 ADC12 高 2～3 倍、导电性能可达 35% IACS，导热性能显著优于 ADC12[[S42,S52]]。

## 关联标准与替代牌号

| 标准体系 | 相近牌号 | 说明 |
|---|---|---|
| 中国 GB/T 15115 | YL113（YZAlSi12Cu2） | 近等效牌号，Sn 上限 ≤0.1% 比 ADC12 更严格[[S25,S19]] |
| 美国 ASTM B85 | A380 | Fe 上限 1.3%，Zn 上限 3.0%[[S31,S27]] |
| 美国 ASTM B85 | A383 | 与 ADC12 成分接近[[S12]] |
| 英国 BS 1490 | LM24 | 与 A380 相当[[S27]] |

## 典型应用

**汽车领域**：ADC12 广泛应用于汽车压铸结构件，具体包括 9AT 变速器壳体、发动机缸体、发动机罩盖、转向器阀壳体、气缸盖罩盖、传感器支架等[[S32,S50,S25,S23]]。

**家电与消费电子领域**：包括日用炊具锅体、电讯接收器底座、散热器盖、常规非高散热要求的电子设备外壳等[[S7,S40]]。

散热器盖 ADC12 压铸件零件图标注了完整的铸件尺寸参数，可作为该领域应用的典型示例[[S40]]。

![ADC12散热器盖压铸件零件图，标注完整尺寸参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a306822c-98c2-40de-8ec6-04a26a3964a0/resource)

## Sources
- S25: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S58: [日本压铸铝合金种类、牌号及特性表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fae2d1e8-81a2-46e9-8c6f-67dc7ccd9deb/resource) (`fae2d1e8-81a2-46e9-8c6f-67dc7ccd9deb`)
- S36: [浅述5G基站散热器壳体压铸工艺对压铸机的诉求](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ac85cbf-9602-4b91-b4e0-5c818dd232b4/resource) (`8ac85cbf-9602-4b91-b4e0-5c818dd232b4`)
- S16: [简明铝合金手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/394db064-901d-4687-8f0d-5fd71b983ee6/resource) (`394db064-901d-4687-8f0d-5fd71b983ee6`)
- S38: [压铸用铝合金锭化学成分表（摘自JIS H2118:2000）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9410b7f9-d70d-43ed-8f3d-dbe88aac65f9/resource) (`9410b7f9-d70d-43ed-8f3d-dbe88aac65f9`)
- S5: [压铸用铝合金（JIS H5302-1976）种类与化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ee060ab-a2c3-40b1-812e-a78bc8f1536b/resource) (`0ee060ab-a2c3-40b1-812e-a78bc8f1536b`)
- S2: [日本压铸铝合金锭化学成分表（摘自JIS H 2118:2000）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/05a5c3d3-8494-4d86-8967-27cc98c9ca29/resource) (`05a5c3d3-8494-4d86-8967-27cc98c9ca29`)
- S8: [表4.2 ADC12铝合金铸件物理性能参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/188724a6-158c-4a88-8273-7479229c1e9c/resource) (`188724a6-158c-4a88-8273-7479229c1e9c`)
- S30: [effects of die temperature of sss die casting on the microstructure and__d27a8b10b6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75a97bcc-de43-4a17-ab9a-4b13197ddfd3/resource) (`75a97bcc-de43-4a17-ab9a-4b13197ddfd3`)
- S11: [ADC12的热物性参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21f20e46-8d20-484f-ba42-a10a4e6e6538/resource) (`21f20e46-8d20-484f-ba42-a10a4e6e6538`)
- S4: [ADC12铝合金密度随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/090a0873-bbf4-4128-9c06-efbd6ae972c2/resource) (`090a0873-bbf4-4128-9c06-efbd6ae972c2`)
- S26: [ADC12铝合金密度随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5522a665-e5b1-40c2-95c9-e971187ac30d/resource) (`5522a665-e5b1-40c2-95c9-e971187ac30d`)
- S24: [ADC12铝合金表面张力随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/535a3ecc-b703-4395-95df-a263aa4248cd/resource) (`535a3ecc-b703-4395-95df-a263aa4248cd`)
- S18: [压铸件的无毛刺压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44a7687b-cbe9-4ecb-9097-c6c309eeefd0/resource) (`44a7687b-cbe9-4ecb-9097-c6c309eeefd0`)
- S53: [压铸件包紧力的动态分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9968664-450c-4d8d-9063-5bd5223d56c9/resource) (`e9968664-450c-4d8d-9063-5bd5223d56c9`)
- S45: [压铸铝合金ADC12产品抛丸起皮原因分析及解决方案推荐](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3225581-e436-401e-a73f-fdabb90d6e8a/resource) (`c3225581-e436-401e-a73f-fdabb90d6e8a`)
- S56: [压铸铝合金ADC12产品抛丸起皮原因分析及解决方案推荐](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec9dd8db-d8b9-4b5d-985a-e8a9d8ecd563/resource) (`ec9dd8db-d8b9-4b5d-985a-e8a9d8ecd563`)
- S55: [ADC12铝合金真空压铸充型过程及铸件性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec51670b-eb4d-44ae-aff2-3bf36f8d8ee7/resource) (`ec51670b-eb4d-44ae-aff2-3bf36f8d8ee7`)
- S20: [T6热处理对高压压铸ADC12铝合金微观结构和性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e699368-32a3-4d41-bee3-26c246828c08/resource) (`4e699368-32a3-4d41-bee3-26c246828c08`)
- S34: [T6热处理对高压压铸ADC12铝合金微观结构和性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81b29e9c-8f38-4542-aa74-d81f10055288/resource) (`81b29e9c-8f38-4542-aa74-d81f10055288`)
- S57: [图3.4 各实体材料设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef483201-d87e-44bb-b9b1-42e60657cff7/resource) (`ef483201-d87e-44bb-b9b1-42e60657cff7`)
- S9: [铸件材料热物性参数设置界面（固液相线温度）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1db997fc-3731-4f86-95d7-1d9c2a90336f/resource) (`1db997fc-3731-4f86-95d7-1d9c2a90336f`)
- S44: [低过热度倾斜板流变压铸对ADC12组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb80db8e-2b73-404b-bd71-036327c607d9/resource) (`bb80db8e-2b73-404b-bd71-036327c607d9`)
- S17: [低过热度倾斜板流变压铸对ADC12组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/396505ff-5283-46b2-a477-fc24ddfa7ddc/resource) (`396505ff-5283-46b2-a477-fc24ddfa7ddc`)
- S51: [低过热度倾斜板流变压铸对ADC12组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3fa2b3f-a1cd-412a-af37-600fb8c6b36a/resource) (`e3fa2b3f-a1cd-412a-af37-600fb8c6b36a`)
- S10: [图5-7 压铸铝合金XRD图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e7ec919-1be1-490e-b4cb-9ddb850b6db4/resource) (`1e7ec919-1be1-490e-b4cb-9ddb850b6db4`)
- S33: [电解法生产铝合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7dfd5172-a60c-42cc-b598-05f0e4b221b3/resource) (`7dfd5172-a60c-42cc-b598-05f0e4b221b3`)
- S3: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06bb853f-0db7-4a0e-aa1e-294c44b4470d/resource) (`06bb853f-0db7-4a0e-aa1e-294c44b4470d`)
- S41: [重力铸造用铝合金的铸造性与铸件特性（JIS 标准）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/abbd012f-5636-4eb7-b588-8bb5b497e4df/resource) (`abbd012f-5636-4eb7-b588-8bb5b497e4df`)
- S35: [主要铸造铝合金（JIS 标准）特性与性能对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81eb4468-a80c-4685-825c-58da307b4d15/resource) (`81eb4468-a80c-4685-825c-58da307b4d15`)
- S15: [ADC12铝合金真空压铸充型过程及铸件性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/268dbb13-3e9f-4842-a105-0bee71de7861/resource) (`268dbb13-3e9f-4842-a105-0bee71de7861`)
- S13: [表面预处理实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24b76530-22c4-422f-9e33-4d002fae41f9/resource) (`24b76530-22c4-422f-9e33-4d002fae41f9`)
- S49: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd53d141-3637-4d14-8329-6f05ad289b8e/resource) (`dd53d141-3637-4d14-8329-6f05ad289b8e`)
- S23: [基于数值模拟的转向器阀壳体压铸模具结构及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5101d702-72b7-4ef7-abdb-559d6ef9a451/resource) (`5101d702-72b7-4ef7-abdb-559d6ef9a451`)
- S46: [Anycasting软件中压铸压室参数设置界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d7954bc9-76ea-4f56-be73-ff1ca815d09f/resource) (`d7954bc9-76ea-4f56-be73-ff1ca815d09f`)
- S28: [eeffects of die casting conditions on the mechanical properties of adc 1__6cc28a87ed](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56bd81a8-513d-41a8-971d-9ea0ebee0e87/resource) (`56bd81a8-513d-41a8-971d-9ea0ebee0e87`)
- S7: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10a6c833-570a-4a34-bcc2-df76cf3ffac4/resource) (`10a6c833-570a-4a34-bcc2-df76cf3ffac4`)
- S43: [图3.11 ADC12铝合金压铸流动性模拟结果对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4c2d6d9-2eb5-4f8a-824e-64771af942ac/resource) (`b4c2d6d9-2eb5-4f8a-824e-64771af942ac`)
- S50: [ADC12-VSr铝合金汽车发动机罩盖的压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e378e323-5918-47f4-a0c4-5494ea8631d5/resource) (`e378e323-5918-47f4-a0c4-5494ea8631d5`)
- S54: [ADC12铝合金压铸工艺条件示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eab52657-2219-41fd-8164-f65b671a0eb9/resource) (`eab52657-2219-41fd-8164-f65b671a0eb9`)
- S21: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ebfa349-6181-4e0c-9b50-0941db5fcec8/resource) (`4ebfa349-6181-4e0c-9b50-0941db5fcec8`)
- S29: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64b92724-fb78-4acc-917d-29ce6e75cc5c/resource) (`64b92724-fb78-4acc-917d-29ce6e75cc5c`)
- S6: [Fig. 10 Temperature dependence of the contribution ratio of strain hardening derived from the initial yield stress –...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0fa98c49-46b9-442c-94d0-5ee492c46fb7/resource) (`0fa98c49-46b9-442c-94d0-5ee492c46fb7`)
- S14: [浅述压铸铝合金行业现状及发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2522ac4b-92cd-47d3-a463-15c9de278471/resource) (`2522ac4b-92cd-47d3-a463-15c9de278471`)
- S47: [压铸铝合金ADC12产品抛丸起皮原因分析及解决方案推荐](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d95063a8-12d4-479a-acc7-a600fd05d1f5/resource) (`d95063a8-12d4-479a-acc7-a600fd05d1f5`)
- S42: [1987-88中华民国压铸工业名录](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b35cd1f4-71b6-42be-9a0d-82568fd52a97/resource) (`b35cd1f4-71b6-42be-9a0d-82568fd52a97`)
- S52: [主要铸造铝合金物理性能 (JIS 标准)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8b24430-3b4b-4d2e-98eb-6f5bb49dc2ca/resource) (`e8b24430-3b4b-4d2e-98eb-6f5bb49dc2ca`)
- S19: [TextNode61](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bbf37bd-ba1d-4a8a-a910-5977d80b2363/resource) (`4bbf37bd-ba1d-4a8a-a910-5977d80b2363`)
- S31: [die casting metallurgy aluminium alloy die castings__6142c8982e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76843354-65be-48c6-9952-0ae476ee4a9f/resource) (`76843354-65be-48c6-9952-0ae476ee4a9f`)
- S27: [die casting metallurgy__8f9e04f2f0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5596e7b6-527a-4439-81e4-1f8bf092905b/resource) (`5596e7b6-527a-4439-81e4-1f8bf092905b`)
- S12: [H13与A380材料的化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22372649-efcc-4d22-98ac-213979cc6b4c/resource) (`22372649-efcc-4d22-98ac-213979cc6b4c`)
- S32: [铝合金9AT变速器壳体的真空压铸工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79e72312-5b14-49c2-a183-e1d3f998a1fa/resource) (`79e72312-5b14-49c2-a183-e1d3f998a1fa`)
- S40: [散热器盖ADC12压铸件零件图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a306822c-98c2-40de-8ec6-04a26a3964a0/resource) (`a306822c-98c2-40de-8ec6-04a26a3964a0`)