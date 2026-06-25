---
version: "v1"
generated_at: "2026-06-18T14:47:36+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 36
  source_quality_score: 0.85
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 概述

MAGMA（亦称 MAGMASOFT、Magma铸造模拟仿真软件、MAGMA有限差分铸造仿真软件）是由德国 MAGMA Gießereitechnologie GmbH 开发的商业化铸造过程数值模拟软件[[S22]]。该软件基于有限差分法（FDM）构建核心求解架构，早期采用 FDM/FEM 混合技术路线，后续迭代升级为全 FDM 架构[[S22,S37]]，属于典型的有限差分法铸造仿真商业软件[[S25,S33]]。MAGMASOFT 能够对铸件充型流动、凝固传热、微观组织演变、残余应力与变形等多物理场进行全流程仿真计算[[S27,S41]]，是全球首个面向铸造行业实现商品化的 CAE 软件[[S22]]。

## 开发商与版本演变

MAGMA 软件由德国亚琛工业大学（Technical University of Aachen）Sahm 教授团队联合丹麦技术大学（Technical University of Copenhagen）相关研究人员共同开发，德国 MAGMA Gießereitechnologie GmbH 负责后续商业化运营，总部位于德国亚琛[[S3,S9,S36]]。该公司在全球设有多个区域运营主体，中国区服务由迈格码（苏州）软件科技有限公司负责[[S24]]。

1988 年，MAGMASOFT 正式在德国首次发行[[S16,S22]]；1989 年在德国第 7 届国际铸造博览会（GIFA）上展出，成为全球铸造行业中首个商品化 CAE 软件[[S22,S37]]。后续版本迭代脉络如下[[S16]]：

| 版本 | 发布时间 | 主要更新内容 |
|------|----------|--------------|
| MAGMA 4 | — | 采用 FDM/FEM 混合算法的成熟版本 |
| MAGMA 5 | 2010 年 | 从 4 版本跨越至 5 版本大升级 |
| MAGMA 5.1 | 2011 年 | 推出面向有色金属铸造场景的优化版本 |
| MAGMA 5.2 | 2012 年 | 新增制芯工艺优化与全 3D 铸造模拟 |
| MAGMA 5.5 | 2015 年 | 功能进一步扩展与性能优化 |

## 核心功能与模块

MAGMASOFT 采用模块化架构，标准基础模块共 7 个，同时面向不同铸造工艺场景配置了 10 余款专用工艺模块，覆盖几乎所有主流铸造工艺类型[[S16,S27,S23]]。

### 标准基础模块

| 模块名称 | 功能描述 |
|----------|----------|
| 项目管理模块（Project Management） | 管理多版本工艺方案数据，支持同一项目下多组模拟参数的对比与数据互通[[S23,S16]] |
| 前处理模块（Pre-processor） | 支持多格式 CAD 模型导入或简单几何自建，完成冷却系统、浇注系统等附属结构设计[[S23,S16]] |
| 流体流动分析模块（MAGMA fill） | 模拟充型全过程，输出流动速度/方向、金属液温度分布、压力场分布等结果，支持优化浇注系统设计、预测卷气卷渣位置与模具冲蚀风险[[S23,S7]] |
| 热传及凝固分析模块（MAGMA solid） | 输出凝固时间、温度梯度、冷却速率等参数，支持补缩系统设计及缩孔缩松缺陷预测[[S23,S7]] |
| 制程仿真模块（MAGMA batch） | 仿真重力铸造、压铸的多周期循环生产工况，模拟模具热平衡状态[[S23,S7]] |
| 后处理显示模块（Post-processor） | 三维可视化展示所有模拟结果与缺陷分布[[S23,S16]] |
| 热物理材料数据库（Thermophysical Database） | 提供各铸造合金与造型材料的热物性参数及过程参数，用户可自定义添加新材料数据[[S7,S23,S41]] |

### 专用工艺模块

MAGMASOFT 提供的专用扩展模块包括[[S27,S16,S8]]：

- **MAGMA lpdc**：低压铸造专业模块
- **MAGMA hpdc**：高压铸造专业模块
- **MAGMA iron**：铸铁专业模块，可预测铸铁从石墨生长到基体相的全阶段微观组织分布与最终力学性能
- **MAGMA steel**：铸钢专业模块，可计算铸钢件宏观偏析与热处理诱导的微观结构变化
- **MAGMA tilt**：倾转浇注铸造专业模块
- **MAGMA roll-over**：浇注翻转铸造专业模块
- **MAGMA thixo**：半凝固射出专业模块
- **MAGMA stress**：应力应变分析模块，可预测铸件残余应力、变形、裂纹倾向与模具全周期应力分布
- **MAGMA DISAMATIC**：迪砂线重力铸造专业模块
- **MAGMA INVESTMENT CASTING**：精密铸造专业模块
- **MAGMA C+M**：射砂制芯专业模块

MAGMA 软件的项目管理模块界面如图示，展示了创建项目、版本管理、删除结果等核心操作选项以及多历史项目的版本列表[[S39]]。

![MAGMA软件项目管理主界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8cbd668-400f-4b90-bd42-ad2b6465f000/resource)

## 基本原理：有限差分法（FDM）

MAGMASOFT 以有限差分法（Finite Difference Method, FDM）为核心求解方法[[S25,S33]]。其核心实现逻辑为：通过差商替代微分，将求解对象在时间与空间上进行离散，对每个离散单元分别完成温度场、流动场、应力场等各类物理场的求解，最终汇总所有单元的结果，得到全时空域的工艺行为预测[[S11,S32]]。

在流体力学数值解法中，有限差分法是在离散的网格点上将各偏导数项化为差商来求数值解：选择合适的基本方程，确定相应的定解条件，然后将微分方程离散到差分网格上求解[[S11,S21]]。

有限差分法具有求解过程简单、计算速度快、前后处理易于实现的优势[[S11,S32]]。在充型流动场分析场景下，与有限元法相比具有独特优势，因此目前进行流体力学数值分析的大多数软件均基于有限差分法[[S11,S21]]。

差分网格布局示意图展示了有限差分法对计算域的空间离散方式[[S31]]。

![有限差分网格布局示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4bd7fdf-a63d-4d74-bad3-d5aab67c6a65/resource)

### 网格划分

MAGMASOFT 的物理网格划分完全基于有限差分法实现，提供四种可选网格生成模式[[S38,S23]]：

| 网格划分模式 | 适用场景 |
|--------------|----------|
| 自动（automatic） | 一般场景快速网格生成 |
| 标准（standard） | 按用户要求调整参数，满足常规计算精度 |
| 高级（advanced） | 分别定义铸件、浇注系统、模具的区域网格大小 |
| 更高阶（advanced2） | 针对特定部位进行更细化的网格细分 |

用户可根据模拟精度需求和计算资源情况选择匹配模式，通过设定全局参数调整整体网格粗细，完成全铸造系统几何的全自动网格划分[[S23,S38]]。

## 材料数据库

MAGMASOFT 内置的热物理材料数据库覆盖多类铸造常用材料[[S27,S41]]：

- **铸造合金**：HT300 等灰铸铁牌号的全套热物性参数[[S1]]，以及全系列铸铁、铸钢、铝合金、镁合金等铸造合金的物性数据[[S27,S41]]
- **造型材料**：呋喃树脂自硬砂等造型材料的热物理属性参数[[S1,S27]]
- **辅助工艺材料**：市面主流压铸机参数、迪砂线造型机参数、FOSCO 滤片、保温冒口等辅助工艺材料的完整工艺数据[[S27,S2]]

用户可直接调用库内默认参数完成模拟，也可自定义添加新材料的物性数据[[S41]]。

MAGMA 材料定义界面展示了材料类型、铸造过程温度参数、材料库配置等核心设置项[[S20]]。

![MAGMA软件材料定义操作界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94d86316-eac8-4a83-ae54-cafb4a09a389/resource)

## 可模拟的铸造工艺

MAGMASOFT 可支持的全部铸造工艺类型包括[[S27,S7,S9]]：

- 普通砂型铸造、迪砂线铸造
- 高压铸造、压力铸造、低压铸造、差压铸造
- 金属型铸造
- 熔模（精密）铸造
- 离心铸造、连续铸造
- 消失模铸造
- 半固态触变铸造、挤压铸造
- 倾转浇注、翻转浇注

### 压力充型模拟

MAGMA 完整支持压力充型方式的模拟计算。软件内置 MAGMA hpdc 高压铸造专业模块和 MAGMA lpdc 低压铸造专业模块，采用 SOLA-VOF 算法求解 Navier-Stokes 方程[[S27,S40,S13]]，可精准模拟高压、低压、差压等压力驱动工况下金属液的充型速度分布与压力场变化，支持高射速压铸等特种压力充型场景的全流程仿真[[S27,S1]]。

### 呋喃树脂自硬砂与 HT300

已有公开工程案例证实，MAGMA 完全适配呋喃树脂自硬砂造型的砂型铸造仿真场景，可结合该类砂型对应的热物理属性参数完成全流程充型与凝固仿真计算[[S1,S19]]。同时，MAGMA 可对 HT300 牌号灰铸铁的充型、凝固过程进行完整模拟，软件内置 MAGMA iron 铸铁专业模块，可针对铸铁材料的石墨生长、基体相结构分布演变进行精准预测[[S1,S27,S8]]。

## 操作流程

MAGMASOFT 的标准操作流程分为前处理、求解计算、后处理三个阶段[[S16,S27,S8]]。

### 前处理
1. 导入由其他三维 CAD 软件输出的 STL 格式几何模型[[S8,S9]]
2. 调用软件自带网格划分工具，按不同区域特征定义网格尺寸参数完成自动网格划分[[S16,S27]]
3. 从材料数据库中设置对应合金与铸型材料的热物理参数[[S27,S9]]
4. 配置完整的工艺边界条件（浇注温度、充型速度、压力边界、冷却条件等）[[S16]]

### 求解计算
调用匹配对应工艺的专用模块（如 MAGMA fill 与 MAGMA solid），输入全过程工艺参数，启动求解器依次完成充型流场计算与凝固温度场计算，同步实现多物理场耦合计算，输出各时间节点的全量计算结果[[S16,S27]]。充型计算采用 SOLA-VOF 算法求解 Navier-Stokes 方程，同时考虑紊流效应、金属液表面张力以及金属液与型壁的相互作用[[S13,S40]]。

### 后处理
从结果数据目录调取不同模拟阶段的输出文件，三维可视化查看充型流动状态、各时刻全域温度分布、凝固进度、缩孔缩松等缺陷分布及应力应变结果，基于可视化输出对仿真结果进行量化评估，支撑后续工艺优化决策[[S16,S27,S8]]。

MAGMA 软件输出的带浇冒系统铝合金铸件缩孔分布热图，以孔隙率百分比为色标可视化展示不同区域的缩孔缺陷占比[[S4]]。

MAGMA 对低压铸造铝合金缸盖凝固过程的温度场模拟结果，展示了铸件在凝固阶段的三维温度分布[[S14]]。

![MAGMA软件低压铸造缸盖凝固温度场模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/587bc7a6-0ced-4d89-ba7d-2f44cd539de0/resource)

## 应用行业

MAGMA 仿真在下游行业中的应用覆盖[[S9,S28]]：
- 汽车零部件（如发动机缸体、缸盖、变速箱壳体、控制臂等铸件）
- 通用机械传动部件
- 航空特种合金铸件
- 工程机械耐磨铸件
- 通讯与消费电子压铸零件

可支撑各类黑色金属与有色金属铸件的工艺优化与新产品开发，有效缩短试制周期[[S9]]。

## 与主流铸造仿真软件对比

以下表格横向对比了 MAGMA、ProCAST、AnyCasting 三款主流铸造数值模拟软件的核心技术特性与适配场景[[S15,S10,S5,S35,S29,S18]]：

| 软件 | 开发国家 | 核心求解方法 | 核心特性 | 不足 |
|------|----------|-------------|----------|------|
| MAGMASOFT | 德国 | FDM（有限差分法） | 模块化程度高，针对不同铸造工艺有专属求解模块，计算速度快，薄壁件充型凝固分析能力突出 | — |
| ProCAST | 美国 | FEM（有限元法） | 多物理场耦合能力优异，求解精度高，对复杂异形铸件与涉及辐射传热的熔模铸造场景适配性极强 | 前处理网格生成能力偏弱，网格划分操作门槛较高，常需搭配第三方网格工具 |
| AnyCasting | 韩国 | FVM（有限体积法） | 操作界面直观易用，自动网格划分效率极高，整体求解速度为三款软件中最快，更适配量产压铸场景的快速工艺验证 | 仅支持 Windows 操作系统，仿真精度略低于 ProCAST |

MAGMASOFT 兼容绝大多数主流 CAD 软件数据接口，支持 IGES、STL、DXF 等通用三维文件格式导入，同时可直接读取 Pro/E、UG 等主流建模软件的原生数据，模型导入与转换便捷[[S30]]。

## Sources
- S22: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a49544a0-99b5-4cc9-8647-3276eb49bd2f/resource) (`a49544a0-99b5-4cc9-8647-3276eb49bd2f`)
- S37: [表1-1 国内外铸造CAE软件概况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecb5ba93-745f-43c0-b78f-5b4ed0a51cbb/resource) (`ecb5ba93-745f-43c0-b78f-5b4ed0a51cbb`)
- S25: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b791779c-501a-40f6-ac79-ec32772621ab/resource) (`b791779c-501a-40f6-ac79-ec32772621ab`)
- S33: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e11e923f-2918-4a2e-b518-eeeaa0c5208d/resource) (`e11e923f-2918-4a2e-b518-eeeaa0c5208d`)
- S27: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba8f3f8b-82a2-4d58-a370-b9a4a6279fe6/resource) (`ba8f3f8b-82a2-4d58-a370-b9a4a6279fe6`)
- S41: [不同型腔真空度对铸件组织和性能的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9defc8e-e493-41ee-8f21-6e8b79cf3fac/resource) (`f9defc8e-e493-41ee-8f21-6e8b79cf3fac`)
- S3: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b5d9a2f-5f00-4c24-bd19-d6a230eedea0/resource) (`0b5d9a2f-5f00-4c24-bd19-d6a230eedea0`)
- S9: [镁合金汽车控制臂铸锻复合成形工艺的研究开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2be64f5d-f564-4218-ba6b-92a231c654d2/resource) (`2be64f5d-f564-4218-ba6b-92a231c654d2`)
- S36: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S24: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4ca88b2-a303-494b-8c1e-939cc87eda09/resource) (`b4ca88b2-a303-494b-8c1e-939cc87eda09`)
- S16: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a62dd6c-7a87-47ef-888c-1374e8938011/resource) (`7a62dd6c-7a87-47ef-888c-1374e8938011`)
- S23: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b17a4f24-0a05-43d8-9c28-390e3da5432c/resource) (`b17a4f24-0a05-43d8-9c28-390e3da5432c`)
- S7: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20c5b741-703b-4565-bfac-711142bfd43f/resource) (`20c5b741-703b-4565-bfac-711142bfd43f`)
- S8: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20f2db5c-2a6f-49c1-ae1d-2e9451819b4d/resource) (`20f2db5c-2a6f-49c1-ae1d-2e9451819b4d`)
- S39: [MAGMA软件项目管理模块界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8cbd668-400f-4b90-bd42-ad2b6465f000/resource) (`f8cbd668-400f-4b90-bd42-ad2b6465f000`)
- S11: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35b43f43-42dd-4b54-8e21-3f2846be22b0/resource) (`35b43f43-42dd-4b54-8e21-3f2846be22b0`)
- S32: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df5c2439-da46-4d16-bba3-6a21310e6b9c/resource) (`df5c2439-da46-4d16-bba3-6a21310e6b9c`)
- S21: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9fea1ad7-8492-483b-b6f9-47db5812bab0/resource) (`9fea1ad7-8492-483b-b6f9-47db5812bab0`)
- S31: [几种不同图形的差分网格布局](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4bd7fdf-a63d-4d74-bad3-d5aab67c6a65/resource) (`d4bd7fdf-a63d-4d74-bad3-d5aab67c6a65`)
- S38: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0947f0f-927f-47ec-aa9e-4866d8b0da9c/resource) (`f0947f0f-927f-47ec-aa9e-4866d8b0da9c`)
- S1: [基于有限差分仿真含过滤网浇注系统的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0787207f-d87c-41b5-a586-3df623f80af3/resource) (`0787207f-d87c-41b5-a586-3df623f80af3`)
- S2: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07f7190d-9f24-405e-9905-ad286127ca0a/resource) (`07f7190d-9f24-405e-9905-ad286127ca0a`)
- S20: [MAGMA软件材料定义界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94d86316-eac8-4a83-ae54-cafb4a09a389/resource) (`94d86316-eac8-4a83-ae54-cafb4a09a389`)
- S40: [汽车发动机铝合金缸体压铸工艺及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f93659b5-5f5d-4c7a-9e6d-719b57cc2662/resource) (`f93659b5-5f5d-4c7a-9e6d-719b57cc2662`)
- S13: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52b7778e-a660-4118-bdaa-be00afc4a329/resource) (`52b7778e-a660-4118-bdaa-be00afc4a329`)
- S19: [725693_树脂自硬砂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/905c6ef2-3105-4102-91e5-4f26cc121248/resource) (`905c6ef2-3105-4102-91e5-4f26cc121248`)
- S4: [图5.4 带浇冒系统铸件的缩孔分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ef0c103-5fd3-489d-b09e-55693b0f1da7/resource) (`0ef0c103-5fd3-489d-b09e-55693b0f1da7`)
- S14: [低压铸造缸盖凝固过程温度场MAGMA模拟图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/587bc7a6-0ced-4d89-ba7d-2f44cd539de0/resource) (`587bc7a6-0ced-4d89-ba7d-2f44cd539de0`)
- S28: [镁合金铸件集合](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c95a34c2-7936-433a-bf7e-527ade063df8/resource) (`c95a34c2-7936-433a-bf7e-527ade063df8`)
- S15: [表2.1 主流铸造数值模拟软件对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62ad51a3-c595-452b-8c7d-bff26d5f2a5f/resource) (`62ad51a3-c595-452b-8c7d-bff26d5f2a5f`)
- S10: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34173a8e-f6f1-4181-9188-514d82f794e5/resource) (`34173a8e-f6f1-4181-9188-514d82f794e5`)
- S5: [燃汽轮机用SCS13合金锁键铸造工艺数值模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12ddc946-447d-4491-91e0-c98f1b605429/resource) (`12ddc946-447d-4491-91e0-c98f1b605429`)
- S35: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S29: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbcee639-0ac9-4d7f-8309-92a4c5d40853/resource) (`cbcee639-0ac9-4d7f-8309-92a4c5d40853`)
- S18: [TC4合金非对称翼型受油管熔模精密铸造工艺及凝固特性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8385eca2-3951-4e3d-a470-d4cedcd6d253/resource) (`8385eca2-3951-4e3d-a470-d4cedcd6d253`)
- S30: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf063c89-7f01-49f0-bec3-84d9babc20a4/resource) (`cf063c89-7f01-49f0-bec3-84d9babc20a4`)