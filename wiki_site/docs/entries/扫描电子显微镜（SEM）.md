---
version: "v1"
generated_at: "2026-06-18T11:51:41+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.86
  freshness_score: 0.84
  evidence_coverage_score: 1.0
---

## 概述

扫描电子显微镜（Scanning Electron Microscope，缩写 SEM）是一种利用聚焦电子束在样品表面逐点扫描、收集电子束与样品相互作用产生的物理信号进行成像的大型精密分析仪器。该设备集成了电子光学技术、真空技术、精密机械技术与现代计算机控制技术，具有制样简单、放大倍数连续可调、图像分辨率高、景深大的显著特点，在材料科学、机械加工、冶金等领域获得了广泛应用[[S48]]。在工业与科研语境中，该设备常被简称为“扫描电镜”。

扫描电子显微术（Scanning Electron Microscopy）则是指依托扫描电镜设备所建立的一整套表面分析方法体系，涵盖成像原理、信号采集与处理、微区形貌与成分表征的完整流程。为区分概念边界，方法学层面通常以“扫描电子显微分析技术”明确指代该分析方法[[S37]]。

## 分类

### 按电子源类型分类

扫描电镜依电子枪类型可分为四类，不同电子源的亮度、束斑直径、分辨率及适配检测附件能力存在显著差异[[S35,S33]]：

| 电子源类型 | 主要特点 |
|---|---|
| 钨灯丝热发射型 | 灯丝成本低，对真空度要求不高；发射源直径较大，分辨率相对较低[[S35]] |
| LaB₆ 热发射型 | 发光效率高、亮度比钨灯丝提升约一个数量级，使用寿命更长[[S33]] |
| 冷场发射型（CFE） | 电子束直径极小（约 10 nm），亮度极高，分辨率可达 0.5 nm；总发射电流较小，适配能谱仪（EDS）[[S35]] |
| 热场发射型（肖特基发射，TFE） | 可提供较大束流，可同时加装能谱仪（EDS）与波谱仪（WDS）；分辨率略低于冷场发射，阴极寿命较短[[S35]] |

### 按功能特性分类

按样品室真空度与适用对象，扫描电镜可分为常规高真空型、低真空型与环境扫描电镜（ESEM/环扫）三类[[S37]]。低真空型与环境扫描电镜可直接观测绝缘样品、含水活态样品等非导电试样，无需对样品进行传统金属镀膜处理[[S12]]。

## 工作原理

扫描电镜以聚焦高能电子束在试样表面逐点扫描成像。由电子枪发射的电子经加速电压加速，经电磁透镜会聚为微细电子束，在扫描线圈驱动下按栅网式路径扫描样品表面[[S48]]。

高能入射电子束与固体样品发生相互作用时，会同时激发出多种物理信号[[S23,S35]]：

- **二次电子（SE）**：来自样品表层 5～10 nm 深度范围，能量较低（<50 eV），对表面形貌极为敏感，是形貌成像的主要信号来源[[S35,S31]]。
- **背散射电子（BSE）**：来自样品表层几百纳米深度范围，产额随原子序数增加而升高，可提供原子序数衬度，定性区分不同相组分[[S23]]。
- **特征 X 射线**：由原子内层电子受激电离后外层电子跃迁产生，能量与波长具有元素特征性，用于微区成分定性与定量分析[[S6]]。

这些信号经探测器接收、转换为电信号并放大后，调制同步扫描的显像管亮度，从而在荧光屏上形成反映试样表面特征的放大图像[[S22]]。

## 核心性能参数

常规商用扫描电镜的主要性能参数范围如下[[S22,S14]]：

| 性能指标 | 典型值/范围 |
|---|---|
| 二次电子分辨率 | 3～6 nm（热发射机型）；场发射机型可达 0.5～1 nm |
| 总放大倍数 | ×20～×200,000 连续可调 |
| 样品台 X/Y 向移动范围 | 50～100 mm（常规三轴台） |
| 样品台 Z 向升降范围 | 10～50 mm（常规三轴台） |

SEM 的性能优势在于景深远超光学显微镜（可达上千倍），成像富有立体感，视场调节范围宽，可直接观察大块样品[[S22,S3]]。

## 关键硬件组成

扫描电镜由以下七大核心单元协同工作[[S34,S31,S22]]：

1. **电子枪**：发射电子束，类型决定整机分辨率等级。
2. **电磁透镜**（聚光镜、物镜）：对电子束进行聚焦，控制束斑直径。
3. **扫描线圈**：驱动电子束按预定路径在样品表面扫描。
4. **二次电子探测器**：收集表面形貌信号。
5. **背散射电子探测器**：收集原子序数衬度信号。
6. **能谱仪（EDS）**：检测特征 X 射线，实现微区元素分析。
7. **真空系统**：维持镜筒与样品室的高真空（通常 10⁻⁴～10⁻⁵ mmHg），防止电子散射与样品污染[[S48]]。

## 在压铸中的应用

### 微观组织观测

SEM 可用于压铸铝合金中 α-Al 枝晶、共晶 Si 形貌的微观组织表征，配合 EDS 可分析不同区域的元素分布并确认第二相组成[[S44,S16]]。背散射电子模式下，利用灰度衬度差异可清晰区分 α-Mg 基体、晶界析出相及富锰/富铁金属间化合物[[S32,S50]]。典型工作电压为 15～20 kV，工作距离 8～12 mm[[S12]]。

![汽车蜗壳压铸件切面SEM微观形貌，优化工艺后组织致密无明显缺陷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f26d4af4-a1e0-4fe5-9efd-2d699eaeefd7/resource)
*图：AnyCasting 工艺优化后汽车蜗壳铝合金压铸件切面的 SEM 形貌，展示致密的微观组织特征[[S49]]*

### 孔洞缺陷分析

SEM-EDS 组合是压铸件气孔、缩松、氧化夹杂等缺陷形貌表征与成分溯源的核心手段，可准确定位缺陷位置，识别缺陷内表面元素构成，区分冷料卷入缺陷、氧化夹渣与碳化物夹渣等不同类型[[S13,S11,S43]]。

### 拉伸断口分析

SEM 可对压铸拉伸试样的断口进行韧窝、解理形貌分析，判定合金断裂模式（如韧-脆混合型断裂、韧性断裂），同时识别断口上的第二相粒子与缺陷特征，关联铸件力学性能表现[[S9,S41,S25]]。

### 第二相分布表征

利用背散射电子成像模式，可通过灰度差异区分不同原子序数的相组分，实现 α-Mg 基体、晶界析出相、富锰/富铁金属间化合物的清晰识别[[S32]]。EDS 面扫描可进一步获得各相的元素分布图谱，确认如 Q-Al₅Cu₂Mg₈Si₆、θ-Al₂Cu、α-Al₁₅(Fe,Mn)₃Si₂ 等第二相的种类[[S44]]。

## 样品制备要求

压铸件 SEM 检测的样品制备全流程如下[[S47,S36,S15,S41]]：

1. **切割取样**：推荐外接尺寸不超过 Φ32 mm，适配常规 SEM 样品台[[S13]]。
2. **研磨**：依次采用 400# 至 5000# 砂纸逐级湿磨，每更换砂纸旋转 90° 以消除上一道划痕[[S47]]。
3. **抛光**：先以金刚石抛光膏粗抛，再以氧化铝悬浮液精抛至镜面效果，以无水乙醇为润滑介质[[S47]]。
4. **清洗**：抛光完成后将样品置于无水乙醇中超声波清洗 ≥5 分钟，去除残留抛光膏与污染物[[S47]]。
5. **腐蚀处理**：如观察金相组织，需使用专用腐蚀液进行短时腐蚀。
6. **导电处理**：导电性良好的金属压铸样品仅需用导电胶粘贴于样品座即可上机。非导电样品需真空蒸镀导电层：喷金适用于低倍形貌观测，喷碳适用于需配套 EDS 进行微区元素定量分析的场合，以避免金元素峰干扰目标元素检测[[S15,S3]]。
7. **断口保护**：拉伸断口试样须做好防护，避免外力磕碰或摩擦破坏断口形貌；必要时可采用低浓度弱酸超声清洗去除表面氧化污物以提升成像质量[[S25]]。

## 常见型号与品牌

压铸检测领域广泛使用的扫描电镜代表性型号包括[[S40,S10,S38,S27]]：

| 品牌 | 代表性型号 |
|---|---|
| 日本电子（JEOL） | JSM-6700F、JSM-6460、JSM-7600F、JSM-7800F |
| 日立（Hitachi） | S-3400N、SU-6600、TM4000 系列 |
| FEI（现 Thermo Fisher） | Nova400、NovaNano450、FEI-Talos F200S、FEI Quanta200F |
| 蔡司（Zeiss） | Sigma 500 系列、EVO 18 |

其中日立 TM4000 系列为台式 SEM，搭载低真空系统，无需对非导电压铸样品进行金属镀膜，支持 5 kV、10 kV、15 kV 三档加速电压与四档束流强度可调[[S12]]。

## 相关标准

- **GB/T 17362-2008《扫描电镜分析法通则》**：为国内 SEM 分析的基础性通用方法导则，涵盖设备通用性能要求、导电/非导电试样的制备规范、四种常用成像模式（SE、BSE、吸收电子、透射电子）的适用场景、放大倍数与分辨率校准要求、微区成分定性及半定量分析通用操作流程及检测报告标准规则[[S46,S36]]。
- **GB/T 13822-2017《压铸有色合金试样》**：将扫描电镜列为拉伸试样断口形貌观测及断裂失效模式判定的指定可选检测方法[[S5]]。

## 局限性与注意事项

1. **放大倍数误差**：SEM 放大倍数示值实际偏差最高可达 25%，须使用 SEM 标准标尺定期校准[[S52]]。
2. **景深与放大倍率的关系**：放大倍率提升时景深同步降低，过高倍率下无法同时对大起伏的压铸粗糙断口全表面实现清晰聚焦[[S22]]。
3. **充电效应**：非导电样品在电子束轰击下表面电荷不断累积，导致图像漂移与亮度异常畸变，常规条件下需蒸镀导电层导走多余电荷[[S3]]。
4. **EDS 定量分析准确度**：对于无标准样的粗糙样品或微小相区域，仅能实现半定量分析，常规 EDS 检测限约 1000 ppm，低于 EPMA 配套的 WDS 波谱仪约 100 ppm 的检测水平[[S51,S39]]。
5. **轻元素 X 射线吸收**：低原子序数元素的特征 X 射线能量低，易被基体吸收，影响定量分析的准确性[[S39]]。

## 与其他检测手段的比较

SEM 与光学显微镜（OM）、透射电镜（TEM）、电子探针（EPMA）的核心性能差异如下[[S42,S18,S51]]：

| 对比维度 | OM | SEM | TEM | EPMA |
|---|---|---|---|---|
| 光源/激发源 | 可见光（~500 nm） | 聚焦电子束 | 高能电子束 | 聚焦电子束 |
| 工作环境 | 空气 | 真空 | 真空 | 真空 |
| 典型分辨率 | ~200 nm | ~1.55 nm（可达 0.5 nm） | ~0.12 nm | 微米级（成分空间分辨率） |
| 检测信息 | 可见光反射/透射 | 二次电子、背散射电子、特征 X 射线 | 透射电子、衍射电子 | 特征 X 射线（WDS/EDS） |
| 样品要求 | 抛光/腐蚀表面 | 导电处理或镀膜 | 超薄箔片（<100 nm） | 抛光平面 |
| 分析深度/范围 | 表面 | 表面层 nm～μm 级 | 整个薄片厚度 | 0.1～5 μm |
| 主要用途 | 金相组织（>1 μm 尺度） | 形貌、断口、半定量成分 | 晶格精细结构、纳米析出相 | 精确定量成分分析 |
| 成分分析能力 | 无 | 半定量（EDS 检测限 ~1000 ppm） | EDS/EELS | 定量误差 ±4%（WDS，检测限 ~100 ppm） |

SEM 在压铸件表征中的核心定位为：适配大块样品原始表面的显微形貌观测与微区半定量成分分析，兼顾分辨率、景深与分析效率，是连接宏观金相检测与纳米级精细结构分析之间的关键中间尺度分析工具[[S42,S46]]。

## Sources
- S48: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eaa1473b-8271-4cd6-b01d-b158714f66e3/resource) (`eaa1473b-8271-4cd6-b01d-b158714f66e3`)
- S37: [木塑复合材料的表面处理与胶接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cce596d6-0a92-4267-8c4e-036edaf761fb/resource) (`cce596d6-0a92-4267-8c4e-036edaf761fb`)
- S35: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c1494015-43e6-430f-bde5-7a168cef5eb4/resource) (`c1494015-43e6-430f-bde5-7a168cef5eb4`)
- S33: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b14ebfcb-0ed2-4d87-aca8-ee6917c5019d/resource) (`b14ebfcb-0ed2-4d87-aca8-ee6917c5019d`)
- S12: [耐热铝合金薄壁构件离心浇注数值仿真及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48012701-3673-4482-a4be-a6c7f2e705dc/resource) (`48012701-3673-4482-a4be-a6c7f2e705dc`)
- S23: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/861106c1-8a7a-41fe-aab6-45d05d436141/resource) (`861106c1-8a7a-41fe-aab6-45d05d436141`)
- S31: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3d39e4a-3780-4719-96a1-ae72d932af89/resource) (`a3d39e4a-3780-4719-96a1-ae72d932af89`)
- S6: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28359469-ce0a-4073-9829-1a7f5c9b7ab5/resource) (`28359469-ce0a-4073-9829-1a7f5c9b7ab5`)
- S22: [金属表面处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7fe79ebe-a154-4f2c-bbcf-1fa28b093b0f/resource) (`7fe79ebe-a154-4f2c-bbcf-1fa28b093b0f`)
- S14: [扫描电子显微镜（SEM）不同类型电子枪的典型特性参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a96f289-f264-4dba-af69-9744d2440603/resource) (`5a96f289-f264-4dba-af69-9744d2440603`)
- S3: [玻璃表面和表面处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d321785-877c-460b-9df4-55d04519c3cc/resource) (`0d321785-877c-460b-9df4-55d04519c3cc`)
- S34: [超大规模集成电路衬底材料性能及加工测试技术工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b159a942-f645-43db-8c3a-f189d38a7390/resource) (`b159a942-f645-43db-8c3a-f189d38a7390`)
- S44: [T5处理对高真空压铸Al-10Si-Cu-Mg-Mn合金组织影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e155de4b-96fd-417e-a09b-6b5e1d5d82ca/resource) (`e155de4b-96fd-417e-a09b-6b5e1d5d82ca`)
- S16: [5G基站散热器用高导电（热）压铸Al-Si-Fe铝合金的热力学设计与试验](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60f01d6b-d6fb-48d0-a8b5-87147e1d126a/resource) (`60f01d6b-d6fb-48d0-a8b5-87147e1d126a`)
- S32: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5556f20-1e29-4a36-bc94-b1b02a0d7869/resource) (`a5556f20-1e29-4a36-bc94-b1b02a0d7869`)
- S50: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa16c00f-1fb7-4bf5-b292-b125fa77884f/resource) (`fa16c00f-1fb7-4bf5-b292-b125fa77884f`)
- S49: [图11 汽车蜗壳切面的SEM形貌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f26d4af4-a1e0-4fe5-9efd-2d699eaeefd7/resource) (`f26d4af4-a1e0-4fe5-9efd-2d699eaeefd7`)
- S13: [真空压铸无缸套铝合金气缸体缸孔铸造缺陷调查_韩洁丽](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55873130-e1e2-45d0-a95a-8ef07b13e0f7/resource) (`55873130-e1e2-45d0-a95a-8ef07b13e0f7`)
- S11: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4590de14-3663-495c-97be-48219a1a42ea/resource) (`4590de14-3663-495c-97be-48219a1a42ea`)
- S43: [effect of controlling process parameters on shrinkage porosity in alumin__a1ce093666](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df586073-8c13-4bc6-a6ca-466f1c027aa8/resource) (`df586073-8c13-4bc6-a6ca-466f1c027aa8`)
- S9: [大规格2A14铝合金铸锭氧化夹杂缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b49ea01-901c-4c1f-9231-20acf8b27bf0/resource) (`3b49ea01-901c-4c1f-9231-20acf8b27bf0`)
- S41: [铝合金半固态压铸工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddfed4c1-b568-4b66-b4cd-9e6405c20166/resource) (`ddfed4c1-b568-4b66-b4cd-9e6405c20166`)
- S25: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87ff354e-ee7b-49ac-ab57-f211d2f6601a/resource) (`87ff354e-ee7b-49ac-ab57-f211d2f6601a`)
- S47: [压铸AZ91D和AE44镁合金三维形貌重构及力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9b24764-77cd-4158-bf86-f34d99ccd9f0/resource) (`e9b24764-77cd-4158-bf86-f34d99ccd9f0`)
- S36: [金属注射成形精密零件生产与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c991d6bb-5ed3-4c4e-bd06-3aa48ae468e3/resource) (`c991d6bb-5ed3-4c4e-bd06-3aa48ae468e3`)
- S15: [a guide to lead free solders physical metallurgy and reliability__ec2bc7eb48](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ccaa68b-65ac-4273-bc8f-0582ee8deea4/resource) (`5ccaa68b-65ac-4273-bc8f-0582ee8deea4`)
- S40: [铝合金机匣铸造工艺及数值模拟分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dbd50a28-19bf-4db7-9e6b-152f1124f4b8/resource) (`dbd50a28-19bf-4db7-9e6b-152f1124f4b8`)
- S10: [Ti颗粒增强AZ81基复合材料的制备及组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fff2d26-3a2d-47f8-9c25-238ea0fe236e/resource) (`3fff2d26-3a2d-47f8-9c25-238ea0fe236e`)
- S38: [effect of heat treatment on microstructures and mechanical properties of__5cf11d89f4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d33058da-45fa-4f0e-a90e-2bf5d92645fd/resource) (`d33058da-45fa-4f0e-a90e-2bf5d92645fd`)
- S27: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/926bdadc-f7c6-4b61-85cf-31e960f471d4/resource) (`926bdadc-f7c6-4b61-85cf-31e960f471d4`)
- S46: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5865418-ccc4-4fb2-9ce6-eeb72924f131/resource) (`e5865418-ccc4-4fb2-9ce6-eeb72924f131`)
- S5: [基于ProCAST的汽车铝合金机油泵体压铸模具开发及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20ed0842-c7fc-473d-844b-8f1352b1ac70/resource) (`20ed0842-c7fc-473d-844b-8f1352b1ac70`)
- S52: [1991 annual book of astm standards section 2 nonferrous metal products v__3abfaf437d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe02b674-4460-4d2f-bf2e-225a354f25c1/resource) (`fe02b674-4460-4d2f-bf2e-225a354f25c1`)
- S51: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc6d987d-4607-4856-b891-23fdc7bb51ea/resource) (`fc6d987d-4607-4856-b891-23fdc7bb51ea`)
- S39: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc/resource) (`d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc`)
- S42: [光学显微镜、扫描电子显微镜与透射电子显微镜对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dedc4bbd-aabb-4964-81c1-f82e1e64ffa7/resource) (`dedc4bbd-aabb-4964-81c1-f82e1e64ffa7`)
- S18: [表 1-1 表面研究方法特性](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/779435fa-7719-4896-81fd-f93ddc760bf7/resource) (`779435fa-7719-4896-81fd-f93ddc760bf7`)