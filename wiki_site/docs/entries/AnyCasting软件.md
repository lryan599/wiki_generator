---
version: "v1"
generated_at: "2026-06-18T11:40:19+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 21
  source_quality_score: 0.83
  freshness_score: 0.91
  evidence_coverage_score: 1.0
---

## 概述

AnyCasting 是由韩国 AnyCasting Co., Ltd. 自主研发的铸造工艺专属 CAE 仿真系统，公司总部位于韩国首尔[[S20,S11,S23,S27]]。该软件基于 Windows 操作平台，采用模块化设计，以铸件充型过程和凝固过程的数值模拟为核心，可支持砂型铸造、高压压铸、低压铸造、熔模铸造等几乎所有常见铸造工艺类型的全流程仿真分析，能够精准预测缩孔缩松、冷隔、气孔、夹渣、变形等常见铸造缺陷[[S11,S27,S8]]。

软件核心求解器于 1985 年研发完成，1990 年正式推广为商业化软件，目前广泛使用的成熟稳定版本为 AnyCasting 6.0[[S11,S29]]。

## 核心功能与模块

AnyCasting 程序结构化程度高，基本程序模块包括[[S11,S12,S27,S1]]：

| 模块名称 | 程序名 | 主要功能 |
|----------|--------|----------|
| 前处理模块 | **anyPRE** | STL 格式三维模型导入、可变网格生成、铸造工艺选择、材料分配、边界条件及参数设置，生成求解器可识别的计算文件 |
| 自动网格工具 | **AutoMesh** | 智能化自动识别铸件壁厚并生成可变网格，保证壁厚方向至少 3 排网格 |
| 网格编辑器 | **anyMESH** | 在不修改原始几何模型的前提下修复和调整网格文件 |
| 材料数据库 | **anyDBASE** | 集成国际主流标准材料全温度区间热物性参数，支持用户自定义材料属性及化学成分自动计算热物性参数 |
| 求解器 | **anySOLVER** | 充型流动、温度场传导、凝固过程的多物理场耦合计算 |
| 后处理模块 | **anyPOST** | 读取计算结果，以图像、动画、数据曲线等形式可视化输出充型与凝固全过程数据 |
| 应力分析模块 | **anyTX** | 热应力/变形分析，预测铸件变形与热裂倾向 |
| 批量处理 | **BatchRunner** | 批量处理模拟任务 |

### 充型与凝固分析

充型分析可高精度复现金属液流动轨迹，预测卷气、冷隔、冲砂等流动相关缺陷。凝固分析集成 Niyama 判据（G/R¹/²）、补缩效率（G/V）和残余熔体模数等模型，精准预测缩孔缩松缺陷[[S11,S12,S1]]。

### 微观组织与力学性能模拟

微观组织模拟模块通过 PDAS/SDAS 二次枝晶臂间距粗化模型和 MT-SK（Macro Transport & Solidification Kinetics）模型预测晶粒尺寸与结核密度，并可基于大量实验经验公式输出硬度、抗拉强度 UTS、屈服强度 YS、延展性等力学性能预测结果[[S12]]。

## 关键参数与操作条件

### 界面传热系数

AnyCasting 支持设置不同实体间的界面传热系数。典型工程应用中空气与固体的界面传热系数推荐取值为 **41.87 W/m²·K**，已在铝合金流变挤压铸造模拟、大型薄壁球墨铸铁无冒口砂型铸造等多个公开案例中被验证有效，作为空冷工况下铸件、铸型与外界空气之间的换热边界条件使用[[S35,S18]]。

| 界面类型 | 典型传热系数 (W/m²·K) |
|----------|------------------------|
| 空气与铸件/模具 | 41.87 |
| 金属模具与铝液 | ≥2700 |
| 铸件与模具（压铸） | 约 1000~2093.5 |

### 材料数据库

anyDBASE 材料数据库覆盖全品类铸造相关材料，包括铁合金（铸铁、铸钢）、非铁合金（铝、镁、铜、锌）、非金属材料（砂、陶瓷）、功能型材料（绝缘材料、保温材料、冷却管路介质），集成中国 GB、韩国 KS、日本 JIS、美国 ASTM/AISI/AA/UNS/SAE、德国 DIN、ISO 等国际主流标准的全温度区间热物性参数[[S12,S11,S1]]。用户可自定义导入自研或非标材料属性，也可通过输入材料化学成分自动计算对应热物性参数[[S12]]。

### 网格划分

采用有限差分法，支持均匀网格与非均匀可变网格两种模式。内置 AutoMesh 智能化网格生成工具，用户定义最大、最小尺寸后自动识别铸件壁厚，按"壁厚方向至少设置 3 排网格"原则自动生成网格，可在数秒至十几秒内完成千万级网格剖分。同时配套 anyMESH 网格编辑器，可直接修复网格文件而无需修改原始几何模型[[S12,S11,S1,S6]]。

### 边界条件设置

AnyCasting 支持导航式流程引导用户完成各类边界条件设置。压铸模拟场景的常规设置顺序为：网格划分 → 铸造工艺类别选择 → 材料分配 → 初始边界条件设置 → 热传导模型设置 → 浇口条件设置 → 流体流动模型设置（k-ε 双方程紊流模型）→ 压室模型设置[[S27,S1,S12]]。

## 局限性与已知问题

### 憋气类缩松预测能力不足

AnyCasting 内置缩松预测算法基于 Niyama 判据（残余熔体模数模型），该判据存在固有局限：其缩松判定的临界值难以统一确定，对非纯凝固收缩诱发的缩松缺陷预测精度不足[[S3]]。

公开学术研究证实，AnyCasting 对憋气类缩松缺陷的预测能力存在明显不足。此类缺陷由型腔内未及时排出的残留空气或砂芯发气形成的滞气区域诱发。铝液与空气的传热系数仅为 41.87 W/m²·K，而金属模具与铝液之间的传热系数可达 2700 W/m²·K 以上，二者相差达 **64 倍**。滞气形成的隐性热节导致的缩松在实际生产中十分普遍，但受参数细节设置偏差和 3D 模型细节简化的影响，AnyCasting 难以准确复现这类缺陷的分布位置与尺寸[[S16,S5]]。

![铝合金金属型低压铸造憋气类缩松缺陷铸件探伤图（型腔排气不良诱发）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f124808a-a8fe-446e-824a-7c9e0720adef/resource)

![憋气类缩松缺陷铸件实物，红框标注缩松所在区域（外表面无明显异常，仅隐蔽内部区域分布）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0c8d704-9410-48ec-9c62-57fff8d86e15/resource)

## 应用领域与典型案例

AnyCasting 可支持几乎所有主流铸造工艺的全流程模拟[[S27,S12,S11]]：

- 砂型铸造
- 熔模铸造
- 金属模铸造
- 重力倾斜铸造
- 高压铸造
- 低压铸造
- 挤压铸造
- 真空铸造
- 离心铸造
- 连续铸造

在汽车行业已有大量公开应用案例，包括：ADC12 铝合金转向器伺服壳体压铸工艺优化、汽车蜗壳压铸件工艺优化、铝合金汽车离合器壳体真空压铸仿真、铝合金变速箱壳体高压铸造工艺优化等[[S7,S4,S14,S33,S13]]。

## 别名说明

**AnyPRE** 并非 AnyCasting 的历史名称或别名，而是 AnyCasting 软件内置的独立专属前处理模块，为软件五大核心运作模块之一[[S27,S28,S12,S15]]。其他形式如"Any Casting模拟软件""CAE软件AnyCasting""Anycasting仿真系统"均为 AnyCasting 的不同称谓或书写变体。

## 版本与历史

| 时间节点 | 事件 |
|----------|------|
| 1985 年 | 核心求解器研发完成 |
| 1990 年 | 正式推广为商业化软件 |
| 当前 | 成熟稳定版本 AnyCasting 6.0 广泛使用 |

## 与其他铸造模拟软件的比较

| 对比维度 | AnyCasting（韩国） | MAGMA Soft（德国） | Flow-3D Cast（美国） | ProCAST（美国） |
|----------|-------------------|--------------------|----------------------|-----------------|
| 数值方法 | 有限差分法 | 有限差分法/有限体积法 | 有限体积法 | 有限元法 |
| 铸造工艺覆盖 | 几乎所有主流工艺，压铸定向优化 | 模块化设计，不同工艺对应专用模块 | 流体模拟准确度高 | 支持多种特殊工艺 |
| 薄壁件分析 | 网格划分效率高 | 薄壁产品分析能力较强 | — | — |
| 计算速度 | 超群 | 较快 | 相对较慢 | — |
| 多物理场耦合 | 流动-传热-应力 | 流动-传热-应力-微观组织 | 流动-传热 | 热-流动-应力完全耦合 |
| 前处理难度 | 操作界面直观，学习门槛低 | 中等 | 操作简单 | 前处理网格划分能力较弱，上手门槛高 |
| 分析精度 | 较高 | 高 | 高 | 高 |

## 用户界面与可视化

AnyCasting 图形交互界面基于 Windows 平台设计，窗口布局归类清晰，配有完整菜单栏与工具栏，支持优先顺序导航式参数设置流程[[S11,S1,S27]]。可直接兼容 IDEAS、CATIA、Pro/E、UG、AutoCAD 等主流三维 CAD 软件导出的 STL 格式模型文件。基于 OpenGL 技术实现全 3D 动态剖面移动功能，支持任意截面的模型、网格、边界条件查看，内置直接测量功能可精准量取实体长度、体积等参数，还支持调整实体透明属性以便观察内部结构[[S11,S1,S27]]。

后处理可视化方面，anyPOST 可以图像、动画、数据曲线等形式输出充型过程的温度、压力、速度、流动状态云图，以及凝固过程的凝固顺序、温度梯度、固相分数、孤立液相区分布等结果，同时支持自动输出过程截图与模拟动画，内置铸件质量评估体系可自动生成标准化分析报告[[S11,S1]]。

---

![AnyCasting软件主操作界面（含菜单栏、三维模型视图区域、属性参数窗口）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/761ef891-2b0c-40e4-a251-5cb99c8e9a1e/resource)

![AnyCasting软件全流程操作工作流程图（STL导入→网格划分→数据处理→求解→后处理→工艺判定）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f65b6752-6e69-41a0-88e4-4ea12204b4a8/resource)

## Sources
- S20: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf/resource) (`a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf`)
- S11: [空压机用铝合金阀盖件的低压铸造工艺开发及模拟优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a7bc564-55c1-4b4d-baa0-8519a629aeb4/resource) (`3a7bc564-55c1-4b4d-baa0-8519a629aeb4`)
- S23: [computer aided engineering cae simulation for the design optimization of__3c0fc6c5de](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc4fba8a-cba7-44fc-8ac0-09fe6f6e53b3/resource) (`bc4fba8a-cba7-44fc-8ac0-09fe6f6e53b3`)
- S27: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S8: [大重量高精度复杂钛合金机匣整体铸造技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32243198-f474-446d-a8bb-09d29c23d0b6/resource) (`32243198-f474-446d-a8bb-09d29c23d0b6`)
- S29: [考虑螺旋离心泵水力性能及铸造成型的多目标优化设计研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5f2dd12-3d4d-49b9-a768-892470b774cf/resource) (`e5f2dd12-3d4d-49b9-a768-892470b774cf`)
- S12: [空压机用铝合金阀盖件的低压铸造工艺开发及模拟优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42f42f00-1d71-413e-8b72-3ebc589ef205/resource) (`42f42f00-1d71-413e-8b72-3ebc589ef205`)
- S1: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06e30961-bad3-4882-a77b-4fb272a32c2c/resource) (`06e30961-bad3-4882-a77b-4fb272a32c2c`)
- S35: [铝合金流变挤压铸造成形技术基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/feb30776-4516-4c56-ac49-6c8d507e88b9/resource) (`feb30776-4516-4c56-ac49-6c8d507e88b9`)
- S18: [基于AnyCasting大型薄壁鞍座铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c3447a9-76cc-45b8-b3c9-b0a20fac24d0/resource) (`6c3447a9-76cc-45b8-b3c9-b0a20fac24d0`)
- S6: [考虑螺旋离心泵水力性能及铸造成型的多目标优化设计研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1dbd8cc8-7691-4fc5-9e94-6f254e161d41/resource) (`1dbd8cc8-7691-4fc5-9e94-6f254e161d41`)
- S3: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0afe2103-07d3-4fe3-ba9b-ae86ad8e95c1/resource) (`0afe2103-07d3-4fe3-ba9b-ae86ad8e95c1`)
- S16: [浅谈憋气引起的缩松问题整改措施](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6309bcc7-920b-48bf-968a-a4ae6eeafb5d/resource) (`6309bcc7-920b-48bf-968a-a4ae6eeafb5d`)
- S5: [浅谈憋气引起的缩松问题整改措施](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18af59f1-b352-4518-8d31-166df210b821/resource) (`18af59f1-b352-4518-8d31-166df210b821`)
- S7: [基于Anycasting软件的壳体仿真分析及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e29685a-4077-4749-8159-8547eec7ca22/resource) (`1e29685a-4077-4749-8159-8547eec7ca22`)
- S4: [基于AnyCasting软件的汽车蜗壳压铸件的铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ed90eb0-f6e8-4e17-a3dd-ce249eacae54/resource) (`0ed90eb0-f6e8-4e17-a3dd-ce249eacae54`)
- S14: [基于AnyCasting软件的汽车蜗壳压铸件的铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a8efab3-48f8-456c-9197-9b9cac791c4d/resource) (`5a8efab3-48f8-456c-9197-9b9cac791c4d`)
- S33: [基于机器学习的铝合金汽车离合器壳体真空压铸工艺参数研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7a03561-d020-409e-8bdb-c86a8d577f0c/resource) (`f7a03561-d020-409e-8bdb-c86a8d577f0c`)
- S13: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4687709f-d0e8-42b2-a15c-5298da553602/resource) (`4687709f-d0e8-42b2-a15c-5298da553602`)
- S28: [基于数值模拟的转向器阀壳体压铸模具结构及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5c25e15-cf4e-4116-b8d8-9d4fc4be5162/resource) (`e5c25e15-cf4e-4116-b8d8-9d4fc4be5162`)
- S15: [表3-1 AnyCasting软件五大模块介绍](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5edeac1b-7050-4e69-a61b-9382094146ca/resource) (`5edeac1b-7050-4e69-a61b-9382094146ca`)