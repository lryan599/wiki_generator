---
version: "v1"
generated_at: "2026-06-18T13:40:50+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 43
  source_quality_score: 0.87
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

锰（Mn）是铝基合金中重要的合金化元素之一，属于过渡金属。在压铸铝合金领域，Mn兼具常规杂质中和元素与免热处理合金核心微合金化组元的双重角色，在Al-Si系压铸合金中可同时实现固溶强化、细化晶粒、中和铁相有害作用及提升防粘模性能等多重效果 [[S5,S16]]。

锰在铝合金共晶温度658℃时，在α-Al固溶体中的最大溶解度为1.82 wt%，随温度降低溶解度显著下降，427℃时仅为0.2 wt% [[S20,S16,S23]]。这一固溶度特性决定了Mn在铝合金中既可通过溶入基体发挥固溶强化作用，又可形成弥散金属间化合物产生第二相强化效果。

## 核心作用机理

### 固溶强化与晶粒细化

Mn原子溶入α-Al基体后会引发铝晶格畸变，提升位错运动阻力，实现固溶强化效果；同时可析出弥散分布的MnAl₆金属间化合物，阻碍晶粒长大，起到细化晶粒的作用 [[S20,S1]]。需要指出的是，在常规铸造铝合金中，Mn单独添加的固溶强化贡献有限，但配合其他合金元素协同作用可显著提升合金高温性能、抗疲劳性能，并降低合金线收缩率 [[S16]]。

### Fe相变质作用

压铸Al-Si合金中，Fe通常以针状β-AlFeSi（Al₅FeSi/Al₉Fe₂Si₂）相存在，这种硬脆针状相严重割裂铝基体，显著降低合金塑性。Mn的核心作用之一是将该针状有害相转化为形貌更温和的汉字状、鱼骨状或球状的α-AlFeMnSi相，从而大幅降低铁相的脆性危害 [[S27,S53,S21]]。

研究表明，Mn添加到Al-Si合金中后，β-Al₅FeSi相倾向于被抑制，转而形成α-Al₁₅(Fe,Mn)₃Si₂相。在Al-Si-Fe-Mn四元合金中，Fe可替代该相中高达90%的Mn [[S21]]。

#### Mn/Fe质量比对铁相形貌的调控规律

锰铁质量比w(Mn)/w(Fe)是调控β-Fe相向α相转变的核心参数。不同Mn/Fe比条件下的铁相形貌演变规律如下表所示 [[S27,S9]]：

| w(Mn)/w(Fe) | 铁相形貌特征 |
|:---:|:---|
| 0.5 | 铁相仍主要以针状形态存在，仅出现极少量汉字状铁相 |
| 0.8 | 汉字状铁相数量有所增加，但仍有大量针状铁相存在 |
| 1.1 | 汉字状铁相明显增多且广泛分布，针状铁相数量显著减少、尺寸细化 |
| 1.4 | 汉字状铁相占绝大多数，针状铁相长度明显变短，几乎全部针状β-Fe相消失 |
| 特殊配比 | 针状铁相全部消失，转变为球状多面体α-(Fe,Mn)₃Si₂Al₁₅相 |

另有研究发现，当Mn/Fe质量比为1.2左右时，合金中全部针状β-Al₅FeSi相可完全转化为汉字状α-Al₁₃(Fe,Mn)₄Si₂相，此时合金的抗拉强度与延展性达到峰值 [[S6]]。

### 抑制压铸粘模（Die Soldering）

压铸过程中，铝合金与钢质模具的高亲和力会引发界面剧烈物化反应，生成一系列Fe-Al-Si金属间化合物，最终导致铝合金粘附在中间层上引发粘模缺陷 [[S51,S13]]。

Mn在压铸铝合金中可减少合金对钢模具的熔蚀与粘附作用，有效降低粘模倾向 [[S19,S12,S8,S18,S52]]。其作用机制主要体现在两方面：

1. **改变富铁相形貌，减少界面反应**：随Mn含量提升，原本针状的硬脆β-Al₅FeSi相向汉字状/骨骼状的细密α-Al₁₃(Fe,Mn)₄Si₂相转变，减少Fe原子向铝合金熔体中的溶解扩散，抑制界面金属间化合物层的过量生成 [[S12,S8,S33,S35,S6,S37]]。

2. **降低合金对钢模的润湿性**：Mn与Fe、Si元素交互作用时，可生成AlMn₂Si、Al₆Mn相，熔体中的Fe原子可部分固溶于该类含Mn相中，降低游离的Al₃Fe、Al₉Fe₅Si₂等针状有害相的占比，大幅降低铝合金对钢模的润湿性与粘附功 [[S33]]。

![铝合金电机壳体脱模受力分析示意图，标注了动模脱模拉力、倒拉、拉裂及无倒拉区域正常包紧力等特征，用以辅助说明粘模引发的脱模受力异常与铸件拉裂失效形式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5cc46dff-71d0-4449-b1fb-3139d352bcec/resource)

## 与其他元素的交互作用

### 与Cu的协同作用

Mn元素可协同优化Al-Si-Cu系压铸合金的组织，促进Cu相关强化相的细化，使θ-Al₂Cu、Q-Al₅Cu₂Mg₈Si₆等析出相分布更均匀，实现Mn与Cu的协同强化效果 [[S35,S6,S37]]。同时，Mn不会对Mg元素形成的Mg₂Si强化相的正常析出产生明显负面干扰 [[S35,S6,S37]]。

### 与Fe、Si的竞争关系

Fe是Al-Si合金中的主要杂质元素，其危害性与Si含量密切相关。Mn作为Fe的中和元素，在熔体中优先与Fe、Si结合形成α-AlFeMnSi相。通常推荐Mn添加量不超过合金中Fe含量的1/2 [[S33,S16]]。当合金中Mn+Fe总含量超过0.8 wt%且Si含量≥8 wt%时，在610~660℃温度区间内会析出粗大的角状初生Al₁₅(Fe,Mn)₃Si₂硬质点（俗称泥渣相sludge），显著降低合金的切削加工性能和铸态致密性 [[S53,S16,S44]]。

## 典型用量范围

### 普通商用压铸铝合金

在ADC12、A380等常规压铸铝合金中，Mn主要作为Fe的中和元素使用，控制上限为0.5 wt%，典型含量约为0.2 wt%，一般要求Mn添加量不超过合金中Fe含量的1/2 [[S12,S29,S16]]。压铸铝合金中Mn的质量分数一般宜控制在≤0.7%，常规工业生产场景下推荐Mn含量不超过0.5% [[S19,S12,S8,S18,S52]]。

### 免热处理一体化压铸铝合金

商用免热处理一体化压铸铝合金中的Mn含量显著高于普通牌号，典型范围为0.4 wt%~0.8 wt%，例如美铝C611合金中Mn控制在0.4%~0.8%，常规AlSi10MnMg类免热处理压铸合金中Mn控制在0.3 wt%~0.7 wt% [[S10,S32]]。

不同应用场景下Mn含量与作用对比：

| 合金类型 | Mn典型含量（wt%） | 主要用途 | 作用特点 |
|:---|:---:|:---|:---|
| 普通压铸合金（ADC12/A380）| ~0.2，≤0.5 | 一般功能件 | 部分中和Fe的有害作用 [[S12,S29,S16]] |
| 免热处理合金（C611）| 0.4–0.8 | 大型一体化压铸件 | 防粘模、保塑性、Fe相变质 [[S10]] |
| AlSi10MnMg类 | 0.3–0.7 | 汽车结构件 | Fe相变质、防粘模、保塑性 [[S32]] |
| Silafont-36 | 0.4–0.65 | 汽车安全结构件 | 低Fe高Mn，Mn/Fe比0.6~0.8 [[S38,S34]] |

Mn含量在0.4%以下时，除改善富铁相形貌外，还可提升压铸铝合金的塑性；但Mn含量过高则会引发元素偏析，同时生成Al₆Mn相降低合金机加工性能 [[S12,S8,S52]]。

## 相关合金体系与应用

### Silafont-36（AlSi9Mg系）

德国Rheinfelden公司开发的Silafont-36属于低Fe高Mn的AlSi9Mg免热处理压铸铝合金。Mn的核心作用是将杂质Fe元素转化为汉字状α-Al₁₅(Fe,Mn)₃Si₂相，抑制针状β-Al₅FeSi相生成。当Mn含量控制在0.4%~0.65%、Mn/Fe比值为0.6~0.8时，2~3 mm壁厚试样的延伸率可达10%以上，性能显著优于普通压铸铝合金 [[S38,S34]]。

### Magsimal-59（AlMg5Si2Mn系）

Magsimal-59为Rheinfelden公司开发的AlMg5Si2Mn型高强韧免热处理压铸铝合金，Mn作为核心合金元素添加，可改善合金抗热裂性能、耐蚀性能和焊接性能。薄壁铸件（<2 mm）下铸态抗拉强度可达300 MPa以上，延伸率10%~15%，主要面向汽车安全结构件场景使用 [[S38,S30,S2]]。

### Aural系列（Al-Si-Mg-Mn系）

麦格纳（原加拿大铝业）开发的Aural系列免热处理压铸铝合金属于Al-Si-Mg-Mn系，Mn的添加策略是调控富Fe相形貌，降低杂质Fe的负面影响，同时抑制压铸过程粘模，面向汽车车身框架结构件应用场景。铸态下延伸率不低于11% [[S34,S36]]。

### XA铝合金（Al-Si-Zn-Mg-Cu系）

> **关于"XA铝合金"的说明**：XA铝合金是国内高校研发的免固溶处理Al-Si-Zn-Mg-Cu系压铸铝合金，仅需进行时效处理即可获得目标强度，不需要经过传统固溶+淬火工序，属于免固溶处理压铸铝合金范畴 [[S54,S11,S15]]。**用户描述提示中"XA铝合金"的提法与此一致**，但需注意该合金并非已纳入国际或国家标准体系的商业化牌号，目前主要处于研究阶段。

XA铝合金的公开成分中，Mn作为重要调控元素添加，配套使用Al-10Mn中间合金完成熔炼配制。合金中存在AlSi(Mn,Cr)Fe相调控来改善组织性能 [[S54,S11,S15]]。研究表明，加入的Zn固溶进AlSi(Mn,Cr)Fe相中，使得AlSi(Mn,Cr)Fe以择优生长方式形成针状，影响了Mn将针状铁相转变为汉字状的效果 [[S15]]。

## 标准与规范

### 国际标准体系

**EN 1706:2020**为欧洲现行压铸铝合金核心标准，由CEN/TC 132铝和铝合金技术委员会牵头制定，定义了压铸铝合金的化学成分限值及单铸试棒力学性能要求，可与EN 1676、EN 576等配套标准协同使用 [[S3,S39]]。

**JIS H5302:2000**为日本现行铝合金压铸件标准，共收录14个压铸铝合金牌号，明确规定各牌号包含Mn在内的全元素含量范围要求，配套的JIS H2118对应压铸用铝合金锭的成分规范 [[S4,S50]]。

### 中国标准体系

中国现行压铸铝合金核心标准**GB/T 15115-2024**对应配套的**GB/T 15114-2023**铝合金压铸件规范，覆盖压铸铝合金从成分控制、力学性能到质量检验的全流程要求，是国内压铸铝合金生产验收的官方依据 [[S3,S41]]。

### 标准中Mn元素的管控方式

在多数普通牌号压铸铝合金标准中，Mn元素作为杂质限定项管控，部分合金明确规定Mn+Cr总占比不超过0.8 wt% [[S49]]。随着免热处理一体化压铸铝合金的发展，Mn已从单纯的杂质管控项转变为关键微合金化组元，其含量范围和管控策略也相应调整。

## 典型缺陷与防控

### 硬质点缺陷

当Mn元素含量过高或控制不当出现偏析时，会与Fe、Si等元素结合形成高硬度的金属间化合物，在铸件中形成硬质点缺陷。这类硬质点会导致刀具磨损加剧、机加工后表面出现明暗不均的斑点，直接引发抛光不良缺陷 [[S14,S43]]。压铸件中的硬质点主要包括氧化物（Al₂O₃等）、非金属混合物、以及Al-Si-Fe系和Al-Si-Mn系金属间化合物 [[S14,S26]]。

### 加工脆性

Mn元素过量偏聚形成的脆性金属间化合物会割裂铝基体，降低合金的延伸率与冲击韧性，引发铸件加工脆性缺陷，导致铸件在受外力作用时易发生无预兆断裂 [[S40,S42]]。

### 防控措施

Mn元素引发的偏析类缺陷，可通过以下方式有效防控 [[S26]]：
- 提高熔炼温度，避免金属间化合物未完全溶解
- 降低合金液保温时长
- 严格控制Mn元素添加比例，不超出工艺窗口
- 熔炼时使用Al-Mn中间合金而非直接加入纯Mn
- 对铝合金液进行高温处理，使高熔点的金属间化合物充分溶解

## Sources
- S5: [铝合金减震塔压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10989aed-8f07-493d-a9c2-40ee2039e6e2/resource) (`10989aed-8f07-493d-a9c2-40ee2039e6e2`)
- S16: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45e2cbc6-a07f-4e15-9c17-37d0509b6a80/resource) (`45e2cbc6-a07f-4e15-9c17-37d0509b6a80`)
- S20: [22251614_Al-Mn合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5641c1cf-77b8-4879-86a4-a02bc9ec4a82/resource) (`5641c1cf-77b8-4879-86a4-a02bc9ec4a82`)
- S23: [有色金属熔炼入门与精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6111d6db-0f87-4cc8-a3b1-aca3ce2521c3/resource) (`6111d6db-0f87-4cc8-a3b1-aca3ce2521c3`)
- S1: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0055175e-2484-4adf-b9e8-3ccff4b504e2/resource) (`0055175e-2484-4adf-b9e8-3ccff4b504e2`)
- S27: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ee75788-569b-4804-ac74-097e2a72b3aa/resource) (`6ee75788-569b-4804-ac74-097e2a72b3aa`)
- S53: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f53928b6-29b1-4aba-b622-322a83c184b8/resource) (`f53928b6-29b1-4aba-b622-322a83c184b8`)
- S21: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59a7de32-aa74-46c7-a2d0-91caf0fdf7b3/resource) (`59a7de32-aa74-46c7-a2d0-91caf0fdf7b3`)
- S9: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28037419-6746-4dbf-af54-9b429642db33/resource) (`28037419-6746-4dbf-af54-9b429642db33`)
- S6: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/193a2dd9-1365-4680-8c80-c964a0c3033d/resource) (`193a2dd9-1365-4680-8c80-c964a0c3033d`)
- S51: [die soldering effect of process parameters and alloy characteristics on__f5bc200f9a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e7a7f979-c119-431a-88f5-54289ad2ba7b/resource) (`e7a7f979-c119-431a-88f5-54289ad2ba7b`)
- S13: [analysis of the mechanism of die soldering in aluminum die casting__39352dca37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/422d14e5-61af-43df-9170-ca1a316110e3/resource) (`422d14e5-61af-43df-9170-ca1a316110e3`)
- S19: [真空压铸铝合金发动机缸体缺陷与热处理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/534b2f1e-685d-40c9-84a5-fe113870339c/resource) (`534b2f1e-685d-40c9-84a5-fe113870339c`)
- S12: [金属压铸工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37479e07-4bba-4215-a4ab-0b69816942cb/resource) (`37479e07-4bba-4215-a4ab-0b69816942cb`)
- S8: [压铸技术基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26dc81d0-987d-49ea-a169-fc6bb5118477/resource) (`26dc81d0-987d-49ea-a169-fc6bb5118477`)
- S18: [压铸技术基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5156262a-1631-45b1-98c3-8398b7d1bdf5/resource) (`5156262a-1631-45b1-98c3-8398b7d1bdf5`)
- S52: [压铸技术基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3d1b587-b760-4725-af10-a90887baee15/resource) (`f3d1b587-b760-4725-af10-a90887baee15`)
- S33: [有色金属熔炼工工艺学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81900657-3a08-494f-a0f7-fa0a67fed284/resource) (`81900657-3a08-494f-a0f7-fa0a67fed284`)
- S35: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82a3ce7a-1524-472a-99b8-fd15ac119383/resource) (`82a3ce7a-1524-472a-99b8-fd15ac119383`)
- S37: [Cu含量和热处理工艺对Al-Si-Mg-Mn-xCu铸造铝合金显微组织和力学性能的影响（英文）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8dc95733-ddf6-4a57-ba38-343dac553554/resource) (`8dc95733-ddf6-4a57-ba38-343dac553554`)
- S44: [金属压铸模设计技巧与实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5725f7b-0ca1-459c-b91d-b7bb2a41f9d4/resource) (`b5725f7b-0ca1-459c-b91d-b7bb2a41f9d4`)
- S29: [effects of die temperature of sss die casting on the microstructure and__d27a8b10b6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75a97bcc-de43-4a17-ab9a-4b13197ddfd3/resource) (`75a97bcc-de43-4a17-ab9a-4b13197ddfd3`)
- S10: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e8a5e3c-e794-452e-a49e-e5ef09bd5223/resource) (`2e8a5e3c-e794-452e-a49e-e5ef09bd5223`)
- S32: [一体化压铸免热处理铝合金研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80a1da1d-888e-4927-b8a1-90fcfd66a408/resource) (`80a1da1d-888e-4927-b8a1-90fcfd66a408`)
- S38: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f2d83aa-b1de-4301-acd1-3fa2a6cba5ef/resource) (`8f2d83aa-b1de-4301-acd1-3fa2a6cba5ef`)
- S34: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82013eee-6b17-4059-9384-bca4ce09589a/resource) (`82013eee-6b17-4059-9384-bca4ce09589a`)
- S30: [压铸工艺与模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c84a791-4785-4a51-a08c-e8bfaaad7408/resource) (`7c84a791-4785-4a51-a08c-e8bfaaad7408`)
- S2: [automotive alloys 1999__dbd41f2733](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04dc2fd3-c2e8-4536-a41e-4cce7fb3891e/resource) (`04dc2fd3-c2e8-4536-a41e-4cce7fb3891e`)
- S36: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cce15c9-13d6-4bc3-a83e-75c736157c17/resource) (`8cce15c9-13d6-4bc3-a83e-75c736157c17`)
- S54: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa110dec-959a-459a-ae24-76ef8835aa89/resource) (`fa110dec-959a-459a-ae24-76ef8835aa89`)
- S11: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/322c5213-a46b-43d8-baa5-9551435fa819/resource) (`322c5213-a46b-43d8-baa5-9551435fa819`)
- S15: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42f6098a-3b27-4274-80e7-51940176b636/resource) (`42f6098a-3b27-4274-80e7-51940176b636`)
- S3: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/072272e1-f319-400f-9748-5a402ac4bb2a/resource) (`072272e1-f319-400f-9748-5a402ac4bb2a`)
- S39: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c31a640-f143-4c34-903f-cbc5961ad1a7/resource) (`9c31a640-f143-4c34-903f-cbc5961ad1a7`)
- S4: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0920bb20-7334-419e-9ebd-ab126087c11e/resource) (`0920bb20-7334-419e-9ebd-ab126087c11e`)
- S50: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e42a0f72-0ab5-4ca7-bc1e-68024d6fdd49/resource) (`e42a0f72-0ab5-4ca7-bc1e-68024d6fdd49`)
- S41: [GBT+15114（铝合金压铸件）-2023.pdf-d582e150-e18c-4269-a253-356e28a756ba](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5a24c02-67d2-4346-ac6f-11fdf6ea24fb/resource) (`a5a24c02-67d2-4346-ac6f-11fdf6ea24fb`)
- S49: [中外铝合金牌号对照速查手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db61e019-15db-4934-b895-09b217a1d86c/resource) (`db61e019-15db-4934-b895-09b217a1d86c`)
- S14: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4258d76b-e64c-4036-a39e-c3d38afb4456/resource) (`4258d76b-e64c-4036-a39e-c3d38afb4456`)
- S43: [5613234_压铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b568a4a2-2de4-4a61-a58b-cb2bf813f3ed/resource) (`b568a4a2-2de4-4a61-a58b-cb2bf813f3ed`)
- S26: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ae221fc-b2fd-4911-a815-4ede47294a55/resource) (`6ae221fc-b2fd-4911-a815-4ede47294a55`)
- S40: [铝合金压铸产品铸造缺陷产生原因及处理办法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a17baafa-48f7-4969-8d64-95a139a176d3/resource) (`a17baafa-48f7-4969-8d64-95a139a176d3`)
- S42: [铝及铝合金加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/adc7f35a-673d-49b9-b791-fb8d03ba1e3c/resource) (`adc7f35a-673d-49b9-b791-fb8d03ba1e3c`)