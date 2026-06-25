---
version: "v1"
generated_at: "2026-06-18T09:08:09+00:00"
confidence_score: 0.83
confidence_level: "high"
confidence_basis:
  cited_sources: 26
  source_quality_score: 0.84
  freshness_score: 0.76
  evidence_coverage_score: 1.0
---

## 概述

DIEVAR 是由瑞典 Uddeholm Tooling 研发的铬-钼-钒（Cr-Mo-V）合金体系热作模具钢，专为高温高压环境设计，属于压铸模具领域的专用热作模具材料[[S21,S25]]。该材料在 AISI H13 基础上，通过优化化学成分与采用电渣重熔（ESR）生产工艺实现性能升级，是低硅优化型热作模具钢[[S33]]。相比常规热作模具钢，其高温强度、耐回火稳定性、韧性及抗热裂性能均得到针对性提升[[S33]]。

DIEVAR 硬度范围覆盖 40–52 HRC，兼具高韧性特征。其抗热疲劳性能较传统 H13 钢种提升约 2 倍[[S21]]。截至 2025 年，DIEVAR 已适配增材制造工艺，广泛应用于汽车零部件压铸、热挤压模具等工业场景[[S21]]。

DIEVAR 所属热作模具钢在模具钢总体分类中的位置，以及热作模具钢按性能特征的细分定位，可参见以下示意图。

![模具钢总体分类体系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aaafbbf4-33a0-4d61-b785-991a4aae0f70/resource)

**图1** 模具钢总体分类体系，DIEVAR 属于热作模具钢大类[[S23]]。

![热作模具钢按性能分类示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16681d0f-7f56-4e2e-96bf-c3485536c9bc/resource)

**图2** 热作模具钢按性能分为高韧性、高热强性、高耐磨性三类，DIEVAR 兼备高韧性与高热强性特征[[S6]]。

## 牌号定位与标准对应

DIEVAR 是 H13 的升级改良型商用钢种。H13 在各国标准体系中的对应牌号如下：

| 标准体系 | 对应牌号 |
|----------|----------|
| EN/DIN   | 1.2344 (X40CrMoV51) |
| AISI     | H13 |
| JIS      | SKD61 |
| GB       | 4Cr5MoSiV1 |

DIEVAR 属于上述牌号下的高纯度电渣重熔优化分支产品[[S30,S14]]。

## 化学成分

DIEVAR 所属基础 H13 钢的公开关键元素典型质量占比如下（单位：%）：

| 元素  | C    | Si   | Cr   | Mo   | V   |
|-------|------|------|------|------|-----|
| H13   | 0.39 | 1.00 | 5.40 | 1.35 | 1.00 |

DIEVAR 在该成分基础上完成了进一步的优化调整[[S30]]。

## 物理与力学性能

### 常规性能

- **出厂硬度**：退火状态 HB 160[[S21,S20]]
- **使用硬度区间**：40–52 HRC[[S21]]
- **抗热疲劳性能**：较传统 H13 钢提升约 2 倍[[S21]]

### 高温性能

在 44 HRC 硬度条件下，DIEVAR 在 600℃ 工况下的高温屈服强度可达 560 MPa，比同硬度等级的 Uddeholm 8407 钢（510 MPa）高出约 10%。这意味着 DIEVAR 具有更好的抗热变形能力与热疲劳表现[[S31]]。

DIEVAR 在相同韧性水平下，允许使用硬度比 8407 高出 2–3 HRC，较高的硬度有助于进一步改善热疲劳性能。在相同冷热循环次数下，DIEVAR 的热疲劳裂纹数目更少，主裂纹深度更浅[[S31]]。

## 热处理工艺

### 回火通用要求

热作模具钢回火时需规避 300℃ 附近的低温回火脆化区间。在 375–575℃ 区间完成回火后，应采用快速冷却方式，避免缓慢冷却诱导的第二类回火脆性[[S9]]。

### 氮碳共渗工艺与表面粗糙度的影响

DIEVAR 在可控低氮势、无白层的工业氮碳共渗工艺下，渗氮效果受基体表面粗糙度的显著影响[[S17,S26]]。

| 表面状态 | 粗糙度 Ra (μm) | 表面硬度 (HV₀.₂) | 渗层深度 (μm) | 均匀性 |
|----------|---------------|-----------------|--------------|--------|
| 400#砂纸及更粗 | ≥0.097 | 1060–1080 | 65–80 | 良好 |
| 1000#砂纸 | 0.032 | 硬区>1000 / 软区 805±5 | 硬区~50 / 软区无 | 失效，软硬分区 |
| 2000#砂纸 | 0.023 | 硬区>1000 / 软区 717±35 | 硬区~50 / 软区无 | 失效，软硬分区 |
| 抛光 | 0.012 | 581±10（接近基体） | 无可检测渗层 | 无明显氮化 |

当基体表面粗糙度在 Ra=0.097 μm（400#砂纸打磨）及以上时，氮碳共渗后可获得均匀完整、表面硬度达 1060–1080 HV₀.₂、有效渗层深度 65–80 μm 的渗氮层[[S17]]。而抛光试样（Ra=0.012 μm）在相同工艺条件下无明显氮化迹象，表面硬度仅为 581±10 HV₀.₂，略高于基体硬度水平[[S26]]。

氮碳共渗后，各试样表面粗糙度仅出现小幅提升，例如抛光试样 Ra 从处理前的 0.012 μm 提升至 0.015 μm，无显著突变[[S17]]。

上述规律在实体"凸"字形工件（46–48 HRC）的验证测试中得到证实：铣床加工面和 400#油石打磨面氮碳共渗后表面硬度 >1100 HV₀.₂，渗层深度约 70 μm；而 R5 mm 转角抛光区域无明显氮化迹象[[S26]]。

## 在压铸中的应用

### 典型应用场景

DIEVAR 主要应用于高压压铸模芯、镶件等核心成型部件，尤其在汽车零部件压铸领域使用广泛[[S21]]。对于大型一体化高压压铸模具，其核心成型区域（模块 A）推荐采用 DIEVAR 等高等级纯净热作模具钢，而靠近浇注系统的非复杂受力区域（模块 B）则可选用普通 H13 钢，在保证模具寿命的前提下降低整体制造成本[[S34]]。

大型一体化压铸模具由于尺寸大、需兼顾韧性与抗开裂能力，推荐使用硬度区间为 45–48 HRC[[S34]]。

### 服役寿命

在捷克高压压铸行业的嵌件寿命对比测试中，同一套高压压铸模具内安装多个不同材料嵌件，累计完成 12 万次压铸循环后，DIEVAR 嵌件仅出现可通过补焊抛光修复的初始微裂纹，远超常规铝合金压铸模具 6–8 万模次的寿命上限[[S24]]。

### 表面粗糙度调控的分区强化策略

实际生产中可利用 DIEVAR 表面粗糙度对渗氮效果的调控特性实现分区强化[[S26]]：

- **需要高耐冲蚀的区域**（如浇口附近）：控制表面粗糙度在合适区间（如 400#砂纸打磨水平），获得完整渗氮层，提升表面硬度和抗冲蚀能力。
- **热应力集中的 R 角区域**（易出现早期龟裂）：采用抛光处理，避免脆性氮化层，防止早期开裂与掉块。

## 失效机制

### 热疲劳裂纹（龟裂）

常规铝合金压铸过程中，模具在反复急冷急热循环下产生循环热应力，这是 DIEVAR 模具热疲劳裂纹失效的核心诱因。据统计，热疲劳裂纹失效在铝合金压铸模具总失效中占比约 67%，为占比最高的失效形式[[S32,S10,S19]]。更广泛的统计表明，约 80% 以上的铝合金压铸模具均因热裂而最终失效[[S31]]。

### 冲蚀失效

冲蚀失效多发生于靠近内浇口的高流速区域，由高速流动的 670℃ 以上铝合金熔体对模具表面的机械冲刷和化学腐蚀共同作用引发，占铝合金压铸模具总失效约 4%[[S32,S10]]。

### 铝合金熔体腐蚀（粘铝）

铝合金熔体长期接触 DIEVAR 模具表面时，铝元素会向基体扩散生成脆性 Fe-Al 金属间化合物相，该相作为裂纹萌生源加速裂纹扩展，最终引发粘铝失效[[S1]]。

### 热变形失效

当 DIEVAR 模具局部工作温度超过其回火温度阈值时，基体硬度下降，局部型腔表面发生不可逆塑性变形。应对措施包括优化模具冷却系统、控制压铸循环下的模具最高工作温度[[S1]]。

## 表面工程

### 氮碳共渗

通用盐浴氮碳共渗工艺（如 Tufftride、Sursulf）通常在 570℃ 保温 1–2 小时，可获得 10–20 μm 的化合物层。相较于常规气体渗氮，该类工艺无高脆性的针状铁氮化物生成，抗疲劳性能与抗磨损性能更优异[[S11,S22,S7]]。

对于 DIEVAR，氮碳共渗的具体效果与基体表面粗糙度密切相关（详见上文热处理工艺章节）。

### 离子渗氮

H13 类压铸模具适配的等离子渗氮参考工艺为：510℃ 保温 36 小时，氮氢混合比 25% N₂ + 75% H₂，压力 10 mbar，可获得 0.2 mm 渗层深度，表面硬度超过 63 HRC，可有效降低铝合金粘模倾向。该参数可作为 DIEVAR 离子渗氮的适配参考[[S11]]。

### PVD 涂层

针对压铸模具开发的 TiN、TiAlN、CrN 三类 PVD 涂层可显著提升模具表面的铝合金熔体腐蚀抗性和冲蚀抗性[[S8,S36]]。其中：

- TiN 涂层使用温度上限最低，高温下易氧化失效。
- 涂层沉积温度通常控制在 400–450℃，低于 DIEVAR 常规回火温度，不会造成基体回火软化。
- 涂层与预处理的渗氮层可形成梯度过渡结构，提升结合力，涂层厚度通常在几微米量级[[S8]]。

韧性优异的 DIEVAR 钢配合适配的 PVD 涂层，可获得兼顾抗热疲劳与抗冲蚀的综合服役性能[[S8]]。

## 与其他热作模具钢的比较

### 与 ASSAB 8407 的对比

ASSAB 8407 同为铬-钼-钒热作合金模具钢，采用电渣重熔工艺制备，出厂硬度约 HB 180，适用硬度范围 45–52 HRC，硫含量可低至 0.0005%，主要应用于铝镁合金压铸模具[[S27]]。

DIEVAR 相较于 8407 的核心优势：
- 600℃ 下高温屈服强度高出约 10%（560 MPa vs 510 MPa，同 44 HRC 条件下）[[S31]]
- 相同韧性水平下允许使用硬度高出 2–3 HRC[[S31]]
- 相同冷热循环次数下热疲劳裂纹数目更少，主裂纹深度更浅[[S31]]

### 常用铝合金压铸模用钢化学成分对比

以下为 DIEVAR 与 H13 等多种热作模具钢的化学成分对比，可直观反映不同钢种的合金体系差异[[S35]]。

> **表** 常用铝合金压铸模用钢化学成分对比（含 DIEVAR、H13 等）

### H13 与 H11 的力学性能参考

作为 DIEVAR 基础钢种的参照，H13 与 H11 钢经 1000℃ 淬火及 580℃ 二次回火后的力学性能如下[[S13]]：

| 钢种 | 硬度 (HRC) | 抗拉强度 (MPa) | 延伸率 (%) | 冲击韧性 (J·m⁻²) |
|------|-----------|---------------|-----------|-----------------|
| H11 | 51 | 1745 | 13.5 | 5.5 |
| H13 | 51 | 1830 | 9.0 | 1.9 |

DIEVAR 在 H13 基础上通过低硅优化和电渣重熔工艺，在保持强度的同时显著提升了韧性水平[[S33,S21]]。

## Sources
- S21: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d58fada-e9ca-41f7-8ccf-a494bd37b45c/resource) (`9d58fada-e9ca-41f7-8ccf-a494bd37b45c`)
- S25: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae517daa-87f6-4d79-adab-6d96990dee6c/resource) (`ae517daa-87f6-4d79-adab-6d96990dee6c`)
- S33: [TextNode111](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/defc9ce1-9d9b-42c6-a097-dddf1a340564/resource) (`defc9ce1-9d9b-42c6-a097-dddf1a340564`)
- S23: [模具钢的分类图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aaafbbf4-33a0-4d61-b785-991a4aae0f70/resource) (`aaafbbf4-33a0-4d61-b785-991a4aae0f70`)
- S6: [热作模具钢按性能分类示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16681d0f-7f56-4e2e-96bf-c3485536c9bc/resource) (`16681d0f-7f56-4e2e-96bf-c3485536c9bc`)
- S30: [0197_c95046d5da48befa_Tool_steel_1.2344](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb7f0c4e-f468-47c1-b3d4-6913a701f1eb/resource) (`cb7f0c4e-f468-47c1-b3d4-6913a701f1eb`)
- S14: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c11e4c5-0199-4968-b428-f651d8e395e6/resource) (`5c11e4c5-0199-4968-b428-f651d8e395e6`)
- S20: [DIEVAR 热作模具钢关键属性表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96e33fd9-94b3-4d68-a122-5161bccf776e/resource) (`96e33fd9-94b3-4d68-a122-5161bccf776e`)
- S31: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5c59de2-325e-4317-94af-23526908f267/resource) (`d5c59de2-325e-4317-94af-23526908f267`)
- S9: [4146860_回火处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d2d7761-1f0e-448b-948f-628fb68337ed/resource) (`1d2d7761-1f0e-448b-948f-628fb68337ed`)
- S17: [DIEVAR模具钢表面粗糙度对其渗氮能力的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d7c284c-65bf-45a0-9993-c5813f0d9873/resource) (`8d7c284c-65bf-45a0-9993-c5813f0d9873`)
- S26: [DIEVAR模具钢表面粗糙度对其渗氮能力的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3cbe18e-a9dc-4314-bb85-95134f33d350/resource) (`b3cbe18e-a9dc-4314-bb85-95134f33d350`)
- S34: [大型压铸模是实现一体化压铸的关键技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e091c932-98f5-4495-ba22-e3d5b48bc3ad/resource) (`e091c932-98f5-4495-ba22-e3d5b48bc3ad`)
- S24: [development of a new tool material for high pressure die casting__040512a74d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/acac86df-ecdb-4c70-9dda-9550696cec73/resource) (`acac86df-ecdb-4c70-9dda-9550696cec73`)
- S32: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6862891-fc2d-4b40-bc27-d2bf20e30913/resource) (`d6862891-fc2d-4b40-bc27-d2bf20e30913`)
- S10: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3506891f-699a-450d-87b6-10c97199c9c1/resource) (`3506891f-699a-450d-87b6-10c97199c9c1`)
- S19: [energy based approach to thermal fatigue life of tool steels for die cas__16af947521](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/925ac59f-f6b6-4e07-9908-d6a1d915fdce/resource) (`925ac59f-f6b6-4e07-9908-d6a1d915fdce`)
- S1: [模具表面处理与表面加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00c373d1-a4c6-481c-83c4-fe9d5419c2f4/resource) (`00c373d1-a4c6-481c-83c4-fe9d5419c2f4`)
- S11: [die casting metallurgy surface treatments for steels__6de99569f3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37ea7268-83b2-42fe-97f8-885bc9117ef0/resource) (`37ea7268-83b2-42fe-97f8-885bc9117ef0`)
- S22: [die casting metallurgy__322fa9dd3c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a00f82ea-a0f8-4105-8a50-24f2aedac2b6/resource) (`a00f82ea-a0f8-4105-8a50-24f2aedac2b6`)
- S7: [die casting metallurgy__8f9e04f2f0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/182cfbeb-794a-41b0-832b-5ddd95403bdb/resource) (`182cfbeb-794a-41b0-832b-5ddd95403bdb`)
- S8: [a study of pvd coatings and die materials for extended die casting die l__ab4f8ab817](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18f16892-df13-489a-948f-e12b9d4e31e8/resource) (`18f16892-df13-489a-948f-e12b9d4e31e8`)
- S36: [corrosion tests of pvd coatings with die lubricant used for al high pres__31d67bdb30](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9c48cb5-43b8-4aa9-98a3-2cfaa0046d8b/resource) (`f9c48cb5-43b8-4aa9-98a3-2cfaa0046d8b`)
- S27: [6149647_8407模具钢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b61405c9-27d0-459b-b9c6-34f9e00e3d70/resource) (`b61405c9-27d0-459b-b9c6-34f9e00e3d70`)
- S35: [常用铝合金压铸模用钢化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e54cf772-7e16-41f1-8742-d28958f14148/resource) (`e54cf772-7e16-41f1-8742-d28958f14148`)
- S13: [H11、H13 钢热处理规范与力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5680a7c1-2817-463c-a209-15f9c3c4895a/resource) (`5680a7c1-2817-463c-a209-15f9c3c4895a`)