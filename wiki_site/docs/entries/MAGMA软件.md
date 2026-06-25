---
version: "v1"
generated_at: "2026-06-18T11:52:53+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 34
  source_quality_score: 0.84
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

MAGMA软件，官方全称MAGMASOFT，中文商业名称为迈格码，是用于铸造工艺计算机辅助工程仿真的专业模流分析软件[[S20,S28]]。该软件由德国亚琛工业大学Sahm教授团队主持开发，1988年在德国正式发行，1989年在第7届国际铸造博览会上作为全球首个商品化铸造CAE软件公开展出[[S28,S39]]。MAGMASOFT以充型、凝固过程的多物理场耦合仿真为核心，覆盖熔炼、造型、浇注到热处理的全流程工艺优化需求，旨在帮助铸造工程师改善铸件质量、优化工艺参数、缩短试制周期并降低废品率[[S9,S3]]。

该软件与地质学中的岩浆概念完全无关。MAGMASOFT由德国Magma Giessereitechnologie公司开发，中文区运营实体为迈格码（苏州）软件科技有限公司，由具有工程背景的铸造工程师提供技术支持，官方网站为www.magmasoft.com[[S3,S8]]。截至相关统计数据发布时，该软件在全球拥有超过900家行业客户，在同期同类铸造CAE软件中处于领先水平[[S3]]。

## 版本与迭代

MAGMA软件经历了持续的版本演进：初代版本于1988年发布，使用FDM与FEM结合的混合算法[[S39]]。2010年推出MAGMA5版本，实现了从4系列版本的重大跨越[[S20,S28]]。后续迭代的关键节点如表1所示。

**表1 MAGMA5系列主要版本及关键技术特征**
| 版本 | 发布年份 | 关键技术特征 |
|------|----------|--------------|
| MAGMA5 | 2010 | 从4版本重大升级 |
| MAGMA5.1 | 2011 | 大幅强化有色金属铸造仿真能力 |
| MAGMA5.2 | 2012 | 新增制芯生产工艺优化模块与全3D铸造模拟技术 |
| MAGMA5.5 | 2015 | 逐步引入试验设计（DOE）与自动优化功能 |

## 核心功能与物理模型

### 充型分析

MAGMASOFT的核心充型求解基于SOLA-VOF技术求解Navier-Stokes方程，采用控制体积有限差分法框架，通过体积函数F（0≤F≤1）的VOF方法追踪自由表面流动状态[[S41,S17,S23]]。在充型过程中，软件将金属液视为黏性不可压缩流体，考虑熔融金属的黏度进行流场、温度场、压力场的耦合计算[[S41]]。

充型与凝固过程采用解耦计算逻辑：默认假定充型过程中金属液温度足够高不发生凝固，将充型结束时刻输出的温度场直接作为凝固计算的初始条件[[S41]]。

### 凝固分析与缺陷预测

MAGMAsolid凝固分析模块依托随温度变化的金属液流动特性与凝固收缩特性，结合重力方向相关的浇注条件完成传导与补缩过程计算，输出未充型区域与缩孔缩松位置结果[[S41]]。

MAGMASOFT集成了多种缺陷预测判据[[S1,S10]]：

- **Niyama判据**：经典表达式为Ny=G/√R，其中G为温度梯度，R为冷却速率。Ny低于设定阈值的区域判定为高缩松倾向性区域，模拟参数NIYAMA默认值为0.9，设为0可关闭该判据计算[[S10,S12,S35]]。
- **无量纲Niyama判据**：在经典判据基础上引入合金特性参数（枝晶间距、液体黏度、凝固收缩率、结晶温度范围等），当无量纲Niyama模型激活时FEEDLEN判据被停用，但宏观管道缩孔仍由POROS判据模块的PIPEFS、MACROFS参数控制[[S10,S16]]。
- **FEEDLEN临界补缩距离判据**：用于宏观缩松预测，配合Niyama判据协同工作[[S10]]。

![MAGMA缩松缺陷双判据预测结果对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15112ba7-19a0-4be8-acf9-b8adc26dab7f/resource)

图1展示的是304不锈钢阀体熔模铸造优化工艺的仿真缺陷预测对比结果，同时显示POROS总缩松率判据和Niyama判据的缺陷分布[[S2]]，所有缩松预测结果均集中于冒口区域，阀体工作区域无缺陷。

### 应力分析

MAGMAstress应力分析模块以热弹塑性本构模型为核心，支持固液两相区流变特性插值处理，输出热应力、相变应力、机械应力耦合的全场分布结果，可计算三维铸件与模具的热弹性/热塑性应力分布，用于预测铸件残余应力、变形、热裂缺陷及模具寿命[[S5,S13,S21,S41]]。

## 模块与结构

MAGMASOFT采用模块化架构，标准模块与专用工艺模块分工明确[[S32,S20,S37]]。标准模块共7个，各模块能力边界如表2所示。

**表2 MAGMASOFT标准模块及功能**
| 模块名称 | 功能描述 |
|----------|----------|
| 项目管理模块 | 统一管理项目下不同工艺方案的版本与数据 |
| 前处理模块 | 支持多格式CAD数据导入、自动网格划分，支持一模多腔与冷却/浇注系统快速建模 |
| MAGMAfill流体流动分析模块 | 仿真充型过程的金属液流场、温度场、压力场，预测包气、卷渣、模具冲蚀缺陷 |
| MAGMAsolid热传及凝固分析模块 | 仿真凝固过程的温度梯度、冷却速率，预测缩孔缩松缺陷，优化冒口与冷铁配置 |
| MAGMA batch制程仿真模块 | 仿真多周期连续生产条件下的模具温度循环与热负荷 |
| 后处理模块 | 提供三维可视化结果查看、切片、动画输出功能 |
| 热物理材料数据库模块 | 内置覆盖全品类铸造合金、铸型材料的性能参数，支持用户自定义扩充 |

![MAGMA软件材料参数定义界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94d86316-eac8-4a83-ae54-cafb4a09a389/resource)

图2为MAGMA软件的材料定义界面，显示材料类型、初始温度、液相线温度、固相线温度参数设置与材料数据库树状列表，属于热物理材料数据库模块的典型操作界面[[S24]]。

专用工艺模块包含11类[[S5,S20,S33,S37,S41]]，核心模块如下：

- **MAGMAhpdc高压压铸专业模块**：适配压射、真空、高速充型的专属求解模型，需输入压射速度曲线、增压比压、型腔排气边界参数[[S8]]。
- **MAGMAlpdc低压铸造专业模块**：针对低压铸造的升液、充型、保压凝固过程开发专属仿真模型，需输入完整的升液/充型/保压全压力曲线参数[[S8]]。
- **MAGMAstress应力应变分析模块**：计算三维铸件与模具的热弹性/热塑性应力分布。
- **MAGMAiron铸铁专业模块**：预测铸铁的石墨球数、相变行为与力学性能。
- **MAGMAsteel铸钢专业模块**：计算铸钢件的宏观偏析与热处理微观组织演变。

此外，软件还内置包含各类压铸机参数、造型机参数、商品化铸辅材料性能的专用工业数据库[[S33,S1]]。

## DOE试验设计与自主优化

MAGMA新版本内置DOE试验设计自主优化模块，支持多因素筛选分析，可快速定位对铸件缺陷影响权重最高的工艺参数，实现多目标工艺优化[[S40,S18]]。DOE影响因子设计表可针对冷却通道材料、加热温度、合金初始温度、换热数据等设计变量设置对应的上下限与步长[[S11]]。

![DOE选定工艺参数下阀体显微缩松区域预测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6195e4b-2afd-4376-bc39-2a33a632917d/resource)

图3为MAGMA铸造DOE优化试验对应的阀体显微缩松区域标记仿真结果，绿色、蓝色高亮区域标示阀体不同部位的高显微缩松风险位置[[S29]]，可用于指导工艺参数对缺陷影响权重的分析。

## 应用案例：A356铝合金低压铸造

MAGMASOFT内置MAGMAlpdc低压铸造专用模块，可完整支持A356铝合金低压铸造场景的全流程仿真计算[[S20,S33]]。在A356低压铸造场景下，软件可对充型流场、流动前沿温度分布、卷气概率进行定量预测，识别浇注系统内气体再循环聚集区域及充型末期型腔内封闭气腔分布，精准定位充型末端气体不稳定缺陷的高风险位置[[S6,S27]]。

A356铝合金低压铸造过程中，90%以上的氧化夹杂物为Al₂O₃类组分，二次氧化缺陷集中分布在铸件充型末端及拐角等最后凝固区域[[S26]]。MAGMA软件通过流动前沿扰动度与金属液-空气接触时长的耦合计算，预测氧化夹杂物的生成高风险区域，有公开的工程案例支撑对应的A356铝合金充型空气夹杂率与表面氧化缺陷浓度分布模拟云图[[S19,S34]]。

该软件针对A356半固态触变成形场景还内置Ostwald-de Waele幂律非牛顿流体黏度模型，其模拟结果与A356合金实际半固态流动特性的匹配度已得到工程验证[[S23]]。

## 软件定位与横向对比

MAGMASOFT在同期国际主流铸造模拟软件中占据重要地位。如表3所示，各主流软件在求解算法、功能维度与适用工艺范围上各有侧重。

**表3 国内外主流铸造CAE软件概况对比**
| 软件名称 | 国家 | 发行年份 | 算法 | 核心分析功能 | 适用工艺 |
|----------|------|----------|------|--------------|----------|
| MAGMASOFT | 德国 | 1989 | FDM+FEM | 建模、充型分析、凝固分析、残余应力分析 | 砂型、壳型、熔模、压力、金属型等几乎所有铸造工艺 |
| ProCAST | 美国/法国 | — | FEM | 充型、凝固、微观组织分析 | 砂型、熔模、压力铸造等 |
| Flow-3D | 美国 | — | FVM | 流体流动、自由表面追踪 | 砂型、压力铸造、消失模等 |

*注：表格数据来源于相关文献对比 [[S39]]。其他软件信息由文献记录，非本词条核心探讨对象。*

进一步的软件适用工艺范围对比可参见主流铸造数值模拟软件属性汇总表[[S38]]。

## 局限性与工程注意事项

MAGMA仿真结果的可信度高度依赖前处理精度与边界条件设置[[S7,S42]]。铸件最小壁厚区域至少需要划分2至3层网格才可保证计算精度，低精度粗网格会直接导致流场计算失准，显著放大卷气、氧化缺陷的预测误差[[S7]]。模具与铸件界面换热系数、低压铸造充型增压速率、浇注初始温度等输入参数的实测偏差会直接降低最终缺陷预测结果与实际铸件探伤结果的匹配度，必须结合同工况已验证的基准样本参数完成校准才可获得可靠预测结果[[S42]]。

## Sources
- S20: [TextNode125](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a62dd6c-7a87-47ef-888c-1374e8938011/resource) (`7a62dd6c-7a87-47ef-888c-1374e8938011`)
- S28: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a49544a0-99b5-4cc9-8647-3276eb49bd2f/resource) (`a49544a0-99b5-4cc9-8647-3276eb49bd2f`)
- S39: [表1-1 国内外铸造CAE软件概况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecb5ba93-745f-43c0-b78f-5b4ed0a51cbb/resource) (`ecb5ba93-745f-43c0-b78f-5b4ed0a51cbb`)
- S9: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35c0bacf-3979-468b-8791-843f11ab87b7/resource) (`35c0bacf-3979-468b-8791-843f11ab87b7`)
- S3: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1dc00ed0-2e10-42ea-970e-17ab68407b7e/resource) (`1dc00ed0-2e10-42ea-970e-17ab68407b7e`)
- S8: [铝合金压铸下箱体的浇注系统设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f4ed40d-f1bd-449b-a754-74ceb8b03b6b/resource) (`2f4ed40d-f1bd-449b-a754-74ceb8b03b6b`)
- S41: [TextNode27](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f93659b5-5f5d-4c7a-9e6d-719b57cc2662/resource) (`f93659b5-5f5d-4c7a-9e6d-719b57cc2662`)
- S17: [不同型腔真空度对铸件组织和性能的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/666a4caa-0a9e-4e1f-a7e6-c019ad4c40be/resource) (`666a4caa-0a9e-4e1f-a7e6-c019ad4c40be`)
- S23: [die design method for thin plates by indirect rheo casting process and e__3c809a0c1d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a3f7468-9e98-4046-ac78-4206fba15b55/resource) (`8a3f7468-9e98-4046-ac78-4206fba15b55`)
- S1: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06009891-94de-4cbb-8d11-e775d2928eeb/resource) (`06009891-94de-4cbb-8d11-e775d2928eeb`)
- S10: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39ff805a-ae97-4482-9719-8ad91144fe1e/resource) (`39ff805a-ae97-4482-9719-8ad91144fe1e`)
- S12: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3db330a1-c305-46b5-bc9d-2068fd494dd9/resource) (`3db330a1-c305-46b5-bc9d-2068fd494dd9`)
- S35: [基于数值模拟的转向器阀壳体压铸模具结构及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1d629e5-7508-4d69-8982-10d1edeed5e8/resource) (`d1d629e5-7508-4d69-8982-10d1edeed5e8`)
- S16: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64d5bb0f-c6c9-4e79-9b9e-407995407cf1/resource) (`64d5bb0f-c6c9-4e79-9b9e-407995407cf1`)
- S2: [图5-4 优化后缺陷预测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15112ba7-19a0-4be8-acf9-b8adc26dab7f/resource) (`15112ba7-19a0-4be8-acf9-b8adc26dab7f`)
- S5: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20f2db5c-2a6f-49c1-ae1d-2e9451819b4d/resource) (`20f2db5c-2a6f-49c1-ae1d-2e9451819b4d`)
- S13: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/54a650dc-7f72-492e-892f-d69ee53f6af6/resource) (`54a650dc-7f72-492e-892f-d69ee53f6af6`)
- S21: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f66d25f-990e-4f9f-bfa5-9be299f12ecf/resource) (`7f66d25f-990e-4f9f-bfa5-9be299f12ecf`)
- S32: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b17a4f24-0a05-43d8-9c28-390e3da5432c/resource) (`b17a4f24-0a05-43d8-9c28-390e3da5432c`)
- S37: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e19e39c1-33ea-4fdf-99c3-5112caedb628/resource) (`e19e39c1-33ea-4fdf-99c3-5112caedb628`)
- S24: [MAGMA软件材料定义界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94d86316-eac8-4a83-ae54-cafb4a09a389/resource) (`94d86316-eac8-4a83-ae54-cafb4a09a389`)
- S33: [TextNode126](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba8f3f8b-82a2-4d58-a370-b9a4a6279fe6/resource) (`ba8f3f8b-82a2-4d58-a370-b9a4a6279fe6`)
- S40: [铝合金发动机缸体低压铸造缺陷控制的工艺及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f82ab5e7-0c83-41cf-95b3-afe7c46ee0a5/resource) (`f82ab5e7-0c83-41cf-95b3-afe7c46ee0a5`)
- S18: [AnyCasting铸造模拟软件Hybrid网格模型以及临界凝固分数的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f263ea1-f315-4991-a7e5-8e7e61bfffa6/resource) (`6f263ea1-f315-4991-a7e5-8e7e61bfffa6`)
- S11: [图5.35 DoE不同影响因子设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b03b059-6e6e-4e4b-bfd5-96ece5d0419c/resource) (`3b03b059-6e6e-4e4b-bfd5-96ece5d0419c`)
- S29: [g) 试验7 阀体铸造显微缩松仿真图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6195e4b-2afd-4376-bc39-2a33a632917d/resource) (`a6195e4b-2afd-4376-bc39-2a33a632917d`)
- S6: [CAE在国六发动机缸体缸盖铸件中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a113832-0a68-489b-93fd-3a3077ac8b6f/resource) (`2a113832-0a68-489b-93fd-3a3077ac8b6f`)
- S27: [A356低压铸造铝合金车轮工艺优化及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a36df718-6006-43a1-999e-d37124212ba6/resource) (`a36df718-6006-43a1-999e-d37124212ba6`)
- S26: [电磁搅拌2219铝合金铸锭夹杂物形成机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97d4ced6-8719-4d48-a5e3-c4f273454ef8/resource) (`97d4ced6-8719-4d48-a5e3-c4f273454ef8`)
- S19: [铝合金半固态压铸工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/776f5d31-c9b3-4609-a22f-8cccae9157cf/resource) (`776f5d31-c9b3-4609-a22f-8cccae9157cf`)
- S34: [原始结构铸件充型过程的空气夹杂率与表面氧化缺陷浓度分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c10bf66c-54b4-4eaa-8717-4e7dbceac01a/resource) (`c10bf66c-54b4-4eaa-8717-4e7dbceac01a`)
- S38: [表2.3 铸造主流软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e39fba15-e487-4979-8a06-2419ecd4b62b/resource) (`e39fba15-e487-4979-8a06-2419ecd4b62b`)
- S7: [镁合金隔板铸件低压铸造工艺数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e0eb03c-961a-487b-b348-78dd1b1bcb68/resource) (`2e0eb03c-961a-487b-b348-78dd1b1bcb68`)
- S42: [表3 Magma软件数值模拟参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc35294f-6f1c-4dc7-8e15-aa55add46b97/resource) (`fc35294f-6f1c-4dc7-8e15-aa55add46b97`)