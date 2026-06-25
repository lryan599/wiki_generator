---
version: "v1"
generated_at: "2026-06-18T05:44:05+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 18
  source_quality_score: 0.84
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

华铸CAE（英文对应名称：InteCAST，压铸场景亦使用缩写 HZCAE）是由华中科技大学（原华中理工大学）华铸软件中心开发的一款铸造工艺分析软件，正式全称为"华铸CAE凝固模拟分析系统"，官方记载的公开别名包括华铸CAE数模模拟软件、华铸CAE/Inte Cast铸造工艺分析软件、华铸CAE铸造工艺模拟软件、华铸CAE系统、华铸CAE软件[[S1]]。该软件属于国产商品化最成熟的铸造CAE产品，以铸件充型与凝固过程数值模拟技术为核心，可为铸造企业提供工艺分析与优化方案[[S25]]。

![华铸CAE铸造工艺分析系统主控界面，展示了前置处理、计算分析、后置处理三大核心功能入口及STL处理、缺陷判断等快捷操作选项](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a5eb840-6f44-4fa1-9411-0f5713a3db2f/resource)

## 开发历程

华铸CAE自1985年起持续研发，经过长期迭代演进[[S1]]。其较早公开的稳定版本为V7.0，于2008年之前推出，可在Windows 98、Windows NT、Windows 2000、Windows XP操作系统下运行，覆盖完整的前置处理、计算分析、后置处理全流程功能体系[[S15,S17]]。当前最新公开稳定版本为V11.0，新增复合网格技术、缺陷定量化预测模型，支持自动完成网格剖分与三维动画后处理，同时集成华铸ERP、华铸FCS等模块，形成完整的数字化铸造平台[[S1,S6]]。V1.0至V6系列的版本推出时间及对应核心升级点，目前无权威公开资料可稽。

研发团队曾获得国家科技进步奖，并拥有多项已授权软件著作权及发明专利[[S1]]。

## 技术原理

华铸CAE采用有限差分法（FDM）作为核心数值计算方法，使用均匀规则立方体网格进行剖分[[S9,S23]]。求解的物理模型覆盖不可压缩流体连续性方程、Navier-Stokes动量方程及带有相变潜热项的能量传热方程，配套体积函数类自由面追踪算法求解充型过程流动前沿，实现充型、凝固全流程耦合求解[[S19,S22]]。

模型数据仅支持STL格式的外部导入，软件内不支持直接修改模型、自动推荐网格、默认参数设置以及模拟结果直接反馈生成优化工艺的功能[[S9]]。

## 技术架构与模块功能

华铸CAE划分为前处理、求解器、后处理三大核心模块，三者按固定顺序操作不可颠倒，数据流遵循前处理准备求解环境、求解器输出计算结果、后处理实现结果可视化的逻辑[[S11,S14,S15]]。

### 前处理

前处理模块负责为迭代计算准备求解环境，主要功能如下[[S14,S17]]：

- 支持市面上绝大多数主流三维CAD软件（包括AutoCAD、Pro/E、UG、SolidWorks、SolidEdge、CATIA、I-DEAS、MDT等）生成的STL格式文件导入与装配校验；
- 最多支持72类不同材质定义；
- 自带邻接优先级设置功能；
- 全自动网格剖分，中等复杂程度铸件剖分千万级网格仅需数分钟；
- 具备STL文件容错纠错能力；
- 铸件模数自动计算与剖分结果自动校验。

### 求解器

求解器是软件计算核心，以程序化、自持式循环迭代完成各物理场的数值求解，所需用户操作量为三模块中最少[[S15]]。具体功能包括[[S14,S15,S17]]：

- 独立完成凝固分析、充型分析及流动与传热耦合计算；
- 凝固分析在微机上支持最大数亿级网格，流场与耦合计算支持数百万单元；
- 铸件质量、体积、工艺出品率自动计算；
- 多种自动存盘方式，支持计算断点自动恢复与现场保护。

### 后处理

后处理模块实现计算结果的可视化表达，主要功能包括[[S14,S16,S17]]：

- 三维场景实时缩放、旋转、任意方向剖切；
- 自动生成X射线透视图、凝固色温图、温度梯度图、铸件结构图、铸型系统装配图、流动向量图、填充体积图、压强分布图、充型温度分布图等十多类结果图形；
- 充型/凝固过程三维动画自动合成与播放；
- 鼠标点选生成任意点温度变化曲线；
- 孤立液相区全自动搜索统计，最终缺陷预测输出。

![华铸CAE前置处理界面，展示了六缸柴油机机体三维模型及对应铸造工艺树](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/092d8dcd-f4ef-4891-9345-817194c56a37/resource)

## 模拟能力与工艺适用范围

### 模拟分析功能

华铸CAE全量模拟能力覆盖充型流动过程、凝固过程温度场模拟、应力应变场模拟[[S22,S18]]。主要内置分析内容如下表所示：

| 分析类别 | 具体内容 |
|---------|---------|
| 核心分析 | 充型过程、流动与传热耦合过程、结晶凝固过程、应力应变分布 |
| 缺陷预测 | 卷气、卷渣、冲砂、浇不足、冷隔、缩孔、缩松、裂纹、变形 |
| 孔缩类缺陷预测精度 | 可达95% |

### 工艺与材质适配范围

华铸CAE支持包括压力铸造（压铸）在内的全系列铸造工艺类型[[S22,S7,S26]]，具体适配情况如下表所示：

| 维度 | 支持范围 |
|------|---------|
| 铸造工艺 | 砂型铸造、金属型铸造、铁模覆砂铸造、压力铸造、低压/差压铸造、熔模铸造、离心铸造、倾斜铸造等 |
| 合金材质 | 铸钢、球墨铸铁、灰铸铁、铸造铝合金、铸造铜合金等 |

### 压铸专用模块

华铸CAE配备独立的DCCAE专用压铸模拟模块，可实现压铸多周期全流程连续模拟，支持不同冷却介质（水、油、气）的复杂冷却工艺仿真。可模拟高压高速充型下的负压分布、卷气夹杂形成过程、充型阶段动态固相率分布，适配压铸高速充型、高压保压的专属工艺特性[[S16,S4,S26]]。

## 典型应用案例

徐尔灵等人开展的转盘铸件充型模拟研究，已被正式学术文献与华铸CAE公开产品资料共同收录，属于该软件公开记载的典型工业应用案例[[S1,S13]]。研究对象为应用于油气勘探、地质勘察等领域的旋转钻机核心转盘部件，关键功能涵盖转动钻杆、承受反扭矩、承托钻杆/套管重量及辅助处理井下事故。该类转盘铸件典型材质为HT300灰铸铁，属多孔多槽结构且壁厚差异大，原有砂型铸造工艺下厚大部位易产生缩孔、缩松、夹渣、气孔等缺陷[[S13]]。

研究团队采用华铸CAE通用分析框架开展模拟：完成转盘铸件及配套浇注系统的三维建模并生成STL格式文件导入软件，设置边界与工艺参数后开展充型过程流场-温度场耦合计算，通过后处理模块分析充型顺序与流动状态，识别并定位潜在缺陷区域[[S13,S22]]。该案例体现了华铸CAE可准确预测转盘类构件充型过程中卷气、冲砂、冷隔、缩孔、缩松等铸造缺陷的能力[[S1,S22]]。

## 与同类主流软件的比较

### 总体对比

目前国内外主流铸造模拟软件中，华铸CAE与ProCAST、AnyCasting、MAGMASoft等各有不同的技术路线与市场定位。

| 软件名称 | 国家 | 算法 | 核心特征 |
|---------|------|------|---------|
| ProCAST | 法国 | FEM | 流动-传热-应力完全耦合模拟，拟合精度高，适配砂铸、压铸、连续铸造等各类工艺 |
| 华铸CAE | 中国 | FDM | 华中科技大学开发，国产商品化最成熟的铸造软件，提供高效精确的工艺分析优化方案 |
| AnyCasting | 韩国 | FEM | 分析速度快、准确度高、功能全面，集成丰富的铸造工程经验数据库 |
| MAGMASoft | 德国 | FDM | 同算法中最成熟产品，提供从零件设计、模具设计到生产的全流程解决方案，缺陷预测精准 |
| FLOW-3DCAST | 美国 | FDM | 充型模拟金属液流动计算方面成熟，提供热模数、热节、凝固时间、Niyama缺陷判据等功能 |

### 压铸CAE专项功能对比

在压铸模拟场景下，华铸CAE与ProCAST的功能特点对比如下[[S9]]：

| 对比项目 | 华铸CAE | ProCAST |
|---------|---------|---------|
| 模型数据格式 | STL | IGES等格式 |
| 数值模拟方法 | 有限差分法(FDM) | 有限元法(FEM) |
| 网格剖分方式 | 均匀网格 | 非均匀网格 |
| 模型修改支持 | 不支持 | 仅支持简单面片修改 |
| 网格自动推荐 | 无 | 无 |
| 默认参数设置 | 无 | 无 |
| 模拟反馈工艺 | 无 | 无 |

### 缺陷预测能力对比

![ProCAST(左)与华铸CAE(右)对大型铸件缩孔缺陷的预测结果对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65fe2539-6415-48a1-b3dd-c2c4ae2f301b/resource)

上图为文献中收录的ProCAST与华铸CAE对同一大型铸件缩孔缺陷的预测结果对比，直观展示了两种软件在缺陷识别标注方面的表现[[S8]]。两者均能有效预测缩孔缺陷位置，但基于各自网格剖分策略与数值算法的差异，在缺陷形态细节的拟合上存在一定差异。

## Sources
- S1: [2505109_华铸CAE](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/019777af-e28f-44e2-9962-ccde177bf179/resource) (`019777af-e28f-44e2-9962-ccde177bf179`)
- S25: [表3.1 国内外主流铸造模拟软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f69680cd-edbb-41aa-a12f-2e53e9ac09ad/resource) (`f69680cd-edbb-41aa-a12f-2e53e9ac09ad`)
- S15: [压铸成形工艺与模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82c247df-f495-4969-93e6-79b08c89f519/resource) (`82c247df-f495-4969-93e6-79b08c89f519`)
- S17: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/986bc2e1-cdd8-4be3-87e7-4242aff793d1/resource) (`986bc2e1-cdd8-4be3-87e7-4242aff793d1`)
- S6: [华铸CAE软件基本信息表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b13f87d-1f6d-4cf1-a2e3-47f2d28c52e8/resource) (`4b13f87d-1f6d-4cf1-a2e3-47f2d28c52e8`)
- S9: [表5-2 压铸CAE功能对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bfcfc6a-4f80-4ed1-b79a-b5451b8c2d41/resource) (`6bfcfc6a-4f80-4ed1-b79a-b5451b8c2d41`)
- S23: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d04bad70-9923-4b41-90d2-14f2fdedb775/resource) (`d04bad70-9923-4b41-90d2-14f2fdedb775`)
- S19: [实用压铸模设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7a96f17-0622-4ce2-bc0d-41f8f493dc87/resource) (`b7a96f17-0622-4ce2-bc0d-41f8f493dc87`)
- S22: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3ff8acc-19ec-43f6-8ec0-ba5d819eca10/resource) (`c3ff8acc-19ec-43f6-8ec0-ba5d819eca10`)
- S11: [CAE软件的组成模块及关系示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f39a8b2-a3b7-4ebc-9f26-099c08b98417/resource) (`6f39a8b2-a3b7-4ebc-9f26-099c08b98417`)
- S14: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a68d6ce-7d45-464e-8e87-746891541ae2/resource) (`7a68d6ce-7d45-464e-8e87-746891541ae2`)
- S16: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/83af0871-a48c-47e4-9756-6dc7ce02b06c/resource) (`83af0871-a48c-47e4-9756-6dc7ce02b06c`)
- S18: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9962a0bc-4e4f-497a-8c39-b2b8fc3fb914/resource) (`9962a0bc-4e4f-497a-8c39-b2b8fc3fb914`)
- S7: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62b8dedb-1441-46ec-ad9a-59cc0c10a772/resource) (`62b8dedb-1441-46ec-ad9a-59cc0c10a772`)
- S26: [压铸成型技术及模具 设计与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbcf1cba-b440-49e4-a6fb-85eaf54e607f/resource) (`fbcf1cba-b440-49e4-a6fb-85eaf54e607f`)
- S4: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38b0f70c-b11c-468f-b414-926818963d61/resource) (`38b0f70c-b11c-468f-b414-926818963d61`)
- S13: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73d5bde8-98b1-41f7-ae78-17c5adf09dcc/resource) (`73d5bde8-98b1-41f7-ae78-17c5adf09dcc`)
- S8: [a3—ProCAST预测缩孔缺陷结果；b3—华铸CAE预测缩孔缺陷结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65fe2539-6415-48a1-b3dd-c2c4ae2f301b/resource) (`65fe2539-6415-48a1-b3dd-c2c4ae2f301b`)