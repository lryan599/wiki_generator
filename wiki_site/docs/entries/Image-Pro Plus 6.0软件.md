---
version: "v1"
generated_at: "2026-06-18T12:38:15+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 23
  source_quality_score: 0.87
  freshness_score: 0.87
  evidence_coverage_score: 1.0
---

## 概述与定义

Image-Pro Plus 6.0是由Media Cybernetics Inc.（美国马里兰州罗克维尔）开发的专业图像处理与分析软件，核心定位为面向科研领域的定量图像分析工具[[S8,S1,S10,S22,S31]]。该软件具备丰富的测量功能与自定义扩展能力，主要用于显微图像的采集、增强、处理和多维度数据统计[[S1]]。

在压铸与材料科学领域，Image-Pro Plus 6.0被广泛用作金相定量分析的核心工具，可完成晶粒度测量、二次枝晶臂间距统计、缩松缺陷比例计算以及工业CT切片的多阈值分割等任务。

## 核心功能

Image-Pro Plus系列软件的通用图像处理流程包含五个核心步骤：图像强度调整、对比度校正、锐化滤波、图像展平、目标粒子计数[[S20]]。上述流程支撑了以下主要功能模块：

| 功能模块 | 说明 |
|----------|------|
| 图像采集与增强 | 支持多种格式显微图像导入，提供对比度校正、展平、锐化等预处理操作 |
| 自动识别与测量 | 可自动识别晶粒、颗粒等目标对象，获取面积、周长、等效直径等参数 |
| 阈值分割 | 内嵌单固定阈值、双固定阈值、Otsu自动阈值等多类分割算法 |
| 三维灰度提取 | 可提取工业CT切片的三维灰度信息，配合多阈值分割区分不同介质 |
| 统计分析 | 提供晶粒尺寸分布、形态因子、变异系数等统计功能 |

## 在压铸检测中的关键应用

### 二次枝晶臂间距（SDAS）测量

Image-Pro Plus 6.0在压铸铝合金SDAS测量中已有完整应用案例[[S26]]。

**测量原理**：采用截线法，在适当放大倍数的金相图像上，通过设定已知长度的测量线段，统计该线段上穿过的二次枝晶臂总数，以此计算平均间距。

**计算公式**：
λ = L / (M · N)[[S26]]

式中，λ为二次枝晶臂间距，L为测量线段总长度，M为金相观测放大倍数，N为线段范围内的二次枝晶臂总数。部分研究采用截取法并以单组枝晶的SDAS取均值，对应公式为λ = [Σ(L/(n-1))]/m，其中L为单组二次枝晶总长度，n为该组内二次枝晶臂个数，m为统计的枝晶组总数[[S2]]。

**试样制备流程**：
1. 依次使用400#至2000#水砂纸逐级粗磨、精磨；
2. 使用1.5μm和0.5μm粒度金刚石抛光剂进行镜面抛光；
3. 采用3强酸腐蚀剂腐蚀，获取清晰的树枝晶形貌；
4. 导入软件后进行截线法测量[[S26]]。

**统计要求**：单组测量须保证不少于20个二次枝晶臂样本，最终取多次测量的平均值[[S26]]。

![图2-8 ZL114A合金二次枝晶臂形态示意图，标注SDAS测量维度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81120436-9b7f-4d99-98c0-916a29719364/resource)

### 基于平均等效圆面积D公式的晶粒尺寸测量

Image-Pro Plus 6.0在真空压铸Cu-Ni-Si-Co-Zr合金的晶粒尺寸表征中已获验证[[S27,S13,S7]]。

**公式定义**：
D = 2√(Aᵢ/π)[[S27]]

式中，Aᵢ为软件识别统计得到的单个晶粒面积。该公式以等效圆面积法原理推算晶粒的平均当量直径。

**标定规则**：
- 每个样品选取5个互不重叠的观测区域；
- 每个区域统计不少于100个有效晶粒[[S27,S13]]；
- 可通过预设筛选规则过滤面积、周长小于阈值的对象，排除共晶组织与夹杂物的干扰[[S19]]。

**实测数据**（真空压铸Cu-Ni-Si-Co-Zr合金）[[S27]]：

| 处理状态 | 平均晶粒尺寸 (μm) |
|----------|-------------------|
| 真空压铸态 | 10.8 ± 1.9 |
| 900℃固溶处理 | 12.5 ± 1.2 |
| 950℃固溶处理 | 21.5 ± 3.5 |

### CT切片三维灰度提取

在材料CT图像处理研究中，Image-Pro Plus 6.0可提取工业CT切片的全三维灰度信息，经内嵌多阈值分割方法区分不同介质的灰度区间后，将切片数据导入AVIZO软件即可完成三维模型重构[[S28]]。该技术路径已用于煤等多孔介质的CT分析，可直接迁移至压铸件工业CT检测，实现内部缩孔、气孔类缺陷的灰度精准分割与体积定量计算[[S28]]。

### 缩松缺陷定量评定

Image-Pro Plus 6.0可通过统计金相视场中缩松区域像素总面积与该视场总像素面积之比，直接计算缩松体积分数[[S26]]。该方法符合GB/T 14999.7-2010的铸造缺陷定量评定规范[[S21,S26]]。

## 阈值分割算法

### 内嵌算法汇总

Image-Pro Plus 6.0内嵌多种阈值分割方法[[S28,S30]]：

| 算法类型 | 原理 | 适用场景 | 局限 |
|----------|------|----------|------|
| 单固定阈值二值化 | 手动设定单一灰度阈值划分目标与背景 | 灰度均匀、噪声低的简单二值场景 | 仅支持两相划分，对灰度梯度大的图像误差高[[S30,S4]] |
| 双固定阈值（灰度切片） | 设定两个阈值提取指定灰度区间目标 | 筛选特定灰度属性的组分 | 阈值调试耗时，对灰度重叠度高的多组分图像区分度差[[S30]] |
| 最大类间方差法（Otsu） | 自动寻优使类间方差最大，确定最优阈值 | 前景与背景灰度差异显著的场景 | 全局算法对局部灰度不均匀图像易出现过分割或欠分割[[S28,S24,S6]] |

### Otsu多阈值分割在材料分析中的应用

在金属材料CT切片图像的多相分割中，Image-Pro Plus 6.0内置的Otsu多阈值分割功能可通过自动寻优确定多组最优阈值参数，将金属基体、析出相与孔隙缺陷三类物相分别精准划分，相较传统FCM聚类等算法可显著降低过分割和欠分割误差[[S28,S12]]。

作为功能对比示例，Otsu算法用于煤体CT切片三分类时，可划分如下介质灰度区间：孔隙结构0~67、煤基质67~128、煤杂质128~255[[S28]]。上述示例展示了Otsu多阈值分割在非金属多孔介质中的通用性，对该功能向压铸合金多相组织分割的迁移具有参考价值。

## 测量标定与参数设置

使用Image-Pro Plus 6.0进行金相定量测量前，须匹配所用显微物镜的放大倍率完成像素与实际物理长度的标定操作，生成对应标尺后方可保证尺寸测量结果的溯源性[[S28]]。

关键测量参数控制要求[[S26,S27,S19]]：

| 测量项目 | 推荐视场数 | 最小统计样本量 | 说明 |
|----------|-----------|---------------|------|
| 晶粒尺寸 | 5个区域 | ≥100个晶粒 | 使用平均等效圆面积D公式计算 |
| SDAS | — | ≥20个二次枝晶臂 | 截线法，取多次测量平均值 |
| 缩松面积比 | 选定视场 | — | 缩松像素面积/总视场像素面积 |

## 关联标准与规范

Image-Pro Plus 6.0的自动图像分析功能可适配以下标准：

- **ASTM E112**：金属平均晶粒度测定方法[[S18,S32,S5]]
- **ASTM E1382**：半自动/自动图像法测定多晶金属平均晶粒度[[S32]]
- **GB/T 6394**：金属平均晶粒度测定法
- **JB/T 7946.4-1999**：铸造铝铜合金晶粒度标准[[S14]]
- **GB/T 14999.7-2010**：高温合金试样显微疏松定量评定[[S21,S26]]

## 局限与注意

- Otsu全局阈值算法对局部灰度分布不均匀的图像，单独使用时易出现过分割或欠分割问题，需结合滑动窗口实现局部自适应阈值优化[[S24,S12]]；
- 双固定阈值算法参数调试耗时，对灰度重叠度高的多组分金相图像区分度差[[S30]]；
- 所有定量测量须在标定完成后方可进行，标定误差将直接影响测量结果的准确性[[S28]]。

## Sources
- S8: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e5d8710-11fd-4186-8a3c-41f974403693/resource) (`5e5d8710-11fd-4186-8a3c-41f974403693`)
- S1: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02b99a26-0c4b-4fe3-a80d-e939128ee765/resource) (`02b99a26-0c4b-4fe3-a80d-e939128ee765`)
- S10: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68ca50b8-6217-47b1-bafc-880fb4c02fe6/resource) (`68ca50b8-6217-47b1-bafc-880fb4c02fe6`)
- S22: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc771273-f841-4a06-ad20-feeb30a11ac4/resource) (`cc771273-f841-4a06-ad20-feeb30a11ac4`)
- S31: [additive manufacturing of high temperature alloys__3a36906d49](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc1d0ef4-b886-47a5-bedc-1e01d3e18720/resource) (`fc1d0ef4-b886-47a5-bedc-1e01d3e18720`)
- S20: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f1bed08-f2f1-4c4c-bc19-0079c6f0d21a/resource) (`9f1bed08-f2f1-4c4c-bc19-0079c6f0d21a`)
- S26: [ZL114A合金薄壁件充型能力及缩松缺陷倾向的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e63a948f-d7ff-4f67-b8cc-c40014b37a70/resource) (`e63a948f-d7ff-4f67-b8cc-c40014b37a70`)
- S2: [机械振动对真空低压铸造ZL114A微观组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ce49bd5-2e48-402b-99c7-7c94b4316760/resource) (`0ce49bd5-2e48-402b-99c7-7c94b4316760`)
- S27: [热处理工艺对真空压铸Cu-Ni-Si-Co-Zr合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6bc6e3c-f35e-4d57-bfd6-504ae9c5a9e6/resource) (`e6bc6e3c-f35e-4d57-bfd6-504ae9c5a9e6`)
- S13: [热处理工艺对真空压铸Cu-Ni-Si-Co-Zr合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73d2b4b9-8e55-43f9-a6c8-74d7b6e6382a/resource) (`73d2b4b9-8e55-43f9-a6c8-74d7b6e6382a`)
- S7: [随流半固态流变模锻技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/588420ee-2098-45a9-8f85-f491f1dbf35d/resource) (`588420ee-2098-45a9-8f85-f491f1dbf35d`)
- S19: [倾转-振动法制备半固态浆料及微观组织的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9dc0f2a9-ad67-4bd3-9c7d-e51bc34cff6a/resource) (`9dc0f2a9-ad67-4bd3-9c7d-e51bc34cff6a`)
- S28: [原位赋存环境下煤体结构损伤演化机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e840670f-76bf-4135-9d1f-f03c2cdfc424/resource) (`e840670f-76bf-4135-9d1f-f03c2cdfc424`)
- S21: [ZL114A合金薄壁件充型能力及缩松缺陷倾向的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b359c110-2c45-49d6-b65b-cbf94ea03b7b/resource) (`b359c110-2c45-49d6-b65b-cbf94ea03b7b`)
- S30: [机械加工工艺基础工程材料及机械制造基础3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb266a7d-6338-4d48-9f79-88f84d094a85/resource) (`fb266a7d-6338-4d48-9f79-88f84d094a85`)
- S4: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cb3884f-6faf-4a7b-bebc-35fe0ef67e64/resource) (`4cb3884f-6faf-4a7b-bebc-35fe0ef67e64`)
- S24: [C_SiC复合材料孔隙缺陷量化识别及其对抗弯性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da480dcf-848d-460e-94ce-9e37ee7625fd/resource) (`da480dcf-848d-460e-94ce-9e37ee7625fd`)
- S6: [机械加工工艺基础工程材料及机械制造基础3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5769f55f-00ff-45c0-ace6-ddaa6302ca43/resource) (`5769f55f-00ff-45c0-ace6-ddaa6302ca43`)
- S12: [C_SiC复合材料孔隙缺陷量化识别及其对抗弯性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f6a9de5-2a59-4b37-9453-c18fb6413c90/resource) (`6f6a9de5-2a59-4b37-9453-c18fb6413c90`)
- S18: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94e25254-34cd-4606-b3ad-7de60902f71f/resource) (`94e25254-34cd-4606-b3ad-7de60902f71f`)
- S32: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff380b8c-8e9d-44a1-993f-44f0fd0e8ff9/resource) (`ff380b8c-8e9d-44a1-993f-44f0fd0e8ff9`)
- S5: [ASTM 标准代号：化学分析与晶粒尺寸测试](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e4823c1-78a1-41e5-8c03-9cc0fa1756b5/resource) (`4e4823c1-78a1-41e5-8c03-9cc0fa1756b5`)
- S14: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74820f01-87ee-4e3a-8d38-f514003fa350/resource) (`74820f01-87ee-4e3a-8d38-f514003fa350`)