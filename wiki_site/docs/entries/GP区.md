---
version: "v1"
generated_at: "2026-06-18T07:26:53+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 45
  source_quality_score: 0.86
  freshness_score: 0.74
  evidence_coverage_score: 1.0
---

## 概述

GP区（Guinier-Preston区）是铝合金时效初始阶段，过饱和固溶体中溶质原子发生偏聚形成的早期共格析出相。该术语源于1938年A. Guinier与G. D. Preston在研究Al-Cu合金单晶自然时效过程中，各自独立地在劳厄照片上发现异常衍射条纹，由此确定为铜原子在基体｛100｝晶面上偏聚形成的富铜区。为纪念这两位发现者，称此类“二维”溶质原子偏聚区为GP区[[S52,S8]]。

GP区的核心特征包括：溶质原子富集偏聚属性、与铝基体完全共格、无独立完整晶体结构，可被位错直接剪切，是铝合金时效强化过程中的重要阶段产物[[S3,S29]]。由于GP区无独立相界面，界面能极低，形核功极小，可借助淬火保留的过饱和空位在很低温度下快速形成，其在基体中的密度可达\(10^{17} \sim 10^{18}\)个/厘米³[[S3]]。

![图1 Al-Cu合金中GP区的TEM形貌，900000×，显示GP区在基体中呈均匀弥散分布的纳米级细小颗粒](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1b0a165-b12e-456a-aa40-2627f6f65131/resource)

**图1** 展示了Al-Cu合金中GP区的透射电镜照片。GP区呈现为基体中相对均匀分布的细小暗色颗粒状结构，反映了GP区在铝基体中的均匀弥散分布特征与纳米级尺寸特点[[S46,S20]]。

## 分类与命名

GP区可依据其有序化程度和尺寸差异区分为两类[[S50,S44]]：

- **GP I区**：溶质原子在基体特定晶面上的富集偏聚区，原子呈无序排列，保持与基体完全相同的晶格结构，尺寸极小。
- **GP II区**：在GP I区基础上，随着时效温度升高或时间延长，溶质原子发生有序化排列，部分合金系中记为\(θ''\)相或\(β''\)相等。GP II区尺寸较GP I区更大，周围晶格畸变更强烈，对位错的阻碍作用更大，是多数铝合金达到峰值时效强化的主要贡献相[[S50,S30]]。

在Al-Cu合金中，文献对命名曾有争议：H. K. Hardy认为\(θ''\)是由GP区重排而成，因此称\(θ''\)为GP(II)区，而将GP区称为GP(I)区。然而从电子显微图像和动力学特征（如\(θ''\)相形核需经一定孕育期且一旦形成即快速长大，而GP区形成几乎无孕育期、长大缓慢）来看，将\(θ''\)视为过渡相更为合理[[S7]]。

## 形成条件

### 不同合金系的GP区析出特征

不同铝合金系中GP区的形成温度区间、形态及尺寸存在显著差异。下表汇总了典型合金系中GP区的关键特征。

| 合金系 | GP区类型 | 形成温度区间 | 形态 | 典型尺寸 | 析出晶面/位向 |
|--------|----------|-------------|------|---------|-------------|
| Al-Cu | GP I区 | ≤80~130℃[[S30,S21]] | 片状（盘状） | 厚度0.4~0.6 nm，直径2~10 nm[[S44]] | ｛100｝晶面[[S30,S44]] |
| Al-Cu | GP II区（θ''） | 80~250℃[[S30]] | 盘状 | 厚度1.0~4.0 nm，直径10~150 nm[[S44]] | ｛100｝晶面[[S30]] |
| Al-Mg-Si | GP区 | 室温~≤200℃[[S27,S11]] | 初始球状→针状 | 直径约6 nm，长20~1000 nm[[S27,S11]] | 平行于基体〈001〉晶向[[S11]] |
| Al-Zn-Mg | GP I区 | 室温~150℃[[S16]] | 球状 | 1~2 nm[[S16]] | ｛100｝晶面[[S16]] |
| Al-Zn-Mg | GP II区 | ≥70℃（需≥450℃淬火）[[S16]] | 盘状 | 几个原子层厚，具一定长径比[[S16]] | ｛111｝晶面[[S16]] |

在Al-Mg-Si系合金中，GP区初期为球状，在接近时效曲线最高强度处转变为针状[[S27]]。该合金系无明确独立划分的GP I和GP II区，强化机制源于位错运动时需要打断Mg-Si键[[S27,S26]]。Al-Zn-Mg系合金中，GP II区仅在特定条件下（高于450℃淬火且高于70℃时效）方会析出[[S16]]。

### 热力学条件与成核驱动因素

GP区的形成需要满足以下基本条件：

1. **合金元素固溶度随温度降低而显著下降**：这是时效硬化的必要条件，满足此条件的典型合金系包括Al-Cu、Al-Mg-Si、Al-Zn-Mg等[[S39,S3]]。
2. **淬火保留过饱和空位**：快速冷却（淬火）获得的过饱和空位促进溶质原子短程扩散，降低GP区形核功，使GP区在极低温度下即可快速形成[[S3,S10]]。淬火冷却速率越高，保留的空位浓度越高，GP区形核越快[[S17]]。
3. **时效温度控制**：时效温度决定析出相的类型与序列。以ω(Cu)=4%的Al-Cu合金为例，130℃以下时效以形成GPI区为主，150~175℃时效以θ''（GPⅡ区）为主，高于200℃即不再生成GP区[[S21,S47]]。

## 结构、形貌与强化机制

### 形态特征

GP区与基体完全共格，其形状主要取决于共格应变能。组元原子直径差不同的合金，应变能各异，因此GP区形状亦不相同[[S54]]。Al-Cu系中铜原子半径约为铝原子半径的87%，GP区呈片状形式以获得较大的接触面积从而减小晶格畸变[[S52,S9]]；Al-Mg-Si系中GP区由球状逐渐演变为针状；Al-Zn-Mg系中GP区呈球状[[S54,S15]]。

### 位错剪切强化机理

GP区可被位错直接剪切，其强化作用主要来自以下三类贡献[[S35,S45,S53]]：

1. **共格强化**：GP区周围共格应变场引起的弹性应力场阻碍位错运动。由于GP区晶格常数与基体不同，在基体中引起点阵畸变，由此产生的应力场对位错构成阻碍[[S45]]。
2. **模量强化**：铝基体与GP区之间剪切模量差异导致的强化效果。当析出相弹性模量大于基体时，位错受到斥力，反之受到吸力[[S45]]。
3. **化学硬化**：位错切过GP区后新增的GP-基体界面导致系统能量升高，由此带来强化效应[[S35,S53]]。

### 临界剪切与Orowan转变

当共格析出相尺寸小于临界半径时，位错优先以剪切方式通过析出相，临界切变应力随析出相半径的0.5次方增长；当尺寸超过临界值时，位错无法剪切析出相，转为以Orowan机制绕过析出相，此时强化作用随粒子间距减小而提升[[S55,S13]]。在AA7055铝合金中，临界半径约为4.7 nm[[S12]]。

## 与后续析出相的关系

### 各合金系析出序列

GP区是时效析出序列中的早期阶段，为后续过渡相和平衡相的形成提供前驱体。不同合金系的完整析出序列如下：

| 合金系 | 完整析出序列 | 平衡相 |
|--------|-------------|--------|
| Al-Cu | 过饱和固溶体 → GP区 → θ''相 → θ'相 → θ相[[S49,S30,S51]] | θ (CuAl₂)[[S7]] |
| Al-Mg-Si | 过饱和固溶体 → GP区 → β''相 → β'相 → β相[[S27,S41]] | β (Mg₂Si)[[S27]] |
| Al-Zn-Mg | 过饱和固溶体 → GP区 → η'相 → η相[[S22,S38]] | η (MgZn₂)[[S38]] |
| Al-Zn-Mg（低Zn/Mg比）| 过饱和固溶体 → GP区 → T'相 → T相[[S38,S22]] | T (Al₂Mg₃Zn₃)[[S38]] |

### 转变过程与性能演变

不同时效阶段的力学性能对应演变规律如下[[S12,S1,S43]]：

- **欠时效阶段**：以GP区和少量亚稳相为主，位错切过机制占主导，合金强度逐步上升，同时保持较高塑性。
- **峰时效阶段**：θ''、β''、η'等亚稳相数量达到最大值，合金强度达到峰值。在Al-Cu合金中，θ''相析出阶段即为合金达到最大强化的阶段[[S1,S43]]。
- **过时效阶段**：析出相失去共格，位错转为Orowan绕过机制，合金强度逐步下降，塑性有所回升[[S1,S43]]。

在Al-Cu合金中，θ''是由GP区通过原子有序重排而成[[S7,S49]]。GP区大部分在θ'相开始析出之前完成溶解[[S19]]。

## 压铸关联

### 压铸铝合金中的GP区析出行为

Al-Mg-Si系压铸铝合金（如A356、AlSi10MnMg等牌号）的时效析出路径与变形铝合金一致[[S11,S37]]：

过饱和固溶体 → 球状GP区 → 针状GP区 → β''相 → β'相 → 平衡Mg₂Si相

在≤200℃短时时效条件下，可观测到尺寸约6 nm × (200~1000 nm)的针状GP区，沿基体〈001〉晶向分布[[S11,S37]]。

### T5与T6热处理中GP区的角色

- **T5处理**（仅人工时效，无单独固溶处理）：在较低温度下保温可促使基体中残留过饱和固溶体直接析出GP区。析出峰期合金的强度较铸态提升约8.9%，塑性出现小幅下降[[S39]]。
- **T6处理**（固溶+淬火+人工时效）：固溶淬火获得的高浓度过饱和固溶体在后续低温时效阶段首先大量析出GP区，GP区可作为后续过渡相的有利形核位点，最终提升整体析出强化效果[[S26,S39,S42]]。

### 压铸快冷对GP区析出的促进作用

压铸工艺的高冷却速率会大幅提升合金中的过饱和空位浓度，促进GP区形核[[S17]]。相比普通金属型铸造的同成分铝合金，压铸合金时效时GP区的析出密度显著更高。以AA6005合金为例，双辊快淬制备的试样人工时效峰值硬度比金属型铸造试样高约15 HV[[S33]]。

高密度纳米级GP区可通过对位错的钉扎作用产生显著应变硬化，同时由于与基体共格的特征，周围错配应变水平较低，可有效降低粗大第二相引发的应力集中，在提升强度的同时抑制微裂纹形核，获得比单独析出亚稳相更优的强塑性协同效果[[S42]]。

## 表征与检测

### 主要表征方法

| 表征技术 | 适用性 | 典型观测内容 |
|---------|--------|------------|
| TEM/HRTEM | 直接观察GP区形貌与分布 | 纳米级GP区的尺寸、形状、分布，通过弹性应变衬度成像[[S29]] |
| DSC（差示扫描量热法） | 检测GP区形成与溶解的热效应 | GP区析出放热峰与溶解吸热峰的位置与焓值[[S19,S40]] |
| XRD（X射线衍射） | 检测晶格畸变与GP区结构 | 劳厄照片上的异常衍射条纹（二维衍射效应）[[S52,S49]] |

### DSC表征典型数据

不同合金和工艺条件下，GP区的DSC特征温度有所差异：

| 合金/工艺 | GP区形成峰温度 | GP区溶解峰温度 |
|-----------|-------------|-------------|
| 半固态挤压铸造Al-17Si-4Cu-0.5Mg | ~101.2℃[[S34]] | ~260℃[[S34]] |
| 重力铸造Al-17Si-4Cu-0.5Mg | ~216.3℃[[S23]] | — |
| Al-Mg-Si-Cu（T4态） | 60~80℃[[S41]] | — |
| 2011铝合金（100℃时效） | — | ~170℃[[S19,S40]] |
| 6013铝合金 | — | ~160℃[[S32]] |

DSC曲线中GP区溶解对应的吸热峰出现在170℃左右（以2011合金为例），而θ'相析出放热峰出现在约340℃位置，表明大部分GP区会在θ'相开始析出之前完成溶解[[S19,S40]]。半固态挤压铸造工艺可显著提前合金的析出进程，其GP区析出放热峰较重力铸造工艺约低100℃[[S23,S34]]。

![图2 10 K/min加热速率下铝合金的DSC曲线，标注GP Zone、θ''、θ'等析出相对应的热流变化特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d897dabe-0f6a-4232-b127-2af89fd7345a/resource)

**图2** 展示了10 K/min加热速率下铝合金典型的DSC测试曲线。图中标注了GP Zone、θ''、θ'等不同析出相对应的热流变化特征，可用于识别各析出阶段的温度区间与热效应规律[[S48]]。

## 工程意义与局限

### 强化贡献

GP区是铝合金时效早期重要的强化相。GP II区（θ''相等有序化区域）析出阶段通常为合金达到最大强化的阶段[[S50,S1]]。时效过程中，GP区的尺寸、数量和分布直接影响合金的强度与塑性匹配[[S12]]。

### 温度稳定性限制

GP区的热稳定性有限。当时效温度超过150℃时，铝合金中的GP区会快速发生溶解，失去共格强化效应，合金开始出现不可逆软化；温度越高，GP区溶解速度越快，合金软化速率也随之升高[[S21]]。

工程应用中应严格控制铝合金的服役温度以避免GP区提前溶解导致性能劣化[[S25]]：

- 6xxx、5xxx系列铝合金：常规质量控制条件下长期服役温度**不建议超过100℃**；
- 7xxx系列铝合金：常规质量控制条件下长期服役温度**不建议超过80℃**。

在严格控制条件下，上述限温分别降至50℃和40℃[[S25]]。

## Sources
- S52: [铝合金及其加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e606b336-96c1-499a-bd04-b5a0182d88db/resource) (`e606b336-96c1-499a-bd04-b5a0182d88db`)
- S8: [2155556_GP区](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1538bf38-f1fc-404f-94e1-8912d1e43b8c/resource) (`1538bf38-f1fc-404f-94e1-8912d1e43b8c`)
- S3: [轻合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a326a97-644e-4bfc-95f3-39f8c125035c/resource) (`0a326a97-644e-4bfc-95f3-39f8c125035c`)
- S29: [工程材料及加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77f4cbdf-fb4e-47aa-98ee-f10d933ef7f9/resource) (`77f4cbdf-fb4e-47aa-98ee-f10d933ef7f9`)
- S46: [图1-6-9 Al-Cu合金中GP区电子显微镜图象](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1b0a165-b12e-456a-aa40-2627f6f65131/resource) (`d1b0a165-b12e-456a-aa40-2627f6f65131`)
- S20: [图1-6-9 Al-Cu合金中GP区电子显微镜图象](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/477e26d8-302e-4e2a-a058-2c81aea14c85/resource) (`477e26d8-302e-4e2a-a058-2c81aea14c85`)
- S50: [铝合金精锻成形技术及设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e396e7a2-1481-47e4-b0b1-27fbd8f7025d/resource) (`e396e7a2-1481-47e4-b0b1-27fbd8f7025d`)
- S44: [铝合金和钛合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8dea136-e730-420e-9906-64baffbf7323/resource) (`c8dea136-e730-420e-9906-64baffbf7323`)
- S30: [0206_45aac865510f0aa6_Aluminium–copper_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ca40087-d082-42cf-a20a-ceaddfedb607/resource) (`7ca40087-d082-42cf-a20a-ceaddfedb607`)
- S7: [铝合金及其加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1028af5d-7190-4a14-abf4-05b6686cd107/resource) (`1028af5d-7190-4a14-abf4-05b6686cd107`)
- S21: [工程材料及金属热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d11860e-a414-4bcc-be6f-0eee2b8a845c/resource) (`4d11860e-a414-4bcc-be6f-0eee2b8a845c`)
- S27: [铝合金及其加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d2b99f0-3157-455d-8f50-dee48e5c68a5/resource) (`6d2b99f0-3157-455d-8f50-dee48e5c68a5`)
- S11: [铝及铝合金管材生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24cc9abe-b746-4503-a78e-cd7d4eb72418/resource) (`24cc9abe-b746-4503-a78e-cd7d4eb72418`)
- S16: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ba7154d-77c2-4fa6-af0b-348b375a3bbc/resource) (`3ba7154d-77c2-4fa6-af0b-348b375a3bbc`)
- S26: [铝合金及其加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62d98d4c-343b-4e07-92ea-3f22dc433f38/resource) (`62d98d4c-343b-4e07-92ea-3f22dc433f38`)
- S39: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7d61785-3c39-45bc-a3ed-2b1d6a2e486a/resource) (`a7d61785-3c39-45bc-a3ed-2b1d6a2e486a`)
- S10: [铝合金无缝管生产原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16f06019-33e8-4459-bcab-ee44c9df0819/resource) (`16f06019-33e8-4459-bcab-ee44c9df0819`)
- S17: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/446cd6ae-4a47-4394-9b23-3db98ba76e5b/resource) (`446cd6ae-4a47-4394-9b23-3db98ba76e5b`)
- S47: [工程材料及金属热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d83f1950-78f1-4dd3-901b-8417bdd8e7cd/resource) (`d83f1950-78f1-4dd3-901b-8417bdd8e7cd`)
- S54: [现代铝合金板带投资与设计技术与装备产品与市场](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eda20051-2eb7-4a24-906d-9bac3559cc42/resource) (`eda20051-2eb7-4a24-906d-9bac3559cc42`)
- S9: [铝合金材料组织与金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15d56aa0-a2c5-47c3-a2f6-f92970668baa/resource) (`15d56aa0-a2c5-47c3-a2f6-f92970668baa`)
- S15: [几种主要合金GP区的形状及存在状态](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38169b48-1844-4541-8655-7451a3f2975f/resource) (`38169b48-1844-4541-8655-7451a3f2975f`)
- S35: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9cb8d48f-a822-43d6-8db9-f7ff3a569cf5/resource) (`9cb8d48f-a822-43d6-8db9-f7ff3a569cf5`)
- S45: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cef715f0-f24e-45c8-be0d-a3a0e90bc7b9/resource) (`cef715f0-f24e-45c8-be0d-a3a0e90bc7b9`)
- S53: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e90051e0-0609-4bf9-a500-a57151cc1757/resource) (`e90051e0-0609-4bf9-a500-a57151cc1757`)
- S55: [aluminium alloys design and development of innovative alloys2022__4bf2a8ae96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9ff6f5f-09d2-4655-8744-1db85cf4839f/resource) (`f9ff6f5f-09d2-4655-8744-1db85cf4839f`)
- S13: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2fe06ace-7c19-4685-83a8-616cd75f5e28/resource) (`2fe06ace-7c19-4685-83a8-616cd75f5e28`)
- S12: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2dddc5b5-39d4-4449-909e-5b16a6a064f6/resource) (`2dddc5b5-39d4-4449-909e-5b16a6a064f6`)
- S49: [铝合金型棒材挤压生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc607e11-f8bf-4661-b406-a629bfe9cb49/resource) (`dc607e11-f8bf-4661-b406-a629bfe9cb49`)
- S51: [0206_45aac865510f0aa6_Aluminium–copper_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4d6ab47-1501-462e-becb-a2fc6e0178d9/resource) (`e4d6ab47-1501-462e-becb-a2fc6e0178d9`)
- S41: [Zn对金属型铸造Al-Mg-Si-Cu合金组织和力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c487e7ed-e47c-4194-aac4-6f42bec66cd1/resource) (`c487e7ed-e47c-4194-aac4-6f42bec66cd1`)
- S22: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/503733d4-0f92-4a70-ac82-395a0f1e4756/resource) (`503733d4-0f92-4a70-ac82-395a0f1e4756`)
- S38: [铝合金及其加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6f4673e-29c4-49dd-a741-0cc4fb8dc6b7/resource) (`a6f4673e-29c4-49dd-a741-0cc4fb8dc6b7`)
- S1: [简明铝合金手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04655552-dfb9-4b92-b8d5-703d13d156c3/resource) (`04655552-dfb9-4b92-b8d5-703d13d156c3`)
- S43: [铝合金锻造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c85ef995-6d01-4592-81f1-8aeffd6d6fac/resource) (`c85ef995-6d01-4592-81f1-8aeffd6d6fac`)
- S19: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46ba1ef1-b885-4688-9bfc-8a462ab6e45a/resource) (`46ba1ef1-b885-4688-9bfc-8a462ab6e45a`)
- S37: [铝合金型棒材挤压生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a2109e91-b2fe-4036-bf7b-22d0fd9de034/resource) (`a2109e91-b2fe-4036-bf7b-22d0fd9de034`)
- S42: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c71dad81-76ca-4dd7-9402-8dfe7d694cca/resource) (`c71dad81-76ca-4dd7-9402-8dfe7d694cca`)
- S33: [双辊铸轧与金属型铸造AA6005铝合金人工时效过程中硬度随时间的变化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92e61b66-30b3-483c-a7fc-c400cedb2ae4/resource) (`92e61b66-30b3-483c-a7fc-c400cedb2ae4`)
- S40: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a813d4d7-cb19-4823-91c5-fec4d456b749/resource) (`a813d4d7-cb19-4823-91c5-fec4d456b749`)
- S34: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99d23920-cf3f-4bb5-ab30-2c1168aefe60/resource) (`99d23920-cf3f-4bb5-ab30-2c1168aefe60`)
- S23: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/596cd4c3-043d-4449-8a7f-3fa39b5dc9a6/resource) (`596cd4c3-043d-4449-8a7f-3fa39b5dc9a6`)
- S32: [aluminium alloys theory and applications__f2d28f5a78](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89524d9a-2443-44ac-aff5-a1015fbd19c5/resource) (`89524d9a-2443-44ac-aff5-a1015fbd19c5`)
- S48: [Fig.6(b) 10 K/min加热速率下Al合金表面层与中心区的DSC热流曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d897dabe-0f6a-4232-b127-2af89fd7345a/resource) (`d897dabe-0f6a-4232-b127-2af89fd7345a`)
- S25: [铝焊后热影响区软化温度控制标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b0e1d13-8078-4739-9d2a-f8683abd4299/resource) (`5b0e1d13-8078-4739-9d2a-f8683abd4299`)