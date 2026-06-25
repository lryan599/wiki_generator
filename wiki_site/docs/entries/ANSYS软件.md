---
version: "v3"
generated_at: "2026-06-18T05:27:46+00:00"
confidence_score: 0.84
confidence_level: "high"
confidence_basis:
  cited_sources: 39
  source_quality_score: 0.83
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

ANSYS软件是美国ANSYS公司研制的大型通用有限元分析（FEA）软件，属于计算机辅助工程（CAE，Computer Aided Engineering）软件范畴 [[S17,S25]]。该软件能与Creo、NASTRAN、Algor、I-DEAS、AutoCAD等多数CAD软件接口实现数据共享和交换，集结构、流体、电场、磁场、声场等多物理场分析于一体 [[S17]]。在机械制造、航空航天、汽车交通、国防军工等数十个工业领域广泛应用，是国际主流的有限元分析仿真工具 [[S3]]。

在压铸领域，ANSYS并非专用的铸造仿真软件，而是作为通用多物理场仿真平台，通过其结构、热、流体等模块的组合运用，承担模具结构强度校核、热平衡分析、热力耦合及型腔耐久性评估等辅助仿真任务 [[S36,S33]]。

**质量认证**：ANSYS是首个通过ISO 9001质量认证的大型分析设计类软件，同时获得美国机械工程师协会（ASME）、美国核安全局（NQA）及近二十种专业技术协会认证的标准分析软件，在中国国内首个通过中国压力容器标准化技术委员会认证 [[S43]]。

## 别名

经行业通用表述验证，符合行业通用习惯的中文别名包括：ANSYS、ANSYS有限元软件、ANSYS有限元模拟软件、ANSYS有限元分析软件、Ansys流固耦合模块 [[S17,S25]]。

经大量工程仿真论文验证，工业领域普遍采用的官方通用英文别名包括：ANSYS、ANSYS Mechanical、ANSYS Fluent、ANSYS Workbench、ANSYS APDL、ANSYS CFX [[S26,S18,S19,S7,S23]]。

## 核心组成与架构

### Workbench 集成环境

ANSYS Workbench是ANSYS公司于2002年随7.0版本推出的集成化工程仿真统一平台，包含三大内置模块 [[S26,S6]]：

| 模块 | 功能 | 说明 |
|---|---|---|
| Design Modeler（DM）| 几何建模 | 可直接建模或从外部CAD导入几何模型，支持参数化设计 [[S6,S46]] |
| Design Simulation（DS）| 仿真计算 | 集成结构、热、流体等分析功能，支持多物理场耦合 [[S6,S19]] |
| Design Explorer（DX）| 优化设计 | 支持参数化优化、拓扑优化及设计空间探索 [[S6]] |

三大模块之间实现参数双向互动调用，可在统一环境下完成多物理场协同仿真 [[S46]]。Workbench平台还支持高性能分布式计算（HPC），相比APDL经典界面更适配批量工业仿真场景 [[S26]]。

### APDL 经典界面

ANSYS APDL（ANSYS Parametric Design Language）经典界面是ANSYS保留的传统命令流操作环境，支持用户通过参数化设计语言完全自定义仿真流程、高度定制复杂仿真逻辑、批量运行重复性计算任务 [[S23]]。在定制化程度高的压铸模具热力耦合分析、复杂多步骤非线性仿真场景中广泛应用 [[S23]]。

### 主要求解器模块

**ANSYS Mechanical 结构求解器**：专注于结构场求解的核心模块，支持结构线性/非线性静力学、动力学、模态分析、谐波响应分析、热-结构耦合等全类型结构相关仿真，内置Python自动化脚本接口可实现批量仿真参数自动设置与结果自动导出 [[S18,S2]]。该模块是压铸模具结构强度校核、型腔应力变形分析的核心求解工具 [[S2]]。

**ANSYS Fluent 流体求解器**：主流通用计算流体动力学（CFD）求解器，遵循确定物理量→几何建模→划分网格→确定物理模型→迭代收敛判断→结果后处理的标准工作流程，支持流体流动、传热、相变等仿真计算 [[S40,S7]]。在压铸场景中可用于金属液充型流态模拟、模具冷却系统流场分析等 [[S4]]。

**ANSYS CFX 流体求解器**：高精度通用流体求解器，主打复杂多物理场耦合流体仿真、旋转机械流体仿真 [[S25]]。

## 前处理模块功能

ANSYS的前处理模块提供完整的材料定义和单元类型选择功能。

**材料模型定义**：支持结构、热、流体等全类别材料属性的设置 [[S42]]。

![ANSYS材料模型定义界面，左侧为已定义材料模型列表，右侧为结构、热、流体等多物理场类别材料模型选项](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc36bffc-b631-44e3-bab8-3b8f2bcf2360/resource)

**单元类型选择**：ANSYS提供涵盖实体单元、壳体单元、梁单元等丰富的单元类型库 [[S14]]，用户可根据分析需求选择相应的单元类型并进行参数配置 [[S13]]。

### 网格划分

ANSYS程序提供四种网格划分方法 [[S2]]：
- **延伸划分**：将二维网格延伸成三维网格
- **映像划分**：将几何模型分解为简单区域后生成映像网格
- **自由划分**：可对复杂模型直接自动划分
- **自适应划分**：基于离散误差自动迭代优化网格

## 在压铸流程中的角色

**重要说明**：ANSYS属于通用多物理场有限元分析软件，内置通用前处理、多物理场求解、后处理模块，**未内置压铸专属仿真模板或专用工艺模块** [[S17]]。所有压铸领域的应用均基于其通用热、结构、流体、多场耦合能力进行二次开发实现，支持通过宏、APDL参数化语言等方式定制压铸场景的专用工作流 [[S3]]。

暂未检索到ANSYS Twin Builder面向压铸全工艺链集成功能的公开明确说明 [[S17]]。

### 具体仿真角色

ANSYS在压铸全流程仿真中的具体角色涵盖多类场景 [[S36,S33]]：

| 仿真类型 | 具体内容 |
|---|---|
| 模具结构强度校核 | 模具型腔应力分析、压室强度评估等 |
| 非稳态瞬态热平衡分析 | 模具温度场多循环模拟、准平衡态判断 |
| 热-结构耦合分析 | 热应力与热变形计算、热疲劳倾向评估 |
| 模具型腔疲劳耐久性评估 | 循环热应力条件下的模具寿命预测 |
| 金属液充型流动CFD仿真 | 基于Fluent的充型流态模拟 |
| 铸件凝固收缩仿真 | 温度场驱动的凝固过程分析 |
| 多场耦合迭代求解 | 电磁场-流场-温度场-应力场联合求解 |

## 压铸应用实例

### 实例一：薄壁压铸件模具温度场仿真

贵州大学2009届硕博论文针对铝合金薄壁盒体、开关盒两类薄壁压铸件的压铸模具温度场开展仿真研究 [[S22,S38]]。

**仿真条件** [[S31,S15]]：
- 铸件材料：铝合金ZAlSi12（ZL102/YL102）
- 模具成型零件：3Cr2W8V耐热钢
- 环境初始温度：25 ℃
- 模具与周围环境换热系数：50 W/(m²·℃)
- 完整压铸生产周期：60 s（30 s开模、40 s取件、50 s喷涂料、60 s合模）
- 建模：Pro/E与ANSYS接口无缝对接

**验证结果**：经热电偶实测验证，多循环仿真结果与实际工况最大误差为10% [[S22]]。模拟得到5次循环后模具温度进入准平衡态 [[S38]]。

**工艺优化**：浇注温度650 ℃、模具预热温度200 ℃时，型腔表面E面区域0~10 s平均升温速率为13.05 ℃/s [[S15]]。

![薄壁类压铸件模具温度场有限元仿真研究中的动模镶块网格划分图，采用Pro/E与ANSYS联合建模后划分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0bfae4d2-00d1-4020-a652-2d399cc8de9e/resource)

### 实例二：H13材质压室流热固耦合仿真

面向H13材质压铸模具的压室流热固耦合仿真，采用第四强度理论进行强度校核，正常工况下压室工作压力设置为70 MPa [[S37]]。通过ANSYS Workbench搭建耦合仿真流程，可准确预测压室的应力集中区域、应力应变的分布和大小，为压室结构改进和强度校核提供理论基础 [[S37]]。

### 实例三：汽车悬架控制臂模具温度仿真

采用CATIA建立实体模型后导出IGES格式导入ANSYS，设置铝合金模具弹性模量70e9、泊松比0.3、传热系数160 W/(m·℃)，空气对流温度22 ℃，通过Smart Size自由网格划分完成前处理 [[S27]]。

### 其他已验证的压铸仿真场景

用户指定的5类压铸相关仿真场景均有公开文献支撑 [[S17]]：
- 钢活塞液锻模具热力耦合分析
- 轿车前门槛压板模态与静力学分析
- 汽车悬架控制臂模具温度分析
- 汽车链条盖有限元分析
- 模具型腔应力与变形分析

## 压铸应用操作流程与参数要求

### 典型操作流程

ANSYS面向压铸模具分析的典型操作流程一般包含7个核心步骤 [[S1,S35]]：
1. 三维模型导入与几何修复
2. 分区域非均匀网格划分
3. 材料属性自定义赋值
4. 不同部件接触对定义与界面换热系数设置
5. 工艺边界条件配置
6. 多物理场求解器耦合设置
7. 结果后处理与缺陷预测

### 网格划分要求

压铸仿真中ANSYS网格划分推荐标准 [[S1]]：

| 区域 | 网格尺寸要求 |
|---|---|
| 充型湍流核心区域、壁厚<3mm薄壁铸件 | 0.5~2 mm |
| 模具型腔工作面 | 2~5 mm |
| 模具外部非工作区域 | 5~15 mm |

所有网格雅可比系数需大于0.7，避免负体积网格导致求解发散 [[S1]]。

### 界面换热系数推荐值

压铸场景下ANSYS通用接触设置推荐规则 [[S35]]：

| 接触界面 | 界面换热系数 [W/(m²·K)] |
|---|---|
| 模具分模面之间 | 1000~2000 |
| 铸件与模具工作面之间 | 800~1500 |
| 铸件与空气之间 | 5~20 |
| 铸件与喷涂隔热层之间 | 50~100 |

## 材料库支持

ANSYS内置通用材料库原生包含H13（4Cr5MoSiV1）热作模具钢以及A356、A380、6061、ADC12等主流压铸铝合金的基础力学和热物理参数 [[S11,S10,S9]]。但无压铸专属的凝固潜热、固相率-温度变化曲线、高温流变参数等专属物性数据，需要用户基于实测数据或专业铸造材料数据库补充定义 [[S10,S9]]。

## 多物理场耦合能力

ANSYS作为通用多物理场仿真平台，可实现电磁场、流场、温度场、结构应力场的多场耦合求解 [[S4,S41]]。其应力计算默认集成Anand流变本构模型，适配压铸过程大温度跨度下的力学行为计算 [[S41]]。

## 优势与局限

### 优势

| 优势项 | 说明 |
|---|---|
| 多物理场耦合能力 | 支持结构-热-流体-电磁的多场耦合，适配压铸模具热力耦合等复杂场景 [[S4]] |
| 定制开发自由度 | 开放UDF、APDL以及丰富的外部接口，支持自定义凝固相变模型、修正界面换热系数、扩展材料数据库 [[S4]] |
| 仿真精度 | 经热电偶实测验证，温度场仿真与实测最大误差10%以内 [[S22]] |
| 集成化工作环境 | Workbench提供统一的仿真平台，支持参数化建模优化和CAD双向参数互通 [[S26,S19]] |
| 质量认证 | 首个通过ISO 9001认证的CAE软件，获多项行业权威认证 [[S43]] |

### 局限

| 局限项 | 说明 |
|---|---|
| 无压铸专用模块 | 原生缺乏面向铸造场景的集成多相流-相变-溶质迁移耦合求解框架 [[S21]] |
| 复杂界面换热支持不足 | 对压铸过程中复杂界面换热系数的专用求解模块原生支持不足 [[S21]] |
| 高温物性数据缺失 | 无压铸专属的凝固潜热、固相率-温度变化曲线等专属数据 [[S9,S10]] |
| 计算资源需求高 | 多模块耦合求解时需同时加载多个求解器，同等仿真规模下内存、CPU资源需求显著高于ProCAST等专用铸造软件 [[S39]] |
| 操作复杂度 | 需要用户自行完成多模块拼接与自定义参数配置，学习曲线陡峭 [[S17]] |

## 与其他压铸仿真软件对比

主流压铸CAE软件对比 [[S20,S32,S5]]：

| 对比维度 | ANSYS | ProCAST | MAGMA | ABAQUS |
|---|---|---|---|---|
| 软件定位 | 通用多物理场平台 | 铸造专用仿真 | 铸造专用仿真 | 通用结构仿真 |
| 数值方法 | 有限元法（FEM）| 有限元法（FEM）| 有限差分法（FDM）| 有限元法（FEM）|
| 网格剖分 | 自由/映像/自适应划分 | 非均匀网格剖分 | 有限差分网格 | 结构化/非结构化 |
| 压铸预置流程 | 无原生预置流程 | 内置全流程仿真模块 | 模块化程度高 | 无铸造专用流程 |
| 热力学数据库 | 通用材料库 | 开放热力学数据库，支持合金成分自动生成相图参数 | 铸造专用数据库 | 通用材料库 |
| 压铸仿真效率 | 需多模块拼接 | 标准化流程，效率较高 | 薄壁件仿真效率高 | 多用于热疲劳/残余应力专项分析 |
| 定制扩展性 | APDL/UDF高度可定制 | 用户子程序 | 中等 | 用户子程序 |

## 主流版本

2015-2023年面向制造业的主流ANSYS版本中，压铸/模具制造行业普及率较高的版本包括 [[S30,S16,S24,S26]]：
- ANSYS R15
- ANSYS R19.2
- ANSYS 2021 R1
- ANSYS 22.0

上述版本广泛用于模具温度场、结构强度、充型流态等压铸工艺仿真研究场景。

## Sources
- S17: [1281099_ansys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61b7c678-6bb0-4c95-8891-8c60c5a1384d/resource) (`61b7c678-6bb0-4c95-8891-8c60c5a1384d`)
- S25: [1281099_ansys__Ansys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8405ebc5-8273-42f8-a0e7-6f3b0b2b125c/resource) (`8405ebc5-8273-42f8-a0e7-6f3b0b2b125c`)
- S3: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/038874bd-8412-4b37-9eef-989c95b6ca21/resource) (`038874bd-8412-4b37-9eef-989c95b6ca21`)
- S36: [薄壁类压铸件模具温度场的有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6e09269-5b06-4266-b080-8b067e6145f4/resource) (`a6e09269-5b06-4266-b080-8b067e6145f4`)
- S33: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99e902e5-33f8-421c-b5af-6561c1aabfb3/resource) (`99e902e5-33f8-421c-b5af-6561c1aabfb3`)
- S43: [大型复杂镁合金压铸件的应力分析数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de95054b-e58a-4819-8fe7-73744e37f19a/resource) (`de95054b-e58a-4819-8fe7-73744e37f19a`)
- S26: [锡电解阳极立模浇铸水冷系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8b325dd7-31e2-4678-93b8-85cf2642f036/resource) (`8b325dd7-31e2-4678-93b8-85cf2642f036`)
- S18: [锻造时压力机应变场与模具温度场的数字重构研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68281582-fe15-46ac-bf1f-eed8dbabe15a/resource) (`68281582-fe15-46ac-bf1f-eed8dbabe15a`)
- S19: [铝合金减震塔压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b8f9520-f9ad-44be-a8ed-7ee601548a64/resource) (`6b8f9520-f9ad-44be-a8ed-7ee601548a64`)
- S7: [图6.12 (b) 平纹织物边缘纱线脱落后单胞模型X方向渗透率预测的速度分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a9f628b-f99c-4eac-a665-c57a3e132975/resource) (`0a9f628b-f99c-4eac-a665-c57a3e132975`)
- S23: [图4.5 联合仿真流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e39fd82-09c4-41e0-99ab-7276492c0540/resource) (`7e39fd82-09c4-41e0-99ab-7276492c0540`)
- S6: [发动机叶片工程应用分析优化加书签](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/097fae4a-2eb4-4145-a7a3-a2b9a217737c/resource) (`097fae4a-2eb4-4145-a7a3-a2b9a217737c`)
- S46: [发动机叶片工程应用分析优化加书签](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f22de8fc-6442-4320-a643-0ba459011fd9/resource) (`f22de8fc-6442-4320-a643-0ba459011fd9`)
- S2: [大型复杂镁合金压铸件的应力分析数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00c678cb-3ce9-4911-84f1-8694cbb8531c/resource) (`00c678cb-3ce9-4911-84f1-8694cbb8531c`)
- S40: [图 2.1 Fluent 软件工作流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c098f431-70c8-49e7-8563-8a4c1eecdbcc/resource) (`c098f431-70c8-49e7-8563-8a4c1eecdbcc`)
- S4: [ZK61镁合金大型铸锭半连续铸造成形工艺与组织调控机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04400e78-81af-4158-a4ea-2103aab1b5e8/resource) (`04400e78-81af-4158-a4ea-2103aab1b5e8`)
- S42: [ANSYS定义材料模型行为对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc36bffc-b631-44e3-bab8-3b8f2bcf2360/resource) (`dc36bffc-b631-44e3-bab8-3b8f2bcf2360`)
- S14: [ANSYS单元类型选择窗口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49e0dd8a-e33c-4f94-967a-8c99d1ffb5d5/resource) (`49e0dd8a-e33c-4f94-967a-8c99d1ffb5d5`)
- S13: [ANSYS单元类型定义对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49afadcf-15f7-44ff-a2dd-747938b440a7/resource) (`49afadcf-15f7-44ff-a2dd-747938b440a7`)
- S22: [薄壁类压铸件模具温度场的有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77a0bdbc-ec2d-4cac-9204-a6a35e484abd/resource) (`77a0bdbc-ec2d-4cac-9204-a6a35e484abd`)
- S38: [薄壁类压铸件模具温度场的有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8e1029a-406c-44f8-b2fb-3e1d7d739501/resource) (`b8e1029a-406c-44f8-b2fb-3e1d7d739501`)
- S31: [薄壁类压铸件模具温度场的有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95b1aecb-1f18-4af5-8640-1c9fc3703be1/resource) (`95b1aecb-1f18-4af5-8640-1c9fc3703be1`)
- S15: [薄壁类压铸件模具温度场的有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a545594-637e-47b1-bdf2-16fdcdf7f49e/resource) (`4a545594-637e-47b1-bdf2-16fdcdf7f49e`)
- S37: [压铸机压室在流热固耦合下的传热与变形分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a81fe9b7-cf43-4c8a-b9cf-cfb1c08ae18f/resource) (`a81fe9b7-cf43-4c8a-b9cf-cfb1c08ae18f`)
- S27: [汽车悬架控制臂模具设计及温度分析研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8b6dc5cd-a5f1-43e7-a83f-9c95573cfee1/resource) (`8b6dc5cd-a5f1-43e7-a83f-9c95573cfee1`)
- S1: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00ba3675-940d-4315-a753-0de69beef2a6/resource) (`00ba3675-940d-4315-a753-0de69beef2a6`)
- S35: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1a53deb-94cb-46cd-9906-31cf334a2897/resource) (`a1a53deb-94cb-46cd-9906-31cf334a2897`)
- S11: [5368567_H13钢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b0c8af7-a5cd-452e-b2be-ceb4c50ca11f/resource) (`3b0c8af7-a5cd-452e-b2be-ceb4c50ca11f`)
- S10: [表3.1 A356与H13材料属性](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27a6c817-b476-455b-9d8b-70667542e639/resource) (`27a6c817-b476-455b-9d8b-70667542e639`)
- S9: [H13与A380材料的化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22372649-efcc-4d22-98ac-213979cc6b4c/resource) (`22372649-efcc-4d22-98ac-213979cc6b4c`)
- S41: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd9e9abf-ce13-4b30-b358-fa22c58ebd64/resource) (`cd9e9abf-ce13-4b30-b358-fa22c58ebd64`)
- S21: [基于冶金冲刷固液相变的三传耦合模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d85f0f9-801d-4e6a-9bdb-0260d180b89c/resource) (`6d85f0f9-801d-4e6a-9bdb-0260d180b89c`)
- S39: [advanced materials processing and manufacturing processes__410843daa8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc548cac-ac3a-4d3d-89d5-186c94cee33f/resource) (`bc548cac-ac3a-4d3d-89d5-186c94cee33f`)
- S20: [表5-2 压铸CAE功能对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bfcfc6a-4f80-4ed1-b79a-b5451b8c2d41/resource) (`6bfcfc6a-4f80-4ed1-b79a-b5451b8c2d41`)
- S32: [表1.2 国内外主流使用铸造软件[43]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98dd3bca-962a-49d8-9d47-d25b3afeb03f/resource) (`98dd3bca-962a-49d8-9d47-d25b3afeb03f`)
- S5: [铝合金水泵座压铸模浇注系统及镶块随形水道设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09448fc3-1210-4b74-8f48-823f39384616/resource) (`09448fc3-1210-4b74-8f48-823f39384616`)
- S30: [h=18mm时异形包装件薄膜厚度分布热力图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/934c998e-065d-4f8c-af6d-cf33841ed4c2/resource) (`934c998e-065d-4f8c-af6d-cf33841ed4c2`)
- S16: [8MPa充型压力下T型件预制体束内间隙充型模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ab6c297-dd9d-4f8d-ab27-fd67ab99b916/resource) (`4ab6c297-dd9d-4f8d-ab27-fd67ab99b916`)
- S24: [advanced materials in engineering applications__0b40dace28](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e9e2cd2-553e-4049-ad07-18c42ccfacd9/resource) (`7e9e2cd2-553e-4049-ad07-18c42ccfacd9`)