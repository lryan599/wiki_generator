---
version: "v1"
generated_at: "2026-06-19T09:57:59+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 39
  source_quality_score: 0.87
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

## 定义

铸造工艺CAD（铸造工艺计算机辅助设计，英文对应 **computer-aided design of the casting process, casting process CAD**）是指利用计算机辅助完成铸造工艺全流程设计的技术 [[S25]]。

依据GB/T 5611—2017《铸造术语》，其涵盖内容为：充型过程流场模拟、温度场模拟、应力场模拟、凝固组织模拟、铸造缺陷模拟，铸件浇注位置、浇注系统、冒口、冷铁等结构的优化设计，以及浇注温度、浇注时间、铸型温度、留型时间等工艺参数的计算与优化 [[S25]]。

在完整意义上，铸造工艺CAD不仅包括浇注系统、冒口、冷铁、型芯等工艺结构的计算机设计及工艺图绘制，还应包含凝固过程数值模拟（铸造工艺CAE）反馈驱动的工艺优化，二者共同构成铸造工艺集成CAD [[S7]]。

## 分类

按适用范围，铸造工艺CAD系统可分为 **通用型** 与 **专用型** 两类 [[S2]]。

| 类型 | 适用场景 | 典型功能 | 细分方向 |
|---|---|---|---|
| 通用铸造CAD | 普通砂型铸造 | 浇注系统设计、补缩系统设计、分型面/拔模斜度/加工余量确定、尺寸标注、工艺图与工艺卡输出 | 按材质分为铸钢、灰铸铁、球铁、有色金属等 |
| 专用铸造CAD | 特定细分场景或特定目的 | 面向特定零件或工艺类型定制 | 压铸型CAD、齿轮类CAD、阀体类CAD、曲轴类CAD等 |

## 在铸造工艺链中的位置

铸造工艺CAD是现代铸造先进制造体系的前端核心环节。典型工作流程为：将铸件模样、铸型材料属性、铸造合金热物性参数、凝固特性及相关数学模型输入计算机，计算得到合理的浇冒口系统方案，再结合凝固过程数值模拟对工艺设计结果进行校验，经多轮迭代优化，在工艺设计阶段提前规避潜在的铸造质量问题 [[S10,S21]]。

该系统以三维实体造型为基础，可与后续铸造工艺CAE、铸造工装CAD/CAE、CAM系统实现无缝数据共享，是铸造CAD/CAE/CAM集成系统以及并行工程环境下虚拟制造成形的关键支撑技术 [[S10,S21]]。

大型铸钢件铸造工艺CAD的全链路运行流程如下：从输入零件蓝图开始，依次经过计算机识图审图、工艺方案确定、通用参数设计、浇冒口系统设计、模型网格剖分、多物理场数值计算，再到质量预测评估，最终通过计算机绘图输出可直接用于生产的工艺文件并完成投产 [[S55]]。

![大型铸钢件铸造工艺CAD全流程框图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e32cc54d-9518-422f-ab79-e1e8f3f7e7c0/resource)

## 核心功能模块

铸造工艺CAD系统的核心功能共包含8大模块 [[S21,S27]]：

| 模块名称 | 功能说明 |
|---|---|
| ① 铸造工艺方案确定 | 浇注位置与分型面选定、铸造与造型方法确定、制芯方法选择、砂箱内铸件数量确定及排列 |
| ② 工艺参数设计确定 | 机械加工余量、拔模斜度、铸造收缩率、最小铸出孔等参数设定 |
| ③ 冒口系统设计 | 冒口与冒口颈的类型、形状、尺寸、安放位置的设计、计算及校核 |
| ④ 浇注系统设计计算 | 选定浇注系统类型，确定内浇道、横浇道、直浇道、浇口杯、阻流片等各组元的尺寸与位置关系 |
| ⑤ 砂芯设计 | 砂型形状及分盒面确定，芯头类型、长度、斜度、间隙等参数设计 |
| ⑥ 模板布置设计 | 在标准模板上排布铸件、浇冒口系统等组件的位置 |
| ⑦ 二维工艺图/卡生成模块 | 自动生成、绘制并输出二维铸造工艺图与铸造工艺卡 |
| ⑧ 工艺文档管理 | 铸件全生命周期工艺查询与资料管理 |

![铸造工艺CAD系统核心功能组成框架](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13b639f1-39af-497f-8dc7-aac096b8b8b7/resource)

## 技术工作流程

完整的铸造工艺CAD流程以三维实体造型为基础，从上游产品设计输出铸件三维模型开始，依次经过以下步骤 [[S2,S5,S7,S29]]：

1. **铸件模型导入与分析**：导入上游铸件三维实体模型，完成结构铸造工艺性分析，自动计算体积、表面积、重量、热模数等基础几何物理量。
2. **工艺方案与参数确定**：交互式或自动选定分型面、浇注位置，设置加工余量、拔模斜度、铸造收缩率、最小铸出孔等工艺参数，生成毛坯铸件图。
3. **补缩系统设计**：依托预凝固模拟得到的热节位置与收缩量数据，开展冒口、冷铁、补缩通道的参数化设计并完成校核 [[S7,S50]]。
4. **浇注系统设计**：按选定类型完成直浇道、横浇道、内浇道等组元尺寸计算与三维建模，支持多方案比对择优 [[S48,S50]]。
5. **砂芯与模板设计**：完成砂芯结构、分盒面、芯头参数设计，在标准模板上排布铸件与浇冒口系统。
6. **CAE仿真验证**：将全工艺三维模型输出给CAE环节，开展充型、凝固过程模拟，基于仿真结果迭代优化工艺参数。
7. **CAM数据传递**：优化后的最终工艺三维模型直接传递给CAM环节，驱动模样、芯盒、模具的数控加工制造 [[S3,S14]]。
8. **工艺文档输出**：自动从三维模型提取二维视图信息，绘制输出标准化铸造工艺图、铸造工艺卡及管理文档。

## 常用软件与工具

### 通用三维CAD平台

工业实践中，铸造工艺设计主要依托通用三维CAD软件开展 [[S31,S44]]。第一代二维平台以AutoCAD为代表，通过AutoLISP/ARX二次开发可生成铸件图与工艺卡 [[S24]]。当前主流三维平台包括：

| 软件 | 开发商 | 铸造相关功能/模块 | 特点 |
|---|---|---|---|
| UG NX | Siemens | Moldwizard（压铸模分型、拔模、模架生成），WAVE装配建模 | 支持STL/IGES输出对接CAE |
| Pro/ENGINEER | PTC | MOLDESIGN模块 | 全参数化统一数据库，修改同步 |
| CATIA | Dassault | 全三维工艺工装建模 | 最高15阶贝塞尔曲面，适配航空汽车复杂铸件 |
| SolidWorks | SolidWorks | 第三方二次开发扩展铸造插件 | Windows平台，易用性好，中小企业主流 |
| Solid Edge | Siemens | 内置铸造设计模块 | Parasolid内核，操作门槛较低 |

### 铸造专用软件

**国际主流仿真工具**（含CAE与CAD/CAE一体化）[[S19,S31,S40,S41,S54]]：

| 软件 | 开发商 | 计算方法 | 核心功能 |
|---|---|---|---|
| MAGMASOFT | Magma（德国） | FDM | 充型、凝固、微观组织、残余应力、铸件/铸型变形，含压铸专用模块，全球部署250余家 |
| ProCAST | ESI（法国） | FEM | 覆盖全品类铸造工艺与合金，可预测残余变形与应力，全球部署150余家 |
| FLOW-3D | Flow Science（美国） | — | 充型液态金属流动模拟精度突出，全球部署200余家 |
| AnyCasting | 韩国生产技术研究院 | — | 首个支持云端铸造数值模拟的商用软件，含充型、凝固、循环铸造模块 |

**国内代表软件** [[S4,S34]]：

| 软件 | 开发单位 | 说明 |
|---|---|---|
| FTCAD（铸造之星） | 清华大学 | 面向球墨铸铁件浇冒口系统参数化设计 |
| CASTCAD | 国内开发 | 集成化铸造工艺辅助设计，适配铝、铸钢、铸铁全品类 |
| 华铸InteCAST | 华中科技大学 | 国内商品化程度最高的铸造CAE软件，依托通用CAD平台完成工艺建模 |
| DCDsoft | 华北工学院 | 压铸专用CAD/CAE/CAM一体化系统 |

## 与CAE/CAM的关系

### 集成衔接机制

铸造工艺CAD是铸造工艺CAE的基础，将带有工艺属性的铸件/砂型/砂芯造型文件传递到CAE系统开展凝固、充型等数值模拟；CAE输出的温度场、流场、应力场分析结果反向反馈至CAD系统进行迭代优化，直至工艺方案满足要求 [[S3,S29]]。优化完成后，CAD将造型文件、工艺图、工艺卡等传递到工装CAM/RPM系统，直接驱动模样、模板、模具、芯盒的数控加工或快速成型制造 [[S3,S14]]。

### 系统集成模式

CAD/CAE/CAM系统间的信息交换存在三种模式 [[S18,S29]]：

| 模式 | 原理 | 特点 |
|---|---|---|
| 点对点专有格式交换 | 子系统间两两开发专用接口 | 原理简单，但子系统增多后接口维护成本极高 |
| 标准中性文件星形交换 | 基于IGES等标准格式，每个系统只与标准文件对接 | 大幅减少接口开发量，为当前主流 |
| 统一产品数据模型直接交换 | 基于STEP标准与统一PDM系统 | 集成度最高，系STEP的核心实现思路 |

实现CAD/CAE/CAM一体化的常用技术路径之一是开发专用接口转换程序实现跨系统信息流传输 [[S14,S36]]。

## 数据交换标准

### IGES

IGES（初始图形交换规范）由美国国家标准局制定，已成为国际标准，支持线框、曲面、边界表示模型、体素构造模型的跨系统交换，广泛用于产品几何设计与有限元分析环节 [[S28,S45]]。IGES的局限在于仅能覆盖局部几何信息，无法完整支持公差、加工工艺、材料属性等非几何类全生命周期产品数据交换 [[S14,S16]]。

![IGES标准中性模型数据交换流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a773d0bb-ee50-4b4b-95cb-2b481c9a2c73/resource)

### STEP

STEP（产品模型数据交换标准）由国际标准化组织（ISO）制定，采用应用层、逻辑层、物理层三级架构，定义EXPRESS数据描述语言，不仅可传递产品几何信息，还可完整传递加工、装配、公差等全流程非几何信息 [[S18,S28]]。在铸造链条中，STEP是连接上游产品设计与下游铸造工艺设计的核心纽带，同时连接铸造工艺输出与工装CAM加工环节，并支持并行工程、跨企业数据共享、产品数据长期存档等场景 [[S3,S33]]。目前STEP仍处于持续迭代发展，尚未完全取代IGES，二者并行使用 [[S14,S36]]。

### STL

STL格式通过大量空间三角形面片逼近原始三维实体，不存在不同CAD系统间的建模兼容性问题，广泛作为铸造工艺CAD与CAE数值模拟系统、快速原型制造（RPM）系统之间的通用转换接口 [[S3,S14,S47]]。其优点是数据处理逻辑简单、与CAD系统无关；缺点是存在顶点重复记录带来的冗余，面片数量过大时文件体积显著膨胀 [[S47]]。

### 格式选用建议

在CAE仿真的前处理环节，不同格式导入后的网格质量存在差异：高质量IGS文件导入后网格匹配率通常高于STL和STP格式，但存在重叠/缺失曲面的低质量IGS文件会大幅增加网格缺陷；使用STP格式导入可获得最优网格效果，IGS文件质量不佳时宜优先选用STL格式 [[S37,S53]]。

## 优势与局限

### 与传统手工设计的比较优势

与传统的铸造工艺设计方法相比，铸造工艺CAD具备以下优势 [[S2,S7,S21]]：

- **计算准确迅速**：可消除人为计算误差。
- **多方案并行比对**：可同时对多个不同方案进行工艺设计与比较，筛选最优方案。
- **经验知识复用**：可系统存储并复用资深铸造工程师的经验知识库，经验不足的设计人员也能输出合规合理的工艺方案。
- **自动化文档输出**：计算结果自动存档，工艺图自动绘制输出，大幅提升设计效率、缩短工艺开发周期。
- **全链路数据贯通**：生成的三维模型可为后续CAE、CAM、CAPP及CIMS实施提供完备的基础信息。

基于三维造型平台的铸造工艺CAD系统还具有额外优势：设计人员在三维零件造型上直接开展工艺设计，过程直观、计算精度高；三维模型几何信息完整，更易于与CAE及工装CAD/CAE系统数据共享 [[S21]]。

### 当前局限

- **自动化程度有限**：各类工艺参数设定、冒口/冷铁放置位置等操作仍高度依赖人工介入 [[S38]]。
- **通用智能系统难度大**：面向全品类任意复杂铸件的通用智能专家系统开发难度极大，需投入极高的人力和研发成本，短期内难以完全落地全覆盖 [[S17,S38]]。
- **数据交换损失**：不同CAD/CAE系统间通过IGES、STL等中性文件传输模型时，易出现复杂面片报错、模型精度降低等问题 [[S17,S38]]。
- **部分专用系统功能缺口**：部分早期压铸CAD系统内置特征库不足，未集成冷却系统设计模块，部分基于AutoCAD平台的系统仅支持外形简单、无倒扣结构的单型腔铸件 [[S9,S43]]。

## 发展趋势

### 集成化

在三维铸造工艺CAD技术基础上，将铸造工艺CAE和铸造生产CAM深度集成为一体化系统，最终构建铸造业CIMS（计算机集成制造系统），实现设计-模拟-加工全流程数据无缝流转，是铸造工艺CAD的核心发展方向 [[S10,S29]]。

### 参数化设计

将可变尺寸设置为控制参数，可大幅提升建模效率，修改设计时仅需调整对应参数即可自动同步更新关联模型，已在压铸溢流槽设计、浇注系统建模等场景得到广泛应用 [[S58,S30]]。

### 智能化

引入专家系统、特征识别技术、相似铸件工艺推荐算法、BP神经网络、模糊集合理论等，将隐性铸造经验转化为显性规则辅助设计决策。集成缺陷预测模型的智能设计系统可实现冒口结构自动化优化，设计周期缩短30%以上；基于相似铸件检索的数字化设计闭环，工艺开发效率比传统"试错模式"提升40%以上 [[S52,S12]]。

### 基于模型的定义（MBD）

全三维无图纸工艺设计是铸造工艺CAD的前沿方向。依托STEP统一产品数据交换标准，在统一产品数据模型中同时完整包含几何信息、加工信息、公差信息、铸造工艺信息等全流程非几何属性，支持并行环境下的多系统信息直接交互，大幅提升系统集成性 [[S29,S36]]。

## Sources
- S25: [TextNode52](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/611f3f08-f8c1-4ef6-b147-317b41dd250f/resource) (`611f3f08-f8c1-4ef6-b147-317b41dd250f`)
- S7: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a4d7375-9e95-497c-8c40-a205cc6379ff/resource) (`1a4d7375-9e95-497c-8c40-a205cc6379ff`)
- S2: [TextNode96](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01052716-190b-4a22-af81-fd0f219c7454/resource) (`01052716-190b-4a22-af81-fd0f219c7454`)
- S10: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/29a5a376-ba2b-4f3e-b231-328b6b732dfa/resource) (`29a5a376-ba2b-4f3e-b231-328b6b732dfa`)
- S21: [TextNode443](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49e7efa0-5d59-4d9e-be5b-7aa549437955/resource) (`49e7efa0-5d59-4d9e-be5b-7aa549437955`)
- S55: [大型铸钢件铸造工艺CAD系统示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e32cc54d-9518-422f-ab79-e1e8f3f7e7c0/resource) (`e32cc54d-9518-422f-ab79-e1e8f3f7e7c0`)
- S27: [TextNode442](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/678cf68f-5335-419c-a1ed-1a2b8f609b80/resource) (`678cf68f-5335-419c-a1ed-1a2b8f609b80`)
- S5: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f194f3e-f22e-48b5-8bbf-dad595c2a750/resource) (`0f194f3e-f22e-48b5-8bbf-dad595c2a750`)
- S29: [TextNode444](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a01aff2-e3bd-467d-97f6-f9a26318b729/resource) (`6a01aff2-e3bd-467d-97f6-f9a26318b729`)
- S50: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc34aebc-2474-42a0-aa7a-20292247a49b/resource) (`bc34aebc-2474-42a0-aa7a-20292247a49b`)
- S48: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbdc71a5-50d2-4c9a-bb89-952f2b940d6b/resource) (`bbdc71a5-50d2-4c9a-bb89-952f2b940d6b`)
- S3: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07955f8f-1c17-4f19-9425-aaab8bc6e29c/resource) (`07955f8f-1c17-4f19-9425-aaab8bc6e29c`)
- S14: [压铸工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32aeeb36-aaf4-4acd-8b26-0325eae0e064/resource) (`32aeeb36-aaf4-4acd-8b26-0325eae0e064`)
- S31: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/83964371-cd55-4357-b8f3-2d230148e14c/resource) (`83964371-cd55-4357-b8f3-2d230148e14c`)
- S44: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad14679d-a737-4681-a5af-3dfc99d408a5/resource) (`ad14679d-a737-4681-a5af-3dfc99d408a5`)
- S24: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ea52d38-61fb-461e-9164-f0b08b2f36e0/resource) (`5ea52d38-61fb-461e-9164-f0b08b2f36e0`)
- S19: [世界知名铸造过程仿真软件主要功能与适用范围](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4972aa4b-4632-4c78-9067-90879d1aedd5/resource) (`4972aa4b-4632-4c78-9067-90879d1aedd5`)
- S40: [表1.1 国内外部分铸造软件及应用功能简介](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e0862eb-9852-4afa-bdf2-6a892ca415fe/resource) (`9e0862eb-9852-4afa-bdf2-6a892ca415fe`)
- S41: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6c0ddc9-3495-490b-bb55-129392d012fc/resource) (`a6c0ddc9-3495-490b-bb55-129392d012fc`)
- S54: [世界知名铸造过程仿真软件主要功能与应用情况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db4066df-5b3f-4764-b4b2-33031f4399ce/resource) (`db4066df-5b3f-4764-b4b2-33031f4399ce`)
- S4: [表2.1 国内外主流铸造软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0eece464-963e-4081-ad3d-363f5dc82bb1/resource) (`0eece464-963e-4081-ad3d-363f5dc82bb1`)
- S34: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94f024fc-c54f-476b-92e4-cb97a88ea0c1/resource) (`94f024fc-c54f-476b-92e4-cb97a88ea0c1`)
- S18: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47058aae-0fbc-4e04-bfbd-a3444d3eec05/resource) (`47058aae-0fbc-4e04-bfbd-a3444d3eec05`)
- S36: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/961da558-87b3-4c67-8a97-690f3154c543/resource) (`961da558-87b3-4c67-8a97-690f3154c543`)
- S28: [机械加工工艺手册第3卷系统技术卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68dd4035-a242-4bfa-b851-914ba3d5b207/resource) (`68dd4035-a242-4bfa-b851-914ba3d5b207`)
- S45: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad824ad1-95ca-44d9-80ea-04ab3451fe71/resource) (`ad824ad1-95ca-44d9-80ea-04ab3451fe71`)
- S16: [computer integrated manufacturing__7d9077b0f8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40950a56-5fe8-43e6-aac3-23375b31f560/resource) (`40950a56-5fe8-43e6-aac3-23375b31f560`)
- S33: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/948fb30a-7979-4993-98e6-b6f8d7e80d28/resource) (`948fb30a-7979-4993-98e6-b6f8d7e80d28`)
- S47: [数字化模具制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb1e0398-ea44-4e87-bfec-b0f29e5ed19a/resource) (`bb1e0398-ea44-4e87-bfec-b0f29e5ed19a`)
- S37: [Moldflow 2015模流分析从入门到精通 升级版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9701749e-3660-4e9e-b0c6-6df8956112c8/resource) (`9701749e-3660-4e9e-b0c6-6df8956112c8`)
- S53: [Moldflow 2018模流分析从入门到精通（升级版）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d654b284-bfe6-4e2c-923e-fbdc6c569165/resource) (`d654b284-bfe6-4e2c-923e-fbdc6c569165`)
- S38: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9715647a-9af8-4a74-ab1c-4bb773fe188c/resource) (`9715647a-9af8-4a74-ab1c-4bb773fe188c`)
- S17: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42c6d40b-6e16-4bcc-966b-b8008d47ea1c/resource) (`42c6d40b-6e16-4bcc-966b-b8008d47ea1c`)
- S9: [development of a die design system for die casting__32289742a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fb19d2a-3a77-4ccd-b954-f36969dd6bc4/resource) (`1fb19d2a-3a77-4ccd-b954-f36969dd6bc4`)
- S43: [development of a die design system for die casting__32289742a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab5103eb-2375-476b-bf8f-6025fc6fdb17/resource) (`ab5103eb-2375-476b-bf8f-6025fc6fdb17`)
- S58: [development of a die design system for die casting__32289742a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fff9ddcf-e369-49f0-8751-de222c8f6b5c/resource) (`fff9ddcf-e369-49f0-8751-de222c8f6b5c`)
- S30: [NX软件中溢流槽参数化的表达式设计界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7778c962-bc53-445a-abf8-7d744a29273a/resource) (`7778c962-bc53-445a-abf8-7d744a29273a`)
- S52: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8e628cf-3eaa-4ed9-bbb0-f4e35e21c8f5/resource) (`c8e628cf-3eaa-4ed9-bbb0-f4e35e21c8f5`)
- S12: [基于形状和工艺相似铸件的工艺推荐系统研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2af73210-9a5b-4889-ad5f-13dc748bb6e2/resource) (`2af73210-9a5b-4889-ad5f-13dc748bb6e2`)