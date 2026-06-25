---
version: "v1"
generated_at: "2026-06-18T17:05:07+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 33
  source_quality_score: 0.86
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述与定义

Thermo-Calc全称为Thermo-chemical Databank for Equilibriums and Phase Diagram Calculations，是基于CALPHAD(CALculation of Phase Diagram)方法开发的代表性热力学计算软件系统[[S4,S22]]。该软件由瑞典皇家工学院的B. Sundman、B. Jansson和M. Schalin等人于1981年发布首个版本，其设计初衷是进行多元系的热力学计算，目前可处理多达40个组元的多组分体系热力学计算[[S4,S22]]。

在铸造合金设计与工艺开发领域，Thermo-Calc作为核心计算工具，不仅可用于各种热力学体系的平衡计算，还可通过对接DICTRA动力学程序进行扩散控制相变的非平衡模拟[[S4]]。

## 工作原理与CALPHAD方法

Thermo-Calc的核心计算逻辑由CALPHAD方法驱动。该方法的基本原理是：集热力学性质、相平衡数据、晶体结构、磁性、有序-无序转变等信息为一体，为体系中各相建立对应的Gibbs自由能表达式，其中的可调参数通过实测热力学和相图数据优化计算获得，最终基于恒温恒压条件下多相体系总Gibbs自由能最小原理进行求解，获得热力学自洽的相图与各相热力学性质参数[[S22,S36,S30]]。

CALPHAD方法的主要优势体现为：
- 体系热力学性质和相图的热力学自洽性，确保所有热力学性质之间的内部一致性[[S22]]
- 可外推和预测多元系热力学性质和相图，避免传统实验测定相图的繁琐过程[[S22]]
- 可计算亚稳相图，覆盖扩散活性小、难以达到平衡的体系以及极端条件下实验难以测定的体系[[S22]]
- 可获得以不同热力学变量为坐标的各种相图形式，适配不同条件下的材料制备与工艺设计需求[[S22]]

![CALPHAD方法Thermo-Calc相图计算全流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/966d7c43-b24a-41e0-8b39-622fbed12b61/resource)

该流程图完整展示了Thermo-Calc基于CALPHAD方法的通用计算步骤：从收集评估已有相图与热力学实测数据、选择各相对应的Gibbs自由能模型、赋予参数初值，到将计算结果与实测数据比对校验，校验合格后存入热力学数据库并完成指定多元合金的相图与热物性结果计算[[S26]]。

## 软件版本与发行形态

Thermo-Calc软件存在两类主流发行版本[[S10,S27]]：

| 版本类型 | 运行环境 | 特点 |
|---------|---------|------|
| TCC | DOS环境 | 功能成熟，核心功能完整性更高 |
| TCW | Windows环境 | 面向普通用户的图形化版本 |

![Thermo-Calc面向Windows平台的TCW版本演示版主界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02718df5-a605-4410-917f-f2e34f5f4240/resource)

该界面展示了Windows平台下Thermo-Calc TCW演示版的主界面，包含软件标识、菜单栏和工具栏，标注有"Demo Version Thermo-Calc TCW"的版本标识[[S1]]。

## 核心功能模块

Thermo-Calc软件核心引擎由600余个独立子程序模块化构成，各模块可运行时动态切换。TCC版本设有七个基本模块[[S4,S10,S12]]：

| 模块名称 | 功能描述 |
|---------|---------|
| TDB | 资料库管理模块，管理热力学数据库 |
| GES | 多相热力学模型处理和数据控制模块，列出体系信息和热力学/动力学数据 |
| TAB | 物相和反应的热力学性质表模块，生成纯物质、混合物或反应的热力学性质表格 |
| POLY | 多组元平衡计算模块，计算各类二元、三元和多元相图及热力学性质 |
| POST | 相图与性能图后处理模块，描绘各种相图与特性图 |
| PARROT | 实验数据评估和参数优化模块，利用实验信息进行相图估算与参数优化 |
| ED_EXP | 实验点编辑和平衡计算模块 |

此外，Thermo-Calc还内置以下专业化功能模块[[S4,S12]]：
- **SCHEIL模块**：专门用于铸造领域的非平衡凝固过程模拟与偏析预测
- **BIN模块**：快速生成二元合金相图
- **TERN模块**：快速生成三元合金相图

![Thermo-Calc软件包整体模块架构与数据流向示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73ebc2a4-53e4-4e6b-bbbf-6f940329f7d5/resource)

该架构图将软件分为"参数评估"和"日常使用"两大功能分区，明确了PARROT优化模块、TDB数据库模块、GES模型模块、POLY平衡计算模块等核心组件的数据流交互逻辑，展示了其对接TC数据库输出相图等计算结果的完整链路[[S16]]。

## 热力学数据库体系

Thermo-Calc配套的内置数据库主要为SGTE（欧洲共同体热化学科学组）系列集成热化学数据库，包含[[S4]]：
- **SSOL数据库**：含经过优化的200余个合金体系的溶液数据库
- **SSUB数据库**：含3000余种化合物热力学参数
- **FEDAT/TCFE数据库**：专门用于钢铁材料相图与热力学性质计算
- **SLAG数据库**：铁液与炉渣专用计算数据库

### 铸造领域专用数据库

**铁基合金**：TCFE是Thermo-Calc官方开发的铁基合金专用热力学数据库，专门适配钢铁类铸造合金的相平衡、凝固路径、夹杂物与析出相计算，是铸造领域黑色金属材料热力学计算的首选专用数据库[[S4,S12]]。

**铝基合金**：TCAL系列是铝基合金专用热力学数据库。TCAL5及更高版本对2xxx系、6xxx系、7xxx系等常见铸造铝合金的平衡相（如Al₂Cu、Mg₂Si、MgZn₂等）热力学参数完成了高精度标定，适配铸造铝合金的凝固路径、析出相演化及热物性参数计算[[S36]]。

**其他有色合金**：Thermo-Calc支持对接第三方商用镁合金、铜合金热力学数据库，可覆盖常用压铸镁合金、铸造铜合金的相平衡计算需求[[S10]]。

## 典型输入与输出

### 输入参数

面向铸造场景的典型输入参数要求[[S30,S12]]：
- 选定对应合金体系的组成元素，并设置其质量分数或摩尔分数范围
- 设置温度计算区间（常规从室温延伸至高于合金液相点300~500℃）
- 默认常压1 atm作为压力边界条件
- 排除冗余的非目标相后启动平衡计算

### 输出结果

Thermo-Calc支持的典型输出结果类型包括[[S12,S23]]：
- 二元/三元/多元等温截面相图
- 不同温度下各平衡相的摩尔分数或质量分数
- 热焓、定压比热容、体积弹性模量等热物理参数
- 液相线温度与固相线温度数值
- 稳定相及亚稳相平衡计算结果

![Thermo-Calc生成的Mg-Li二元相图及操作功能面板示例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76cf6792-be71-4fa7-9bf5-5d463ee64eb9/resource)

该图展示了Thermo-Calc生成的Mg-Li二元合金相图操作界面，右侧为带温度与成分坐标轴的可视化区域，左侧操作面板标注了坐标轴设置、原子/质量分数单位切换、晶体数据表导出等常用功能按钮[[S17]]。

## 铸造应用场景

### 合金成分正向设计

Thermo-Calc可直接用于铸造合金的成分设计与优化。以ZL201铸造铝合金为例，软件可分别计算Al-Cu、Al-Mn、Al-Ti二元系，以及Al-Cu-Mn、Al-Cu-Ti、Al-Mn-Ti三元系的平衡相图与冷却凝固曲线，明确θ相（Al₂Cu）、Al₂₀Cu₂Mn₃、Al₃Ti等强化相的析出温度，为该类铸造铝合金的成分正向设计提供精准热力学依据[[S36,S20]]。

类似地，可利用Thermo-Calc定量计算Al-4.5Cu-0.5Mn-0.5Mg-0.2Si合金在Fe含量0~2 wt.%范围内的物相析出顺序和凝固温度区间，为控制合金中杂质Fe相的有害影响、预判合金热裂敏感性提供直接数据支撑[[S2]]。

### 半固态加工工艺窗口预测

Thermo-Calc 2019a版本已在半固态铸造领域得到实际工程应用。通过计算不同铸造铝合金的液相分数随温度变化曲线，可获得半固态加工的合适工艺窗口。研究表明，356、357等铸造铝合金的半固态加工窗口显著宽于2024、7075等变形铝合金[[S29]]，这为半固态流变成形工艺参数制定提供了可靠的热力学依据。

### 凝固过程与非平衡模拟

Thermo-Calc内置的SCHEIL模块可直接完成Scheil非平衡凝固模拟，面向铸造场景可快速求解合金在非平衡冷却条件下的凝固区间、共晶相析出含量、微观偏析趋势等关键铸造工艺参数，支持332.1等牌号铸造铝合金的凝固过程定量计算[[S4,S33]]。

### 热裂敏感性预判

Thermo-Calc计算得到的合金凝固温度区间、固相线/液相线温度、不同固相分数下的残余液相比例等热力学参数，可作为Clyne-Davies准则、HTS热裂敏感性系数等主流铸造热裂预判模型的基础输入数据，支撑铸造工艺窗口中热裂风险的提前评估[[S32,S11]]。

![轻合金铸造热撕裂与微孔隙预测通用计算流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2f4a13a-4888-41dc-a19b-2121d2b31d3a/resource)

该流程图展示了轻合金直接冷却铸造中热撕裂与微孔隙预测的计算流程。输入温度、应变、温度变化率参数后，通过凝固模型计算固相分数，结合本构模型输出的应力，通过收缩率与补缩率的对比判断最终缺陷类型。Thermo-Calc输出的热力学固相分数参数在该仿真流程中处于核心输入地位[[S35]]。

### 计算验证与可靠性

多项公开验证研究表明Thermo-Calc计算结果的可靠性：

- Fe-Mn-Ni-Cr-Al-Si系高熵铸造合金验证研究显示，Thermo-Calc预测的平衡相类型（FCC、BCC/B2、硅化物相）与实际铸态试样的金相观测结果高度匹配[[S21]]
- FM52合金固相线、液相线温度的热力学计算结果与差热分析（DTA）实测结果吻合度较高[[S13]]
- 319s铸造铝合金平衡热力学计算结果与SPSC实测数据一致性较好，其中温度随液相分数提升基本保持恒定，焓随液相质量分数上升呈近线性增长趋势[[S6]]

## 动力学扩展模块：DICTRA

DICTRA（Diffusion Controlled TRansformation）是Thermo-Calc配套的动力学附加模块，专门用于模拟多元合金中的扩散控制相变过程。其核心特性为[[S4,S18,S28]]：
- 通过内置接口直接调用Thermo-Calc提供的热力学数据
- 搭配MOB系列迁移率数据库，计算随温度、组分变化的多组元扩散系数
- 当前支持平面形、圆柱形、球形三类简单几何形状体系的扩散求解

DICTRA在铸造工艺中的典型应用场景包括：
- 合金均匀化处理过程模拟
- 渗碳/脱碳/渗氮工艺模拟
- 凝固微观偏析分析
- 析出相粗化（Ostwald熟化）过程定量预测
- 珠光体长大过程分析
- 硬质合金烧结模拟

结合Thermo-Calc的热力学求解能力与DICTRA的动力学模拟功能，可精准计算铸造冷却及时效过程中析出相的类型、析出序列、平衡含量、相界面浓度等参数，已被广泛用于钢铁、铝合金铸造工艺开发中的析出相调控设计[[S18]]。

## PARROT参数优化模块

PARROT是Thermo-Calc中负责热力学模型参数评估与优化的核心模块，其工作流程为[[S12,S14]]：利用实验与文献数据，构建、评价并优化不同的热化学及动力学参数，将实验数据组合构成模型参数，判断其可靠性，并可为进一步实验提供方案，为相变模型和仿真提供基础。该方式使材料设计脱离了传统的试错法，不仅能提供稳定相数据，还能提供亚稳相的化学势及驱动力数据。

![Thermo-Calc PARROT模块基于实验数据优化热力学模型参数的工作流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/648188d0-81cf-426b-af98-9e340dac6fbe/resource)

该流程图展示了PARROT模块的完整工作逻辑：从基本理论、经验法则、实测实验数据出发，构建Gibbs自由能热力学模型，经PARROT模块迭代优化后写入数据库，最终输出经过校验的平衡相图与对应热力学性能数据；优化失败时可返回重选模型或调整参数[[S14]]。

## 与铸造仿真软件的协同关系

### 功能定位差异

Thermo-Calc与主流宏观铸造仿真软件的功能定位存在明确差异[[S31,S34,S3]]：

| 软件类型 | 代表软件 | 核心功能 | 计算尺度 |
|---------|---------|---------|---------|
| 热力学计算工具 | Thermo-Calc | 多元多相平衡相图计算、凝固过程热力学参数输出 | 原子/相尺度 |
| 铸造过程仿真软件 | ProCAST | 基于有限元（FEM）的充型流动、温度场、应力场、缺陷分布宏观仿真 | 宏观铸件尺度 |
| 铸造过程仿真软件 | MAGMAsoft | 三维流动场、温度场、残余应力场分析，显微组织预测、机械性能预测 | 宏观铸件尺度 |

Thermo-Calc不直接开展宏观铸造工艺过程的流固热耦合模拟[[S31]]。

### 协同工作模式

铸造行业常见的配合使用模式为[[S24,S5]]：首先使用Thermo-Calc计算目标合金的全套热物性参数（密度、热焓、固相分数随温度的变化关系、粘度、导热系数等），将导出的参数作为自定义材料库导入ProCAST或MAGMAsoft中，替代软件默认的简化材料参数，可大幅提升后续宏观充型凝固仿真的计算精度，解决通用铸造仿真软件自带材料库针对性不足的问题。

### 同类软件对比

PANDAT与Thermo-Calc同属基于CALPHAD方法的相图热力学计算软件，核心计算原理接近，均用于合金热力学性能计算。两者的主要差异在于：Thermo-Calc数据库覆盖范围更广，针对钢铁、铝镁等有色合金的工业级数据优化程度更高；PANDAT在部分轻合金变温截面相图快速计算场景下有其自身适配性[[S9,S31]]。

## 优势与局限性

### 核心优势

- 基于CALPHAD方法，计算结果热力学自洽性高，可确保体系所有热力学性质之间的内部一致性[[S22]]
- 最多可支持40个组元的多元合金体系热力学计算，适用范围广[[S4]]
- 内置SGTE等经过工业界长期验证的多套专业热力学数据库，覆盖钢铁、铝合金、镍基合金等铸造常用合金体系[[S4,S10]]
- 内置独立的Scheil凝固模拟模块，可直接用于铸造非平衡凝固过程的热力学计算[[S4]]
- 配套DICTRA动力学模块，可补充扩散控制相变过程的模拟能力，扩展在铸造微观偏析、相变动力学场景下的应用范围[[S4]]
- 计算效率优势突出[[S4,S10]]

### 局限性

- 原生Thermo-Calc的纯平衡热力学计算默认基于体系自由能最小的完全平衡假设，对于铸造过程中非平衡快速凝固场景下的溶质截留、亚稳相生成现象，纯平衡计算结果会出现明显预测偏差[[S15,S8]]
- 必须耦合Scheil非平衡凝固模型或对接DICTRA动力学模块才能提升非平衡场景下的预测准确度[[S15,S8]]
- 早期版本操作界面不够友好，入门门槛较高[[S10]]
- 动力学（扩散）数据覆盖范围目前尚不完备[[S10]]

## Sources
- S4: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0986da0d-4799-47f3-8703-0bf0a49c3038/resource) (`0986da0d-4799-47f3-8703-0bf0a49c3038`)
- S22: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8454e805-fe97-4a7c-8302-7e5bd385ae72/resource) (`8454e805-fe97-4a7c-8302-7e5bd385ae72`)
- S36: [ZL201铸造铝合金副车架集成计算初步研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd57db76-9c51-4c88-a691-af2d70fd0bd3/resource) (`fd57db76-9c51-4c88-a691-af2d70fd0bd3`)
- S30: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c17e20e1-cc0c-4fe6-9657-209d49187cfe/resource) (`c17e20e1-cc0c-4fe6-9657-209d49187cfe`)
- S26: [相图计算流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/966d7c43-b24a-41e0-8b39-622fbed12b61/resource) (`966d7c43-b24a-41e0-8b39-622fbed12b61`)
- S10: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b146c32-845c-420d-8374-5d67c175a863/resource) (`4b146c32-845c-420d-8374-5d67c175a863`)
- S27: [计算机在材料热加工工程中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99f02c2d-0499-4091-959c-9846e69f74a8/resource) (`99f02c2d-0499-4091-959c-9846e69f74a8`)
- S1: [Thermo-Calc TCW 软件演示版本主界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02718df5-a605-4410-917f-f2e34f5f4240/resource) (`02718df5-a605-4410-917f-f2e34f5f4240`)
- S12: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5555d85a-8e39-4a47-86a8-b5ea69fb93c5/resource) (`5555d85a-8e39-4a47-86a8-b5ea69fb93c5`)
- S16: [Thermo-Calc软件包结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73ebc2a4-53e4-4e6b-bbbf-6f940329f7d5/resource) (`73ebc2a4-53e4-4e6b-bbbf-6f940329f7d5`)
- S23: [binary systems part 4 binary systems from mn mo to y zr phase diagrams p__a33075e020](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/867d5365-8dbf-4845-9bd5-9288fb1f07c2/resource) (`867d5365-8dbf-4845-9bd5-9288fb1f07c2`)
- S17: [图9-49 Mg-Li系二元合金相图及软件界面功能说明](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76cf6792-be71-4fa7-9bf5-5d463ee64eb9/resource) (`76cf6792-be71-4fa7-9bf5-5d463ee64eb9`)
- S20: [ZL201铸造铝合金副车架集成计算初步研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c57dc84-f6e1-4806-bd41-62e8011f2a2c/resource) (`7c57dc84-f6e1-4806-bd41-62e8011f2a2c`)
- S2: [图3.10 使用Thermo-Calc软件计算不同合金的凝固顺序：(a) 0.7Fe合金；(b) 1.2Fe合金；(c) Al-4.5Cu-0.5Mn-0.5Mg-0.2Si-xFe (x = 0 - 2) 合金的垂直截面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/073fa8c7-1d6f-47c2-8de5-0b55bc3fd4e9/resource) (`073fa8c7-1d6f-47c2-8de5-0b55bc3fd4e9`)
- S29: [图1-6 基于几种常用铝合金流变成形数值模拟结果的液相分数曲线(Thermo-Calc 2019a软件基于Scheil模型)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab7292f9-657c-4119-9c7c-20988927d9b4/resource) (`ab7292f9-657c-4119-9c7c-20988927d9b4`)
- S33: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d37c0b26-2565-4299-913c-4e030936fd92/resource) (`d37c0b26-2565-4299-913c-4e030936fd92`)
- S32: [高强高导铝合金铸造性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb196496-cd1e-4206-88b6-0e5b27f53a9b/resource) (`cb196496-cd1e-4206-88b6-0e5b27f53a9b`)
- S11: [铸造铝合金热裂倾向性检测系统开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4eb01dea-8d62-4e51-8bec-091de5cc5f6b/resource) (`4eb01dea-8d62-4e51-8bec-091de5cc5f6b`)
- S35: [热撕裂与微孔隙预测的计算流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2f4a13a-4888-41dc-a19b-2121d2b31d3a/resource) (`f2f4a13a-4888-41dc-a19b-2121d2b31d3a`)
- S21: [casting alloy design and characterization__2702a787cd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80e95e9a-3f29-46e9-a1bf-1b59bf6fd766/resource) (`80e95e9a-3f29-46e9-a1bf-1b59bf6fd766`)
- S13: [不同方法测定的FM52及Ni合金的固相线与液相线温度对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ca9df33-9a42-42e6-a61e-4848ab20d276/resource) (`5ca9df33-9a42-42e6-a61e-4848ab20d276`)
- S6: [319s合金液相分数与温度、焓的关系（含Thermo-Calc计算与SPSC测量结果）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/229aac7e-cbec-4753-85d6-9a68c2f4beb0/resource) (`229aac7e-cbec-4753-85d6-9a68c2f4beb0`)
- S18: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/773cad9b-d715-4ecc-95d2-a5c4630114c8/resource) (`773cad9b-d715-4ecc-95d2-a5c4630114c8`)
- S28: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5f8d7e8-5abd-4a68-b6b2-0b5303dff872/resource) (`a5f8d7e8-5abd-4a68-b6b2-0b5303dff872`)
- S14: [Thermo-Calc软件中PARROT模块的参数优化流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/648188d0-81cf-426b-af98-9e340dac6fbe/resource) (`648188d0-81cf-426b-af98-9e340dac6fbe`)
- S31: [alloys and metals__72b166ff2a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c457c377-04f7-48f4-bc3f-6898b2590a8e/resource) (`c457c377-04f7-48f4-bc3f-6898b2590a8e`)
- S34: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S3: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07f7190d-9f24-405e-9905-ad286127ca0a/resource) (`07f7190d-9f24-405e-9905-ad286127ca0a`)
- S24: [基于ProCAST的复杂形貌耐热不锈钢薄壁件模拟与工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/868cb457-0490-4d82-96a5-4c930a731aff/resource) (`868cb457-0490-4d82-96a5-4c930a731aff`)
- S5: [稀土镁合金热焓与温度关系的ProCAST和JmatPro计算曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16c063e9-cb5d-4762-bdbe-ab40d6b9d5db/resource) (`16c063e9-cb5d-4762-bdbe-ab40d6b9d5db`)
- S9: [Mg、Si质量比与热处理对压铸Al-Mg-Si-Mn-Cu-Zr合金组织性能影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4156b3bf-fd85-4b1b-a681-cb4b642bcd90/resource) (`4156b3bf-fd85-4b1b-a681-cb4b642bcd90`)
- S15: [金属液态成型原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ce1605f-e468-434d-977a-665dc194987b/resource) (`6ce1605f-e468-434d-977a-665dc194987b`)
- S8: [低合金钢板坯与轧材均质化控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/327595db-9092-4ebc-8e62-8954f580828a/resource) (`327595db-9092-4ebc-8e62-8954f580828a`)