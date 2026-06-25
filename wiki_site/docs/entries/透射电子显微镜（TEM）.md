---
version: "v1"
generated_at: "2026-06-18T12:12:32+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 51
  source_quality_score: 0.85
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

透射电子显微镜（Transmission Electron Microscope，TEM）是面向材料微观结构表征的高分辨率分析仪器。其核心原理为：在真空环境下，经高压加速的高能电子束穿透厚度为数十至数百纳米的电子透明试样，借助电磁透镜聚焦，利用透射电子与散射电子携带的结构信息成像，可观测到亚纳米甚至原子级别的晶体结构、位错、析出相等特征[[S53,S29,S39]]。TEM在压铸铝合金、镁合金、锌合金等材料的组织分析、析出相鉴定、缺陷溯源及界面表征中具有不可替代的技术价值。

## 工作原理与成像模式

### 基本成像原理

当一束高能电子投射到薄晶体试样时，一部分电子直接透过形成透射束，另一部分受晶面布拉格衍射作用偏转形成衍射束。二者之间存在强度分布差异，这是图像衬度的基本来源[[S53]]。透过试样的电子束携带有样品内部的结构信息，经物镜会聚调焦和初级放大后，再经中间镜和投影镜综合放大，最终在荧光屏上形成可见影像[[S39]]。

### 主要成像模式

TEM成像模式主要分为明场像、暗场像和高分辨像三类，选择逻辑见下表[[S53,S42,S52]]：

| 成像模式 | 光阑位置 | 参与成像的电子束 | 衬度机制 | 典型应用 |
|---------|---------|----------------|---------|---------|
| 明场像（BF） | 物镜光阑套在中心透射斑点上 | 仅透射电子 | 质厚衬度、衍射衬度 | 组织形貌、位错、缺陷观察 |
| 暗场像（DF） | 物镜光阑套在指定衍射斑点上 | 仅该衍射束 | 与明场像互补 | 特定取向晶粒、第二相辨识 |
| 高分辨像（HRTEM） | 选取透射束与至少一束衍射束 | 多束电子干涉 | 相位衬度 | 晶格排列、原子级结构观测 |

明场像中，试样中厚度较大、原子序数较高的区域对电子散射更多，在图像上亮度更低[[S53]]。暗场像的图像衬度与明场像正相反，实际操作中可通过偏转入射电子束使衍射束沿物镜光轴入射，获得衬度更优的中心暗场像[[S42]]。高分辨像是透射束与衍射束发生干涉形成的相位衬度像，可直接显示材料的晶格排列特征[[S52,S38,S35]]。

![TEM不同成像模式工作原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7545f8ef-4bdf-4445-815e-8a808e948dc9/resource)

该示意图展示了透射电子显微镜三类基础成像模式（明场、暗场、高分辨）的光路结构，标注了电子束入射与不同模式的物镜调整方式[[S26]]。

### 衍射模式

调整中间镜将成像平面切换到物镜后焦面，即可获得电子衍射花样。单晶体对应规则排列的衍射斑点，多晶体或非晶试样对应同心衍射环，可用于晶体结构、取向及点阵常数的标定[[S42]]。

## 设备分类

### 常规TEM

以质厚衬度和衍射衬度成像为主，可实现显微组织形貌观察和选区电子衍射分析[[S53]]。

### 高分辨TEM（HRTEM）

HRTEM是配置低球差高分辨物镜极靴、适配高相干性电子源的TEM。通过相位衬度成像直接获得原子级别的晶格排列图像，可分辨材料中单个原子层的分布特征，适配厚度小于20 nm的弱相位体试样[[S52,S38]]。

### 扫描透射TEM（STEM）

STEM的工作模式是将聚焦至亚纳米级的电子探针在试样表面逐点扫描，通过不同位置的探测器收集透射信号。其中，环形探测器采集高角度散射电子获得的图像为Z衬度像，像点亮度直接对应原子序数的平方，可实现无需解析的直观原子分布观察[[S33,S49]]。

![STEM明场与环形暗场成像系统示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/feacc316-ab76-4ab6-81ca-62cf2b53e163/resource)

该示意图展示了STEM两种成像模式（明场BF与环形暗场ADF）的光路结构，标注入射电子束、试样与对应探测器的位置关系，辅助说明Z衬度成像的实现方式[[S56]]。

### 分析型TEM

在基础TEM上集成EDS（能量色散X射线谱）和EELS（电子能量损失谱）谱学模块，可在纳米甚至原子空间分辨尺度下同步获得微区元素组成、电子结构及元素分布面扫信息，适配界面、析出相等精细微区的联合表征[[S33]]。

### 原位TEM

在设备中集成功能化原位试样台的TEM，可在观测过程中同步对试样施加加热、拉伸、通入气氛等外场条件，实时记录材料相变、位错运动、界面反应等动态过程。典型双倾加热台可实现800～1000 ℃温度范围的动态观测[[S35,S30]]。

## 主要构成

TEM的主体结构由照明系统、成像系统、观察与记录系统、真空系统和电器系统组成[[S39]]：

- **电子枪**：分为热发射电子枪（钨丝、LaB₆灯丝）和场发射电子枪两类。热发射枪成本低，场发射枪电子源尺寸更小、相干性和亮度更高，主要用于高端高分辨型号[[S39]]。
- **聚光镜**：将电子枪发射的电子束会聚成束流稳定、光斑均匀的平行入射光斑，可切换平行照明和汇聚探针照明两种模式[[S39,S34]]。
- **物镜**：TEM成像系统的核心，承担试样透射信号的第一次聚焦与放大，其球差系数直接决定设备的分辨率上限。物镜后焦面位置的物镜光阑用于选择参与成像的透射束或衍射束[[S39,S34]]。
- **中间镜与投影镜**：完成综合放大成像[[S39]]。

## 关键参数

常规商用材料分析用TEM的电子加速电压主流取值范围为100～400 kV，其中200 kV级别的场发射TEM典型点分辨率可达0.23 nm，高端设备分辨率可低至0.18～0.2 nm[[S32,S53]]。

## 样品制备

金属材料常规TEM试样的厚度要求一般为50～500 nm，优先通过机械预减薄、双喷电解减薄或离子减薄的方式制备获得电子透明的薄区；对于特定微区的定位试样，可采用聚焦离子束（FIB）加工制备[[S7,S25,S42]]。

### 压铸铝合金常规制备流程

采用线切割或电火花切割从大块压铸坯料上切下0.2～0.3 mm厚薄片，经砂纸手工减薄或化学减薄至几十微米，最终用电解双喷设备或离子减薄仪完成终减薄。合格试样需满足电子透明、完整保留原始大块压铸材料的组织结构、具备足够强度和刚度、大尺寸透明区域的要求[[S37]]。

### 压铸镁合金离子减薄工艺

以Mg-4Al-5RE-xGd压铸镁合金为例，标准制备工艺为：切取0.4～0.5 mm厚试样，用150目砂纸机械研磨至100～200 μm，冲出直径3 mm圆片后用1200目砂纸磨至约40 μm，最后采用Gatan Model 695离子减薄仪完成终减薄。核心操作参数为[[S7]]：

| 操作参数 | 初始阶段 | 终穿孔阶段 |
|---------|---------|-----------|
| 样品室真空度 | 5×10⁻⁴ Pa | 5×10⁻⁴ Pa |
| 样品台转速 | 3 rpm | 3 rpm |
| 离子枪电压 | 5 keV | 2 keV |
| 离子束与样品夹角 | 7° | 3° |

### FIB精准定位取样

聚焦离子束（FIB）制备压铸合金TEM试样的典型操作流程为：在集成低电压成像电子枪、30 kV Ga³⁺离子枪的SEM腔室内，先对待取样微区预先沉积保护性Pt层，先后铣削目标区域两侧凹槽，从底部铣断薄片与基体的连接，使用纳米探针将薄试样取出并转移至TEM栅格上，逐步降低离子束电流对薄片两侧逐步减薄，最终获得厚度约200 nm的电子透明区域，最后采用0.1～1 kV的低电压离子束做表面清洗去除高能离子引入的辐照损伤[[S15,S34]]。该方法可实现对裂纹尖端、特定第二相等指定微区的精准定位取样，尤其适配压铸多相共存合金、涂层与基体界面类特殊微区的取样需求[[S15]]。

### 压铸多相合金减薄优化要点

针对压铸合金多相共存、不同相离子溅射速率差异大、软相易发生机械变形的特点，在试样即将穿孔阶段将离子枪电压从常规5～6 kV降至2～3 kV，离子束夹角从常规7°～10°降至3°左右，既可避免高压高角度离子轰击造成的软相变形、硬相过度溅射剥落，同时可扩大有效电子透明薄区的尺寸[[S7,S40]]。

## 在压铸领域中的应用

### 微观组织分析

#### α-Al枝晶亚结构

TEM可分辨压铸凝固过程中形成的两类α-Al晶粒的亚结构差异：压室预结晶的粗大α₁-Al晶粒内部的位错分布特征和亚晶界细节，以及充型快速冷却条件下形成的细小圆整α₂-Al晶粒的内部缺陷密度，直接揭示压铸非平衡快速凝固过程对α-Al枝晶亚结构的调控作用[[S51]]。

#### 共晶硅形貌

经稀土变质处理的压铸Al-Si合金共晶硅的TEM精细表征结果显示：变质后的共晶硅全部界面为圆弧状非晶面，不再以传统小平面机制生长；可观测到共晶硅内部高密度的层错线，层错线与Si晶体<100>生长方向夹角为20～40°，未发现孪晶线，表明变质后共晶硅的生长机制从传统TPRE孪晶机制转变为金属型连续长大机制[[S4]]。

#### 金属间化合物相鉴定

高真空压铸Al-10Si-Cu-Mg-Mn合金铸态分析实例：结合TEM形貌观测、EDS能谱分析和选区电子衍射标定，可准确识别分布在晶界和Al-Si共晶区的三类金属间化合物[[S51]]：

| 物相 | 化学式 | 外观特征 | 分布位置 |
|------|--------|---------|---------|
| α-Fe相 | α-Al₁₅(Fe,Mn)₃Si₂ | 深灰色粒状 | 晶界、共晶区 |
| Q相 | Q-Al₅Cu₂Mg₈Si₆ | 灰白色层片状 | 晶界、共晶区 |
| θ相 | θ-Al₂Cu | 亮白色，粒状至块状 | 晶界、共晶区 |

此外，随Cu含量增加，θ相从分散粒状逐步聚集粗化为块状[[S51]]。

### 时效析出相分析

#### 压铸Al-Si-Cu-Mg合金

半固态/压铸过共晶Al-Si-Cu-Mg合金时效阶段的亚稳析出相可通过沿<001>Al入射方向的TEM清晰观测[[S43,S36]]：

- **时效初期**：基体中出现点状GP区。
- **峰时效阶段**：大量沿<001>Al方向析出的针状亚稳相β″，对应选区衍射斑点可见特征"十"字辉纹，同时可同步识别θ″亚稳相和短棒状Q′亚稳相。
- **过时效阶段**：亚稳相逐步粗化长大，向平衡稳定相转变。

高真空压铸Al-10Si-Cu-Mg-Mn合金T5时效后，沿[001]Al方向的TEM明场像结合HRTEM和快速傅里叶变换（FFT）标定，可识别出弥散分布的三类纳米亚稳析出相：短棒状的β″相、板条状的θ′相和颗粒状的Q′前驱C相，其中β″相和θ′相是该类压铸铝合金的核心强化相[[S28]]。

#### GP区形貌特征

- **Al-Cu系合金**：GP区呈圆片状，直径约5～10 nm，厚度仅几个原子层。TEM明场像中GP区对应位置呈现深色线条，周边暗色区域为GP区引发的晶格应变场[[S11,S5]]。
- **Al-Mg-Si系合金**：GPI区是室温～150 ℃区间形成的圆形原子团簇，尺寸仅1～2 nm；GPII区（即θ″相）是出现在{111}Al晶面上的薄层状团簇，厚度仅几个原子层，尺寸可达数十纳米，GPII区周边的共格应变场覆盖范围远大于GPI区[[S12]]。

![压铸铝合金时效析出相TEM明场像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f225ac7-e3da-4a77-8da3-7939418239ff/resource)

该TEM明场像展示AA2195压铸铝合金经3%预变形、150 ℃时效30 h后的析出相分布，晶界及晶内可见板条状T1相与θ′析出相[[S16]]。

### 界面分析

通过HRTEM结合选区电子衍射（SAED），可直接测定两相界面的点阵错配度、晶体学位向关系，判定界面为共格（错配度δ < 5%）、半共格还是非共格状态，并可定量分析界面位错间距、界面元素扩散层厚度，揭示压铸合金中第二相与基体的界面结合状态及析出相钉扎晶界的作用机理[[S13,S3,S19]]。

压铸工件表面耐磨/耐蚀涂层与基体界面的TEM表征采用FIB精准截取界面微区后，通过TEM明场像、高分辨成像、配套的EDS线扫描/面扫描，可清晰观测界面处的元素扩散行为、界面金属间化合物的生成种类与厚度，判定界面是否存在微裂纹、孔隙等冶金缺陷[[S15,S22]]。

### 缺陷分析

针对压铸试样的气孔/缩松周边微区，采用FIB精准从缺陷边缘取样后，通过TEM可清晰观测缺陷周边基体的位错组态、微裂纹萌生与扩展路径，精准识别缺陷位置的夹杂物成分与物相类型，揭示压铸热裂纹萌生和扩展的微观诱因，验证夹杂物/脆性第二相作为裂纹萌生源的作用机制[[S23,S44,S24]]。

## Talos F200XG2

### 可检索参数

赛默飞（Thermo Fisher）官方公开的Talos F200XG2完整技术参数（标准加速电压范围、标配硬件包含Super-X EDS系统、STEM探测器配置的官方说明）可检索公开证据不足[[S45,S10]]。同样，"原位多功能"的官方明确定义以及配套加热/力学拉伸/气相反应/电学测试原位附件的具体配置信息的可检索公开证据也不足[[S54,S8]]。

### 同系列公开信息

已公开发表的同系列Talos F200型号TEM配套有FEI Super X EDS系统，可用于微区成分分析[[S31]]。

![Thermo Fisher Talos F200系列透射电子显微镜](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfa09f42-44c1-4e93-aa51-8621280a782a/resource)

该图来自公开的高强半固态铝合金研究文献，展示了FEI/Thermo Fisher品牌Talos F200X透射电子显微镜在材料实验室中的实体外观[[S41]]。

### 压铸相关应用实例

Talos F200XG2在压铸合金研究中的已公开发表应用实例为：在真空压铸Cu-Ni-Si-Cr合金的微观组织与性能研究中，该设备被用于对压铸态、时效态合金的微观形貌与微区成分开展表征分析[[S48]]。

同系列Talos F200系列TEM在压铸合金领域的已公开非原位应用记录包括[[S20,S17]]：

- Mg-4Al-5RE-xGd压铸镁合金组织性能研究中使用Talos F200X开展显微组织观测（配套采用Gatan Model 695离子减薄仪制备TEM样品）。
- 热处理对Mg-10Gd-1.9Y-1Zn-0.5Zr铸造镁合金显微组织影响的研究中，使用FEI Talos F200X对铸态、固溶态和时效态合金开展表征，完成第二相鉴定、元素含量测试、LPSO相及时效析出β系列相的形貌与致密度分析。

现有公开可检索文献中，未找到采用Talos F200XG2开展原位加热/力学加载等动态测试，针对压铸铝合金析出相动态演变或加载过程中位错运动进行观测的已发表研究实例，该部分相关证据不足[[S21,S27]]。

## 与其他表征手段的关系

### 与SEM对比

TEM相较于SEM的不可替代优势在于可实现亚埃至原子级别的空间分辨率，可同步获得微区的晶体结构、位错组态、原子排列信息；SEM以表面形貌观测为主，常规分辨率仅为1 nm左右，无法直接观测内部晶格结构[[S46,S47,S50]]。TEM的局限性在于试样制备难度远高于SEM，要求试样为电子透明（厚度一般小于200 nm），常规观测视场极小，无法直接获得宏观统计结果[[S46,S47]]。

### 与XRD对比

TEM相较于XRD的不可替代优势在于可实现纳米级甚至原子级的微区单晶结构分析，可获得单个析出相、单个晶粒的结构信息；XRD是全局统计的多晶平均结果，仅能获得大量晶粒平均后的物相信息。TEM的局限性为无法实现宏观大体积试样的整体统计分析，试样制备要求高，对无定形材料的定量分析难度远高于XRD[[S1,S18]]。

## Sources
- S53: [超大规模集成电路衬底材料性能及加工测试技术工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f22957b8-bc6e-4605-a11b-4f5fff46e902/resource) (`f22957b8-bc6e-4605-a11b-4f5fff46e902`)
- S29: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ccf3ae3-5868-40e3-80da-3f1ea1018db3/resource) (`7ccf3ae3-5868-40e3-80da-3f1ea1018db3`)
- S39: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b14ebfcb-0ed2-4d87-aca8-ee6917c5019d/resource) (`b14ebfcb-0ed2-4d87-aca8-ee6917c5019d`)
- S42: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfcbfb06-999a-47b4-b871-f2aba1b711b6/resource) (`bfcbfb06-999a-47b4-b871-f2aba1b711b6`)
- S52: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5652b6c-1673-4898-ac34-b9c80ee04a22/resource) (`e5652b6c-1673-4898-ac34-b9c80ee04a22`)
- S38: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a74f142c-adaf-4e4f-b6ac-3109071371ab/resource) (`a74f142c-adaf-4e4f-b6ac-3109071371ab`)
- S35: [alloy physics a comprehensive reference__0572c6adf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8fa8e9a8-46f7-4d72-922e-fb9d9042404b/resource) (`8fa8e9a8-46f7-4d72-922e-fb9d9042404b`)
- S26: [透射电子显微镜（TEM）中的不同成像模式示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7545f8ef-4bdf-4445-815e-8a808e948dc9/resource) (`7545f8ef-4bdf-4445-815e-8a808e948dc9`)
- S33: [alloy physics a comprehensive reference__0572c6adf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/864db5d6-bbdd-48d0-9ef7-d05db9a5812f/resource) (`864db5d6-bbdd-48d0-9ef7-d05db9a5812f`)
- S49: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce3af02-8ca4-49e7-9425-0c5cf34b25ac/resource) (`dce3af02-8ca4-49e7-9425-0c5cf34b25ac`)
- S56: [STEM的明场（BF）与环形暗场（ADF）成像系统示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/feacc316-ab76-4ab6-81ca-62cf2b53e163/resource) (`feacc316-ab76-4ab6-81ca-62cf2b53e163`)
- S30: [alloy physics a comprehensive reference__0572c6adf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7fd1c8e0-6bbe-4d0b-9858-3ba3b83f7408/resource) (`7fd1c8e0-6bbe-4d0b-9858-3ba3b83f7408`)
- S34: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89a8a185-135c-41fa-90ad-700a06417717/resource) (`89a8a185-135c-41fa-90ad-700a06417717`)
- S32: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/859da1cf-d29f-4923-b28f-b40f4a200f6a/resource) (`859da1cf-d29f-4923-b28f-b40f4a200f6a`)
- S7: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f5411d6-1a1b-4089-ad91-9895b6f56414/resource) (`1f5411d6-1a1b-4089-ad91-9895b6f56414`)
- S25: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72cc6b73-d884-4c41-9469-6789eefdaf5c/resource) (`72cc6b73-d884-4c41-9469-6789eefdaf5c`)
- S37: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6e138b9-9db4-4d2a-b972-daedadb50dbd/resource) (`a6e138b9-9db4-4d2a-b972-daedadb50dbd`)
- S15: [carbon alloys novel concepts__44fdd170cc](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b6f9ff8-905d-470a-a288-d6befd73f9d7/resource) (`4b6f9ff8-905d-470a-a288-d6befd73f9d7`)
- S40: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba5eaca3-99d7-4f4a-bd86-45d74b4ff80d/resource) (`ba5eaca3-99d7-4f4a-bd86-45d74b4ff80d`)
- S51: [T5处理对高真空压铸Al-10Si-Cu-Mg-Mn合金组织影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e155de4b-96fd-417e-a09b-6b5e1d5d82ca/resource) (`e155de4b-96fd-417e-a09b-6b5e1d5d82ca`)
- S4: [稀土在铝合金中的行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1187260a-ba8b-4706-8d24-f98e451b7c43/resource) (`1187260a-ba8b-4706-8d24-f98e451b7c43`)
- S43: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce639175-277d-4800-b21c-15c6be3b5314/resource) (`ce639175-277d-4800-b21c-15c6be3b5314`)
- S36: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5424a2b-e8a5-4e4f-8b01-dfe4017e9c7c/resource) (`a5424a2b-e8a5-4e4f-8b01-dfe4017e9c7c`)
- S28: [T5处理对高真空压铸Al-10Si-Cu-Mg-Mn合金组织影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75eb76b7-3edb-47da-bfed-d6e098104fb6/resource) (`75eb76b7-3edb-47da-bfed-d6e098104fb6`)
- S11: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3446542f-707b-4934-bd74-f560736d28de/resource) (`3446542f-707b-4934-bd74-f560736d28de`)
- S5: [2155556_GP区](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1538bf38-f1fc-404f-94e1-8912d1e43b8c/resource) (`1538bf38-f1fc-404f-94e1-8912d1e43b8c`)
- S12: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ba7154d-77c2-4fa6-af0b-348b375a3bbc/resource) (`3ba7154d-77c2-4fa6-af0b-348b375a3bbc`)
- S16: [AA2195铝合金3%变形、150℃时效30h后的TEM明场像，显示T1和θ'析出相在晶界及晶内的形核](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f225ac7-e3da-4a77-8da3-7939418239ff/resource) (`4f225ac7-e3da-4a77-8da3-7939418239ff`)
- S13: [TiB2_205A铝基复合材料组织性能及制动盘液态模锻成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4188f603-35fb-466c-bb5d-ee1883e2b8cb/resource) (`4188f603-35fb-466c-bb5d-ee1883e2b8cb`)
- S3: [振动和稀土Gd对消失模铸造镁_铝双金属界面的调控及强化机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07a98ad4-5905-40de-b936-b0200b56db2a/resource) (`07a98ad4-5905-40de-b936-b0200b56db2a`)
- S19: [Ti颗粒增强AZ81基复合材料的制备及组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55e9b53e-2f60-46fc-93f2-495308b9ad22/resource) (`55e9b53e-2f60-46fc-93f2-495308b9ad22`)
- S22: [智能制造与机器人理论及技术研究丛书 复杂金属零件热等静压整体成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67294644-3ae2-493a-a891-e77a467f711c/resource) (`67294644-3ae2-493a-a891-e77a467f711c`)
- S23: [真空压铸铝合金发动机缸体缺陷与热处理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6eb7ba71-58dc-4792-93c5-516bb1018cd7/resource) (`6eb7ba71-58dc-4792-93c5-516bb1018cd7`)
- S44: [压铸ADC12铝合金手机中框热裂分析及解决措施](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cfb2c570-72c9-4990-a0e2-f0fdf8280f97/resource) (`cfb2c570-72c9-4990-a0e2-f0fdf8280f97`)
- S24: [激光粉末床熔融制备316L不锈钢及其抗腐蚀性能研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fe1e225-8314-46f1-a763-7de59117c798/resource) (`6fe1e225-8314-46f1-a763-7de59117c798`)
- S45: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d35e1b38-cae2-440d-91af-defeb8b03c0e/resource) (`d35e1b38-cae2-440d-91af-defeb8b03c0e`)
- S10: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31acf6a0-95d6-47b3-83df-a6a9f43d95f3/resource) (`31acf6a0-95d6-47b3-83df-a6a9f43d95f3`)
- S54: [aluminum recycling and processing for energy conservation and sustainability__c9cc743f4e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2b9493e-bdae-40b0-b93f-3289811feba6/resource) (`f2b9493e-bdae-40b0-b93f-3289811feba6`)
- S8: [aluminum recycling and processing for energy conservation and sustainability__e2106648bb](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fb6098a-89a6-4008-8f61-cb09878e1118/resource) (`1fb6098a-89a6-4008-8f61-cb09878e1118`)
- S31: [complex concentrated alloys ccas__861b70e9c9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84ba2d55-448e-4397-ac0a-3304d5e0375c/resource) (`84ba2d55-448e-4397-ac0a-3304d5e0375c`)
- S41: [图2-12 透射电子显微镜 FEI Talos F200X](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfa09f42-44c1-4e93-aa51-8621280a782a/resource) (`bfa09f42-44c1-4e93-aa51-8621280a782a`)
- S48: [真空压铸Cu-Ni-Si-Cr合金微观组织及性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dac78760-0e74-4b2e-9242-3f9555347193/resource) (`dac78760-0e74-4b2e-9242-3f9555347193`)
- S20: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64b0c68e-4c4b-459e-9203-20990db0768d/resource) (`64b0c68e-4c4b-459e-9203-20990db0768d`)
- S17: [热处理对Mg-10Gd-1.9Y-1Zn-0.5Zr铸造镁合金显微组织和力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5060dea4-834a-4e88-b5ca-6d8f24c1bfb8/resource) (`5060dea4-834a-4e88-b5ca-6d8f24c1bfb8`)
- S21: [Mg-3Sm-0.5Zn-0.4Zr合金的高温蠕变机制和组织演变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65123203-01e0-4935-84dd-7ffc34e8504c/resource) (`65123203-01e0-4935-84dd-7ffc34e8504c`)
- S27: [Mg-3Sm-0.5Zn-0.4Zr合金的高温蠕变机制和组织演变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7590e1db-e4d8-4c52-9dfe-1244ef8d5be7/resource) (`7590e1db-e4d8-4c52-9dfe-1244ef8d5be7`)
- S46: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc/resource) (`d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc`)
- S47: [civil engineering materials__02d83efc13](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d43afc97-bf13-405b-9fb8-14084223ef24/resource) (`d43afc97-bf13-405b-9fb8-14084223ef24`)
- S50: [光学显微镜、扫描电子显微镜与透射电子显微镜对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dedc4bbd-aabb-4964-81c1-f82e1e64ffa7/resource) (`dedc4bbd-aabb-4964-81c1-f82e1e64ffa7`)
- S1: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0145eb27-8393-47ea-804d-ccf579a0ba51/resource) (`0145eb27-8393-47ea-804d-ccf579a0ba51`)
- S18: [civil engineering materials__02d83efc13](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/54be10dd-870e-436b-aa13-cf03c2f49c4c/resource) (`54be10dd-870e-436b-aa13-cf03c2f49c4c`)