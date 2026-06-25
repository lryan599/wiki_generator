---
version: "v1"
generated_at: "2026-06-18T10:10:16+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 35
  source_quality_score: 0.87
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

三氧化二铁（化学式 Fe₂O₃，英文 Ferric oxide / Iron(III) oxide），别名铁红、铁锈、氧化铁红，CAS 登录号 1309-37-1，分子量 159.69 g/mol，外观为红至红棕色粉末，密度 5.24 g/cm³，熔点 1565 ℃，不溶于水，可溶于盐酸、硫酸，微溶于硝酸 [[S18,S20]]。在铸造语境中，Fe₂O₃ 主要作为非金属氧化夹杂物被讨论，是影响铸件质量的重要缺陷类型之一。

从晶体结构看，人工制备的高纯 Fe₂O₃ 晶粒尺寸约 44 nm，晶格微应变水平为 0.76×10⁻³，存在孪晶包装缺陷；天然产出的赤铁矿晶粒尺寸可达 94 nm，晶格微应变水平为 1.3×10⁻³ [[S24]]。

## 在铸造中的来源与角色

### 生成来源

Fe₂O₃ 作为非金属夹杂物进入金属熔体的主要途径包括 [[S1]]：

1. **熔炼工具锈蚀**：工具表面铁锈未清理完全，接触高温熔体后剥落进入熔体；
2. **回炉料氧化**：未进行抛丸预处理的锈蚀回炉料直接入炉，直接带入 Fe₂O₃ 夹杂；
3. **炉衬侵蚀**：炉衬长期受铁液侵蚀，表面生成的 Fe₂O₃ 剥落混入熔体；
4. **二次氧化**：金属液在转注、充型过程中发生湍流卷气，铁元素与氧气反应生成 Fe₂O₃。

此外，金属与外界物质相互作用生成的氧化物、金属液被大气氧化生成的氧化物，均属于外来夹杂物范畴 [[S4]]。

### 对铸件质量的影响

Fe₂O₃ 夹杂物对铸件质量具有显著危害 [[S9,S4]]：

| 影响维度 | 具体表现 |
|---------|---------|
| 力学性能 | 疲劳强度降低，冲击韧性明显下降；尖角形夹杂引起应力集中，促使微裂纹产生 |
| 铸造性能 | 金属液含固体夹杂物时流动性显著降低 |
| 热裂纹 | 分布在晶界上的 Fe₂O₃ 等低熔点夹杂是铸件产生热裂纹的主要原因之一 |
| 致密性 | Fe₂O₃ 可作为形核核心促进气孔生成，降低铸件整体致密性，促进微观缩孔和气缩孔形成 |

据统计，汽车零件的断裂 90% 是由疲劳裂纹造成的，其裂纹源大多为非金属夹杂物 [[S9]]。

## 检测方法

Fe₂O₃ 夹杂物的常规识别检测手段包括 [[S14,S23,S40]]：

- **金相显微观测法**：可直观观察夹杂物形貌与分布，配合能谱分析（EDS）可精准判定夹杂物为 Fe₂O₃ 相；
- **X 射线 / 工业 CT 无损检测法**：对夹杂物检测最为直观、可靠；
- **超声波探伤法**：适用于内部缺陷检测；
- **磁粉探伤法**：适用于铁磁性材料表面及近表面开口不连续的检验。

![含Fe₂O₃的铝合金熔渣EDS能谱图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0967698c-d7bd-4f81-bd99-809d5d29afa1/resource)

上图为含 Fe 元素的铝合金混合氧化夹杂能谱检测图谱，谱线中清晰呈现 O、Al、Si、Ca、Fe 的特征峰，证明该类熔渣中存在 Fe₂O₃ 组分 [[S2]]。

## 控制与去除措施

工业生产中控制 Fe₂O₃ 夹杂的主流工艺措施包括 [[S1,S9,S38]]：

| 措施 | 具体要求与效果 |
|------|--------------|
| 回炉料预处理 | 对所有回炉料提前做抛丸除锈，避免 Fe₂O₃ 直接带入金属液 |
| LF 精炼吹氩搅拌 | 对金属液进行 15–25 min 吹氩搅拌，可使整体非金属夹杂物质量分数降低约 40% |
| 浇注系统过滤 | 在浇注系统中设置过滤装置，拦截悬浮的 Fe₂O₃ 夹杂 |
| 惰性气体保护熔炼 | 避免金属液二次氧化生成 Fe₂O₃ |
| 铸型烘干 | 对铸型进行充分烘干，减少浇注过程中金属液的氧化反应 |

此外，排除和减少金属液中气体或气泡的工艺措施（如真空熔炼、避免金属液飞溅或涡流、金属液通过过滤器再注入型腔等）同样能达到减少夹杂物的目的 [[S9]]。

## 脉冲电流作用下的电迁移行为

### 研究范围与实验条件

针对 1 kg 质量的无氧铜（TU0）熔体，有研究证实脉冲电流作用下 Fe₂O₃ 夹杂物存在向阴极定向迁移的行为 [[S11,S17]]。**需注意：该特性由单实验室小体量实验验证，目前尚无公开的多研究交叉验证的行业普适性共识，仅适用于该限定实验场景。**

该实验的固定边界条件为 [[S8,S11]]：
- 电极插入深度为熔体总高度的 1/4；
- 脉冲电流类型为单向脉冲；
- 采用 1 kg 体量的无氧铜熔体作为实验对象。

### 迁移参数与效果

在该实验条件下，Fe₂O₃ 夹杂向阴极迁移的电流阈值约为 **50 A**，脉冲频率参数约为 **1000 Hz** [[S11,S34,S22]]。该参数下：

- Fe₂O₃ 向阴极迁移的电动力可抵消频域搅拌作用；
- 阴极处 Fe₂O₃ 最高含量可达 **0.525 wt.%**，远高于阳极侧 0.151 wt.%；
- 在靠近负极的顶部区域出现 Fe₂O₃ 富集区，富集峰值可达约 **5.2 wt.%**。

当采用双向脉冲电流处理铜熔体时，仅起到均匀化 Fe₂O₃ 夹杂物分布的搅拌作用，不会出现夹杂物定向向阴极富集的现象 [[S8,S30]]。

### 迁移机理

Fe₂O₃ 在铜熔体中定向迁移的主导作用力为**电子风力**，该作用在高导电导热铜熔体中效果显著 [[S29,S39]]。具体机理为 [[S29,S39]]：

- Fe₂O₃ 在铜熔体中的有效电荷数为 **+2±1**，在电场驱动下向阴极移动；
- 叠加浮力、电自由能差产生的电势能驱动力共同决定夹杂物最终迁移轨迹；
- 实验测得铜熔体中该场景下的磁场仅为 10⁻⁵ T 量级，对应的电磁斥力可忽略不计；
- 过大的电流产生的焦耳热会加剧熔融原子不规则运动，干扰定向迁移，因此脉冲电流参数存在阈值。

![脉冲电流作用下铜熔体中氧化夹杂受力迁移原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22bb1dd6-45f7-4809-842c-95dbd61df063/resource)

上图展示了脉冲电流处理铜熔体中氧化夹杂的迁移机理：无电作用时熔体内部以涡流带动夹杂物无规则运动，通电后夹杂物受浮力、重力、电场力、电子风力等多力叠加的合力作用向阴极顶部迁移富集 [[S7]]。

### 不同材料体系中的迁移差异

| 材料体系 | 迁移特征 | 原因分析 |
|---------|---------|---------|
| 无氧铜（TU0） | Fe₂O₃ 向阴极明显富集 | 熔体粘度较低，电子风力驱动显著 |
| 铜碲合金 | Fe₂O₃ 分布更均匀，迁移难度显著高于无氧铜 | 铜碲合金同温度下熔体粘度高于无氧铜 [[S8,S15]] |

**铝熔体方面**：现有公开文献中仅收录了常规交变电磁场分离铝合金熔体中富铁相的相关研究，暂未找到脉冲电流作用下铝合金熔体中 Fe₂O₃ 夹杂物向阴极迁移、且匹配 50 A / 1000 Hz 参数的相关公开研究记录 [[S37,S13]]。

## 相关标准与规范

### 夹杂物评级标准

| 标准 | 适用范围 | 说明 |
|------|---------|------|
| ASTM E45 | 钢中非金属夹杂物含量检测 | 通过金相法对照标准图谱对各类氧化物夹杂（包括 Fe₂O₃）进行分级评价 [[S3,S5]] |
| ISO 4967 | 钢中非金属夹杂物金相评级 | 与 GB/T 10561 等效，覆盖 Fe₂O₃ 等氧化夹杂的分类统计规则 [[S25,S6]] |

### 有色金属成分限制标准

| 标准 | 适用范围 | 与 Fe₂O₃ 的关系 |
|------|---------|----------------|
| GB/T 1173、GB/T 9438 | 铸造铝合金 | 规定铝合金中 Fe 元素质量分数上限，从成分端限定 Fe₂O₃ 夹杂物的生成总量 [[S28,S32]] |
| GB/T 1176、GB/T 13819 | 铸造铜合金 | 对铜基体中 Fe 元素杂质含量设置明确限值，间接管控 Fe₂O₃ 夹杂物占比 [[S31,S27]] |

## 与其他常见铸造氧化物的对比

### 物理参数对比

Fe₂O₃ 的熔点低于 Al₂O₃、高于 SiO₂ 的玻璃态夹杂熔点，密度处于铁基氧化物和铝基氧化物之间，在金属熔体中的上浮行为符合斯托克斯定律 [[S16]]。

### 行为差异对比

| 对比维度 | Fe₂O₃ | Al₂O₃ | SiO₂ |
|---------|--------|-------|------|
| 化学活性 | 活性较高，可与部分合金组元发生界面反应生成尖晶石类复合夹杂 [[S12,S19]] | 化学稳定性高 | 在高温熔体中多呈低熔点玻璃态分布 |
| 对性能影响 | 优先成为富铁相形核基底，在铝合金中促进富铁针状相析出，更易降低塑韧性和耐蚀性 [[S4,S36]] | 硬质点引发应力集中 | 较 Fe₂O₃ 危害程度相对较低 |

在钢铁中，Fe₂O₃ 属于简单氧化物夹杂的一类；也可参与形成复杂氧化物，如尖晶石类夹杂 FeO·Fe₂O₃ [[S12,S4]]。

## Sources
- S18: [氧化铁（Fe₂O₃）理化性质表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c651e54-ddc3-4884-a54d-57255e5a8d7d/resource) (`7c651e54-ddc3-4884-a54d-57255e5a8d7d`)
- S20: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89481f03-b31c-4a50-aabb-16cfc1b73034/resource) (`89481f03-b31c-4a50-aabb-16cfc1b73034`)
- S24: [agglomeration in metallurgy__261520a6c6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9342a911-95da-4349-82e7-3bdadc4895df/resource) (`9342a911-95da-4349-82e7-3bdadc4895df`)
- S1: [球墨铸铁涡轮壳铸件缩松与夹渣缺陷分析及改善](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04d92207-5294-455d-a8a5-8603d2633c80/resource) (`04d92207-5294-455d-a8a5-8603d2633c80`)
- S4: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19c9ab67-77f0-4573-9620-060dd681f994/resource) (`19c9ab67-77f0-4573-9620-060dd681f994`)
- S9: [材料成形工艺基础金属工艺学热加工部分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fb4e32e-b8d7-440d-be82-ceb885150301/resource) (`3fb4e32e-b8d7-440d-be82-ceb885150301`)
- S14: [轻合金车轮制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c60a512-cda6-4e2d-9026-7e431750a64b/resource) (`6c60a512-cda6-4e2d-9026-7e431750a64b`)
- S23: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8dc026ff-3073-48b8-ab05-f4980c7b7673/resource) (`8dc026ff-3073-48b8-ab05-f4980c7b7673`)
- S40: [实用有色合金铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f915df70-39db-40a8-af8b-4a6251d73b81/resource) (`f915df70-39db-40a8-af8b-4a6251d73b81`)
- S2: [铝合金夹杂物的熔渣能谱化学成分分析图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0967698c-d7bd-4f81-bd99-809d5d29afa1/resource) (`0967698c-d7bd-4f81-bd99-809d5d29afa1`)
- S38: [光固化3D打印复杂零件快速铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2daa9af-a46a-4a60-9d2e-2b8da41c5a03/resource) (`e2daa9af-a46a-4a60-9d2e-2b8da41c5a03`)
- S11: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55e86128-555e-475b-b779-3b8a11bbdf2b/resource) (`55e86128-555e-475b-b779-3b8a11bbdf2b`)
- S17: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/776e805b-f542-4294-832e-6bcda58827d7/resource) (`776e805b-f542-4294-832e-6bcda58827d7`)
- S8: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3538a747-aab9-4a5e-ab86-57878dc4c4b8/resource) (`3538a747-aab9-4a5e-ab86-57878dc4c4b8`)
- S34: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce464dc3-4b39-4252-8c5c-1b98d26439fa/resource) (`ce464dc3-4b39-4252-8c5c-1b98d26439fa`)
- S22: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d34f6f1-1b82-4bbc-9527-e291a9582d8b/resource) (`8d34f6f1-1b82-4bbc-9527-e291a9582d8b`)
- S30: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b583bcd0-99f9-4edb-8555-e6c7c6247c72/resource) (`b583bcd0-99f9-4edb-8555-e6c7c6247c72`)
- S29: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2685b34-706b-4ddc-84cf-109007d3410a/resource) (`b2685b34-706b-4ddc-84cf-109007d3410a`)
- S39: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f166576d-6067-4603-a54a-802be1d0e5bd/resource) (`f166576d-6067-4603-a54a-802be1d0e5bd`)
- S7: [图5.9 脉冲电流处理铜熔体中氧化夹杂元素Si/Fe分离机理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22bb1dd6-45f7-4809-842c-95dbd61df063/resource) (`22bb1dd6-45f7-4809-842c-95dbd61df063`)
- S15: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f50ae9d-1e03-434a-859d-5ebd2362a018/resource) (`6f50ae9d-1e03-434a-859d-5ebd2362a018`)
- S37: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da47a431-0b74-4040-b71c-2ebef852adcd/resource) (`da47a431-0b74-4040-b71c-2ebef852adcd`)
- S13: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62a45060-1470-46f1-9d9e-96106da744aa/resource) (`62a45060-1470-46f1-9d9e-96106da744aa`)
- S3: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a9e1487-78d2-4ac1-9bd9-3dc5013340f8/resource) (`0a9e1487-78d2-4ac1-9bd9-3dc5013340f8`)
- S5: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ed0d364-f44c-404b-98e4-225d99d16cd3/resource) (`1ed0d364-f44c-404b-98e4-225d99d16cd3`)
- S25: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94e25254-34cd-4606-b3ad-7de60902f71f/resource) (`94e25254-34cd-4606-b3ad-7de60902f71f`)
- S6: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2130b12d-afbb-4f13-80ad-1150d840783f/resource) (`2130b12d-afbb-4f13-80ad-1150d840783f`)
- S28: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6027e3a-2c77-42a3-b1df-934c6eea6f9c/resource) (`a6027e3a-2c77-42a3-b1df-934c6eea6f9c`)
- S32: [铸造铝合金杂质允许含量表（GB1175—86）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c515247f-1c1b-4243-b398-0d1efd02d356/resource) (`c515247f-1c1b-4243-b398-0d1efd02d356`)
- S31: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbdfd10d-500b-41dd-bd20-5ac0efd8c501/resource) (`bbdfd10d-500b-41dd-bd20-5ac0efd8c501`)
- S27: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a59e9b99-dc6c-44a7-8dfb-c36c8180b4cc/resource) (`a59e9b99-dc6c-44a7-8dfb-c36c8180b4cc`)
- S16: [表3-2 中间包钢液中夹杂物平均密度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72c42a8b-ebe0-4c88-9ad0-c5c9cf92fde9/resource) (`72c42a8b-ebe0-4c88-9ad0-c5c9cf92fde9`)
- S12: [金属液态成型原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e633849-c16d-4b6a-bbfa-1eaf553e6cf0/resource) (`5e633849-c16d-4b6a-bbfa-1eaf553e6cf0`)
- S19: [有色金属熔炼入门与精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/857ec825-584f-495d-a1ef-b0c253bd646f/resource) (`857ec825-584f-495d-a1ef-b0c253bd646f`)
- S36: [铝熔体中杂质Fe扩散行为及熔剂润湿行为的分子动力学模拟与试验](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d496f93c-7658-406d-accb-086fdcf91560/resource) (`d496f93c-7658-406d-accb-086fdcf91560`)