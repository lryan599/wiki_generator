---
version: "v1"
generated_at: "2026-06-18T18:10:30+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 22
  source_quality_score: 0.87
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 概述
电子探针X射线显微分析（Electron Probe Microanalysis，EPMA），简称电子探针，是一种将显微成像与微区成分高精度定量分析相结合的检测技术。该技术由法国科学家R. Castaing于1948年提出并制成首台设备，1958年实现商品化，其核心定位为微区成分定量分析，以区别于以形貌观察为主的扫描电镜（SEM）[[S31,S22]]。EPMA可分析从铍（Be）到铀（U）的绝大多数元素，探测极限可达50~1000 ppm，微量分析相对精度为1%~5%，是材料科学与冶金领域微区成分表征的关键手段[[S19]]。

## 基本原理
EPMA建立在电子与物质相互作用的基础之上。仪器采用5~30 keV的细聚焦高能电子束轰击固体样品表面微区，使样品原子内层电子电离，当外层电子向内层跃迁时，辐射出具有特征波长/能量的X射线[[S31,S33]]。通过波谱仪（Wavelength Dispersive Spectrometer, WDS）或能谱仪（Energy Dispersive Spectrometer, EDS）检测这些特征X射线，依据波长/能量进行元素定性识别，依据特征X射线强度并配合标准试样校正，实现定量分析[[S31,S30]]。电子束与样品的相互作用体积决定了分析的空间分辨率，探测深度随加速电压和基体原子序数变化，通常在0.1~5 μm量级[[S33]]。

![电子探针显微分析仪JXA-8530F PLUS实验室设备场景](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b769e67-3973-4ce5-a50e-d70eba89a22c/resource)  
*图：场发射电子探针显微分析仪（JXA-8530F PLUS）实物图，包含主机及配套操作终端，用于实验室微区元素定性定量分析[[S3]]。*

## 仪器结构与工作模式
常规EPMA在扫描电镜基础构型上增设专属X射线光谱分析模块，主要组成部分包括电子光学系统、WDS/EDS组合X射线谱仪、光学显微镜定位系统、电子信号检测系统、高真空系统以及计算机自动控制与数据处理模块[[S31]]。多数商用EPMA可集成在扫描电镜或透射电镜镜筒上，实现微区形貌、晶体结构和成分分析的同步检测[[S31]]。

EPMA具有三种标准分析工作模式[[S31]]：
1. **定点分析**：电子束固定在选定微区，完成全谱扫描，获取该点的定性、半定量及高精度定量成分信息。
2. **线扫描分析**：电子束沿预设直线轨迹移动，采集元素特征X射线强度变化，得到沿线元素含量分布曲线。
3. **面扫描分析**：电子束在样品表面进行光栅式扫描，以特定元素X射线强度调制亮度，生成该元素在二维区域的浓度分布彩色图像。

## 波谱仪与能谱仪对比
EPMA通过WDS（波谱仪）和EDS（能谱仪）两类X射线谱仪实现信号采集，二者在性能和应用上形成互补，主要差异如表所示。

| 对比项 | WDS（波谱仪） | EDS（能谱仪） |
|--------|--------------|--------------|
| 分光原理 | 衍射分光 | 半导体探测器直接识别光子能量 |
| 能量分辨率 | ~5 eV | 145~150 eV |
| 检测限 | ~100 ppm | ~1000 ppm |
| 分析精度 | 高，适合痕量及重叠峰定量 | 较低，适合快速筛查 |
| 分析速度 | 慢，逐元素扫描 | 快，可同时采集全谱 |
| 表面要求 | 严格，需平整抛光表面 | 较宽，可接受一定粗糙度 |
| 适用场景 | 元素线分布、面分布高精度成像 | 原位形貌同步快速成分筛查 |

*表：WDS与EDS核心性能对比[[S30,S27,S1]]。*

## 与其他微区分析技术的比较
EPMA与扫描电镜能谱分析（SEM-EDS）、X射线荧光光谱（XRF）同属基于X射线的成分分析技术，但在激发源、空间分辨率和适用尺度上存在本质差异[[S33,S13,S24]]。

| 对比项 | EPMA | SEM-EDS | XRF |
|--------|------|---------|-----|
| 激发源 | 聚焦电子束 | 聚焦电子束 | X射线/γ射线 |
| 探测深度 | 0.1~5 μm（浅表层） | 0.1~5 μm | 数十至数百 μm（体相） |
| 空间分辨率 | 0.1~1 μm | 数μm~数十μm | 毫米级以上 |
| 检测限 | WDS ~100 ppm | ~1000 ppm | 可达ppm级（非微区） |
| 样品要求 | 抛光平整 | 可容忍粗糙表面 | 研磨压片即可 |
| 适用范围 | 微区高精度定量 | 原位形貌同步快速筛查 | 块体常量元素无损检测 |

## 关键操作参数
**加速电压** 是影响分析结果的核心参数。提高加速电压会增大电子与样品的相互作用体积，加深X射线激发深度，有利于提高重元素特征谱线的激发效率；但对于轻元素，其浅层出射的X射线更易被基体吸收，导致定量精度下降。参数选型可借助蒙特卡洛模拟预测X射线生成体积进行优化[[S29]]。EPMA的镜室和样品分析腔需维持10⁻⁶~10⁻⁴ Pa量级的高真空度，以降低电子与残余气体分子的散射，保障微区分析精度[[S23]]。

## 样品制备要求
样品表面必须经过完备的机械抛光处理，最终表面粗糙度应不粗于0.16 μm，以防表面凹凸引入X射线出射路径差异造成定量误差[[S21]]。对于玻璃、陶瓷等非导电试样，分析前需在表面蒸镀一层厚度均匀的碳膜或金属导电层，避免电子束轰击过程中的电荷积累，防止图像漂移和X射线强度畸变[[S19]]。对于含钾、钠等易迁移碱金属元素的样品，需在液氮制冷的低温环境下开展分析，抑制电子束导致的元素迁移与挥发[[S19]]。

## 定量分析方法与校正
测得的特征X射线原始强度与元素质量分数间并非简单的线性关系，定量分析必须进行基体效应校正。通常采用ZAF校正流程，包含三个校正项[[S30,S33]]：
- **原子序数校正（Z）**：修正不同基体对入射电子的阻挡和背散射差异。
- **吸收校正（A）**：修正特征X射线在样品内部传输过程中的吸收损耗。
- **荧光校正（F）**：修正其他元素被特征X射线激发产生的二次荧光干扰。

校正后的待测元素浓度可根据与标准样品的对比关系计算：
\( C = C_s \times (P_u - B_u) / (P_s - B_s) \)
其中 \(C_s\) 为标准样品中该元素的已知质量分数，\(P\) 和 \(B\) 分别为试样与标样的特征峰强度和背景强度[[S20]]。对平整光滑样品，采用纯元素或已知成分标样校正后的定量误差可控制在±4%以内[[S33]]。

## 在压铸及铸造领域的应用
EPMA在压铸和常规铸造领域中主要用于微观偏析评估、相鉴定与缺陷分析，为工艺优化提供直接的微区成分证据。

**微观偏析分析**  
利用面扫描和线扫描可直观获取铸态或热处理后合金元素在枝晶内部与枝晶间的分布特征。例如，对DD10镍基单晶高温合金母合金的EPMA面扫和点扫研究表明，合金呈典型树枝晶组织，Al、Ta、Ti在枝晶间呈正偏析，Co、Cr、W在枝晶核心呈负偏析，Mo分布均匀；随浇注温度降低，偏析程度先降后升，在1380 ℃时达到最低，Ti、W、Cr、Co的偏析得到显著改善[[S17]]。在镁合金领域，通过EPMA可清晰观察到Mg-Al-Ca电磁铸造合金中Ca、Al、Zn元素在α-Mg晶界附近的富集行为[[S18]]。

**相鉴定与定量**  
EPMA定点定量分析能够精准测定铸造合金中第二相的元素组成。例如，通过EPMA对半固态挤压铸造过共晶Al-Si-Cu-Mg合金进行点分析，可直接获得不同区域Mg、Al、Si、Cu、Fe元素的重量与原子百分比，确认Al₆FeMn、Al₁₅(FeMn)₃Si₂等金属间化合物的相身份[[S25,S26]]。

**工艺参数优化**  
EPMA可定量比较不同铸造工艺对成分均匀性的影响。7075铝合金流变压铸件的EPMA测试结果显示，螺旋电磁搅拌工艺可使铸件中心、中间及边缘位置的Zn元素含量稳定在5.6 wt%左右，成分均匀性显著优于普通铸造和普通电磁搅拌[[S5]]。冷却速率的提升可使正偏析元素Ti、Ta在枝晶间的浓度降低，负偏析元素W在枝晶间的浓度升高，微观偏析整体减弱[[S17]]。

**缺陷分析**  
在压铸件失效分析中，EPMA用于识别缺陷处的夹杂物。例如，铝合金压铸件缩孔周围铝基体上的白亮点夹杂物可通过EPMA确认为氧化夹杂物，从而建立熔体中夹杂物含量与铸件内部气孔、孔洞形成机制的关联，为熔炼除气和精炼工艺优化提供依据[[S11]]。

![高压压铸Al基合金C2中Cr元素EPMA面分布图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/387006c6-fb0a-4e17-a2ee-fa42dd4adfc8/resource)  
*图：高压压铸Al-Mg-Si-Mn合金中Cr元素的EPMA浓度分布图。色标显示Cr含量，标尺5 μm，用于研究微尺度下难熔偏析元素的分布特征[[S6]]。*

**热处理效果评估**  
EPMA可用于表征热处理前后合金元素的固溶与析出行为。例如，高强半固态铝合金热处理样的Cu元素EPMA面扫描图像表明，Cu富集区与针状析出物位置对应，可有效评估热处理工艺对元素分布的影响[[S14]]。

## 局限性与注意事项
- **定量准确度受表面状态制约**：表面粗糙度、倾斜等因素会引入X射线出射路径差异，降低定量精度，粗糙表面通常仅能实现半定量分析[[S33]]。
- **轻元素分析灵敏度较低**：低能量特征X射线更易被基体吸收，导致检测困难[[S29,S33]]。
- **空间分辨率与激发体积相关**：分析区域并不等同于电子束斑尺寸，而是由电子束在样品内部散射及X射线激发体积决定，在微米至亚微米尺度[[S33]]。
- **不适用于宏观偏析直接表征**：EPMA探测深度局限于表层数微米，无法替代XRF等体相分析技术进行块体宏观偏析评价[[S33]]。
- **碱金属元素迁移效应**：含K、Na等易迁移元素的样品若在常温下长时间分析，会导致特征X射线强度持续下降，需采用低温环境抑制[[S19]]。
- **WDS分析速度限制**：波谱仪成谱扫描速度较慢，不适合未知点的快速初筛，通常与EDS配合使用[[S30]]。

## 相关术语与关系
- **微观偏析/枝晶偏析**：EPMA是表征枝晶尺度元素不均匀分布的标准手段，与二次枝晶间距、冷却速率等凝固参数密切相关[[S17]]。
- **DD10合金/浇注温度**：DD10镍基单晶高温合金母合金的EPMA研究揭示，浇注温度通过影响二次枝晶间距和液相流动性，进而调控元素偏析程度与碳化物尺寸及形态[[S17]]。
- **压铸件力学性能/热处理**：EPMA提供的相成分与元素分布信息，可用于建立工艺-微观结构-力学性能之间的定量关联，支持热处理制度优化[[S14,S17]]。

## Sources
- S31: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2cc2f81-8c15-4b2a-9642-9f62ee586f61/resource) (`e2cc2f81-8c15-4b2a-9642-9f62ee586f61`)
- S22: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9eef6f3e-42cb-4a4c-9f2b-5b09391ee606/resource) (`9eef6f3e-42cb-4a4c-9f2b-5b09391ee606`)
- S19: [玻璃表面和表面处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bb4e4b8-93ee-486f-8e33-2c9ac4e18688/resource) (`8bb4e4b8-93ee-486f-8e33-2c9ac4e18688`)
- S33: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc6d987d-4607-4856-b891-23fdc7bb51ea/resource) (`fc6d987d-4607-4856-b891-23fdc7bb51ea`)
- S30: [玻璃表面处理技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6673f11-36a1-46f4-aa4a-902439eb8919/resource) (`d6673f11-36a1-46f4-aa4a-902439eb8919`)
- S3: [图2-11 电子探针显微分析仪；Fig.2-11 Electron probe microanalyzer (EPMA)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b769e67-3973-4ce5-a50e-d70eba89a22c/resource) (`1b769e67-3973-4ce5-a50e-d70eba89a22c`)
- S27: [表 2-3 波谱仪 (WDS) 与能谱仪 (EDS) 特征对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9363c47-159a-4a55-9767-8a09449712e2/resource) (`c9363c47-159a-4a55-9767-8a09449712e2`)
- S1: [表 9.1 波谱仪与能谱仪的比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/071c92a5-1e58-469f-8ab2-ffa44ef43f04/resource) (`071c92a5-1e58-469f-8ab2-ffa44ef43f04`)
- S13: [表 1-1 表面研究方法特性](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/779435fa-7719-4896-81fd-f93ddc760bf7/resource) (`779435fa-7719-4896-81fd-f93ddc760bf7`)
- S24: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7642b0d-982b-46a4-a788-f84c901f0381/resource) (`b7642b0d-982b-46a4-a788-f84c901f0381`)
- S29: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc/resource) (`d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc`)
- S23: [国防科工委十五规划教材材料加工工艺过程的检测与控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a34abe4e-d0eb-497c-8437-b130a0b9b05f/resource) (`a34abe4e-d0eb-497c-8437-b130a0b9b05f`)
- S21: [试样技术要求](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95c35923-d514-4dca-b055-07e5628466c8/resource) (`95c35923-d514-4dca-b055-07e5628466c8`)
- S20: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91f49dd0-3bcb-4e7c-98ce-2147062a83af/resource) (`91f49dd0-3bcb-4e7c-98ce-2147062a83af`)
- S17: [浇注温度对DD10母合金微观偏析及碳化物的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/846e2ff1-0ef4-4e3d-96d4-67b2d0517943/resource) (`846e2ff1-0ef4-4e3d-96d4-67b2d0517943`)
- S18: [先进镁合金制备与加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84df343e-2723-448d-8f44-0cd23d82055b/resource) (`84df343e-2723-448d-8f44-0cd23d82055b`)
- S25: [c C点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd5a1a2f-1b68-40bc-8f6a-7795f5a0c0e2/resource) (`bd5a1a2f-1b68-40bc-8f6a-7795f5a0c0e2`)
- S26: [a 半固态挤压铸造Al-Si-Cu-Mg合金的EPMA元素分析图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c65aca71-e706-4cd9-a3ee-576d3db492fa/resource) (`c65aca71-e706-4cd9-a3ee-576d3db492fa`)
- S5: [三种铸造方法制备铸件不同位置的Zn元素含量对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3021738c-256b-4c53-b478-5f88adc45b8b/resource) (`3021738c-256b-4c53-b478-5f88adc45b8b`)
- S11: [压铸实用技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/721033d1-5355-40d9-8e47-a8e489af1d8d/resource) (`721033d1-5355-40d9-8e47-a8e489af1d8d`)
- S6: [EPMA map of Cr distribution in C2 alloy](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/387006c6-fb0a-4e17-a2ee-fa42dd4adfc8/resource) (`387006c6-fb0a-4e17-a2ee-fa42dd4adfc8`)
- S14: [图5-17(c) 热处理态试样Cu元素EPMA面扫描结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7853eaa1-3137-4122-82cb-7f243c5d881c/resource) (`7853eaa1-3137-4122-82cb-7f243c5d881c`)