---
version: "v1"
generated_at: "2026-06-18T12:39:11+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 44
  source_quality_score: 0.85
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

Navier-Stokes方程（纳维尔-斯托克斯方程，简称N-S方程）是描述黏性流体运动的核心控制方程，在压铸领域被广泛应用于充型与流动数值模拟[[S20,S60]]。该方程基于牛顿第二定律建立，通过对流体微团进行受力分析，将微团所受合外力（体积力、压力、黏性力）与微团动量变化率建立对等关系，结合牛顿流体本构方程封闭剪切应力未知项，最终得到描述黏性流体动量守恒的偏微分方程组[[S15,S57,S19]]。在压铸充型数值模拟中，N-S方程与连续性方程、能量方程共同构成铸造充型流动场仿真的核心数学模型[[S14,S16]]。

## 物理含义与基本形式

对于不可压缩黏性流体（密度ρ为常数，速度散度为零），N-S方程的三维直角坐标分量表达式为[[S12,S51,S60]]：

$$\rho\left(\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} + w\frac{\partial u}{\partial z}\right) = -\frac{\partial p}{\partial x} + \rho g_x + \mu\nabla^{2}u$$

$$\rho\left(\frac{\partial v}{\partial t} + u\frac{\partial v}{\partial x} + v\frac{\partial v}{\partial y} + w\frac{\partial v}{\partial z}\right) = -\frac{\partial p}{\partial y} + \rho g_y + \mu\nabla^{2}v$$

$$\rho\left(\frac{\partial w}{\partial t} + u\frac{\partial w}{\partial x} + v\frac{\partial w}{\partial y} + w\frac{\partial w}{\partial z}\right) = -\frac{\partial p}{\partial z} + \rho g_z + \mu\nabla^{2}w$$

式中各物理项含义明确[[S12,S58,S46]]：

| 方程项 | 物理含义 |
|--------|----------|
| 左侧各项 | **惯性力项**，表征流体微团的全加速度与密度的乘积 |
| −∂p/∂x项 | **压力梯度项**，表征作用于微团的静压强梯度作用力 |
| μ∇²u项 | **黏性力项**，由拉普拉斯算子作用于速度分量乘以动力黏度组成，表征流体内摩擦剪切作用力 |
| ρg项 | **体积力项**，常见类型包括重力、电磁力、浮升力等 |

该方程耦合连续性方程 ∂u/∂x + ∂v/∂y + ∂w/∂z = 0 后，构成不可压缩黏性流体流动的封闭控制方程组[[S17,S48,S42]]。

## 在压铸充型模拟中的作用

在高压压铸（HPDC）充型数值模拟中，通常将金属液假定为不可压缩的牛顿流体，其流动遵循质量守恒与动量守恒定律，对应的数学表达即为连续性方程与Navier-Stokes方程[[S17,S48]]。完整的铸造充型与凝固过程数学控制模型由三类核心方程耦合构成[[S16,S41]]：

1. **动量守恒方程（N-S方程）**—求解速度场与压力场
2. **质量守恒方程（连续性方程）**—保证流动的不可压缩约束
3. **能量守恒方程**—实现流动与温度场的耦合计算

首先通过数值方法联立求解N-S方程与连续性方程得到流场的速度与压力分布，再将该结果代入能量方程实现流动与温度场的耦合计算，同时配合体积函数（VOF）方程完成自由表面的追踪，最终得到完整的充型-温度场结果，作为后续凝固模拟的初始输入[[S16,S5]]。

求解N-S方程的主流数值方法包括SIMPLE法、MAC法、SMAC法、SOLA-VOF法四类[[S35,S23]]。其中SOLA-VOF法通过调整网格压力逐步迭代使速度场满足连续性方程要求，无需反复迭代泊松方程，求解效率更高，是当前压铸充型模拟中应用最广泛的求解方案[[S23,S61]]。

![压铸充型流场模拟SOLA算法求解N-S方程流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff929f5a-25d9-46e1-b148-ad33bd805375/resource)

图：SOLA算法求解N-S方程的完整流程——从初始化流场开始，通过求解N-S方程得到试算速度，经压力校正、速度校正循环迭代至满足连续性条件，最终判断是否达到稳态[[S65]]。

## 形式分类

### 全Navier-Stokes方程（DNS形式）

直接求解瞬时Navier-Stokes方程（Direct Numerical Simulation, DNS）的不可压缩动量方程表达式为[[S27]]：

$$\frac{\partial u_i}{\partial t} + u_j\frac{\partial u_i}{\partial x_j} = -\frac{1}{\rho}\frac{\partial p}{\partial x_i} + \nu\frac{\partial^{2}u_i}{\partial x_j\partial x_j} + f_i$$

该形式无需引入额外湍流封闭模型，理论上可直接解析所有瞬态湍流细节。然而DNS对计算算力、网格分辨率要求极高，当前技术条件下仅适用于低雷诺数基础湍流研究，无法直接落地到常规高压压铸工程仿真场景[[S27,S39]]。

### 雷诺平均Navier-Stokes（RANS）方程

RANS方程是对全N-S方程做时间平均处理得到的导出形式，所有瞬时流动变量被分解为时均量与脉动量的叠加[[S27,S28]]：

$$\frac{\partial \langle u_i\rangle}{\partial t} + \langle u_j\rangle\frac{\partial \langle u_i\rangle}{\partial x_j} = -\frac{1}{\rho}\frac{\partial \langle p\rangle}{\partial x_i} + \nu\frac{\partial^{2}\langle u_i\rangle}{\partial x_j\partial x_j} - \frac{\partial \langle u_i' u_j'\rangle}{\partial x_i} + \langle f_i\rangle$$

相比原始全N-S方程，RANS方程新增了**雷诺应力项** −∂⟨u'_i u'_j⟩/∂x_i，导致方程组不封闭，必须引入额外湍流模型才能完成求解[[S27]]。RANS类方法通过时间平均过滤掉细小湍流脉动信息，显著降低仿真计算开销，是当前高压压铸高速湍流仿真的工业主流方案[[S28,S31]]。

### 压铸湍流模拟常用简化形式

高压压铸场景下，金属液充型速度通常可达10~30 m/s，雷诺数通常高于10⁵，充型过程处于强紊流状态[[S50,S11]]。常规应用中多采用RANS结合k-ε双方程湍流模型进行简化求解[[S63]]：

| 模型类别 | 关键特征 | 适用场景 |
|----------|----------|----------|
| 标准k-ε | 最广泛应用的双方程模型，引入湍流动能k和湍动能耗散率ε两个输运方程 | 管道、通道类湍流模拟 |
| RNG k-ε | 基于重整化群理论，对近壁区流动、高应变率射流适配性优于标准k-ε | 压铸高速射流充型场景 |
| Realizable k-ε | 湍流黏度根据湍流场函数求解而非经验常数，适用范围更广 | 更广泛的湍流流动场景 |

通过 μ_t = C_μ ρ k²/ε 计算湍流黏度完成RANS方程组封闭[[S63,S38,S62]]。

## 关键参数与边界条件

### 物性参数

压铸场景下求解N-S方程的核心物性参数为熔融金属的密度ρ和动力黏度μ。常规全液态压铸铝合金场景下，金属黏度通常取10⁻³ Pa·s，属于恒定值的牛顿流体假设范畴[[S44,S6]]。

### 边界条件

压铸数值模拟中求解N-S方程需定义三类核心边界条件[[S25,S36]]：

| 边界类型 | 速度条件 | 压力/其他条件 |
|----------|----------|---------------|
| 入流边界（浇道口） | 浇道速度由PQ²图计算得出 | 入口压力设置为对应压射压力；湍流入口紊动能取流体总动能的1%~10% |
| 壁面边界（模具壁） | 法向速度为零，切向速度近似为零（无滑移） | 壁面K、ε法向梯度近似为零；物性参数取相邻内单元平均值 |
| 自由表面（出口） | 满足连续性方程的速度边界 | 自由表面压力等于环境参考压强（高雷诺数下可忽略黏度对表面应力的影响） |

### 工艺参数映射

压铸工艺参数与N-S方程求解存在直接映射关系[[S9,S31]]：
- 压铸机的**注射（压射）速度**直接映射为入流边界的入口速度项
- **压射压力**直接作为入流边界的入口压力项
- **模具温度**直接映射为壁面边界的温度初始条件

三者共同完成整个控制方程组的定解配置。

## 应用范围与局限性

### 适用范围

N-S方程在以下压铸场景中具有成熟的工程适用性[[S11,S22]]：
- **常规液态高压压铸**：金属液作为不可压缩牛顿流体，在高速充型（10~30 m/s）条件下搭配RANS湍流模型可获得符合工程精度的流场预测
- **充型流动可视化**：基于N-S方程求解得到的速度场、压力场云图可直观展示充型顺序、速度分布，预测卷气、冷隔等缺陷风险

压铸充型流动数值模拟以Navier-Stokes动量守恒方程和质量守恒方程为核心控制方程进行求解，是所有压铸充型流动仿真可视化结果的理论数学基础[[S22]]。

![基于N-S方程求解得到的压铸件充型全过程流场模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe3339de-c4fa-4391-be71-24cda5d525fa/resource)

图：AnyCasting软件生成的压铸件完整充型过程流场模拟结果，直观展示金属液在型腔内的流动分布，可用于充型平稳性分析和卷气风险预判[[S64]]。

### 局限性

**1. 牛顿流体假设的局限**

高压压铸高速湍流场景下，直接求解瞬时Navier-Stokes方程需要远高于常规工业场景的网格分辨率，计算成本极高，现有工程应用中通常必须搭配RANS类湍流模型进行简化修正[[S11,S18]]。此外，标准牛顿流体假设仅适用于全液态金属；半固态压铸场景中，半固态金属浆料的黏度比常规全液态金属高出3个数量级以上，且黏度随剪切速率升高而降低，表现出典型的剪切变稀非牛顿（伪塑性）流动行为[[S53,S10]]。

**2. 半固态压铸的非牛顿修正需求**

直接使用常黏度N-S方程求解半固态压铸会得到完全失准的充型结果，必须搭配Carreau-Yasuda、幂律等非牛顿黏度模型对N-S方程中的黏度项进行修正[[S4]]。两种流态的充型差异显著[[S55,S26]]：

| 对比维度 | 常规液态压铸（牛顿流体） | 半固态压铸（非牛顿流体） |
|----------|---------------------------|---------------------------|
| 黏度量级 | ~10⁻³ Pa·s | >1 Pa·s（高3个数量级以上） |
| 流动形态 | 湍流，易飞溅、卷气 | 平稳层流，流动前沿平直 |
| 充型特征 | 易产生浇不足、裹气、夹杂 | 层流充型，低缺陷优势 |
| N-S方程适用性 | 可直接使用（需配合湍流模型） | 需修正黏度项（引入非牛顿本构） |

## 关于张子健等人的研究

多轮针对国内作者张子健的压铸、铸造流动模拟、N-S方程相关文献定向检索，未检索到署名该作者的符合要求的公开学术成果记录[[S29,S20,S8]]。该线索在当前知识库中无法验证，请在获取可靠来源后补充。

## Sources
- S20: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/620aba15-6b0c-486d-863d-a492401df2ef/resource) (`620aba15-6b0c-486d-863d-a492401df2ef`)
- S60: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f51bc577-caf1-4849-8437-19ed03e684c6/resource) (`f51bc577-caf1-4849-8437-19ed03e684c6`)
- S15: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53da7cd0-40b5-490e-932f-a9e57eb7b0fa/resource) (`53da7cd0-40b5-490e-932f-a9e57eb7b0fa`)
- S57: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3b86ffc-9e0b-47f2-8261-2dec4a201149/resource) (`e3b86ffc-9e0b-47f2-8261-2dec4a201149`)
- S19: [铝合金压铸充型流态动态演变过程研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ebd11a2-6acb-47aa-ad9b-5c5df943ebc3/resource) (`5ebd11a2-6acb-47aa-ad9b-5c5df943ebc3`)
- S14: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b87d010-3b1d-4cbc-851d-cf5a79c7db17/resource) (`4b87d010-3b1d-4cbc-851d-cf5a79c7db17`)
- S16: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5aabe43c-77be-406e-9cb6-e19a44b2869f/resource) (`5aabe43c-77be-406e-9cb6-e19a44b2869f`)
- S12: [casting an analytical approach engineering materials and processes__4c01099d6c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3f517771-193d-4c36-85c2-4b9555c67ac7/resource) (`3f517771-193d-4c36-85c2-4b9555c67ac7`)
- S51: [复杂铸件3D打印砂型成形工艺优化及低压铸造工艺验证的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b45a51a1-7e99-4ed5-ad0d-5ff012b21c00/resource) (`b45a51a1-7e99-4ed5-ad0d-5ff012b21c00`)
- S58: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e675decf-60e9-46cf-aa0b-1a16ccc61b9f/resource) (`e675decf-60e9-46cf-aa0b-1a16ccc61b9f`)
- S46: [casting an analytical approach engineering materials and processes__4c01099d6c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b650aaf-89b8-410e-ab07-47a68755aeb8/resource) (`9b650aaf-89b8-410e-ab07-47a68755aeb8`)
- S17: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5bd6bc4d-2d61-43b1-b71c-5c2caafe73b1/resource) (`5bd6bc4d-2d61-43b1-b71c-5c2caafe73b1`)
- S48: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1a86997-63dc-4098-830a-09b3f5df4c1c/resource) (`a1a86997-63dc-4098-830a-09b3f5df4c1c`)
- S42: [压铸与液态模锻复合成形车用空调头盖技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/904de3cb-f8b0-4161-97ed-992f98bd01b1/resource) (`904de3cb-f8b0-4161-97ed-992f98bd01b1`)
- S41: [铸造数值模拟软件技术及应用进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8fbc5469-8b94-4564-9b38-8a4218c437d4/resource) (`8fbc5469-8b94-4564-9b38-8a4218c437d4`)
- S5: [现代模具设计基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/275aba7f-6a83-44b3-98ef-d35bf97242a0/resource) (`275aba7f-6a83-44b3-98ef-d35bf97242a0`)
- S35: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b7c68ca-c779-40dd-b2d9-70f943b67af2/resource) (`7b7c68ca-c779-40dd-b2d9-70f943b67af2`)
- S23: [材料热加工过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69168934-2f9b-43de-8c2a-1ed7ec199de2/resource) (`69168934-2f9b-43de-8c2a-1ed7ec199de2`)
- S61: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f75c0f01-61a3-4342-959e-b373e6f28dc5/resource) (`f75c0f01-61a3-4342-959e-b373e6f28dc5`)
- S65: [金属液流场模拟程序流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff929f5a-25d9-46e1-b148-ad33bd805375/resource) (`ff929f5a-25d9-46e1-b148-ad33bd805375`)
- S27: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d7c0630-ad7f-4601-8e02-f357455bc7f5/resource) (`6d7c0630-ad7f-4601-8e02-f357455bc7f5`)
- S39: [铝合金车轮低压铸造模具冷却系统界面换热机理分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bd2950e-4894-4624-a2dd-da6172edec18/resource) (`8bd2950e-4894-4624-a2dd-da6172edec18`)
- S28: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6eea0344-e6cf-45fd-9ef3-1305b96fb85a/resource) (`6eea0344-e6cf-45fd-9ef3-1305b96fb85a`)
- S31: [插秧机后桥轻量化设计与压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72141f87-1507-46bb-8d43-5c2514267e7b/resource) (`72141f87-1507-46bb-8d43-5c2514267e7b`)
- S50: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b31cd045-99d1-4556-8db0-c456c7e5bce4/resource) (`b31cd045-99d1-4556-8db0-c456c7e5bce4`)
- S11: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34df93ec-8e29-4285-9ea0-2a8a361b7d95/resource) (`34df93ec-8e29-4285-9ea0-2a8a361b7d95`)
- S63: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fde8524a-2e4f-4d69-b303-21764535cabc/resource) (`fde8524a-2e4f-4d69-b303-21764535cabc`)
- S38: [连铸液相穴钢液中非金属夹杂物碰撞长大的数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/830fd692-8cf0-4ec9-8940-72132d12b4fa/resource) (`830fd692-8cf0-4ec9-8940-72132d12b4fa`)
- S62: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7/resource) (`fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7`)
- S44: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96c9d241-5936-41f7-9461-8f33e17a229e/resource) (`96c9d241-5936-41f7-9461-8f33e17a229e`)
- S6: [基于ProCAST的非牛顿流体压铸过程模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27c8dfd4-483a-4d9c-8cd4-12c85bb30b89/resource) (`27c8dfd4-483a-4d9c-8cd4-12c85bb30b89`)
- S25: [表 4-2 边界条件; Tab.4-2 Boundary conditions](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b782ee3-e285-45d0-8d51-3afe12c46e4d/resource) (`6b782ee3-e285-45d0-8d51-3afe12c46e4d`)
- S36: [液态成型工艺及cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bb7e0eb-2c0c-4b67-bb6c-feeb307cbccc/resource) (`7bb7e0eb-2c0c-4b67-bb6c-feeb307cbccc`)
- S9: [插秧机后桥轻量化设计与压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d4c0ad3-0a2a-48fc-be1e-90724a6acda3/resource) (`2d4c0ad3-0a2a-48fc-be1e-90724a6acda3`)
- S22: [模具设计基础及模具cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/66005360-110f-4900-8456-0fd10209ef9f/resource) (`66005360-110f-4900-8456-0fd10209ef9f`)
- S64: [压铸件充型过程流场模拟图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe3339de-c4fa-4391-be71-24cda5d525fa/resource) (`fe3339de-c4fa-4391-be71-24cda5d525fa`)
- S18: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c9f0cc1-4de4-4f21-8438-2a2d06698c86/resource) (`5c9f0cc1-4de4-4f21-8438-2a2d06698c86`)
- S53: [普通高等教育“十三五”规划教材 特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5531dad-f3d0-40c6-bdb2-dac9ab8d1fed/resource) (`c5531dad-f3d0-40c6-bdb2-dac9ab8d1fed`)
- S10: [基于ProCAST的非牛顿流体压铸过程模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f598373-0b06-4385-82d2-32ef35ba2d23/resource) (`2f598373-0b06-4385-82d2-32ef35ba2d23`)
- S4: [半固态金属成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b39ee3a-68fe-449b-ac3e-344927394cf0/resource) (`0b39ee3a-68fe-449b-ac3e-344927394cf0`)
- S55: [development of semi solid die casting process technology for aluminium a__9c5833baa9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d22f44e3-858e-47c8-9cb5-4dd5daba0c4b/resource) (`d22f44e3-858e-47c8-9cb5-4dd5daba0c4b`)
- S26: [基于ProCAST的非牛顿流体压铸过程模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d7649e9-3462-43f8-85ed-f047d5ea8791/resource) (`6d7649e9-3462-43f8-85ed-f047d5ea8791`)
- S29: [插秧机后桥轻量化设计与压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7147751e-d138-4336-91a5-1133fe4db7eb/resource) (`7147751e-d138-4336-91a5-1133fe4db7eb`)
- S8: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2931a091-5ed4-4540-9ee5-864498317345/resource) (`2931a091-5ed4-4540-9ee5-864498317345`)