---
version: "v1"
generated_at: "2026-06-18T11:46:47+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 39
  source_quality_score: 0.83
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

ProCAST 是由法国 ESI 集团开发的基于有限元法（FEM）的专业铸造过程数值模拟商业 CAE 软件，能够实现铸造过程中流场、温度场、应力场的完全耦合求解，覆盖砂型铸造、高压铸造、低压铸造、熔模铸造、离心铸造、消失模铸造等几乎所有主流铸造工艺，支持钢、铁、铝基、铜基、镁基、镍基、钛基、锌基等全系列合金材质的模拟分析[[S8,S30,S7]]。该软件在行业内亦常被非正式地写作 PROCAST 或 Pro-CAST，而 PorCast、Pro CAST、Pro Cast 等均为拼写错误或非规范拆分写法，不属于官方认可别名[[S16,S18]]。

ProCAST 适用于砂型铸造、消失模铸造、高压铸造、低压铸造、重力铸造、倾斜浇铸、熔模铸造、壳型铸造、挤压铸造、触变铸造、触变成形、流变铸造。由于采用了标准化、通用的用户界面，任何一种铸造过程都可以用同一软件包进行分析和优化。它可以用来研究设计结果，例如浇注系统、出气孔和溢流孔的位置，冒口的位置和大小等[[S7]]。

![图：ProCAST 全模块组成架构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/506caaa6-d2bd-47a8-82db-154528965eb8/resource)

ProCAST 可分析缩孔、裂纹、裹气、冲砂、冷隔、浇不足、应力、变形、模具寿命、工艺开发及可重复性等[[S8]]。其核心代码最初由美国团队主导开发，1990 年后瑞士洛桑 Calcom SA 公司与瑞士联邦科技研究院加入，主导开发晶粒计算模块和反向求解模块；2002 年 ProCAST 整体并入法国 ESI 集团，重组为美国马里兰州的 ProCAST Inc. 和瑞士洛桑的 Calcom ESI，后续整合 ESI 原有热物理仿真产品线（PAM-CAST、SYSWELD 等）形成完整的铸造热物理综合解决方案[[S8]]。

## 核心功能与模拟能力

ProCAST 针对铸造过程进行流动—传热—应力耦合分析，主要由 8 个可独立选择启用的功能模块组成[[S26,S48]]：

| 模块类别     | 模块名称                                                          | 主要功能说明                                                                                                                |
| ------------ | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **标准模块** | 传热分析及前后处理模块（Base License）                            | 用于传热计算并包含所有前后处理功能，使用热焓方程式计算液相和固相转变过程中的潜热[[S23]]                                     |
| **标准模块** | 流动分析模块（Fluidflow）                                         | 通过完全 Navier-Stokes 流动方程对流体流动和传热进行耦合计算，可模拟湍流、触变行为及多孔介质流动[[S12,S23]]                   |
| **工具模块** | 有限元网格划分模块（MeshCAST）                                    | 先生成表面网格，再基于合格的面网格生成四面体体积网格，支持针对不同仿真区域差异化设置网格尺寸[[S16,S40,S27]]               |
| **工具模块** | 反向求解模块（Inverse）                                           | 利用实际测温数据反算边界条件和材料热物理性能，最大限度地提高模拟结果的可靠性[[S12,S42]]                                    |
| **高级模块** | 显微组织分析模块（Micromodel）                                    | 定性分析和定量计算固相转变，支持等轴晶模型、包晶/共晶转变模型，内置 Fe-C 合金专用模型适配铸铁、铸钢件微观组织仿真[[S12,S42]] |
| **高级模块** | 晶粒结构模块（CA-FE）                                             | 基于元胞自动机方法模拟充型完成后晶粒的形核与生长过程[[S12]]                                                                |
| **附加模块** | 应力分析模块（Stress）                                            | 以位移法为基础求解控制方程，支持弹性、弹塑性、热弹塑性多种力学模型，可预测铸件残余应力分布与变形量[[S12,S22]]               |
| **附加模块** | 热辐射分析模块（Radiation）                                       | 精准计算辐射角系数和阴影效应，适配镍基等高温合金熔模铸造的仿真需求[[S12,S33]]                                              |

普通常规使用只需配置前后处理与网格划分、传热、流动、应力模块即可[[S26,S48]]。

![图：ProCAST 软件功能模块架构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b96a1fe5-8e24-4a13-beff-73f17863883b/resource)

**缺陷预测能力方面**，ProCAST 支持采用 FEEDLEN 判据和 Niyama 判据组合预测缩孔、缩松缺陷，内置 Hot Tearing Indicator 热裂倾向分析功能模块，同时可识别冷隔、浇不足、裹气、冲砂、冷偏析、气包等常见铸造缺陷，还可辅助预测压铸模具的热疲劳寿命[[S16,S3,S5,S9]]。

## 技术原理与输入输出

**数值方法**：ProCAST 底层数值方法明确基于有限元（FEM）架构，区别于采用有限差分法（FDM）的其他主流铸造仿真软件，具备复杂几何边界高精度拟合、薄壁零件仿真适配性强的技术特点[[S28,S16,S13]]。软件采用热焓法处理凝固潜热，结合傅里叶导热方程求解，支持充型-凝固全耦合计算，也可单独设置初始边界条件完成纯凝固求解，适用于周期性循环铸造过程的多周期温度演化分析[[S6,S5]]。充型流场计算通过完全 Navier-Stokes 流动方程求解，支持任意时刻金属液状态分析，可识别大尺寸铸件充型过程中的湍流现象[[S12,S23]]。

**网格生成**：ProCAST 内置的 MeshCAST 有限元网格生成模块采用两步法生成网格：先生成表面网格，再基于合格的面网格生成四面体体积网格，支持针对不同仿真区域差异化设置网格尺寸，远离铸件的模具部分采用大尺寸网格，铸件热节、薄壁、金属液流转折区域采用加密细网格，可在保证关键区域精度的同时降低整体计算量[[S16,S40,S27]]。

**材料数据库**：ProCAST 内置热物性数据库由英国 ThermoTech 公司开发，为开放可扩展架构，覆盖钢/铁、铝基、钴基、铜基、镁基、镍基、钛基、锌基等全系列合金，同时内置砂型、精铸壳等各类铸型材料的物性参数。用户可直接输入合金化学成分，软件可自动生成对应液相线温度、固相线温度、固相率变化、比热、潜热、黏度、热膨胀系数、杨氏模量等全套热流固热力学参数，还支持基于实测测温数据通过反向求解模块反算界面换热系数[[S7,S23,S39,S12]]。

**CAD/CAE 集成**：ProCAST 2016 版本的接口体系分为三类：①专用接口，支持 UG NX 的 PARASOLIDS 格式原生对接；②通用接口，可读取 IGES、STEP、STL 等通用 CAD 格式文件；③预划分有限元网格接口，可直接导入 Hypermesh、ANSYS、Patran、I-DEAS 等软件输出的已有网格文件，无需在 MeshCAST 内重新生成网格[[S16,S1,S35,S38]]。

## 版本历史

ProCAST 经过多年发展，经历了若干重要版本迭代：

| 版本            | 发布时间           | 主要特性                                                                                                                                     |
| --------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ProCAST v2004.0 | 2003 年 10 月      | 配套 DataCAST 模块用于将 PreCAST 输出的配置文件转换为二进制计算文件，基于早期命令行运行逻辑实现核心有限元求解能力[[S21]]                     |
| ProCAST 2010    | 2010 年前后        | ESI 整合产品线后推出的主流稳定版本，新增由英国 ThermoTech 公司开发的独有热力学数据库，用户可直接输入合金化学成分自动生成全套热力学参数[[S8]] |
| ProCAST 14.5    | 后续迭代版本       | 图形化工作流版本，拥有 Visual-Process Executive 图形化主界面，提供新建项目、打开项目入口，集成了 Process Templates、Pedestrian Report 等功能 |

## 应用范围与典型案例

ProCAST 可适配几乎所有主流铸造工艺类型，具体覆盖压铸（高压/低压压铸）、砂型铸造、金属型铸造、熔模铸造、离心铸造、连铸、消失模铸造、触变铸造、挤压铸造、倾转铸造、壳型铸造等全场景[[S16,S7,S41,S3]]。以下为若干公开发表的工程应用案例：

**机床支架砂型铸造**：针对 ZG230-450 铸钢机床支架，采用自下而上的底注封闭式浇注系统，ProCAST 模拟显示充型过程稳定，无明显湍流。优化后所有缩孔缩松集中在冒口区域，铸件本体无分散缩松缺陷，且铸件整体处于低应力状态，无明显应力集中，可直接获得合格铸件[[S2,S31]]。

**铝合金支架挤压铸造**：在浇注温度 700 ℃、模具温度 200 ℃、压力 150 bar 的工艺条件下，t = 4.05 s 时除料饼和薄厚壁过渡区外支架大部分区域已完成凝固，ProCAST 可准确预测出易产生裂纹的薄厚壁过渡区位置[[S11]]。

**ADC12 铝合金汽车壳体件压铸**：先后增设四周连通的溢流槽消除初始充型裹气缺陷，采用压室推挤金属液的修正仿真模型开展正交试验，最终优选工艺参数为浇注温度 650 ℃、一级压射速度 0.2 m/s、高低速切换位置 320 mm、二级压射速度 2 m/s，实际生产后 X 射线检测显示原严重缩松缺陷完全消除[[S37]]。

**航空航天高温合金熔模铸造**：ProCAST 内置专属辐射计算模块，可精准计算辐射角系数和阴影效应，广泛应用于航空航天高温合金铸件的充型、凝固及热应力预测场景，已公开的工程案例覆盖排气机匣等航空精密铸件的工艺优化工作[[S33,S7]]。

## 与同类软件的对比

ProCAST、MAGMAsoft、AnyCasting 三款主流铸造仿真软件的横向核心差异如下[[S15,S43,S46,S44]]：

| 对比维度     | ProCAST                                             | MAGMAsoft                                       | AnyCasting                                     |
| ------------ | --------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------- |
| **求解方法** | 纯 FEM 有限元                                       | FDM/FEM 混合架构                                | FDM 有限差分                                   |
| **开发公司** | 法国 ESI 集团                                       | 德国 Magma Foundry Technologies                 | 韩国 AnyCasting 公司                           |
| **功能特点** | 辐射精确计算、高阶热-力耦合、微观组织全流程仿真     | 面向不同铸造工艺配置专属细分模块                  | 快速自动流场计算和一键生成网格                  |
| **操作复杂度** | 中等                                                | 较高，需基于铸造工程经验配置专属参数              | 较低，自动化程度最高                            |
| **适配场景** | 薄壁复杂精密铸件、航空高温合金铸件仿真              | 汽车领域大批量常规铸件的全流程工艺优化            | 中小型铸造企业快速完成常规压铸、重力铸造工艺仿真 |

ProCAST 采用有限元（FEM）求解架构，实现流场-温度场-应力场全耦合计算，支持非连续网格和无级变密度网格划分，相比有限差分类仿真软件可大幅降低薄壁复杂铸件的计算量、提升曲面特征的模拟精度[[S7]]。

## 别名与易混淆名称

ProCAST 的官方唯一标准推荐书写格式为首字母大写 Pro 后续全大写无空格的 **ProCAST**；行业出版物广泛通用的非正式认可变体为全大写写法 **PROCAST**、带半字线分隔的 **Pro-CAST**；而 **PorCast** 是典型的拼写错误，将首音节 Pro 误写为代表孔隙的 Por；**Pro CAST**、**Pro Cast** 属于用户随意在字符间添加空格的非规范拆分写法，不属于官方认可别名[[S16,S18]]。

## 局限性

**材料数据库固有误差**：ProCAST 内置通用材料物性数据库存在固有误差，其计算的部分合金热物性参数（如球墨铸铁热膨胀系数）与实测值存在偏差，用户导入特定材料的实测热物性参数可进一步提升仿真精度[[S24,S34]]。

**高速压铸流场模拟短板**：ProCAST 采用 FEM 求解架构，常规低速充型工况下仿真精度表现优异，高速压铸极端高流速湍流充型场景下，流场模拟精度相比专用流体仿真软件存在短板，不属于其优势适用场景[[S15]]。

**计算资源需求**：有限元法需要高质量的有限元生成器来生成合适的单元网格，方程组复杂且运算不可分解，需要大量的内存资源和较长的计算时间[[S13]]。但 ProCAST 原生支持多节点并行计算，可通过多 CPU 核心协同运算大幅降低大尺度复杂铸造模型的总仿真时长[[S25]]。

## 关系与生态

**上下游工具集成**：ProCAST 支持将自身仿真得到的应力、应变等结果数据无缝传递至 ABAQUS、PAM-CRASH、SYSWELD、DEFORM 等下游工程仿真软件，实现铸造-后续热处理/力学性能分析的链式耦合全流程计算[[S7]]。在全流程数字化铸造链条中，ProCAST 处于 CAD 模具设计完成后、实际铸造成型投产前的核心工艺仿真验证环节，可通过录制操作脚本实现与 SiPESC 等通用集成仿真平台的对接，自动完成铸造工艺参数迭代优化[[S20,S32]]。

**标准仿真流程**：ProCAST 标准仿真流程一般包括 CAD 模型导入 → MeshCAST 网格生成 → PreCAST 前处理参数配置 → DataCAST 求解前数据校验 → ProCAST 核心求解计算 → ViewCAST 后处理结果可视化五个标准环节[[S6,S18]]。

## Sources
- S8: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ef11554-2e86-4f0f-8f90-4908a7c498b4/resource) (`3ef11554-2e86-4f0f-8f90-4908a7c498b4`)
- S30: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6c0ddc9-3495-490b-bb55-129392d012fc/resource) (`a6c0ddc9-3495-490b-bb55-129392d012fc`)
- S7: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3eddaa0f-952f-40b2-9e09-bee2330c6760/resource) (`3eddaa0f-952f-40b2-9e09-bee2330c6760`)
- S16: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63b3e66c-c55a-4cc4-82e0-b16103a22763/resource) (`63b3e66c-c55a-4cc4-82e0-b16103a22763`)
- S18: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b7a3f34-ec19-4de1-bdc2-9dfcb55e8f1d/resource) (`6b7a3f34-ec19-4de1-bdc2-9dfcb55e8f1d`)
- S26: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a14f6fc-8302-4aa0-8268-75ac725cf37f/resource) (`8a14f6fc-8302-4aa0-8268-75ac725cf37f`)
- S48: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe0c050e-e159-4526-8b45-b84e3a2141d0/resource) (`fe0c050e-e159-4526-8b45-b84e3a2141d0`)
- S23: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81103ba7-fae6-40d9-b4b2-702aac88b88e/resource) (`81103ba7-fae6-40d9-b4b2-702aac88b88e`)
- S12: [基于ProCAST砂型铸造高锰钢斗齿的工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5434f168-c7cc-4b02-af30-893e26f72d94/resource) (`5434f168-c7cc-4b02-af30-893e26f72d94`)
- S40: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd18bda9-cc1c-466e-87fc-224bca5ba3f4/resource) (`dd18bda9-cc1c-466e-87fc-224bca5ba3f4`)
- S27: [56336290_网格生成](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b794561-f90a-429c-ac8d-4662637f320b/resource) (`9b794561-f90a-429c-ac8d-4662637f320b`)
- S42: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e14a4c12-1c9e-490f-b811-41979e25169d/resource) (`e14a4c12-1c9e-490f-b811-41979e25169d`)
- S22: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7d3ef7ec-65e9-4e35-993a-19ad9926f654/resource) (`7d3ef7ec-65e9-4e35-993a-19ad9926f654`)
- S33: [锡电解阳极立模浇铸水冷系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/adc147b1-44fe-4269-971f-7147d5756a59/resource) (`adc147b1-44fe-4269-971f-7147d5756a59`)
- S3: [大尺寸铝合金轮毂低压铸造凝固模拟及结构强度的仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d1cb07b-8d9a-4d31-af09-a50f709fbbdc/resource) (`0d1cb07b-8d9a-4d31-af09-a50f709fbbdc`)
- S5: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23485e18-d829-41c6-b386-06248fcee281/resource) (`23485e18-d829-41c6-b386-06248fcee281`)
- S9: [金属材料液态成型实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e9b4595-5752-4870-a9ef-f44eb135a437/resource) (`4e9b4595-5752-4870-a9ef-f44eb135a437`)
- S28: [表1.1 国内外部分铸造软件及应用功能简介](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e0862eb-9852-4afa-bdf2-6a892ca415fe/resource) (`9e0862eb-9852-4afa-bdf2-6a892ca415fe`)
- S13: [基于传热原理的热节快速分析模型及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f38db28-1050-4dc8-81ce-f1ba1afa0a3c/resource) (`5f38db28-1050-4dc8-81ce-f1ba1afa0a3c`)
- S6: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c1603cf-1be4-4bca-b6df-6bf644a57b69/resource) (`3c1603cf-1be4-4bca-b6df-6bf644a57b69`)
- S39: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3a31ed1-0c0d-4c71-bc3c-6818b40da0ae/resource) (`d3a31ed1-0c0d-4c71-bc3c-6818b40da0ae`)
- S1: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00ba3675-940d-4315-a753-0de69beef2a6/resource) (`00ba3675-940d-4315-a753-0de69beef2a6`)
- S35: [表3.1 Procast2016接口格式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3079230-7e28-48d9-b077-3ff425d521e0/resource) (`b3079230-7e28-48d9-b077-3ff425d521e0`)
- S38: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb9822e6-dbe7-428b-83fd-0ece263fd1be/resource) (`cb9822e6-dbe7-428b-83fd-0ece263fd1be`)
- S21: [显示ProCAST与DataCAST版本信息的命令行窗口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bd4ee2c-ec8e-4846-a216-284da02d99fe/resource) (`7bd4ee2c-ec8e-4846-a216-284da02d99fe`)
- S41: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd273b06-cd96-497f-ac47-0861037cc35f/resource) (`dd273b06-cd96-497f-ac47-0861037cc35f`)
- S2: [基于ProCAST的机床支架铸造工艺模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01274704-0c32-4425-8eba-f249a2ddba70/resource) (`01274704-0c32-4425-8eba-f249a2ddba70`)
- S31: [基于ProCAST的机床支架铸造工艺模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/abc6356a-a849-4f60-8961-a30d61856f9f/resource) (`abc6356a-a849-4f60-8961-a30d61856f9f`)
- S11: [t=4.05 s时铝合金支架凝固过程固相分数分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/528c39ab-99bc-4669-b242-db93a13ee177/resource) (`528c39ab-99bc-4669-b242-db93a13ee177`)
- S37: [汽车壳体类铸件的压铸工艺优化及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c48d621c-7d65-454b-abf8-50b5c8c10f2e/resource) (`c48d621c-7d65-454b-abf8-50b5c8c10f2e`)
- S15: [表2.1 主流铸造数值模拟软件对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62ad51a3-c595-452b-8c7d-bff26d5f2a5f/resource) (`62ad51a3-c595-452b-8c7d-bff26d5f2a5f`)
- S43: [表2.3 铸造主流软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e39fba15-e487-4979-8a06-2419ecd4b62b/resource) (`e39fba15-e487-4979-8a06-2419ecd4b62b`)
- S46: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S44: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S24: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8567b1f4-a2a5-460d-84a1-0536a45dc839/resource) (`8567b1f4-a2a5-460d-84a1-0536a45dc839`)
- S34: [图2.2(e) ProCAST与JMatPro的球墨铸铁热膨胀系数对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae42e896-2fb8-4f6d-8025-5524d2abe9ea/resource) (`ae42e896-2fb8-4f6d-8025-5524d2abe9ea`)
- S25: [挤压铸造成形铝合金飞轮壳构件微观组织与力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86f9aa7c-356e-4e30-a1e8-766f1f791f2c/resource) (`86f9aa7c-356e-4e30-a1e8-766f1f791f2c`)
- S20: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7865ee9f-f3b1-417a-ab89-5103ba29a441/resource) (`7865ee9f-f3b1-417a-ab89-5103ba29a441`)
- S32: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad14679d-a737-4681-a5af-3dfc99d408a5/resource) (`ad14679d-a737-4681-a5af-3dfc99d408a5`)