---
version: "v1"
generated_at: "2026-06-21T06:13:27+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 59
  source_quality_score: 0.87
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

有限差分法（FDM）是求解偏微分方程的一类主要数值方法。其核心思想是：将连续的求解域划分为差分网格，以有限个网格节点代替连续的求解域；通过Taylor级数展开将控制方程中的导数转换为网格节点上函数值的差商，从而将微分方程问题转化为可直接求解的代数方程组。该方法属于数学层面的近似离散方法，原理清晰直观、易于编程实现、并行适配性好，在材料加工领域的传热、流动、扩散等数值模拟中应用广泛。[[S42,S49,S19]]

在铸造领域中，FDM是应用最为广泛的数值方法之一，绝大部分充型流动场和凝固温度场数值模拟计算均采用此方法。铸造领域的主流商用模拟软件如MAGMA、PAM-CAST、NovaCast等均以FDM作为底层核心算法。[[S68,S5,S38,S34]] 有限差分法又称泰勒展开差分法，是最早应用于传热计算的数值方法。[[S5,S34]]

## 核心原理

### 离散化方式
FDM将连续的时间-空间域进行剖分，得到以空间步长Δx、Δy、Δz和时间步长Δt为特征的离散网格。所有连续的场变量均在网格节点上定义。[[S45,S19]] 离散推导的基础是Taylor级数展开：通过截断高阶小项得到不同精度的差商近似式。[[S42,S49]]

常见的差商构造形式包括三种：
- **向前差分**：∂u/∂x ≈ (u(x+Δx)-u(x))/Δx，截断误差为O(Δx)，属于一阶精度。[[S46,S42]]
- **向后差分**：∂u/∂x ≈ (u(x)-u(x-Δx))/Δx，截断误差为O(Δx)，属于一阶精度，常用于构造迎风格式以避免非物理的数值振荡。[[S46,S42,S18]]
- **中心差分**：∂u/∂x ≈ (u(x+Δx)-u(x-Δx))/(2Δx)，通过抵消一阶误差项，截断误差为O(Δx²)，属于二阶精度。[[S46,S42]]

有限差分法规则网格离散化的典型表现形式如下图中所示，将连续的求解域离散为规则的正方形网格单元，在曲面边界处会形成阶梯状的逼近特征：[[S70]]

![有限差分法规则正交网格离散化示意图，展示连续求解域被剖分为规则正方形网格单元及曲面边界处的阶梯状逼近](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f870ef1d-f9b9-45f4-a88f-3a346b973951/resource)

### 显式与隐式格式
FDM求解时间相关问题时，时间维度的处理区分出两类基本格式：[[S53,S24]]

- **显式差分格式**：当前时刻的未知变量仅由上一时刻已求解的相邻节点变量直接计算得出，无需联立方程组。每个节点的方程均可独立求解，程序实现简单、内存占用低，在铸造模拟中应用广泛。但显式格式仅为**条件稳定**，时间步长受严格限制。[[S53,S1,S24,S8]]
- **隐式差分格式**：当前时刻的未知变量由同一步长下的相邻节点变量共同组成方程组，必须通过线性代数求解获取所有未知量。程序实现复杂度更高、内存占用更大，但属于**无条件稳定**，可采用远大于显式格式的时间步长。在大时间尺度的非稳态传热模拟中，隐式格式效率优势显著。[[S53,S1,S24,S47]]

两种核心解法的对比总结如下表：[[S69]]

| 解法类型 | 优点 | 缺点 |
|----------|------|------|
| 显式解法 | 程序简单、内存占用小 | 时间步长受稳定性限制，总迭代次数多 |
| 隐式解法 | 时间步长可大、同步长精度高 | 程序复杂、内存要求高，需求解线性方程组 |

### 收敛性与稳定性
差分方程的**收敛性**是指：当空间步长Δx和时间步长Δt同时趋近于0时，数值解能够无限逼近原始偏微分方程的精确解析解。对于一维扩散方程，显式格式当傅里叶数Fo≤1/2时满足收敛条件。[[S31,S49,S19]]

差分格式的**稳定性**是指数值求解过程中产生的舍入误差不会随迭代步数增长而无限制放大的特性。数学上定义为存在不随Δx、Δt趋近0而变化的有限Lipschitz常数K，保证任意时刻的数值解误差范数不超过初始时刻误差范数的K倍。常用判定方法包括von Neumann傅里叶级数分析法。[[S43,S44,S30]]

针对扩散主导的热传导问题，显式FDM的稳定性约束条件严格：[[S54,S1,S56]]

| 维度 | 稳定性条件（均匀网格） |
|------|------------------------|
| 一维直角坐标 | Fo = αΔt/Δx² ≤ 1/2 |
| 二维直角坐标 | Fo ≤ 1/4 |
| 三维直角坐标 | Fo ≤ 1/6 |

针对双曲型对流方程，还需满足**CFL（Courant-Friedrichs-Lewy）条件**，即Courant数C = uΔt/Δx ≤ 1，保证流体在一个时间步长内的运动距离不超过对应网格的空间步长。该条件由R.Courant等人于1928年提出。[[S43,S44,S20]]

## 结构化网格与交错网格

### 结构化网格
FDM最常用的离散网格为正交均匀结构化网格，所有节点按行列索引规则排布，单元邻接关系规整，生成简单、离散格式推导便捷。但结构化网格对复杂曲面边界的表征能力弱，仅能通过加密小尺寸单元来降低几何近似误差，在边界上易出现锯齿状（阶梯状）逼近。[[S41,S8,S38]] 下图为工业级连铸模拟中使用的三维结构化FDM六面体网格实例，边部区域网格加密：[[S12]]

![工业级连铸全流程模拟的三维结构化FDM六面体网格实例，计算域总长34.5m](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/191b8e6d-3e19-4713-a43d-e81b66681f48/resource)

### MAC交错网格
MAC（Marker-and-Cell）法由Harlow等人提出，是一种用于不可压缩流体Navier-Stokes方程求解的特殊FDM网格体系。其核心特征为：标量（压力、温度）定义在单元中心；各方向速度分量分别定义在对应单元面的中心位置。这种场变量错位分布避免了非交错网格中容易出现的不合理速度场也满足连续性方程的数值解振荡问题，同时使压力梯度直接作为单元相邻面法向速度的自然驱动力，物理意义明确。[[S66,S39,S62]] MAC网格搭载标记点追踪自由液面位置，是铸造行业主流FDM模拟软件的核心流场求解网格体系。[[S39,S32,S62]] 下图为MAC单元的二维结构示意图：[[S17]]

![MAC单元的二维结构示意图，标注单元尺寸及x、y向速度分量与单元中心压力存储位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e15031b-7994-46a6-9ee4-eab7309b3192/resource)

### 精度阶数与边界条件
不同差分离散格式的精度阶数区分如下：[[S49,S53]]
- 一阶精度：向前差分、向后差分、一阶迎风格式、显式欧拉格式。
- 二阶精度：中心差分格式、Crank-Nicolson隐式格式。

常见的三类边界条件及其差分处理方式：[[S28,S58,S45]]
1. **Dirichlet（第一类）边界条件**：直接指定边界节点的场变量定值，代入离散方程组即可。
2. **Neumann（第二类）边界条件**：指定边界处的法向导数（如绝热边界的零热流密度），通过边界外虚拟节点构造离散方程。
3. **混合（第三类）边界条件**：同时指定变量值与法向导数的换热关系，合并前两类的离散条件求解。

## 在压铸CAE中的过程作用

FDM在压铸CAE场景下的核心定位是用于充型过程和凝固过程的快速数值模拟。[[S5,S34,S9]]

### 温度场求解
在压铸三维非稳态传热过程中，FDM将Fourier传热偏微分方程通过差分离散转化为显式、隐式或交替方向隐式格式的代数方程。显式FDM因通用性强、逻辑简单，是绝大多数商用压铸模拟软件实现温度场求解的主流方案。[[S21,S63]]

### 凝固模拟与潜热处理
在压铸凝固模拟的FDM框架下，针对相变过程的潜热释放特性，有三类经过工程验证的标准处理方式：温度回升法、等价比热法和热焓法。[[S33,S68]] FDM可通过规则网格快速迭代计算得到不同时刻的固相率分布，基于残余熔体模数等判据预测缩孔、缩松、卷气、冷隔等典型压铸缺陷的位置与分布。[[S26,S38,S52]]

### 模具热平衡仿真
FDM可用于压铸模具热平衡仿真，支持连续多生产周期的温度场快速迭代计算，辅助优化模具预热工艺、冷却系统排布，预测模具稳态温度分布与最佳开模时间。[[S33,S68]]

### 多物理场耦合
FDM框架下的温度场-流场-应力场耦合可分为两类实现逻辑：[[S33]]
- **单向耦合**：先通过FDM完成温度场求解，再将温度场作为体载荷导入后续应力求解模块。
- **双向耦合**：采用同一种FDM方法完成全部多场求解，使用带温度和位移自由度的耦合单元同步输出温度、应力计算结果。

## 与有限元法、有限体积法的对比

### 有限元法 (FEM)
FEM基于变分原理推导离散方程，支持不规则非结构化网格，可高精度适配任意复杂铸件几何边界。在应力场和变形仿真领域精度优势明显。但其网格生成流程繁琐、求解方程复杂度高、计算耗时久、硬件资源占用高，面向流场仿真的落地应用少于FDM。[[S38,S48]] FEM在压铸场景中多用于模具的力学性能分析与结构设计环节。[[S5,S34,S9]]

下图为FEM非结构化网格示意，与FDM规则网格形成直观对比：[[S15]]

![铸件充型凝固数值模拟用的有限元非结构化网格划分示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/240275bb-227b-4a77-9fab-3b9bfe8cc7cc/resource)

### 有限体积法 (FVM)
FVM基于积分型守恒方程推导离散格式，将网格单元作为控制体积输出物理量平均值。它在结合FDM计算简便性的同时，对复杂边界具有更强的适配能力，在求解守恒型流体流动问题时精度表现优异。[[S6,S4]]

## 主流压铸模拟软件的算法归属

公开学术文献整理的铸造数值模拟软件核心参数对比如下表所示：[[S37]]

| 软件名称 | 开发方 | 算法 | 分析内容 | 主要特点 |
|----------|--------|------|----------|----------|
| MAGMASoft | 德国 | 有限体积法/有限差分法 | 传质与传热、微观组织 | 网格自动划分，可实现凝固收缩、表面缺陷跟踪、显微组织分析 |
| ProCAST | 美国 | 有限元法 | 传质与传热、应力 | 自动网格划分、完整数据库及可视化结果 |
| Flow-3D | 美国 | 有限体积法/有限差分法 | 传质与传热、微观组织 | 同MAGMASoft |
| AnyCasting | 韩国 | 有限差分法 | 传质与传热、应力 | 强大的前处理功能，热物性数据库完善 |
| 华铸CAE | 中国 | 有限差分法 | 传质与传热 | 基于FDM分析温度场和流场，含缺陷分析模型 |

按算法架构分类：纯FDM架构软件包括韩国AnyCasting、中国华铸CAE（InteCAST）；FDM与FVM混合架构软件包括德国MAGMASOFT、美国FLOW-3D；纯FEM架构软件包括美国ProCAST。[[S37,S52,S68]]

## 压铸工程应用案例

**案例一：铝合金汽车曲轴箱**——基于FDM算法的MAGMA软件完成铝合金汽车曲轴箱高压压铸仿真，可准确预测充型流动路径、填充时长、凝固序列、型腔空气压力分布与卷气缺陷位置，辅助优化浇注系统与排气布局，仿真精度经生产实测验证匹配。[[S68]]

**案例二：铝合金支架**——国产FDM架构HZ CAE软件用于汽车铝合金支架高压压铸仿真，采用1mm边长立方FDM规则网格，总网格量达106.9万，准确识别出初始浇注方案中两股金属流汇合位置的卷气缺陷，通过修改辅助流道厚度消除该缺陷，最终得到合格铸件。[[S57]]

**案例三：发电机顶盖**——日立研发的纯FDM软件ADSTEFAN用于汽车发电机顶盖ADC12铝合金高压压铸仿真，设置1mm网格单元共668.9万个，基于仿真结果识别出单流道方案导致的局部表面缺陷，改为双流道后完成仿真验证并生产出无缺陷合格铸件。[[S23]]

**案例四：轴承盖**——基于FDM架构的AnyCasting软件完成轴承盖高压压铸仿真，通过概率缺陷参数、残余熔体模数判据计算得到缩孔缩松仅分布在排溢系统区域，铸件本体无高概率缺陷位置，实际生产铸件质量完全合格，仿真预测结果与实测完全吻合。[[S26]]

## 局限性与注意事项

**复杂几何适应性差**：传统FDM采用规则六面体网格，对非规则曲面边界会产生锯齿状（阶梯状）逼近。面向薄壁铸件仿真时精度受限。若要提升边界精度必须大幅加密网格，会显著拉高计算量。[[S38,S10,S27]]

**应力场计算精度低**：常规FDM难以直接独立完成应力场的高精度计算。工程应用中通常先采用FDM/FVM求解温度场，再将场数据映射导入有限元模型完成热力耦合应力求解，这一跨模型数据匹配过程会引入额外误差。[[S55,S38]]

**自由表面追踪困难**：FDM针对压铸高压高速充型过程的自由表面追踪（通常依赖VOF体积函数法），需严格满足数值稳定性条件。当适配压铸工况下雷诺数普遍大于10⁵的强湍流流动时，易出现自由界面数值耗散和捕捉失真的问题。[[S14,S32]]

## 直接差分法 (DFDM)

直接差分法是有限差分法的一种明确衍生变体。其核心特征区别于常规基于微分方程泰勒展开的FDM：DFDM不依赖原始控制微分方程推导差分格式，而是直接对离散后的微元单元应用守恒定律生成可直接计算的差分方程，属于典型的直接形格式。这一方法最早由日本大中逸雄（Ohnaka）提出。[[S7,S65,S59]]

DFDM的重大优势在于能够适配任意形状的多边形/多面体单元，突破了常规正交FDM网格的形状限制，便于模拟复杂几何形状的铸件外形。[[S41,S36]]

根据节点和节点领域的定义方式，直接差分法分为两类：[[S65,S7]]
- **内节点法**：将微元本体定义为节点领域，以微元外心作为节点。
- **外节点法**：将微元顶点定义为节点，以节点邻域的边/面垂直平分线围合区域作为节点领域。

DFDM与常规FDM的主要特性对比如下：[[S36]]

| 对比维度 | DFDM | FDM |
|----------|------|-----|
| 网格形状 | 灵活（三角形、四边形等） | 规则正交网格 |
| 输入数据量 | 大 | 较小 |
| 程序复杂度 | 复杂 | 较简单 |
| 所用内存 | 较大 | 较小 |
| 计算时间 | 稍长 | 较短 |

## 分类与主要变体

常规有限差分法的主流衍生变体包括：显式有限差分法、隐式有限差分法、交替方向隐式法（ADI）、Saul'yev有限差分法、控制体积有限差分法等。不同变体在时间步长稳定性、求解效率、守恒性上存在差异化特征，均已在铸造充型、凝固模拟中获得工业化应用。[[S7,S2,S60]]

差分格式从精度上可分为一阶格式（向前差分、向后差分、显式欧拉格式）和二阶格式（中心差分、Crank-Nicolson格式）；从空间形式可分为中心格式、迎风格式；时间维度可组合为显格式、隐格式和显隐交替格式。[[S49]]

> 注：现有检索范围内未在ISO/TR 22716《金属铸造的数值模拟通用要求》等公开内容中检索到直接提及有限差分法的专项规范或不适用于压铸的具体限制意见。已收录的ASTM系列压铸标准均为针对压铸合金成分、力学性能测试和产品验收的材料与制品标准，也未检索到针对FDM在铸造模拟中使用的强制限定要求。[[S16,S35,S51]]

## Sources
- S42: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70e0e4d0-1ce0-4035-be47-42bef37462d8/resource) (`70e0e4d0-1ce0-4035-be47-42bef37462d8`)
- S49: [凝固界面换热系数反求及铝合金薄壁件压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/974637af-eaa3-428a-96db-7a25bb375528/resource) (`974637af-eaa3-428a-96db-7a25bb375528`)
- S19: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35b43f43-42dd-4b54-8e21-3f2846be22b0/resource) (`35b43f43-42dd-4b54-8e21-3f2846be22b0`)
- S68: [die casting parameters and simulations for crankcase of automobile using__2a23cb7ad5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f012419a-8360-4070-8060-9a6b3553fc90/resource) (`f012419a-8360-4070-8060-9a6b3553fc90`)
- S5: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f70ea36-ce52-4e3b-8342-33eaab4b0fcc/resource) (`0f70ea36-ce52-4e3b-8342-33eaab4b0fcc`)
- S38: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/680eb6b2-cf3d-4364-a11c-ce185417ca6d/resource) (`680eb6b2-cf3d-4364-a11c-ce185417ca6d`)
- S34: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/617fc0c9-9b13-476e-94f7-e86c3eb8515b/resource) (`617fc0c9-9b13-476e-94f7-e86c3eb8515b`)
- S45: [计算机在材料热加工工程中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7de80487-63f9-4fa1-b549-d53eba299aa7/resource) (`7de80487-63f9-4fa1-b549-d53eba299aa7`)
- S46: [橡塑挤出模具设计与工程模拟原著](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/840e740f-4cfc-40cc-9ead-09703969e479/resource) (`840e740f-4cfc-40cc-9ead-09703969e479`)
- S18: [格子玻尔兹曼方法基础与工程应用附计算机代码](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3306ec2a-ca05-465c-8b8d-5ea77b2570fd/resource) (`3306ec2a-ca05-465c-8b8d-5ea77b2570fd`)
- S70: [有限差分法的几何离散网格示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f870ef1d-f9b9-45f4-a88f-3a346b973951/resource) (`f870ef1d-f9b9-45f4-a88f-3a346b973951`)
- S53: [金属塑性成形仿真技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a88d88fc-c64e-46ed-b1ae-d8c8710f2f9a/resource) (`a88d88fc-c64e-46ed-b1ae-d8c8710f2f9a`)
- S24: [机械工程手册 第2版 7 机械制造工艺及设备卷 1 第2篇 铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43854f5f-1791-4957-a009-2a76f861df5c/resource) (`43854f5f-1791-4957-a009-2a76f861df5c`)
- S1: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02a4c98d-808d-4c9f-b27b-b095f87af230/resource) (`02a4c98d-808d-4c9f-b27b-b095f87af230`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12a737d3-bc7a-48eb-8223-1c496a0ae282/resource) (`12a737d3-bc7a-48eb-8223-1c496a0ae282`)
- S47: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84a18056-0a4f-40c3-b3da-c0382fc0d393/resource) (`84a18056-0a4f-40c3-b3da-c0382fc0d393`)
- S69: [显式解法和隐式解法的比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3252d14-449b-4619-a897-1a9436241dcf/resource) (`f3252d14-449b-4619-a897-1a9436241dcf`)
- S31: [计算机在材料热加工工程中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5faf7a4b-a438-4d7b-bb7a-465d3f7797a4/resource) (`5faf7a4b-a438-4d7b-bb7a-465d3f7797a4`)
- S43: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71421ec2-47b7-4b5c-b3bd-ed61bc80abae/resource) (`71421ec2-47b7-4b5c-b3bd-ed61bc80abae`)
- S44: [现代模具设计基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72dbd046-8175-42bd-9b06-81c73d67b04c/resource) (`72dbd046-8175-42bd-9b06-81c73d67b04c`)
- S30: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e26d9f2-1193-49ab-aeaf-4bbbcf6b7845/resource) (`5e26d9f2-1193-49ab-aeaf-4bbbcf6b7845`)
- S54: [材料热加工过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab72588b-b91d-47fb-a776-bd703bfecb32/resource) (`ab72588b-b91d-47fb-a776-bd703bfecb32`)
- S56: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b63a66e7-9b4c-4861-bacf-f3b71281b1de/resource) (`b63a66e7-9b4c-4861-bacf-f3b71281b1de`)
- S20: [FTBS格式不同时间步长比下的误差传播系数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38221431-70d3-4ee1-9b7c-b39039ec8843/resource) (`38221431-70d3-4ee1-9b7c-b39039ec8843`)
- S41: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ebbf345-9487-482f-aea6-a2b91cfb89a8/resource) (`6ebbf345-9487-482f-aea6-a2b91cfb89a8`)
- S12: [图4-1 板坯连铸全长度钢液流动、传热和凝固过程的计算域和网格](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/191b8e6d-3e19-4713-a43d-e81b66681f48/resource) (`191b8e6d-3e19-4713-a43d-e81b66681f48`)
- S66: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e50a5a8a-ea26-4ff4-af16-af6227ebd023/resource) (`e50a5a8a-ea26-4ff4-af16-af6227ebd023`)
- S39: [钛合金复杂薄壁构件离心熔模铸造充型与凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68683d2d-b213-4aaa-b276-c63ceebfa02d/resource) (`68683d2d-b213-4aaa-b276-c63ceebfa02d`)
- S62: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d63fdc81-9f47-4422-8dbd-664133bbb123/resource) (`d63fdc81-9f47-4422-8dbd-664133bbb123`)
- S32: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fc549e6-bd30-494d-9539-91fb93d9a5b4/resource) (`5fc549e6-bd30-494d-9539-91fb93d9a5b4`)
- S17: [MAC单元示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e15031b-7994-46a6-9ee4-eab7309b3192/resource) (`2e15031b-7994-46a6-9ee4-eab7309b3192`)
- S28: [computational techniques for process simulation and analysis using matla__7fd12c8940](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55371b96-9d0e-4535-9de1-addde2ed929a/resource) (`55371b96-9d0e-4535-9de1-addde2ed929a`)
- S58: [computational techniques for process simulation and analysis using matla__7fd12c8940](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bde7f56d-b77d-4e09-a10c-a0ac5b925ac9/resource) (`bde7f56d-b77d-4e09-a10c-a0ac5b925ac9`)
- S9: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/13553474-1d89-4c9d-8a4b-89cef7a2e522/resource) (`13553474-1d89-4c9d-8a4b-89cef7a2e522`)
- S21: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39cbaeb5-45df-4980-b35f-54bde14d26f3/resource) (`39cbaeb5-45df-4980-b35f-54bde14d26f3`)
- S63: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d68412ab-3845-4e0c-a4a9-43d9af97c270/resource) (`d68412ab-3845-4e0c-a4a9-43d9af97c270`)
- S33: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6166f5cf-af07-4697-8dd4-b764281e27f4/resource) (`6166f5cf-af07-4697-8dd4-b764281e27f4`)
- S26: [轴承盖压铸缺陷分析及工艺优化_杨匀龙](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bdb7977-ce10-44a5-a125-fa3113b01f06/resource) (`4bdb7977-ce10-44a5-a125-fa3113b01f06`)
- S52: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9962a0bc-4e4f-497a-8c39-b2b8fc3fb914/resource) (`9962a0bc-4e4f-497a-8c39-b2b8fc3fb914`)
- S48: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89e3e9c6-6303-4f2e-9313-7271d78d8ce7/resource) (`89e3e9c6-6303-4f2e-9313-7271d78d8ce7`)
- S15: [有限元网格划分一般形式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/240275bb-227b-4a77-9fab-3b9bfe8cc7cc/resource) (`240275bb-227b-4a77-9fab-3b9bfe8cc7cc`)
- S6: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0fbf22d0-6af8-4216-9cf9-216302160ffa/resource) (`0fbf22d0-6af8-4216-9cf9-216302160ffa`)
- S4: [TextNode5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f178906-c445-45c6-827c-9ca9972d8b79/resource) (`0f178906-c445-45c6-827c-9ca9972d8b79`)
- S37: [表1-1 主要铸造数值模拟软件的介绍](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/675cb923-8f6c-45af-8dd4-5aa3814b2092/resource) (`675cb923-8f6c-45af-8dd4-5aa3814b2092`)
- S57: [die casting die design based on the application of cae simulation__42797f6dd3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd1c2689-4c53-4a17-8733-d01ef9e61db4/resource) (`bd1c2689-4c53-4a17-8733-d01ef9e61db4`)
- S23: [design of die casting process of top cover of automobile generator throu__2ef2b83fdd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d59f385-1fa0-45ba-995f-582970e69bf3/resource) (`3d59f385-1fa0-45ba-995f-582970e69bf3`)
- S10: [实用压铸模设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16040f7c-eaf5-4ba8-bf14-7d6e83e53e26/resource) (`16040f7c-eaf5-4ba8-bf14-7d6e83e53e26`)
- S27: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cd67177-a90d-4707-80b9-f1ac832013d9/resource) (`4cd67177-a90d-4707-80b9-f1ac832013d9`)
- S55: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5bdc545-64e8-4068-b3bb-731464fd2d9c/resource) (`b5bdc545-64e8-4068-b3bb-731464fd2d9c`)
- S14: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23d70eda-79f4-44b0-b37c-bc532b62d592/resource) (`23d70eda-79f4-44b0-b37c-bc532b62d592`)
- S7: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/107477e2-5438-407f-9a1f-f37f0e706ba0/resource) (`107477e2-5438-407f-9a1f-f37f0e706ba0`)
- S65: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e18843e0-d55e-45f8-8570-52380c5a472b/resource) (`e18843e0-d55e-45f8-8570-52380c5a472b`)
- S59: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c91ac59d-443d-4d69-96a2-25de40392172/resource) (`c91ac59d-443d-4d69-96a2-25de40392172`)
- S36: [DFDM与FDM方法对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/641916d3-126f-43e0-95e5-2f1fa5700380/resource) (`641916d3-126f-43e0-95e5-2f1fa5700380`)
- S2: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04921441-ca69-4078-8cb8-9033a1578239/resource) (`04921441-ca69-4078-8cb8-9033a1578239`)
- S60: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d04bad70-9923-4b41-90d2-14f2fdedb775/resource) (`d04bad70-9923-4b41-90d2-14f2fdedb775`)
- S16: [casting copper base alloys__d5182d5c2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27965a22-9b1c-434e-8c96-71db97cd78c2/resource) (`27965a22-9b1c-434e-8c96-71db97cd78c2`)
- S35: [1991 annual book of astm standards section 2 nonferrous metal products volume 0202 die cast metals aluminum and magne...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6277650d-109d-485b-a35d-420a7236f60f/resource) (`6277650d-109d-485b-a35d-420a7236f60f`)
- S51: [1991 annual book of astm standards section 2 nonferrous metal products volume 0202 die cast metals aluminum and magne...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99364ce8-7f61-4820-b169-af52609cef64/resource) (`99364ce8-7f61-4820-b169-af52609cef64`)