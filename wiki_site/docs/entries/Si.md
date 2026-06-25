---
version: "v1"
generated_at: "2026-06-18T09:09:36+00:00"
confidence_score: 0.84
confidence_level: "high"
confidence_basis:
  cited_sources: 60
  source_quality_score: 0.85
  freshness_score: 0.76
  evidence_coverage_score: 1.0
---

## 定义与分类

硅（Si）是压铸铝硅合金的核心合金元素。铝硅合金是指以铝为基体、硅为最主要合金元素的铸造合金，其硅含量范围通常为3%~25%[[S68,S8,S71]]。硅的添加可显著提升合金流动性、降低热裂倾向、减小线收缩率，是大规模商用铝合金压铸工艺的核心基础元素[[S68,S8,S71]]。

按硅含量可将铝硅合金划分为三类[[S68,S33,S51]]：

- **亚共晶铝硅合金**：硅质量分数低于共晶点（约12.6%Si），凝固组织由初生α-Al相和共晶硅相构成。
- **共晶铝硅合金**：硅质量分数接近12%~12.6%，凝固组织由α-Al相和共晶硅相组成。
- **过共晶铝硅合金**：硅质量分数大于共晶点，凝固组织包含初生硅相、共晶α-Al相和共晶硅相。

Al-Si为典型的简单共晶体系，共晶温度为577°C，共晶点硅质量分数为12.6%。硅在577°C时在铝中的最大固溶度为1.65%（质量分数），室温下溶解度降至0.05%以下，不会形成任何二元金属间化合物[[S26,S48]]。

![Al-Si合金结晶示意图，展示亚共晶、共晶、过共晶区域的温度与凝固速率关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87bb827f-51a8-40ba-9c75-4dcf8877d94c/resource)

## 工艺作用

### 流动性

硅对合金流动性的提升来自两方面机制：一是硅含量升高会窄化亚共晶合金的凝固温度区间；二是硅的熔化潜热约为同体积铝的4.5倍，可降低熔体黏度[[S63,S29,S65]]。二元Al-Si合金的流动性在硅含量5~6wt%区间为低值区，7~18wt%范围内整体具备优异流动性[[S46,S42]]。值得注意的是，工业实测表明流动性峰值出现在18wt%Si处而非共晶点[[S46]]。凝固区间与流动性的关系存在明显的工艺差异：常规常压自由流动条件下，流动性随凝固区间扩大而降低；而在高压压铸强制充型条件下，流动性随凝固区间扩大整体呈上升趋势[[S66]]。

### 热裂倾向

铝硅合金的热裂倾向随硅含量升高持续降低。当硅含量接近共晶成分时，合金凝固温度区间极窄，热裂倾向几乎完全消失，在所有商用压铸铝合金中抗热裂性能最优[[S63,S29,S12,S18]]。

### 凝固收缩

随硅含量增加，合金线收缩率和体积收缩率同步降低。体积收缩率随硅含量升高呈线性下降，理论上硅含量达到25wt%时合金凝固体积收缩为零，完全消除收缩缺陷倾向[[S63,S65,S12]]。

### 脱模性能

压铸铝合金中硅含量低于0.6wt%时，合金与钢铁模具亲和力强，粘模倾向严重；硅含量超过0.6wt%后，粘模倾向大幅降低，脱模性能显著提升[[S70]]。

![不同硅含量下压铸铝合金铸造性能变化曲线，包含温度、流动性、线收缩、体收缩、热裂倾向和气密性指标](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82002201-fbe1-41e5-b4b8-acd324b06bfd/resource)

## 分类与压铸适应性

不同硅含量类别的铝硅合金在压铸中表现出不同的工艺适应性[[S31,S9,S13]]：

| 分类 | 硅含量范围 | 压铸工艺特性 | 典型应用场景 |
|------|------------|-------------|-------------|
| 亚共晶合金 | Si < 12% | 充型性能良好，适配绝大多数常规薄壁复杂压铸件 | 通用压铸结构件 |
| 共晶/近共晶合金 | Si 11%~13% | 流动性最优，充型能力最强，可制备极薄壁厚件，热裂倾向最低 | 薄壁复杂件、精密铸件 |
| 过共晶合金 | Si > 13%（典型16%~19%） | 热膨胀系数极低，耐磨性优异，但初生硅相导致刀具磨损，需变质处理 | 活塞等耐高温高耐磨件 |

## 典型合金牌号与硅含量

主流商用压铸铝硅合金牌号的硅含量普遍高于6%，验证了工业领域常规硅含量较高的行业特征[[S24,S59,S13,S62,S34]]。各牌号标准硅含量如下：

| 标准体系 | 牌号 | 硅含量范围（wt%） | 合金系 | 分类 |
|----------|------|-------------------|--------|------|
| JIS H5302 | ADC12 | 9.6~12.0 | Al-Si-Cu | 亚共晶至近共晶[[S24,S15,S28,S3]] |
| JIS H5302 | ADC10 | 7.5~9.5 | Al-Si-Cu | 亚共晶[[S59,S3]] |
| ASTM B85 | A380 | 7.5~9.5 | Al-Si-Cu | 亚共晶，通用型[[S13,S58,S11]] |
| ASTM B85 | A383 | 9.5~12.5 | Al-Si-Cu | 亚共晶至近共晶，适配复杂薄壁件[[S15,S58]] |
| ISO 3522 | AlSi9Cu3 | 8.0~11.0 | Al-Si-Cu | 亚共晶[[S59,S50]] |
| BS | LM24 | 7.5~9.5 | Al-Si-Cu | 对应A380[[S62,S25,S6]] |
| GB/T 15115 | YL104（YZAlSi10） | 8.0~10.5 | Al-Si | 对应ADC10[[S59,S34]] |

## 力学性能

随硅含量提升，合金的抗拉强度和硬度同步升高，而伸长率（塑性）持续下降。典型压铸态性能对比如下[[S70,S37,S41,S2]]：

| 合金 | Si含量（wt%） | 抗拉强度（MPa） | 伸长率（%） | 布氏硬度（HB） |
|------|-------------|---------------|------------|---------------|
| AlSi7Mg（压铸态） | ~7 | 170 | 2.5 | 55 |
| AlSi10Mg(Fe)（压铸态） | ~10 | 240 | 1 | 70 |
| AlSi17Cu4Mg(A390)（压铸态） | ~17 | 200 | <1 | 110 |

### 高硅脆化机理

高硅压铸铝合金塑性下降、脆性上升的微观机制如下：硅为硬脆相，随硅含量升高，合金中粗大初晶硅占比提升，初晶硅优先在应力集中位置成为裂纹萌生点并发生解理断裂；高占比的硅相割裂铝基体，硅颗粒相互搭接，变形过程中产生严重不协调引发大量裂纹；铝基体的塑性变形特征随硅含量升高被逐步弱化，合金整体从韧性断裂向完全脆性断裂转变[[S22,S14,S60]]。

## 免热处理压铸铝合金中的硅

### Silafont-36（AlSi9Mg）

德国莱茵铝业开发的Silafont-36免热处理压铸铝硅合金，硅含量设计为9.5%~11.5%的亚共晶区间。通过将铁含量严格控制在0.15%以下、优化Mn/Fe比以形成汉字状α-Al₁₅(Fe,Mn)₃Si₂相，并搭配Sr变质处理细化共晶硅，该合金无需后续热处理即可在铸态下获得高强度与高延伸率，流动性优异，适配车身薄壁结构件压铸[[S47,S44,S53]]。

### Magsimal-59（AlMg5Si2Mn）

与Silafont-36形成对比，Magsimal-59免热处理压铸铝合金采用约2%的低硅设计，硅元素以少量共晶相形式存在。铸态下抗拉强度可达300MPa，断后延伸率15%~17%，具备优异的韧性和焊接性能，适配汽车安全相关结构件压铸[[S47,S39,S16]]。

## 变质处理

### 钠变质

钠是共晶硅的高效变质剂，以钠盐或纯金属形式加入，熔体中钠质量分数通常控制在0.01%~0.02%。钠变质可将粗大针片状共晶硅转化为珊瑚状或纤维状，使铸造Al-Si合金的室温伸长率从未变质的2%~3%提升至6%~10%，抗拉强度同步提升[[S27,S69]]。但钠变质有效时间仅为30~60分钟，高温下失效更快，重熔后变质效果完全消失[[S4,S38,S32,S21]]。钠变质过程中易与水汽反应生成氢气，升高合金含气量，导致压铸件出现皮下针孔和夹渣缺陷；高镁合金中过量钠还会引发钠脆问题，且NaF有毒[[S67,S38]]。

### 锶变质

锶作为长效变质剂，通常以Al-5%Sr或Al-10%Sr中间合金形式加入，推荐添加质量分数为0.04%~0.08%，在710°C保温条件下有效变质时间可达6~12小时，重熔后仍可保留变质效果，对坩埚无浸蚀作用[[S4,S69,S54,S10]]。但锶会大幅提高铝合金熔体吸氢倾向，增加最终铸件的针孔度，在敞开式大气熔炼环境中若不配套除气工艺极易造成气孔超标[[S67,S69,S10]]。

### 压铸条件下的特殊性

压铸工艺冷却速度远高于砂型铸造，本身即可细化部分共晶硅。若对硅含量7%以下的合金额外进行变质处理，会升高合金熔体黏度，降低充型能力，同时增加针孔生成倾向，因此多数薄壁压铸件无需专门进行变质处理[[S4,S32]]。

## 与其他元素的交互作用

### 铜

压铸Al-Si合金中铜含量在0.8%以下时可提升合金强度、硬度与弹性极限；铜含量超过0.8%后会析出硬脆的θ-Al₂Cu相，降低合金塑性与耐蚀性，同时增大热裂倾向[[S17,S30,S12]]。

### 镁

添加0.2%~0.3%的镁可生成Mg₂Si强化相，在不明显降低塑性的前提下提升合金整体强度。镁含量过高会增大合金熔体氧化倾向，同时使凝固收缩量变大，更容易产生热裂与缩松缺陷[[S12,S7]]。

### 铁与锰

铁在压铸铝合金中易形成针状硬脆的β-AlFeSi相，大幅降低合金塑性与冲击韧性。锰元素可将针状富铁相转化为汉字状/球状的Al-Fe-Si-Mn相，消除铁相的割裂作用，减少缩松倾向；同时合金中铁含量控制在0.7%~0.9%区间可显著缓解铝合金对压铸模具的粘模倾向[[S12,S49,S7,S64]]。

## 局限与工程注意事项

### 机加工刀具磨损

硅含量超过13%的过共晶压铸铝合金中存在大量高硬度初生硅硬质相，普通未涂层硬质合金刀具的磨损速率远高于亚共晶合金，加工后工件表面光洁度差。行业推荐采用聚晶金刚石（PCD）刀具或金刚石涂层刀具进行切削加工[[S36,S52,S9]]。此外，未溶初晶硅颗粒及Fe/Mn偏析形成的金属间化合物硬质点也会加剧刀具磨损，导致加工表面出现亮度异常斑点[[S61]]。

### 焊接性能

常规压铸生产的高硅压铸件内部残留大量气孔与氧化夹渣，在熔焊过程中内部气体受热膨胀，容易沿焊缝向外溢出形成"发泡"缺陷，导致焊接接头强度不合格。仅经过特殊高致密化压铸工艺制备的高硅铝合金铸件才可实现稳定焊接[[S1]]。

### 塑性不足

高硅铝合金的塑性随硅含量升高而逐渐降低，主要归因于粗大初晶硅的应力集中效应和基体割裂作用[[S22,S14]]，使其不适用于对延展性要求较高的结构件场景。

## Sources
- S68: [GBT+5611（铸造术语）-2017.pdf-dd5ce1f8-c5b9-4d94-87e7-fc40cbfe0347](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4aa6473-0eb1-43f7-aec4-1de50d6dbd31/resource) (`f4aa6473-0eb1-43f7-aec4-1de50d6dbd31`)
- S8: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1676cda4-8182-4faf-88d8-c70645585bf0/resource) (`1676cda4-8182-4faf-88d8-c70645585bf0`)
- S71: [aluminum and aluminum alloys introduction and overview__ca28de7c4d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc89dfec-c7f6-40b3-87f0-7baf4a4d7abe/resource) (`fc89dfec-c7f6-40b3-87f0-7baf4a4d7abe`)
- S33: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65aa0475-7435-40f4-ada2-945ac5143fda/resource) (`65aa0475-7435-40f4-ada2-945ac5143fda`)
- S51: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a17bfeeb-5bf5-41bd-a79e-d20066b46a17/resource) (`a17bfeeb-5bf5-41bd-a79e-d20066b46a17`)
- S26: [binary alloy phase diagrams__4d8db6f6f7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/574ba4e7-c35f-421b-a86a-6f0717631b67/resource) (`574ba4e7-c35f-421b-a86a-6f0717631b67`)
- S48: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91abf338-dbc0-4792-a7cb-a9139a29e725/resource) (`91abf338-dbc0-4792-a7cb-a9139a29e725`)
- S63: [金属压铸工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4af45c6-d284-4fef-aa4a-23e1aa0ce93e/resource) (`d4af45c6-d284-4fef-aa4a-23e1aa0ce93e`)
- S29: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c336558-b411-491c-a3a1-f2a085d33544/resource) (`5c336558-b411-491c-a3a1-f2a085d33544`)
- S65: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea79ab82-cb6a-4ff5-a6b7-65fc6aecf78b/resource) (`ea79ab82-cb6a-4ff5-a6b7-65fc6aecf78b`)
- S46: [aluminium cast house technology theory practice__d10cf55c8c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c3f7e59-d597-4212-97d9-4660e2e13a8d/resource) (`8c3f7e59-d597-4212-97d9-4660e2e13a8d`)
- S42: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8133575e-ab69-4ad3-b5cb-a378ad55b130/resource) (`8133575e-ab69-4ad3-b5cb-a378ad55b130`)
- S66: [图1.11 流动性与合金凝固区间大小的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ee36ab00-5494-4895-9f4b-325cfceaa74d/resource) (`ee36ab00-5494-4895-9f4b-325cfceaa74d`)
- S12: [金属压铸模设计技巧与实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22f48744-dd53-4cbb-be01-eae48e663dec/resource) (`22f48744-dd53-4cbb-be01-eae48e663dec`)
- S18: [9797399_铝硅合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/459bfcfa-4ab0-4fa3-b83e-f7248c229a2d/resource) (`459bfcfa-4ab0-4fa3-b83e-f7248c229a2d`)
- S70: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc43b8fb-6115-4327-9504-781b29b0099f/resource) (`fc43b8fb-6115-4327-9504-781b29b0099f`)
- S31: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61c008f8-1895-43db-90c0-165b4bec5a47/resource) (`61c008f8-1895-43db-90c0-165b4bec5a47`)
- S9: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d49f927-e71e-4b03-a64e-f6005f2ec5cf/resource) (`1d49f927-e71e-4b03-a64e-f6005f2ec5cf`)
- S13: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23d65afd-66a9-43d8-8a8a-6469fcd2d3e6/resource) (`23d65afd-66a9-43d8-8a8a-6469fcd2d3e6`)
- S24: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S59: [2960711_ADC10](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4fe8dc6-3cfd-4110-8283-38c2cc092914/resource) (`b4fe8dc6-3cfd-4110-8283-38c2cc092914`)
- S62: [压铸用铝合金LM2、LM24及A380.0的化学成分含量表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccbb8d6c-33d6-435c-9147-a4168c0602dc/resource) (`ccbb8d6c-33d6-435c-9147-a4168c0602dc`)
- S34: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bf0f644-14ad-4bac-8898-80fb92285ee7/resource) (`6bf0f644-14ad-4bac-8898-80fb92285ee7`)
- S15: [铝合金压铸件不良品对策问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/331cf3d4-e17f-477b-8857-1e5d72fc9be5/resource) (`331cf3d4-e17f-477b-8857-1e5d72fc9be5`)
- S28: [表2-1 ADC12合金具体成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58600a9e-9e29-4bdd-be4e-77f5d6369639/resource) (`58600a9e-9e29-4bdd-be4e-77f5d6369639`)
- S3: [压铸用铝合金（JIS H5302-1976）种类与化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ee060ab-a2c3-40b1-812e-a78bc8f1536b/resource) (`0ee060ab-a2c3-40b1-812e-a78bc8f1536b`)
- S58: [ANSI/AA Al-Si-Cu 合金工艺性能和使用性能对照表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4618ac3-7622-45d2-adbe-e2086641d83f/resource) (`b4618ac3-7622-45d2-adbe-e2086641d83f`)
- S11: [H13与A380材料的化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22372649-efcc-4d22-98ac-213979cc6b4c/resource) (`22372649-efcc-4d22-98ac-213979cc6b4c`)
- S50: [0230_23bb365dd533025d_AlSi10Mg](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9872230c-c0fb-416b-92ae-142614a7c746/resource) (`9872230c-c0fb-416b-92ae-142614a7c746`)
- S25: [铝硅铜合金各国规格及成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/54309d27-3ac2-4eab-b976-18425d373376/resource) (`54309d27-3ac2-4eab-b976-18425d373376`)
- S6: [Zinc and aluminium alloy solidification phase diagram for die casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15ff800e-4aa9-4179-ba92-313d5b364fcb/resource) (`15ff800e-4aa9-4179-ba92-313d5b364fcb`)
- S37: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b589232-953f-4f25-9cd9-43a77e38bc68/resource) (`7b589232-953f-4f25-9cd9-43a77e38bc68`)
- S41: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f625288-8ea9-452c-af81-5d66e012053a/resource) (`7f625288-8ea9-452c-af81-5d66e012053a`)
- S2: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b17d0ae-1955-462d-9a0b-1a7df6562332/resource) (`0b17d0ae-1955-462d-9a0b-1a7df6562332`)
- S22: [粉末冶金法制备AlMgSix高硅铝合金工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e86aae5-0454-45c1-b0ad-c6e65cf70d55/resource) (`4e86aae5-0454-45c1-b0ad-c6e65cf70d55`)
- S14: [快速凝固铝硅合金电子封装材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28f3eed3-7725-4147-a4cd-e28d0e6c26c6/resource) (`28f3eed3-7725-4147-a4cd-e28d0e6c26c6`)
- S60: [effects of cu content on the microstructure mechanical property and hot__90e549550b](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b87a455b-b765-42c9-998f-32bb18b7c998/resource) (`b87a455b-b765-42c9-998f-32bb18b7c998`)
- S47: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f2d83aa-b1de-4301-acd1-3fa2a6cba5ef/resource) (`8f2d83aa-b1de-4301-acd1-3fa2a6cba5ef`)
- S44: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82013eee-6b17-4059-9384-bca4ce09589a/resource) (`82013eee-6b17-4059-9384-bca4ce09589a`)
- S53: [乘用车白车身铝合金压铸结构件及材料应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6775f77-b490-47a4-aa81-d41afa62c1cc/resource) (`a6775f77-b490-47a4-aa81-d41afa62c1cc`)
- S39: [压铸工艺与模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c84a791-4785-4a51-a08c-e8bfaaad7408/resource) (`7c84a791-4785-4a51-a08c-e8bfaaad7408`)
- S16: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39d012df-15d6-44a2-b46f-a0fdb58209d1/resource) (`39d012df-15d6-44a2-b46f-a0fdb58209d1`)
- S27: [工程材料及加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57a88766-3bec-4388-8a17-43cdad1836eb/resource) (`57a88766-3bec-4388-8a17-43cdad1836eb`)
- S69: [有色金属熔炼入门与精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fac6fcae-11a7-48ff-bcc2-9a258da04311/resource) (`fac6fcae-11a7-48ff-bcc2-9a258da04311`)
- S4: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0fdd653c-5f4f-42d6-9244-2fb7ced5c0a3/resource) (`0fdd653c-5f4f-42d6-9244-2fb7ced5c0a3`)
- S38: [铝及铝合金加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8585ca-cdc6-422a-9020-cffe488367d8/resource) (`7b8585ca-cdc6-422a-9020-cffe488367d8`)
- S32: [铝合金熔炼理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6216e751-2a1c-4716-86aa-b1c9fd6cab3b/resource) (`6216e751-2a1c-4716-86aa-b1c9fd6cab3b`)
- S21: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d5ee5bd-14b9-4539-a471-0dabf88771a8/resource) (`4d5ee5bd-14b9-4539-a471-0dabf88771a8`)
- S67: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f03f75df-dd74-499c-b0d4-8fa241c37bc2/resource) (`f03f75df-dd74-499c-b0d4-8fa241c37bc2`)
- S54: [轻有色金属及其合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8b2cc18-a441-4367-a713-1513182ff77e/resource) (`a8b2cc18-a441-4367-a713-1513182ff77e`)
- S10: [castings principles the new metallurgy of cast metals__9ac1d4f9a8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e47f8c0-0cd4-4c75-9ddc-be7c16d2d866/resource) (`1e47f8c0-0cd4-4c75-9ddc-be7c16d2d866`)
- S17: [压铸模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d0213f2-a834-47c4-99e7-9a13798a23c8/resource) (`3d0213f2-a834-47c4-99e7-9a13798a23c8`)
- S30: [压铸技术基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ce88c5c-3f45-4fcd-9cca-69660bf78efe/resource) (`5ce88c5c-3f45-4fcd-9cca-69660bf78efe`)
- S7: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1631db39-2a75-47bd-a4b9-95f28929046c/resource) (`1631db39-2a75-47bd-a4b9-95f28929046c`)
- S49: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96c653e0-ccfe-4266-8bf9-870deeb6c07d/resource) (`96c653e0-ccfe-4266-8bf9-870deeb6c07d`)
- S64: [压力铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4e4c9f3-9017-48af-96ae-c4cabc3410f1/resource) (`d4e4c9f3-9017-48af-96ae-c4cabc3410f1`)
- S36: [9797399_铝硅合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ad2b4ec-72a5-4d97-8ede-2988045900fc/resource) (`7ad2b4ec-72a5-4d97-8ede-2988045900fc`)
- S52: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a597aeae-89e9-4966-844a-f481257dbb8a/resource) (`a597aeae-89e9-4966-844a-f481257dbb8a`)
- S61: [full](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc1e913d-f5f4-4f23-bb43-81943abe0f70/resource) (`bc1e913d-f5f4-4f23-bb43-81943abe0f70`)
- S1: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0598b3f5-5539-4c48-82d8-811674f8a40b/resource) (`0598b3f5-5539-4c48-82d8-811674f8a40b`)