---
version: "v1"
generated_at: "2026-06-18T13:53:32+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 46
  source_quality_score: 0.87
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

TEM微观组织分析是压铸合金微观表征的核心高级技术手段之一，广泛应用于免热处理压铸铝合金、半固态压铸镁/铝合金等压铸体系的纳米析出相、晶界相、缺陷等精细微观结构分析，是光学显微镜（OM）、扫描电子显微镜（SEM）、X射线衍射（XRD）表征手段的重要补充技术[[S47,S17,S48]]。

透射电子显微镜（TEM）以波长极短的电子束作为照明光源，用电磁透镜代替光学透镜来聚焦成像，是一种高分辨率、高放大倍数的分析测试仪器[[S3]]。其最大的特点是能够同时进行材料的组织形貌和晶体结构的同位分析，能够完成光学显微镜、低倍扫描电镜等低倍表征手段无法实现的纳米级析出相精准鉴定、位错组态直接成像、晶界精细结构分析及非平衡快速凝固亚稳相表征，是压铸铝合金、镁合金、锌合金微观机理研究与质量检测的核心高端表征手段[[S3]]。

## 核心原理

### 成像原理

透射电子显微镜以波长极短的电子束为照明源，以磁透镜聚焦成像。其工作原理是：由电子枪发射出来的电子束，在真空通道中沿着镜体光轴穿越聚光镜，通过聚光镜将之会聚成一束尖细、明亮而又均匀的光斑，照射在样品室内的样品上；透过样品后的电子束携带有样品内部的结构信息，经过物镜的会聚调焦和初级放大后，进入下级的中间透镜和投影镜进行综合放大成像，最终被放大了的电子影像投射在观察室内的荧光屏板上[[S42,S28]]。当电子被加速到100 keV时，其波长仅为0.37 nm，为可见光的十万分之一左右，因此用电子束来成像，分辨率大大提高[[S29]]。

电子束与薄压铸金属样品的相互作用可产生多种透射信号，其中穿透样品的透射电子信号由微区厚度、晶体结构及成分共同决定，其质厚效应、衍射效应、衍衬效应可分别用于分析样品形貌、晶体结构取向、内部缺陷等信息[[S15]]。

### 衬度机制

**质厚衬度**：由样品微区的原子序数（质量）差异或厚度差异引发。同厚度下高原子序数区域散射更多电子，同原子序数下厚区域散射更多电子，在明场像中更厚/更高原子序数的区域更暗，在暗场像中衬度相反。该衬度机制适用于非晶样品、复型样品的形貌观察[[S11,S15]]。

**衍射衬度（衍衬）**：由相干弹性散射的布拉格衍射引发。样品不同相邻微区的晶体取向、晶体结构存在差异时，满足布拉格衍射条件的区域衍射束强度存在显著区别，透射束与衍射束强度互补，从而形成图像衬度。该衬度可用于显示压铸金属晶粒形貌、不同第二相的分布状态以及晶体内部的位错、层错等结构缺陷[[S12,S15,S7,S8]]。

## 与其他显微技术的对比

| 特性 | 光学显微镜（OM） | 扫描电镜（SEM） | 透射电镜（TEM） |
|------|------------------|----------------|----------------|
| 分辨率 | 约200 nm | 约1.55~6 nm | 0.12~0.2 nm |
| 成像介质 | 可见光，空气中工作 | 电子束，真空环境 | 电子束，真空环境 |
| 信息维度 | 样品表面微米级形貌 | 表面形貌、原子序数衬度、微区成分 | 纳米级内部形貌、晶体衍射结构、微区原子级成分|
| 制样难度 | 最低 | 低~中等 | 最高 |

TEM的分辨率可达0.1~0.2 nm，比常规扫描电镜高一个数量级，可直接分辨原子面间距级别的精细结构[[S50,S30,S51,S29,S56]]。

> **图示说明**：下图为200倍光学显微镜下的压铸零件微观组织，展示常规OM表征的微米级尺度，辅助对比TEM的纳米级表征能力[[S55]]。
>
> ![200倍金相显微镜下的压铸零件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f81055ed-fd1b-463f-a499-0730aabd281a/resource)

## 在压铸领域的应用目标

TEM在压铸合金研究中主要解决以下问题[[S3]]：

- **纳米析出相鉴定**：精准识别压铸合金时效过程中弥散析出的纳米级亚稳相（如β″、θ′、Q′等），明确不同纳米析出相对合金强度的贡献机制[[S25]]。
- **位错组态分析**：直接观测压铸合金中的位错组态与分布特征[[S10]]。
- **晶界精细结构**：表征晶界处析出相与基体的共格/半共格关系、晶界相的钉扎效应[[S46]]。
- **非平衡亚稳相表征**：观测压铸快凝过程中形成的常规低倍表征无法识别的纳米级亚稳相，完善相转变理论体系[[S2]]。

## 样品制备方法

TEM样品必须满足电子透明的厚度要求，通常需控制在50~200 nm区间[[S43,S53]]。针对压铸合金，常用三种制备方法：

### 电解双喷

用于成分相对均匀的压铸铝、镁类合金。常用电解液为体积分数30%的硝酸甲醇溶液，操作电压范围5~12 V，抛光温度控制在-35℃~-25℃低温环境，制样速度快且无明显机械损伤。主要伪像为表面氧化层，可通过出孔后立即用酒精充分清洗消除[[S21,S60]]。

### 离子减薄

适用于含异相、脆硬相的非均相压铸合金。典型工艺参数：初始减薄阶段采用5 keV离子电压、6°~7°入射角度；快穿孔时将参数调整为2~3 keV离子电压、3°低角度继续减薄15~20 min；样品台保持3 rpm转速，设备真空度控制在5×10⁻⁴ Pa级别[[S6,S33,S24]]。

### FIB（聚焦离子束）制备

可分纳米级特征位置的定点取样，适用含特定缺陷、局部微区的压铸合金样品。通用流程为：先在选定区域表面先后通过电子束、离子束沉积保护层Pt/W，再用30 keV Ga⁺离子铣出两侧沟槽，取出薄片转移至铜网，逐步降低离子束电流和电压最终减薄至电子透明厚度（<200 nm）[[S31,S16,S24]]。主要伪像为Ga离子注入损伤层，可通过最终0.1~1 keV低能离子清修去除[[S24]]。

> **图示说明**：下图为压铸合金TEM制备用FIB系统结构示意图，标注了W沉积层、Cu支撑网、FIB加工方向与TEM观测方向，清晰展示了FIB定向减薄的工作模式[[S27]]。
>
> ![FIB系统结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78ed177f-917f-4c14-bd00-26c291135d2c/resource)

## 关键操作参数与成像模式

### 加速电压与放大倍数

压铸合金TEM分析常用加速电压范围为100~300 kV，主流商用设备常规采用200 kV配置，对应的典型点分辨率为0.18~0.23 nm，可满足压铸合金中纳米析出相、位错、相界面等精细结构的观测需求[[S40,S60]]。放大倍数覆盖从10³倍（对应视场百微米级）到10⁶倍（对应原子尺度观测）的区间，可实现从宏观多相分布统计到单个原子级相结构表征的全尺度覆盖[[S37,S40]]。

### 主要分析模式

| 分析模式 | 功能 | 压铸合金选用原则 |
|----------|------|----------------|
| SAED（选区电子衍射） | 物相晶体结构标定、位向关系测定 | 标定析出相的点阵类型、晶格参数及与基体的位向关系[[S59,S23,S54]] |
| HRTEM（高分辨像） | 原子级晶格排列直接观测 | 观测析出相与基体的共格/半共格界面、纳米相原子排列特征[[S59,S25]] |
| STEM | 亚纳米尺度扫描透射成像 | 结合EDS/EBSD实现亚纳米尺度的元素面分布表征[[S59,S45]] |
| EDS | 原子序数大于11的常规金属元素定量分析 | 微区成分分析[[S59,S20]] |
| EELS | 轻元素、低原子序数元素的高精度检测 | 氧化物、氮化物等夹杂物的成分分析，空间分辨率优于EDS[[S59,S20,S45]] |

## 典型组织信息产出

### 明场像（BF）

通过未散射的透射电子束成像，可清晰观测压铸合金中纳米级析出相的形貌、位错组态、晶界分布等微观组织特征。例如，高真空压铸Al-10Si-Cu-Mg-Mn合金T5处理态中短棒状、板条状纳米析出相的分布状态可通过明场像直观表征[[S43,S25,S53]]。

### 暗场像（DF）

通过选取特定衍射电子束成像，衬度与明场像相反，可提升低体积分数特征相的辨识度，适用于区分压铸合金中与基体衬度差异低的细小析出相、特定位向的晶粒等[[S53]]。

### 选区电子衍射花样（SADP）

可获取微区晶体结构信息，用于确定压铸合金中析出相的点阵类型、晶格参数、相的晶体结构，还可获得析出相与基体的位向关系。例如，压铸Mg-RE合金中不同时效析出相的HCP、FCC晶体结构及与α-Mg基体的共格/半共格取向匹配关系可通过该方法标定[[S23,S54,S25]]。

### 高分辨晶格像（HRTEM）

可直接分辨合金的原子级晶格排列，用于表征压铸合金中纳米析出相与基体的界面共格关系、原子尺度的晶格畸变、层错等精细晶体缺陷[[S25,S53]]。

### STEM元素面分布图

可实现选定微区内各元素的二维分布可视化表征，用于分析压铸合金中溶质元素在析出相、晶界、基体中的偏聚行为。例如，压铸耐热铝合金中Cu、Mg、Si等元素在不同金属间相中的富集分布规律可精准表征[[S44,S9]]。

## 压铸缺陷的TEM表征

采用TEM可识别压铸特有的四类纳米级缺陷[[S18]]：

| 缺陷类型 | TEM表征特征 |
|----------|------------|
| 纳米级气孔 | 可观测孔壁的非平衡凝固枝晶纳米突起特征 |
| 纳米微缩松 | 可识别纳米级连通缝隙的界面衍射衬度差异 |
| 纳米级冷隔界面 | 可分辨厚度仅几十纳米的氧化薄膜层 |
| 纳米氧化夹杂物 | 可通过SAED判定Al₂O₃、MgO等氧化物的晶体结构 |

上述纳米缺陷的精准定性溯源是常规低倍表征手段无法完成的[[S18]]。

## 压铸合金应用案例

### 纳米析出相鉴定——高真空压铸Al-Si-Cu-Mg-Mn合金

高真空压铸Al-10Si-Cu-Mg-Mn合金T5热处理研究中，通过TEM明场像配合HRTEM、快速傅里叶变换（FFT）技术，精准识别出合金中弥散分布的短棒状/板条状纳米亚稳相β″、θ′以及Q′相前驱体C相，明确了不同纳米析出相对合金强度的贡献机制[[S25]]。

### 共格相与高温性能——AX系耐热压铸镁合金

AX系列耐热压铸镁合金研究中，通过TEM观测确认晶界处与铝基体完全共格的高热稳定性相(Mg,Al)₂Ca，该相可有效钉扎晶界、抑制镁合金高温服役过程中的晶界滑动，解释了该系列压铸镁合金优异的高温抗蠕变性能来源[[S46]]。

### 位错组态与微合金化强化——半固态压铸Mg-Zn-Gd合金

半固态流变压铸Mg-5Zn-xGd-0.6Zr合金研究中，采用TEM直接观测合金中的位错组态、纳米尺度Gd富集析出相的分布特征，阐明了Gd元素微合金化提升该压铸镁合金力学性能的微观机理[[S10]]。

## 局限性与注意事项

| 局限性 | 说明 |
|--------|------|
| 样品尺寸限制 | 待测区域需为电子透明厚度（50~200 nm），高原子序数合金可容许的样品厚度进一步降低[[S43,S53]] |
| 电子束损伤 | 高能入射电子轰击样品时会引入空位、点缺陷等辐照损伤，改变原本的微观组织状态，高原子序数合金受该效应影响更为显著[[S19]] |
| 统计代表性不足 | 单次观测视场极小，2004年全球所有TEM累计检测的金属总测试体积仅约0.7 mm³，局部小范围观测结果难以代表压铸构件的整体组织特征[[S19]] |
| 图像解释多解性 | TEM呈现的是三维样品经全厚度投影后的二维图像，不同深度位置的相、缺陷会发生投影重叠，容易导致误判[[S19]] |

## 与其他表征技术的互补关系

压铸合金常用五类表征技术的特征对比如下：

| 表征技术 | 分辨率 | 主要信息类型 | 检测范围 | 制样难度 |
|----------|--------|-------------|----------|----------|
| OM | 0.1~0.2 μm | 宏观晶粒形貌、微米级第二相分布 | 毫米级 | 最低 |
| SEM | 1~1.5 nm | 亚微米级第二相形貌、微区点/面成分分布 | 微米~毫米级 | 低~中 |
| EBSD | 侧向10 nm | 晶粒取向、织构分布、晶界类型统计 | 表层10 nm以内 | 中 |
| XRD | 无微区成像分辨率 | 全域物相组成、平均晶格参数、宏观织构 | 毫米~厘米级 | 较低 |
| TEM | 0.12~0.2 nm | 纳米/原子级析出相形貌、晶体结构、位错组态、界面共格关系、微区元素分布 | 纳米~数微米级 | 最高 |

针对压铸合金的表征流程，通常先采用OM和XRD获得宏观全域的组织与物相基础信息，再采用SEM/EBSD完成亚微米尺度的形貌、成分、晶粒取向统计分析，最终选用TEM针对目标微区开展纳米/原子级的精细表征。不同技术的观测尺度、分析能力相互补充，可构建从宏观到微观的全维度压铸合金组织表征体系[[S32,S4,S38,S1,S19]]。

## Sources
- S47: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3c32e0d-af22-4af7-9f8e-3b5d7f62bb28/resource) (`d3c32e0d-af22-4af7-9f8e-3b5d7f62bb28`)
- S17: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52185873-da3f-4ef3-a9a9-06f4cd8847ff/resource) (`52185873-da3f-4ef3-a9a9-06f4cd8847ff`)
- S48: [Mg-3Sm-0.5Zn-0.4Zr合金的高温蠕变机制和组织演变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6314a40-5c9d-4d52-9ea4-f7e1d0c5c633/resource) (`d6314a40-5c9d-4d52-9ea4-f7e1d0c5c633`)
- S3: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/110640a0-e263-48cc-a85e-10c9e36f9441/resource) (`110640a0-e263-48cc-a85e-10c9e36f9441`)
- S42: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b14ebfcb-0ed2-4d87-aca8-ee6917c5019d/resource) (`b14ebfcb-0ed2-4d87-aca8-ee6917c5019d`)
- S28: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ccf3ae3-5868-40e3-80da-3f1ea1018db3/resource) (`7ccf3ae3-5868-40e3-80da-3f1ea1018db3`)
- S29: [金属表面处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7fe79ebe-a154-4f2c-bbcf-1fa28b093b0f/resource) (`7fe79ebe-a154-4f2c-bbcf-1fa28b093b0f`)
- S15: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a101d21-7c3d-4afd-86c1-3e205d97a981/resource) (`4a101d21-7c3d-4afd-86c1-3e205d97a981`)
- S11: [complex metallic alloys fundamentals and applications__9544bf64ae](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e7247b8-6d93-4d65-abc5-8ece48ca9b93/resource) (`3e7247b8-6d93-4d65-abc5-8ece48ca9b93`)
- S12: [complex metallic alloys fundamentals and applications__9544bf64ae](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e9ad259-2fed-4355-856d-351298969ad3/resource) (`3e9ad259-2fed-4355-856d-351298969ad3`)
- S7: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28359469-ce0a-4073-9829-1a7f5c9b7ab5/resource) (`28359469-ce0a-4073-9829-1a7f5c9b7ab5`)
- S8: [effect of disorder and defects in ion implanted semiconductors electrical and physicochemical characterization__09b14...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2eba88df-f448-4419-ba25-810069cded76/resource) (`2eba88df-f448-4419-ba25-810069cded76`)
- S50: [光学显微镜、扫描电子显微镜与透射电子显微镜对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dedc4bbd-aabb-4964-81c1-f82e1e64ffa7/resource) (`dedc4bbd-aabb-4964-81c1-f82e1e64ffa7`)
- S30: [光学显微镜、扫描电子显微镜与透射电子显微镜的比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8079cdfc-8ffd-45cc-b26f-f44c494543b1/resource) (`8079cdfc-8ffd-45cc-b26f-f44c494543b1`)
- S51: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5865418-ccc4-4fb2-9ce6-eeb72924f131/resource) (`e5865418-ccc4-4fb2-9ce6-eeb72924f131`)
- S56: [表面沉积技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8b1899a-8d41-4931-a582-397c05d10baf/resource) (`f8b1899a-8d41-4931-a582-397c05d10baf`)
- S55: [200倍金相显微镜下的压铸零件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f81055ed-fd1b-463f-a499-0730aabd281a/resource) (`f81055ed-fd1b-463f-a499-0730aabd281a`)
- S25: [T5处理对高真空压铸Al-10Si-Cu-Mg-Mn合金组织影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75eb76b7-3edb-47da-bfed-d6e098104fb6/resource) (`75eb76b7-3edb-47da-bfed-d6e098104fb6`)
- S10: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/368e475c-7966-4237-b348-db69f2173bad/resource) (`368e475c-7966-4237-b348-db69f2173bad`)
- S46: [先进镁合金制备与加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3215a30-edb1-408d-81d7-54ecb6d4d011/resource) (`d3215a30-edb1-408d-81d7-54ecb6d4d011`)
- S2: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03096f1b-db0a-4310-ad0c-ba1515774561/resource) (`03096f1b-db0a-4310-ad0c-ba1515774561`)
- S43: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfcbfb06-999a-47b4-b871-f2aba1b711b6/resource) (`bfcbfb06-999a-47b4-b871-f2aba1b711b6`)
- S53: [超大规模集成电路衬底材料性能及加工测试技术工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f22957b8-bc6e-4605-a11b-4f5fff46e902/resource) (`f22957b8-bc6e-4605-a11b-4f5fff46e902`)
- S21: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c4c77fd-83cb-4c5e-9628-3cce43a94170/resource) (`5c4c77fd-83cb-4c5e-9628-3cce43a94170`)
- S60: [effect of cu addition on microstructures and tensile properties of high__15b7a22a5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd1ca4a4-daaa-4381-be7b-0ebe64a0dfda/resource) (`fd1ca4a4-daaa-4381-be7b-0ebe64a0dfda`)
- S6: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f5411d6-1a1b-4089-ad91-9895b6f56414/resource) (`1f5411d6-1a1b-4089-ad91-9895b6f56414`)
- S33: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/926bdadc-f7c6-4b61-85cf-31e960f471d4/resource) (`926bdadc-f7c6-4b61-85cf-31e960f471d4`)
- S24: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72cc6b73-d884-4c41-9469-6789eefdaf5c/resource) (`72cc6b73-d884-4c41-9469-6789eefdaf5c`)
- S31: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89a8a185-135c-41fa-90ad-700a06417717/resource) (`89a8a185-135c-41fa-90ad-700a06417717`)
- S16: [carbon alloys novel concepts__44fdd170cc](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b6f9ff8-905d-470a-a288-d6befd73f9d7/resource) (`4b6f9ff8-905d-470a-a288-d6befd73f9d7`)
- S27: [Fig.11 Schematic diagram of the FIB system](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78ed177f-917f-4c14-bd00-26c291135d2c/resource) (`78ed177f-917f-4c14-bd00-26c291135d2c`)
- S40: [超大规模集成电路衬底材料性能及加工测试技术工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8599460-c5dc-4962-bab9-3225d914b939/resource) (`a8599460-c5dc-4962-bab9-3225d914b939`)
- S37: [Table 9.4: Magnification Calibration for a Phillips EM400T at 120 kV](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9bd5cba6-1ec0-4826-9145-92b44e58edf9/resource) (`9bd5cba6-1ec0-4826-9145-92b44e58edf9`)
- S59: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc6d987d-4607-4856-b891-23fdc7bb51ea/resource) (`fc6d987d-4607-4856-b891-23fdc7bb51ea`)
- S23: [Mg-3Sm-0.5Zn-0.4Zr合金的高温蠕变机制和组织演变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65123203-01e0-4935-84dd-7ffc34e8504c/resource) (`65123203-01e0-4935-84dd-7ffc34e8504c`)
- S54: [alsicunimg系铸造耐热铝合金组织及其高温性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6e488ec-be28-48d9-b268-d680f526ee27/resource) (`f6e488ec-be28-48d9-b268-d680f526ee27`)
- S45: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc5f3a1d-d6a7-4e74-bb0a-dc231d0a4b9e/resource) (`cc5f3a1d-d6a7-4e74-bb0a-dc231d0a4b9e`)
- S20: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c1d3896-f147-4d77-96de-c071543fa40f/resource) (`5c1d3896-f147-4d77-96de-c071543fa40f`)
- S44: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9f18e0d-26be-4f79-9338-cf00d2e5a2cf/resource) (`c9f18e0d-26be-4f79-9338-cf00d2e5a2cf`)
- S9: [developing a die casting magnesium alloy with excellent mechanical perfo__81e986a15a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ffa9ba3-47f3-48e8-9e38-5cc5481712bf/resource) (`2ffa9ba3-47f3-48e8-9e38-5cc5481712bf`)
- S18: [真空压铸无缸套铝合金气缸体缸孔铸造缺陷调查_韩洁丽](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55873130-e1e2-45d0-a95a-8ef07b13e0f7/resource) (`55873130-e1e2-45d0-a95a-8ef07b13e0f7`)
- S19: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ab0c282-1a94-4b19-8aa8-bd4950a93346/resource) (`5ab0c282-1a94-4b19-8aa8-bd4950a93346`)
- S32: [2195铝合金的制备与表征流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a082f13-c479-4f51-8cbc-3f049852ebd4/resource) (`8a082f13-c479-4f51-8cbc-3f049852ebd4`)
- S4: [表面机械研磨处理后样品晶粒尺寸沿厚度方向的变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/110d091a-c266-4f8a-b58f-529cb86dd95d/resource) (`110d091a-c266-4f8a-b58f-529cb86dd95d`)
- S38: [超声熔体处理和Al-Ti-B协同作用下Al-Cu合金的显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ffcb976-16de-4060-8fdf-a7438ea7fa94/resource) (`9ffcb976-16de-4060-8fdf-a7438ea7fa94`)
- S1: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0145eb27-8393-47ea-804d-ccf579a0ba51/resource) (`0145eb27-8393-47ea-804d-ccf579a0ba51`)