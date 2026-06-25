---
version: "v1"
generated_at: "2026-06-18T14:38:43+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 19
  source_quality_score: 0.82
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

Visual-Cast（也常写作 Visual Cast 模块）是法国 ESI 集团 ProCAST 铸造仿真软件在 2009 版之后，集成于 Visual-Environment 中的核心前处理与求解触发模块。它在完整的铸造仿真流程中，位于网格划分模块 Visual-Mesh 之后、DataCast/ProCAST 求解器之前，并与后处理模块 Visual-Viewer 共同构成从几何离散到结果可视化的闭环链路[[S24,S16,S11]]。Visual-Cast 并非一个单纯的“初始条件设置”工具，而是承担铸造工艺全参数配置、多物理场耦合前处理以及计算启动功能的综合性平台。

## 分类与定位
Visual-Cast 属于 ESI 的 Visual-Environment 系列组件，与同套件中的 Visual-Mesh、Visual-Viewer 协同工作。它在软件架构中完全替代了旧版 ProCAST（2009 版前）中的独立前处理器 PreCAST，将原来需要通过不同程序间手动传递中间文件才能完成的材料分配、界面定义、边界条件加载等工作，统一到同一个集成环境内执行[[S12,S24,S25]]。

## 核心功能
Visual-Cast 的功能边界已经远超出单一的初始条件设置，其覆盖的前处理能力包括[[S16,S11,S7,S19]]：
- 导入有限元网格模型后，为不同域（铸件、铸型、浇注系统等）分配材料属性；
- 设置不同材料配对间的界面换热系数（支持 EQUIV、COINC、NCOINC 三种换热类型）[[S26]]；
- 配置各类动态边界条件，如热交换、运动位移、加载压力、冷却方式等；
- 定义通用铸造工艺参数，包括重力方向、金属液流速、充型速率、初始填充率等，以及各工艺专属参数（例如高压铸造的压力参数、离心铸造的旋转参数）；
- 设定求解器运行参数，如模拟总步数、模拟终止温度、最大模拟时长；
- 提供基于 500+ 种合金的热物性参数库，并支持用户通过输入合金化学成分自动计算热物理参数，以及自行构建和录入自定义材料模型；
- 在完成所有参数设置后，自动执行参数合法性自检，排查参数遗漏或取值超出合理范围等错误，自检通过后即可提交 DataCast/ProCAST 求解器开始多场耦合计算。

## 工艺参数与输入方式
### 可配置的关键参数
根据工艺需要，Visual-Cast 环境下需要配置和可配置的核心基础参数如下表所示（典型示例）[[S2,S8,S18,S16]]：

| 参数类别 | 参数示例 | 说明 |
| :--- | :--- | :--- |
| 通用必选参数 | 重力矢量（默认 9.8 m/s²，可自定义方向） | 定义铸造系统坐标系及充型方向 |
|  | 材料初始温度 | 各域（铸件、模具等）的起始温度 |
|  | 初始填充率 | 充型开始前型腔的初始状态 |
| 工艺专属参数 | 浇注温度、充型质量流量、充型速率 | 重力铸造及一般充型 |
|  | 压力参数（冲头压力、保压压力等） | 高压/低压压铸 |
|  | 旋转速度、离心参数 | 离心铸造 |
| 界面条件 | 不同材料配对之间的界面换热系数（W/(m²·K)） | 如金属‑砂、金属‑金属界面 |
| 求解控制参数 | 模拟总步数（NSTEP） | 防止步数不足导致模拟中断 |
|  | 模拟终止温度 | 计算停止的温度阈值 |
|  | 最长模拟运行时长 | 计算时间上限 |

参数配置采用三层架构：首先设置重力方向、所有材料的初始温度和初始填充率等通用必选参数；其次根据所选铸造工艺（如高压压铸、离心铸造等）添加对应的专属参数；最后定义求解控制参数，如计算步长、停止温度、最大步数和最长运行时间。所有参数设置完成后，模块自动执行合法性检测，无异常即允许启动求解[[S18]]。

### 数据录入方式
Visual-Cast 提供三类数据输入途径[[S5,S23]]：
1. **网格属性自动继承**：直接从上游 Visual-Mesh 模块接收已完成校验的体网格（.mesh 文件），网格中的域信息无需重复录入；
2. **材料数据库调用**：从内置超过 500 种合金的热物性参数库中直接选取材料，系统自动载入相应的热导率、密度、比热、焓等参数；用户也可通过输入合金成分，由软件基于 Scheil 模型等自动计算热物性[[S19,S11]]；
3. **手动自定义**：对材料库中未涵盖的特殊材料，用户可手工录入全部热物性数据，或基于工艺需要直接键入自定义边界条件与运行参数。

## 操作流程与界面
Visual-Cast 的标准参数设置工作流程如图示[[S18,S22]]：

![Visual-Cast 铸造仿真参数配置操作全流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c12d6384-b07f-41c7-be42-f7b37097dd32/resource)

图中所展现的典型步骤为：设置重力方向 → 配置材料参数 → 设置界面换热系数 → 添加工艺专属参数 → 定义边界条件 → 执行参数合理性自检 → 自检通过后启动求解计算。这一流程将几何、材料与工艺信息有序组织，保证仿真前处理的可追溯性。

在参数配置的具体界面中，Process Condition Manager 以表格形式直观呈现工艺条件的设置逻辑。界面按“参数名称–参数类型–作用实体区域–边界条件数值”四列排布，支持直接设置热交换、运动位移、压力加载等工艺条件[[S6]]。

![Visual-Cast 工艺条件参数配置对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b754a21-889a-45cb-a0c9-5150698124e4/resource)

此外，Visual-Cast 的操作界面中，通过“文件‑会话”菜单路径，用户可以录制和运行 Python 脚本，以实现批量参数化仿真和自定义流程扩展[[S15]]。

## 支持的铸造工艺
Visual-Cast 可适配的铸造工艺类型十分广泛，覆盖了绝大多数主流和特种工艺，包括砂型铸造、熔模铸造、高压压铸（HPDC）、低压压铸（LPDC）、重力铸造、离心铸造、连续铸造、液态模锻以及半固态成形等[[S11,S16,S5]]。模块内部通过工艺专属参数集来区分不同工艺的物理边界条件，使用户只需在统一界面下切换参数模板即可完成相应工艺的仿真前设置。

## 与相邻模块的数据传递关系
在整个 ProCAST 工作流中，模块间采用严格的串行数据传递逻辑[[S16,S1,S4,S11]]：
1. **上游 Visual-Mesh** 完成几何检查与面/体网格划分，生成检查合格的 .mesh 文件；
2. **Visual-Cast** 读取 .mesh 文件，进行材料、界面、边界条件及求解参数的全套配置，自检通过后保存为 .vdb 格式，提交给 DataCast/ProCAST 求解器；
3. **求解器（DataCast/ProCAST）** 读入 .vdb 进行多场耦合计算，输出 .unf 结果文件；
4. **下游 Visual-Viewer** 读取 .unf 文件，进行温度场、流场、应力场等结果的可视化分析。

这一闭环中，前一模块的输出必须通过校验才能进入下一环节，从而保证了仿真数据链的一致性与可靠性。

## 局限性
在现有文献和使用案例中，Visual-Cast 存在以下已知局限：
- **对大尺寸复杂几何的网格依赖**：原生配套的 MeshCAST 在处理单元数极高（例如达 445 万）的复杂壳体等大型模型时，网格划分能力有限，需要借助 HyperMESH 等第三方前处理工具生成符合要求的 .sm 格式网格，再在 Visual-Cast 中完成加载，否则易出现网格缺陷导致计算不收敛或程序崩溃[[S9]]。
- **非传统材料支持不足**：内置合金数据库主要覆盖常用铸造合金。对于非传统复合材料或特殊定制材料，系统不提供默认热物性参数，用户必须手动录入全部热物性数据（热导率、密度、比热、焓等），自行构建用户材料库[[S11,S4]]。
- **自定义多变量耦合初始条件受限**：常规可视化界面无法直接定义某些复杂的多变量耦合初始条件。要实现参数化批量仿真，需通过“文件‑会话”路径录制 Python 脚本进行二次开发[[S15]]。
- **数据接口封闭**：Visual-Cast 仅支持 ProCAST 系列内部专属格式（.mesh、.vdb、.unf）与上下游模块进行数据交互，无法直接对接第三方有限元求解器的通用输入输出格式[[S16]]。

## Sources
- S24: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd18bda9-cc1c-466e-87fc-224bca5ba3f4/resource) (`dd18bda9-cc1c-466e-87fc-224bca5ba3f4`)
- S16: [基于ProCAST的压气机持环铸钢件缺陷研究和工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6dd1ce20-ce2b-413b-beab-9a1a3ebdca0f/resource) (`6dd1ce20-ce2b-413b-beab-9a1a3ebdca0f`)
- S11: [TiB2_205A铝基复合材料组织性能及制动盘液态模锻成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5910e2de-9864-4bb4-9992-f1df025225a9/resource) (`5910e2de-9864-4bb4-9992-f1df025225a9`)
- S12: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63b3e66c-c55a-4cc4-82e0-b16103a22763/resource) (`63b3e66c-c55a-4cc4-82e0-b16103a22763`)
- S25: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd273b06-cd96-497f-ac47-0861037cc35f/resource) (`dd273b06-cd96-497f-ac47-0861037cc35f`)
- S7: [铝合金大壁厚差支架挤压铸造工艺设计及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b913285-1e00-49e4-abf8-fe0a6dd717e9/resource) (`3b913285-1e00-49e4-abf8-fe0a6dd717e9`)
- S19: [铝合金大壁厚差支架挤压铸造工艺设计及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bcc0d92-7418-4cd9-ac20-c39002106f99/resource) (`8bcc0d92-7418-4cd9-ac20-c39002106f99`)
- S26: [超声波辅助铸造铝合金的组织细化与强化补缩的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbe4bc67-fcf4-4573-8662-d485f0cac442/resource) (`fbe4bc67-fcf4-4573-8662-d485f0cac442`)
- S2: [基于ProCAST的压气机持环铸钢件缺陷研究和工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04b7c20d-269c-47cd-96a2-c861aad794ca/resource) (`04b7c20d-269c-47cd-96a2-c861aad794ca`)
- S8: [TiB2_205A铝基复合材料组织性能及制动盘液态模锻成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43630962-1338-4875-90b3-5c2f663d3be3/resource) (`43630962-1338-4875-90b3-5c2f663d3be3`)
- S18: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8647e5c3-fad0-4706-8fb0-075e476b709b/resource) (`8647e5c3-fad0-4706-8fb0-075e476b709b`)
- S5: [低压铸造筒形件组织性能及铸造缺陷消除机制研究_朱继虎](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30f7ee62-3813-49dd-9eba-89e00d1d941a/resource) (`30f7ee62-3813-49dd-9eba-89e00d1d941a`)
- S23: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbcee639-0ac9-4d7f-8309-92a4c5d40853/resource) (`cbcee639-0ac9-4d7f-8309-92a4c5d40853`)
- S22: [图2-4 Visual-Cast中铸造工艺参数设置过程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c12d6384-b07f-41c7-be42-f7b37097dd32/resource) (`c12d6384-b07f-41c7-be42-f7b37097dd32`)
- S6: [图2-5 Visual-Cast中的工艺条件参数设置界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b754a21-889a-45cb-a0c9-5150698124e4/resource) (`3b754a21-889a-45cb-a0c9-5150698124e4`)
- S15: [图4-5 ProCAST-Python脚本录制入口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65a075e0-739b-4ede-9cd8-a2364e602a0b/resource) (`65a075e0-739b-4ede-9cd8-a2364e602a0b`)
- S1: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00ba3675-940d-4315-a753-0de69beef2a6/resource) (`00ba3675-940d-4315-a753-0de69beef2a6`)
- S4: [低熔点合金再造加工基准的组织性能及成形工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30a05f52-399e-48c5-aaa8-bc548788c66e/resource) (`30a05f52-399e-48c5-aaa8-bc548788c66e`)
- S9: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e7cda16-ba0f-460c-8326-8dbddca2c9f7/resource) (`4e7cda16-ba0f-460c-8326-8dbddca2c9f7`)