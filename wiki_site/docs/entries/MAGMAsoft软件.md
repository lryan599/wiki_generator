---
version: "v1"
generated_at: "2026-06-18T11:43:48+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 32
  source_quality_score: 0.86
  freshness_score: 0.78
  evidence_coverage_score: 1.0
---

## 概述

MAGMASOFT（正式注册商标标识为 MAGMASOFT®）是由德国 MAGMA Gießereitechnologie GmbH（常简称为 MAGMA GmbH）开发的铸造过程模拟软件[[S24,S27,S29]]。公司总部位于德国亚琛（Aachen），并在新加坡、美国伊利诺伊州阿灵顿高地和中国苏州等地设有区域性子公司[[S23,S10,S29]]。该软件于1988年在德国正式发行，并于1989年在德国第7届国际铸造博览会上公开展出，是20世纪80年代末问世的全球首款商品化铸造CAE软件[[S24,S27]]。

MAGMASOFT 采用全有限差分法（FDM）技术路线，支持充型流动、传热凝固、应力演变及微观组织等全流程仿真，广泛应用于高压压铸、低压铸造、重力铸造、砂型铸造、离心铸造及挤压铸造等各类铸造工艺[[S24,S27,S31]]。

**已知拼写变体**：MAGMASOFT、MAGMAsoft、MAGMA-soft、MAGMA Soft、MAGMA SOFT，中文官方译名为"迈格码"[[S24,S28,S29]]。该软件类术语需与地质领域指代岩浆的通用术语 MAGMA 明确区分[[S38]]。

## 历史与版本

MAGMASOFT 由德国亚琛大学 Sahm 教授团队主持开发，最初采用 FDM/FEM 结合的技术路线，后改为全 FDM 技术[[S27]]。版本更迭里程碑如下[[S24]]：

| 时间 | 版本/事件 | 核心内容 |
|------|----------|---------|
| 1988年 | 首次发行 | 全球首款商品化铸造CAE软件 |
| 2010年 | 5版本 | 从4版本跨代升级到5版本 |
| 2011年 | MAGMA5.1 | 面向有色金属铸造场景优化 |
| 2012年 | MAGMA5.2 | 集成制芯生产工艺优化功能与3D全场景铸造模拟技术 |
| 2015年 | MAGMA5.5 | 正式发布 |

MAGMA5.3 版本在工业界有公开落地应用记录，用于铝合金低压铸造气缸盖的充型、凝固过程缺陷仿真分析[[S12]]。公开可查的权威来源中未明确记载 MAGMASOFT 5.4 及 MAGMASOFT 6.0 的正式发布时间和核心更新里程碑。

## 软件架构与模块

MAGMASOFT 采用模块化架构，由标准模块和专用模块构成[[S31,S28]]。

### 标准模块

| 模块名称 | 功能描述 |
|---------|---------|
| 项目管理模块（Project Management） | 创建和管理项目及多方案版本，所有模块共享接口，数据可在不同版本间互传[[S28]] |
| 前处理模块（Pre-processor） | 导入或构建几何模型，支持STL、IGES等格式及多款CAD软件直接接口，可构建冷却水道、浇道、激冷块等，自动网格划分[[S28,S31]] |
| 流体流动分析模块（MAGMA fill） | 基于流体力学控制方程求解充型过程，输出料流路径、速度场、压力场、温度分布[[S28]] |
| 热传及凝固分析模块（MAGMA solid） | 基于传热学模型计算凝固过程，输出凝固时间、温度梯度、冷却速率、热负荷[[S28,S31]] |
| 制程仿真分析模块（MAGMA batch） | 仿真重力铸造和压铸的多周期循环生产过程[[S28,S7]] |
| 后处理显示模块（Post-processor） | 三维视图显示模拟结果，支持立体切片、透视功能，可动态显示充型、凝固及缺陷形成过程[[S28,S7]] |
| 热物理材料数据库（Thermophysical Database） | 提供多种合金及辅料的热物性数据，支持用户自定义添加新合金材料[[S28,S7]] |

### 专用模块

专用模块面向具体铸造工艺和需求场景设计[[S24,S31]]：

- **MAGMA hpdc**：高压铸造专业模块
- **MAGMA lpdc**：低压铸造专业模块
- **MAGMA iron**：铸铁专业模块，可预测石墨析出形态和微观组织分布
- **MAGMA steel**：铸钢专业模块，可计算宏观偏析和热处理后局部微观结构
- **MAGMA stress**：应力应变分析模块，全三维计算热弹性/热塑性应力应变
- **MAGMA tilt**：倾转浇注铸造模块
- **MAGMA roll-over**：浇注翻转铸造模块
- **MAGMA thixo**：半凝固射出专业模块
- **MAGMA DISAMATIC**：迪砂线重力铸造模块
- **MAGMA INVESTMENT CASTING**：精密铸造专业模块
- **MAGMA C+M**：射砂制芯专业模块

关于 MAGMAfrontier 和 MAGMAlink 两款辅助工具，当前公开可引用的文献资料中未收录其详细功能说明[[S20,S4]]。

MAGMASOFT 项目管理模块界面展示如下：

![MAGMASOFT项目管理模块操作界面，支持多项目多版本并行管理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8cbd668-400f-4b90-bd42-ad2b6465f000/resource)

该界面包含创建新项目、版本管理、删除结果等功能选项，同时展示已有项目及对应版本列表[[S41]]。

## 支持铸造工艺范围

MAGMASOFT 支持覆盖全品类铸造工艺的模拟分析[[S31]]：

| 分类维度 | 支持范围 |
|---------|---------|
| 按材质 | 铸铁、铸钢、铸铝、铸镁，均设专用模块 |
| 按成形工艺 | 普通砂型铸造、高压铸造、迪砂线铸造、离心铸造、连续铸造、消失模铸造、低压铸造、差压铸造、半固态触变铸造、挤压铸造、精密熔模铸造 |
| 按物理场 | 温度场、流动场、应力场、显微组织、机械性能，可模拟热处理过程 |

## 高压压铸专用功能

高压压铸专用模块 MAGMA hpdc 可支持多周期连续生产仿真，导入不同型号压铸机参数，模拟多轮压铸循环后型腔与模具的稳态温度分布[[S24,S28]]。该模块可预测卷气、冷隔、缩孔、热变形等典型压铸缺陷，辅助优化浇注系统、排气通道、冷却水路的布局设计[[S28,S8,S5]]。

内置数据库预设市面主流型号压铸机参数、迪砂线造型机参数、商用过滤片与保温冒口产品的标准参数[[S31]]。

**压铸场景常用输入参数**包括[[S31,S19,S9]]：

| 参数 | 说明 |
|-----|------|
| 压铸机锁模力 | 根据铸件投影面积计算选定 |
| 压射速度 | 含低速段和高速段速度设置 |
| 内浇口截面积 | 影响充型速度与流态 |
| 浇注温度 | 金属液浇注时的温度 |
| 模具预热温度 | 模具初始温度条件 |
| 保压压力 | 凝固过程的补缩压力 |
| 目标充型时间 | 设计充型完成时间 |
| 边界条件 | 金属-模具界面换热系数、冷却水对流换热系数等 |

## 缺陷预测能力

MAGMASOFT 各物理模块对应的缺陷预测能力如下[[S28,S31,S8,S3,S39]]：

| 物理模块 | 预测缺陷/输出 |
|---------|-------------|
| MAGMA fill（充型流动） | 卷渣、卷气、金属流对模具的冲蚀风险位置、冷裂纹可能发生位置 |
| MAGMA solid（凝固） | 宏观及微观缩孔、缩松分布 |
| MAGMA stress（应力） | 热裂、残余变形、残余应力 |
| 铸铁专用模块 | 组织疏松、白口倾向，可预测石墨形态、硬度和力学性能 |
| 铸钢专用模块 | 宏观偏析 |

以下为 MAGMAsoft 输出的典型缺陷预测可视化结果：该图以镁合金压铸件充型仿真为例，高亮标记的最晚填充位置可直接用于识别压铸过程中气体滞留、卷气缺陷的潜在生成区域[[S2]]。

![MAGMAsoft输出的AZ91HP镁合金铸件最后填充区域分布，用于预判气体孔隙潜在位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/037cfcb0-ef45-4696-ad40-40fccccdef72/resource)

## 与同类软件的比较

### 主流软件核心参数对比

下表为国内外主流铸造商业模拟软件的参数对比，MAGMAsoft 条目显示了其技术特性[[S25,S26]]：

| 特性 | MAGMA Soft |
|-----|-----------|
| 国别 | 德国 |
| 算法 | FDM/FEM 组合（后改为全FDM） |
| 最大处理网格数 | 无限制 |
| 支持物理场 | 温度场(T)、流场(F)、应力场(S) |
| 适用铸造工艺 | 覆盖所有铸造工艺类型 |
| 分析内容 | 流动与传热、应力、微观组织分析 |

### 软件特性差异

MAGMASOFT 与其他主流铸造模拟软件的核心特性差异如下[[S36,S27,S32,S22]]：

| 软件 | 核心特点 |
|-----|---------|
| **MAGMASOFT** | 全FDM算法，常规压铸充型凝固计算效率高，网格自动划分自动化程度好，各类铸造工艺专用模块覆盖度广 |
| **ProCAST** | 基于有限元（FEM）架构，多物理场耦合能力更强，复杂薄壁件应力与辐射传热计算精度更优 |
| **FLOW-3D** | 采用专用流体算法，自由表面流动模拟精度最高，计算资源需求较大 |
| **AnyCasting** | 韩国产品，性价比更高，在中小铸造企业覆盖度较好，高端工业场景专用功能少于MAGMASOFT |

## 行业地位与应用

MAGMASOFT 是美国铸造协会（AFS）1997年工艺过程设计和仿真委员会官方收录的全球主流铸造仿真软件之一[[S15,S16]]。软件发布后长期处于同类模拟软件领先水平，是铸造行业公认的工艺优化核心工具[[S24,S27,S13]]。

### 典型应用案例

**汽车结构件**：

- 德国大众汽车采用 MAGMASOFT 对镁合金变速箱体进行压铸工艺仿真，模拟充型过程、凝固特性与模具热平衡状态，优化浇注系统后，该镁合金变速箱体已成功量产并应用于 Passat、奥迪 A4、奥迪 A6 等主流乘用车型[[S35]]。
- 在国六排放发动机缸体铸件开发中，使用 MAGMASOFT 模拟不同工艺方案的凝固过程液相比分布与缩松位置，通过增设冷铁优化工艺，最终铸件的缩孔缺陷率降至1%以下[[S14]]。

**铝合金轮毂低压铸造**：

- 使用 MAGMASOFT 模拟凝固顺序与缩孔位置，结合热电偶实测温度数据校验模拟精度后，改进冷却系统与保温材料设置，可实现顺序凝固补缩通道顺畅，完全消除铸件内部缩孔缺陷[[S11]]。

**通讯壳体**：

- 利用 MAGMASOFT 对铝合金压铸下箱体进行充型过程模拟，分析缺陷产生的根本原因并优化浇注系统，铸件外观及内部质量有较大提升，缩短开发周期[[S10]]。

### 在压铸质量全流程控制中的作用

MAGMASOFT 在压铸质量全流程控制中的典型应用包括[[S28,S35,S31,S21]]：

1. 优化浇注系统与溢流槽结构
2. 预测金属液充型过程的卷气/夹渣位置
3. 定量判定宏观及微观缩孔缩松分布
4. 定位冷裂纹与热裂纹潜在发生区域
5. 计算压铸模具热平衡状态
6. 校核压射工艺参数的合理性
7. 支持虚拟迭代验证不同工艺方案的效果

## Sources
- S24: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a62dd6c-7a87-47ef-888c-1374e8938011/resource) (`7a62dd6c-7a87-47ef-888c-1374e8938011`)
- S27: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a49544a0-99b5-4cc9-8647-3276eb49bd2f/resource) (`a49544a0-99b5-4cc9-8647-3276eb49bd2f`)
- S29: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4ca88b2-a303-494b-8c1e-939cc87eda09/resource) (`b4ca88b2-a303-494b-8c1e-939cc87eda09`)
- S23: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6389d6d3-0f08-42f8-b93e-6134d7442364/resource) (`6389d6d3-0f08-42f8-b93e-6134d7442364`)
- S10: [铝合金压铸下箱体的浇注系统设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f4ed40d-f1bd-449b-a754-74ceb8b03b6b/resource) (`2f4ed40d-f1bd-449b-a754-74ceb8b03b6b`)
- S31: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba8f3f8b-82a2-4d58-a370-b9a4a6279fe6/resource) (`ba8f3f8b-82a2-4d58-a370-b9a4a6279fe6`)
- S28: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b17a4f24-0a05-43d8-9c28-390e3da5432c/resource) (`b17a4f24-0a05-43d8-9c28-390e3da5432c`)
- S38: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eded8b51-375e-4d60-ba1a-0f901a65a88c/resource) (`eded8b51-375e-4d60-ba1a-0f901a65a88c`)
- S12: [某发动机气缸盖油泵安装座泄漏缺陷问题分析及解决](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3469a110-5d48-4070-88a7-b7f19f940782/resource) (`3469a110-5d48-4070-88a7-b7f19f940782`)
- S7: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20c5b741-703b-4565-bfac-711142bfd43f/resource) (`20c5b741-703b-4565-bfac-711142bfd43f`)
- S20: [corrosion and corrosion prevention of low density metals and alloys proceedings of the international symposium__f64e2...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5bf8b1f4-493d-4ece-9574-80990764c95a/resource) (`5bf8b1f4-493d-4ece-9574-80990764c95a`)
- S4: [building cross platform apps using titanium alloy and appcelerator cloud services__3511b43db0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c91e233-211c-422b-a73d-56f5cc098f8b/resource) (`0c91e233-211c-422b-a73d-56f5cc098f8b`)
- S41: [MAGMA软件项目管理模块界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8cbd668-400f-4b90-bd42-ad2b6465f000/resource) (`f8cbd668-400f-4b90-bd42-ad2b6465f000`)
- S8: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20f2db5c-2a6f-49c1-ae1d-2e9451819b4d/resource) (`20f2db5c-2a6f-49c1-ae1d-2e9451819b4d`)
- S5: [压铸模拟软件MAGMAhpde的参数设置界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ed3c7cf-673b-4b14-8224-9b367385678d/resource) (`0ed3c7cf-673b-4b14-8224-9b367385678d`)
- S19: [表1 模拟分析工艺参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59e747c6-c680-411e-b2d0-82d2625cd5fe/resource) (`59e747c6-c680-411e-b2d0-82d2625cd5fe`)
- S9: [镁合金汽车控制臂铸锻复合成形工艺的研究开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2be64f5d-f564-4218-ba6b-92a231c654d2/resource) (`2be64f5d-f564-4218-ba6b-92a231c654d2`)
- S3: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b5d9a2f-5f00-4c24-bd19-d6a230eedea0/resource) (`0b5d9a2f-5f00-4c24-bd19-d6a230eedea0`)
- S39: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0947f0f-927f-47ec-aa9e-4866d8b0da9c/resource) (`f0947f0f-927f-47ec-aa9e-4866d8b0da9c`)
- S2: [压铸数值模拟的铸件最后填充区域图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/037cfcb0-ef45-4696-ad40-40fccccdef72/resource) (`037cfcb0-ef45-4696-ad40-40fccccdef72`)
- S25: [表1 国内外广泛使用的商业模拟软件一览表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bf456be-ed58-4479-8422-12ae3f8502a0/resource) (`7bf456be-ed58-4479-8422-12ae3f8502a0`)
- S26: [表1.1 国内外主流铸造模拟软件[65]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7db5a11c-f301-4cd6-86f1-1813d7ea09ac/resource) (`7db5a11c-f301-4cd6-86f1-1813d7ea09ac`)
- S36: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S32: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbcee639-0ac9-4d7f-8309-92a4c5d40853/resource) (`cbcee639-0ac9-4d7f-8309-92a4c5d40853`)
- S22: [表2.1 主流铸造数值模拟软件对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62ad51a3-c595-452b-8c7d-bff26d5f2a5f/resource) (`62ad51a3-c595-452b-8c7d-bff26d5f2a5f`)
- S15: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d3e3075-f2cb-4bc0-897d-19ffd7943ac4/resource) (`3d3e3075-f2cb-4bc0-897d-19ffd7943ac4`)
- S16: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fa4a401-8a01-4d24-9e77-ee0ea61dda40/resource) (`3fa4a401-8a01-4d24-9e77-ee0ea61dda40`)
- S13: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35c0bacf-3979-468b-8791-843f11ab87b7/resource) (`35c0bacf-3979-468b-8791-843f11ab87b7`)
- S35: [不同型腔真空度对铸件组织和性能的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df3a4ef1-a9ed-4a30-8551-cc6a351b293f/resource) (`df3a4ef1-a9ed-4a30-8551-cc6a351b293f`)
- S14: [CAE在国六发动机缸体缸盖铸件中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/361a7604-600f-47f7-84eb-298e55f2de24/resource) (`361a7604-600f-47f7-84eb-298e55f2de24`)
- S11: [铝合金发动机缸体低压铸造缺陷控制的工艺及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/320ccac5-cf9e-4434-bafe-96c05a18a266/resource) (`320ccac5-cf9e-4434-bafe-96c05a18a266`)
- S21: [a numerical and an experimental investigation of a high pressure die cas__76acfbd839](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/612ff9ff-1a60-46fb-92ed-ebd4be5718dd/resource) (`612ff9ff-1a60-46fb-92ed-ebd4be5718dd`)