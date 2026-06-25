---
version: "v1"
generated_at: "2026-06-18T18:29:51+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.87
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

## 概述

Unigraphics NX（简称UG、UG-NX，现称Siemens NX）是由Siemens PLM Software推出的集CAD（计算机辅助设计）、CAE（计算机辅助工程）、CAM（计算机辅助制造）、PDM（产品数据管理）于一体的三维参数化集成工业软件，采用Parasolid实体建模核心技术，支持从产品概念设计到数控加工全流程的数字化造型、仿真验证与数据无缝集成，面向全产品生命周期管理提供经过工程验证的解决方案[[S8,S41,S23,S20]]。该软件广泛适用于航空航天、汽车、通用机械、模具设计、电子工业等工程设计领域[[S18,S29,S20,S41]]，在压铸模具设计领域更是当前主流的三维工业软件，具备完善的复杂型面建模、模具装配设计、数控加工刀路生成能力，可支撑从压铸件产品三维建模到压铸模具全结构设计、后续数控加工的全链路需求[[S8,S20,S38]]。

## 发展历史与版本沿革

Unigraphics系列软件经历了漫长而关键的发展历程。1983年，UG产品正式进入市场；1990年被选定为McDonnell Douglas（即后来的波音公司）的机械CAD/CAE/CAM标准[[S8,S16]]。1993年，UG首次引入复合建模概念，融合实体建模、曲面建模、线框建模、半参数化及参数化建模能力，同年被美国通用汽车选为全公司CAD/CAE/CAM/CIM主导系统[[S8]]。1995年首次发布Windows NT版本[[S8,S16]]，此后陆续新增自动干涉检查高级装配模块、先进CAM模块、A级曲面造型工业设计模块以及WAVE产品模板管控技术[[S8]]。

1997年Unigraphics Solutions公司合并Intergraph旗下机械CAD产品，将Solid Edge统一至Parasolid平台，形成覆盖高低端、同时支持UNIX工作站和Windows NT微机的全层级CAD/CAE/CAM/PDM集成系统[[S8]]。2000年发布的UG V17版本成为业界首个支持深度嵌入基于工程知识（KBE）语言的主流MCAD软件[[S8,S16]]。2001年EDS公司收购UGS后合并SDRC，整合UGII最高独立版本V18与IDEAS最高独立版本V8后发布重命名的UG NX 1.0[[S19,S16]]。在NX 5.0版本阶段，Unigraphics Solutions被德国西门子公司正式收购，归属西门子旗下产品线，后续发布的NX 6.0版本主界面开始明确显示“SIEMENS”标识[[S16]]。此后版本继续迭代，陆续推出NX 7.5、NX 8.0、NX 8.5、NX 9.0、NX 10.0、NX 12.0等官方正式版本[[S16,S36,S34]]。

![早期UGS旗下NX产品官方主题图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a00075c1-8d39-47a0-8dbd-07a06c262a31/resource) [[S28]]

![Unigraphics NX 2建模操作界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63a460d0-01ca-4992-97d0-4038e6167038/resource) [[S21]]

## 类别与定位

Unigraphics NX不属于单一功能的普通CAD软件，而是面向全产品生命周期管理的高端数字化产品开发解决方案类软件[[S18,S29,S20,S41]]。该系统实现了CAD/CAM/CAE三大系统紧密集成：用户在使用实体造型、曲面造型、虚拟装配及创建工程图等设计功能时，可使用CAE模块进行有限元分析、运动学分析和仿真模拟以提高设计可靠性；根据建立的三维模型，还可由CAM模块直接生成数控代码用于产品加工[[S8,S23]]。

在压铸模具开发链中，NX承担着从压铸件产品三维建模到模具结构设计、仿真前处理数据输出、数控加工编程的全链路核心角色[[S8,S20]]。国内压铸模具设计领域已有专业书籍《UG压铸模具设计入门与提高》（电子工业出版社，2008）系统讲授了端盖、罩盖、箱架等典型压铸零件从NX三维建模、分型面创建、压铸模全零部件设计到装配、工程图导出的全流程应用实例[[S31,S42,S33]]。同时，NX压铸模具设计流程可匹配国内现行压铸领域相关国家标准，包括GB/T 8847-2003《压铸模术语》、GB/T 4678系列压铸模零件标准及GB/T 15115-2024《压铸铝合金》等[[S3,S25]]。

## 核心功能与模块（压铸场景）

### 实体与曲面建模

Siemens NX面向压铸场景的实体建模工具包含拉伸、回转、沿导引线扫掠等功能，自由曲面建模则提供点到面、线到面、面到面三类工具，可支持压铸件成形特征的快速抽取与建模操作[[S11,S15]]。压铸件整体建模流程一般包括建立UG部件文件、选择应用环境、检查/预设置参数、建立关键设计变量、创建对象、分析对象、修改对象、保存文件等步骤[[S15]]。

### 分模工具

UG NX压铸专用分模流程覆盖压铸模具分型面的判别和脱模方向计算，支持快速创建水平分型面、斜分型面与阶梯分型面，随后完成动定模划分、凹模/凸模/型芯的创建工作，适配各类复杂压铸模具的分模需求[[S37,S33]]。

### 浇注系统与溢流排气系统设计

UG NX在压铸场景下可独立完成浇注系统的快速创建，同时支持溢流、排气系统的参数化建模，直接匹配压铸工艺的充型与排气设计要求[[S37,S24]]。基于NX平台实现的压铸溢流槽参数化快速建模，其输出的三维数据可直接对接华铸CAE等压铸专用数值模拟软件，实现CAD与压铸模流仿真前处理的无缝集成[[S12]]。

### 装配设计

UG NX支持面向压铸模具设计的三类装配建模方案：自底向上装配建模、自顶向下装配建模，以及基于UG/WAVE关联技术的自顶向下压铸模具设计方法。其中WAVE技术可实现模具零部件的同步更新与快速修改[[S40,S42]]。装配过程中，模具零件以逻辑对齐、贴合、偏移等方式灵活地配对和定位，零件设计修改后装配模型会自动更新，保持双向关联性[[S27]]。

### Mold Wizard模块

UG Mold Wizard模块原生为注塑模设计开发，但分型面选择、拔模方向、收缩率、顶杆、复位杆等核心设计原理与压铸模设计高度相通。通过适配修改金属收缩率、镶块尺寸等参数，可实现压铸模的自动化设计。完整流程为：项目初始化→压铸模具坐标系确定→金属收缩率设置→成型镶块尺寸定义→型腔布局→修补分模面→生成型芯与型腔[[S30,S35]]。鉴于压铸合金（如ADC铝合金）的收缩率通常不在UG数据库预设之内，需在“项目初始化”中将“部件材料”设为“无”，在后续步骤中手动设置收缩率（如X、Y、Z均为1.005）[[S30,S35]]。

### 工程图

NX工程图模块生成的压铸模具二维视图与三维实体模型完全关联。当三维模型发生修改时，工程图的尺寸、视图等信息可自动同步更新，同时支持输出符合GB、ISO、ANSI等标准的零件工程图与模具装配工程图[[S9,S40]]。

![UG NX 4.0环境下创建后导入AutoCAD编辑完成的压铸模具装配工程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23d007f4-cd63-48ea-a14a-e6b642611d5a/resource) [[S7]]

## 工艺角色与工作流

基于UG NX的压铸全流程标准工作流可分为四个阶段[[S42,S33]]：

| 阶段 | 主要任务 | 使用的核心NX功能 |
|------|----------|------------------|
| **压铸件产品设计阶段** | 完成压铸件三维实体建模与成形特征校验 | 实体建模、曲面建模、脱模斜度与圆角设置 |
| **压铸模具开发阶段** | 完成分模、浇注排气系统设计、抽芯/导向/推出等机构的装配建模 | 分模工具、浇注/溢流系统创建、装配建模（自底向上/自顶向下/混合） |
| **仿真迭代准备阶段** | 输出对接压铸模流分析软件的前处理数据 | CAD数据导出（STEP、IGES、Parasolid、STL等格式） |
| **数控加工阶段** | 完成所有模具成型零件的数控加工编程，最终输出加工刀路文件 | NX CAM模块 |

### 重卡接线盒建模示例

针对重卡接线盒这类典型的盒类薄壁多筋压铸件，采用UG NX进行三维建模时，可依次抽取接线盒的安装、密封、散热等成形特征，完成薄壁主体、内部安装凸台、散热筋等结构的参数化建模，设置适配铝合金压铸的脱模斜度与圆角，预留后续机加工余量，再通过分模工具快速生成对应的动定模仁、侧抽芯机构与浇注溢流系统[[S15,S37]]。

![基于UG的压铸模CAD系统完整功能流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef5cd370-097b-4a5f-be00-a747c841f899/resource) [[S39]]

## 专用术语与别名

| 类别 | 内容 | 来源 |
|------|------|------|
| 通用别名 | Unigraphics、UG、UG-NX、Siemens NX | [[S16,S41,S1,S10]] |
| 当前正式名称 | Siemens NX | [[S16,S41]] |
| 核心文件格式 | .prt（原生专有文件格式，用于存储三维模型、装配结构、工程图关联数据） | [[S1,S34]] |
| 关键模块名称 | Mold Wizard、UG/WAVE、NX CAM | [[S30,S35,S27,S33]] |

## 与其他系统的关系

### 与模流分析软件的数据交换

Unigraphics NX原生支持与压铸模流软件的通用CAD数据交换，支持的标准格式包括STEP（STEP203、STEP214）、IGES、Parasolid(*.x_t)、STL等[[S18,S22,S6]]。其中MAGMA软件可直接读取NX导出的STL格式完成前处理几何导入，大幅降低跨平台数据丢失风险[[S6]]。NX的CAD数据交换能力处于行业领先水平，转换后的模型可保留可编辑特征，无需重新建模[[S18]]。

基于NX10.0平台通过二次开发（Block UI Styler、UFUN接口）可实现压铸数值模拟系统的无缝集成，无需跨软件切换即可在NX环境内直接完成切片法网格剖分、卷气/缩孔缺陷后处理可视化、参数化溢流槽快速建模等操作，减少数据传递环节，已有罩壳压铸件、新能源汽车电池壳的应用验证实例[[S32,S13]]。

![UG NX导出模型导入压铸仿真软件后的操作界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1629b2a8-7323-4127-a5d1-ca6f5c51254d/resource) [[S4]]

### 与PLM/Teamcenter的集成

Siemens NX与同属西门子体系的Siemens Teamcenter/PLM系统天然原生集成，采用统一的主模型机制，实现压铸模具全生命周期设计、工艺、制造数据的同步共享，支持多人并行协同设计[[S27]]。

### CAD/CAE集成应用实例

基于华铸压铸模CAD的压铸模设计系统，以NX为三维造型和二次开发平台，集成零件预处理、成形部分设计、浇溢流系统设计、模架设计等模块，输出STL文件可直接传入华铸CAE完成数值模拟，实现CAD/CAE闭环优化，已完成后盖压铸零件的压铸工艺与全模具三维设计验证[[S33]]。

NX平台还可对接压铸CAE仿真后处理的可视化显示需求，建立了温度场、流动场可视化色标区间与NX系统内置颜色编号的一一对应规则，使仿真结果可直接在NX环境中进行渲染分析[[S38]]。

## 在压铸领域的应用案例

- **专业教材体系**：《UG压铸模具设计入门与提高》（电子工业出版社，2008）系统提供了端盖、罩盖、箱架等典型压铸件的完整NX建模与模具设计实例，内容按压铸模具实际设计工作流程编排，符合压铸模具行业设计规范[[S31,S42,S33]]。
- **华铸集成系统**：基于UG的华铸压铸模CAD系统集成了零件预处理、成形部分设计、浇溢流系统设计、模架设计等模块，输出直接对接华铸CAE，已完成后盖压铸件的工艺设计与全模具三维验证[[S33]]。
- **二次开发集成**：基于NX10.0的压铸数值模拟集成系统实现了切片法网格剖分、卷气/缩孔缺陷后处理、溢流槽快速建模等功能的NX内嵌集成，已在罩壳压铸件和新能源汽车电池壳实例中得到验证[[S32,S13]]。
- **Mold Wizard适配实例**：以背投电视冷却腔（ADC铝合金）为例，利用Mold Wizard完成了从项目初始化、收缩率设置（X、Y、Z均为1.005）、镶块尺寸定义到分型面生成的完整压铸模设计流程[[S30,S35]]。

## Sources
- S8: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3125672b-dfcf-4e7e-8638-832cc3cb6635/resource) (`3125672b-dfcf-4e7e-8638-832cc3cb6635`)
- S41: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8eb10cb-e1cc-461d-92ad-b981b4a32466/resource) (`f8eb10cb-e1cc-461d-92ad-b981b4a32466`)
- S23: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/768f3647-beac-4b35-8b78-ba45cdfba52e/resource) (`768f3647-beac-4b35-8b78-ba45cdfba52e`)
- S20: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ea52d38-61fb-461e-9164-f0b08b2f36e0/resource) (`5ea52d38-61fb-461e-9164-f0b08b2f36e0`)
- S18: [cadcam模具设计与制造实用教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4aaed525-e7e5-4502-b625-e885e4c1c82a/resource) (`4aaed525-e7e5-4502-b625-e885e4c1c82a`)
- S29: [三维建模与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae2630db-6556-42a2-8606-a6ef62304be6/resource) (`ae2630db-6556-42a2-8606-a6ef62304be6`)
- S38: [表2-2 色标映射表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e30f208a-f5ab-4266-8ecc-b08fe35793d6/resource) (`e30f208a-f5ab-4266-8ecc-b08fe35793d6`)
- S16: [ug数控加工自动编程经典实例教程第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/461bf3a0-e427-48d1-8542-b2adf4ec3013/resource) (`461bf3a0-e427-48d1-8542-b2adf4ec3013`)
- S19: [模具先进制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ad14312-11e3-4725-a771-374ed42758d9/resource) (`4ad14312-11e3-4725-a771-374ed42758d9`)
- S36: [UG NX 12.0模具设计完全学习手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf8dba94-e375-40f7-a193-6b2612adf3d3/resource) (`cf8dba94-e375-40f7-a193-6b2612adf3d3`)
- S34: [UG NX 10.0 设计 模具 完全学习手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb4748ff-3ca1-4b1c-8d9a-0a58c91aa2fb/resource) (`cb4748ff-3ca1-4b1c-8d9a-0a58c91aa2fb`)
- S28: [UG NX软件相关主题图片](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a00075c1-8d39-47a0-8dbd-07a06c262a31/resource) (`a00075c1-8d39-47a0-8dbd-07a06c262a31`)
- S21: [UG软件中的零件三维建模界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63a460d0-01ca-4992-97d0-4038e6167038/resource) (`63a460d0-01ca-4992-97d0-4038e6167038`)
- S31: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7ebee3a-adf1-4cf9-a065-610258e6630c/resource) (`b7ebee3a-adf1-4cf9-a065-610258e6630c`)
- S42: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb0de9cf-73be-4cbb-9dde-da905ed14bab/resource) (`fb0de9cf-73be-4cbb-9dde-da905ed14bab`)
- S33: [模具设计基础及模具cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8dd952c-ec93-4303-bdbd-013488dc1bbf/resource) (`c8dd952c-ec93-4303-bdbd-013488dc1bbf`)
- S3: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1455808a-e78b-47ad-a074-08246342c605/resource) (`1455808a-e78b-47ad-a074-08246342c605`)
- S25: [64380928_压铸铝合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/946c37f9-0dac-4d06-9c46-873a93dcf173/resource) (`946c37f9-0dac-4d06-9c46-873a93dcf173`)
- S11: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40aa74c8-0182-47c1-bc8c-59a7cf1af323/resource) (`40aa74c8-0182-47c1-bc8c-59a7cf1af323`)
- S15: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4505b3ca-62ee-45c5-b291-4f6704b17004/resource) (`4505b3ca-62ee-45c5-b291-4f6704b17004`)
- S37: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d17ccb5f-74fd-42de-9a2c-62838d341cb5/resource) (`d17ccb5f-74fd-42de-9a2c-62838d341cb5`)
- S24: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79ff98f5-4acc-4aed-95df-568b5157fedb/resource) (`79ff98f5-4acc-4aed-95df-568b5157fedb`)
- S12: [基于NX的压铸数值模拟集成与溢流槽快速建模系统研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/421789e3-2c95-45d7-9736-c84c5093ed7a/resource) (`421789e3-2c95-45d7-9736-c84c5093ed7a`)
- S40: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2d27e45-d617-41c9-bc19-a48aa372478a/resource) (`f2d27e45-d617-41c9-bc19-a48aa372478a`)
- S27: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ef284ae-95d3-47d0-bcf0-c10573444def/resource) (`9ef284ae-95d3-47d0-bcf0-c10573444def`)
- S30: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b04d3f97-0129-4b42-8bc0-ec1f5cc4e3ea/resource) (`b04d3f97-0129-4b42-8bc0-ec1f5cc4e3ea`)
- S35: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb7c158f-0131-4bbb-adfb-6a34726ccaeb/resource) (`cb7c158f-0131-4bbb-adfb-6a34726ccaeb`)
- S9: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3759fcb9-3f61-4101-9453-cf6ede8ee926/resource) (`3759fcb9-3f61-4101-9453-cf6ede8ee926`)
- S7: [气动刮水器盖压铸模具装配工程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23d007f4-cd63-48ea-a14a-e6b642611d5a/resource) (`23d007f4-cd63-48ea-a14a-e6b642611d5a`)
- S39: [压铸模CAD系统功能模型图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef5cd370-097b-4a5f-be00-a747c841f899/resource) (`ef5cd370-097b-4a5f-be00-a747c841f899`)
- S1: [UG_NX_9.0模具设计完全学习手册.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0488ab63-71b7-41a7-a0a4-0af6ca4af598/resource) (`0488ab63-71b7-41a7-a0a4-0af6ca4af598`)
- S10: [UG NX 8.5 注射模具设计实例精讲](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fc09e2f-13f8-48b4-8fd5-87c4e8977044/resource) (`3fc09e2f-13f8-48b4-8fd5-87c4e8977044`)
- S22: [ugnx120数控加工编程应用实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75ab154b-56a9-4578-b257-480b38c8813d/resource) (`75ab154b-56a9-4578-b257-480b38c8813d`)
- S6: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20f2db5c-2a6f-49c1-ae1d-2e9451819b4d/resource) (`20f2db5c-2a6f-49c1-ae1d-2e9451819b4d`)
- S32: [基于NX的压铸数值模拟集成与溢流槽快速建模系统研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bda64f6e-42b5-4a33-a450-63b641f293b8/resource) (`bda64f6e-42b5-4a33-a450-63b641f293b8`)
- S13: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43ab30f5-c6ab-4556-a92e-10f38e38c62b/resource) (`43ab30f5-c6ab-4556-a92e-10f38e38c62b`)
- S4: [Autodesk Moldflow 2012软件中导入的塑件模型界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1629b2a8-7323-4127-a5d1-ca6f5c51254d/resource) (`1629b2a8-7323-4127-a5d1-ca6f5c51254d`)