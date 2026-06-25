---
version: "v1"
generated_at: "2026-06-18T09:14:02+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 43
  source_quality_score: 0.85
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

IF钢（Interstitial-Free Steel，无间隙原子钢）是在超低碳钢中加入足量的钛（Ti）、铌（Nb）等强碳氮化合物形成元素，将钢中间隙固溶的碳（C）、氮（N）原子完全固定为稳定的碳氮化物，从而获得基体中无间隙原子的洁净铁素体钢 [[S37,S34,S18,S43]]。IF钢具有极低的屈服强度和屈强比、高断后伸长率、高塑性应变比（r值）、高加工硬化指数（n值）以及完全无时效性，具备极强的超深冲成形性能，是继沸腾钢和铝镇静钢之后开发的第三代汽车用冷成形深冲压钢 [[S50,S29,S43]]。

IF钢已形成普通IF钢板、电镀锌IF钢板、热镀锌IF钢板、镀铝IF钢板、高强度IF钢板等完整产品系列，广泛用于汽车外覆盖件、高端家电面板等对深冲性能和表面质量要求严苛的场景 [[S50,S29,S23]]。

## 分类与微合金化路线

工业生产中，IF钢按微合金化元素添加方式分为三类 [[S50,S33]]：

| 类型 | 特点 | 优势 | 劣势 |
|------|------|------|------|
| **Ti-IF钢** | 仅添加Ti，通过Ti同时固定C、N、S元素 | r值和伸长率最高，成分对工艺波动不敏感，工艺可操作性强 | 平面各向异性（Δr）大，镀层抗粉化能力差 |
| **Nb-IF钢** | 仅添加Nb固定C原子，搭配其他元素固定N | 平面各向异性小，镀层抗粉化能力好，可细化晶粒 | r值和延伸率略低于Ti-IF钢，力学性能对工艺敏感 |
| **（Ti+Nb）-IF钢** | 同时添加Ti和Nb，Ti优先固定N/S，Nb负责固定C | 兼具两类优点，整卷性能均匀，屈服/抗拉强度更高，Δr值低（<0.3），镀层抗粉化优异 | 伸长率和r值略低于Ti-IF钢 |

Ti+Nb复合添加IF钢在780℃及以上退火温度区间内晶粒度稳定在19级，退火温度升高时无明显晶粒长大，有利于焊接性能；其Δr值整体低于0.3，远低于Ti-IF钢（退火780℃以上大于0.5），可大幅降低冲压制耳率；铌元素的加入还可避免高钛钢种常见的表面“木纹”缺陷，适用于汽车外板等对表面质量和冲压均匀性要求高的场景 [[S24,S52,S46,S33]]。

**图：Nb-Ti-IF钢与Ti-IF钢镀层抗粉化特性对比**
![Nb-Ti-IF钢与Ti-IF钢粉化特性对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/351228a1-d795-4b14-921f-abd2d26f5f35/resource) [[S14]]

## 化学成分与稳定化机理

### 典型成分范围

现代IF钢的典型成分控制要求：w_C ≤ 0.005%（50 ppm），w_N ≤ 0.003%（30 ppm），有效合金元素原子比 w_X(at%) / w_C(at%) ≈ 1。Ti-IF钢的Ti质量分数约为0.05%，Nb-IF钢的Nb质量分数约为0.1% [[S34,S49,S39]]。

工业实测IF钢全成分实例（wt.%）[[S32]]：

| C | Si | Mn | P | S | Al | Nb | Ti | N |
|---|---|---|---|---|---|---|---|---|
| 0.0014 | 0.0041 | 0.1443 | 0.0115 | 0.01 | 0.0615 | 0.0036 | 0.0411 | 0.0016 |

IF钢属于高级优质钢范畴，S、P杂质控制水平远高于普通钢要求（普通钢 w_S ≤ 0.055%，w_P ≤ 0.045%）[[S6]]。

### 间隙原子固定计算

Ti-IF钢中钛完全稳定的计算公式为 [[S49,S34]]：

- **Ti(稳定) = 3.42N + 1.5S + 4C**

Ti+Nb复合IF钢中，Ti用于固定N和S，Nb用于固定C [[S49,S34,S24]]：

- **Ti(稳定) = 3.42N + 1.5S**
- **Nb(稳定) = 7.74C**

**图：IF钢有效合金元素含量与碳含量匹配关系**
![新型超低碳钢与普通IF钢的成分范围示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/372164b8-064a-468a-aed5-bf0e5dc829f5/resource) [[S16]]

## 力学性能特征

常规工业量产IF钢的典型力学性能指标 [[S34,S43,S50,S23]]：

| 性能指标 | 典型值 |
|------|------|
| 屈服强度 | ≤ 180 MPa |
| 抗拉强度 | 270 ~ 350 MPa |
| 断后伸长率 | ≥ 50% |
| 平均塑性应变比 r | ≥ 2.0（典型2.5） |
| 加工硬化指数 n | ≥ 0.25（典型0.27） |
| 屈强比 | ≤ 0.55 |
| 时效指数 AI | ≈ 0（完全无时效） |

这些指标远高于常规深冲钢，使IF钢成为超深冲场景的首选材料。

## 生产工艺路线

IF钢全链路典型生产工艺流程为：**铁水预处理 → 底吹转炉/电炉初炼 → RH真空循环脱气精炼 → 连铸板坯生产 → 热轧 → 冷轧 → 罩式退火/连续退火**，部分镀锌IF钢后续衔接连续热镀锌工序 [[S39,S34]]。

### 关键工艺控制点

**碳控制** [[S5,S39]]：
- 转炉终点控制：RH脱碳前钢水碳300~400 ppm，氧500~600 ppm
- RH脱碳阶段通过提升气体流量、增大浸渍管直径、降低真空室压力提高循环流量
- RH总处理时间：10~25 min
- 采用真空槽冷钢、中间包覆盖剂、结晶器保护渣、长水口氩气密封等全流程防增碳措施

**氮控制** [[S5]]：
- 转炉停吹氮控制在20 ppm以下
- 钢包-中间包区域通过长水口氩封将全程浇铸增氮量控制在3 ppm以内

**热轧**：采用低温加热、低温卷取工艺，降低能耗同时避免酸洗效率和成材率下降 [[S39]]。

**退火**：IF钢无需设置过时效段；连续退火温度控制在840℃以上可促进{111}取向γ纤维织构充分发展，提升深冲性能 [[S39,S40]]。

## 夹杂物特征与控制

### Al₂O₃夹杂物的形成与分布

铝脱氧工艺下，IF钢连铸板坯中典型非金属夹杂物以纯Al₂O₃为绝对主要类型，二维形貌可分为不规则形和长条状 [[S36,S2]]。Al₂O₃夹杂物熔点高达2050℃，可作为异质形核点，在连铸凝固过程中TiN夹杂物高概率在其表面附着析出，MnS夹杂物附着析出概率较低 [[S36]]。

夹杂物在连铸坯中的分布规律为：内弧侧皮下位置夹杂物数密度最高、平均尺寸最小；板坯厚度中心位置夹杂物数密度最低、平均尺寸最大。由于连铸弯曲段大尺寸夹杂物受浮力作用上浮至内弧侧被凝固坯壳捕获，连铸坯内弧侧总氧含量高于外弧侧 [[S36,S2]]。小尺寸Al₂O₃夹杂物主要在连铸坯表层被捕获，30 μm级大尺寸Al₂O₃夹杂物除表层外，还会在连铸坯内弧侧1/4厚度位置聚集 [[S3]]。

### 表面缺陷遗传

Al₂O₃夹杂物常以颗粒聚集成云簇状分布，这类簇状硬脆夹杂物在轧制过程中几乎不发生塑性变形，会沿轧制方向被拉长后留存于冷轧薄板基体中 [[S7]]。在IF钢连铸-热轧-冷轧全流程遗传过程中，硬脆未变形的Al₂O₃簇状夹杂物会在冷轧薄板表面诱发沿轧制方向延伸的线状sliver缺陷；当夹杂物在板坯表层附近聚集时，后续轧制延伸过程中会破坏基体连续性，形成表面翘皮缺陷，夹杂物尺寸越大、簇状聚合程度越高，缺陷产生概率越高 [[S7,S51]]。

### 结晶器电磁搅拌（M-EMS）的作用

结晶器电磁搅拌在IF钢连铸中的工业典型操作参数区间为电流180~600 A，频率1.8~6 Hz，经工业验证的优化工况为600 A/4 Hz（适配230 mm厚度板坯）[[S35,S4,S31]]。

**图：结晶器电磁搅拌对连铸过程的作用机理**
![M-EMS对夹杂物分布和凝固组织的影响机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73871de2-5673-4382-b7c5-02e8a1866456/resource) [[S30]]

M-EMS作用下，IF钢连铸坯皮下Al₂O₃夹杂物关键参数变化 [[S36,S25,S8]]：

| 参数 | 无M-EMS | 有M-EMS（600A/4Hz） | 变化幅度 |
|------|------|------|------|
| 数密度 | 9.99 个/mm² | 6.11 个/mm² | **降低38.8%** |
| 面积分数 | 69.51×10⁻⁶ | 57.31×10⁻⁶ | 降低约17.5% |
| 平均粒径 | 2.45 μm | 2.87 μm | 增大17.1% |
| 皮下总氧含量 | — | 降低1~3 ppm | — |

夹杂物从钢液向结晶器顶渣的去除率由20.15%（无M-EMS）提升至29.19%（600A），向凝固坯壳的捕获率由79.85%降至70.81%；M-EMS对夹杂物分布的作用区域集中在铸坯表层约30 mm深度范围内 [[S25,S4]]。

## 残余元素Cu、Sn引起的表面热裂

### 高温氧化与界面富集

IF钢在1050℃空气气氛下氧化后，氧化层由外到内依次为Fe₂O₃、Fe₃O₄、FeO+Fe₃O₄、FeO四层结构 [[S45,S38]]。残余元素Cu、Sn的添加会降低钢的氧化激活能，使氧化层厚度增加，氧化层内长条状缝隙数量明显增多、致密性下降 [[S45,S26]]。

由于Cu、Sn氧化势低于Fe，在950~1200℃的常规热轧温度区间发生Fe优先氧化，Cu、Sn元素在氧化层-基体界面富集 [[S47,S12]]：
- 单独添加Sn：不会在界面产生明显Sn富集，仅出现微弱晶界偏聚
- 单独添加Cu：析出富Cu液相并直接向晶界渗透
- **同时存在Cu和Sn**：Sn显著降低Cu在奥氏体中的溶解度，并进一步降低富Cu相的熔点，在界面生成低熔点富Cu-Sn相；该液相沿晶界向内渗透，大幅降低晶界结合强度

### 热裂临界含量与机理

实验条件下（1050℃预氧化2h，1000℃热压缩、应变速率5 s⁻¹、变形量60%）不同Cu、Sn含量IF钢的表面热裂纹数量密度 [[S12,S38]]：

| 试样条件 | 裂纹数量密度 |
|------|------|
| 空白IF钢 | 0.663 |
| 仅添加0.11% Sn | 2.122（全部为微小裂纹） |
| 仅添加0.11% Cu | 4.191（已出现明显可观测裂纹） |
| 同时添加0.11% Cu + 0.11% Sn | **6.446**（大尺寸裂纹占比显著提升） |

当Cu、Sn同时达到0.11 wt%时，裂纹数量密度骤升至6.446，表面热裂缺陷发生率进入快速上升区间，该组合浓度即为对应实验条件下的临界安全限值 [[S12,S38]]。

**图：残余元素Cu、Sn在氧化层-基体界面的富集特征（BSE形貌及面扫结果）**
![不同样品氧化层-基体界面处Cu、Sn富集情况的BSE形貌和面扫结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3099db0a-a471-434f-94af-96b45e819dd0/resource) [[S47]]

## 稀土镧（La）的减害化效果

### 改善表面热脆

针对含0.11%Cu + 0.11%Sn的IF钢试样，添加0.013%（质量分数）La后，热压缩表面裂纹数密度由6.446降至3.316，**抑制比例达48.6%**，有效改善含残余Cu、Sn IF钢的表面热脆性能 [[S12,S38]]。

La抑制热裂的作用机理包含三部分 [[S12,S47,S26]]：
1. 与钢中部分Sn元素反应消耗基体中残余Sn，同时降低钢的氧化速率，减少氧化层-基体界面处低熔点富Cu-Sn液相的析出量
2. 在晶界处偏聚，强化晶界强度，阻碍低熔点液相向晶界渗透
3. 细化晶粒，延长氧沿晶界扩散路径，提升氧化层致密性

### Al₂O₃夹杂物改性

稀土元素对钢中棱角状Al₂O₃夹杂物的改性路径为：**Al₂O₃ → 稀土铝酸盐（REAlO₃）→ 稀土氧硫化物**。La添加后可将IF钢中原生的棱角状Al₂O₃夹杂物逐步转化为高熔点稀土铝酸盐类夹杂物，促进小尺寸夹杂物碰撞聚合为大尺寸夹杂物，提升上浮去除效率，降低夹杂危害 [[S26,S17,S44]]。

## 相关牌号与标准

### 常见国际牌号

冷轧冲压钢板按发展历程分为三代：第一代沸腾钢，第二代铝镇静钢（如08Al），第三代IF钢（IF-grade）[[S29]]。

| 标准体系 | 普通深冲级（非IF） | IF级超深冲 |
|------|------|------|
| 中国 GB/T 5213 | 08Al（SC1） | SC2、SC3 |
| 德国/欧标 | St14、DC04 | St15、DC05、DC06 |
| 日本 JIS | SPCE | SPCEN（非时效性） |

DC04为普通深冲级，r值和n值仅做单方向指标保证；DC05、DC06属于IF级超深冲钢，要求r值和n值按多方向加权平均值保证（r=(r₉₀+2r₄₅+r₀)/4，n=(n₉₀+2n₄₅+n₀)/4）。日标SPCE属于第二代铝镇静深冲钢，仍含有一定量间隙固溶原子，无法达到IF钢的超深冲和非时效性能 [[S10,S41]]。

### 国家标准要求

中国国家标准GB/T 5213系列针对深冲冷轧薄钢板的强制要求包括 [[S22,S28,S42,S48]]：
- 08Al类深冲钢按拉深质量分为 **ZF**（最复杂拉深）、**HF**（很复杂拉深）、**F**（复杂拉深）三个等级
- 不同厚度区间钢板对应的杯突试验最低值
- 厚度≥2 mm时180°冷弯试验（弯心直径d=0）不得出现裂纹、裂口、分层
- IF级超深冲钢产品进一步要求r值、n值的加权平均值达标
- 尺寸精度分为普通厚度精度PT·A和高级厚度精度PT·C，不平度精度分为PF·A和PF·C

## 典型应用

IF钢广泛用于以下领域 [[S50,S29,S23]]：
- **汽车外覆盖件**：门外板、行李箱盖板、侧围外板、顶盖、发动机盖外板
- **形状复杂车身冲压件**：高强度车身冲压件、发动机油底壳等复杂深冲件
- **高成形性镀锌板基板**：解决连续热镀锌工艺下的钢板时效问题
- **高端家电面板**：对表面质量和复杂深冲需求高的民用产品

## Sources
- S37: [6168621_无间隙原子钢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a42a4b15-c2e2-4f71-acfa-ddea6976c26f/resource) (`a42a4b15-c2e2-4f71-acfa-ddea6976c26f`)
- S34: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84633b23-e269-42f2-a102-0bc4de2d1e29/resource) (`84633b23-e269-42f2-a102-0bc4de2d1e29`)
- S18: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a14045d-adb4-4214-a955-da79c13a8a43/resource) (`4a14045d-adb4-4214-a955-da79c13a8a43`)
- S43: [金属塑性成形手册 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c6a5cdcf-c19a-4d1e-b9eb-7c18220c6fd0/resource) (`c6a5cdcf-c19a-4d1e-b9eb-7c18220c6fd0`)
- S50: [汽车覆盖件模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8ecd2ea-2316-4a79-9dc8-0917f56088d1/resource) (`e8ecd2ea-2316-4a79-9dc8-0917f56088d1`)
- S29: [实用冲压工艺及模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/713ca62f-50c8-428e-9244-b17b7524243c/resource) (`713ca62f-50c8-428e-9244-b17b7524243c`)
- S23: [汽车覆盖件模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ac62997-fc73-40c6-8abf-748b92ad2247/resource) (`5ac62997-fc73-40c6-8abf-748b92ad2247`)
- S33: [实用冲压工艺及模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/820815ce-45af-4ac8-bc4e-7050d3cdd5b4/resource) (`820815ce-45af-4ac8-bc4e-7050d3cdd5b4`)
- S24: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c165603-bc08-421d-bfab-a382fd4ddbe4/resource) (`5c165603-bc08-421d-bfab-a382fd4ddbe4`)
- S52: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fde7dfe0-8f54-4351-8f58-6cec4cf3a67d/resource) (`fde7dfe0-8f54-4351-8f58-6cec4cf3a67d`)
- S46: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbc5bbe9-c3fc-4729-bc3a-40364ec26f30/resource) (`cbc5bbe9-c3fc-4729-bc3a-40364ec26f30`)
- S14: [Nb-Ti-IF钢与Ti-IF钢粉化特性对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/351228a1-d795-4b14-921f-abd2d26f5f35/resource) (`351228a1-d795-4b14-921f-abd2d26f5f35`)
- S49: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de84ca07-c975-4b4a-bf7c-ff83767138fb/resource) (`de84ca07-c975-4b4a-bf7c-ff83767138fb`)
- S39: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0d43fd6-6e61-4462-bf56-63125c45e149/resource) (`b0d43fd6-6e61-4462-bf56-63125c45e149`)
- S32: [表2-2 IF钢的化学成分 (wt.%)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e25b742-7881-4556-bb73-56efcdccf185/resource) (`7e25b742-7881-4556-bb73-56efcdccf185`)
- S6: [钢按质量分类的标准示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/299811dc-e729-4b0f-b1de-ab82e5fcabcb/resource) (`299811dc-e729-4b0f-b1de-ab82e5fcabcb`)
- S16: [新型超低碳钢与普通IF钢的成分范围示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/372164b8-064a-468a-aed5-bf0e5dc829f5/resource) (`372164b8-064a-468a-aed5-bf0e5dc829f5`)
- S5: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16eee1b8-9c25-4b88-bf1a-615f9e909a58/resource) (`16eee1b8-9c25-4b88-bf1a-615f9e909a58`)
- S40: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba2ce65d-e02e-49cb-9367-a9677f64d971/resource) (`ba2ce65d-e02e-49cb-9367-a9677f64d971`)
- S36: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c648af7-9b9c-4884-9230-6d5386fee34e/resource) (`8c648af7-9b9c-4884-9230-6d5386fee34e`)
- S2: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03e191ae-8b1c-49e3-b289-8d4ef9dec1b5/resource) (`03e191ae-8b1c-49e3-b289-8d4ef9dec1b5`)
- S3: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a89fd30-8cd6-48f0-85ff-95962dce8a9a/resource) (`0a89fd30-8cd6-48f0-85ff-95962dce8a9a`)
- S7: [continuous casting volume three the application of electromagnetic stirring ems in the continuous casting of steel__7...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b02350c-2bba-438c-8ca5-c2b2adea639d/resource) (`2b02350c-2bba-438c-8ca5-c2b2adea639d`)
- S51: [夹杂物组成、尺寸对不同产品缺陷的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4f66a90-5d7f-4b6e-8217-ab3c67013f90/resource) (`f4f66a90-5d7f-4b6e-8217-ab3c67013f90`)
- S35: [连铸液相穴钢液中非金属夹杂物碰撞长大的数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8af8a531-57bf-4bec-80bd-5218dd5a3df0/resource) (`8af8a531-57bf-4bec-80bd-5218dd5a3df0`)
- S4: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14738322-ebc6-48e9-8898-f7b6eda86eb3/resource) (`14738322-ebc6-48e9-8898-f7b6eda86eb3`)
- S31: [表2-3 连铸参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73aa85b3-a08f-49c6-be7e-61427563a41e/resource) (`73aa85b3-a08f-49c6-be7e-61427563a41e`)
- S30: [图1-27 M-EMS对夹杂物分布和凝固组织的影响机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73871de2-5673-4382-b7c5-02e8a1866456/resource) (`73871de2-5673-4382-b7c5-02e8a1866456`)
- S25: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69306daf-96d0-403b-adb3-05cfb208bb66/resource) (`69306daf-96d0-403b-adb3-05cfb208bb66`)
- S8: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2bf7790e-079d-4539-bc32-881400782be1/resource) (`2bf7790e-079d-4539-bc32-881400782be1`)
- S45: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cba9d87f-a4c7-44d9-bf8a-b6c4fca5f3ea/resource) (`cba9d87f-a4c7-44d9-bf8a-b6c4fca5f3ea`)
- S38: [TextNode6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af9e8e6a-9e86-471b-875a-8fe11a5d29fe/resource) (`af9e8e6a-9e86-471b-875a-8fe11a5d29fe`)
- S26: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6da2882d-308c-457d-9bd3-0ee6227624d8/resource) (`6da2882d-308c-457d-9bd3-0ee6227624d8`)
- S47: [TextNode4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf91836b-5710-4c0a-9a8b-1e412eebc074/resource) (`cf91836b-5710-4c0a-9a8b-1e412eebc074`)
- S12: [TextNode5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3099db0a-a471-434f-94af-96b45e819dd0/resource) (`3099db0a-a471-434f-94af-96b45e819dd0`)
- S17: [钢液铈处理对超大型钢锭中非金属夹杂物的影响及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fb208b6-2a13-4702-a77f-eb18c0927051/resource) (`3fb208b6-2a13-4702-a77f-eb18c0927051`)
- S44: [钢液铈处理对超大型钢锭中非金属夹杂物的影响及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c727ac26-a279-47f1-b413-738aede34799/resource) (`c727ac26-a279-47f1-b413-738aede34799`)
- S10: [汽车覆盖件模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e7fd44e-d763-4110-ab1c-54f615dd5cb9/resource) (`2e7fd44e-d763-4110-ab1c-54f615dd5cb9`)
- S41: [冲压模具制造技术问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf514b84-cc23-4228-9fec-50a361395a98/resource) (`bf514b84-cc23-4228-9fec-50a361395a98`)
- S22: [冲压模具设计手册多任务位级进模](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/548b8edf-c784-42f0-99cb-45b03f2af6af/resource) (`548b8edf-c784-42f0-99cb-45b03f2af6af`)
- S28: [中国模具工程大典 第四卷 冲压模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e8148ed-3c65-498b-9c56-842b7861552b/resource) (`6e8148ed-3c65-498b-9c56-842b7861552b`)
- S42: [中国模具工程大典 第四卷 冲压模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfba4153-d42d-4338-8e3a-21aac7d21318/resource) (`bfba4153-d42d-4338-8e3a-21aac7d21318`)
- S48: [金属塑性成形手册 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d7ee827c-2418-4d34-a361-8cdaaca652cd/resource) (`d7ee827c-2418-4d34-a361-8cdaaca652cd`)