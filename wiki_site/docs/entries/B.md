---
version: "v1"
generated_at: "2026-06-18T09:06:48+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 30
  source_quality_score: 0.86
  freshness_score: 0.76
  evidence_coverage_score: 1.0
---

## 概述

硼（Boron，元素符号B）是元素周期表IIIA族非金属元素，原子量为10.81[[S19]]。在免热处理压铸铝合金体系中，硼属于对材料塑性存在负面影响的非金属杂质元素，必须对其含量进行严格管控[[S19]]。然而，硼在铝合金中的角色具有典型的双面性：当通过Al-Ti-B中间合金以适量引入时，可作为晶粒细化剂的关键组元实现细晶强化效果；当含量超标时则成为有害杂质，劣化合金的延伸率、冲击韧性及疲劳性能[[S19,S5]]。这一双重属性要求对免热处理压铸铝合金中硼的来源、存在形式、损害机理及控制标准有系统的认识。

## 来源与引入途径

压铸铝合金熔体中硼的引入渠道包含五类主要路径[[S38,S17,S23,S13,S30]]：

1. **原生铝锭带入**：电解铝制备过程中，以含硼化物形式进入电解质的硼，有不超过60%转入铝熔体，构成痕量硼的本底来源[[S3]]。
2. **回炉料累积**：循环使用的压铸回炉料经反复重熔，导致硼元素逐步累积。
3. **晶粒细化剂引入**：添加商用Al-Ti-B系晶粒细化剂时伴随引入硼。常规Al-5Ti-1B中间合金硼含量约为1.03 wt.%，工业常用细化剂的Ti与B典型质量比为5:1[[S38,S5]]。
4. **精炼剂副产物**：使用含硼酸（H₃BO₃）、氟硼酸钠（Na₃BF₆）等成分的精炼剂进行除气除渣处理时，反应生成AlB₂、TiB₂等硼化物进入铝熔体[[S17]]。
5. **设备涂层剥落**：压铸设备流道、模具所用的BN（氮化硼）耐高温涂层在高温服役过程中磨损剥落，进入铝液[[S30,S13]]。

## 存在形式与微观组织

### 主要硼化物相

免热处理压铸铝合金中硼主要以硼化物形式存在，核心相包括AlB₂和TiB₂[[S17,S18,S37,S32]]：

- **AlB₂**：六方C32型晶体结构，晶格参数a=3.009 Å，c=3.262 Å，c/a=1.084。形貌为六角形或矩形板状，显微观测下呈暗灰色或褐灰色[[S18,S17]]。
- **TiB₂**：铝熔体晶粒细化的核心非均质形核相，形貌为规则六角形颗粒。工业铝熔体中硼化物整体浓度为0.1~100 ppm[[S37]]。

此外，AlB₂和TiB₂属等形貌结构，二者之间可形成固溶体(Al,Ti)B₂ [[S15]]。

### 分布特征与偏聚行为

铝熔体中的TiB₂硼化物存在显著的非均匀分布与晶界偏聚行为[[S37]]。在合金凝固过程中，受凝固前沿的推动作用，大量TiB₂团簇优先在晶界位置富集析出；部分硼化物团簇残留在晶粒内部。含量过高时，硼化物极易聚集形成大尺寸团簇，大尺寸的硼化物聚集体会成为加工缺陷源，降低刀具使用寿命，劣化合金的延伸率等力学性能[[S37,S28]]。

### 固溶度特征

硼在纯铝中固溶度极低，仅为约0.00x%量级；Al-B二元共晶点出现在0.022 wt%（即220 ppm）硼含量处，低于该值时硼主要以固溶形式存在于铝基体中[[S36]]。

![图10.2-33 铝合金分类图，展示硼含量与温度坐标下变形铝合金与铸造铝合金的分类边界，可呈现免热处理非强化合金与热处理强化合金的划分逻辑](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d88497ea-5df4-4875-9ebc-2b951eec35da/resource)

## 对塑性的损害机理

当免热处理压铸铝合金中的硼杂质含量超过铝基体固溶极限后，会沿晶界析出硬脆的AlB₂等硼化物相[[S16]]。这些脆性硼化物直接作为裂纹萌生核心，弱化晶界结合力，诱导沿晶或穿晶脆性断裂，最终导致合金延伸率、冲击韧性、疲劳性能出现明显劣化[[S16]]。

硼对塑性的损害具有明确的含量阈值特性。当铝合金中硼的质量分数超过0.1%后，粗大的TiB₂或AlB₂硼化物硬质点大量聚集形成有害夹杂物，显著恶化合金的延性与塑性；硼质量分数超过0.2%后，铝晶粒会重新出现粗大化现象，熔体形成铸造夹杂物的风险大幅升高[[S28]]。金属硼化物在机加工时降低工具的寿命，粗颗粒形态的由有害的夹杂物组成，对机械性能和延性产生不良的影响[[S28]]。

## 含量控制标准与容许限量

### 国际标准中的通用规定

国内GB/T 15115系列、美国ASTM B85、欧洲EN 1706、日本JIS H5302四大主流压铸铝合金标准中，ADC12、A380、AlSi9Cu3等常规牌号未对硼设置单独强制限量，统一纳入“其余单个杂质元素质量分数≤0.05%”的通用管控条款[[S10,S25]]。

### 新能源免热处理专用牌号的严控标准

面向新能源一体化压铸的免热处理专用牌号（如AlSi10MnMg、Silafont-36），相关衍生行业规范将硼的限量进一步收紧至质量分数≤0.03%[[S9]]。高延伸率结构件专用牌号（如C611、AlSi10MnMg、Castasil-37）对硼杂质敏感度极高，规定其允许硼杂质上限需控制在50 ppm（0.005 wt%）以下，微量硼超标即对其铸态12%以上的延伸率指标造成明显损害[[S21]]。

### 不同合金牌号的硼敏感度与阈值差异

| 合金牌号/类型 | 硼敏感度 | 允许硼杂质上限 | 说明 |
|---|---|---|---|
| C611、AlSi10MnMg、Castasil-37等结构件专用牌号 | 极高 | ≤50 ppm（0.005 wt%） | 微量超标即损害大于12%的铸态延伸率[[S21]] |
| ADC12、A380等普通牌号 | 较低 | 100~150 ppm | 固有延伸率仅1%~3%，硼超标后塑性下降相对幅度更小[[S21,S10]] |
| 新能源免热处理专用牌号 | 高 | ≤0.03%（300 ppm） | 避免高硼损害免热处理状态下的高延伸率[[S9]] |
| 常规添加Al-Ti-B细化剂的Al-Si系合金 | 中等 | 100~150 ppm（安全阈值） | 超过该范围粗大硼化物致塑性断崖式下降[[S22]] |
| 不含Ti的高纯无Ti免热处理Al-Si合金 | 更高 | 50~80 ppm（安全阈值） | 对硼耐受能力更低[[S15]] |

### 企业内控标准差异

头部压铸铝合金企业的内控标准存在明显差异[[S38,S20]]：传统通用压铸生产企业延续主流标准的0.05%通用单杂质硼上限要求；新能源领域专用免热处理铝合金材料生产企业将硼的内控限量收紧至0.015%~0.03%；部分头部厂要求最终成品合金硼质量分数不超过Al-Ti-B细化剂正常带入的0.02%[[S38,S20]]。

## 与有益作用的辩证关系

### 作为晶粒细化剂的正面作用

硼在铝合金中实现晶粒细化的常规有效添加质量分数区间为0.005%~0.1%，工业常用Al-Ti-B晶粒细化剂的Ti与B典型质量比为5:1[[S5]]。细化所需的最低添加量为0.01%，添加量为0.04%时细化效果达到峰值，添加量为0.05%~0.10%时可获得完全细化的等轴晶组织[[S27]]。

硼与钛在铝熔体中反应生成高熔点稳定相TiB₂，TiB₂可作为异质形核核心细化铝晶粒[[S34]]。含钛的铝熔体中当含3×10⁻⁶（3 ppm）的硼时，仅0.8%（质量分数）的TiAl₃粒子起细化作用；而加入1×10⁻⁴（100 ppm）的硼后，有2.4%（质量分数）的TiAl₃粒子起细化作用，细化效率增加3倍[[S15]]。

### 从有益到有害的转折点

硼添加量在0.005%~0.01%低区间时，生成的细小弥散硼化物可辅助晶粒细化、提升合金塑性；仅当硼含量超过临界值，形成大尺寸粗颗粒硼化物夹杂物时，才会通过应力集中诱发裂纹、劣化延性[[S28,S33,S34,S35]]。当硼含量显著过量时，TiB₂会形成粗颗粒硼化物夹杂物，劣化合金延性，还会加剧熔池渣相聚集，提升铸造夹杂物生成风险[[S34,S28]]。

## 工艺调控与除硼方法

### 化学沉淀法

工业上脱除铝熔体中过量硼的成熟工艺为向熔体中加入钛或锆元素[[S8,S11,S12,S4]]：

- **加钛除硼**：钛与硼反应生成高熔点不溶的TiB₂相，配合由金属氯化物/氟化物组成的活性熔剂，通过充分搅拌使熔剂捕集二硼化物沉淀颗粒，随后静置依靠密度差沉降分离[[S8,S11]]。工艺中硼添加量需保证完全络合熔体中绝大部分溶解态的Ti、V杂质[[S12]]。
- **加锆除硼**：锆与硼反应生成高熔点不溶的ZrB₂金属间化合物，密度大于铝熔体可沉降至炉底，实现硼的定向脱除[[S4]]。

采用720°C下先熔炼保温2h，再投入活性助熔剂继续处理2h的工艺，可将铝熔体中硼元素含量降至(0.1~10)×10⁻⁴%（1~100 ppm）范围，除硼过程不会显著降低合金的抗拉强度，铝熔体中Fe、Si等主量杂质不受该除硼工艺影响[[S8]]。

### 全流程源头控硼

全流程源头控硼措施包括[[S3,S6]]：

1. **电解铝环节管控**：严格控制向电解质中投入的含硼物料总量。进入铝电解质的硼总量中，不超过60%转入铝熔体，不超过20%进入气相，其余部分留在渣层[[S3]]。
2. **回炉料预处理**：压铸废铝预处理阶段分拣剔除含硼添加剂、硼化物增强相的特殊铝基复合废料，避免硼元素随废料混入主熔体[[S6]]。
3. **精炼过滤**：精炼阶段搭配陶瓷泡沫过滤装置，拦截未完全沉降的细小硼化物夹杂物颗粒[[S6]]。

## 与其他杂质元素的对比分析

### B、Fe、Ca杂质对塑性损害机理对比

| 对比维度 | B（硼） | Fe（铁） | Ca（钙） |
|---|---|---|---|
| 损害产物 | AlB₂、TiB₂粗大硼化物[[S16]] | 针状Al₃Fe、α-AlFeSi富铁相[[S33]] | CaSi₂相、诱发疏松[[S33]] |
| 损害机理 | 硬脆硼化物沿晶界析出，应力集中诱发裂纹[[S16]] | 针状化合物割裂铝基体[[S33]] | 提升吸氢倾向增加疏松，同时抑制共晶硅变质[[S33,S34]] |
| 阈值特征 | 存在收益区间：0.005%~0.01%可细化晶粒提升塑性，超过100~150 ppm临界值后劣化[[S28,S33]] | 不存在收益区间：含Fe>0.2%即析出粗大针状相直接损害塑性[[S33,S35]] | 无收益区间：Ca含量>0.005%即对延性产生不良影响[[S28]] |
| 作用特点 | 损害具有明显的阈值转折[[S28,S33]] | 含量增加即单调劣化[[S33]] | 低含量即可引发疏松[[S28]] |

### 交互作用信息

现有压铸铝相关冶金手册未记录硼与Fe、Ca、P在铝熔体中形成稳定复合夹杂相的反应，不存在硼与铁的协同脆化作用，也不存在硼与该三类元素的相互抑制析出效应[[S33,S28,S34]]。具体而言：Fe在铝熔体中生成的典型相为Al₃Fe、α-AlFeSi等针状富铁相；Ca在铝熔体中可与硅生成难溶的CaSi₂相；P在常规压铸铝熔体中无高稳定性含硼复合相生成记录[[S33,S34]]。

![图1-3 铝合金汽车配件，展示四款不同类型免热处理压铸铝合金汽车零部件，体现硼元素管控在工程化应用场景中的实际要求](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d31f501-60dd-46ff-b054-1aff29594d8e/resource)

## Sources
- S19: [400485_硼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/787bb9da-11d6-4df4-bc5a-a7b4bc15d3e3/resource) (`787bb9da-11d6-4df4-bc5a-a7b4bc15d3e3`)
- S5: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e8783b2-4898-4a43-9d56-9fe9ffade2c0/resource) (`1e8783b2-4898-4a43-9d56-9fe9ffade2c0`)
- S38: [晶粒细化对免热处理压铸铝合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff0b8c0e-38a1-4963-9054-633e2deae52e/resource) (`ff0b8c0e-38a1-4963-9054-633e2deae52e`)
- S17: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68b8d9eb-1208-4525-a0c6-d2db868dcbe8/resource) (`68b8d9eb-1208-4525-a0c6-d2db868dcbe8`)
- S23: [铝熔体中净化剂的净化机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6cf42cf-b7ba-4ffe-99b5-84480abf90a1/resource) (`b6cf42cf-b7ba-4ffe-99b5-84480abf90a1`)
- S13: [aluminium cast house technology vii__ec5c7df913](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c2c0525-aefb-445a-991d-92eb57d403ba/resource) (`5c2c0525-aefb-445a-991d-92eb57d403ba`)
- S30: [aluminium cast house technology vii__ec5c7df913](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d778b2bb-1523-431e-be45-2d3d695c2c94/resource) (`d778b2bb-1523-431e-be45-2d3d695c2c94`)
- S3: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/110cfe55-8ebb-45f5-8983-c306bd97f485/resource) (`110cfe55-8ebb-45f5-8983-c306bd97f485`)
- S18: [a handbook of lattice spacings and structures of metals and alloys__d7369eca0e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72b3085c-c567-4809-88d1-396e714fa506/resource) (`72b3085c-c567-4809-88d1-396e714fa506`)
- S37: [制冷管铝材中典型夹杂物形成机制及其腐蚀行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb34eb1f-ee82-4601-9048-f00c8da80b86/resource) (`fb34eb1f-ee82-4601-9048-f00c8da80b86`)
- S32: [铝合金组织细化用中间合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d99cb352-6f37-484f-8684-cca3e87ccd68/resource) (`d99cb352-6f37-484f-8684-cca3e87ccd68`)
- S15: [铝合金车轮与钢制车轮轮箍生产加工新工艺新技术及产品质量检测实用手册1卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5eb246f6-cc21-4b14-a2c1-823758f95c6e/resource) (`5eb246f6-cc21-4b14-a2c1-823758f95c6e`)
- S28: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d42eba23-db3c-417c-af8e-8fedc8eb01bf/resource) (`d42eba23-db3c-417c-af8e-8fedc8eb01bf`)
- S36: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f10b13a8-ebb0-4302-9ccc-faa48bf88a9b/resource) (`f10b13a8-ebb0-4302-9ccc-faa48bf88a9b`)
- S16: [basic mechanical properties and lattice defects of intermetallic compounds__affa85d061](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63a5b116-6696-42c5-b428-f8d39d591c6c/resource) (`63a5b116-6696-42c5-b428-f8d39d591c6c`)
- S10: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S25: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bcff56b2-c8a1-443a-9b1d-cb672736b917/resource) (`bcff56b2-c8a1-443a-9b1d-cb672736b917`)
- S9: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ed805b5-2ea0-42e3-a291-d5267ecc34fa/resource) (`3ed805b5-2ea0-42e3-a291-d5267ecc34fa`)
- S21: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a02050cf-086e-4071-ad7f-87b05b503352/resource) (`a02050cf-086e-4071-ad7f-87b05b503352`)
- S22: [基于AlSi8系高强韧免热处理压铸铝合金开发及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af7bd26c-054a-4e88-bfea-8298ce06892e/resource) (`af7bd26c-054a-4e88-bfea-8298ce06892e`)
- S20: [变质剂和不同细化剂对免热处理压铸铝合金变质及细化的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9883f122-2742-4ee0-89ec-6de4e981a85c/resource) (`9883f122-2742-4ee0-89ec-6de4e981a85c`)
- S27: [变形铝合金的细化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c82c403d-1f00-454b-8563-09c96cb0eb45/resource) (`c82c403d-1f00-454b-8563-09c96cb0eb45`)
- S34: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e12d9a09-d966-4c4c-93c9-3131a3b7e829/resource) (`e12d9a09-d966-4c4c-93c9-3131a3b7e829`)
- S33: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e06f0ccd-8b4c-4526-bbc2-7dc481f07347/resource) (`e06f0ccd-8b4c-4526-bbc2-7dc481f07347`)
- S35: [铝合金压铸件不良品对策问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/edd199b0-7f41-44e9-a55e-53ffac990572/resource) (`edd199b0-7f41-44e9-a55e-53ffac990572`)
- S8: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2fde6567-c69b-47f7-a9cb-73ffa3e8b885/resource) (`2fde6567-c69b-47f7-a9cb-73ffa3e8b885`)
- S11: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/586f03e1-dc83-4cf9-a785-7b3b209b75e3/resource) (`586f03e1-dc83-4cf9-a785-7b3b209b75e3`)
- S12: [原铝及其合金的熔铸生产问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ab3b33e-5ed9-4da6-8be9-9a58b7cbfa92/resource) (`5ab3b33e-5ed9-4da6-8be9-9a58b7cbfa92`)
- S4: [变形铝合金的细化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11704b2e-3283-47e8-a9b3-d7b6509c24dd/resource) (`11704b2e-3283-47e8-a9b3-d7b6509c24dd`)
- S6: [aluminum recycling__799280468c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c5062a8-459e-4e61-b26e-63821ae2f44f/resource) (`2c5062a8-459e-4e61-b26e-63821ae2f44f`)