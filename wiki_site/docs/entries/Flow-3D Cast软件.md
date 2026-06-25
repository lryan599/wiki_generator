---
version: "v1"
generated_at: "2026-06-18T13:12:40+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 46
  source_quality_score: 0.83
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

**Flow-3D Cast**（亦称Flow3D-CAST、Flow-3dcast）是由美国Flow Science Inc.研发的三维流体动力学与传热分析仿真软件在压铸领域的专用版本[[S17,S28,S8]]。公司由流体力学学者、VOF方法核心开发者C.W.(Tony) Hirt博士于1980年创立，软件于1985年正式商业化发布[[S8,S28]]。官方网站为www.flow3d.com[[S17,S28]]。

该软件以独有的FAVOR™网格技术和TruVOF自由液面追踪算法为核心，专为高压/低压/半固态等压铸工艺的充型与凝固全流程模拟而优化，广泛应用于型腔填充分析、卷气与气孔预测、排气系统效果验证及浇排系统设计优化等领域[[S53,S33,S8,S18]]。

## 核心功能与数值方法

### FAVOR™网格技术

Flow-3D搭载独有的FAVOR™（Fractional Area/Volume Obstacle Representation，分数面积/体积障碍物表征）技术[[S15,S25,S46]]。该技术基于笛卡尔直角网格，无需传统有限差分/有限元的贴体网格来适配复杂几何[[S39,S46]]。其工作原理为：通过预处理器统计每个网格单元内固体占据的体积比例，以及x、y、z三个方向上流体可流通的面积比例，从而仅用少量规则矩形网格即可高精度表征任意复杂铸型结构[[S25,S15]]。FAVOR技术避免了传统方法的网格畸变问题，大幅降低网格生成工作量与总单元数量，同时提升计算效率[[S39,S46]]。

![FAVOR技术对球体几何的非贴体网格表征效果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d08cc79-86f9-449a-848c-c2943b7df2d9/resource)

上图展示了FAVOR技术对球形几何体的网格划分效果：在规则笛卡尔网格中，FAVOR通过分数占比来表征曲面复杂几何，而非让网格沿曲面产生畸变[[S10,S25]]。

### TruVOF自由液面追踪

软件搭载的TruVOF是基于经典SOLA-VOF算法迭代优化而来的改进型流体体积法[[S25,S45]]。其核心是通过网格内金属液体积分数α的动态求解实现自由液面精准追踪[[S45]]：

| α值 | 含义 |
|---|---|
| α = 0 | 该单元完全由气体占据，无金属液 |
| α = 1 | 该单元已被金属液完全充满 |
| 0 < α < 1 | 气液混合界面单元 |

计算过程中，TruVOF自动忽略低能量的气体运动部分，将空气单元简化为无质量的均匀压力场，既大幅降低计算开销，又可精准捕捉金属液高速充型过程中的飞溅、汇合并发的动态界面形态[[S45]]。

### 温度场-速度场-压力场三场耦合

Flow-3D通过控制方程联立求解实现温度场、速度场、压力场的全耦合计算[[S15,S23]]。具体计算逻辑为：

| 物理场 | 求解方法 |
|---|---|
| 速度场 | 基于带面积分数/体积分数修正的Navier-Stokes方程求解[[S15]] |
| 压力场 | 通过压力迭代校正算法求解[[S15]] |
| 温度场 | 通过带潜热项的能量方程实时更新温度分布[[S15]] |

不同物理场的时间步长自动同步，实现充型过程中金属液流动、温度传递、压力演化的完全联动模拟[[S15]]。ASME公开文献中进一步明确了求解器配置：压力求解为隐式，自由表面求解为隐式，体积流体对流采用分裂拉格朗日法，动量对流为一阶格式[[S23]]。

### 排气槽/排气道气体流动建模

Flow-3D Cast压铸专属模块支持直接导入排溢系统的三维几何模型作为空气域计算单元[[S53,S21]]。通过此功能可实现：

- 型腔内背压演化的动态计算[[S53,S18]]
- 不同排气方案下气体流动路径的预测[[S53,S18]]
- 充型过程中卷气位置的定量分析[[S53,S18,S33]]
- 溢流槽、排气道布局的排气效率验证与迭代优化[[S18,S53]]

排气槽几何参数支持用户在外部CAD软件中完成任意规格的三维建模，导出STL文件后直接导入软件，完成厚度、宽度、长度、流道走向的完全自定义，并在排气出口位置配置对应压力边界即可实现排气过程仿真[[S53,S16]]。

## 压铸工艺典型应用场景

### 型腔填充与流动分析

Flow-3D Cast可完整复现压铸充型全流程，输出不同时间节点下金属液的填充顺序、流场速度、温度分布结果[[S30,S27]]。软件支持对压射室多级变速位置、充满度等参数的自定义设置[[S53]]。已落地应用于铝合金汽车减震器顶胶支座、汽车减速器壳体、新能源汽车后舱大型一体化压铸件等复杂产品的充型过程仿真，可预判充型平稳性及金属液飞溅等异常流动情况[[S30,S27,S12]]。

### 卷气与氧化夹杂预测

基于交错网格离散控制方程和金属浆料-空气自由液面计算能力，Flow-3D Cast可高效预测充型过程中的卷气和氧化夹杂生成位置与分布范围[[S33]]。通过半固态压铸9组不同工艺参数的正交模拟验证，软件可精准识别卷气集中分布的规律（如集中在铸件上半部分前端、横浇道边缘），指导溢流槽和排气道的布局设计，将卷气集中到非铸件区域[[S33,S52]]。

软件内置简化凝固收缩（SSS）模型，不需要求解完整流体流动方程，仅通过计算各隔离液区凝固收缩体积即可快速定量计算孔隙率，可分别统计气体析出型气孔和凝固收缩型气孔的占比[[S37]]。

### 排气槽尺寸优化

Flow-3D Cast可通过三场耦合仿真，精准评估不同厚度排气槽的排气效果和金属液渗漏风险[[S19]]。典型铸钢件案例中：

> 通过模拟不同厚度排气槽的充型过程，观察到1mm薄板金属液提前冷凝、2mm薄板金属液在压力升高后溢出的规律，最终选定的排气槽方案既实现了型腔憋气的有效排出，彻底消除了加工面皮下气孔缺陷，同时未出现钢水外溢问题，使铸件皮下气孔废品率从60%直接降至0%[[S19]]。

### 浇排系统设计优化

Flow-3D Cast可支撑浇注系统、溢流槽、排溢布局的全流程迭代优化[[S12,S14]]。

- **汽车后舱一体化压铸件案例**：通过模拟发现U型槽区域不同渣包间铝液串流干涉卷气的问题，优化后截断连通溢流槽，为U型槽渣包独立引出排气，解决了该区域的气孔缺陷[[S12]]。
- **铝合金水泵壳体案例**：通过增设多组不同规格的环形溢流槽，在金属液最后填充位置设置排气槽，优化后铸件主体卷气量大幅降低，表面缺陷率低于2%，卷气完全集中在可切除的溢流槽区域[[S14]]。

## 输入参数与输出结果

### 网格划分

Flow-3D Cast采用非均匀多块分区结构化网格架构[[S53]]。操作流程为：
1. 导入STL格式三维几何模型
2. 手动/自动设置网格总数量完成网格自动分割
3. 利用FAVOR完成几何与网格的适配校验
4. 按需局部加密或粗化网格以平衡计算精度与效率[[S53]]

### 材料数据库

软件内置包含50余种合金铸件、10余种铸型的材料数据库[[S17,S53]]，覆盖主流压铸合金（铝合金、镁合金、锌合金等）和常用H13类模具钢[[S53]]。支持用户自定义导入随温度变化的粘度、固液相分数、热导率、比热等热物性参数，也可对接JMatPro等材料计算软件生成的自定义合金属性[[S53,S33]]。

### 边界条件与物理模型

Flow-3D Cast的高压压铸HPDC专用模块支持[[S43,S8]]：

| 仿真阶段 | 功能 |
|---|---|
| 热模循环 | 模具预热到稳定热平衡状态 |
| 填充 | 金属液充型流动仿真 |
| 凝固 | 冷却与凝固过程分析 |
| 冷却 | 开模与喷涂冷却阶段 |

支持的物理模型与参数包括：模具背压、型芯发气、金属液空气夹杂、空化气泡、湍流、热应力演化、表面张力等[[S43,S53]]。冷却管道的对流传热系数Nu可通过雷诺数Re和普朗特数Pr自动计算[[S8,S43]]。终止条件支持以时间、充型完成百分比或凝固完成百分比设置[[S43]]。

### 输出结果字段

Flow-3D Cast后处理可导出的定量结果包含[[S43,S53]]：

- 全流程充型时序分布
- 全域流速矢量场
- 充型各阶段压力场分布
- 全域温度场分布
- 凝固过程固相分数分布
- 不同区域卷气含量占比
- 氧化夹杂/表面缺陷位置与占比
- 热应力场分布
- 空蚀缺陷分布
- 充型完整度统计

## 模拟工作流程

![Flow-3D压铸模拟标准操作流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/883fdef8-151a-467c-a927-06e48ba37e45/resource)

上图展示了Flow-3D Cast压铸模拟的标准操作流程，涵盖创建工作文件、导入STL模型、网格划分、常规选项设置、物理模型设置、材料参数配置、边界条件定义、初始条件设置、输出参数设定、模拟运算到结果分析的完整步骤[[S32]]。

![基于Flow-3D的压铸工艺闭环优化工作流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c1aef86-315a-44fd-a65d-fdca219580ab/resource)

上图展示了基于Flow-3D的压铸工艺闭环优化流程：从压铸工艺设计、三维建模导入Flow-3D、网格划分与模型校验、物理模型参数设置，到求解得到多场结果、缺陷分析、工艺参数迭代优化，直至确定最优压铸工艺的完整闭环逻辑[[S3]]。

## 与其他主流铸造仿真软件对比

### 技术参数对比

| 软件名称 | 开发商（国家） | 核心算法 | 核心分析能力 |
|---|---|---|---|
| Flow-3D | Flow Science Inc.（美国） | FVM/FDM耦合 [[S34]] | 流动与传热分析，自由液面追踪精度突出 [[S34,S20,S22]] |
| MAGMASOFT | MAGMA GmbH（德国） | 有限差分法（FDM）[[S20,S4,S41]] | 模块化程度高，薄壁压铸件分析强 [[S7,S4,S41]] |
| ProCAST | ESI Group（美国） | 有限元法（FEM）[[S31,S44,S34]] | 多物理场耦合，应力/辐射分析优势显著 [[S31,S44,S1]] |
| AnyCasting | AnyCasting Co.（韩国） | 有限差分法（FDM），SOLA-VOF [[S31,S35]] | 支持真空压铸等特种工艺，操作门槛低 [[S31,S35,S7]] |

### 压铸适用场景对比

| 对比维度 | Flow-3D Cast | MAGMASOFT | ProCAST | AnyCasting |
|---|---|---|---|---|
| 充型流动精度 | **突出**：VOF自由表面追踪精度高，适合高速充型与卷气分析 [[S20,S22,S52]] | 良好：薄壁件分析能力强 [[S7,S4]] | 一般：FEM架构在极高速紊流场景下精度弱于FDM [[S22]] | 良好：配备RNG k-ε湍流模型 [[S35]] |
| 排气系统仿真 | **专项支持**：可导入排气道几何，支持背压与排气效率验证 [[S18,S53]] | 支持：内置排气塞等参数 [[S50,S1]] | 支持：通过边界条件设置 [[S16]] | 支持：可预测卷气、夹渣缺陷 [[S7,S54]] |
| 压铸工艺覆盖 | 高压/低压/半固态/挤压铸造 [[S53,S28]] | 高/低压铸造定向适配，含拔塞浇注等专项参数 [[S50,S1]] | 覆盖全面，含离心、连续铸造等 [[S31,S50,S22]] | 适配真空压铸、挤压铸造 [[S7,S49,S54]] |
| 典型用户群体 | 流体工程背景高校/科研团队，充型机理研究 [[S34,S48,S40]] | 欧美整车企业，薄壁精密压铸件生产 [[S50,S2,S11]] | 精密铸件科研院所，航空航天类铸造 [[S44,S1,S36]] | 东亚中小压铸企业，常规铝合金/镁合金件 [[S31,S35]] |
| 操作系统 | Windows等 [[S17]] | Windows NT等 [[S50]] | Windows/Linux/UNIX [[S31,S1]] | 仅Windows [[S31]] |

### 各软件优势与局限

**Flow-3D Cast**：核心优势集中在流体流动仿真领域，对压铸高速充型过程中的氧化夹杂分布、卷气行为仿真精度高，已有文献验证其普通压铸与真空压铸的氧化夹杂分布差异模拟结果与生产实测吻合度良好[[S40,S48]]。局限在于宏观组织预测、大尺寸铸件残余应力变形仿真能力弱于MAGMASOFT与ProCAST[[S22,S49]]。公开实测数据显示对样本压铸试件单次模拟平均耗时低于11秒[[S26]]。版本方面，Flow-3D 9.0在原有基础上新增了6自由度运动物体、空气夹带、温度应力与变形、微观缩松等物理模型[[S28]]。

**MAGMASOFT**：模块化程度高，支持从熔炼、模具设计到热处理的全链条工艺优化[[S2,S50]]，内置模具热平衡计算、出品率自动核算等压铸专属工具[[S50,S1]]。德国大众已使用该软件完成奥迪镁合金变速箱体的压铸优化，产品批量应用至奥迪、帕萨特等量产车型[[S47,S11,S7]]。

**ProCAST**：以有限元法为核心，自动生成四面体网格，在异形复杂铸件中网格适应性更强[[S44,S31]]。内置逆运算模块可迭代校准界面换热等边界条件[[S31,S1]]。福特汽车公司采用该软件完成5.4升Triton发动机壳体的压铸优化[[S11,S54,S5]]。

**AnyCasting**：仅支持Windows操作系统[[S31,S35]]，操作门槛相对更低，面向常规铝合金、镁合金压铸件工艺优化场景性价比突出[[S31,S35]]。在超大型一体化压铸件的百万级网格并行计算效率上不及面向工业级并行优化的头部软件[[S49]]。

## 验证案例与行业应用

### 铸钢件排气槽设计验证

通过Flow-3D Cast模拟不同厚度排气槽的充型过程，系统考察了金属液温度场、速度场和压力场的三场耦合效应[[S19]]。模拟结果表明：1mm薄板提前出现冷隔阻断金属液流出，2mm薄板在压力升高后金属液溢出；通过综合评估，最终选定的排气槽方案既达成有效排气，又未发生钢水外溢，将铸件皮下气孔废品率从60%降至0%[[S19]]。

### 铝合金水泵壳体排溢系统优化

基于Flow-3D Cast对铝合金水泵壳体的压铸过程进行数值模拟，发现初始方案中卷气最高达56%，表面缺陷达7.3%[[S14]]。优化后增设多组不同规格的环形溢流槽，将排气槽设置在金属液最后填充位置，卷气完全集中在溢流槽和排气槽区域，铸件主体无残留卷气。实际生产验证得到无缺陷合格铸件[[S14]]。

### 汽车后舱一体化压铸件缺陷改善

针对汽车后舱一体化压铸件U型槽区域的气孔缺陷，通过Flow-3D充型模拟发现原方案中渣包间铝液串流干涉卷气的问题，优化后截断连通溢流槽，为U型槽渣包独立引出排气，解决了该区域的气孔缺陷[[S12]]。

### 半固态压铸充型验证

在Mg-5Zn-xGd-0.6Zr合金半固态压铸研究中，通过Flow-3D Cast开展正交试验模拟（浆料温度600°C–630°C、压射速度3–5 m/s、模具温度235°C–275°C），成功预测了不同参数下的卷气分布规律和充型完整度，模拟结果与实际生产吻合良好[[S33,S48]]。

## 局限性

1. **物理模型简化**：Flow-3D Cast在凝固收缩建模中使用简化凝固收缩（SSS）模型，该模型假定凝固金属中的流体流动可忽略，主要用于快速计算收缩孔隙率，但对复杂补缩行为的模拟精度有限[[S37]]。

2. **宏观组织与残余应力仿真能力不足**：Flow-3D Cast的核心优势集中在流体流动领域，在宏观组织预测、大尺寸铸件残余应力与变形仿真方面能力弱于MAGMASOFT与ProCAST[[S22,S49]]。

3. **计算资源需求**：网格越精细则计算精度越高，但单元总数呈指数级增长，对计算资源是极大挑战，需在精度与周期之间权衡[[S25]]。在超大型一体化压铸件的百万级网格并行计算效率上，可能不及面向工业级并行优化的头部软件[[S49]]。

4. **网格分辨率限制**：若几何特征尺寸小于单个网格，FAVOR技术将无法识别（如无法识别一个小于网格尺寸的球形），需通过提高网格分辨率来解决[[S25]]。

## Sources
- S17: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58ea8fb5-232c-48b4-9a7c-03034cd5c0bd/resource) (`58ea8fb5-232c-48b4-9a7c-03034cd5c0bd`)
- S28: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/749d0b51-3857-4a91-9926-d67f29bd8056/resource) (`749d0b51-3857-4a91-9926-d67f29bd8056`)
- S8: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/253c6116-36e9-40db-a180-a738c4ae692b/resource) (`253c6116-36e9-40db-a180-a738c4ae692b`)
- S53: [压铸成形工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa653782-48b3-45b0-b066-21a80e9c2568/resource) (`fa653782-48b3-45b0-b066-21a80e9c2568`)
- S33: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96a3121e-d459-46d4-b384-31bde07b56f9/resource) (`96a3121e-d459-46d4-b384-31bde07b56f9`)
- S18: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f16a007-fb87-48e2-bdcb-0e4d410a93bb/resource) (`5f16a007-fb87-48e2-bdcb-0e4d410a93bb`)
- S15: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bd5b67b-bc75-4609-8a08-252e25bf7148/resource) (`4bd5b67b-bc75-4609-8a08-252e25bf7148`)
- S25: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69505a7b-549e-4f04-b2ed-1458f5808d4e/resource) (`69505a7b-549e-4f04-b2ed-1458f5808d4e`)
- S46: [asme asme 2014 12th biennial conference on engineering systems design an__a15afb75a5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d43bd130-dfab-4462-9eb7-b7cf91bf877b/resource) (`d43bd130-dfab-4462-9eb7-b7cf91bf877b`)
- S39: [铝合金套筒低压铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad069a84-7504-476e-9a87-37a9f7957175/resource) (`ad069a84-7504-476e-9a87-37a9f7957175`)
- S10: [FAVOR法划分的球形网格](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d08cc79-86f9-449a-848c-c2943b7df2d9/resource) (`3d08cc79-86f9-449a-848c-c2943b7df2d9`)
- S45: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cebf24c0-955e-4e04-a8bf-1cead4723270/resource) (`cebf24c0-955e-4e04-a8bf-1cead4723270`)
- S23: [CFD 数值计算参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6352b7b4-9f42-454d-af09-a3a68951e651/resource) (`6352b7b4-9f42-454d-af09-a3a68951e651`)
- S21: [a numerical and an experimental investigation of a high pressure die cas__76acfbd839](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/612ff9ff-1a60-46fb-92ed-ebd4be5718dd/resource) (`612ff9ff-1a60-46fb-92ed-ebd4be5718dd`)
- S16: [基于压铸工艺的铝合金车门结构设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/556f30f4-fa4b-4517-8973-4210eed2926d/resource) (`556f30f4-fa4b-4517-8973-4210eed2926d`)
- S30: [铝合金汽车减震器顶胶支座压铸工艺和模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f351662-0e7f-45f8-9598-a7ff51f497bb/resource) (`7f351662-0e7f-45f8-9598-a7ff51f497bb`)
- S27: [汽车减速器壳体压铸模具设计分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7343a994-1df0-4f1b-a91c-f79bc8521d0e/resource) (`7343a994-1df0-4f1b-a91c-f79bc8521d0e`)
- S12: [某汽车后舱一体化压铸件工艺分析及缺陷改善_卢灿雄](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43bef8c0-acfb-4fdc-b63c-1b2963603bb3/resource) (`43bef8c0-acfb-4fdc-b63c-1b2963603bb3`)
- S52: [铝合金发动机缸体低压铸造缺陷控制的工艺及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f82ab5e7-0c83-41cf-95b3-afe7c46ee0a5/resource) (`f82ab5e7-0c83-41cf-95b3-afe7c46ee0a5`)
- S37: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8c06ba3-93e0-43a4-83fe-ec5bca8d9b5d/resource) (`a8c06ba3-93e0-43a4-83fe-ec5bca8d9b5d`)
- S19: [FLOW-3D CAST铸造仿真软件改善铸钢件气孔的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60990ba6-c17e-46ed-bbd5-96a82fb18c2e/resource) (`60990ba6-c17e-46ed-bbd5-96a82fb18c2e`)
- S14: [铝合金壳体压铸工艺设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4899ff0b-49f4-4ff1-a8a5-4a5b8c3b912f/resource) (`4899ff0b-49f4-4ff1-a8a5-4a5b8c3b912f`)
- S43: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0d64694-bf0f-4e97-9b7f-24b2a007420c/resource) (`c0d64694-bf0f-4e97-9b7f-24b2a007420c`)
- S32: [Flow-3D操作基本流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/883fdef8-151a-467c-a927-06e48ba37e45/resource) (`883fdef8-151a-467c-a927-06e48ba37e45`)
- S3: [图2.1 压铸数值模拟流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c1aef86-315a-44fd-a65d-fdca219580ab/resource) (`0c1aef86-315a-44fd-a65d-fdca219580ab`)
- S34: [表1.2 国内外主流使用铸造软件[43]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98dd3bca-962a-49d8-9d47-d25b3afeb03f/resource) (`98dd3bca-962a-49d8-9d47-d25b3afeb03f`)
- S20: [挤压铸造成形铝合金飞轮壳构件微观组织与力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60fa6913-a484-4100-b3ec-8a89a83c9e1e/resource) (`60fa6913-a484-4100-b3ec-8a89a83c9e1e`)
- S22: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61c24028-9370-4819-9603-27dffb5c1618/resource) (`61c24028-9370-4819-9603-27dffb5c1618`)
- S4: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c6644c8-7d4c-4ef6-959e-5ca061062687/resource) (`0c6644c8-7d4c-4ef6-959e-5ca061062687`)
- S41: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b791779c-501a-40f6-ac79-ec32772621ab/resource) (`b791779c-501a-40f6-ac79-ec32772621ab`)
- S7: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848/resource) (`1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848`)
- S31: [TC4合金非对称翼型受油管熔模精密铸造工艺及凝固特性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8385eca2-3951-4e3d-a470-d4cedcd6d253/resource) (`8385eca2-3951-4e3d-a470-d4cedcd6d253`)
- S44: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbcee639-0ac9-4d7f-8309-92a4c5d40853/resource) (`cbcee639-0ac9-4d7f-8309-92a4c5d40853`)
- S1: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07f7190d-9f24-405e-9905-ad286127ca0a/resource) (`07f7190d-9f24-405e-9905-ad286127ca0a`)
- S35: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf/resource) (`a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf`)
- S50: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S54: [铝合金低压铸造过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe51c21e-8783-4b9f-a73c-b8354c194671/resource) (`fe51c21e-8783-4b9f-a73c-b8354c194671`)
- S49: [表2.3 铸造主流软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e39fba15-e487-4979-8a06-2419ecd4b62b/resource) (`e39fba15-e487-4979-8a06-2419ecd4b62b`)
- S48: [图4.1 试棒模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dff00ab3-4c7d-4af0-87f5-8f2e6c6ce95f/resource) (`dff00ab3-4c7d-4af0-87f5-8f2e6c6ce95f`)
- S40: [执手多型腔压铸工艺及模具优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad27d26f-c0f7-40f3-bc3a-262bed5164db/resource) (`ad27d26f-c0f7-40f3-bc3a-262bed5164db`)
- S2: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b5d9a2f-5f00-4c24-bd19-d6a230eedea0/resource) (`0b5d9a2f-5f00-4c24-bd19-d6a230eedea0`)
- S11: [铝合金箱体压铸工艺过程模拟及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ecedcaf-56fd-42f7-9a09-b5dec10af257/resource) (`3ecedcaf-56fd-42f7-9a09-b5dec10af257`)
- S36: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6c0ddc9-3495-490b-bb55-129392d012fc/resource) (`a6c0ddc9-3495-490b-bb55-129392d012fc`)
- S26: [表 4 不同压铸模拟对样本试件模拟平均耗时分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71d0721d-0be9-4c29-93b5-52c552ecf862/resource) (`71d0721d-0be9-4c29-93b5-52c552ecf862`)
- S47: [application of an integrated cad cae cam system for die casting dies__96a43cb0a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de012533-d236-4f2e-8930-8309e436ad58/resource) (`de012533-d236-4f2e-8930-8309e436ad58`)
- S5: [(e) 充型时间 350s](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1682b60f-9d15-4560-97e7-d883638aea4f/resource) (`1682b60f-9d15-4560-97e7-d883638aea4f`)