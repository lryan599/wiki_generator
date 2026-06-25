---
version: "v1"
generated_at: "2026-06-18T11:44:37+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.85
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

Flow-3D是一款通用计算流体动力学（CFD）软件，由美国Flow Science, Inc.开发，1985年正式民用商业化发布 [[S21,S45,S15,S7]]。其开发商由VOF（流体体积）方法的原始开发者之一C.W.（Tony）Hirt博士于1980年创立 [[S7]]。在铸造仿真领域，Flow-3D的核心优势是基于VOF算法可高精度模拟自由液面流动，尤其适配压铸过程中金属液高速充型的复杂流态场景 [[S32,S7,S44]]。

Flow-3D并非专用于压铸，其铸造仿真覆盖范围包括砂型铸造、金属型铸造、低压铸造、高压铸造（压铸）、消失模铸造、离心铸造、熔模铸造、壳型铸造、半固态铸造、倾斜浇注等全品类铸造工艺 [[S21,S45,S15]]。

**官方商标与别名**：Flow-3D的官方注册商标写法为带注册商标符号的全大写“FLOW-3D®” [[S13]]。行业通用的非正式别名包括“Flow 3D”（无连字符）、“Flow-3D铸造模拟软件”、“FLOW-3D仿真软件”等，均非官方正式命名 [[S39]]。“FLOWD”在Flow Science官方资料及行业记载中不存在，属于输入笔误 [[S13]]。**OpenFOAM与Flow-3D为完全独立的两款软件**——Flow-3D为商业闭源软件，OpenFOAM为开源免费CFD工具箱，二者从底层代码体系完全无关 [[S9,S28]]。

## 产品线与模块

Flow-3D存在并行两条产品线：面向全行业通用CFD仿真的通用版，以及专门面向铸造行业用户优化的铸造专用版FLOW-3D CAST [[S7,S26,S12]]。

| 模块/组件 | 功能描述 | 来源 |
|-----------|---------|------|
| Flow-3D/MP（并行计算模块） | 内置多处理器并行计算功能，支持多核心运算提升仿真效率 | [[S45]] |
| FLOW-VU（后处理工具） | 支持2D/3D可视化输出仿真结果（速度场、压力场、温度场等）、生成充型过程动画、支持指定坐标点数据提取与后处理分析 | [[S45,S4]] |
| 材料数据库 | 提供五十多种铸件和十几种铸型材料数据库 | [[S21]] |

Flow-3D 9.0版本为重要迭代，新增了六自由度运动物体模型、空气夹带模型、温度应力与变形模型、微观缩松预测模型，同时优化了原有数值算法 [[S21]]。

## 核心功能与技术原理

### 数值方法与自由表面追踪

Flow-3D采用FDM/FVM（有限差分/有限体积混合）数值框架 [[S9,S36,S10]]。其核心自由表面追踪采用自研TrueVOF（Volume of Fluid）算法，通过定义流体体积分数α（0代表全气相、1代表全液相、0<α<1代表气液交界面）实现动态自由液面追踪，支持金属液高速充型过程中界面聚合、飞溅等复杂行为的精确求解 [[S19,S41,S36,S44]]。

### FAVOR™网格技术

Flow-3D独有FAVOR™（Fractional Area/Volume Obstacle Representation，分数面积/体积障碍物表示）网格技术，通过预处理器计算几何与网格相交形成的流体可流通体积分数、三维方向流通面积分数，将其直接嵌入流体控制方程，实现无贴体矩形网格下的复杂几何精确表征 [[S14,S19,S32,S17]]。

FAVOR技术的核心优势包括：
- 无需对曲面几何进行复杂贴体网格划分，仅用少量矩形网格即可获得远高于传统FDM方法的几何表征精度，网格生成简便、计算效率更高 [[S14,S19,S45]]
- 支持嵌套局部加密网格对薄壁区域做高精度剖分，相邻不同尺寸网格需保持2:1的对齐比例以降低计算误差 [[S19]]
- 仅当特征尺寸小于当前网格尺寸时会出现识别偏差，可通过提升局部网格分辨率修正 [[S19]]

![FAVOR技术划分的球形模型网格效果图，直观展示规则矩形网格下对曲面几何的近似表征效果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d08cc79-86f9-449a-848c-c2943b7df2d9/resource)

### 多物理场耦合

Flow-3D支持流动场、温度场、传热、凝固过程、湍流、表面张力、凝固区域热应力演化的全耦合求解 [[S7,S38,S45]]。内置模型支持自动计算模具冷却通道的努塞尔数Nu，分别适配湍流区（10⁴<Re<5×10⁶，0.5<Pr<1.5）和层流区管道传热 [[S38,S7,S45]]。

### 压铸缺陷预测模型

Flow-3D内置气泡空蚀模型、表面缺陷追踪、氧化渣追踪、二元合金偏析、缩松模型。通过对温度梯度G、冷却速率R的实时计算等效实现Niyama判据（Ny=G/√R）对缩孔缩松缺陷的预测功能，支持含气量/卷气缺陷的全过程追踪 [[S38,S44,S30]]。此外还具有独特的表面缺陷/氧化膜卷入追踪模型 [[S45,S44,S17]]。

## 在压铸工艺中的应用

### 压铸充型与缺陷预测

Flow-3D可针对压射套筒内的合金流动过程进行仿真设置，用户可自由定义压室充满度、多级压射速度、快慢速转换位置等参数，精准模拟压室内部金属液流动状态。相关研究验证：当慢压射速度0.2m/s、快压射速度3.5m/s、高低速压射切换点设置为560mm时，模流平稳度最高，卷气概率最低，铸件内部组织致密性和力学性能显著提升 [[S3,S43]]。

Flow-3D支持模拟的压铸物理过程包括 [[S45,S38,S17]]：
- 压射室多级速度/变速位置任意设定的金属液充型过程
- 型腔背压、排气效果模拟
- 卷气气泡/空化气泡追踪
- 氧化夹杂/冷隔缺陷生成演化过程
- 凝固收缩过程模拟，缩孔缩松演化模拟
- 模具热循环与温度分布计算，热应力演化分析
- 冷却通道热交换参数自动计算

### 冷却水道优化

Flow-3D可支持压铸模具温度场热循环全过程仿真，通过对冷却水道的参数化建模，精确计算不同水道布置下模具整体温度分布、冷却速率差异，辅助完成水道结构优化，改善模温均匀性，减少铸件局部热积导致的粘模拉伤、缩松缺陷，最终缩短压铸生产循环周期 [[S3]]。

### 仿真效率

2026年公开研究显示，采用Flow-3D开展铝合金壳体压铸过程模拟的单样本平均计算耗时低于11秒，仿真效率较同类压铸仿真软件提升30%以上，可支撑快速工艺迭代需求 [[S20]]。

## 与同类铸造仿真软件对比

### 主流铸造仿真软件概览

| 软件 | 开发商 | 国别 | 数值方法 | 核心定位 | 来源 |
|------|--------|------|----------|---------|------|
| Flow-3D | Flow Science, Inc. | 美国 | FDM/FVM | 通用CFD衍生，自由液面高速流动高精度模拟 | [[S1,S42,S3,S27]] |
| MAGMASOFT | MAGMA GmbH | 德国 | FDM | 全铸造工艺专用，模块化程度极高 | [[S1,S42]] |
| ProCAST | ESI Group | 法国（原美国） | FEM | 有限元法专用，应力/变形/多工艺适配 | [[S1,S42]] |
| AnyCasting | AnyCasting Co. | 韩国 | FDM | 轻量化易用型，快速充型凝固计算 | [[S1,S42]] |
| NovaFlow&Solid | NovaCast | 瑞典 | — | 高端精密铸造，微观组织与流场耦合 | [[S1]] |

### 核心优劣势对比

| 维度 | Flow-3D | MAGMASOFT | ProCAST | AnyCasting |
|------|---------|-----------|---------|------------|
| 高速充型流态精度 | ★★★★★（独有VOF+FAVOR） | ★★★ | ★★★ | ★★★ |
| 残余应力/变形分析 | 附加模块，成熟度较低 | 中等 | ★★★★★（FEM优势） | 基础支持 |
| 微观组织预测 | 附加模块 | ★★★★★ | ★★★★ | 基础支持 |
| 操作易用性 | 使用通用技术名词，学习曲线陡峭 | 模块化铸造术语 | 中等 | ★★★★★（操作门槛低） |
| 计算资源消耗 | 网格加密时数量指数级上升 | 中等 | 中等 | 较快 |

来源：[[S5,S42,S3,S44,S3,S6]]

### 市场定位

在国内压铸仿真市场，Flow-3D份额明显低于MAGMASOFT和ProCAST，高于NovaFlow&Solid。市场受众以高校流体方向研究团队、头部压铸企业的高速充型专项优化部门为主 [[S23]]。

## 局限性

1. **学习曲线陡峭**：操作界面采用通用流体力学专业术语而非铸造行业专用术语，缺乏针对压铸场景的一键式向导和标准化预设模板，新用户需要掌握大量流体力学相关知识 [[S3,S6]]

2. **网格敏感性**：采用结构化矩形网格搭配FAVOR切割技术，网格尺寸选择直接影响自由液面模拟精度。局部薄壁区域网格加密时总网格数量会指数级上升，大尺寸整车结构类压铸件的全流程仿真计算耗时较长 [[S32]]

3. **多相流模型精度局限**：虽然自由液面单相流动精度很高，但针对多相多组分的气-渣-金属液三相耦合计算的精度不如专用铸造仿真软件。残余应力、铸件大变形、微观组织演化的仿真功能属于附加模块，成熟度不及MAGMASOFT和ProCAST的对应模块，不适合以高精度应力/微观组织预测为核心目标的压铸场景 [[S7,S5]]

## 行业认可与应用案例

### 中国市场与代理

2008年美国Flow Science公司在上海设立Flow-3D中国分公司，该软件在中国大陆及港澳台地区压铸领域已实现长期商业化落地应用。上海析模计算机科技有限公司为其官方授权代理之一 [[S32,S24]]。

### 学术与工程应用

- 国内多所高校（大连交通大学、重庆理工大学、合肥工业大学、盐城工学院等）压铸相关研究团队2016—2026年间均采用Flow-3D开展压铸充型缺陷预测、工艺参数优化类研究，覆盖汽车零部件、消费电子类压铸件的仿真验证场景 [[S7,S33,S31]]。
- 国内权威压铸行业手册《压铸技术与生产》《压铸成形工艺与模具设计》《压铸模具典型结构图册》等均将Flow-3D列为国内压铸行业主流商用仿真软件 [[S3,S45,S21]]。
- 核心VOF算法源自美国洛斯阿拉莫斯国家实验室，已获得NASA超音速喷嘴设计、美国海军舰艇油系统设计等官方工程场景验证，在压铸领域的仿真精度已得到行业广泛认可 [[S21]]。

### 典型研究案例

- **2019年**：《基于Flow-3D的铝合金铸件低压铸造卷气行为》发表于《特种铸造及有色合金》，核心结论为采用Flow-3D的卷气预测模型可准确识别铝合金充型过程中气体卷入的位置和体积，为低压铸造排气系统优化提供仿真依据 [[S31]]。
- **2022年**：高校学位论文《前油封端盖压力铸造工艺与缺陷研究》采用Flow-3D开展铝合金油封端盖压铸过程仿真，通过预测充型和凝固阶段的缺陷分布，结合X射线检测验证，优化后工艺方案可有效降低铸件孔隙率，提升成品合格率 [[S7]]。
- 国内用户已使用Flow-3D完成镁铝合金大型复杂压铸件充型过程模拟，通过追踪卷气和自由表面缺陷分布，优化浇注系统结构，确定合理的充型速度、充型温度、模具预热温度等工艺参数 [[S18]]。

### 标准引用

遍历公开可查的ISO、ASTM、GB等国内外铸造相关标准文本，未发现直接指定Flow-3D作为压铸仿真唯一或指定工具的强制条款。现有通用铸造标准仅规定性能测试、工艺通用要求，不绑定特定商业软件 [[S8,S35]]。

## 相关图示

### 基础操作流程

![Flow-3D操作基本流程示意图，展示从创建工作文件、导入STL、网格划分到模拟运算及结果分析的完整环节](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/883fdef8-151a-467c-a927-06e48ba37e45/resource)

该流程图展示了Flow-3D从创建项目到完成结果后处理的全操作步骤，覆盖STL导入、网格划分、多类参数配置、求解运算的所有环节 [[S25]]。

## Sources
- S21: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/749d0b51-3857-4a91-9926-d67f29bd8056/resource) (`749d0b51-3857-4a91-9926-d67f29bd8056`)
- S45: [压铸成形工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa653782-48b3-45b0-b066-21a80e9c2568/resource) (`fa653782-48b3-45b0-b066-21a80e9c2568`)
- S15: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58ea8fb5-232c-48b4-9a7c-03034cd5c0bd/resource) (`58ea8fb5-232c-48b4-9a7c-03034cd5c0bd`)
- S7: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/253c6116-36e9-40db-a180-a738c4ae692b/resource) (`253c6116-36e9-40db-a180-a738c4ae692b`)
- S32: [铝合金套筒低压铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad069a84-7504-476e-9a87-37a9f7957175/resource) (`ad069a84-7504-476e-9a87-37a9f7957175`)
- S44: [铝合金发动机缸体低压铸造缺陷控制的工艺及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f82ab5e7-0c83-41cf-95b3-afe7c46ee0a5/resource) (`f82ab5e7-0c83-41cf-95b3-afe7c46ee0a5`)
- S13: [casting an analytical approach engineering materials and processes__4c01099d6c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4aa217e4-71a1-4359-ad5b-073a183c4014/resource) (`4aa217e4-71a1-4359-ad5b-073a183c4014`)
- S39: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4741781-c2bd-47b6-89cb-29a6b409102a/resource) (`c4741781-c2bd-47b6-89cb-29a6b409102a`)
- S9: [表1-2 常用商业软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c158da6-fa99-4987-9598-4700db4b2a6f/resource) (`2c158da6-fa99-4987-9598-4700db4b2a6f`)
- S28: [ACE液液分层流动CFD模拟研究参数对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/931642f8-13fa-47d5-8f94-ec696c3b06f2/resource) (`931642f8-13fa-47d5-8f94-ec696c3b06f2`)
- S26: [die filling behaviour of semi solid a356 al alloy slurry during rheo pre__109c153787](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ce7b2b4-4d39-4c42-a99a-9cb198d991b9/resource) (`8ce7b2b4-4d39-4c42-a99a-9cb198d991b9`)
- S12: [空压机用铝合金阀盖件的低压铸造工艺开发及模拟优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e634a0b-e008-4678-84e0-f2ab194cc209/resource) (`3e634a0b-e008-4678-84e0-f2ab194cc209`)
- S4: [asme asme 2014 12th biennial conference on engineering systems design an__a15afb75a5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/164ea6d5-29bf-48e9-aa56-ef506645311f/resource) (`164ea6d5-29bf-48e9-aa56-ef506645311f`)
- S36: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd3925b0-a710-464c-8658-7e1a047df7b8/resource) (`bd3925b0-a710-464c-8658-7e1a047df7b8`)
- S10: [casting an analytical approach engineering materials and processes__4c01099d6c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38b7c47f-9b7d-44f9-8723-601243db06c0/resource) (`38b7c47f-9b7d-44f9-8723-601243db06c0`)
- S19: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69505a7b-549e-4f04-b2ed-1458f5808d4e/resource) (`69505a7b-549e-4f04-b2ed-1458f5808d4e`)
- S41: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cebf24c0-955e-4e04-a8bf-1cead4723270/resource) (`cebf24c0-955e-4e04-a8bf-1cead4723270`)
- S14: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bd5b67b-bc75-4609-8a08-252e25bf7148/resource) (`4bd5b67b-bc75-4609-8a08-252e25bf7148`)
- S17: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f16a007-fb87-48e2-bdcb-0e4d410a93bb/resource) (`5f16a007-fb87-48e2-bdcb-0e4d410a93bb`)
- S38: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0d64694-bf0f-4e97-9b7f-24b2a007420c/resource) (`c0d64694-bf0f-4e97-9b7f-24b2a007420c`)
- S30: [ADC12铝合金真空压铸充型过程及铸件性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ae35fda-325c-4b64-9824-7989bc7c5e45/resource) (`9ae35fda-325c-4b64-9824-7989bc7c5e45`)
- S3: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/112a7bab-6f8f-48c8-8749-731180dc6620/resource) (`112a7bab-6f8f-48c8-8749-731180dc6620`)
- S43: [基于ProCAST的汽车铝合金机油泵体压铸模具开发及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5b2e7dd-667f-4e5e-9864-34d89caf73f4/resource) (`f5b2e7dd-667f-4e5e-9864-34d89caf73f4`)
- S20: [表 4 不同压铸模拟对样本试件模拟平均耗时分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71d0721d-0be9-4c29-93b5-52c552ecf862/resource) (`71d0721d-0be9-4c29-93b5-52c552ecf862`)
- S1: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b5d9a2f-5f00-4c24-bd19-d6a230eedea0/resource) (`0b5d9a2f-5f00-4c24-bd19-d6a230eedea0`)
- S42: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S27: [实用压铸模设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d415fd7-31a1-4c43-83ba-5a550df794ad/resource) (`8d415fd7-31a1-4c43-83ba-5a550df794ad`)
- S5: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848/resource) (`1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848`)
- S6: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20c5b741-703b-4565-bfac-711142bfd43f/resource) (`20c5b741-703b-4565-bfac-711142bfd43f`)
- S23: [TC4合金非对称翼型受油管熔模精密铸造工艺及凝固特性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8385eca2-3951-4e3d-a470-d4cedcd6d253/resource) (`8385eca2-3951-4e3d-a470-d4cedcd6d253`)
- S24: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/85cc7da7-93d4-42d8-81c7-1cf3210bea66/resource) (`85cc7da7-93d4-42d8-81c7-1cf3210bea66`)
- S33: [执手多型腔压铸工艺及模具优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad27d26f-c0f7-40f3-bc3a-262bed5164db/resource) (`ad27d26f-c0f7-40f3-bc3a-262bed5164db`)
- S31: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a061f7a9-dbbb-463f-b5ab-62b86b0f7c17/resource) (`a061f7a9-dbbb-463f-b5ab-62b86b0f7c17`)
- S18: [铝合金发动机缸体低压铸造缺陷控制的工艺及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/682f1d14-a7ab-4b82-8fc5-c02626a5a88a/resource) (`682f1d14-a7ab-4b82-8fc5-c02626a5a88a`)
- S8: [casting copper base alloys__d5182d5c2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27965a22-9b1c-434e-8c96-71db97cd78c2/resource) (`27965a22-9b1c-434e-8c96-71db97cd78c2`)
- S35: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/babd7e04-c49d-4201-94cc-734f31ac963f/resource) (`babd7e04-c49d-4201-94cc-734f31ac963f`)
- S25: [Flow-3D操作基本流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/883fdef8-151a-467c-a927-06e48ba37e45/resource) (`883fdef8-151a-467c-a927-06e48ba37e45`)