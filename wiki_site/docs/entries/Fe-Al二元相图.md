---
version: "v1"
generated_at: "2026-06-18T15:41:58+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 25
  source_quality_score: 0.86
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

## 概述

Fe-Al二元相图（又称Al-Fe相图）是描述铁（Fe）与铝（Al）二元合金体系在不同温度与成分条件下平衡相组成与相变规律的热力学模型。该相图在压铸工艺中主要用于分析铝合金熔体与钢制模具（如H13钢）界面处发生的金属间化合物生成、粘模（焊合）机理以及铝合金中铁元素含量的调控。全成分范围相图包含液相(L)、富铁端α-Fe固溶体、富铝端(Al)固溶体以及Fe₃Al、FeAl、FeAl₂、Fe₂Al₅、FeAl₃等一系列金属间化合物相区[[S18,S26]]。

## 关键相与特征温度

Fe-Al二元体系中存在多个具有不同晶体结构与稳定温度区间的中间相，下表汇集了各相的基本参数与相变特征。

| 相名称 | 化学式/标识 | 晶体结构 | 铝含量范围 | 生成方式与关键温度 | 备注 |
|--------|-------------|----------|-------------|-------------------|------|
| α-Fe | α-(Fe,Al) | 体心立方 (bcc)，a=2.8664 Å | 0~34.5 wt% (最大溶解度，1232°C) | — | 常温下铝含量约30 wt% [[S30,S36]] |
| β-Fe (Fe₃Al) | Fe₃Al | DO₃有序结构 (BiF₃型)，a≈0.578 nm | 25~32 at.% (室温) | 有序化转变温度约550~555°C，高于此温度转变为无序bcc结构 [[S16,S20,S33]] | β-Fe为Fe₃Al相的有序态，上限约555°C |
| FeAl (β₂) | FeAl | B2有序结构 (CsCl型)，a=0.2903 nm | 33~51 at.% (室温) | 稳定存在温度范围宽，从室温至约1100°C [[S16,S30]] | — |
| ε相 | — | — | — | 1232°C包晶反应生成，1103°C~1232°C区间稳定，低于1103°C分解 [[S36]] | — |
| FeAl₂ (ζ) | FeAl₂ | 单斜晶系 | ~49.13 wt% | 1158°C形成（亚稳相），低于1000°C时发生分解反应：3FeAl₂ = Fe(Al) + Fe₂Al₅ [[S30,S36]] | 亚稳相 |
| Fe₂Al₅ (η) | Fe₂Al₅ | 斜方晶系，a=7.688 Å，b=6.408 Å，c=4.20 Å | 52.7~55.4 wt% | 熔点1173°C [[S30,S31]] | 压铸界面最易生成的铁铝相 |
| FeAl₃ (θ) | FeAl₃/Al₁₃Fe₄ | 单斜晶系，a=15.489 Å，b=8.0834 Å，c=12.476 Å，β=107°43' | 58~59.4 wt% | 1160°C包晶反应生成 [[S30,S31]] | 压铸铝合金中最常见的富铁杂质相 |

### 关键共晶与包晶反应点

- **1165°C**：铝浓度约50 wt%处发生共晶反应，产物为ε相 + Fe₂Al₅(η相) [[S36]]。
- **1160°C**：铝浓度59.2 wt%处发生包晶反应，生成FeAl₃(θ相) [[S36]]。
- **665°C（富铝端共晶点）**：铝浓度为98.3 wt%，此温度下铁在铝中的最大溶解度为0.03 wt% [[S36]]。该共晶反应为L ↔ (Al) + FeAl₃，共晶温度下铁在铝基体中的最大溶解度为0.052 wt% [[S8,S14]]。当铝基体中铁含量超过该值时，平衡组织中将出现α(Al) + FeAl₃共晶[[S14,S5]]。

### β-Fe相温度范围的核实

β-Fe相（即Fe₃Al有序相）的稳定温度上限经多个权威资料确认约为550~555°C，而非某些提示中给出的570~615°C。当温度高于约555°C时，Fe₃Al的DO₃有序结构将转变为无序的bcc型α-Fe固溶体[[S33,S20]]。压铸工况下模具表面温度通常超过该值，因此β-Fe有序相不易在压铸界面直接生成。

## 压铸工艺相关性

### 模具与铝合金的匹配

压铸生产中常用的模具钢为H13（4Cr5MoSiV1），其典型化学成分为：C 0.32%~0.45%、Si 0.80%~1.20%、Mn 0.20%~0.50%、Cr 4.75%~5.50%、Mo 1.10%~1.75%、V 0.80%~1.20%，余量为Fe [[S3,S35,S34]]。

典型压铸铝合金的铁含量控制范围如下：
- **ADC12 (AlSi11Cu3)**：常规铁含量上限为1.3 wt%，工业实际生产中通常控制在0.6~0.9 wt% [[S17,S22]]。
- **A380 (AlSi9Cu3)**：常规铁含量控制在0.6~1.0 wt%范围内 [[S6,S25]]。

### 界面反应与焊合机制

当H13钢模具与熔融铝合金接触时，铝原子向钢基体扩散，铁原子向铝侧反向渗透。基于Fe-Al二元相图，可将模具-铝液界面区域划分为三个区[[S27,S23]]：

| 界面分区 | 铝含量范围 | 主要相组成 | 固相线温度 | 压铸意义 |
|---------|-----------|-----------|-----------|---------|
| I区（靠近铝液侧） | >61.3 wt% | FeAl₃ + 富铝液相 | 655°C（Al-FeAl₃共晶温度） | 焊合的关键区域 |
| II区（中间化合物层） | 11~61.3 wt% | FeAl₃, Fe₂Al₅, FeAl₂, FeAl | 均高于1100°C | 固态存在，不影响焊合 |
| III区（钢基体） | <11 wt% | 钢基体 | — | 未受明显影响的基材 |

当模具表面温度高于655°C（即Al + FeAl₃共晶反应的临界温度）时，I区将出现富铝液相。该液相在冷却凝固过程中同时嵌入模具侧的金属间化合物层和铝合金铸件基体，形成冶金结合，最终导致压铸焊合（粘模）缺陷。液相的体积分数随铝原子向模具内部的扩散量增大而升高，粘模严重程度随之增大[[S2,S12]]。

### 合金元素对焊合临界温度的影响

基于Fe-Al二元相图的热力学延伸计算表明，常用合金元素对Al-Fe体系固相线温度（即焊合临界温度）的影响规律如下[[S24]]：

- **提高临界温度（有利于抑制焊合）**：Ti、Cr、Mn
- **降低临界温度（加剧焊合倾向）**：Cu（降低效果最强）、Ni、Zn、Mg、Si

该规律可直接用于ADC12、A380等典型压铸铝合金的成分优化设计。

### 压铸生产中铁含量的调控实践

在铝硅系压铸铝合金中，将铁元素含量控制在0.8~0.9 wt%区间，可依据Fe-Al二元相图的固溶度规律减缓模具侧铁原子向铝液的溶解扩散速率，从而大幅降低铁铝金属间化合物的生成速率，有效减轻粘模缺陷。该方法已在汽车发动机缸体、磁电机盖等压铸件的批量生产中成功应用[[S22,S19]]。当铁含量低于0.7 wt%时，模具表面铁原子向铝液的渗透速率会加快，粘模缺陷风险显著升高[[S22]]。

## 相图图示

ASM合金相图集收录的Fe-Al二元平衡相图是压铸领域进行界面反应热力学分析最为权威的参考版本，横轴同时标注铝的原子百分比与质量百分比，纵轴为温度，完整标注了液相L、αFe、(Al)以及Fe₃Al、FeAl、FeAl₂、Fe₂Al₅、FeAl₃等所有平衡相的相区边界与特征温度[[S18]]。

![ASM数据库标准Fe-Al二元合金相图，完整标注各平衡相区与特征温度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/735178a0-26e0-46af-ab75-88fcdb8b9a49/resource)

富铁区域的局部相图则清晰展示了α-Fe、Fe₃Al（β-Fe）、FeAl等相区的边界以及与有序-无序转变相关的关键温度点，可用于理解β-Fe相的热力学稳定范围[[S32]]。

![Fe-Al二元相图富铁侧局部放大图，标注αFe与Fe₃Al相区边界及有序化转变温度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2bf8f38-fd4d-4f4c-b4b3-ef01253b06f0/resource)

## Sources
- S18: [Fe-Al二元合金相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/735178a0-26e0-46af-ab75-88fcdb8b9a49/resource) (`735178a0-26e0-46af-ab75-88fcdb8b9a49`)
- S26: [Fe-Al二元合金相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afe9b0b2-7ce4-4bd1-b613-e2a7a1d29a40/resource) (`afe9b0b2-7ce4-4bd1-b613-e2a7a1d29a40`)
- S30: [铝及铝合金与其他金属的焊接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbbc5b91-2b70-4478-bf32-2692a4815c44/resource) (`cbbc5b91-2b70-4478-bf32-2692a4815c44`)
- S36: [TextNode396](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea529c92-9f79-4315-8b4a-ced65ebe9854/resource) (`ea529c92-9f79-4315-8b4a-ced65ebe9854`)
- S16: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e80e6cc-6588-41f8-8baa-9d8845957858/resource) (`4e80e6cc-6588-41f8-8baa-9d8845957858`)
- S20: [constitution of binary alloys__494ae46018](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8331f875-e937-4286-88c6-837e0b63f87f/resource) (`8331f875-e937-4286-88c6-837e0b63f87f`)
- S33: [constitution of binary alloys second supplement__3fdd8bcc52](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d516aa7b-d5ce-40dc-820f-bedd601843d7/resource) (`d516aa7b-d5ce-40dc-820f-bedd601843d7`)
- S31: [表面处理技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf4ea3ab-aeb3-46cb-8eea-8dd8e4379f3b/resource) (`cf4ea3ab-aeb3-46cb-8eea-8dd8e4379f3b`)
- S8: [船用铝合金焊接及其船体建造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25541e1f-cd67-41f4-85c4-439d20377f31/resource) (`25541e1f-cd67-41f4-85c4-439d20377f31`)
- S14: [铝合金材料组织与金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48061ca6-76db-4861-b055-dd6c3e38d6ba/resource) (`48061ca6-76db-4861-b055-dd6c3e38d6ba`)
- S5: [船用铝合金焊接及其船体建造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10834ff0-4bcb-43c0-87a9-36529610601a/resource) (`10834ff0-4bcb-43c0-87a9-36529610601a`)
- S3: [模具材料及表面强化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0992cc81-ed39-44dd-adca-898444e4808f/resource) (`0992cc81-ed39-44dd-adca-898444e4808f`)
- S35: [10398210_H13钢材](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc323f7a-0003-435c-9e0a-fe587dfc5769/resource) (`dc323f7a-0003-435c-9e0a-fe587dfc5769`)
- S34: [表4-3 H13化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da62db55-2eeb-4d10-9653-04af198b587b/resource) (`da62db55-2eeb-4d10-9653-04af198b587b`)
- S17: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6daa7aff-a93f-46c5-833a-17489008219b/resource) (`6daa7aff-a93f-46c5-833a-17489008219b`)
- S22: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/878ebc6a-9d77-4114-af0e-248bf5edb82a/resource) (`878ebc6a-9d77-4114-af0e-248bf5edb82a`)
- S6: [H13与A380材料的化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22372649-efcc-4d22-98ac-213979cc6b4c/resource) (`22372649-efcc-4d22-98ac-213979cc6b4c`)
- S25: [高真空压铸铝合金的研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af18281e-e7d7-4f82-b357-4adb0e2d94a3/resource) (`af18281e-e7d7-4f82-b357-4adb0e2d94a3`)
- S27: [analysis of the mechanism of die soldering in aluminum die casting__39352dca37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bab6a9bd-de0f-478b-8129-a7b1aecfd7c4/resource) (`bab6a9bd-de0f-478b-8129-a7b1aecfd7c4`)
- S23: [analysis of the mechanism of die soldering in aluminum die casting__39352dca37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95194fd0-85da-4bd7-88fa-218e5d59a1b8/resource) (`95194fd0-85da-4bd7-88fa-218e5d59a1b8`)
- S2: [analysis of the mechanism of die soldering in aluminum die casting__39352dca37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0301d1d1-a5e9-42ca-a830-8821087cd8e2/resource) (`0301d1d1-a5e9-42ca-a830-8821087cd8e2`)
- S12: [analysis of the mechanism of die soldering in aluminum die casting__39352dca37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/422d14e5-61af-43df-9170-ca1a316110e3/resource) (`422d14e5-61af-43df-9170-ca1a316110e3`)
- S24: [analysis of the mechanism of die soldering in aluminum die casting__39352dca37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99877613-dc9c-48be-809b-937c09073959/resource) (`99877613-dc9c-48be-809b-937c09073959`)
- S19: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7aceaae2-6736-4d2a-8324-b4978b26e451/resource) (`7aceaae2-6736-4d2a-8324-b4978b26e451`)
- S32: [图1.3 Fe3Al局部相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2bf8f38-fd4d-4f4c-b4b3-ef01253b06f0/resource) (`d2bf8f38-fd4d-4f4c-b4b3-ef01253b06f0`)