---
version: "v1"
generated_at: "2026-06-18T14:45:47+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 33
  source_quality_score: 0.84
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

## 概述

元胞自动机（Cellular Automaton，CA）是一种空间、时间及系统状态全部离散的动力学系统，无显式控制方程，属于一类模型/方法框架的统称 [[S36,S15]]。在金属凝固模拟领域，CA方法融合了确定性模型与随机性模型的优势：既能体现溶质浓度与过冷度之间的物理关联，又能引入形核分布和晶粒取向的随机性，支持在较大计算域下描述凝固组织随时间的全流程演化 [[S34,S1]]。相比于相场法，CA方法能够适配更大的模拟尺度，工程实用性更强，已成为压铸微观组织模拟的主流技术之一 [[S18,S20]]。

## 基本原理与构造规则

凝固模拟CA方法的基础构造规则包括以下四个核心方面 [[S15,S36]]：

1. **空间离散**：将计算域离散为大量均匀元胞（cell），元胞排列在规则的离散空间网格上。
2. **状态离散**：每个元胞携带有限个离散状态与变量。
3. **时间离散**：所有元胞在统一设置的离散时间步长下同步更新状态。
4. **局部演化**：单个元胞在$t+1$时刻的状态由其自身及邻域元胞$t$时刻的状态通过预设的局部转移规则计算得到。

### 元胞状态定义

在凝固模拟中，元胞状态通常划分为三类 [[S26,S10,S2]]：

| 状态值 | 物理含义 |
|--------|----------|
| 0 | 纯液态（Liquid） |
| (0, 1) | 固液界面/糊状区（Mushy） |
| 1 | 纯固态（Solid） |

每个元胞除状态值外，还携带温度、溶质浓度、固相分数、晶向标识和形核状态等变量 [[S36]]。

### 邻域交互规则

CA方法的邻胞交互规则定义了中心元胞更新状态时需参考的周边元胞范围，主流规则包括三类 [[S10,S28]]：

- **Von Neumann规则**：仅考虑与中心元胞共边的邻胞（二维下为4个）。
- **Moore规则**：考虑与中心元胞共边及共顶点的全部邻胞（二维下为8个）。
- **Margolus规则**：基于元胞块的分组交互规则。

![凝固模拟CA方法的Moore邻胞规则示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ee92753-9545-421d-804c-3ae663fd6ca7/resource)

该图展示了Moore邻域规则的排布：中心红色固相元胞周边8个相邻元胞均为棕色界面元胞，直观呈现了该邻域规则在凝固模拟中的元胞覆盖范围 [[S4]]。

### 元胞几何形态

CA方法支持的元胞几何形态主要包括三角形、正方形和正六边形三类，其中二维模拟中最常用的是正方形与正六边形网格 [[S36,S28,S2]]。不同网格形态需配套针对性的各向异性校正策略，以消除网格本身带来的晶粒生长方向偏差 [[S28]]。

![凝固模拟CA方法元胞类型及演化过程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9734ccc8-bd04-4ae8-8a4c-c5ddbe9977af/resource)

该图标注了凝固模拟CA方法的三类元胞（固相胞、界面胞、液相胞），分步演示不同状态元胞的邻域交互及捕获生长过程，直观呈现了CA方法的基础演化逻辑 [[S24]]。

## 核心模型分类

### 晶粒生长CA模型

晶粒生长CA模型以Rappaz和Gandin于1993年提出的经典CA模型为代表 [[S34,S36]]。该模型采用以下核心机制：

- **形核模型**：基于高斯分布的连续形核模型，分别设定型壁表面形核与熔体内部体积形核两套独立参数 [[S7,S35]]。
- **生长动力学**：采用KGT枝晶尖端生长动力学模型，枝晶尖端生长速率$v$与过冷度$\Delta T$的关系拟合为多项式 $v(\Delta T) = a_2 \Delta T^2 + a_3 \Delta T^3$ [[S7,S32]]。
- **捕获规则**：通过计算晶粒累计生长长度$L(t)$，当$L(t)$达到元胞对角线方向尺寸$l(\cos\theta+|\sin\theta|)$时捕获相邻液态元胞 [[S31]]。
- **主要应用**：晶粒形核、晶粒竞争生长、柱状晶向等轴晶转变（CET）的模拟 [[S34,S31]]。

### 枝晶生长CA模型

枝晶生长CA模型以2001年Zhu等人提出的改进型MCA（Modified Cellular Automaton）模型为代表 [[S34,S28]]。该模型在晶粒生长模型基础上进一步纳入：

- 晶体取向；
- 固液界面曲率；
- 溶质再分配参数；
- 溶质扩散方程与温度场方程的耦合求解。

该模型可精确再现单/多枝晶的二维及三维形貌、枝晶竞争生长和微观偏析现象，以及流动对枝晶生长的影响，模拟精度显著高于基础晶粒生长CA模型 [[S34]]。

### 耦合类CA模型

耦合类CA模型是当前工程应用的主流，主要包括三类 [[S36,S6]]：

- **CAFE（元胞自动机-有限元耦合）**：采用双网格体系，粗尺度有限元网格求解宏观温度场，细尺度CA网格求解微观形核与生长，通过节点插值完成数据交互，是目前应用最广的耦合方案 [[S36,S9]]。
- **CAFD（元胞自动机-有限差分耦合）**：宏观温度场通过有限差分法求解，与CA微观组织计算耦合 [[S2,S9]]。
- **CA-FV（元胞自动机-有限体积耦合）**：宏观传输方程通过有限体积法离散，与CA方法耦合 [[S36]]。

在CAFE框架中，凝固过程释放的潜热从CA侧反馈至宏观有限元节点以更新温度场，可实现大尺度铸件在非均匀温度场下的全流程凝固组织模拟。ProCAST等商用铸造CAE软件的凝固组织预测模块即基于CAFE模型开发 [[S36,S9]]。

![有限元宏观传热与元胞自动机微观晶粒生长的耦合原理示意](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21910589-76cf-476c-81c5-56a1bb19d4a6/resource)

该图从网格、温度分布、序参数和固液界面四个维度直观呈现了有限元宏观传热计算与微观元胞自动机晶粒生长的衔接逻辑 [[S5]]。

## 在压铸凝固过程中的应用

### 晶粒形貌预测

CA方法预测晶粒形貌的实现逻辑为：将计算域内满足形核条件的元胞标记为晶核，从预设的多组结晶取向中随机分配取向，以[001]为择优生长方向向外捕获相邻液态元胞，通过KGT模型计算枝晶尖端生长速率，动态更新元胞状态即可可视化输出不同取向的多晶枝晶形貌 [[S13,S31]]。

### 柱状晶向等轴晶转变（CET）模拟

CA方法通过结合随机形核规则，在糊状区引入游离形核质点，利用竞争生长机制刻画从型壁外延生长的柱状晶被熔体内部新生等轴晶阻断的全过程，可定量预测不同冷却条件下柱状晶区与中心等轴晶区的占比 [[S6]]。

### 微观偏析预测

在元胞状态更新过程中，CA方法引入固液界面的溶质再分配计算，跟踪每个元胞凝固过程中排出的溶质在相邻液态元胞内的扩散行为，可刻画晶粒内部和晶界处的溶质元素富集偏析现象 [[S28]]。

### 缩松缺陷预测

CA方法耦合宏观Niyama判据（$G/\sqrt{R}$，即凝固末期温度梯度与凝固速率的比值）实现缩松缺陷预测：当局部区域的$G/\sqrt{R}$值低于对应合金的临界阈值时，判定该区域存在缩松生成倾向，进一步结合流动场的达西渗流计算可定量预测缩松的分布与尺寸 [[S13,S16]]。

## 参数与运行条件

### 形核参数

CA模拟的形核过程广泛采用符合高斯分布的连续形核模型，形核概率随局部过冷度动态变化 [[S7]]。针对压铸场景，需分别设置型壁表面形核与熔体内部体积形核两套独立的高斯分布参数，核心参数包括：

- 最大形核密度 $n_{max}$；
- 平均形核过冷度 $\Delta T_{max}$；
- 过冷度标准差 $\Delta T_\sigma$。

以下为三种典型合金CA模拟的形核参数参考值：

**6082铝合金** [[S35]]：

| 浇注温度 (K) | 型壁 $n_S$ (m⁻²) | 型壁 $\Delta T_{S,max}$ (K) | 型壁 $\Delta T_{S,\sigma}$ (K) | 熔体 $n_V$ (m⁻³) | 熔体 $\Delta T_{V,max}$ (K) | 熔体 $\Delta T_{V,\sigma}$ (K) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 950 | $2.4\times 10^7$ | 0.5 | 0.1 | $2.0\times 10^9$ | 5 | 0.1 |
| 980 | $1.1\times 10^7$ | 0.5 | 0.1 | $1.2\times 10^9$ | 4 | 0.1 |
| 1010 | $1.8\times 10^6$ | 0.5 | 0.1 | $3.6\times 10^8$ | 3 | 0.1 |

**42CrMo钢** [[S25]]：

| 参数 | 值 | 单位 |
|------|-----|------|
| 最大体形核密度 | $2\times 10^{10}$ | m⁻³ |
| 平均体形核过冷度 | 5.5 | K |
| 体形核过冷度标准差 | 5 | K |
| 最大面形核密度 | $5\times 10^7$ | m⁻² |
| 平均面形核过冷度 | 0.5 | K |
| 面形核过冷度标准差 | 0.1 | K |

### 生长动力学参数

KGT枝晶生长模型中，生长动力学系数$a_2$、$a_3$由Gibbs-Thomson系数$\Gamma$、溶质扩散系数$D$、液相线斜率$m$、溶质平衡分配系数$k$及初始浓度$c_0$共同决定 [[S7,S32]]：

- **6082铝合金**：Gibbs-Thomson系数 $\Gamma = 2.4\times 10^{-7} \ \text{m}$，液相溶质扩散系数 $D_L = 3\times 10^{-9} \ \text{m}^2/\text{s}$，$a_2 = 1.989\times 10^{-6} \ \text{m/(s}\cdot\text{K}^2)$，$a_3 = 3.892\times 10^{-6} \ \text{m/(s}\cdot\text{K}^3)$ [[S33]]。
- **ZL203铝合金**：Gibbs-Thomson系数 $\Gamma = 2\times 10^{-7} \ \text{m}$，$a_2 = 0$，$a_3 = 8.744537\times 10^{-6} \ \text{m/(s}\cdot\text{K}^3)$，型壁面形核密度与熔体体形核密度满足换算关系 $n_v = 0.8\ n_s^{3/2}$ [[S30]]。

### 时间步长约束

CA模拟的时间步长$\Delta t$选取须同时满足两个约束条件 [[S8]]：

1. **溶质扩散数值稳定性**：$\Delta t < (\Delta X)^2 / (4D_L)$；
2. **枝晶生长空间约束**：$\Delta t < \Delta X / V_{max}$，保证单个时间步内枝晶生长的最大距离不超过1个元胞边长，避免跨越多重元胞导致数值失真。

## 与其他模拟方法的对比

### 方法特性对比

| 方法 | 适用尺度 | 维度 | 核心应用场景 | 模拟精度 |
|------|----------|------|-------------|---------|
| 元胞自动机（CA） | 介观晶粒级 | 2D/3D | 晶粒组织演化预测、杂晶/雀斑缺陷预测、疏松缺陷模拟 | 中等 |
| 相场法（PF） | 微观/介观枝晶级 | 2D/3D | 枝晶尖端动力学、二次枝晶臂生长、低角度晶界形成机制 | 高 |
| 有限元法（FEM） | 宏观物理场尺度 | 1D/2D/3D | 全局温度场、流场、应力场模拟与工艺优化 | 中等 |

CA方法在适用尺度上填补了相场法小尺度高计算量与纯有限元法无法直接输出微观晶粒结构的应用空白 [[S3]]。

### 定性对比总结

- **确定性模型**：物理背景清晰，但无法考虑随机过程和晶粒晶体学特征，不能模拟枝晶形貌与CET转变 [[S12]]。
- **蒙特卡罗（MC）法**：基于概率抽样可生成近似晶粒形貌，但未纳入枝晶尖端生长动力学参数，缺乏明确物理基础，模拟迭代步长与实际凝固时间无对应关系 [[S12,S22]]。
- **相场法**：无需显式追踪固液界面，可高精度模拟枝晶二次臂等精细微观结构，但计算域小、求解复杂度高，难以在工业级大构件场景应用 [[S19,S22]]。
- **CA法**：兼具物理基础与随机性优势，效率与模拟尺度综合表现最优，适配工业级铸件晶粒组织工程预测需求 [[S12,S19,S20]]。

## 软件集成

主流压铸模拟软件对CA方法的集成实现如下：

- **ProCAST**：内置独立CAFE微观组织模块，采用高斯分布连续形核模型与KGT枝晶尖端生长动力学描述晶粒演化，通过宏观有限元节点向CA元胞插值传递温度场边界，CA侧计算得到的凝固潜热同步反馈至宏观FE节点实现双向耦合 [[S36,S33]]。
- **MAGMASOFT**：在其显微组织分析子模块中集成了基于元胞自动机框架的随机凝固组织预测功能，支持高压压铸工艺下晶粒分布和CET转变的工程化模拟计算 [[S11,S23]]。

## 优势与局限

### 优势

- 融合确定性与随机性模型优势，兼顾溶质浓度、过冷度的物理机制和形核分布、晶粒取向的随机性 [[S34,S20]]。
- 相比相场法模型参数少、计算效率高，可在较大的计算区域下高效描述凝固组织随时间的演化 [[S20,S28]]。
- 可与宏观有限元/有限差分方法耦合形成CAFE/CAFD跨尺度仿真体系，衔接宏观温度场与微观组织演变 [[S34,S9]]。

### 局限性

- 状态转移规则多基于经验设定，部分推导缺乏严格理论支撑，对复杂微观物理过程的内在机制描述精度受限 [[S29]]。
- 常规公开的压铸场景CA模拟计算域通常局限于1 mm³量级区域，无法完整覆盖大尺寸压铸件的全范围非均匀组织（表层、偏析带、心部） [[S17]]。
- 尚需进一步耦合压铸特有的高压传递、强制对流和压力作用下溶质重分布等效应，才能完整适配大尺寸压铸构件全流程模拟需求 [[S17]]。

## Sources
- S36: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5dd046a-6d09-4419-9377-bee1308b3a85/resource) (`f5dd046a-6d09-4419-9377-bee1308b3a85`)
- S15: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71a182ef-2cfc-45f6-ab1f-99aaeaae5eba/resource) (`71a182ef-2cfc-45f6-ab1f-99aaeaae5eba`)
- S34: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e94d58ee-7715-44e3-9cf1-62b295b3d05c/resource) (`e94d58ee-7715-44e3-9cf1-62b295b3d05c`)
- S1: [钛合金TC4真空自耗熔炼铸锭质量控制基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02dd1ffd-5fbe-459d-aba4-41f8fdc38e8f/resource) (`02dd1ffd-5fbe-459d-aba4-41f8fdc38e8f`)
- S18: [不同铸造工艺条件下工型异形件凝固组织数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87228438-b70d-4b0a-b52c-43d3a784fb39/resource) (`87228438-b70d-4b0a-b52c-43d3a784fb39`)
- S20: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8da005e9-4fc8-4417-a168-94fbdd7cdf1e/resource) (`8da005e9-4fc8-4417-a168-94fbdd7cdf1e`)
- S26: [表 2-1 元胞状态值与对应状态关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b9f1e544-6684-4402-9423-29e207119078/resource) (`b9f1e544-6684-4402-9423-29e207119078`)
- S10: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/517e67e6-a5fe-4c5b-96c1-1b85392824bf/resource) (`517e67e6-a5fe-4c5b-96c1-1b85392824bf`)
- S2: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/041a03be-ddc2-4e84-8c4e-1b4b6216f19c/resource) (`041a03be-ddc2-4e84-8c4e-1b4b6216f19c`)
- S28: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cdb160b9-aaaf-4157-aef1-d9882532394d/resource) (`cdb160b9-aaaf-4157-aef1-d9882532394d`)
- S4: [(b) Moore规则](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ee92753-9545-421d-804c-3ae663fd6ca7/resource) (`1ee92753-9545-421d-804c-3ae663fd6ca7`)
- S24: [凝固模拟中元胞自动机法（CA法）的元胞类型与邻域交互规则示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9734ccc8-bd04-4ae8-8a4c-c5ddbe9977af/resource) (`9734ccc8-bd04-4ae8-8a4c-c5ddbe9977af`)
- S7: [基于深度学习的42CrMo八角锭铸造参数预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31357d3a-5280-488a-9708-9c7a9bd9331e/resource) (`31357d3a-5280-488a-9708-9c7a9bd9331e`)
- S35: [表3.1 模拟中所用形核参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2b33cf9-98f3-4a55-85bc-d7aa64d01433/resource) (`f2b33cf9-98f3-4a55-85bc-d7aa64d01433`)
- S32: [TextNode32](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d7e1b035-beae-4459-be95-eaa845104008/resource) (`d7e1b035-beae-4459-be95-eaa845104008`)
- S31: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d57dbdf3-881a-4ebe-aedb-fa5c3e5214b0/resource) (`d57dbdf3-881a-4ebe-aedb-fa5c3e5214b0`)
- S6: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26041cf4-e2e1-4025-975e-5ccfb763ad39/resource) (`26041cf4-e2e1-4025-975e-5ccfb763ad39`)
- S9: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4630ada2-31e0-4c8a-958d-22c0f2ff8bd0/resource) (`4630ada2-31e0-4c8a-958d-22c0f2ff8bd0`)
- S5: [有限元传热与元胞自动机晶粒结构耦合示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21910589-76cf-476c-81c5-56a1bb19d4a6/resource) (`21910589-76cf-476c-81c5-56a1bb19d4a6`)
- S13: [不同铸造工艺条件下工型异形件凝固组织数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6012bf71-ce28-446a-ac54-bde81396530a/resource) (`6012bf71-ce28-446a-ac54-bde81396530a`)
- S16: [图4.25 不同压射速度条件下Niyama准则预测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75e0e1b0-612f-44b3-b248-72e3791d4253/resource) (`75e0e1b0-612f-44b3-b248-72e3791d4253`)
- S25: [表3-2 形核参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a84acb66-6642-4e1e-a37e-6df965a68871/resource) (`a84acb66-6642-4e1e-a37e-6df965a68871`)
- S33: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd543b58-df06-4174-b3e1-432086507ff5/resource) (`dd543b58-df06-4174-b3e1-432086507ff5`)
- S30: [不同铸造工艺条件下工型异形件凝固组织数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d320bb1a-1eb7-4d45-b875-876b9f2db7f8/resource) (`d320bb1a-1eb7-4d45-b875-876b9f2db7f8`)
- S8: [铝及铝合金铸轧成形与裂纹扩展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43276c31-143f-4296-ba4a-fcd56d3c31b7/resource) (`43276c31-143f-4296-ba4a-fcd56d3c31b7`)
- S3: [表1 镍基高温合金定向凝固数值模拟主要方法对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e29e57f-03d0-4bca-bd61-6eba8bd1e796/resource) (`0e29e57f-03d0-4bca-bd61-6eba8bd1e796`)
- S12: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/567a8618-b51c-4dd4-a232-e5a61ebc6663/resource) (`567a8618-b51c-4dd4-a232-e5a61ebc6663`)
- S22: [铝及铝合金铸轧成形与裂纹扩展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91cb450f-151d-4489-95b0-1a4bd4608757/resource) (`91cb450f-151d-4489-95b0-1a4bd4608757`)
- S19: [表1-2 三种不同模拟方法的对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bd266d3-5f83-4d09-bcc9-d012bf2cae9e/resource) (`8bd266d3-5f83-4d09-bcc9-d012bf2cae9e`)
- S11: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52de7543-8714-4606-8b56-1b9689943624/resource) (`52de7543-8714-4606-8b56-1b9689943624`)
- S23: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92a4eeba-faae-477e-9596-e5adbbf25424/resource) (`92a4eeba-faae-477e-9596-e5adbbf25424`)
- S29: [镁稀土合金激光选区熔化宏_微观组织跨尺度调控研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0465d33-b778-4cf8-8f53-30aab603f918/resource) (`d0465d33-b778-4cf8-8f53-30aab603f918`)
- S17: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8f34c5-e0a7-4690-86b6-0a9a7180f2f4/resource) (`7b8f34c5-e0a7-4690-86b6-0a9a7180f2f4`)