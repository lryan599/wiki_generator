---
version: "v1"
generated_at: "2026-06-18T05:50:21+00:00"
confidence_score: 0.84
confidence_level: "high"
confidence_basis:
  cited_sources: 49
  source_quality_score: 0.82
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

工业CT（Industrial Computed Tomography，别名工业计算机断层扫描成像、工业CT扫描技术、XCT、ICT）是应用于工业场景的核成像类无损检测技术。其基本过程为：利用X射线或γ射线穿过被检测工件，基于不同材料对射线的衰减特性差异，结合计算机断层重建算法，生成工件内部无影像重叠的断层图像乃至完整三维结构，从而实现缺陷检测、内部尺寸测量、逆向工程等多种功能 [[S44,S24,S36]]。

在压铸领域，工业CT主要用于铝合金、镁合金压铸件内部缺陷的无损定量检测与质量评定，能够对气孔、缩孔、缩松、夹杂、宏观偏析等缺陷的空间位置、尺寸和形貌进行精确表征。

## 工作原理

### X射线衰减与比尔定律

工业CT的物理基础是X射线穿透物质时的衰减现象。当单能X射线穿过非均匀物质时，其强度衰减严格遵循比尔-朗伯定律（Beer-Lambert Law） [[S1,S42,S45]]：

\[
I = I_0 \exp\left(-\int_L \mu(x,y)\;dl\right)
\]

其中 \(I_0\) 为入射初始射线强度，\(I\) 为透射后射线强度，\(\mu(x,y)\) 为被检测工件内部对应位置的线性衰减系数，\(L\) 为X射线穿透路径长度 [[S1,S42,S5]]。不同组分（如铝基体、孔洞、夹杂物）具有不同的质量吸收系数和密度，因此透射射线强度能够反映材料内部密度的差异，这是工业CT区分缺陷与基体的物理依据 [[S45,S5]]。

为便于定量比较不同区域的密度差异，工业CT常引入CT值（亨氏单位，Hu）作为标准化参数，其计算以水或空气的衰减系数为基准 [[S45]]。

### 投影采集与断层重建

工业CT通过在被检测工件周围360°范围内采集多组投影数据实现断层成像。对每个旋转角度，探测器记录穿过工件的X射线强度分布，形成一个一维或二维的投影。将足够多角度的投影数据输入计算机后，采用图像重建算法反演出工件断层面内各点的衰减系数 \(\mu(x,y)\)，生成二维断层灰度图像；将一系列连续断层切片按空间位置叠加、插值，即可重建出工件的完整三维结构模型 [[S42,S51,S28,S5]]。

常见的重建算法包括：
- **迭代法**：通过求解一系列以衰减系数为未知数的线性方程组，逐步逼近真实衰减系数分布 [[S42,S5]]；
- **滤波反投影算法**：在反投影操作之前对投影数据施加滤波，以消除星形伪影并提升图像质量 [[S42,S3]]；
- **Feldkamp三维重建算法**：针对锥束CT场景开发的近似三维重建方法，是目前工业锥束CT中最常用的重建算法之一 [[S5]]。

### 系统组成

工业CT检测系统通常由四个核心子系统组成 [[S36,S32]]：
1. **X射线源**：产生用于穿透工件的X射线束；
2. **机械扫描与载物台系统**：实现工件精确定位、旋转及平移运动；
3. **探测器系统**：接收透过工件的X射线并将其转化为电信号；
4. **计算机与图像重建系统**：控制扫描过程，执行图像重建算法，生成断层图像和三维模型。

![工业CT检测系统整体组成示意图，标注有射线源、旋转机械载物台、平板探测器、计算机控制模块四大核心部件 [[S32]]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8694f71e-51dd-4bf9-b064-2030c1c7bb15/resource)

## 设备分类

根据X射线束的几何形态和探测器配置方式，面向压铸检测的工业CT系统主要分为三类 [[S24,S56,S36]]。

### 锥束工业CT

锥束工业CT采用二维面探测器（如平板探测器），X射线以锥形体束形式覆盖待检测工件。工件只需在载物台上旋转360°，即可在一次扫描中获取完整的三维投影数据，扫描效率远高于传统扇束CT [[S24,S56]]。该类设备符合国内 GB/T 29070-2012 检测规范要求，典型商用设备（如ICT-450）的焦点尺寸为0.4 mm，投影采样幅数≥1600幅，体素尺寸可低至0.083 mm，特别适用于中小尺寸铝合金压铸件的快速全尺寸三维缺陷检测，是目前压铸行业应用最广泛的CT类型 [[S37,S20]]。

### 扇束工业CT

扇束工业CT采用单排或线阵探测器，X射线经准直形成薄扇形束，只覆盖工件的一个断层面。扫描时需要工件同步进行机械平动与旋转，逐层采集每个断层所需的投影数据，扫描速度较锥束CT慢。但由于射线集中在较薄的断层面内，大厚度工件的射线利用率和信噪比更高，适合大尺寸、大厚度重型铝合金压铸件的逐层高精度扫描 [[S24,S56,S36]]。

### 微焦点工业CT

微焦点工业CT采用微米级焦点的X射线源，空间分辨率可达微米甚至亚微米量级。此类设备可观测压铸件内部的微米级显微孔洞、第二相粒子分布等微观特征，适用于压铸材料研发阶段的微观组织定量分析以及小型精密压铸零部件的高精度几何量测量。主流商用设备（如GE phoenix v|tome|x c型）最大输出电压可达240 kV，能够穿透常规厚度的铝合金试样并实现亚微米级三维成像 [[S5,S47,S45]]。

![压铸行业常用GE phoenix v|tome|x c型工业CT检测设备实拍图，载物台上放置待检测铝合金变速箱壳体压铸件 [[S47]]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2c13871-60d0-4f29-9d03-e37d0af0a282/resource)

## 核心性能参数

工业CT的核心性能参数决定了其对压铸件内部缺陷的检出能力和检测效率。

### 主要参数范围

| 参数类别 | 典型值或范围 | 说明 |
|---------|------------|------|
| X射线管电压 | 160 kV – 450 kV（常规），225 kV（微焦点） | 决定穿透能力，根据工件材料和厚度选择 [[S27,S51,S19]] |
| 空间分辨率 | 1 lp/mm（常规），亚微米级（微焦点） | 分辨微小细节的能力 [[S58,S51,S5]] |
| 密度分辨率 | ≥0.1%（常规），0.5%（大型工程CT） | 区分不同密度材料或缺陷的能力 [[S51,S58]] |
| 可检工件最大回转直径 | 1 – 2.5 m | 取决于CT系统规格 [[S58]] |
| 可检工件最大高度 | 2 – 8 m | 取决于CT系统规格 [[S58]] |
| 单层扫描时间 | 约3 min/层 | 典型值，大工件整机扫描耗时可达数十分钟至数小时 [[S58,S22]] |

### 空间分辨率与密度分辨率的互斥关系

在固定辐射剂量条件下，工业CT的空间分辨率与密度分辨率是一对互斥指标：提高空间分辨率（追求更小像素和更清晰的细节边界）会降低密度分辨率（区分微小密度差异的能力）；反之亦然 [[S62]]。在具体检测中，需根据缺陷类型特征（如关注显微孔洞还是大面积疏松区域）合理偏重或折中设置参数。

## 操作条件与影响因素

### 管电压与管电流

工业CT检测中，管电压直接决定X射线的穿透能力。铝合金压铸件检测需根据壁厚匹配管电压：厚壁大尺寸压铸件选择高电压配置以保证射线穿透性；薄壁精细压铸件宜选择适配低电压，以保障密度分辨率。同时，配套调整管电流和积分时间，可进一步优化投影采集信号质量 [[S1,S51,S34]]。以铝合金机匣类压铸件为例，实测典型配置为：管电压400 kV，管电流1.7 mA，积分时间500 ms [[S19]]。

### 滤波

在X射线源出射窗口配置金属滤波片（常为铝、铜等薄片），可过滤掉X射线谱中的低能软X射线成分，产生线束硬化效果，降低射束硬化伪影，减少低能光子被铝合金表层过度吸收所带来的图像不均匀噪声，有效提升图像信噪比 [[S18,S3]]。

### 投影采样幅数

投影采集的幅数直接影响成像重建质量。投影幅数不足会导致采样不充分，引入伪影，降低缺陷识别精度；而过高的幅数虽有利于提升对微小缺陷的细节分辨能力，但会显著增加扫描时间。常规铝合金压铸件检测的投影采样幅数通常不低于1600幅，可在扫描效率与成像质量之间取得平衡 [[S19,S3]]。

### 典型检测参数示例

以铝合金复杂机匣类压铸件为对象，ZXVoxel D-450型工业CT的完整检测配置如表所示 [[S19]]：

| 参数 | 设定值 |
|------|-------|
| 管电压 | 400 kV |
| 管电流 | 1.7 mA |
| 焦点尺寸 | 0.4 mm |
| 积分时间 | 500 ms |
| 射线源-探测器距离（SDD） | 1300 mm |
| 射线源-样品距离（SOD） | 800 mm |
| 扫描方式 | 锥束偏置 |
| 投影采样幅数 | 1600 |

## 在压铸/铸造中的应用

### 内部缺陷检测

工业CT是压铸件内部缺陷三维定量检测的核心手段，可识别的典型缺陷类型及其CT图像特征包括 [[S20,S23,S51,S60]]：

- **气孔**：边缘锐利的类圆形暗斑；
- **缩孔**：中心黑度值突变的团簇状显影；
- **纤维状缩松**：不规则连续性黑色区域；
- **树枝状缩松**：枝晶状高黑度区域；
- **海绵状缩松**：云雾状弥散分布特征，无明显边界；
- **非金属夹杂**（含氧化夹杂）：通过密度灰度差异识别高密度夹杂物。

工业CT的密度分辨率可达0.1%以上，能够有效分辨基体与上述各类缺陷之间的密度差异 [[S51,S20]]。公开数据显示，在实际工业检测中，工业CT初检准确率可达99.4%，复核后可实现100%检测准确率 [[S58]]。

![工业CT识别铝合金排气肘压铸件内部收缩空洞缺陷的量化检测结果示例，附该缺陷的体积、孔隙率、等效密度等参数 [[S21]]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/518805ea-3ba2-4d09-8f9b-e0841dca258d/resource)

### 海绵状疏松的计算机辅助分级

工业CT对铝合金铸件海绵状疏松的分级可参考HB5396-88铝合金铸件X射线照相检验海绵状疏松标准和标准样品。通过对CT切片中海绵状疏松的面积和密度分布特征进行统计量化分析，可实现计算机辅助自动定级：不同厚度的标准样品中，疏松面积随缺陷级别从1级到5级基本呈单调递增 [[S15,S10,S54]]；CT分级结果与传统X射线照相人工分级结果一致性高，具备快速、准确、重现性好等优点 [[S50,S10]]。

### 尺寸测量与逆向工程

工业CT无需剖切压铸件即可获取完整三维体数据。经投影重建、降噪后处理与表面提取，可生成包含铸件内外全部结构表面的点云数据，对复杂型腔压铸件内部的隐藏特征、壁厚、内腔尺寸进行直接拟合测量，消除了传统三坐标测量和激光扫描无法触及内部型腔的检测盲区 [[S31,S41,S46]]。生成的全结构点云可直接用于逆向工程，输出完整包含内外形貌的CAD模型，支撑复杂压铸件的模具复刻、几何尺寸公差分析等应用 [[S6,S24,S53]]。

### 孔隙率定量分析

快速工业CT可对高压压铸铝合金部件进行孔隙率定量评估。公开实验数据显示，不同工艺条件下生产的A356类Al-Si合金压铸件，部件整体孔隙率处于0.33%~1.05%区间；X射线显微CT与金相法的对比实验验证，工业CT对20 μm以上的微小孔隙具备可靠检出能力，且可通过密度灰度差异识别宏观尺度的元素成分不均（宏观偏析）区域 [[S13,S25,S55]]。

## 与其他无损检测方法的对比

### 三维表征能力

工业CT是压铸件无损检测方法中唯一具备完整三维断层重建与体积定量测量能力的技术 [[S31,S24]]。其他常见方法均存在表征维度的限制：
- **二维X射线探伤（DR）** 仅能输出二维投影图像，存在前后缺陷重叠的问题 [[S52,S61]]；
- **超声检测** 仅能提供一维定位信号，无法形成缺陷的三维形态图像 [[S61,S9]]；
- **渗透检测** 和 **磁粉检测** 仅能显示表面或近表面缺陷的二维形貌 [[S4,S39]]。

### 综合特性对比

| 对比维度 | 工业CT | 二维X射线探伤（DR） | 超声检测 | 渗透检测 | 磁粉检测 |
|---------|--------|-------------------|---------|---------|---------|
| 三维表征能力 | 完整三维断层重建与体积定量 | 仅二维投影，缺陷前后重叠 | 仅一维定位信号，无三维成像 | 仅表面二维形貌 | 仅表面/近表面二维形貌 |
| 最小可检出缺陷 | 0.05 mm级裂纹 | 约为壁厚的1%~2% | 随厚度变化 | 开口宽度0.01 mm级 | 长0.1 mm级近表面裂纹 |
| 检测效率（单件） | 数分钟至数十分钟 | 几秒至数分钟 | 自动化后较快 | 慢（多工序） | 慢（多工序） |
| 设备与检测成本 | 显著高于其他方法 | 中等 | 较低 | 最低 | 较低 |
| 对复杂内腔/壁厚不均件的适配性 | 完全适配，逐层扫描无盲区 | 影像重叠影响判读，复杂位置易漏检 | 仅适用简单形状、壁厚均匀件 | 无法探测封闭内腔内部 | 仅检出铁磁性材料表面/近表面缺陷 |
| 操作门槛 | 需掌握扫描参数设置与三维图像解读 | 需考取射线操作资质 | 需经验判读反射信号 | 简单 | 简单 |

上述对比综合依据 [[S30,S61,S4,S39,S58,S20,S9,S35,S49,S52]]。

### 工业CT的独特优势

相较于其他无损检测方法，工业CT具备以下核心优势 [[S51,S52,S50,S58,S20]]：
- 完全消除传统二维射线探伤的影像重叠问题，直接获取任意断层的无遮挡内部结构；
- 精确测量缺陷的三维空间位置、实际体积与形貌特征；
- 密度分辨率可达0.1%以上，检测过程不受复杂内腔结构干扰，无常规检测方法的盲区问题；
- 初检准确率可达99.4%，复核后可达100%检测准确率；
- 支持海绵状疏松等缺陷的计算机辅助自动分级，结果重现性好。

### 工业CT的局限性

当前工业CT在压铸量产场景中的应用仍存在以下局限 [[S30,S61,S57,S29,S17,S22]]：
- 整机采购与日常检测成本显著高于常规无损检测方法；
- 单件完整扫描与三维重建耗时较长，明显慢于二维X射线实时成像检测；
- 民用级经济型工业CT系统的空间分辨率有限，难以检出亚微米级微小缺陷；
- 在汽车压铸生产线上，当前主要局限于材料研发阶段抽检和高价值安全类压铸件的质量验证，尚未实现全件在线量产全检。

## 相关标准与规范

与压铸件工业CT检测相关的标准包括：
- **GB/T 36589《铸件 工业计算机层析成像(CT)检测》**：国内压铸件CT检测的核心标准，明确规定了铝、镁合金压铸件内部孔隙、偏析、夹杂的定量检测参数设置要求和缺陷定量评级规则 [[S14]]；
- **GB/T 29070-2012**：工业锥束CT检测的执行规范，在多篇压铸件CT检测研究文献中被实际引用 [[S37,S20]]；
- **ASTM E1441-1993《Standard Guide for Computed Tomography (CT) Imaging》**：早期通用工业CT成像基础指南，在铝合金铸件缺陷分级相关研究中被引用，为铸件CT检测的通用流程提供参考 [[S50]]；
- **HB5396-88《铝合金铸件X射线照相检验海绵状疏松标准和标准样品》**：虽是X射线照相标准，但其分级方法被工业CT对铝合金铸件海绵状疏松的计算机辅助分级研究采用为对照依据，验证了CT分级与X射线照相分级结果的一致性 [[S50,S10,S15]]。

## Sources
- S44: [2988569_工业CT](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be1b69d5-a840-41f9-8ba4-3b7ab11cc5a9/resource) (`be1b69d5-a840-41f9-8ba4-3b7ab11cc5a9`)
- S24: [0106_45863d73c1329812_Industrial_computed_tomography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5bda5606-5ef0-47e2-b627-970666b90606/resource) (`5bda5606-5ef0-47e2-b627-970666b90606`)
- S36: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/989ee977-c7c1-4cd1-8458-b668a099de6b/resource) (`989ee977-c7c1-4cd1-8458-b668a099de6b`)
- S1: [2988569_工业CT](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/085e17a6-601a-4030-a446-6fd12b60dcd3/resource) (`085e17a6-601a-4030-a446-6fd12b60dcd3`)
- S42: [C_SiC复合材料孔隙缺陷量化识别及其对抗弯性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b818b74b-1dc0-4f71-a197-510db79f09a1/resource) (`b818b74b-1dc0-4f71-a197-510db79f09a1`)
- S45: [渐进堵塞条件下多孔沥青混合料细观结构特征演变及对排水性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0ea5177-5402-4242-8263-7e1d18bc43ad/resource) (`c0ea5177-5402-4242-8263-7e1d18bc43ad`)
- S5: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a9f3325-f9be-4c55-8f7c-87aafa1d41ee/resource) (`1a9f3325-f9be-4c55-8f7c-87aafa1d41ee`)
- S51: [ZL204合金疏松特征及成因分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cea7ab60-b3bc-4d47-a575-d7b72d4e2c05/resource) (`cea7ab60-b3bc-4d47-a575-d7b72d4e2c05`)
- S28: [ZL204合金疏松特征及成因分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7462ed79-62f3-4046-8408-ff1eee77e805/resource) (`7462ed79-62f3-4046-8408-ff1eee77e805`)
- S3: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12bab1ce-3e49-43ae-a42a-e71b5814383c/resource) (`12bab1ce-3e49-43ae-a42a-e71b5814383c`)
- S32: [图2.6 工业CT检测示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8694f71e-51dd-4bf9-b064-2030c1c7bb15/resource) (`8694f71e-51dd-4bf9-b064-2030c1c7bb15`)
- S56: [0233_5ddd3de0bab1d2c8_Cone_beam_reconstruction](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efc98f94-ca1d-4682-94f9-34fcade37eeb/resource) (`efc98f94-ca1d-4682-94f9-34fcade37eeb`)
- S37: [基于ProCAST的复杂形貌耐热不锈钢薄壁件模拟与工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b3734d4-52c0-4ca6-a95d-acd561ac01cf/resource) (`9b3734d4-52c0-4ca6-a95d-acd561ac01cf`)
- S20: [基于ProCAST的复杂形貌耐热不锈钢薄壁件模拟与工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/478aeeb4-e0f9-4e55-bee9-cfa569659d2a/resource) (`478aeeb4-e0f9-4e55-bee9-cfa569659d2a`)
- S47: [图14 在工业CT机上检测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2c13871-60d0-4f29-9d03-e37d0af0a282/resource) (`c2c13871-60d0-4f29-9d03-e37d0af0a282`)
- S27: [铝合金水泵座压铸模镶块冷却水道结构改进与压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/678eb6ac-4dd0-4cf0-b4ea-91a2dafe9e9d/resource) (`678eb6ac-4dd0-4cf0-b4ea-91a2dafe9e9d`)
- S19: [表2.2 铝合金机匣铸件CT测试参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/453d97da-4ad1-4382-8726-3d54f0beb102/resource) (`453d97da-4ad1-4382-8726-3d54f0beb102`)
- S58: [2988569_工业CT](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f534c912-33fd-470d-98f5-cce217b845db/resource) (`f534c912-33fd-470d-98f5-cce217b845db`)
- S22: [0083_62e008975a13e5a6_X射线断层成像测量技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55be40b5-f986-4539-b6cb-dd7955cfd949/resource) (`55be40b5-f986-4539-b6cb-dd7955cfd949`)
- S62: [2988569_工业CT](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcef9b6b-7c5e-4c66-a0e0-ced69be535ee/resource) (`fcef9b6b-7c5e-4c66-a0e0-ced69be535ee`)
- S34: [工业CT在印制板孔隙率无损检测中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91f2581c-d767-4c48-9bdb-06ddcdb15d73/resource) (`91f2581c-d767-4c48-9bdb-06ddcdb15d73`)
- S18: [0168_694dfa42b2c66504_X-ray](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44007b1d-da68-41bd-852a-861678239245/resource) (`44007b1d-da68-41bd-852a-861678239245`)
- S23: [基于ProCAST的复杂形貌耐热不锈钢薄壁件模拟与工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/581d48fe-64fe-49ca-84d7-b384eb4ec1a9/resource) (`581d48fe-64fe-49ca-84d7-b384eb4ec1a9`)
- S60: [大规格2A14铝合金铸锭氧化夹杂缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa16d626-969f-4a52-944f-1b1efe1bbcce/resource) (`fa16d626-969f-4a52-944f-1b1efe1bbcce`)
- S21: [排气肘铸件工业CT检测结果，显示收缩空洞缺陷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/518805ea-3ba2-4d09-8f9b-e0841dca258d/resource) (`518805ea-3ba2-4d09-8f9b-e0841dca258d`)
- S15: [工业CT对铝合金铸件海绵状疏松分级方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3565cdaa-967f-47f2-9367-0c1a4dd7d5e2/resource) (`3565cdaa-967f-47f2-9367-0c1a4dd7d5e2`)
- S10: [工业CT对铝合金铸件海绵状疏松分级方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/247eb4d5-7e74-4ba8-b7ae-4f60ade4aa9a/resource) (`247eb4d5-7e74-4ba8-b7ae-4f60ade4aa9a`)
- S54: [工业CT对铝合金铸件海绵状疏松分级方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dfc5a4a1-655b-4b9e-a3b9-0587c85ea74b/resource) (`dfc5a4a1-655b-4b9e-a3b9-0587c85ea74b`)
- S50: [工业CT对铝合金铸件海绵状疏松分级方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccb13fdd-eb94-4f35-85b8-0346195cc1d4/resource) (`ccb13fdd-eb94-4f35-85b8-0346195cc1d4`)
- S31: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82586d51-7509-4525-847a-0e3a0e065e3f/resource) (`82586d51-7509-4525-847a-0e3a0e065e3f`)
- S41: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7699dfe-7628-4040-bfdc-62212951ff50/resource) (`a7699dfe-7628-4040-bfdc-62212951ff50`)
- S46: [0083_62e008975a13e5a6_X射线断层成像测量技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0ef1431-d885-4d25-bdc6-04ba5ee36ed5/resource) (`c0ef1431-d885-4d25-bdc6-04ba5ee36ed5`)
- S6: [模具制造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d259aed-c811-4791-8bc1-0faf9b50c6df/resource) (`1d259aed-c811-4791-8bc1-0faf9b50c6df`)
- S53: [0106_45863d73c1329812_Industrial_computed_tomography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9a6d766-070b-461a-a8cb-08add919a55e/resource) (`d9a6d766-070b-461a-a8cb-08add919a55e`)
- S13: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31cf34bd-2985-49b5-8583-e5b71c71a8b7/resource) (`31cf34bd-2985-49b5-8583-e5b71c71a8b7`)
- S25: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e8abb1b-9ff1-45af-ad53-23df40ea0ee6/resource) (`5e8abb1b-9ff1-45af-ad53-23df40ea0ee6`)
- S55: [effect of cooling process on porosity in the aluminum alloy automotive w__3a2b5190f1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed2a8bcc-e174-4b9f-9c67-f27393021d60/resource) (`ed2a8bcc-e174-4b9f-9c67-f27393021d60`)
- S52: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0b58933-d995-4fdc-8b8a-df8c75faa017/resource) (`d0b58933-d995-4fdc-8b8a-df8c75faa017`)
- S61: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb897efc-a6e1-4b49-8bdb-f54197e3db95/resource) (`fb897efc-a6e1-4b49-8bdb-f54197e3db95`)
- S9: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2045deba-9085-43f6-a305-6c846d955c6e/resource) (`2045deba-9085-43f6-a305-6c846d955c6e`)
- S4: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19ff374d-680f-4e32-8fa3-fea57f912f62/resource) (`19ff374d-680f-4e32-8fa3-fea57f912f62`)
- S39: [木塑复合材料的表面处理与胶接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a390b7dd-e202-4ba1-9c14-d8539527c091/resource) (`a390b7dd-e202-4ba1-9c14-d8539527c091`)
- S30: [表 5-23 常见的铸造缺陷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ff25475-c963-4501-b9f1-fcecc6a1b90f/resource) (`7ff25475-c963-4501-b9f1-fcecc6a1b90f`)
- S35: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/972094cb-2ac5-46e0-9523-cbadbbaca479/resource) (`972094cb-2ac5-46e0-9523-cbadbbaca479`)
- S49: [适用于不同形状铸件的无损检测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cca5e8c9-d27b-4d29-a880-e8179a384ad8/resource) (`cca5e8c9-d27b-4d29-a880-e8179a384ad8`)
- S57: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1a3def8-0954-411e-afe5-fb19b3093f04/resource) (`f1a3def8-0954-411e-afe5-fb19b3093f04`)
- S29: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/759dd8fd-f117-4c6e-b4d4-de78f0ae03af/resource) (`759dd8fd-f117-4c6e-b4d4-de78f0ae03af`)
- S17: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/415d60d6-5ed1-490a-8977-29871e4a7609/resource) (`415d60d6-5ed1-490a-8977-29871e4a7609`)
- S14: [GBT+13821（锌合金压铸件）-2023.pdf-c97b7b51-db31-45ae-aa6a-7937c1e7cd89](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3302f210-ce90-43c3-ab99-568272124048/resource) (`3302f210-ce90-43c3-ab99-568272124048`)