---
version: "v1"
generated_at: "2026-06-18T05:53:50+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 36
  source_quality_score: 0.83
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 1 概述

Mg‑Al 系合金是以镁为基体、铝为主要合金元素的轻金属材料体系，既包含变形镁合金也包含铸造镁合金分支，是镁合金中牌号最多、应用最广的系列[[S13,S38,S18]]。在压铸领域，绝大多数商用镁合金都属于该体系，其核心优势在于 Al 在镁中最大固溶度可达 12.7 wt%，固溶强化效果突出，且随 Al 含量提升合金铸造流动性同步提高，与高压压铸工艺适配性优异[[S18]]。

与其他主要镁合金系相比，Mg‑Zn 系依靠 Zn 固溶和时效强化，但二元 Mg‑Zn 合金固液区间大、晶粒粗大、铸造流动性差、热裂倾向高，常规压铸性能远低于 Mg‑Al 系[[S18,S14]]；Mg‑Mn 系则以耐蚀性和焊接性见长，整体强度偏低，主要用作板材、管材等变形材料，商用压铸牌号极少[[S39]]。因此，Mg‑Al 系在压铸镁合金中占据绝对主导地位。

按照是否引入钙元素进行改性，Mg‑Al 系可划分为**无钙标准 Mg‑Al 合金**和**含钙 Mg‑Al‑Ca 合金**两大子类。

**无钙标准 Mg‑Al 合金**根据核心的第三类主合金元素进一步细分为四个商用子系列[[S13,S21,S37]]：
- **AZ 系**（Mg‑Al‑Zn）：如 AZ91D，综合力学性能和铸造性能好，用量最大。
- **AM 系**（Mg‑Al‑Mn，指 AZ 系列之外的 Mg‑Al‑Mn 合金）：如 AM50A、AM60B，铝含量降低，塑性及韧性突出。
- **AS 系**（Mg‑Al‑Si）：如 AS41B，通过 Mg₂Si 相改善高温抗蠕变性能。
- **AE 系**（Mg‑Al‑RE）：如 AE44，依靠 Al₁₁RE₃ 等热稳定相获得更高的耐热性能。

**含钙 Mg‑Al‑Ca（AX）系**是在 Mg‑Al 合金基础上引入钙元素形成的重要改性分支[[S13,S37,S1]]。钙的加入显著提升抗氧化阻燃性能与耐腐蚀能力，抑制凝固过程中亚稳态 Mg₁₇Al₁₂ 相的析出，生成 Mg₂Ca、(Mg, Al)₂Ca 及 Al₂Ca 等热稳定金属间化合物，可进一步提高室温和高温力学性能[[S13,S1]]。该亚类还可衍生出 Mg‑Al‑Ca‑RE 等多元改性牌号[[S37]]。

![镁合金成形工艺分类及压铸Mg-Al系合金分支明细图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ac836bb-464b-4139-8e02-d954b3f6efe7/resource)

## 2 牌号与标准

Mg‑Al 系压铸镁合金的主流商用牌号在多个国家标准中均有明确规定。常见牌号包括 AZ91D、AM60B、AS41B、AE44 等，对应标准体系如 GB/T 13820、GB/T 25748、ASTM B94、EN 1754 等[[S4,S10,S5,S15]]。其中 AZ91D、AM60B、AS41B 被定义为高纯级耐蚀压铸牌号，标准中对其 Fe/Mn 元素最大比值作出了严格限定，以保障耐蚀性能[[S4]]。

含钙类牌号方面，既有早期开发的 AMCa602（含 2% Ca 的非燃烧镁合金），也有后来面向耐热应用的 MRI 153M、MRI 230D 以及新开发的高强韧牌号 AX73、AXT710 等[[S28,S26]]。表 1 整理了典型牌号与其所属子系列和化学成分特征。

| 牌号 | 子系列 | 主要化学成分特征（质量分数） | 备注 |
|------|--------|-------------------------------|------|
| AZ91D | AZ (Mg-Al-Zn) | Al 约 9%，Zn 约 0.7%，Mn 0.15%~0.5% | 高纯耐蚀牌号，最常用压铸合金 |
| AM60B | AM (Mg-Al-Mn) | Al 约 6%，Mn 0.24%~0.6% | 高纯耐蚀牌号，高伸长率 |
| AS41B | AS (Mg-Al-Si) | Al 约 4%，Si 约 1% | 高纯耐蚀牌号，改善高温性能 |
| AE44 | AE (Mg-Al-RE) | Al 4%，RE 4% | 商用综合性能最好的压铸耐热镁合金 |
| AMCa602 | AX (Mg-Al-Ca) | Al 6%，Ca 2% | 非燃烧镁合金 |
| MRI 230D | AX (Mg-Al-Ca-Sn-Sr) | Al 6.5%，Ca 2%，Sn 1%，Sr 0.3% | 耐热 Mg-Al-Ca 系合金 |
| AXT710 | AX (Mg-Al-Ca-Sn) | Al 7%，Ca 1%，Sn 0.2% | 抗拉强度 258 MPa，屈服 188 MPa，延伸率 10.2% |

## 3 化学成分

Mg‑Al 系压铸镁合金中 Al 元素的质量分数常规分布于 2%~10%[[S41,S21,S17,S13]]。各主要合金元素的作用与典型含量汇总于表 2。

| 元素 | 典型含量范围（wt%） | 在 Mg‑Al 系中的主要作用 |
|------|---------------------|--------------------------|
| Al | 2~10 | 主要合金化元素，固溶强化、提高流动性；超过 9% 合金变脆、冷裂倾向上升 |
| Zn | <2 | 提高强度与耐腐蚀性；含量过高增大热裂倾向 |
| Mn | 0.2~0.5 | 形成 Al‑Fe‑Mn 化合物减少杂质 Fe 的影响，提升耐蚀性 |
| Si | 0.3~0.6 | 生成高熔点 Mg₂Si 相改善高温抗蠕变性能 |
| RE | 3~5 | 生成 Al₁₁RE₃ 等热稳定相，提高耐热性与抗蠕变能力 |
| Ca | 1~3 | 抑制 Mg₁₇Al₁₂ 相析出，形成含钙耐热相，提升阻燃性、耐蚀性和高温力学性能 |

## 4 显微组织与相组成

### 4.1 无钙 Mg‑Al 合金的典型组织

无钙 Mg‑Al 压铸合金的凝固按照如下顺序进行：首先形成 α‑Mg 固溶体，随后在约 565 ℃ 析出 Mg₂Si 相，最终在约 186 ℃ 析出 β‑Mg₁₇Al₁₂ 相[[S29,S54]]。β‑Mg₁₇Al₁₂ 相的形貌与 Al 含量密切相关：Al 含量较低时呈碎块状，随 Al 含量升高逐渐转变为孤岛状，当 Al 含量达到 11 wt% 时可连接成连续网状；网状分布的粗大 Mg₁₇Al₁₂ 相会割裂基体，恶化合金力学性能[[S12]]。

Mg₂Si 相在无钙合金中以汉字状或多边形形态存在，微量 Si 杂质形成的多边形 Mg₂Si 颗粒可作为 Mg₁₇Al₁₂ 相的异质形核基底，促进 Mg₁₇Al₁₂ 相细化[[S29,S32]]。在 AM60 系列压铸合金中，Mg₁₇Al₁₂ 相的质量分数稳定在约 0.68%；添加微量 Ce 或 La 稀土后，会生成极少量 Al₁₁RE₃ 相（约 0.0001 wt%），同时进一步抑制 Mg₁₇Al₁₂ 相的析出[[S6]]。

![Mg-Al二元系铝量变化对充型能力、热裂倾向、缩松倾向的影响规律](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c55965a-bb2f-426c-a70e-7d8c05c63aea/resource)

### 4.2 含钙 Mg‑Al 合金的组织演变

向 Mg‑Al 系合金中添加 Ca 元素可有效抑制凝固过程中亚稳态 Mg₁₇Al₁₂ 相的析出，转而生成 Mg₂Ca、(Mg, Al)₂Ca 及 Al₂Ca 等高熔点含钙金属间化合物[[S13]]。这些化合物主要分布在晶界位置，对晶界起钉扎作用，高温下能有效阻碍晶界滑移与迁移，从而显著提升合金的高温蠕变抗力[[S48,S1]]。

Ca 元素的适量添加可以同时提升室温强度与高温性能，但存在明显的性能权衡：Ca 添加量超过适宜范围后，合金延伸率显著下降[[S13]]。过量 Ca 会形成粗大网状 Al₂Ca 相割裂基体，造成塑性劣化和过变质问题[[S13,S53]]。

## 5 力学性能

### 5.1 室温力学性能与蠕变抗力

无钙 Mg‑Al 压铸合金的室温拉伸性能统计范围大致为：屈服强度 110~140 MPa，抗拉强度 180~250 MPa，延伸率 6%~18%[[S30]]。在 150 ℃/50 MPa 条件下的 100 h 蠕变抗力由低到高的排列顺序为 AZ91D < AM60B < AS41 < AS21，规律表现为 Al 含量越低、共晶相体积分数越小，蠕变抗力越高[[S42,S27]]。

常规无钙 Mg‑Al 合金（如 AZ91 和 AM 系）因 β‑Mg₁₇Al₁₂ 相在 150 ℃ 以上软化，持久强度和蠕变性能大幅下降，使用温度通常不超过 120 ℃[[S3]]。

### 5.2 钙添加带来的性能变化

含钙 Mg‑Al 系合金通过晶界含钙金属间化合物的钉扎作用，使长期服役温度可达到 150 ℃[[S48,S1]]。新开发的 AXT710 合金室温抗拉强度可达 258 MPa、屈服强度 188 MPa、延伸率 10.2%[[S26]]；当 Ca 添加量控制在 0.5% 时，延伸率最高可达 18%[[S47]]。

然而，采用 Ca 完全替代 RE 元素制备的 AEX422 压铸合金虽然屈服强度提升至 204 MPa，但延伸率降至仅 4%，已不满足结构件韧性要求[[S26]]。这表明 Ca 添加必须在强度与塑性之间进行精细调控。

## 6 工艺性能

### 6.1 流动性与成形特性

无钙标准 Mg‑Al 压铸合金熔点低、凝固快，与铁的亲和力小，正常压铸条件下粘模倾向低，模具使用寿命可达铝合金的 4~5 倍，且铸件尺寸稳定性优异[[S7]]。

合金中适当提高 Al 含量可明显改善流动性并降低粘模倾向，但 Al 含量推荐控制在 9% 以下，超过 9% 后合金脆性上升、冷裂纹倾向增大[[S41]]。Zn 能改善流动性，但通常应限制在 1% 以下，否则会增大热裂倾向[[S41]]。Mg‑Al 二元系中 Al 含量对充型能力、热裂倾向和缩松倾向的影响规律可用实验曲线予以描述[[S23]]（见第 4 节配图）。

### 6.2 阻燃性与免热处理特性

无钙 Mg‑Al 合金中低熔点的 β‑Mg₁₇Al₁₂ 相（共晶温度仅 437 ℃）导致高温抗氧化性差，熔炼时易发生氧化燃烧[[S20,S52]]。向 Mg‑Al 系中添加 Ca 元素可显著改善这一状况：Ca 与氧亲和力高，通过外氧化和镁的内氧化作用在熔体表面形成致密的 MgO/CaO 复合氧化膜，有效阻碍高温氧化；Ca 质量分数达到 1% 以上时，燃点明显提高，在压铸过程中可大幅降低 SF₆ 等特殊保护气体的使用需求，显著提升生产安全性[[S20,S43]]。

与此同时，含钙 Mg‑Al 合金因生成热稳定含钙金属间化合物，可在无需后续热处理的条件下达到目标力学性能，满足免热处理要求，这对简化一体化大型压铸车身结构件的工艺流程、缩短生产周期具有重要意义[[S13,S47]]。

## 7 耐腐蚀性

对于无钙 Mg‑Al 压铸合金，耐腐蚀性主要通过严格控制杂质元素及 Fe/Mn 比值来保障。高纯级牌号如 AZ91D、AM60B、AS41B 都在相应标准中明确了 Fe 和 Mn 含量的上限以及二者之间的最大比值[[S4]]。

含钙 Mg‑Al 合金中，Ca 的引入可促使合金表面形成更为致密的氧化层，抑制腐蚀扩展。与传统合金相比，盐雾腐蚀速率可降低约 60%[[S53,S47]]。

## 8 应用领域

### 8.1 汽车轻量化零部件

汽车轻量化是 Mg‑Al 系压铸镁合金最主要的应用领域，历史上该领域消耗了 80%~90% 的镁合金压铸件[[S24]]。不同子系列面向不同工况需求：

- **AZ91D**：凭借优良的压铸性能和机械强度，在车用压铸镁合金中占比高达 80%，广泛用于电动工具机壳、普通薄壁结构件[[S16]]。
- **AM50/AM60**：塑性较 AZ91 提升约 15%，多用于汽车仪表盘支架、方向盘骨架等对韧性有要求的车内次受力件[[S47,S3]]。
- **AS41**：高温稳定性提升约 40%，用于 120 ℃ 以下工作的变速箱壳体、发动机支架等部件[[S47]]。
- **AE44**：添加稀土元素提升蠕变抗力，服役温度突破 150 ℃，可用于电池箱盖等动力系统周边耐热件，高温蠕变寿命较常规合金延长 3 倍[[S47,S3]]。
- **Mg‑Al‑Ca 系合金**：借助阻燃、耐蚀和高塑性优势，适用于对阻燃性能、高延伸率有要求的一体化大型压铸车身结构件，并可简化后续后处理工序约 30%[[S47,S26]]。

### 8.2 电子产品壳体

在消费电子领域，压铸 Mg‑Al 系合金的应用正在扩大。典型案例如 2026 年发布的小米笔记本 Pro 14，采用一体压铸成型镁合金机身，较传统铝合金减重 30% 以上，整机重量仅 1.08 kg；5G 基站散热壳体采用高导热 Mg‑Al 系压铸镁合金后，整机温度均匀性可提升 15%[[S47]]。

## 9 缺陷与局限

Mg‑Al 系压铸合金在使用中同样存在若干缺陷与限制。

**无钙合金的主要局限**：
- β‑Mg₁₇Al₁₂ 相以连续网状分布于晶界时，会显著降低合金的强度与延伸率，铸件中心区域易出现大尺寸缩孔[[S11,S30]]。
- 在时效热处理过程中存在非连续析出行为，会导致力学性能恶化，即明显的时效脆化倾向[[S13]]。
- 常规使用温度不超过 120 ℃，150 ℃ 以上 β‑Mg₁₇Al₁₂ 相软化，持久强度与蠕变性能大幅下降，不能满足高温长期服役要求[[S3]]。
- Al 含量超过 9% 时合金明显变脆，冷裂纹倾向增加[[S41]]。

**含钙 Mg‑Al‑Ca 合金的特有限制**：
- Ca 添加量超过合理范围时，延伸率急剧下降，粗大网状 Al₂Ca 相会割裂基体，严重降低塑性[[S13,S53]]。
- 存在过变质问题：Ca 添加超过合理变质阈值后，粗大的含钙金属间化合物大量析出，丧失细晶强化效果，合金综合力学性能恶化[[S26]]。
- 过量 Ca 还会增大热裂倾向和粘模缺陷的发生概率[[S26,S53]]。

## Sources
- S13: [22244039_Mg-Al系合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e1d0717-315a-4eb8-95c5-0f6d5c9599c5/resource) (`3e1d0717-315a-4eb8-95c5-0f6d5c9599c5`)
- S38: [机械工程材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6880a23-5f0f-46d6-bfd3-394e60f9a686/resource) (`a6880a23-5f0f-46d6-bfd3-394e60f9a686`)
- S18: [稀土成分对EA43合金组织、力学及导热性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58becad5-c581-4f96-a208-2a2b2e8db23b/resource) (`58becad5-c581-4f96-a208-2a2b2e8db23b`)
- S14: [22242925_Mg-Zn系合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44c3801d-42e4-442e-ba9a-d25c89b124e1/resource) (`44c3801d-42e4-442e-ba9a-d25c89b124e1`)
- S39: [advances in wrought magnesium alloys fundamentals of processing properties and applications__b1eb9cd50a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0d0342f-230a-4261-8b28-563e819d65d4/resource) (`b0d0342f-230a-4261-8b28-563e819d65d4`)
- S21: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/663c0e73-4391-4135-a495-a734c004d497/resource) (`663c0e73-4391-4135-a495-a734c004d497`)
- S37: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a603b0e2-9627-44ac-8947-de2922fca2eb/resource) (`a603b0e2-9627-44ac-8947-de2922fca2eb`)
- S1: [casting defects and mechanical properties of high pressure die cast mg z__3dc01b33c7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03bce57d-224b-4120-aadf-342af0e09a05/resource) (`03bce57d-224b-4120-aadf-342af0e09a05`)
- S4: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/153f0e53-f314-4073-9137-e774ca375546/resource) (`153f0e53-f314-4073-9137-e774ca375546`)
- S10: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2bb2cd84-ec09-451e-8924-15496febd703/resource) (`2bb2cd84-ec09-451e-8924-15496febd703`)
- S5: [先进材料及特种液态成型上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19346f1f-b7b3-4231-af10-5b69ca2e03ff/resource) (`19346f1f-b7b3-4231-af10-5b69ca2e03ff`)
- S15: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bd9c0d4-b942-47e2-a2f5-f223107775fb/resource) (`4bd9c0d4-b942-47e2-a2f5-f223107775fb`)
- S28: [0044_c29a032a8cc9db4b_镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79fe51a9-eb94-4461-9ae9-d78bf1eb3276/resource) (`79fe51a9-eb94-4461-9ae9-d78bf1eb3276`)
- S26: [镁合金一体化压铸缺陷控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70149ee3-bd50-46e6-a823-6f688e1cbcfd/resource) (`70149ee3-bd50-46e6-a823-6f688e1cbcfd`)
- S41: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c35d2442-94e9-47dd-96b5-9dc643870601/resource) (`c35d2442-94e9-47dd-96b5-9dc643870601`)
- S17: [金属材料液态成型实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/558f836e-6bcf-485f-ad8d-f162acd23a5c/resource) (`558f836e-6bcf-485f-ad8d-f162acd23a5c`)
- S29: [镁合金熔体氧化孕育细化行为及其机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8566720e-74be-48f4-bcb0-5e846f5ee6a1/resource) (`8566720e-74be-48f4-bcb0-5e846f5ee6a1`)
- S54: [镁合金熔体氧化孕育细化行为及其机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc2a9721-93ae-41a9-9fa3-e9af84855aac/resource) (`fc2a9721-93ae-41a9-9fa3-e9af84855aac`)
- S12: [Mg-Al-Si系合金凝固与时效组织演化及力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3513dddb-c141-4ba3-9d98-da0cf2670e3c/resource) (`3513dddb-c141-4ba3-9d98-da0cf2670e3c`)
- S32: [镁合金熔体氧化孕育细化行为及其机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91c50a44-bbb1-414e-8f10-cfd48b7b50e5/resource) (`91c50a44-bbb1-414e-8f10-cfd48b7b50e5`)
- S6: [Table 3. Mg17Al12 和 Al11RE3 相在 AM60 系合金中的含量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1eb7254b-b1fb-471a-bf85-142e6b0652d9/resource) (`1eb7254b-b1fb-471a-bf85-142e6b0652d9`)
- S48: [压铸耐热镁合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebbd0197-f18b-4029-8618-c43226d1695e/resource) (`ebbd0197-f18b-4029-8618-c43226d1695e`)
- S53: [挤压铸造镁合金研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9c5e6bc-046c-47c6-9129-372ff9188d44/resource) (`f9c5e6bc-046c-47c6-9129-372ff9188d44`)
- S30: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/907c900a-7984-42ce-817e-876204882e81/resource) (`907c900a-7984-42ce-817e-876204882e81`)
- S42: [design perspectives for creep resistant magnesium die casting alloys__2a57842716](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c6aad577-5aeb-4de1-87c6-430d187f6c0e/resource) (`c6aad577-5aeb-4de1-87c6-430d187f6c0e`)
- S27: [design perspectives for creep resistant magnesium die casting alloys__2a57842716](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/747f34c3-a56d-4ebb-9d44-23146ad1bea5/resource) (`747f34c3-a56d-4ebb-9d44-23146ad1bea5`)
- S3: [压铸耐热镁合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12543171-7ccc-45ac-80c6-9d93fd011ae5/resource) (`12543171-7ccc-45ac-80c6-9d93fd011ae5`)
- S47: [9067826_压铸镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e240cd80-41de-444b-8fba-61f65a8f1e7d/resource) (`e240cd80-41de-444b-8fba-61f65a8f1e7d`)
- S7: [金属液态成型模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fad29f8-73d1-400c-bcb7-c293e07a8ae7/resource) (`1fad29f8-73d1-400c-bcb7-c293e07a8ae7`)
- S23: [Mg-Al二元系铝量变化对合金铸造性能的影响曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c55965a-bb2f-426c-a70e-7d8c05c63aea/resource) (`6c55965a-bb2f-426c-a70e-7d8c05c63aea`)
- S20: [AZ91镁合金受控扩散凝固组织与反重力铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c25dbbf-d42d-495b-ba44-dbc37ec909ae/resource) (`5c25dbbf-d42d-495b-ba44-dbc37ec909ae`)
- S52: [AZ91镁合金受控扩散凝固组织与反重力铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f58fdbf4-c648-4a4e-9fa1-4698e4b34f7e/resource) (`f58fdbf4-c648-4a4e-9fa1-4698e4b34f7e`)
- S43: [镁合金高铁枕梁的结构设计及成型工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c72f7e59-c650-44d1-a71f-fd33f38eb6d8/resource) (`c72f7e59-c650-44d1-a71f-fd33f38eb6d8`)
- S24: [先进镁合金制备与加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ef0c630-b622-4b2b-a1c2-fd4450ff9156/resource) (`6ef0c630-b622-4b2b-a1c2-fd4450ff9156`)
- S16: [application of automobile lightweight alloys and the development of its__b2f5c2064a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50414bbf-c789-405a-88a1-d2fb62c73b01/resource) (`50414bbf-c789-405a-88a1-d2fb62c73b01`)
- S11: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ee12f65-19e1-4ee9-88aa-eb964567b887/resource) (`2ee12f65-19e1-4ee9-88aa-eb964567b887`)