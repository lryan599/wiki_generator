---
version: "v1"
generated_at: "2026-06-18T17:00:44+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 12
  source_quality_score: 0.85
  freshness_score: 0.86
  evidence_coverage_score: 1.0
---

JDA2b 是上海交通大学轻合金中心开发的免热处理高强韧压铸铝合金，属该单位自定义的 JDA2 系列代号，目前未收录于 GB/T 15115 等公开国家或行业标准中 [[S11,S14,S15]]。该合金通过成分设计与复合变质处理，在铸态下即可获得优异的强度与塑性，适配高真空高压压铸工艺，主要用于汽车底盘类受力结构件及大型薄壁一体化车身零件 [[S11,S18]]。

## 显微组织特征
JDA2b 的共晶组织占总组织的 40%~50%，为该合金提供了良好的压铸工艺性能 [[S11]]。组织调控方面，主要通过以下手段实现细化与变质：
- 添加 Ti、Zr、V 元素进行组织细化 [[S11]]；
- 采用 Ca/RE 复合变质处理，获得细小的共晶 Mg₂Si 相 [[S11]]。

![经Ca/RE复合变质处理的JDA2b合金细小共晶Mg2Si相TEM形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/889f889f-4ef2-4a19-afaa-0fb871f85d36/resource)
*图：变质后 Mg₂Si 相的 TEM 图像 [[S11]]*

## 力学性能
JDA2b 在铸态下的力学性能已公开的主要参数如下：

| 性能指标 | 典型值/范围 | 备注 |
|----------|--------------|------|
| 屈服强度 | 180~220 MPa | 高值记录 >200 MPa [[S11,S14]] |
| 抗拉强度 | 360~400 MPa | [[S11,S14]] |
| 伸长率   | 8%~12%      | 高值记录 >10% [[S11,S14]] |

该铸态性能水平可达到 AlSi10MnMg 合金经 T6 热处理后的性能 [[S14]]，因而在应用中可免去常规高强压铸铝合金所需的 T6/T7 热处理及后续矫形工序 [[S14]]。

## 工艺特性与优势
- **免热处理**：JDA2b 铸件无需进行 T6/T7 热处理，避免了热处理过程中的鼓泡、变形等缺陷，显著降低一体化压铸的生产成本 [[S14]]。
- **薄壁效应**：JDA2 体系合金针对薄壁零件设计，解决了低硅铝合金流动性较差的问题，可大幅降低大型薄壁压铸件的报废率 [[S8,S18]]。
- 对于采用 JDA 系列铝合金的大型结构件高压压铸，可参考以下通用工艺参数范围（源自同类大型一体化压铸件的实践）：模具预热温度约 150 °C，浇注温度约 720 °C，低速压射速度约 0.2 m/s，高速压射速度约 6.5 m/s，压射比压 30~40 MPa [[S13]]。

![铝合金压铸P-Q²特性匹配曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f2ef32e-c458-4730-baf1-3ea9bee8de06/resource)
*图：压铸机特性线（ML）与模具特性线（DL）的 P‑Q² 匹配关系，可用于指导 JDA2b 大型结构件压铸时的设备与模具适配 [[S6]]*

## 应用领域
JDA2b 及其所属的 JDA2 体系主要面向汽车底盘类高强高韧零件，满足铸件较高的冲击与疲劳耐久要求 [[S18]]。典型应用场景包括：
- 副车架、控制臂、转向节等底盘受力结构件 [[S18]]；
- 大型薄壁一体化车身压铸件 [[S18]]。

## 与相近压铸铝合金的对比
JDA2b 与传统压铸铝合金的关键性能差异如下表所示：

| 对比合金 | 状态 | 屈服强度 | 抗拉强度 | 伸长率 | 核心差异 |
|----------|------|----------|----------|--------|----------|
| JDA2b | 铸态 | >200 MPa（180~220 MPa）| 360~400 MPa | >10%（8%~12%） | 免热处理，高强高韧 [[S11,S14]] |
| AlSi10MnMg | 真空压铸+T6 | ≥180 MPa | 230~295 MPa | ≥8% | 需 T6 热处理，强度与塑性均低于 JDA2b 铸态 [[S14,S17]] |
| ADC12 | 铸态 | 较低（未详列） | 约 230 MPa | <2% | 含 Cu，伸长率远低于 JDA2b，且热处理易变形 [[S11,S17]] |
| A380 | 铸态/T6 | 较低 | 中等 | 较低 | 综合强韧性显著低于 JDA2b，难以通过 T6 达到相近门槛 [[S11,S17]] |

## 缺陷与质量控制
由于尚无公开发布的 JDA2b 专属缺陷数据，其生产中可能出现的压铸缺陷与通用 Al‑Si 系压铸件类似，主要包括气孔、缩孔、冷隔、热裂、变形等 [[S9,S10,S12]]。对应的质量控制对策可概括为：
- 严格控制铝液含气量，优化浇排系统并配合高真空排气，减少充型卷气 [[S12,S1]]；
- 通过数值模拟优化充型顺序与压力传递，改善补缩，降低缩孔倾向 [[S9]]；
- 合理调整合金成分与变质处理，匹配适宜的浇注与模具温度，降低热裂风险 [[S9,S12]]；
- 优化压射速度区间，避免高速紊流卷气或低速导致的冷隔 [[S9]]；
- 控制开模时机并均衡脱模力，防止铸件变形 [[S10]]。

## 技术定位与未确认事项
- JDA2b 为上海交通大学自主研发的免热处理压铸铝合金代号，目前公开资料未显示其化学成分质量分数范围、密度、硬度等具体数值 [[S11,S14]]；
- 该代号未出现在现行 GB/T 15115 等压铸铝合金国家标准中，属于企业内部牌号 [[S15,S17]]。

## Sources
- S11: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/889f889f-4ef2-4a19-afaa-0fb871f85d36/resource) (`889f889f-4ef2-4a19-afaa-0fb871f85d36`)
- S14: [一体化压铸免热处理铝合金研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4733cbe-bdcf-4407-8b11-94abff137054/resource) (`b4733cbe-bdcf-4407-8b11-94abff137054`)
- S15: [免热处理铝合金大型结构件一体压铸研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce3645bc-4f9a-4657-8dc4-51c5ea6f8ec4/resource) (`ce3645bc-4f9a-4657-8dc4-51c5ea6f8ec4`)
- S18: [铝合金一体化压铸技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea380b35-b160-40cf-b36d-2c1aae1f804e/resource) (`ea380b35-b160-40cf-b36d-2c1aae1f804e`)
- S8: [基于压铸工艺的铝合金车门结构设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78a1930b-d60c-4702-ae84-211a58eabb0d/resource) (`78a1930b-d60c-4702-ae84-211a58eabb0d`)
- S13: [某汽车后舱一体化压铸件工艺分析及缺陷改善_卢灿雄](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3c99480-14c0-4100-b6d0-1f61b5313c13/resource) (`a3c99480-14c0-4100-b6d0-1f61b5313c13`)
- S6: [图3.6压铸机特性线（ML）及模具特性线（DL）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f2ef32e-c458-4730-baf1-3ea9bee8de06/resource) (`5f2ef32e-c458-4730-baf1-3ea9bee8de06`)
- S17: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce2d13e-413c-4061-9d2d-8e1edc9e49c7/resource) (`dce2d13e-413c-4061-9d2d-8e1edc9e49c7`)
- S9: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7af0a7e0-b7df-472a-85ab-a1928b542769/resource) (`7af0a7e0-b7df-472a-85ab-a1928b542769`)
- S10: [压铸技术简明手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87b11f16-625b-4f6c-8013-a908f4a55d1d/resource) (`87b11f16-625b-4f6c-8013-a908f4a55d1d`)
- S12: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/948ee161-12c4-4770-811d-63f44be31723/resource) (`948ee161-12c4-4770-811d-63f44be31723`)
- S1: [铝合金压铸制品缩孔缺陷影响因素分析及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b44a51e-7eb9-4c46-9de9-192bdda997d8/resource) (`2b44a51e-7eb9-4c46-9de9-192bdda997d8`)