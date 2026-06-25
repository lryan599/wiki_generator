---
version: "v1"
generated_at: "2026-06-21T06:11:04+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 35
  source_quality_score: 0.87
  freshness_score: 0.73
  evidence_coverage_score: 1.0
---

## 概述

Pro/ENGINEER（简称Pro/E）是由美国参数技术公司（PTC，Parametric Technology Corporation）开发推出的三维CAD/CAM/CAE一体化参数化软件，开创了三维参数化CAD的先河 [[S28,S26,S5,S19]]。其核心技术特征为基于特征、全参数、全相关、单一数据库架构，采用尺寸驱动的设计修改方式，产品开发过程中某一处数据发生修改，整个设计中的所有相关数据自动同步更新 [[S26,S20]]。

Pro/E在压铸行业被广泛视为压铸模设计的三大主流通用CAD平台之一，凭借其首屈一指的全参数化技术，大量企业以Pro/E为核心完成铸件实体造型、模具结构设计、浇注系统建模与模具装配的全流程三维数字化设计 [[S30,S34,S13]]。

## 发展历程与版本沿革

PTC公司1985年成立于美国波士顿，1988年正式发布首款Pro/ENGINEER 1.0版本，标志着Pro/E产品的诞生 [[S26,S20,S18]]。此后版本经历清晰可分的迭代阶段：

| 年份 | 版本/阶段 | 主要特征 |
|------|----------|---------|
| 1988 | Pro/ENGINEER 1.0 | 首款版本正式发布 [[S26]] |
| 1995 | Pro/ENGINEER 2000i | 新增并行工程支持 [[S26,S11]] |
| — | 2000i² | 迭代版本 |
| 2001 | Pro/ENGINEER 2001 | 改进界面，新增预览功能，增加图模关联 [[S26,S11,S18]] |
| 2003 | Pro/ENGINEER Wildfire（野火版） | 强调操作易用性与设计人员互联性 [[S26]] |
| 2006–2007 | 野火版3.0/4.0 | 持续优化 [[S11]] |
| 2009前后 | 野火版5.0 | 国内广泛应用的成熟版本 [[S28]] |
| 2010 | Creo产品体系发布 | 整合Pro/E参数化技术，原Pro/E重构为Creo Elements/Pro [[S15,S36]] |

2010年10月PTC正式推出Creo产品体系，将原Pro/ENGINEER的参数化技术、CoCreate直接建模技术和ProductView三维可视化技术进行整合。原Pro/ENGINEER产品线首先被重构为Creo Elements/Pro，后续全部迭代并入Creo 1.0、Creo 2.0等Creo全系列产品，Pro/E野火版原有技术完全继承至Creo产品线中 [[S15,S36]]。

## Pro/E在压铸行业的应用历史

Pro/E在国内模具行业的普及始于2000年之前，最早在广东深圳、东莞、广州以及华东沿海压铸产业聚集区率先得到广泛应用。2000-2010年期间，随着野火系列版本的推广，国内压铸行业进入大规模应用Pro/E开展数字化设计的阶段，将其作为压铸模三维造型和结构设计的主流通用CAD平台[[S18,S12]]。

截至2012年的正式出版压铸专业教材中，Pro/E仍被列为国内压铸行业三大主流通用CAD软件（Pro/E、UG、CATIA）之一，凭借极强的参数化设计能力保留大量存量用户，广泛用于压铸模CAD二次开发、压铸产品及模具全三维数字化设计场景[[S13,S30,S8]]。

## 压铸模具设计模块

Pro/E原生内置了专门的模具设计模块，可完整支撑压铸模设计全流程：

- **Pro/CASTING**：Pro/E用于压铸模的专用设计模块，全面提供在Pro/E软件中仿真压铸模设计的过程[[S10,S22]]。
- **Pro/Molddesign**：通用模具设计模块，既可实现产品设计、模具装配、分型面的构造与分型等操作，亦提供投影面积自动计算、拔模检查、分型面质量检查、干涉检查等面向压铸工序的辅助分析功能[[S21,S42]]。
- **EMX（Expert Moldbase Extension）**：模架专家扩展模块，可配合Pro/Molddesign使用，自动生成压铸模所需的标准模架、滑块、斜销等标准件，大幅缩短压铸模设计周期[[S21,S42]]。

此外，Pro/E自带的Pro/TOOLKIT底层二次开发接口及第三方提供的Automation GATEWAY工具，支持开发人员基于VC++或VB等语言定制专用的压铸模参数化设计插件，可实现浇注系统、砂芯等组件的参数化快速建模[[S4]]。

![Pro/E二次开发定制压铸模设计系统主菜单界面，包含系统初始化、原始数据输入、压铸机选择、浇注系统设计、抽芯机构设计等功能入口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81f3c3f7-f319-4096-b27c-519158f741f4/resource)

*图：Pro/E环境中基于二次开发定制的"压铸模设计"下拉菜单界面，涵盖从系统初始化到浇注系统设计、抽芯机构设计等全流程功能入口 [[S23]]*

## Pro/E在压铸模具设计中的应用

### 铸件三维造型

Pro/E支持分别完成压铸件、浇注系统、砂芯的独立三维实体造型，所有独立建模完成后可通过自带的装配模块完成全部组件的预装配，完全适配压铸工艺设计全流程要求[[S24,S40]]。多本公开出版的压铸类专业教材明确将Pro/E列为压铸件测绘与三维实体造型的主流通用工具，该类应用已纳入高职压铸专业项目化教学体系[[S41,S17]]。

《压铸模CADCAECAM》公开实例记录使用Pro/E完成ZAlSi12材质壳形压铸件三维实体造型的完整操作流程，该铸件质量0.48kg、壁厚7mm、腔深34mm，建模时设置100MPa压射比压以适配薄壁气密性压铸件要求[[S29]]。

### 模具设计全流程

基于Pro/E的压铸模设计典型流程如下[[S21,S42,S25]]：

① 独立完成压铸件三维造型，或通过IGES、STEP等交换格式导入其他软件生成的铸件模型；
② 进入Pro/Molddesign模块完成模具装配，将铸件参照模型和成型镶块装配定位；
③ 可分别对X、Y、Z三个坐标轴方向设置不同的压铸材料收缩率，也可针对单个特征或尺寸单独设定缩放系数；
④ 完成主分型面和侧抽芯分型面的创建；
⑤ 利用分型面将模具镶块分割为定模、动模体积块；
⑥ 在分割完成的动定模上进一步完成浇注系统、排溢系统、侧抽芯机构的三维建模，最终完成整套压铸模设计。

![Pro/E建模完成的阀盖压铸件定动模浇注系统三维模型，展示分型面两侧浇注系统的布局形态](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e75ca22e-577b-444c-a31a-3ebd03edb6db/resource)

*图：阀盖压铸件基于Pro/E完成的定模与动模浇注系统三维模型，属于模具造型设计过程中典型的分型面分割后的浇注系统布局输出 [[S38]]*

### 集成应用案例

公开英文文献收录的工业级应用案例显示，基于Pro/ENGINEER搭建压铸CAD/CAE/CAM集成设计平台，配合自研压铸工艺设计专家系统可完成铝合金水泵、镁合金罩壳等复杂压铸件的三维建模、浇注系统设计、溢流槽与冷却通道布局的全流程设计。对接MAGMASOFT开展流动与凝固模拟后优化的方案可有效消除原有设计的卷气、缩松缺陷，显著缩短压铸模开发周期[[S43,S12,S3]]。

Pro/E同样被验证可完成铝合金仪器壳体压铸件的全三维实体建模，建模后保存为IGS格式即可直接导入Mastercam等CAM软件开展后续数控加工路径规划，有效降低铝合金压铸件开发过程的迭代成本[[S35,S9]]。

## 模型交换与数据接口

Pro/E采用单一统一数据库架构，所有设计环节的模型数据完全同源，可直接对接后续压铸CAE充型凝固模拟和CAM数控加工工序，打通压铸设计全流程的数据通道[[S20]]。

主流压铸数值模拟软件均支持Pro/E导出的标准STL格式文件进行直接识别导入。各类软件的数据交换格式支持情况如下：

| 模拟软件 | 支持的Pro/E导出格式 | 说明 |
|---------|-------------------|------|
| AnyCasting | STL | 前处理模块AnyPRE可直接对接Pro/E生成的三维模型开展网格划分与模拟条件设定 [[S37,S31]] |
| MAGMA Soft | STL、IGES、DXF | 与Pro/E之间具有快速、方便的几何数据转换接口 [[S31,S39]] |
| Flow-3D Cast | STL | 通过标准STL格式接口完成模型传递 |

公开文献记录的Pro/E对接AnyCasting标准化操作流程为：在Pro/E中完成坩埚、料筒等部件三维造型，将模型以STL格式导出，直接导入AnyCasting前处理模块AnyPRE，后续依次完成网格划分、工艺参数设置、数值求解与后处理结果分析，该流程已在半固态浆料制备数值模拟项目中得到实际验证[[S32]]。

## 别名与称呼

在压铸领域公开出版的专业文献中，"Pro/E三维造型平台""Pro-E软件""Pro/E三维绘图软件""Pro/E建模软件"均属于用于明确界定该三维CAD工具属性的通用行业称呼，该类称呼广泛应用于压铸行业教材与设计手册中，用于描述Pro/E在压铸模具设计、三维造型、参数化建模等环节中的角色[[S41]]。其中"Pro/E"为最通用的简称形式，与全称"Pro/ENGINEER"在压铸行业教材与手册中均可互换使用[[S13,S28]]。

## Sources
- S28: [Pro_ENGINEER中文野火版5.0模具设计实例精解（修订版）.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b49cbb24-a052-4008-b387-61ae71ce3898/resource) (`b49cbb24-a052-4008-b387-61ae71ce3898`)
- S26: [大型复杂镁合金压铸件的应力分析数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94bf548f-0811-4d9f-89db-fe149e6086ae/resource) (`94bf548f-0811-4d9f-89db-fe149e6086ae`)
- S5: [机械加工工艺手册第二版第一卷工艺基础卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2fe9e40c-2b9f-4ce3-8240-e88506ed2d2a/resource) (`2fe9e40c-2b9f-4ce3-8240-e88506ed2d2a`)
- S19: [机械加工工艺手册第1卷工艺基础卷第二版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e5a1657-2298-45ef-86d1-bd0806808455/resource) (`6e5a1657-2298-45ef-86d1-bd0806808455`)
- S20: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7661bfda-0d96-4119-9a57-fa3e7c49e945/resource) (`7661bfda-0d96-4119-9a57-fa3e7c49e945`)
- S30: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c58e5abb-67b1-453f-bc38-50228e0b05d6/resource) (`c58e5abb-67b1-453f-bc38-50228e0b05d6`)
- S34: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da72e20e-e7d7-4261-922f-97370022afa1/resource) (`da72e20e-e7d7-4261-922f-97370022afa1`)
- S13: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5816ebc8-274b-405b-a60d-fbb789e5119b/resource) (`5816ebc8-274b-405b-a60d-fbb789e5119b`)
- S18: [proengineer2001模具设计与制造实用教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6682af01-9ef3-4482-9e92-4cc6ae9de387/resource) (`6682af01-9ef3-4482-9e92-4cc6ae9de387`)
- S11: [proengineer2001模具设计与制造实用教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4caef722-7049-4c18-9112-e693fbeb5b6e/resource) (`4caef722-7049-4c18-9112-e693fbeb5b6e`)
- S15: [Creo_3.0模具设计完全自学宝典.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6042a3b8-45a9-43bc-8749-f9bd224b5139/resource) (`6042a3b8-45a9-43bc-8749-f9bd224b5139`)
- S36: [Creo_2.0模具设计教程.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2de3b27-49f6-498a-9e45-5867cfed599b/resource) (`e2de3b27-49f6-498a-9e45-5867cfed599b`)
- S12: [application of an integrated cad cae cam system for die casting dies__96a43cb0a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d4649ff-c3d2-4a72-94b2-09dafe778a34/resource) (`4d4649ff-c3d2-4a72-94b2-09dafe778a34`)
- S8: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43db26df-9171-48e7-b720-a11b9125de3e/resource) (`43db26df-9171-48e7-b720-a11b9125de3e`)
- S10: [proengineerwildfire50模具设计与制造实用教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/477542bc-cae1-474b-ac40-0b647cced6c6/resource) (`477542bc-cae1-474b-ac40-0b647cced6c6`)
- S22: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80313616-c72c-4ea2-bd04-77d7891e4b39/resource) (`80313616-c72c-4ea2-bd04-77d7891e4b39`)
- S21: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79110add-397d-46c9-9cf2-11a7f80933e2/resource) (`79110add-397d-46c9-9cf2-11a7f80933e2`)
- S42: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0e0bc0d-bda5-40a1-a0ea-966adf110c2c/resource) (`f0e0bc0d-bda5-40a1-a0ea-966adf110c2c`)
- S4: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ada7625-c7b3-40ef-a760-98aaec16cb71/resource) (`2ada7625-c7b3-40ef-a760-98aaec16cb71`)
- S23: [压铸模CAD系统的“压铸模设计”下拉菜单界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81f3c3f7-f319-4096-b27c-519158f741f4/resource) (`81f3c3f7-f319-4096-b27c-519158f741f4`)
- S24: [压铸成型工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84904864-a44c-4c71-809d-72c0b70d57ef/resource) (`84904864-a44c-4c71-809d-72c0b70d57ef`)
- S40: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebdc9352-79ef-42ef-82c0-ecd176357374/resource) (`ebdc9352-79ef-42ef-82c0-ecd176357374`)
- S41: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0a32c24-eed3-4024-ae63-148992c7bdcf/resource) (`f0a32c24-eed3-4024-ae63-148992c7bdcf`)
- S17: [压铸模具设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64d92f75-6818-4bc9-83e8-bcfb714d533e/resource) (`64d92f75-6818-4bc9-83e8-bcfb714d533e`)
- S29: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf758a23-2772-478a-bb35-28f96040bc8f/resource) (`bf758a23-2772-478a-bb35-28f96040bc8f`)
- S25: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/877cb9ad-1978-4b75-8d39-0111149a9cfd/resource) (`877cb9ad-1978-4b75-8d39-0111149a9cfd`)
- S38: [阀盖压铸件定模与动模浇注系统三维模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e75ca22e-577b-444c-a31a-3ebd03edb6db/resource) (`e75ca22e-577b-444c-a31a-3ebd03edb6db`)
- S43: [application of an integrated cad cae cam system for die casting dies__96a43cb0a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f65eaa79-9e10-436e-ab48-72ca54b10371/resource) (`f65eaa79-9e10-436e-ab48-72ca54b10371`)
- S3: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848/resource) (`1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848`)
- S35: [die casting mold design for aluminum alloy shell of instrument__cbd6c85af0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1f74f3d-e1c4-4299-9d09-1cac080cc652/resource) (`e1f74f3d-e1c4-4299-9d09-1cac080cc652`)
- S9: [die casting mold design for aluminum alloy shell of instrument__cbd6c85af0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43faaee5-1005-4d4b-a827-c8dc4b6dff6a/resource) (`43faaee5-1005-4d4b-a827-c8dc4b6dff6a`)
- S37: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S31: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf063c89-7f01-49f0-bec3-84d9babc20a4/resource) (`cf063c89-7f01-49f0-bec3-84d9babc20a4`)
- S39: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e83871fa-17b8-4d29-ae73-f85451844526/resource) (`e83871fa-17b8-4d29-ae73-f85451844526`)
- S32: [倾转-振动法制备半固态浆料及微观组织的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d56943ee-dfff-4763-beb4-2af59d79efd6/resource) (`d56943ee-dfff-4763-beb4-2af59d79efd6`)