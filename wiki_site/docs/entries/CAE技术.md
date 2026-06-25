---
version: "v2"
generated_at: "2026-06-18T05:33:40+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 72
  source_quality_score: 0.86
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

计算机辅助工程（Computer-Aided Engineering，简称CAE技术）是通过计算机软件对工程和产品进行仿真与分析，实现工程全生命周期管理的计算机技术。其核心在于整合设计、分析与制造各环节的数据，借助有限元分析、多体动力学、计算流体动力学（CFD）、多物理场耦合仿真以及优化设计等手段，对产品的工作状态和运行行为进行模拟与验证[[S55,S40,S52]]。在先进制造业中，CAE已从专业分析工具成长为制造业信息化体系的关键组成部分，能够大幅替代传统的物理样机验证流程，是现代产品设计和模具开发的核心支撑技术之一[[S55,S40,S16]]。

在注塑成型领域，CAE利用高分子材料学、流变学、传热学、计算力学和计算机图形学建立成型过程的数学物理模型，实现从充填、保压到冷却的全流程仿真，使对注射成型的认知从宏观、定性、静态维度升级到微观、定量、动态维度，从而在模具加工前完成虚拟试模，显著减少实际试模次数[[S51,S66,S59]]。在压铸领域，CAE以有限元、有限差分、边界元等数值计算方法为基础，模拟充型与凝固全流程，预测缩孔、卷气、冷隔等缺陷，辅助优化浇注系统和压铸工艺参数，直接减少试制环节，提升铸件成品率与模具寿命[[S38,S24,S33]]。

## 分类与范畴

CAE技术总体上可分为通用CAE软件与专用CAE软件两大类[[S77]]。

- **通用CAE软件**：可进行结构、流体、振动、传热等多类跨领域仿真分析，典型代表如ANSYS、ABAQUS、NASTRAN等[[S77,S12]]。
- **专用CAE软件**：面向特定工艺开发，如注塑模流分析用Moldflow、Moldex3D，压铸模流分析用FLOW‑3D、ProCAST，焊接仿真用SysWeld等[[S77]]。

根据分析对象和物理场的不同，CAE常见的功能类型包括：

- **结构分析**：对应力、刚度、动态响应、疲劳寿命等进行力学性能仿真，用于强度校核与失效预测[[S12,S40]]。
- **流体仿真（计算流体动力学，CFD）**：基于流体力学控制方程模拟流动与传热过程，用于流场分布、压力损失优化等[[S40,S54]]。
- **热分析**：模拟温度场分布、热传导及相变凝固过程，用于铸造/压铸凝固预测和模具冷却评估[[S24,S40,S27]]。
- **模流分析**：面向塑料熔体或金属液的充型过程，可预测熔接痕位置、气穴分布、充填不平衡等问题，是模具制造行业最常用的CAE细分类型[[S37,S51,S40]]。

**CAE与CAD、CAM的关系**  
CAD（计算机辅助设计）主要完成产品的三维几何造型与结构设计，CAE则基于CAD导出的几何数据进行物理场仿真验证与性能优化，CAM（计算机辅助制造）利用CAD的模型数据生成数控加工刀路和NC代码。三者通过标准数据格式（如IGES、STEP、STL等）实现跨软件数据交互与集成，CAE的分析结果可反向反馈优化CAD设计方案，避免制造环节出现性能缺陷[[S39,S29,S21,S32]]。

## 在注射成型中的应用

注塑CAE将设计或加工方案作为初值导入系统，通过计算机模拟评估结果并反复迭代修正，直至制品的成型质量、生产效率等满足设计要求。其核心功能模块包含流动模拟、冷却模拟、结构分析和纤维取向预测[[S11,S72,S79]]。

- **流动模拟**：预测熔体充填模式、熔接痕位置、气穴（困气）缺陷、所需锁模力等，辅助浇口数量与位置的优化[[S37,S56,S74]]。  
- **冷却模拟**：分析模具、塑料与冷却管道间的热传递，优化冷却系统设计，并关联收缩与翘曲分析[[S72,S74]]。  
- **结构分析与纤维取向预测**：评估制品的强度刚度，预测纤维取向对力学性能和翘曲变形的影响[[S72,S74]]。

在缺陷预测方面，CAE通过以下逻辑实现对关键问题的预先判断：

| 缺陷类型 | CAE预测原理 | 整改方向 |
|----------|-------------|----------|
| 困气（气穴） | 追踪熔体前锋，识别型腔内气体无法排出的聚集区[[S74,S56,S6]] | 增设排气孔、调整浇口位置或流动平衡，将困气转移至非关键区域 |
| 缩痕/缩孔 | 基于体积收缩仿真及保压压力传递分析，识别壁厚突变区域[[S8,S74]] | 协调壁厚均匀性，优化保压曲线 |
| 翘曲变形 | 综合冷却不均、收缩差异与分子/纤维取向效应，输出全域变形量分布[[S8,S72,S74]] | 改进冷却系统，调整工艺参数 |
| 熔接痕 | 跟踪多股熔体前锋交汇位置，结合熔体温度与速度评估熔接质量[[S56,S14,S35]] | 将熔接痕迁移至非受力、非外观区域，或通过提高模温/保压改善强度 |

热流道注塑模具的设计优化通常经历参数化建模、仿真分析以及优化迭代。下图展示了基于SolidWorks参数化建模，经ANSYS Workbench仿真提取设计变量与目标函数，再由Design Explorer完成优化迭代，直至热平衡参数全部达标的CAE优化流程[[S47]]。  

![热流道喷嘴热平衡优化的CAE流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/819aa7f6-5b44-4b01-bc9d-14fa20fb2978/resource)

在工程优化案例中，对于支撑板类塑件，采用优化浇注系统和工艺方案后，塑件总体注射体积收缩率由5.132%降至3.678%，不同开口两侧的体积收缩率差值显著降低，避免了各区域收缩不均导致的翘曲缺陷；原本集中在屏幕开口上方狭窄受力区的熔接痕和气穴缺陷，全部转移至塑件边缘非敏感区域，产品整体强度大幅提升[[S18,S31]]。而对于风机面壳塑件，经CAE联合多目标优化算法迭代后，翘曲变形量降低58.03%，残余应力降低13.67%，实际生产平均翘曲值为2.049 mm，与预测值误差仅为7.321%，有效解决了自动化连续生产中的质量波动问题[[S9]]。

## 在铸件充型与凝固过程中的应用

压铸CAE以数值计算为基础，将高温金属液抽象为三维非稳态、带自由面的不可压缩粘性流体，其充型过程的控制方程以Navier‑Stokes动量方程和连续性质量守恒方程为核心，并采用SOLA‑VOF等方法实现自由表面的精确跟踪；对于高速充型场景，通常引入k‑ε紊流模型描述复杂的湍流流动状态[[S45,S46,S70,S20]]。传热与凝固模拟则以经典非稳态Laplace导热方程为基础，结合成熟的结晶潜热数值处理方法，覆盖金属/铸型内部热传导、对流换热和辐射换热三类基础传热方式[[S45,S67,S41]]。在凝固组织的数值模拟中，主流技术路线是将随机性形核模型与确定性晶粒生长模型耦合，用于预测微观组织演变[[S45,S67]]。

CAE仿真识别充型困气（卷气）的核心判断依据包括：充型过程的最后填充区域为高困气风险区；流场内存在未被金属液完全填充的空腔、再循环流动区或多股金属流交汇形成的封闭区域；局部气体压力远高于标准大气压；金属液出现剧烈紊流与飞溅的区域[[S15,S34]]。

基于仿真结果可形成针对性的整改方案：

| 整改类型 | 具体措施 | 目的 |
|----------|----------|------|
| 浇口优化 | 调整各内浇口截面积比例，优先使底层浇口进料，保证液面平稳上升，避免上层浇口过早参与充型导致飞溅卷气[[S15,S17]] | 消除浇道内空腔和再循环区，降低卷气风险 |
| 排气系统优化 | 将溢流槽、排气槽精准布置在最后充型区域和困气聚集区域，引导气体有序排出[[S30,S62]] | 使铸件主体区域卷气率降至接近0 |
| 工艺参数优化 | 调整压射速度切换曲线，提高压室充满度，避免过早切换高速导致剧烈氧化卷气，并优化充型温度参数[[S63,S15]] | 从源头减少困气生成概率 |

以大型壳体类压铸件为例，经工艺优化后在充型时间t=0.327 s时的模拟充型情况如图所示，熔体温度分布范围为836.0～943.0℃，金属液可快速、均衡地充填至铸件远端，保障全域压力均匀传递，从而大幅降低困气与缩孔生成的概率[[S36]]。  

![变速箱壳体类压铸件优化后充型模拟热图（t=0.327 s）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58ae0249-26e4-4982-a572-a0e839282f29/resource)

除充型模拟外，压铸CAE的典型应用还包括凝固过程与温度场仿真（预测孤立液相区及缩孔缩松缺陷，优化冷却水路与顺序凝固方案）[[S61]]、多循环热平衡仿真（评估模具冷却系统设计合理性和热疲劳风险）[[S57]]、应力/应变场仿真（预测热裂纹和模具热变形趋势）[[S57,S4]]，以及微观组织与力学性能预测（耦合元胞自动机‑有限元模型模拟晶粒生长过程）[[S41,S58]]。

## 核心工作流程

CAE分析遵循前处理、求解器计算、后处理三个不可颠倒的阶段，这是行业通用的标准操作逻辑[[S77,S25,S40]]。

1. **前处理**：导入CAD三维模型、划分网格、设置材料属性、指定边界条件（如压力、温度、换热系数等）。网格尺寸需根据分析对象的最小壁厚确定，材料数据通常从软件内置数据库中选取或自定义[[S53,S25,S68,S26]]。
2. **求解器计算**：新建工作目录，选择分析类型（流场、温度场、结构场或多物理场耦合），设定终止条件、时间步长与存盘间隔，启动求解计算自动迭代。计算过程中可实时查看进度与核心变量的瞬时值[[S19,S25,S27]]。
3. **后处理**：读取计算结果数据，以彩色云图、动画等形式展示充型流动、温度分布、应力分布等仿真结果，支持任意截面剖切、指定点数值提取和缺陷自动预判，辅助技术人员评估方案合理性并输出优化方向[[S25,S27]]。

CAE软件内部通常包含前处理、求解器和后处理三大部分，广义上前处理可剥离独立的三维建模模块，求解和后处理构成CAE本体的计算与分析核心。下图为一典型压铸模CAE软件的结构与数据流示意图[[S78]]。  

![压铸模CAE软件通用结构组成与数据流示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ee1321e0-0614-4dc8-ae47-18bbbb181b10/resource)

## 常见CAE软件工具

### 注塑成型领域

- **Moldflow**：由澳大利亚Moldflow公司开发（现归属Autodesk），1976年发布首套塑料注塑成型流动分析软件，长期主导注塑CAE市场。系列包含AMI（高级成型分析专家）、AMA（塑件顾问）等模块，支持浇口位置、流道与冷却系统设计优化以及工艺参数优化，提供一维、中面、双层面及三维多种网格类型，内置海量材料数据库[[S22,S64,S43]]。
- **华塑CAE**：华中科技大学模具技术国家重点实验室自主开发，支持STL、UNV、INP等多种通用格式，内置上千种注射机参数和丰富的材料物性库，可预测流动前沿位置、熔接痕/气穴位置、温度场、压力场、翘曲变形等，并支持气体辅助注塑成型仿真[[S73,S13]]。
- **Moldex3D**：按工艺复杂程度划分为eDesign Basic、eDesign、Professional、Advanced、Solution Add‑on五个层级，分别对应产品设计师、模具设计师和高级CAE专家等不同用户群，满足从基础到高级的注塑模流分析需求[[S60]]。

### 铸造/压铸领域

主流商用铸造CAE软件的对比见下表[[S5,S10,S76,S23,S71,S26,S28,S1]]。

| 软件 | 开发商 | 算法类型 | 核心特点 |
|------|--------|----------|----------|
| MAGMASOFT | 德国MAGMA | 有限差分/有限元耦合 | 模块化程度高，计算速度快，薄壁件分析能力强，支持几乎所有主流铸造工艺，可完成充型、凝固、显微组织、应力及变形全流程仿真 |
| ProCAST | 美国UES（现法国ESI） | 有限元法（FEM） | 温度场、流场、应力场、电磁场完全耦合，适用于异形复杂构件，前处理网格需借助第三方软件（如HyperMesh），支持砂型、消失模、高压、低压、熔模等多种工艺 |
| AnyCasting | 韩国AnyCasting | 有限差分法（FDM） | 操作界面友好，计算速度超群，支持千万级网格快速剖分，内置覆盖多国标准合金的材料数据库，适用于砂型、高压/低压、离心铸造等几乎所有工艺 |
| 华铸CAE | 华中科技大学 | 有限差分法（FDM） | 国产主流铸造CAE软件，具备自动网格剖分和缺陷定量化预测功能，孔缩预测精度可达95%，支持钢、铁、铝、铜等多种合金的砂型、金属型、离心铸造 |

## 优势与局限性

**优势**  
CAE技术能够大量减少物理样机试制次数，将产品研发周期大幅缩短，降低试模、迭代修改造成的材料与人工成本，提前在虚拟阶段预判潜在设计缺陷，保障最终产品的性能合格率[[S52,S59,S50,S16]]。在注塑和压铸领域，CAE实现了将经验驱动的试错设计转变为基于物理模型和数值计算的科学工程方法，显著提升了模具和工艺设计的可靠性与效率[[S37,S38]]。

**局限性**  
仿真结果的准确度高度依赖于模型假设的合理性，同时受材料参数标定精度、网格划分质量、边界条件设置准确度的多重影响。当前CAE难以完全复现复杂工况下的全部物理变量，其结果仍需通过实际生产验证进行最终确认[[S40,S51,S50]]。在注塑成型CAE分析中，从最初的中面流技术到双面流技术再到实体流技术，由于算法的不完善，三种技术至今仍并存，分析人员在面对厚薄差异较大的制品时需要组合采用不同网格类型以平衡计算效率与精度[[S22,S75]]。

## 相关标准与规范

目前我国尚未发布覆盖全行业的铸造工艺仿真统一系列标准，铸造行业标准化工作仍主要集中在材料、涂层、质量、试验等领域。有关方面正在推进铸造工艺仿真标准化体系建设，拟从仿真环境要求、工作内容、工作流程和仿真结果应用四个维度建立规范，以解决当前仿真应用随意性强、规范性差的问题[[S65]]。在国际层面，ISO、ASTM等标准体系中压铸铝合金的牌号命名与材料性能要求已与各国CAE软件内置的材料物性参数标准实现对接，为仿真输入的材料参数合规性提供了基础支撑；同时，CAE仿真所依赖的有限元、有限差分、控制体积法等数值求解理论体系已纳入通用工程仿真标准框架[[S69,S32]]。

## Sources
- S55: [18884456_CAE技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99871add-f4a0-46d0-84c6-0034272319be/resource) (`99871add-f4a0-46d0-84c6-0034272319be`)
- S40: [模具设计与制造专业英语](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/604413b6-be44-4266-b1c9-6b4f395be5b0/resource) (`604413b6-be44-4266-b1c9-6b4f395be5b0`)
- S52: [Moldflow注塑模流分析从入门到精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/950c6c29-bc4f-4e6f-880f-eb75777e9da1/resource) (`950c6c29-bc4f-4e6f-880f-eb75777e9da1`)
- S16: [高密度模块封装模流仿真技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a7fd23b-acf4-4df9-b835-837b4d2fa639/resource) (`2a7fd23b-acf4-4df9-b835-837b4d2fa639`)
- S51: [2004年中国工程塑料加工应用技术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91c78d1b-27cc-43ab-a967-93c237a922d1/resource) (`91c78d1b-27cc-43ab-a967-93c237a922d1`)
- S66: [2004年中国工程塑料加工应用技术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c09f684e-04cf-42c0-a9b1-9ea3c4edd494/resource) (`c09f684e-04cf-42c0-a9b1-9ea3c4edd494`)
- S59: [基于CAE的某生化仪内支架注塑成型过程模拟及工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aadad58f-42e5-456e-bb54-62d505547ef5/resource) (`aadad58f-42e5-456e-bb54-62d505547ef5`)
- S38: [不同型腔真空度对铸件组织和性能的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c23155a-339f-44d1-86d8-5fa52d08051d/resource) (`5c23155a-339f-44d1-86d8-5fa52d08051d`)
- S24: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38325002-b308-4ab2-9d5f-2317bebdcd11/resource) (`38325002-b308-4ab2-9d5f-2317bebdcd11`)
- S33: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e3191b7-63f2-40a7-9632-1e673c2d3967/resource) (`4e3191b7-63f2-40a7-9632-1e673c2d3967`)
- S77: [Moldflow注塑模流分析从入门到精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecc423fd-a5bb-4f23-a5bb-1eaee82dee7d/resource) (`ecc423fd-a5bb-4f23-a5bb-1eaee82dee7d`)
- S12: [三维建模与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f97c5de-b45d-4bc8-987a-ff3cc61b790b/resource) (`1f97c5de-b45d-4bc8-987a-ff3cc61b790b`)
- S54: [Moldflow注塑模流分析从入门到精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9919e940-8eb6-4ee2-a80e-52afbd67cd08/resource) (`9919e940-8eb6-4ee2-a80e-52afbd67cd08`)
- S27: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c1603cf-1be4-4bca-b6df-6bf644a57b69/resource) (`3c1603cf-1be4-4bca-b6df-6bf644a57b69`)
- S37: [注塑模具设计与制造教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5bbdb627-7278-4b13-802b-42a2322192a1/resource) (`5bbdb627-7278-4b13-802b-42a2322192a1`)
- S39: [模具数字化设计与制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5dfa8f7b-2624-4dce-b7d3-6c3b54129f4e/resource) (`5dfa8f7b-2624-4dce-b7d3-6c3b54129f4e`)
- S29: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47058aae-0fbc-4e04-bfbd-a3444d3eec05/resource) (`47058aae-0fbc-4e04-bfbd-a3444d3eec05`)
- S21: [压铸工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32aeeb36-aaf4-4acd-8b26-0325eae0e064/resource) (`32aeeb36-aaf4-4acd-8b26-0325eae0e064`)
- S32: [application of an integrated cad cae cam system for die casting dies__96a43cb0a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d4649ff-c3d2-4a72-94b2-09dafe778a34/resource) (`4d4649ff-c3d2-4a72-94b2-09dafe778a34`)
- S11: [橡塑模具优化设计技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e6e4078-4893-4f29-adf1-90f11189892c/resource) (`1e6e4078-4893-4f29-adf1-90f11189892c`)
- S72: [塑料注射成型与模具设计指南](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea272046-4602-4274-9ee3-4c476ed25608/resource) (`ea272046-4602-4274-9ee3-4c476ed25608`)
- S79: [塑料注射成型与模具设计指南](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f68a4077-0cdb-4812-88f6-6def6cd9a0c4/resource) (`f68a4077-0cdb-4812-88f6-6def6cd9a0c4`)
- S56: [塑料注射成型与模具设计指南](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ac84b17-8e21-40bc-ba60-c10019d57b0e/resource) (`9ac84b17-8e21-40bc-ba60-c10019d57b0e`)
- S74: [computer aided injection mold design and manufacture__e9a0863baa](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb3831ba-72a0-4ff9-85f9-6e6817fea84a/resource) (`eb3831ba-72a0-4ff9-85f9-6e6817fea84a`)
- S6: [注塑模具设计与制造教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/112e8c64-3d4c-4ad5-8219-c23d1c583c51/resource) (`112e8c64-3d4c-4ad5-8219-c23d1c583c51`)
- S8: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12e03980-7981-4f2e-98a8-c69c5b5ff81e/resource) (`12e03980-7981-4f2e-98a8-c69c5b5ff81e`)
- S14: [复杂注塑模具设计新方法及案例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28c47c84-c16e-4e4c-9140-c359e25f4cfc/resource) (`28c47c84-c16e-4e4c-9140-c359e25f4cfc`)
- S35: [软布基拉链注塑工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/576c121d-e79c-4a85-9ae4-0fd9e48c01a7/resource) (`576c121d-e79c-4a85-9ae4-0fd9e48c01a7`)
- S47: [热流道喷嘴热平衡优化流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/819aa7f6-5b44-4b01-bc9d-14fa20fb2978/resource) (`819aa7f6-5b44-4b01-bc9d-14fa20fb2978`)
- S18: [Moldflow 2015模流分析从入门到精通 升级版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2da6187f-d14d-44e2-8a48-6e33fc3ecbe5/resource) (`2da6187f-d14d-44e2-8a48-6e33fc3ecbe5`)
- S31: [Moldflow 2018模流分析从入门到精通（升级版）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d315622-632b-4dc1-b479-e4477276898e/resource) (`4d315622-632b-4dc1-b479-e4477276898e`)
- S9: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a1a8243-572b-4fe3-87fa-845583d4be8b/resource) (`1a1a8243-572b-4fe3-87fa-845583d4be8b`)
- S45: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ccc9c88-ff84-4ca0-9be6-d78d266e1a8d/resource) (`6ccc9c88-ff84-4ca0-9be6-d78d266e1a8d`)
- S46: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b83f11e-7ab8-4661-a3fa-adc8fef3464b/resource) (`7b83f11e-7ab8-4661-a3fa-adc8fef3464b`)
- S70: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3b86ffc-9e0b-47f2-8261-2dec4a201149/resource) (`e3b86ffc-9e0b-47f2-8261-2dec4a201149`)
- S20: [材料加工工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f5675d5-7a25-4172-84a2-448e13d71595/resource) (`2f5675d5-7a25-4172-84a2-448e13d71595`)
- S67: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2ed0057-9f86-459e-8b26-47e9ca7ddbfa/resource) (`c2ed0057-9f86-459e-8b26-47e9ca7ddbfa`)
- S41: [不同铸造工艺条件下工型异形件凝固组织数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62c2a6a3-f62c-4853-be7b-c6455b170c2d/resource) (`62c2a6a3-f62c-4853-be7b-c6455b170c2d`)
- S15: [CAE在国六发动机缸体缸盖铸件中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a113832-0a68-489b-93fd-3a3077ac8b6f/resource) (`2a113832-0a68-489b-93fd-3a3077ac8b6f`)
- S34: [局部挤压降低压铸发动机支架的气孔缺陷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52a62220-a4c5-41d7-a997-df7f1dd1da0c/resource) (`52a62220-a4c5-41d7-a997-df7f1dd1da0c`)
- S17: [computer aided engineering cae simulation for the design optimization of__3c0fc6c5de](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c7a1b11-e678-4663-a2ec-85ae6958455a/resource) (`2c7a1b11-e678-4663-a2ec-85ae6958455a`)
- S30: [铝合金壳体压铸工艺设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4899ff0b-49f4-4ff1-a8a5-4a5b8c3b912f/resource) (`4899ff0b-49f4-4ff1-a8a5-4a5b8c3b912f`)
- S62: [换向塔压铸缺陷分析及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b05d397f-5152-494e-ba89-7917f90c3e27/resource) (`b05d397f-5152-494e-ba89-7917f90c3e27`)
- S63: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3e1a06b-33c5-4cd3-a9f5-36acdd96bbdd/resource) (`b3e1a06b-33c5-4cd3-a9f5-36acdd96bbdd`)
- S36: [图 4 优化设计后 t=0.327 s 时的模拟充型情况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58ae0249-26e4-4982-a572-a0e839282f29/resource) (`58ae0249-26e4-4982-a572-a0e839282f29`)
- S61: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab1d0aa4-e987-45d7-be84-a7206c6d60e1/resource) (`ab1d0aa4-e987-45d7-be84-a7206c6d60e1`)
- S57: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1cb2643-bc72-4bf3-a1c5-4aadb70c6d0e/resource) (`a1cb2643-bc72-4bf3-a1c5-4aadb70c6d0e`)
- S4: [压铸工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a493296-2113-485d-be9a-5081caf84fa5/resource) (`0a493296-2113-485d-be9a-5081caf84fa5`)
- S58: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a952aa40-f67d-422b-acb1-6c937f36acaa/resource) (`a952aa40-f67d-422b-acb1-6c937f36acaa`)
- S25: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38b0f70c-b11c-468f-b414-926818963d61/resource) (`38b0f70c-b11c-468f-b414-926818963d61`)
- S53: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/950ede45-d8e0-4f40-b4d3-8ecaec0c0934/resource) (`950ede45-d8e0-4f40-b4d3-8ecaec0c0934`)
- S68: [基于NX的压铸数值模拟集成与溢流槽快速建模系统研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4a101c1-6a61-4dbd-9b3c-ec192466ece1/resource) (`d4a101c1-6a61-4dbd-9b3c-ec192466ece1`)
- S26: [空压机用铝合金阀盖件的低压铸造工艺开发及模拟优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a7bc564-55c1-4b4d-baa0-8519a629aeb4/resource) (`3a7bc564-55c1-4b4d-baa0-8519a629aeb4`)
- S19: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f3e4711-5a42-4c3f-a7ac-a1778574bd7f/resource) (`2f3e4711-5a42-4c3f-a7ac-a1778574bd7f`)
- S78: [压铸模CAE软件结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ee1321e0-0614-4dc8-ae47-18bbbb181b10/resource) (`ee1321e0-0614-4dc8-ae47-18bbbb181b10`)
- S22: [现代注塑模具设计实用技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32c5b640-c259-4112-91c3-aab4bc93cfb4/resource) (`32c5b640-c259-4112-91c3-aab4bc93cfb4`)
- S64: [注塑模具设计原则、要点及实例解析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb5f3910-0d5f-44d2-877c-3ad9ee8deda7/resource) (`bb5f3910-0d5f-44d2-877c-3ad9ee8deda7`)
- S43: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69c99b2b-2989-4763-97d4-e575c98e6805/resource) (`69c99b2b-2989-4763-97d4-e575c98e6805`)
- S73: [现代注塑模具设计实用技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb27777f-81a7-4a91-b62a-6a17f2aa700e/resource) (`eb27777f-81a7-4a91-b62a-6a17f2aa700e`)
- S13: [Moldflow注塑模流分析从入门到精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26690c92-ee06-4494-bbab-2f9e46dcb102/resource) (`26690c92-ee06-4494-bbab-2f9e46dcb102`)
- S60: [Moldex3D模流分析工具对应不同用户及工艺复杂程度的层级图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aae991ca-bbf5-430b-be24-8fa996e1ecc9/resource) (`aae991ca-bbf5-430b-be24-8fa996e1ecc9`)
- S5: [表2.1 国内外主流铸造软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0eece464-963e-4081-ad3d-363f5dc82bb1/resource) (`0eece464-963e-4081-ad3d-363f5dc82bb1`)
- S10: [表1.2 国外主要CAE铸造仿真软件技术概况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1cfe721b-75ef-4e63-936a-9ab0fab4ae61/resource) (`1cfe721b-75ef-4e63-936a-9ab0fab4ae61`)
- S76: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S23: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34173a8e-f6f1-4181-9188-514d82f794e5/resource) (`34173a8e-f6f1-4181-9188-514d82f794e5`)
- S71: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S28: [空压机用铝合金阀盖件的低压铸造工艺开发及模拟优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42f42f00-1d71-413e-8b72-3ebc589ef205/resource) (`42f42f00-1d71-413e-8b72-3ebc589ef205`)
- S1: [2505109_华铸CAE](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/019777af-e28f-44e2-9962-ccde177bf179/resource) (`019777af-e28f-44e2-9962-ccde177bf179`)
- S50: [汽车散热器水室成型的数值分析及优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ed4c348-cbfb-429b-8dc3-854a6f98fe73/resource) (`8ed4c348-cbfb-429b-8dc3-854a6f98fe73`)
- S75: [现代注塑模具设计实用技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb527889-0662-4665-8999-09df199e2d66/resource) (`eb527889-0662-4665-8999-09df199e2d66`)
- S65: [铸造工艺仿真标准研究及案例验证](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bcd9c895-af26-4ae8-bee1-ff9d2b1e1344/resource) (`bcd9c895-af26-4ae8-bee1-ff9d2b1e1344`)
- S69: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dce2d13e-413c-4061-9d2d-8e1edc9e49c7/resource) (`dce2d13e-413c-4061-9d2d-8e1edc9e49c7`)