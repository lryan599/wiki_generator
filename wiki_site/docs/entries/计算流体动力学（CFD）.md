---
version: "v1"
generated_at: "2026-06-18T12:23:59+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 63
  source_quality_score: 0.84
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

在压铸技术范畴下，计算流体动力学（Computational Fluid Dynamics，简称CFD）是将高温、高压下金属液高速充型的流场与温度场由时空连续的物理量离散为有限个节点值的数值计算技术。CFD通过求解质量守恒、动量守恒与能量守恒控制方程组，以可视化形式预测压铸充型与凝固阶段的流动、传热现象，支撑工艺优化与缺陷预判[[S39]]。该技术能够输出不同时刻金属液的速度、压力、温度及液相体积分数分布，直观展示充型动态过程[[S16,S13,S57,S7,S1]]。

CFD在压铸领域的数值模拟通常结合有限差分法、有限元法或有限体积法实现空间离散，并采用SOLA-VOF、SIMPLE等算法求解流场，通过k-ε湍流模型描述高雷诺数下的紊流效应[[S57,S29]]。

---

## 核心控制方程

压铸充型过程的CFD模拟建立在流体力学基本守恒定律之上。工程应用中通常将金属液假设为不可压缩牛顿流体，建立以下控制方程组：

### 质量守恒方程（连续性方程）

连续性方程是质量守恒定律的数学表述。对于不可压缩流体（密度恒定），该方程简化为速度场散度为零的形式[[S59,S11,S51,S46]]：

$$
\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0
$$

式中，u、v、w分别为速度矢量在x、y、z方向上的分量。

### 动量守恒方程（Navier-Stokes方程）

动量守恒方程基于牛顿第二定律建立，描述压力项、体积力项与黏性力项对流体动量变化的作用关系[[S59,S30,S51,S34]]：

$$
\rho\left(\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} + w\frac{\partial u}{\partial z}\right) = -\frac{\partial P}{\partial x} + \rho g_x + \mu\nabla^2u
$$

y、z方向同理。式中，ρ为金属流体密度，P为压力，μ为运动黏度，g为重力加速度，∇²为拉普拉斯算子。压铸充型过程中雷诺数通常大于10⁵，属于紊流状态，N-S方程适配此非稳态流动特征[[S34]]。

### 能量守恒方程

能量方程基于热力学第一定律构建，描述金属液流动过程中的热量传导、对流换热与内热源关系，用于计算充型过程的温度分布，并为后续凝固仿真提供初始温度场[[S51,S33,S4,S46]]：

$$
\rho c\frac{\partial T}{\partial t} + \rho c u\frac{\partial T}{\partial x} + \rho c v\frac{\partial T}{\partial y} + \rho c w\frac{\partial T}{\partial z} = \frac{\partial}{\partial x}\left(\lambda\frac{\partial T}{\partial x}\right) + \frac{\partial}{\partial y}\left(\lambda\frac{\partial T}{\partial y}\right) + \frac{\partial}{\partial z}\left(\lambda\frac{\partial T}{\partial z}\right) + S
$$

式中，c为比热容，T为温度，λ为导热系数，S为内热源项。

### 体积函数（VOF）方程

为追踪充型过程中的自由表面位置，引入体积函数方程[[S1]]：

$$
\frac{\partial F}{\partial t} + U_j\frac{\partial F}{\partial x_j} = 0,\quad 0 \leq F \leq 1
$$

VOF方法结合高分辨率界面捕捉（HRIC）方案，可实现金属-空气界面的锐利分辨[[S17]]。

---

## 离散化方法

CFD数值求解的关键在于将连续控制方程离散化为代数方程组。压铸模拟中主要采用以下三类离散方法[[S5,S20]]：

| 离散方法 | 核心特点 | 压铸CFD中的主要应用 |
|----------|----------|---------------------|
| **有限差分法（FDM）** | 用差商代替导数，推导简单、计算成本低，对曲面边界拟合精度较低 | 充型流动、温度场的快速求解；多数商用压铸CAE软件的默认求解方法[[S28,S5,S66]] |
| **有限元法（FEM）** | 基于变分原理或加权余量法，对复杂边界拟合精度高，但离散过程复杂 | 压铸模具应力场与结构强度仿真；薄壁复杂压铸件的流场求解[[S28,S5,S20]] |
| **有限体积法（FVM）** | 以控制体积为基础，保证质量、动量、能量的全局守恒，结合SIMPLE算法求解 | 近年压铸充型多相流模拟中大量应用，适配金属-空气两相流动计算[[S51,S20,S17]] |

压铸CFD充型模拟中，SOLA-VOF方法是应用最广泛的求解方法之一，它结合体积分数法追踪自由表面位置，适配压铸充型中自由界面快速移动的特征[[S51]]。其他常用求解技术包括SIMPLE法、MAC法、分数步长法（Projection Method）等[[S57,S29]]。

如下表所示，压铸数值模拟中的离散方案涉及时间离散、梯度离散、散度离散等多个类别[[S24]]：

**表：压铸数值模拟常用离散方法设置**

| 离散类别 | 常用方法 |
|----------|----------|
| 时间离散 | 欧拉离散 |
| 梯度离散 | 最小二乘法（Least Squares Cell Based） |
| 散度离散（对流项） | 二阶离散 |
| 压力离散 | PRESTO! |
| 体积分数离散 | Geo-Reconstruct |

![气液两相流计算网格示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e386f1e-d273-4ab5-bcc8-6a51d20a20cc/resource)

上图为CFD仿真中的流动区域与计算网格示意图，用于支撑气液两相流SIMPLE-GALA算法的数值计算，直观展示了流场求解的空间离散方式[[S48]]。

---

## 在压铸中的角色与应用

### 充型过程模拟

液态金属在压力下充型的流态、流速与压力分布对压铸件质量有决定性影响。许多缺陷如浇不足、冷隔、气孔等均与充型过程直接相关[[S16,S13,S40,S42]]。CFD充型模拟可在此过程中发挥关键作用：

- **检验浇注系统合理性**：判断充型是否平稳、是否存在紊流飞溅，预测最后充型区域以确定溢流槽和排气槽的设置位置[[S16,S13,S40,S42]]。
- **优化内浇口位置与尺寸**：通过参数化模拟不同内浇口截面积与流速组合，获取最优充型状态[[S21]]。
- **评估充型速度场与温度场**：输出各时刻的流速分布与温度分布，识别局部高速冲刷区域与低温前沿[[S6,S67]]。

![铝合金水泵座压铸充型80%模拟图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16169853-06e7-48eb-8417-80307b73168a/resource)

上图展示了铝合金水泵座充型至80%时的金属液流速分布，可直观反映充型中期不同区域的金属液速度差异，用于分析充型流动特性、识别局部高速冲刷区域[[S6]]。

### 热场与凝固分析

基于CFD的热场与凝固模拟可计算全周期压铸过程中铸件与模具的温度时空分布，识别孤立热节位置，预测凝固顺序与补缩通道的演变规律[[S13,S40,S42]]。采用循环稳态热平衡法（CSM）可避免重复计算多轮压铸周期才能达到的稳态温度状态，大幅提升计算效率[[S29]]。

### 缺陷预测

**卷气缺陷**：内浇口处金属液流速通常可达30~60 m/s，金属液在复杂浇道与型腔中形成不规则紊流，气体无法及时排出而被卷入液相，凝固后形成气孔[[S31,S15,S65]]。CFD气液两相流（金属液-空气模型）模拟可直接追踪气泡的夹带、输运与合并过程，精准预测卷气区域的位置和占比[[S31,S15,S65]]。采用不可压缩-可压缩两相流模型相比传统单相流模型可更准确描述气泡动态行为，进一步提升预测精度[[S65]]。

**缩孔/缩松缺陷**：CFD凝固模拟结合残余熔体模数（Retained Melt Modulus）判据，可预测缩孔/缩松分布位置与概率，大量案例显示预测结果与实际铸件吻合度较高[[S18,S2,S55]]。

**冷隔/浇不足缺陷**：CFD耦合流场-温度场模拟可输出不同充型时刻的金属液前沿温度，提前识别前沿温度低于合金固相线的区域，预测冷隔类缺陷的产生风险[[S13,S43,S40]]。

### 浇排系统设计优化

基于CFD的浇排系统迭代优化遵循典型路径：模拟初始方案的充型流场→识别流速不均、絮流、卷气隐患→调整横浇道、内浇口、溢流槽和排气槽参数→验证优化效果[[S19,S23,S67,S35]]。

- **散热器类压铸件案例**：将双型腔浇排系统改为单型腔设计，型腔内卷气占比从19.29%降低至3.12%，同时缩短冷却时长[[S35]]。
- **发动机曲轴箱体案例**：通过增设中部浇口，将铸件底部充型温度从不足600℃提升至610℃以上，彻底消除冷隔缺陷；散热片侧壁金属液充型速度从60m/s降至40m/s，有效解决粘模问题[[S67]]。
- **汽车壳体零件案例**：采用Anycasting软件结合正交试验优化，确定浇注温度700℃、压射速度3m/s、模具预热温度220℃为最优组合工艺参数[[S36]]。

### 受控扩散凝固（CDS）的CFD研究

受控扩散凝固（Controlled Diffusion Solidification, CDS）是一种新型半固态凝固技术，将高热质量（HTM）和低热质量（LTM）两种预制合金熔体按比例混合，利用强制对流效应实现非枝晶细化组织[[S9]]。CFD技术是研究CDS混合过程的核心手段，通常采用Fluent软件结合VOF多相流模型与k-ε湍流模型，建立包含连续方程、动量守恒方程、能量守恒方程与溶质输运方程的数学模型，输出混合过程中的流场、温度场与溶质浓度场分布[[S68,S32,S50]]。

针对Al-8%Si合金CDS过程的CFD模拟研究表明[[S32]]：
- 湍流涡流扩散与主体对流扩散的共同作用可使两种合金在无机械搅拌条件下实现成分与温度的宏观均匀分布；
- 混合熔体仅存在几度过热，大量局部过冷区域可显著提升形核率，细化初生α-Al晶粒；
- CFD参数化模拟发现：Si含量越低、预制合金初始温度越高、混合时间越短，形核率发生相应变化（从52%降至0或11%），规律与实际金相观测结果一致[[S32]]。

---

## 分类

压铸CFD可从多个维度进行系统分类[[S11,S34,S27,S47,S58]]：

### 按时间相关性

| 类型 | 特点 | 压铸应用 |
|------|------|----------|
| 定常（稳态）流动仿真 | 假设流场不随时间变化 | 仅用于简化分析，实际压铸中极少采用 |
| 非定常（瞬态）流动仿真 | 可捕捉流场随时间的动态变化 | 压铸主流仿真类型，适配毫秒级高速充型的瞬态特征[[S11]] |

### 按流动状态

由于压铸充型过程中金属液雷诺数通常大于10⁵，属于充分发展的紊流[[S34,S27,S47]]。绝大多数压铸CFD仿真采用RANS系列k-ε双方程湍流模型完成流动求解。层流假设仅适用于极少数低流速特殊压铸工况[[S34]]。

### 按求解相数

| 类型 | 建模方式 | 预测能力 |
|------|----------|----------|
| 单相流仿真 | 仅求解金属液流动，忽略气相影响 | 早期应用，无法预测卷气行为[[S58,S47]] |
| 两相/多相流仿真 | 同时求解液相金属与周围气相/固相运动，结合VOF方法追踪自由表面 | 可实现卷气现象精准预测，为当前主流方法[[S58,S47,S17]] |

### 按数值离散方法

| 方法 | 主要特点 | 典型应用 |
|------|----------|----------|
| 有限差分法（FDM） | 效率高，边界拟合弱 | 充型、温度场快速求解[[S5,S66]] |
| 有限元法（FEM） | 边界拟合好，计算量大 | 应力场、结构场仿真[[S5,S20]] |
| 有限体积法（FVM） | 守恒性好 | 高精度多相流充型求解[[S20,S17]] |

---

## 关键仿真参数与设置

### 网格划分

压铸CFD仿真中网格划分质量直接影响求解精度。针对中小尺寸复杂压铸件，常用1mm级别的单元尺寸；仿真汽车发电机罩盖时1mm单元可产生约6,689,610个网格；汽车支架类零件同样以1mm单元可得到约1,069,320个网格单元[[S14,S60,S41]]。

### 湍流模型

针对高速充型的金属液湍流流动，标准k-ε模型适配大部分常规高压压铸充型工况[[S54,S62]]。针对半固态压铸充型，可设置WALLF壁面滑移参数调整壁面摩擦特性：取值0.99对应常规高压压铸的低摩擦特性，取值0.8对应半固态压铸更高的壁面摩擦效果[[S62]]。

### 边界条件与工艺参数

**界面换热系数典型值**[[S56,S44,S49]]：

| 界面类型 | 换热系数范围 [W/(m²·K)] |
|----------|-------------------------|
| 铸件与模具 | 1000~1500 |
| 模具组件间 | 1000 |
| 模具与外界空气 | 10 |
| 脱模剂喷涂区域 | 200~1000 |
| 铸型外表面空冷 | 对应室温20℃ |

**镁合金高压压铸推荐参数范围**[[S49]]：

| 工艺参数 | 推荐取值 |
|----------|----------|
| 浇注温度 | 640~730℃ |
| 模具预热温度 | 180~260℃ |
| 压射速度 | 0.3~5 m/s |
| 增压比压 | 30~50 MPa |

### 材料物性

常用压铸合金密度参考[[S22,S53,S14]]：

| 合金类型 | 密度 [kg/m³] | 其他属性 |
|----------|-------------|----------|
| ADC12铝合金 | 2471 | 黏度0.00125 Pa·s |
| A380铝合金 | 2700 | — |
| 镁合金 | 1700 | — |
| 锌合金 | 6500 | — |
| 铜合金 | 8400 | — |

模具常用H13/SKD61热作模具钢的热物性参数需随温度变化关联设置，以保证传热计算准确性[[S14]]。

---

## 局限性

### 计算成本高

完成包含完整热循环的高压压铸仿真通常需执行5~10次连续压铸循环运算才能达到模具温度稳态。针对1400万网格单元模型，即使采用500MHz个人计算机也需15小时以上；如需耦合型腔内气体流动、背压、充型过程同步凝固等多物理场模块，算力消耗和计算时间将进一步大幅提升[[S63]]。

### 模型假设偏差

当前绝大多数工程应用的压铸CFD仿真为降低算力门槛，普遍采用等温液态流动简化假设，未充分耦合以下复杂物理现象[[S63,S10,S29]]：
- 温度动态变化
- 充型过程中提前凝固
- 气体运动反压
- 氧化夹杂生成
- 非牛顿流变特性

由此导致仿真结果与实际生产工况存在系统性偏差。

### 验证困难

压铸充型过程发生在密闭不透明的模具型腔内部，瞬态流动时间仅几毫秒，很难通过直接的可视化观测手段获取内部流场真实数据用于仿真结果对标验证。当前验证多采用间接的缺陷位置对比方法，难以完成高精度的定量校准[[S38]]。

---

## 与其他模拟方法的关系

压铸数值模拟领域中，CFD方法与有限元结构分析、相场法微观模拟在求解尺度、核心方程和应用场景上有本质区别[[S5,S26]]：

| 方法 | 核心方程 | 求解尺度 | 主要应用场景 |
|------|----------|----------|-------------|
| CFD | 流体流动、传热传质方程（N-S方程） | 宏观 | 充型过程流场与温度场仿真 |
| 有限元结构分析 | 弹塑性力学方程 | 宏观 | 模具热疲劳应力、铸件残余应力与变形预测 |
| 相场法 | 相变动力学方程 | 介观 | 凝固过程中晶粒生长、偏析等微观组织演化模拟 |

三类方法可互为补充但不可相互替代。

---

## 常用压铸CFD仿真软件

主流压铸CFD仿真商用软件各有侧重[[S69,S52,S12,S64]]：

| 软件名称 | 核心方法 | 突出优势 |
|----------|----------|----------|
| **MAGMASOFT**（德国） | 有限差分法 | 压铸全周期模具热循环计算精度高 |
| **Flow-3D**（美国） | 有限差分法 | 自由表面流动、卷气缺陷仿真效果优 |
| **ProCAST**（法国） | 有限元法 | 热应力分析、辐射传热模拟优势突出 |
| **AnyCasting**（韩国） | 有限差分法+有限元法 | Windows平台，操作便捷，多材质多工艺适配 |
| **华铸CAE**（中国） | 有限差分法 | 适配国产压铸合金牌号，本地物性数据库齐全 |
| **FT-Star**（中国） | 有限差分法 | 缩孔缩松缺陷定量预测 |

各软件均支持充型流场、温度场与凝固过程模拟分析，并通过图形、图像、动画等方式输出模拟结果，辅助缺陷预测与工艺优化[[S12]]。

## Sources
- S39: [casting an analytical approach engineering materials and processes__4c01099d6c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84b61e9a-194c-4566-82f0-087a22230c73/resource) (`84b61e9a-194c-4566-82f0-087a22230c73`)
- S16: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45fd0c6d-e2ba-44a6-ab90-96bea7c8a687/resource) (`45fd0c6d-e2ba-44a6-ab90-96bea7c8a687`)
- S13: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/373c14ce-1359-4b83-924b-e4691374ca68/resource) (`373c14ce-1359-4b83-924b-e4691374ca68`)
- S57: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b31cd045-99d1-4556-8db0-c456c7e5bce4/resource) (`b31cd045-99d1-4556-8db0-c456c7e5bce4`)
- S7: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b93c64a-b97f-4c0a-ae34-732ca0959f43/resource) (`1b93c64a-b97f-4c0a-ae34-732ca0959f43`)
- S1: [computer aided engineering cae simulation for the design optimization of__3c0fc6c5de](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a820d3c-fd57-4e84-81eb-10cde17bdae2/resource) (`0a820d3c-fd57-4e84-81eb-10cde17bdae2`)
- S29: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6036fc9e-b11f-4f35-9c1e-d0b419319c14/resource) (`6036fc9e-b11f-4f35-9c1e-d0b419319c14`)
- S59: [链条盖压铸工艺及数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbd564cf-7be3-487b-b351-980948277482/resource) (`bbd564cf-7be3-487b-b351-980948277482`)
- S11: [压铸机压室在流热固耦合下的传热与变形分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/327e5e6e-b327-4c92-a529-56fa708f0047/resource) (`327e5e6e-b327-4c92-a529-56fa708f0047`)
- S51: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1a86997-63dc-4098-830a-09b3f5df4c1c/resource) (`a1a86997-63dc-4098-830a-09b3f5df4c1c`)
- S46: [casting an analytical approach engineering materials and processes__4c01099d6c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b650aaf-89b8-410e-ab07-47a68755aeb8/resource) (`9b650aaf-89b8-410e-ab07-47a68755aeb8`)
- S30: [汽车壳体类铸件的压铸工艺优化及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6519d5cf-2029-46ac-9f3b-668817cf57ad/resource) (`6519d5cf-2029-46ac-9f3b-668817cf57ad`)
- S34: [插秧机后桥轻量化设计与压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72141f87-1507-46bb-8d43-5c2514267e7b/resource) (`72141f87-1507-46bb-8d43-5c2514267e7b`)
- S33: [插秧机后桥轻量化设计与压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7147751e-d138-4336-91a5-1133fe4db7eb/resource) (`7147751e-d138-4336-91a5-1133fe4db7eb`)
- S4: [特种铸造与先进铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ecd606d-6a3b-4fa1-9b54-fdf86a1989b5/resource) (`0ecd606d-6a3b-4fa1-9b54-fdf86a1989b5`)
- S17: [cfd modeling and simulation in materials processing 2016 tms cfd simulat__395156bdb3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b78185d-beed-4853-bc86-dfa996fada26/resource) (`4b78185d-beed-4853-bc86-dfa996fada26`)
- S5: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f70ea36-ce52-4e3b-8342-33eaab4b0fcc/resource) (`0f70ea36-ce52-4e3b-8342-33eaab4b0fcc`)
- S20: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cd67177-a90d-4707-80b9-f1ac832013d9/resource) (`4cd67177-a90d-4707-80b9-f1ac832013d9`)
- S28: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fc549e6-bd30-494d-9539-91fb93d9a5b4/resource) (`5fc549e6-bd30-494d-9539-91fb93d9a5b4`)
- S66: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d63fdc81-9f47-4422-8dbd-664133bbb123/resource) (`d63fdc81-9f47-4422-8dbd-664133bbb123`)
- S24: [表4-4 离散方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/594a1ccb-1ca7-4d75-a4d9-7c3d1db1163a/resource) (`594a1ccb-1ca7-4d75-a4d9-7c3d1db1163a`)
- S48: [连续铸造数值模拟的流动区域与计算网格示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e386f1e-d273-4ab5-bcc8-6a51d20a20cc/resource) (`9e386f1e-d273-4ab5-bcc8-6a51d20a20cc`)
- S40: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/866c7b79-5b36-468c-8715-98c422009311/resource) (`866c7b79-5b36-468c-8715-98c422009311`)
- S42: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/924756b7-736b-4fbe-b79c-3d5aa1556d64/resource) (`924756b7-736b-4fbe-b79c-3d5aa1556d64`)
- S21: [表3-1 模拟参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f98ac6e-6773-4516-addb-096e94fb565a/resource) (`4f98ac6e-6773-4516-addb-096e94fb565a`)
- S6: [(e) 铝合金水泵座压铸充型80%模拟图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16169853-06e7-48eb-8417-80307b73168a/resource) (`16169853-06e7-48eb-8417-80307b73168a`)
- S67: [农用耕地机发动机曲轴箱体一体化压铸模浇排系统的设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d896ba89-fb1a-47b3-9ad9-a4704ee301ba/resource) (`d896ba89-fb1a-47b3-9ad9-a4704ee301ba`)
- S31: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c6f3ed6-f215-4361-9051-e755b0da952a/resource) (`6c6f3ed6-f215-4361-9051-e755b0da952a`)
- S15: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41caac48-01b0-4727-b17e-a3c5e27b9b32/resource) (`41caac48-01b0-4727-b17e-a3c5e27b9b32`)
- S65: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd34741b-b05d-4824-97fa-873b08397fb2/resource) (`cd34741b-b05d-4824-97fa-873b08397fb2`)
- S18: [轴承盖压铸缺陷分析及工艺优化_杨匀龙](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bdb7977-ce10-44a5-a125-fa3113b01f06/resource) (`4bdb7977-ce10-44a5-a125-fa3113b01f06`)
- S2: [A380铝合金零件压铸充型、凝固过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0cd2f88f-7aef-420f-946a-26fd1fa83ca4/resource) (`0cd2f88f-7aef-420f-946a-26fd1fa83ca4`)
- S55: [铝合金减震塔压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae2f05ec-463b-49f2-8d8b-7b1e0344f3c1/resource) (`ae2f05ec-463b-49f2-8d8b-7b1e0344f3c1`)
- S43: [压铸工艺与模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/927b3a0c-95e9-4e57-b902-b4a6d37f5c24/resource) (`927b3a0c-95e9-4e57-b902-b4a6d37f5c24`)
- S19: [铝合金汽车方向机壳体压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ca17ba3-032f-4c55-911a-9af50d397435/resource) (`4ca17ba3-032f-4c55-911a-9af50d397435`)
- S23: [铝合金汽车方向机壳体压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/582d8cdb-50d0-4be6-ac53-a7431160a211/resource) (`582d8cdb-50d0-4be6-ac53-a7431160a211`)
- S35: [analysis design of the gating system on high pressure die casting proces__93028dec73](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74ea42f5-75dd-4904-a5ab-e395d1b286ac/resource) (`74ea42f5-75dd-4904-a5ab-e395d1b286ac`)
- S36: [汽车壳体零件压铸工艺的优化设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/758025ef-dac1-4b66-b9fe-9093a3e46226/resource) (`758025ef-dac1-4b66-b9fe-9093a3e46226`)
- S9: [AZ91镁合金受控扩散凝固组织与反重力铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2943a202-c68c-4374-9fbe-fdc426fdfdbe/resource) (`2943a202-c68c-4374-9fbe-fdc426fdfdbe`)
- S68: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e79e1e32-ad44-4dc5-a426-43fc2cf52c18/resource) (`e79e1e32-ad44-4dc5-a426-43fc2cf52c18`)
- S32: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70725c84-f440-4b38-9c05-1ff61a3f85cb/resource) (`70725c84-f440-4b38-9c05-1ff61a3f85cb`)
- S50: [AZ91镁合金受控扩散凝固组织与反重力铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a181147a-68aa-4fe3-aec4-0c8c3a55135e/resource) (`a181147a-68aa-4fe3-aec4-0c8c3a55135e`)
- S27: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f725fd6-d405-41eb-a69a-e52ce62fa69f/resource) (`5f725fd6-d405-41eb-a69a-e52ce62fa69f`)
- S47: [american institute of aeronautics and astronautics 31st thermophysics co__84bde37c6f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c16bdc6-6200-479f-b37b-ce774873cb6e/resource) (`9c16bdc6-6200-479f-b37b-ce774873cb6e`)
- S58: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b64615da-3fc1-45de-9804-7666f9cf257d/resource) (`b64615da-3fc1-45de-9804-7666f9cf257d`)
- S14: [design of die casting process of top cover of automobile generator throu__2ef2b83fdd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d59f385-1fa0-45ba-995f-582970e69bf3/resource) (`3d59f385-1fa0-45ba-995f-582970e69bf3`)
- S60: [die casting die design based on the application of cae simulation__42797f6dd3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd1c2689-4c53-4a17-8733-d01ef9e61db4/resource) (`bd1c2689-4c53-4a17-8733-d01ef9e61db4`)
- S41: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ef55194-eb26-4bf5-8f99-7a7b59b3fbd7/resource) (`8ef55194-eb26-4bf5-8f99-7a7b59b3fbd7`)
- S54: [真空压力浸渗Cf_Al复合材料T型件的成形工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab6be752-9e8d-4d52-a6e3-0104cbc32e98/resource) (`ab6be752-9e8d-4d52-a6e3-0104cbc32e98`)
- S62: [a time dependent power law viscosity model and its application in modell__4740485700](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3893b80-4478-454e-8140-8b4d3b29b30e/resource) (`c3893b80-4478-454e-8140-8b4d3b29b30e`)
- S56: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af91a708-6114-4255-8b57-94e3aa162c45/resource) (`af91a708-6114-4255-8b57-94e3aa162c45`)
- S44: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/957856b4-035c-4f6f-bf3a-66dba655678f/resource) (`957856b4-035c-4f6f-bf3a-66dba655678f`)
- S49: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a07cf7d6-e6bc-4fcb-8278-67113ef1f426/resource) (`a07cf7d6-e6bc-4fcb-8278-67113ef1f426`)
- S22: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5578076a-f43a-4d15-bbf0-49cd85333975/resource) (`5578076a-f43a-4d15-bbf0-49cd85333975`)
- S53: [ADC12 铝合金流体属性参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa330e6f-8ca3-45c5-b871-15341ffa7eac/resource) (`aa330e6f-8ca3-45c5-b871-15341ffa7eac`)
- S63: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c647f2a0-46b6-479f-ae23-0a067d051a1b/resource) (`c647f2a0-46b6-479f-ae23-0a067d051a1b`)
- S10: [computer modelling in die casting applications__d020aa1d2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cb75566-bc2f-4a7e-9ccf-5ad9a9cb913d/resource) (`2cb75566-bc2f-4a7e-9ccf-5ad9a9cb913d`)
- S38: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b83f11e-7ab8-4661-a3fa-adc8fef3464b/resource) (`7b83f11e-7ab8-4661-a3fa-adc8fef3464b`)
- S26: [0164_733a6135ef3276ba_Phase-field_model](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b5b4b89-5e6c-4efe-adfb-317ad7d831d3/resource) (`5b5b4b89-5e6c-4efe-adfb-317ad7d831d3`)
- S69: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebf55376-41f8-47cc-bd91-b93d96e4af98/resource) (`ebf55376-41f8-47cc-bd91-b93d96e4af98`)
- S52: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a49544a0-99b5-4cc9-8647-3276eb49bd2f/resource) (`a49544a0-99b5-4cc9-8647-3276eb49bd2f`)
- S12: [大型铸件铸造工艺及数值模拟研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32eda958-1c7f-4b03-ba14-935876ca4c74/resource) (`32eda958-1c7f-4b03-ba14-935876ca4c74`)
- S64: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbcee639-0ac9-4d7f-8309-92a4c5d40853/resource) (`cbcee639-0ac9-4d7f-8309-92a4c5d40853`)