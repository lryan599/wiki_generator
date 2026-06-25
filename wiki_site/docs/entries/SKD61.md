---
version: "v1"
generated_at: "2026-06-18T12:59:09+00:00"
confidence_score: 0.84
confidence_level: "high"
confidence_basis:
  cited_sources: 41
  source_quality_score: 0.86
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

## 定义与分类

SKD61是由日本工业标准JIS G4404《合金工具钢》规定的热作模具钢牌号，属于该标准中合金工具钢大类下的热作模具钢子类，是典型的空冷硬化型热作模具钢 [[S28,S12]]。其官方正式名称为SKD61，日常使用的“SKD61合金”属于非规范的泛化称谓，而“SKD61铸钢”是完全错误的分类表述——SKD61属于变形合金工具钢范畴，不属于铸钢 [[S30,S34]]。

在国际标准中，SKD61的主要等效对应牌号为：美国AISI H13、德国DIN 1.2344 / X40CrMoV5-1、中国GB 4Cr5MoSiV1，不同标准下的该类钢属于同一款型的不同标准命名 [[S9,S41,S47]]。其中，SKD61与AISI H13存在细微成分差异：SKD61的碳含量范围为0.32%~0.42%，较AISI H13的0.32%~0.45%控制区间更窄；两者钒含量规定范围均为0.8%~1.2% [[S10,S3]]。

## 化学成分

SKD61的标准化学成分（质量分数，wt%）如下 [[S16,S46]]：

| 元素 | C | Si | Mn | Cr | Mo | V | P | S |
|------|-----|-----|------|------|------|------|------|------|
| SKD61 | 0.32~0.42 | 0.8~1.2 | ≤0.50 | 4.5~5.5 | 1.0~1.5 | 0.8~1.2 | ≤0.03 | ≤0.01 |

该钢以铬、钼、钒为主要合金元素，Cr-Mo-V的成分配比提供了优异的抗热冲击磨损性能和高温强度 [[S20]]。

## 物理与力学性能

### 常温物理与力学性能

SKD61的典型常温力学与物理性能参数如下 [[S36]]：

| 性能 | 硬度 | 密度 | 弹性模量 | 泊松比 | 屈服强度 | 热导率 | 比热容 |
|------|------|------|------|------|------|------|------|
| 数值 | 50 HRC | 7.85 g/cm³ | 210 GPa | 0.3 | 1490 MPa | 29 W/(m·K) | 460 J/(kg·K) |

### 热物理性能

SKD61在不同温度下的线膨胀系数与热传导率如下 [[S19]]：

| 温度区间 | 线膨胀系数 (×10⁻⁶/℃) |
|----------|----------------------|
| 20~100℃ | 11.3 |
| 20~200℃ | 12.5 |
| 20~300℃ | 13.4 |

在200℃时，热传导率为0.095 cal/(cm·sec·℃)，参数覆盖铝合金压铸常见工况的温度区间 [[S19]]。

### 相变点

SKD61的关键相变温度为：Ac相变点847~918℃，Ar相变点725~769℃，Ms点280℃ [[S42]]。

## 热处理工艺

### 常规热处理规范

SKD61的标准锻造与热处理参数如下 [[S42]]：

| 工艺 | 温度范围 | 冷却方式 | 硬度结果 |
|------|----------|----------|----------|
| 锻造 | 900~1100℃ | — | — |
| 退火 | 820~870℃ | 缓冷 | ≤29.5 HRC |
| 淬火 | 1000~1050℃ | 空冷 | — |
| 回火 | 550~650℃ | 空冷 | ≤53 HRC |

### 淬火工艺选择

SKD61的淬火温度区间为1000℃~1050℃，具体选择需根据模具的服役要求确定 [[S17,S42]]：

- **1000~1020℃空淬**：针对形状复杂、要求韧性优先、控制热处理变形的工件；
- **1030~1050℃空淬**：针对要求高耐磨性、高抗压性的工件。

常规淬火后推荐进行直接回火处理：工件从淬火温度空冷至马氏体转变量约90%的温度点（约100℃）时，停止冷却，直接转入回火炉。装炉温度需控制在300℃以下，缓慢升温至指定回火温度，回火操作不得少于2次；形状复杂、大尺寸工件需回火3次，以避免内应力过高引发开裂 [[S5]]。

### 回火硬度控制

SKD61压铸模具常规使用状态的回火硬度为HRC45~47。回火温度超过580℃后硬度会快速下降，该区间的回火参数需严格控制精度 [[S5,S45]]。50~55HRC的回火区间符合该钢种二次硬化特性的行业规范 [[S5]]。

示例热处理工艺：采用1025℃油冷淬火，565℃回火后硬度可达51.4HRC；若采用860℃油冷淬火、550℃回火，最终硬度为46.4HRC [[S40]]。

### 热处理变形特性

在淬火回火至硬度HRC47的条件下，SKD61表现出独特的热处理变形特征：直径方向尺寸变化率约0.17%，长度方向呈现出独特的负向收缩，明显区别于其他热作模具钢 [[S1]]。这一特征在模具设计与加工阶段需加以考虑。

![常用热作模具钢回火后尺寸变化率对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0430b03b-5777-454e-a6da-35ac6c40223d/resource)

### 表面处理

**氮化处理**：SKD61压铸模的常规氮化处理要求获得0.15~0.2mm深度的氮化层，氮化完成后建议将氮化表面研磨去除0.01mm，以消除氮化层表层的脆性白亮层，避免压铸使用过程中表面剥落 [[S5]]。

针对SKD61等效钢种H13的压铸用气体渗氮工艺，常规处理温度为525℃，通过控制氨分解率可获得最高硬度约70HRC的渗层，处理后工件表面耐磨性、抗铝液熔蚀性能显著提升 [[S27,S35]]。液体盐浴氮碳共渗常规操作温度为570℃，处理效率远高于气体渗氮 [[S27,S35]]。

**喷丸预处理**：渗氮前增加喷丸预处理的SKD61类热作钢，渗氮层有效深度可从常规的54μm提升至72μm，最高表面硬度可达1196HV，同时渗氮层白亮层厚度从3.7μm提升至4.1μm，可进一步提升模具表面抗热疲劳性能 [[S32]]。

## 压铸工艺中的角色

SKD61是压铸模具的核心材料之一，铬钼钒的成分配比提供了优异的抗热冲击磨损和高温强度性能，适配铝合金、锌合金、镁合金三种主流低熔点合金的压铸模具生产场景，广泛用于普通工况下的铝合金压铸模芯，在一体化压铸的非严苛工况模芯部位也可选用 [[S20,S7,S21]]。

SKD61在600℃服役温度下仍能保持较高强度、硬度与耐磨性，同时兼顾良好韧性和抗热疲劳性能，相比传统钨系3Cr2W8V钢制作的铝合金压铸模寿命有显著提升 [[S8]]。该钢种具备良好的耐热性、耐氧化性和抗热冲击性能，交替经受急热急冷循环时不易产生热压龟裂 [[S24,S41,S23,S20]]。

### 典型应用

SKD61是汽车类铝合金压铸件模具的常用制造材料，涵盖油底壳、发动机缸体类大型铝合金铸件、换向塔、平板类通信或家电铝合金壳体压铸件模具，也常用于压铸模的标准镶件、模梢等易损零件 [[S21,S44]]。

## 缺陷与失效机制

国内铝合金压铸模具的失效形式分布为：热疲劳裂纹占67%，碎裂/整体脆断占18%，磨耗占6%，熔损冲蚀占4%，SKD61压铸模具的失效分布与该统计结果高度吻合 [[S43,S37]]。

### 热疲劳龟裂

热疲劳龟裂是SKD61模具最主要的失效形式。模具反复经历激冷激热循环，型腔表面和内部产生交替循环的热应力，当应力超过材料疲劳极限时表面萌生微裂纹，后续微裂纹逐步扩展形成龟裂状形貌。裂纹一般深度不超过1mm。服役时浇注温度与模具预热温差越大、冷却速度越快，龟裂产生速度越快 [[S18,S6,S26]]。

### 冲蚀与熔蚀

SKD61模具的冲蚀失效多发生在近浇口位置，是高速高压高温金属液的机械冲刷、高温腐蚀、材料与铝液发生化学反应生成脆性相共同作用的结果。熔蚀（粘铝）失效是模具表面防护涂层脱落后，铝液与SKD61基体直接接触生成FeAl₃金属间化合物，后续被流动金属液逐步剥离形成表面损伤 [[S26,S8]]。

### 整体脆断

SKD61模具脆断多发生在服役初期，诱因包括模具结构设计尖角应力集中、冶金质量差晶界存在脆性相、热处理后内应力未完全消除、焊接修补部位夹杂超标。材料塑韧性不足时，热疲劳裂纹会快速失稳扩展引发整体断裂 [[S43,S2]]。

## 与其他模具钢的比较

### H11

H11（4Cr5MoSiV）不含额外钒元素，500℃以下服役时热强性良好，淬透性优异（直径100mm以下工件空冷即可淬硬）。抗热疲劳性能优于SKD61，但热强性、耐磨性低于SKD61。适配工况偏冲击载荷高、温度峰值低的高速锤锻模及对热疲劳要求极高的非浇口区域压铸模 [[S31,S4]]。

### H21

H21属于高钨系热作模具钢，高温抗软化、抗冲蚀能力远优于SKD61，但常温韧性显著偏低，正常服役工况下脆性风险更高，不能直接水冷。适配铜合金高温压铸模具、高温热挤压模具场景，服役温度不宜超过650℃ [[S39,S38]]。

### DAC（SKD61同牌号工业化量产钢种）

DAC是日本日立公司生产的SKD61同牌号工业化量产钢种，兼顾良好高温强度、韧性、耐磨性、易切削性，热处理变形量小，广泛用于铝、镁、锌合金压铸模具 [[S21]]。

### 8418/8407

8407（对应8418）由瑞典一胜百生产，采用特殊精炼工艺冶炼，组织纯度与各向同性显著高于传统SKD61（H13），抗机械疲劳、抗热应力疲劳性能更优。在不损失韧性的前提下可将使用硬度提升1~2HRC，整体模具寿命比普通SKD61高，适用于高负荷、高批量生产场景下的大型铝合金压铸模 [[S25]]。

## 相关标准与规范

SKD61关联的主流权威标准包括 [[S34,S9,S10]]：

| 标准 | 内容 |
|------|------|
| JIS G4404（2000版） | 日本合金工具钢标准，SKD61的原始规范标准 |
| ASTM A681 | 美国热作合金工具钢标准，涵盖AISI H13 |
| GB/T 1299 | 中国合金工具钢标准，涵盖4Cr5MoSiV1 |
| NADCA #207-2003 | 北美压铸协会优质压铸模具钢标准，对H13系列钢的硫、磷杂质含量做出更严苛限定：优级品硫含量≤0.005%，超级品硫含量≤0.003%、磷含量≤0.015% |

NADCA #207-2003标准明确了优质级H13（即SKD61升级高纯版本）的硬度、冲击韧性的最低验收指标，可作为压铸模具钢选型与质量验收的权威参考依据 [[S38,S11]]。

## Sources
- S28: [模具材料性能与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e1a774a-dc6d-4a1d-afc3-d78cd2600ff6/resource) (`8e1a774a-dc6d-4a1d-afc3-d78cd2600ff6`)
- S12: [模具材料应用手册第二版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46354fed-aa67-412f-ba27-5730cfbf4727/resource) (`46354fed-aa67-412f-ba27-5730cfbf4727`)
- S30: [压铸技术实务](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a2cad1bc-d0c3-4077-b0b2-54b8e67dec67/resource) (`a2cad1bc-d0c3-4077-b0b2-54b8e67dec67`)
- S34: [实用模具材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b02824f4-4196-4fc2-92a4-54f9fdfd7043/resource) (`b02824f4-4196-4fc2-92a4-54f9fdfd7043`)
- S9: [5368567_H13钢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b0c8af7-a5cd-452e-b2be-ceb4c50ca11f/resource) (`3b0c8af7-a5cd-452e-b2be-ceb4c50ca11f`)
- S41: [0197_c95046d5da48befa_Tool_steel_1.2344](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb7f0c4e-f468-47c1-b3d4-6913a701f1eb/resource) (`cb7f0c4e-f468-47c1-b3d4-6913a701f1eb`)
- S47: [注塑模具设计实用教程 第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8011a96-a75a-4216-8444-f627ad17d9fb/resource) (`f8011a96-a75a-4216-8444-f627ad17d9fb`)
- S10: [10398210_H13钢材](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d3f68c6-2be5-44f9-bb95-247c85616831/resource) (`3d3f68c6-2be5-44f9-bb95-247c85616831`)
- S3: [模具材料及表面强化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0992cc81-ed39-44dd-adca-898444e4808f/resource) (`0992cc81-ed39-44dd-adca-898444e4808f`)
- S16: [工具钢SKD61主要成份含量表（wt%）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a0cfce9-afa8-4b4a-8b45-ccea9c0a3460/resource) (`5a0cfce9-afa8-4b4a-8b45-ccea9c0a3460`)
- S46: [表3.1 SKD61模具材料化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0926a42-002e-4272-977b-129f9a9fe1cc/resource) (`f0926a42-002e-4272-977b-129f9a9fe1cc`)
- S20: [0197_c95046d5da48befa_Tool_steel_1.2344](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70496189-13fd-4480-91cd-64fa7600ae2b/resource) (`70496189-13fd-4480-91cd-64fa7600ae2b`)
- S36: [Table 3.2 SKD61模具材料性能参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8958db4-4f64-4023-9708-fbfe678747b7/resource) (`b8958db4-4f64-4023-9708-fbfe678747b7`)
- S19: [工具钢热膨胀系数与热传导率参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/661d8b09-246a-4a3d-925d-11b0fb21748d/resource) (`661d8b09-246a-4a3d-925d-11b0fb21748d`)
- S42: [工具钢锻造与热处理参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2331740-8fcd-41dc-b21c-78dd0f3689b2/resource) (`d2331740-8fcd-41dc-b21c-78dd0f3689b2`)
- S17: [模具材料及其热处理译文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/614c0cb2-122f-4b93-93c8-f92f1d94414a/resource) (`614c0cb2-122f-4b93-93c8-f92f1d94414a`)
- S5: [压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19016426-a6c7-441b-92e3-9fd48d10799c/resource) (`19016426-a6c7-441b-92e3-9fd48d10799c`)
- S45: [模具材料及其热处理译文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec1c45ef-d0b7-40e0-965b-af78729afb8f/resource) (`ec1c45ef-d0b7-40e0-965b-af78729afb8f`)
- S40: [模具材料性能与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb6c676e-0002-47bf-b50d-47d85caa6766/resource) (`cb6c676e-0002-47bf-b50d-47d85caa6766`)
- S1: [图10 典型热模钢经淬火回火到硬度为HRC47时的尺寸变化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0430b03b-5777-454e-a6da-35ac6c40223d/resource) (`0430b03b-5777-454e-a6da-35ac6c40223d`)
- S27: [die casting metallurgy surface treatments for steels__6de99569f3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87187a35-4252-4613-bb09-67816651870c/resource) (`87187a35-4252-4613-bb09-67816651870c`)
- S35: [die casting metallurgy__322fa9dd3c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2b0f759-8673-430f-a31e-21ec1c43e5b2/resource) (`b2b0f759-8673-430f-a31e-21ec1c43e5b2`)
- S32: [application of shot peening and shot blasting to increase hardness and d__2594a1d422](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a66723f0-2d16-4502-92c6-a7982e6e8cba/resource) (`a66723f0-2d16-4502-92c6-a7982e6e8cba`)
- S7: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f778e38-12d2-4004-a3a0-241ae8abdf35/resource) (`1f778e38-12d2-4004-a3a0-241ae8abdf35`)
- S21: [模具材料的选用与热处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/750727d2-838b-4110-8237-b89ec44357af/resource) (`750727d2-838b-4110-8237-b89ec44357af`)
- S8: [模具失效与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d57d311-a5d4-468f-8b16-1c4de437e23b/resource) (`2d57d311-a5d4-468f-8b16-1c4de437e23b`)
- S24: [模具制造基础知识](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8eb5c6-2190-43ae-a034-3c04b73a9d77/resource) (`7b8eb5c6-2190-43ae-a034-3c04b73a9d77`)
- S23: [压铸模具常用钢材国内外钢号对照表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79314949-a9aa-4fb8-aa53-d7d6e1d403ee/resource) (`79314949-a9aa-4fb8-aa53-d7d6e1d403ee`)
- S44: [图16-9 模梢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da44f23a-2c7d-41e1-858e-698c1fae7261/resource) (`da44f23a-2c7d-41e1-858e-698c1fae7261`)
- S43: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6862891-fc2d-4b40-bc27-d2bf20e30913/resource) (`d6862891-fc2d-4b40-bc27-d2bf20e30913`)
- S37: [实用模具材料应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b979790f-5613-4f1d-aad3-ddff7ea30c58/resource) (`b979790f-5613-4f1d-aad3-ddff7ea30c58`)
- S18: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/624320c2-1513-4030-9f2d-81e22afec100/resource) (`624320c2-1513-4030-9f2d-81e22afec100`)
- S6: [工模具材料强化处理应用技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/193e2f86-def0-4617-9824-026cc895e0bb/resource) (`193e2f86-def0-4617-9824-026cc895e0bb`)
- S26: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82c2d2a6-0a26-428e-b2ee-9ad3a571ce7e/resource) (`82c2d2a6-0a26-428e-b2ee-9ad3a571ce7e`)
- S2: [压力铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0460a8b1-f128-4c45-a463-7dfffe422e6b/resource) (`0460a8b1-f128-4c45-a463-7dfffe422e6b`)
- S31: [模具材料及表面强化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5e06f02-6a28-4498-a689-6eae1fc41720/resource) (`a5e06f02-6a28-4498-a689-6eae1fc41720`)
- S4: [模具材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/187def75-68d5-41ba-ba3f-65424e659b36/resource) (`187def75-68d5-41ba-ba3f-65424e659b36`)
- S39: [工模具材料应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc5a085a-4575-417f-98ff-e374ed6ec871/resource) (`bc5a085a-4575-417f-98ff-e374ed6ec871`)
- S38: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc53cb25-5396-484c-be87-4b2a0e144011/resource) (`bc53cb25-5396-484c-be87-4b2a0e144011`)
- S25: [模具材料的选用与热处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/826a5454-7354-4a37-8e7a-f32e76f768d0/resource) (`826a5454-7354-4a37-8e7a-f32e76f768d0`)
- S11: [die cast engineering a hydraulic thermal and mechanical process__e5dfda1a8e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42014a26-20e9-4084-9dd4-f837d839c990/resource) (`42014a26-20e9-4084-9dd4-f837d839c990`)