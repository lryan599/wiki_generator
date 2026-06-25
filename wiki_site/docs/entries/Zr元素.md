---
version: "v1"
generated_at: "2026-06-21T06:08:54+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 34
  source_quality_score: 0.86
  freshness_score: 0.84
  evidence_coverage_score: 1.0
---

## 概述

锆（Zr）作为过渡族微合金化元素，在压铸铝合金及变形铝合金中常以微量添加形式使用，主要作用包括晶粒细化、固溶强化、抑制再结晶并提升高温性能。[[S19,S39]] 在 Al-Mg-Zn 系合金中，Zr 可控制晶粒伸长与再结晶过程，降低应力腐蚀敏感性；在 Al-Si 系免热处理压铸铝合金中，Zr 通过生成纳米析出相实现细晶强化，是免固溶处理合金设计的关键强化元素之一。[[S19,S39,S38]]

## 基本性质与在铝基体中的行为

锆原子半径为 0.160 nm，显著大于铝基体的 0.143 nm，固溶时引起严重的晶格畸变，从而阻碍位错运动，产生固溶强化效应。[[S22]] 固溶 Zr 含量的增加使铝基体晶格参数线性增长；含 2.2 wt% Zr 时，晶格参数升至 4.054 × 10⁻¹⁰ m，同时高温区热膨胀系数降低，熔体粘度上升，电阻率迅速增至 18 × 10⁻⁸ Ω·m。[[S5,S21]]

## Al‑Zr 二元相图与固溶度

Al‑Zr 体系铝端的不变反应为包晶反应：含 0.11 wt% Zr 的液相与 ZrAl₃ 反应生成铝基固溶体，公认的包晶平衡温度为 933.5 K（约 660.4 ℃），而非早期提出的 937 K。[[S18,S39]] 平衡状态下，Zr 在铝基固溶体中的最大固溶度为 0.28 wt% Zr（933.5 K），随温度降低固溶度持续下降，700 K 时仅为 0.05 – 0.06 wt% Zr。[[S10,S29,S39]] 当采用液相快淬等非平衡凝固手段时，Zr 的过饱和固溶度可提升至 2 – 2.5 wt% Zr。[[S10,S29,S18]]

![Al‑Zr二元合金相图，示出铝端包晶反应及富铝端固溶度变化。](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8949e8b6-afba-429d-b27c-380b7284fe05/resource)

## 相结构与化合物

### 平衡相 Al₃Zr

平衡态 Al₃Zr 含 53.0 wt% Zr，熔点为 1850 K，属体心四方晶系，空间群 I4/mmm，晶胞含 16 个原子；晶格参数 a = 4.013 – 4.015 × 10⁻¹⁰ m，c = 17.32 – 17.35 × 10⁻¹⁰ m。[[S18,S39]] 其密度约 4100 kg/m³，电阻率 17 × 10⁻⁸ Ω·m，热膨胀系数 12.1 × 10⁻⁶ m/(m·K)，维氏硬度高达 4270 – 7400 MN/m²，属于典型的高硬度脆性金属间化合物。[[S5,S18]]

### 亚稳相

在快速凝固或从过饱和固溶体时效过程中，可析出亚稳 L1₂ 型立方结构的 Al₃Zr 相（空间群 Pm3m，点阵常数约 4.05 × 10⁻¹⁰ m），取向关系为 (001)ₚ∥(001)Al，[100]ₚ∥[100]Al。[[S27]] 持续时效后，亚稳相可转变为稳定的 DO₂₃ 型四方 Al₃Zr 相。[[S16,S34]] 亚稳 L1₂‑Al₃Zr 与铝基体的晶格错配度约为 +0.8%，属于极低界面错配水平，有利于高效异质形核。[[S27,S40]]

### (Al, Zr, Si) 三元针状相

Al‑Zr‑Si 三元体系中存在四方 D0₂₂ 型结构的 (Al, Si)₃Zr 相，其稳定形式约为 (Al₀.₉, Si₀.₁)₃Zr，晶格参数 a = 5.520 Å，c = 9.008 Å。[[S7]] 该相多呈针状形貌，择优沿 (002) 晶向生长，尺寸明显大于共晶 Si，常横跨晶粒。[[S50]] 其形成受 Mg、Zn 元素促进：Mg 与 Zn 同时加入会提高 Zr 的偏摩尔吉布斯自由能，减弱 Zr 在液相中的稳定性，促使其与 Si 反应形成该针状相。[[S50,S15]] 硅的存在还会降低 Zr 在铝中的固溶度，促使 (Al, Si)₃Zr 提前析出；富铝端 Al‑Zr‑Si 三元相图中，仅 Al₃Zr 相与单质 Si 可与铝基体平衡共存。[[S43]]

![免固溶处理XA铝合金中含Si、Zr的针状相TEM形貌，标尺10 μm，显示针状相尺寸与分布。](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3f8e0574-4873-44ac-8453-aed116acde2a/resource)

## 晶粒细化机制

### 异质形核与错配度

当铝合金熔体中 Zr 含量超过 0.11 wt% 时，冷却过程中会优先析出初生 Al₃Zr 相，该相可作为 α‑Al 的异质形核核心，降低形核功从而实现晶粒细化。[[S17]] Zr 诱导 α‑Al 形核无需额外过冷，存在多个低不共格的取向匹配关系，且亚稳 L1₂‑Al₃Zr 与铝基体的晶格错配度仅约 +0.8%，能实现低能共格界面，提升异质形核效率。[[S27,S40]]

### 临界条件与形成温度

初生 Al₃Zr 的形成温度随 Zr 含量增加而显著升高。以 2219 铝合金为例，Zr 质量分数在 0.11 ‑ 0.25% 区间时，初生 Al₃Zr 形成温度从 660.5 ℃ 逐步升至 741 ℃。[[S17,S48]]

| Zr 质量分数 (wt%) | 初生 Al₃Zr 形成温度 (℃) |
|-------------------|--------------------------|
| 0.11              | 660.5                    |
| 0.13              | 约 672                   |
| 0.16              | 约 692                   |
| 0.19              | 约 711                   |
| 0.22              | 约 727                   |
| 0.25              | 741                      |

*表据 [[S48]] 数据整理。*

虽然提高 Zr 含量可增强晶粒细化效果，但通常需 Zr 含量达 2 wt% 以上才能观察到明显的柱状晶转变；工业中单独使用 Zr 作为晶粒细化剂的效率低于 Ti，且无法通过添加 B 元素提升细化效果，因此 Zr 未被用作商用主流晶粒细化剂。[[S19,S17]]

### 与传统细化剂的对比及“毒化”效应

当铝合金中同时存在 Zr 与 Al‑Ti‑B（或 Al‑Ti‑C）细化剂时，会诱发细化剂“中毒”。Zr 与 TiAl₃ 反应生成 (Ti₁₋ₓZrₓ)Al₃ 三元相，改变 TiAl₃ 与铝基体的晶格匹配度，降低 TiB₂ 表面富 Ti 层的吸附能力，从而削弱细化效果。[[S46]] 在 800 ℃ 下仅需 0.12 wt% Zr 即可使 0.2 wt% 的 Al‑5Ti‑0.4C 完全失去细化作用，对于 Al‑5Ti‑1B 细化剂，随 Zr 添加量从 0 增加至 0.12 wt%，晶粒显著粗化。[[S44,S33]]

## 固溶强化与沉淀析出

Zr 原子半径远大于 Al，固溶于基体时产生强烈的晶格畸变，阻碍位错运动，从而发挥固溶强化作用。[[S22]] 当含有过饱和 Zr 的铝合金进行时效处理时，首先析出与基体共格的纳米 L1₂ 型 Al₃Zr 相，随后逐步转变为稳态 DO₂₃ 型四方 Al₃Zr。[[S27,S16]] 这些低错配度的纳米析出相可有效钉扎晶界、亚晶界与位错，可将铝合金再结晶温度最高提升 100 K，显著改善高温强度与抗蠕变性能。[[S27,S16]] 在 2219 等耐热铝合金中，弥散分布的 Al₃Zr 纳米相还能延缓高温下 θ 相的粗化，使合金经 300 ℃ × 100 h 热暴露后仍保持细小均匀的析出组织，保障高温服役稳定性。[[S32]]

## 在免热处理/免固溶处理压铸铝合金中的应用

### Castasil‑37 合金

德国莱茵菲尔德公司开发的 Castasil‑37（AlSi9MnMoZr）是一种商用免热处理压铸合金，不含 Mg，复合添加了 Mo 和 Zr（总占比 < 0.3 wt%，Zr 添加量处于 0.1 – 0.2 wt% 的工业参考区间）。[[S38,S3]] 在压铸快冷条件下，Zr 形成细小弥散相，实现细晶强化；与未添加 Zr 的同基体合金相比，合金延伸率提升约 30%，铸态屈服强度可达 120 MPa 以上，延伸率可达 12% 以上，适用于高载荷、高韧性的汽车结构件。[[S38,S3]] 与此相对的 Silafont‑36（AlSi9Mg）原生合金并未引入 Zr，其强韧化主要依靠低 Fe 控制、Sr 变质及 Mn/Fe 比的优化。[[S28,S23]]

### 免固溶处理 XA 铝合金

“免固溶处理”指合金在铸态或仅经低温时效即可获得满足要求的力学性能，避免了固溶淬火带来的变形与表面缺陷。公开报道的 XA 铝合金为一种 Al‑Si‑Zn‑Mg‑Cu 系免固溶处理合金，其 Zr 成分控制在 0.1 – 0.3 wt%。[[S6]] 重力铸造条件下，该合金铸态室温抗拉强度为 221 MPa；添加 La、Sb 复合变质后，共晶硅形态改善，抗拉强度提升至 232 MPa，延伸率由 2.11% 增至 3.58%。[[S20]] 采用压铸工艺并仅经 150 ℃ 时效处理后，抗拉强度可达 293 MPa，体现出 Zr 微合金化与压铸快冷相结合的优势。[[S20,S42]]

## 压铸工艺与加入方式

工业生产中，铝合金添加 Zr 的主流方式为 Al‑Zr 中间合金，推荐使用含 Zr 10% 的商用 Al‑10Zr 中间合金。[[S47,S25]] 加入时熔体温度宜控制在 730 – 740 ℃，加入后保温 20 min 以保证完全熔解分散，随后依次进行精炼、除气、静置，确保成分均匀。[[S4]] 早期使用的锆盐添加法（如 K₂ZrF₆、ZrCl₄）Zr 吸收率仅为 3% – 18%，工艺复杂且易引入杂质，当前工业场景已基本淘汰。[[S47,S25]]

## 缺陷与限制

### 粗大初生 Al₃Zr 脆性相

当 Zr 含量超过其在铝基体中的溶解度时，Zr 元素偏聚并在凝固过程中生成粗大的枝晶状 Al₃Zr 相，无法作为有效形核基底，反而劣化合金的塑韧性与力学性能。[[S35,S44]] 低 Zr 含量时 Al₃Zr 呈细小弥散分布，过量即产生粗大枝状，危害极大。[[S44]]

### (Al, Zr, Si) 针状相降低塑性

在含 Mg、Zn 的合金中易形成 (Al, Zr, Si) 针状相。该相尺寸显著大于共晶 Si，常横跨晶粒，受载时优先发生断裂并扩展至基体，成为脆性断裂的裂纹源，大幅降低合金延伸率。[[S50,S15]]

### 细化剂“中毒”与添加上限

Zr 易与 Al‑Ti‑B、Al‑Ti‑C 等细化剂中的 TiAl₃、TiC 反应，形成 Al₃(Zr, Ti) 团聚物，导致细化剂失效。[[S44]] 从工艺可行性与性能角度考虑，压铸铝合金中 Zr 的安全添加上限建议为 0.1 wt%，超过该值易引起元素偏聚、降低合金流动性，并生成粗大初生相，恶化力学性能。[[S36]] 此外，Zr 成本较高，使其在设计低成本的免热处理合金时需综合考虑强化效果与经济性。[[S6]]

## Sources
- S19: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59cd6796-6bec-46ab-b84a-b3a767a619ab/resource) (`59cd6796-6bec-46ab-b84a-b3a767a619ab`)
- S39: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b892217a-6468-4024-b7f0-044f8a98b455/resource) (`b892217a-6468-4024-b7f0-044f8a98b455`)
- S38: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b79ab69b-233a-477d-99d7-7fccc1cc57ce/resource) (`b79ab69b-233a-477d-99d7-7fccc1cc57ce`)
- S22: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/805ad2ad-2943-4573-af4f-b2c9d9f60339/resource) (`805ad2ad-2943-4573-af4f-b2c9d9f60339`)
- S5: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b5ad462-77c0-4799-a917-b31d3599865f/resource) (`0b5ad462-77c0-4799-a917-b31d3599865f`)
- S21: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76194af3-25e1-4189-a1c1-5d971d2363e2/resource) (`76194af3-25e1-4189-a1c1-5d971d2363e2`)
- S18: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/532c2678-96f7-46ec-abaa-094b5bb4fcab/resource) (`532c2678-96f7-46ec-abaa-094b5bb4fcab`)
- S10: [船用铝合金焊接及其船体建造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25541e1f-cd67-41f4-85c4-439d20377f31/resource) (`25541e1f-cd67-41f4-85c4-439d20377f31`)
- S29: [船用铝合金焊接及其船体建造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/931b6369-b453-46df-85fb-9c308b1651ac/resource) (`931b6369-b453-46df-85fb-9c308b1651ac`)
- S27: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f1a4602-fefd-4df2-8da1-957703f242c1/resource) (`8f1a4602-fefd-4df2-8da1-957703f242c1`)
- S16: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ec66b5a-7af1-4ce9-9aff-cde988527cba/resource) (`4ec66b5a-7af1-4ce9-9aff-cde988527cba`)
- S34: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a18bd1d4-eedf-4a25-b482-1751cf52300a/resource) (`a18bd1d4-eedf-4a25-b482-1751cf52300a`)
- S40: [aluminium lithium alloys iii proceedings of the third international aluminium lithium conference__658fc7f1f6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bacc628a-6704-44c5-a1a3-6999e9455a25/resource) (`bacc628a-6704-44c5-a1a3-6999e9455a25`)
- S7: [a handbook of lattice spacings and structures of metals and alloys__d7369eca0e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e382bdc-a011-420d-ad75-9be1229e381a/resource) (`0e382bdc-a011-420d-ad75-9be1229e381a`)
- S50: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef0a05c9-c511-4ef3-b335-d8af95f7a842/resource) (`ef0a05c9-c511-4ef3-b335-d8af95f7a842`)
- S15: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42f6098a-3b27-4274-80e7-51940176b636/resource) (`42f6098a-3b27-4274-80e7-51940176b636`)
- S43: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6418f18-c523-4474-b549-9810d8bef5ed/resource) (`d6418f18-c523-4474-b549-9810d8bef5ed`)
- S17: [电磁搅拌2219铝合金铸锭夹杂物形成机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f610c09-1f72-4947-ba7b-5030b18ff2bf/resource) (`4f610c09-1f72-4947-ba7b-5030b18ff2bf`)
- S48: [表5.1 不同Zr元素含量的初生Al₃Zr相形成温度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4e154a3-9c3d-4437-8a5f-df4efb3240ae/resource) (`e4e154a3-9c3d-4437-8a5f-df4efb3240ae`)
- S46: [aluminium cast house technology viii__22bdc9a7f6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3f0ab29-792c-4cce-b73d-bc3e31472a53/resource) (`e3f0ab29-792c-4cce-b73d-bc3e31472a53`)
- S44: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dab080d4-ba53-4a23-9ecf-29e9d527dd81/resource) (`dab080d4-ba53-4a23-9ecf-29e9d527dd81`)
- S33: [图2-30 向工业纯铝中加入Zr元素后的宏观组织照片](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f3d1ed8-298d-4022-9ccb-8a36b4e91ee5/resource) (`9f3d1ed8-298d-4022-9ccb-8a36b4e91ee5`)
- S32: [稀土在铝合金中的行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d294b9d-5824-4963-97bb-c0cfbc8be8e9/resource) (`9d294b9d-5824-4963-97bb-c0cfbc8be8e9`)
- S3: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07f6a7c3-735f-457a-88fe-8eeca3cac19d/resource) (`07f6a7c3-735f-457a-88fe-8eeca3cac19d`)
- S28: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f2d83aa-b1de-4301-acd1-3fa2a6cba5ef/resource) (`8f2d83aa-b1de-4301-acd1-3fa2a6cba5ef`)
- S23: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82013eee-6b17-4059-9384-bca4ce09589a/resource) (`82013eee-6b17-4059-9384-bca4ce09589a`)
- S6: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d36da63-63bf-4c22-9326-79e464ddba82/resource) (`0d36da63-63bf-4c22-9326-79e464ddba82`)
- S20: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6643981c-fdeb-4e31-bf48-a1d19c156cfd/resource) (`6643981c-fdeb-4e31-bf48-a1d19c156cfd`)
- S42: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cfd35b75-37ff-4857-b98b-92e72e26aac0/resource) (`cfd35b75-37ff-4857-b98b-92e72e26aac0`)
- S47: [有色合金铸造经验选编](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e48528af-c45d-4f02-b6cc-005c99d2dfbd/resource) (`e48528af-c45d-4f02-b6cc-005c99d2dfbd`)
- S25: [有色合金铸造经验选编](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8402c83d-d1f2-48b1-bc39-12fbce28e849/resource) (`8402c83d-d1f2-48b1-bc39-12fbce28e849`)
- S4: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0871ac40-4658-413f-a50a-f2ab84f9ee42/resource) (`0871ac40-4658-413f-a50a-f2ab84f9ee42`)
- S35: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab761791-ece2-472a-9f27-0b9cab830207/resource) (`ab761791-ece2-472a-9f27-0b9cab830207`)
- S36: [基于AlSi8系高强韧免热处理压铸铝合金开发及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af7bd26c-054a-4e88-bfea-8298ce06892e/resource) (`af7bd26c-054a-4e88-bfea-8298ce06892e`)