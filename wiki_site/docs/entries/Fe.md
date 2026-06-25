---
version: "v1"
generated_at: "2026-06-18T08:36:55+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 41
  source_quality_score: 0.86
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

铁（Fe）在压铸铝合金，尤其是免热处理Al-Si系压铸合金中，被定义为一种不可避免的杂质元素，而非有意添加的合金化元素[[S2,S4]]。其在固态铝中的最大平衡固溶度极低（共晶温度下仅为0.03%~0.05%，平衡态不超过0.05%），几乎全部以第二相（金属间化合物）形式析出[[S4,S31]]。

然而，铁在压铸工艺语境下具有特殊的“双刃剑”效应：适量的铁对于抑制铝合金熔体与钢质模具、压射冲头的粘模（焊合）倾向、提升压铸脱模性至关重要，但含量超标时会形成硬脆的富铁相，严重恶化合金的塑性、加工性能和耐蚀性[[S2,S33,S45,S48]]。

## 工艺作用与机理

### 抑制粘模（焊合）
在压铸过程中，高温铝液与钢质模具及压射冲头直接接触。若铁含量不足，模具表面的铁元素会因浓度梯度快速向铝液扩散，生成铁-铝或铁-铝-硅金属间化合物，导致铸件粘附在模具上[[S28,S11]]。

- 当铁质量分数低于0.6%时，铝合金对模具的粘附倾向极强，粘模现象尤为严重[[S16,S33]]。
- 当铁含量提升至0.6%以上时，铝液与模具钢的界面反应受到抑制，粘模现象大幅缓解[[S1,S15,S28]]。
- 常规压铸场景下，铁的适宜控制范围为0.7%~1.2%，进一步优化脱模效果可将铁含量控制在0.8%~1.0%区间[[S30,S48,S28]]。

### 抗热裂倾向
适量的铁可提升压铸铝合金的抗热裂能力[[S26]]。但若铁含量过高导致粗大针状β-Fe相先析出，这些先结晶相会阻塞液态金属的补缩通道，增加热节位置的缩孔、缩松缺陷概率，间接提升热裂倾向[[S28,S37,S31]]。

## 分类与识别

在Al-Si系免热处理压铸铝合金中，富铁相主要以α-Fe相和β-Fe相两种类型存在[[S28,S40]]。

| 相类型 | 化学式 | 典型形貌 | 晶系 | 危害程度 |
|--------|--------|----------|------|----------|
| α-Fe相 | Al₈Fe₂Si 或 Al₁₅(Fe,Mn)₃Si₂ | 汉字状、块状、骨架状 | 六方晶系 | 较低 |
| β-Fe相 | Al₅FeSi 或 Al₉Fe₂Si₂ | 针状、薄片状 | 单斜晶系 | 最高 |

β-Fe相是对合金力学性能危害最显著的富铁金属间化合物，其针状形貌割裂铝基体连续性，成为应力集中点和裂纹萌生源[[S31,S28,S18,S17,S46]]。

## 来源与引入途径

铁杂质在免热处理压铸铝合金生产过程中的不可避免引入来源可分为三类[[S2,S23,S11,S47]]：

1. **炉料端**：低品位原生铝锭、回收再生铝、成分未严格管控的回炉料本身自带铁杂质，且随回炉料循环使用次数增加，合金中铁含量会逐步累积抬升[[S11,S47]]。

2. **熔炼装备端**：铁制坩埚、铁质熔炼工具在与铝液接触时发生溶解渗入。若铝液在铁质容器中长期保温，铁元素的渗透速度会显著加快[[S2,S23,S47]]。

3. **压铸工序端**：长期与高温铝液接触的钢质压射冲头、成型模具表面的铁元素会逐步扩散进入合金熔体。大型一体化压铸机的大吨位、高流速工况加剧了这一增铁效应[[S2,S11]]。

## 成分限量与合金牌号

### 常规压铸铝合金铁含量规范

压铸工艺的高速、高压、快速凝固特性显著弱化了铁元素的有害影响，使其铁含量允许上限远高于砂型铸造（≤0.6%）、金属型重力铸造（≤1.0%）等慢冷工艺[[S8,S37,S39]]。

| 合金牌号 | 对应标准 | 铁含量上限（max%） | 工业实际控制范围 |
|----------|----------|-------------------|------------------|
| ADC12（YL113） | JIS H5302-2006 | ≤1.3% | ≤0.9%，纯铝配制时约0.6% [[S15,S3,S43]] |
| A380 | ASTM B85（铸件A380.0） | ≤1.3% | 铸锭级A380.1更严格 [[S41,S22]] |
| AlSi9Cu3 | EN 1706 | ≤1.0% | 实际多处于0.8%~1.0% [[S19,S27]] |
| EN AC-43400（AlSi10Mg(Fe)） | EN标准铸造合金 | ≤1.0% | — [[S19]] |

### 免热处理高强韧压铸铝合金铁含量控制

早期的免热处理压铸铝合金（如Silafont-36、Castasil-37）将铁含量严格控制在≤0.15%，目的是避免生成针状β-AlFeSi脆性相，确保合金的高延伸率[[S24,S20]]。

![免热处理压铸铝合金早期标准规定的铁元素最大含量标注（0.15% max）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e918a88-91e8-42de-ba4d-4cdd8061457d/resource)

为降低对高纯原生铝原料的依赖、适配再生铝合金资源化利用的产业需求，在添加足量Mn元素将针状富铁相球化为低危害的Al₁₂Mn₃Si₂等球状相的基础上，免热处理压铸铝合金的铁允许上限可从原有的0.15%放宽至0.25%[[S14,S19]]。**该放宽范围仅适用于低合金化Al-Si-Mn系免热处理牌号，不适用于传统高硅高铜类普通压铸铝合金。**

上海交通大学开发的免热处理压铸铝合金明确限定铁元素最高质量分数≤0.1%，对应锰元素含量区间为0.4%~2.0%，可作为高要求免热处理结构件的铁、锰元素管控参考[[S36]]。

## 对合金性能与缺陷的影响

### 力学性能
随铁含量升高，免热处理压铸铝合金的延伸率、冲击韧性等塑性指标显著下降，抗拉强度小幅上升后基本保持稳定[[S48,S16,S46]]。硬脆针状β-Fe相作为应力集中点易成为裂纹萌生位置，直接割裂铝基体的连续性[[S46,S16]]。

在无Mn、Cr添加的B95铝合金中，铁含量从0提升至1.5%时，抗拉强度基本保持稳定，但断面收缩率和伸长率持续降低[[S49]]。

### 切削加工性能
铁含量过高时形成的大量高硬度富铁相硬点会直接磨损刀具，大幅缩短刀具寿命。研究表明，将A380合金铁含量从1.4%降至0.7%可使刀具寿命显著提高[[S45,S26,S44]]。

### 耐腐蚀性能
β-Fe相的电极电位显著高于α-Al基体，二者存在较大电位差形成微电偶对，加速局部电化学腐蚀。大量分布的β-Fe相还会破坏铝合金表面致密氧化膜的连续性，含铁量过高的铝硅合金甚至无法满足表面阳极氧化处理的要求[[S2,S37]]。

### 热裂与缩松
过量析出的粗大针状β-Fe相作为先结晶相直接阻塞液态金属的补缩通道，增大热节位置的缩孔、缩松缺陷概率，间接提升合金的热裂倾向[[S28,S37,S31]]。

## 工艺应对措施

### Mn/Fe比调控
当铁含量超出允许上限时，工业上最常用的中和调控方法是添加锰元素改变铁相形态。锰可将原本粗大片状/针状的脆性β-Fe相转化为汉字状、块状的α-Fe相（Al₁₅(Fe,Mn)₃Si₂），显著削弱有害作用[[S2,S21,S30,S6]]。

| Mn/Fe质量比 | 效果 |
|-------------|------|
| ≥0.5 | 常规控制下限，出现少量汉字状铁相 [[S21,S6]] |
| 0.67~0.83 | 经典最优区间，生成块状AlSiMnFe相 [[S2,S8,S10]] |
| ≥1.1 | 汉字状铁相占比显著升高，针状β-Fe大量减少 [[S21]] |
| ≥3.0 | 新一代大型一体化压铸铝合金方案，兼具高抗粘模能力 [[S7]] |

需注意：Mn总含量超过0.7%时可能生成新的脆性金属间化合物，反而降低合金综合力学性能[[S38]]。

### 联合元素调控
除锰外，还可添加Cr、Co、Mo等元素协同中和过量铁的有害作用[[S2,S34]]。压铸行业给出的铁、锰、铬联合控制经验公式为[[S35]]：

**(w(Fe) + 1.5 × w(Mn) + 2 × w(Cr)) ≤ 1.85**

该公式可避免合金中过量铁、锰、铬组合生成大量高密度的硬质点沉渣而影响铸件切削加工性能。

### 沉渣法
铁含量超标的铝液可在610~660℃温度区间保温静置，使添加锰、铬等元素后生成的高比重复合含铁相（沉渣）充分沉降到坩埚底部。生产浇注过程禁用坩埚底部的铝液，可直接降低浇注熔体中的实际铁含量[[S23,S34,S45]]。

### 废料处置
当合金中铁元素质量分数超过2.0%后，铁相危害完全不可通过常规元素调控消除，对应回炉料必须降级作为低要求非受力件的压铸原料，不得混入高性能免热处理铝合金批次[[S2]]。

## 微观组织图示

针状β-Fe相是危害性最高的富铁相形态，其形貌在免热处理Al-Si系合金中具有典型特征。

![免热处理Al-Si系合金针状β-Fe相典型金相组织，标尺50μm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/969285fc-c48c-448a-962e-feee41791852/resource)

经Mn元素调控后，有害的针状β-Fe相可转化为危害较低的汉字状α-Fe相。

![免热处理Al-Si系合金汉字状α-Fe相典型金相组织，标尺50μm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3730bedf-edd1-4878-bcd8-dd2ac88df930/resource)

## 相关标准体系

### 中国标准
中国现行压铸铝合金标准以GB/T 15115—2024《压铸铝合金》为核心，配套GB/T 15114—2023《铝合金压铸件》及GB/T 8733—2016《铸造铝合金锭》，共同构成技术框架，覆盖Al-Si系、Al-Si-Mg系、Al-Si-Cu系及Al-Mg系等主要合金系列，其中对免热处理牌号的铁限值区分不同强度等级要求设置[[S43]]。

### 国际标准对照
主要对标标准体系包括ISO 3522、ASTM B85/B108、EN 1706及JIS H5302等，共同构成全球压铸铝合金标准体系[[S43,S41]]。各类标准对铁含量的允许上限因合金系列和铸造工艺不同而异，压铸工艺普遍允许更高的铁含量。

## Sources
- S2: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06731c2f-0d22-4a2f-9d1b-5af683a087a4/resource) (`06731c2f-0d22-4a2f-9d1b-5af683a087a4`)
- S4: [effect of iron on the microstructure and mechanical properties of al die__89e9bcdcad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1593c10c-6346-45bc-9979-d046a0339291/resource) (`1593c10c-6346-45bc-9979-d046a0339291`)
- S31: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c6c4c57-f5ee-4aed-8767-aad3dcaab9a3/resource) (`8c6c4c57-f5ee-4aed-8767-aad3dcaab9a3`)
- S33: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96c653e0-ccfe-4266-8bf9-870deeb6c07d/resource) (`96c653e0-ccfe-4266-8bf9-870deeb6c07d`)
- S45: [die casting metallurgy aluminium alloy die castings__6142c8982e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e71daef0-6516-4cba-a106-75f2da5b6865/resource) (`e71daef0-6516-4cba-a106-75f2da5b6865`)
- S48: [铝合金压铸件不良品对策问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/edd199b0-7f41-44e9-a55e-53ffac990572/resource) (`edd199b0-7f41-44e9-a55e-53ffac990572`)
- S28: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/878ebc6a-9d77-4114-af0e-248bf5edb82a/resource) (`878ebc6a-9d77-4114-af0e-248bf5edb82a`)
- S11: [die cast engineering a hydraulic thermal and mechanical process__e5dfda1a8e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a48277f-f365-490a-8af2-3239515af4a7/resource) (`4a48277f-f365-490a-8af2-3239515af4a7`)
- S16: [压铸技术基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ce88c5c-3f45-4fcd-9cca-69660bf78efe/resource) (`5ce88c5c-3f45-4fcd-9cca-69660bf78efe`)
- S1: [die casting metallurgy__8f9e04f2f0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02594943-246c-4b24-8522-76bf9ec10e4d/resource) (`02594943-246c-4b24-8522-76bf9ec10e4d`)
- S15: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S30: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c3b2fa8-620c-4cb6-8c3f-1c85471f2001/resource) (`8c3b2fa8-620c-4cb6-8c3f-1c85471f2001`)
- S26: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8133575e-ab69-4ad3-b5cb-a378ad55b130/resource) (`8133575e-ab69-4ad3-b5cb-a378ad55b130`)
- S37: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd6e34cc-c2b2-47aa-a0e9-342101d9c6d1/resource) (`bd6e34cc-c2b2-47aa-a0e9-342101d9c6d1`)
- S40: [表1-2 铝合金中主要富铁相及其晶体学特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9fc6144-7af8-4402-88ce-87de7258df53/resource) (`c9fc6144-7af8-4402-88ce-87de7258df53`)
- S18: [casting and solidification of light alloys__06e9012dec](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ca29442-e997-4c9f-9ca1-44295f4ea3a2/resource) (`6ca29442-e997-4c9f-9ca1-44295f4ea3a2`)
- S17: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/669ffbdc-d323-4553-aeab-6b3c9b0863eb/resource) (`669ffbdc-d323-4553-aeab-6b3c9b0863eb`)
- S46: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebe19588-6613-42f0-9465-0731eb1934a4/resource) (`ebe19588-6613-42f0-9465-0731eb1934a4`)
- S23: [有色金属熔炼工工艺学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7d480a9b-89e0-4d0e-ad9c-1428c522f775/resource) (`7d480a9b-89e0-4d0e-ad9c-1428c522f775`)
- S47: [铝与铝合金材料生产技术500问](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/edbc290e-df08-4bdc-ba21-4864c8f8bdaf/resource) (`edbc290e-df08-4bdc-ba21-4864c8f8bdaf`)
- S8: [有色金属熔炼工工艺学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28096384-881f-4e8c-b689-89336c6197ee/resource) (`28096384-881f-4e8c-b689-89336c6197ee`)
- S39: [铝及镁合金铸锭最大铁含量限制表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c08afbbe-3503-4d1e-a5cf-bd0c265a6aec/resource) (`c08afbbe-3503-4d1e-a5cf-bd0c265a6aec`)
- S3: [压铸用铝合金（JIS H5302-1976）种类与化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ee060ab-a2c3-40b1-812e-a78bc8f1536b/resource) (`0ee060ab-a2c3-40b1-812e-a78bc8f1536b`)
- S43: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce2d13e-413c-4061-9d2d-8e1edc9e49c7/resource) (`dce2d13e-413c-4061-9d2d-8e1edc9e49c7`)
- S41: [die casting metallurgy__322fa9dd3c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cde8fbba-c836-4618-b7bf-faae50bb9c1f/resource) (`cde8fbba-c836-4618-b7bf-faae50bb9c1f`)
- S22: [die casting metallurgy aluminium alloy die castings__6142c8982e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76843354-65be-48c6-9952-0ae476ee4a9f/resource) (`76843354-65be-48c6-9952-0ae476ee4a9f`)
- S19: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e29b31c-b0d3-4dfc-8470-25f90c2c1759/resource) (`6e29b31c-b0d3-4dfc-8470-25f90c2c1759`)
- S27: [研究中所用铝合金的化学成分分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8439577b-ca47-428e-b29b-3eeb305571bf/resource) (`8439577b-ca47-428e-b29b-3eeb305571bf`)
- S24: [新能源汽车用铸造铝合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e5ecda4-6519-45f7-8a09-005c0e2bc33a/resource) (`7e5ecda4-6519-45f7-8a09-005c0e2bc33a`)
- S20: [铝合金中铁元素含量标注（0.15% max）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e918a88-91e8-42de-ba4d-4cdd8061457d/resource) (`6e918a88-91e8-42de-ba4d-4cdd8061457d`)
- S14: [免热处理铝合金大型结构件一体压铸研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50566832-293a-474c-9549-499da62cab58/resource) (`50566832-293a-474c-9549-499da62cab58`)
- S36: [表1-5 上海交通大学开发的免热处理合金成分（wt.%）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb4c9f8a-a5ae-456e-978c-d5cc397c221f/resource) (`bb4c9f8a-a5ae-456e-978c-d5cc397c221f`)
- S49: [铁对不含锰和铬的B95合金挤压棒材性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbc4bc4f-297f-4a06-9631-bc325284f699/resource) (`fbc4bc4f-297f-4a06-9631-bc325284f699`)
- S44: [压铸冶金学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df41d41a-8769-4985-845e-8baf044790f8/resource) (`df41d41a-8769-4985-845e-8baf044790f8`)
- S21: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ee75788-569b-4804-ac74-097e2a72b3aa/resource) (`6ee75788-569b-4804-ac74-097e2a72b3aa`)
- S6: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/216c1631-0033-4344-ab76-f708ee2a6076/resource) (`216c1631-0033-4344-ab76-f708ee2a6076`)
- S10: [金属压铸工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37479e07-4bba-4215-a4ab-0b69816942cb/resource) (`37479e07-4bba-4215-a4ab-0b69816942cb`)
- S7: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2617b3fb-b636-4458-9d6e-0f47e2795799/resource) (`2617b3fb-b636-4458-9d6e-0f47e2795799`)
- S38: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0336a4b-7d51-4bc7-899e-913cb70f35ce/resource) (`c0336a4b-7d51-4bc7-899e-913cb70f35ce`)
- S34: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/983d94a0-3e20-44af-9712-8c9075b368e0/resource) (`983d94a0-3e20-44af-9712-8c9075b368e0`)
- S35: [压铸手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/baf8f1bb-eaf2-470f-9300-ed6334e19eb6/resource) (`baf8f1bb-eaf2-470f-9300-ed6334e19eb6`)