---
version: "v1"
generated_at: "2026-06-18T11:48:18+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 43
  source_quality_score: 0.87
  freshness_score: 0.76
  evidence_coverage_score: 1.0
---

## 概述

Unigraphics（简称UG，后续迭代版本名为Siemens NX，国内常俗称UG三维制图软件）是集CAD/CAE/CAM/PDM于一体的全三维参数化工程软件，拥有统一数据库支持全流程数据无缝集成[[S5,S14,S7,S28]]。该软件最早应用于美国麦道飞机公司，当前在航空、汽车、压铸模具等行业广泛使用[[S5,S7]]。在压铸领域，Siemens NX（UG）覆盖高压压铸模具从概念设计、功能工程、加工制造到产品发布的全开发环节，是压铸行业应用广泛的主流通用压铸模具设计工具[[S50,S46,S12]]。

## 历史演变与别名

### 开发商变更

UG软件的完整开发商变更时间线如下[[S14,S7,S15]]：

- 1970年代，由美国麦道飞机公司开发；
- 1991年11月，并入EDS公司，后续独立为Unigraphics Solutions（UGS）公司；
- 1997年，Unigraphics Solutions合并Intergraph公司的机械CAD产品线，纳入Solid Edge；
- 2001年，EDS收购UGS全部股权，同时并购IDEAS开发商SDRC公司，将UG与IDEAS技术合并后正式推出NX产品线；
- 后续UGS整体被西门子收购，先后归属Siemens PLM Software、Siemens Digital Industries Software，从NX 6.0版本开始软件界面正式标注SIEMENS标识[[S14]]。

### 版本发展脉络

UG到NX系列的版本发展过程如下[[S5,S14,S7,S32,S3]]：

| 时间节点 | 版本/事件 |
|---------|----------|
| 1983年 | UG产品正式进入市场 |
| 1990年 | UG成为波音公司（原麦道）的官方CAD/CAE/CAM标准 |
| 1995年 | 首次发布Windows NT版本 |
| 2000年 | 发布UG V17，成为全球首个内置深度KBE（基于工程知识）语言的主流MCAD软件 |
| 2001年 | 发布UG V18，同年后续产品线正式更名为NX |
| 2001年后 | 先后推出NX 1.0至NX 11.0系列版本 |
| 2017年 | 推出NX 12.0版本 |
| 2019年 | NX 12.0发布配套全系列官方教程 |

NX 12.0版本面向全流程产品研发，基于NX 5.0引入的角色化交互框架进一步扩展全应用场景覆盖，优化了与Teamcenter的深度集成能力，强化了逆向工程处理、曲面建模、I-DEAS内核迁移、NX Nastran求解的全链条能力[[S40]]。

### 别名说明

各别名的产生原因如下[[S45,S14,S33]]：

- **UG**：Unigraphics的首字母缩写，为行业内传播最广的简称；
- **UG三维制图软件**：国内制造业从业者早期因该软件核心功能优势集中在三维造型制图领域而衍生的俗称；
- **Unigraphics NX / Siemens NX**：被西门子收购后产品线先后使用的两个正式命名；
- **UG12.0软件**：面向压铸模具领域使用的NX 12.0版本被行业内的简称。

## 面向压铸行业的核心模块

### 基本功能模块

UG/NX面向压铸行业的核心预装模块清单包含[[S29,S8,S10]]：

| 模块 | 压铸应用功能 |
|------|-------------|
| UG/Gateway基础环境模块 | 系统运行基础 |
| 三维实体建模模块 | 压铸件与模具零件造型 |
| 曲面建模模块 | 复杂型腔曲面创建 |
| 装配设计模块 | 支持自底向上/自顶向下/WAVE驱动的压铸模具结构设计 |
| 工程图模块 | 压铸模具全系列工程图自动生成与GB/ISO标准标注 |
| 运动仿真模块 | 压铸模具开合模、抽芯、推出全流程运动干涉验证 |
| 数控加工CAM模块 | 型腔型芯等成形零件数控加工刀路生成 |

## 压铸模具设计中的典型作用

### 三维造型与型腔创建

NX三维造型设计环节可基于压铸成形特征完成压铸件三维建模，按指定合金收缩率自动偏移型腔尺寸，通过补孔、特征编辑等操作快速完成压铸模具型腔、型芯等成形零件的三维实体创建[[S22,S50]]。

### 浇注系统与排溢系统设计

在NX通用建模环境下，设计者可完成高压压铸浇注系统（含直浇道、横浇道、内浇口、浇口套、分流锥）和溢流排气系统（含溢流槽、排气槽）的全参数化设计[[S18,S25]]。

![压铸模具浇注、溢流、排气系统设计过程流程图，完整展示两大系统的分步设计节点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b7a6281-6a64-465d-871f-5f25ded5e7b9/resource)

### 装配结构设计

NX装配结构设计环节可通过内置UG/WAVE技术实现高压压铸模具的自顶向下全相关参数化设计，同时兼容自底向上、混合装配两种建模模式，设计修改时所有关联零部件可自动同步更新，大幅提升复杂压铸模具的设计效率[[S16,S25]]。

### 工艺参数计算与校核

NX可自动计算压铸件的体积、质量、分型面投影面积等工艺参数，同时借助实体几何分析功能完成压铸模各部位壁厚的合规性检测，直接匹配压铸机锁模力的选型校核要求[[S41]]。

### 运动仿真与干涉检查

NX内置运动仿真模块，可针对压铸模具的开模动作、侧抽芯机构、推出机构的完整运动过程进行模拟，提前排查验证模具运行过程中的碰撞、干涉风险[[S50,S8]]。

### CAM加工一体化

NX生成的压铸模具三维实体模型可直接无缝对接其内置CAM模块，自动完成型腔型芯等成形零件的数控加工刀路生成，无需额外格式转换，避免数据丢失，实现压铸模设计与制造流程一体化[[S13]]。

### 关于Mold Wizard模块

NX Mold Wizard（注塑模向导）模块是专门面向注塑模场景开发的设计向导模块，内置的所有标准模架库、标准件库均适配注塑模具设计需求，未内置任何高压压铸模具专用的设计向导、压铸模专属标准模架以及压铸专用标准零件库，高压压铸模具设计需在NX通用建模、装配环境下自定义完成[[S51,S34]]。

## 数据交换与协同

### 支持的交换格式

Siemens NX原生支持的通用CAD数据交换格式清单包含Parasolid（\*.x\_t、\*.x\_b）、IGES（\*.igs、\*.iges）、STEP（\*.step、\*.stp）、STL、DXF/DWG等主流格式，同时支持VDA-FS等工业领域常用中性交换格式[[S37]]。

### 与CAE软件的接口

| CAE软件 | 支持的接口格式 |
|---------|---------------|
| ProCAST | 专用Parasolid接口，以及IGES、STEP、STL通用格式[[S1,S21,S47,S20]] |
| MAGMA | IGES、STL、DXF等格式，Pro/E、UG均可直接读取[[S39]] |
| FLOW-3D CAST | STL、IDEAS、ANSYS等实体格式，兼容NX导出的IGES、STL格式[[S2]] |

## 二次开发能力

### 开发工具集

Siemens NX提供完整的二次开发工具集，包含UG/Open GRIP、UG/Open Menu Script、UG/Open UIStyler、UG/Open API（NX Open）四大类接口，支持C、VB、C++等多种主流编程语言进行自定义功能开发[[S19,S11,S31]]。

### 压铸工艺参数自动计算

基于NX二次开发函数库中的UF\_MODL\_ask\_mass\_props\_3d接口可自动获取压铸件的体积、质量、表面积、重心等基础属性参数，配合内置经验公式可自动完成压铸机锁模力、内浇口截面积、浇注系统关键尺寸等压铸工艺参数的自动计算[[S6,S17]]。

### CAD/CAE集成系统

基于NX二次开发可搭建压铸CAD/CAE集成系统，实现压铸网格自动剖分、流场温度场可视化、分型面自动生成、溢流槽参数化快速建模等功能，将传统手工压铸设计效率大幅提升，相关技术已通过汽车压铸件工程实例验证[[S13]]。

## 应用案例

基于NX4.0完成了覆盖压铸件建模、分型面设计、模具零部件创建、装配建模、工程制图、成形运动仿真全流程的压铸模具设计实例，为UG压铸模具设计领域经典工程实践案例，配套有电源盒壳体等典型双斜销抽芯压铸模具零件设计案例[[S35,S50,S4]]。

核心期刊论文中记录了基于NX平台开发的压铸工艺设计CAD/CAE集成系统，以新能源汽车结构件电池壳体作为验证实例完成了浇注系统交互式生成与仿真直接分析，避免跨软件切换带来的模型数据失真问题[[S13]]。

## 局限性与常见问题

### 缺少压铸专用模块

Siemens NX（UG）原生未提供专属压铸模具设计专业模块，基于通用三维造型平台完成压铸模具设计时，对于简单压铸模可以利用自带的实体、曲面造型功能快速完成，但处理结构复杂的压铸模时，整体设计流程会非常繁琐，缺少压铸领域专属的自动化设计引导能力[[S38]]。

### Mold Wizard不适用

在压铸设计场景中直接套用NX自带的面向塑料模具开发的Moldwizard注塑模具模块存在明显局限性，该模块默认的模架参数、工艺规则与压铸模具的实际工艺要求、结构特征存在显著差异，无法完全适配压铸模设计需求[[S38]]。

### 二次开发依赖性

工业界基于NX平台开发的专用压铸模CAD系统属于二次开发附加插件，NX原生功能并未集成该类压铸专属的标准化设计子模块，原生环境下完成完整压铸模的浇注系统、溢流槽、冷却系统快速标准化设计无法直接实现[[S42]]。

### 版本兼容性问题

| 问题类型 | 具体表现 |
|---------|---------|
| 装配加载异常 | 不同NX版本生成的压铸模具装配文件，尤其是使用WAVE关联功能创建的自顶向下关联装配压铸模文件，在高版本NX中直接打开低版本设计的压铸模组件时容易出现WAVE关联断裂、组件加载异常问题，需要用户在NX 12.0的“装配加载选项”对话框中提前手动调整加载参数[[S26]] |
| 后处理器配置失效 | NX 12.0默认采用临时指定方式选择后处理器时，配置仅对当前打开的图档生效，切换图档或重启软件后该配置会自动失效，需要用户手动通过系统环境变量UGII\_CAM\_POST\_DIR指定全局后处理器目录路径重启后方可永久生效[[S44]] |

![UG NX 12.0的“装配加载选项”对话框界面，用于调整压铸模装配文件的加载策略，减少高版本打开低版本压铸模装配文件时出现的关联断裂、组件缺失报错](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e2a93c4-5733-486c-b420-4d862fc169bd/resource)

## 相关信息概览

| 项目 | 内容 |
|------|------|
| 软件全称 | Unigraphics（现Siemens NX） |
| 开发商 | Unigraphics Solutions → Siemens Digital Industries Software |
| 当前主流版本 | NX 12.0，NX系列持续更新 |
| 所属类别 | CAD/CAE/CAM一体化软件 |
| 压铸设计方式 | 通用建模/装配环境自定义设计（无专用压铸模块） |
| 装配技术 | 自底向上/自顶向下/混合装配，UG/WAVE全相关参数化 |
| 数据交换 | Parasolid、IGES、STEP、STL、DXF/DWG、VDA-FS |
| 二次开发 | UG/Open API、GRIP、Menu Script、UIStyler，支持C/C++/VB |
| 典型应用行业 | 汽车及摩托车（占我国压铸件48%）、机械产品及零部件、家电及电子产品[[S23]] |

## Sources
- S5: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f76534e-5f83-4575-969c-6231f090c1d9/resource) (`1f76534e-5f83-4575-969c-6231f090c1d9`)
- S14: [ug数控加工自动编程经典实例教程第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/461bf3a0-e427-48d1-8542-b2adf4ec3013/resource) (`461bf3a0-e427-48d1-8542-b2adf4ec3013`)
- S7: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3125672b-dfcf-4e7e-8638-832cc3cb6635/resource) (`3125672b-dfcf-4e7e-8638-832cc3cb6635`)
- S28: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9984c472-2d2b-4aca-a7b5-795a80e33066/resource) (`9984c472-2d2b-4aca-a7b5-795a80e33066`)
- S50: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb0de9cf-73be-4cbb-9dde-da905ed14bab/resource) (`fb0de9cf-73be-4cbb-9dde-da905ed14bab`)
- S46: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebe95829-70b6-4b25-9a6e-7a1de63947b7/resource) (`ebe95829-70b6-4b25-9a6e-7a1de63947b7`)
- S12: [基于NX的压铸数值模拟集成与溢流槽快速建模系统研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/421789e3-2c95-45d7-9736-c84c5093ed7a/resource) (`421789e3-2c95-45d7-9736-c84c5093ed7a`)
- S15: [模具先进制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ad14312-11e3-4725-a771-374ed42758d9/resource) (`4ad14312-11e3-4725-a771-374ed42758d9`)
- S32: [ugnx110模具设计教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6fc66cc-9e39-45cb-886b-dc0e2c8eaa96/resource) (`a6fc66cc-9e39-45cb-886b-dc0e2c8eaa96`)
- S3: [UG NX 12.0模具设计实例精解](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15058880-9563-4879-9202-e1ad24f5b940/resource) (`15058880-9563-4879-9202-e1ad24f5b940`)
- S40: [UG NX 12.0模具设计完全学习手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d235d8da-6ea5-4c4b-831e-b90084ec4eae/resource) (`d235d8da-6ea5-4c4b-831e-b90084ec4eae`)
- S45: [压铸模具设计及CAD](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eab0a9c9-b5b3-4956-9ba9-88e7d0ba8697/resource) (`eab0a9c9-b5b3-4956-9ba9-88e7d0ba8697`)
- S33: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad0bddf9-b846-4368-9b86-e7d27e308fd0/resource) (`ad0bddf9-b846-4368-9b86-e7d27e308fd0`)
- S29: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ef284ae-95d3-47d0-bcf0-c10573444def/resource) (`9ef284ae-95d3-47d0-bcf0-c10573444def`)
- S8: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3759fcb9-3f61-4101-9453-cf6ede8ee926/resource) (`3759fcb9-3f61-4101-9453-cf6ede8ee926`)
- S10: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3dc6e11a-cbe8-40b9-b2ca-0a9c7dc960f2/resource) (`3dc6e11a-cbe8-40b9-b2ca-0a9c7dc960f2`)
- S22: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a7bc29c-1ce2-4121-9840-fbb40a65ad43/resource) (`6a7bc29c-1ce2-4121-9840-fbb40a65ad43`)
- S18: [压铸模具浇注、溢流、排气系统设计过程流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b7a6281-6a64-465d-871f-5f25ded5e7b9/resource) (`5b7a6281-6a64-465d-871f-5f25ded5e7b9`)
- S25: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79ff98f5-4acc-4aed-95df-568b5157fedb/resource) (`79ff98f5-4acc-4aed-95df-568b5157fedb`)
- S16: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53c5db49-42a1-425d-8efc-b6b618ba2834/resource) (`53c5db49-42a1-425d-8efc-b6b618ba2834`)
- S41: [压铸工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df555f38-8013-4691-bd67-8ef35da03998/resource) (`df555f38-8013-4691-bd67-8ef35da03998`)
- S13: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43ab30f5-c6ab-4556-a92e-10f38e38c62b/resource) (`43ab30f5-c6ab-4556-a92e-10f38e38c62b`)
- S51: [UG NX中文版模具设计基础教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbc5371a-0f34-4a32-90f5-76fb6b96db64/resource) (`fbc5371a-0f34-4a32-90f5-76fb6b96db64`)
- S34: [UG_NX_8.0模具设计教程（典藏版）.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0ab570b-dca2-4785-a553-33347f2bb16e/resource) (`b0ab570b-dca2-4785-a553-33347f2bb16e`)
- S37: [cadcam模具设计与制造实用教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bef6a66f-2e08-459a-89a4-878c71b02fd5/resource) (`bef6a66f-2e08-459a-89a4-878c71b02fd5`)
- S1: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00ba3675-940d-4315-a753-0de69beef2a6/resource) (`00ba3675-940d-4315-a753-0de69beef2a6`)
- S21: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63b3e66c-c55a-4cc4-82e0-b16103a22763/resource) (`63b3e66c-c55a-4cc4-82e0-b16103a22763`)
- S47: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S20: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61c24028-9370-4819-9603-27dffb5c1618/resource) (`61c24028-9370-4819-9603-27dffb5c1618`)
- S39: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf063c89-7f01-49f0-bec3-84d9babc20a4/resource) (`cf063c89-7f01-49f0-bec3-84d9babc20a4`)
- S2: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/112a7bab-6f8f-48c8-8749-731180dc6620/resource) (`112a7bab-6f8f-48c8-8749-731180dc6620`)
- S19: [基于KBE的压铸模具冷却工艺设计系统开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5dabe2bb-cb9c-4c20-ba45-ff01842a1cc9/resource) (`5dabe2bb-cb9c-4c20-ba45-ff01842a1cc9`)
- S11: [基于KBE的压铸模具冷却工艺设计系统开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/419951cc-e471-4562-bff5-b0ef669934a7/resource) (`419951cc-e471-4562-bff5-b0ef669934a7`)
- S31: [注塑模具浇注系统的快速设计系统开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a20e269a-1cbb-4c44-8036-5c55e91470d4/resource) (`a20e269a-1cbb-4c44-8036-5c55e91470d4`)
- S6: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/257fd11c-3240-4bff-b4e2-b435651a2800/resource) (`257fd11c-3240-4bff-b4e2-b435651a2800`)
- S17: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5578076a-f43a-4d15-bbf0-49cd85333975/resource) (`5578076a-f43a-4d15-bbf0-49cd85333975`)
- S35: [UG压铸模具设计入门与提高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7ebee3a-adf1-4cf9-a065-610258e6630c/resource) (`b7ebee3a-adf1-4cf9-a065-610258e6630c`)
- S4: [电源盒壳体压铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d30e347-0f77-42bd-9b78-7fd363dacfe6/resource) (`1d30e347-0f77-42bd-9b78-7fd363dacfe6`)
- S38: [模具设计基础及模具cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8dd952c-ec93-4303-bdbd-013488dc1bbf/resource) (`c8dd952c-ec93-4303-bdbd-013488dc1bbf`)
- S42: [development of a semi automated die casting die design system__d3f173ce13](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e159b5d8-c7e2-4815-b131-2c40944db415/resource) (`e159b5d8-c7e2-4815-b131-2c40944db415`)
- S26: [UG NX 12.0的装配加载选项对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e2a93c4-5733-486c-b420-4d862fc169bd/resource) (`7e2a93c4-5733-486c-b420-4d862fc169bd`)
- S44: [ugnx120数控加工编程应用实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e27a3a6f-1c2b-43c8-ac07-3350da66355c/resource) (`e27a3a6f-1c2b-43c8-ac07-3350da66355c`)
- S23: [图1-1 我国压铸件使用分布情况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/721b624e-9659-430b-8196-68869626369b/resource) (`721b624e-9659-430b-8196-68869626369b`)