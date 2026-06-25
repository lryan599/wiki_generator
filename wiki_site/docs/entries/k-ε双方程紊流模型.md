---
version: "v1"
generated_at: "2026-06-18T12:17:02+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 39
  source_quality_score: 0.84
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

k-ε双方程紊流模型（又称k-ε模型、k-ε湍流模型、K-ε紊流模型、湍流k-ε模型、k-ε方程）是雷诺平均Navier-Stokes（RANS）涡粘模型体系下的经典双方程湍流模型[[S10,S29,S14]]。该模型通过同时求解湍动能k和湍动能耗散率ε两个独立输运方程来完成方程组的封闭，属于比零方程和单方程模型适用场景更广泛的封闭方法，是目前工业工程仿真领域应用普及率最高的湍流模型类型[[S10,S29,S14]]。模型基于涡粘假设，将雷诺应力与时均速度梯度通过涡粘系数关联，涡粘系数由湍动能k和耗散率ε的半经验关系式确定[[S4]]。在RANS涡粘湍流模型体系中，k-ε类模型被明确划归为双方程模型类别，与Spalart-Allmaras单方程模型、雷诺应力模型并列[[S34]]。

## 核心方程组与参数

### 湍动能k与耗散率ε的定义

湍动能k的物理定义为湍流脉动速度的动能统计均值：

$$k = \frac{1}{2}\left(u'^2 + v'^2 + w'^2\right)$$

该参数表征湍流脉动的总能量水平[[S4,S16]]。湍动耗散率ε的物理定义为分子粘性作用下单位时间单位质量流体的湍动能耗散量：

$$\varepsilon = \nu \overline{\frac{\partial u_i'}{\partial x_j} \frac{\partial u_i'}{\partial x_j}}$$

该参数表征湍流小尺度涡的能量耗散速率[[S4,S16]]。

### 标准k-ε模型方程

标准k-ε模型由Launder和Spalding于1974年提出[[S43]]。模型包含两个输运方程：

**湍动能k方程**（通用形式）：

$$\frac{\partial(\rho k)}{\partial t} + \frac{\partial(\rho k u_j)}{\partial x_j} = \frac{\partial}{\partial x_j}\left[\left(\mu + \frac{\mu_t}{\sigma_k}\right)\frac{\partial k}{\partial x_j}\right] + G_k + G_b - \rho\varepsilon - Y_M + S_k$$

**湍动能耗散率ε方程**（通用形式）：

$$\frac{\partial(\rho\varepsilon)}{\partial t} + \frac{\partial(\rho\varepsilon u_j)}{\partial x_j} = \frac{\partial}{\partial x_j}\left[\left(\mu + \frac{\mu_t}{\sigma_\varepsilon}\right)\frac{\partial\varepsilon}{\partial x_j}\right] + C_{1\varepsilon}\frac{\varepsilon}{k}(G_k + C_{3\varepsilon}G_b) - C_{2\varepsilon}\rho\frac{\varepsilon^2}{k} + S_\varepsilon$$

上述方程中，涡粘系数由Prandtl-Kolmogorov关系式确定[[S4]]：

$$\mu_t = C_\mu \rho \frac{k^2}{\varepsilon}$$

式中：k为湍动能，ε为湍动能耗散率，ρ为密度，t为时间，μ为运动粘度，μₜ为湍流（涡流）粘度，σₖ与σₑ为湍流Prandtl数或Schmidt数，Gₖ为速度梯度产生的湍动能项，G_b为浮力产生的湍动能项，Y_M为可压缩湍流中脉动扩散引起的波动项，Sₖ和S_ε为源项[[S1,S6,S22,S37]]。

### 标准模型常数

标准k-ε模型的五个关键经验常数由Launder和Spalding基于近壁湍流对数律、格栅后湍流衰减等经典实验标定，被《数值传热学》《湍流模型及有限分析法》等国内经典传热流体力学教材以及国际冶金领域专著统一确认[[S6,S18,S31,S43]]。

| 常数 | 符号 | 标准取值 | 说明 |
|------|------|----------|------|
| 涡粘系数 | Cμ（CD） | 0.09 | 基于近壁湍流推得 |
| ε方程产生项系数 | C1ε（C₁） | 1.44 | 由近壁对数速度剖面推得 |
| ε方程耗散项系数 | C2ε（C₁） | 1.92 | 由格栅后湍流衰减推得 |
| k的湍流Prandtl数 | σk | 1.0 | — |
| ε的湍流Prandtl数 | σε | 1.3 | — |
| 涡粘常数 | C₁ε* | 1.44 | 压铸专业文献额外注明 |

注：上表中各常数取值由多个独立来源交叉确认[[S6,S31,S43,S3,S28,S1,S42]]。

## 主要变体与适用条件

### 三类主流变体比较

k-ε模型存在三种主要的工程变体，其方程形式、模型常数和适用条件各有侧重。

| 属性 | Standard k-ε | RNG k-ε | Realizable k-ε |
|------|-------------|---------|-----------------|
| 提出者/方法 | Launder & Spalding, 1974 | Orszag & Yokhot, 重整化群理论推导 | Shih et al., 基于雷诺正应力数学约束 |
| Cμ | 0.09（固定） | 0.084 | 应变率函数，动态调整 |
| C1ε（C₁） | 1.44 | 1.42 | 含η修正项 |
| C2ε（C₁） | 1.92 | 1.68 | 1.9 |
| 核心改进 | 基准模型 | 耗散率方程附加源项R，有效普朗特数随输运率变化 | 约束雷诺正应力不可为负，ε方程含涡量脉动项 |
| 近壁处理 | 需壁面函数，y+≈30~300 | 内置低雷诺数粘性修正，可直接适配近壁区 | 需配合壁面函数或低Re模型 |
| 适用优势 | 无旋通道类常规湍流 | 复杂剪切流、大应变率流、旋涡流、射流、圆柱绕流 | 回流、分离流动、离散流动、复杂二次流 |
| 主要局限 | 高强旋流/弯曲壁面流动不准，大应变率时可能产生负正应力 | — | 适用范围广，但对某些近壁条件需额外处理 |

资料来源：[[S22,S10,S20,S37,S18,S25,S41,S17,S37,S6]]

### RNG k-ε模型的详细改进

RNG k-ε模型由Orszag和Yokhot基于重整化群数学方法推导得到，与标准模型的核心区别在于[[S37,S18]]：

1. **模型常数理论推导**：RNG k-ε方程中的常数是由理论分析得到的，而非通过试验标定。取值为Cμ=0.084，C1ε=1.42，C2ε=1.68[[S18]]。

2. **有效普朗特数修正**：αₖ = α_ε = 1.39，为湍流动能和耗散率的有效普朗特系数的倒数，可精确计算有效雷诺数对涡流输运的影响[[S18,S37]]。

3. **附加源项R**：耗散率方程中引入与η（时均应变率参数，η₀=4.337，β=0.012）相关的修正源项，使模型能更好地捕捉高应变率区域的耗散特性[[S18]]。

4. **内置低Re修正**：通过对式d(ρ²k/√(εμ))的积分处理，可直接适配低雷诺数和近壁流动问题而无需单独的壁面函数[[S37]]。

RNG k-ε模型是AnyCasting等压铸专用仿真软件默认或推荐采用的主流湍流模型，尤其适用于高压压铸中高速射流和绕流等复杂紊流场景[[S25,S41,S35,S2,S13,S40,S33]]。

### Realizable k-ε模型的特殊机制

Realizable k-ε模型的核心改进是引入对雷诺正应力的数学约束关系[[S17,S37]]：

- **动态Cμ**：在大时均应变率条件下，Cμ不再是常数，而是由公式Cμ=1/(A₀+AₛU*k/ε)动态计算（A₀=4.0，Aₛ通过φ角确定），从根本上解决原始标准k-ε模型可能产生非物理负正应力的缺陷[[S17]]。
- **修正常数**：σₖ=1.0，σ_ε=1.2，C₂=1.9[[S17]]。
- **ε方程改进**：ε方程新增与平均涡量脉动（Ω_ij）和时均应变率相关的项，对回流、分离现象和复杂二次流动的预测精度显著高于另外两类变体[[S17]]。

### 近壁处理方法

| 方法 | 适用模型 | y+要求 | 特点 |
|------|---------|--------|------|
| **壁面函数法** | 标准k-ε（高Re版） | 30~300 | 第一内节点布置在旺盛紊流区，近壁影响全部集中在第一内节点控制体内，通过经验和半经验方法确定边界节点扩散系数，以近似反映近壁区全部影响[[S22,S20]] |
| **低雷诺数修正法** | 低Re k-ε | ≈1 | 引入近壁衰减函数fμ、f₂（fμ=e^(-2.5/(1+Re_t/50))，f₂=0.3exp(-Re_t²)或fμ=e^(-3.14/(1+0.02Re)²)，f₂=1-0.3e^(-Re_t²)），将分子粘性影响直接耦合到输运方程中，可直接解析粘性底层湍流分布[[S21,S20,S10]] |
| **RNG内置处理** | RNG k-ε | 可较低 | 模型内置低雷诺数粘性修正，能直接应用于近壁区域[[S25,S41,S37]] |

## 在压铸工艺中的角色

### 高压压铸充型流动模拟

高压压铸充型过程金属液雷诺数通常超过紊流临界值，k-ε双方程模型是压铸充型紊流模拟领域工程上广泛采用的紊流描述模型[[S1,S42,S3,S28]]。该模型的输运方程明确定义了湍流动能k、紊流动能耗散率ε、紊流黏度μₜ等核心物理量的计算规则[[S1,S42]]。

在三大主流压铸仿真软件中，k-ε模型的使用情况如下[[S35,S2,S11,S23,S26,S13,S40,S33]]：

- **AnyCasting**：前处理中将k-ε双方程紊流模型列为压铸充型流动计算的默认流体流动模型，可根据用户需求切换为RNG k-ε扩展模型，适配高压压铸中高速射流、绕流等复杂紊流场景[[S35,S2,S25]]。
- **FLOW-3D Cast**：内置标准k-ε、RNG k-ε、k-ω三类k-ε族紊流模型，工程实践中优先选用RNG k-ε模型处理常规高压压铸场景，软件默认开启Passive Air entrainment被动卷气计算模式[[S13,S40,S33]]。
- **ProCAST**：高压压铸充型流动模块默认耦合k-ε双方程紊流模型，可自动适配高压压铸过程的流场-温度场耦合求解流程，配套提供压铸场景下铸件与模具界面换热系数的工程推荐设置规则[[S11,S23,S26]]。

配合上述软件求解，充型过程采用SOLA-VOF方法进行动量与质量守恒方程耦合求解及自由表面追踪，已在压铸模拟中得到工程验证[[S25,S1]]。

### 卷气缺陷预测

k-ε类紊流模型可与气液两相流模型耦合，支撑高压压铸场景下卷气缺陷的定量预测[[S30,S9,S25]]。基于紊流流场的高精度计算结果，可定位流场漩涡区、负压区的分布，追踪宏观气泡与微观弥散气泡的生成演化过程，实现铸件内部气孔缺陷位置的高精度预判[[S30,S9,S25]]。卷气缺陷往往发生在负压区或漩涡区域，而单相流动的k-ε模拟可以将这些区域反映出来。若充型过程中某些部位长时间出现负压或漩涡，即可认定为卷气夹杂的危险区域[[S30]]。

### 冷隔与温降预测

耦合k-ε紊流模型的充型-传热耦合仿真，可同步计算充型过程中金属液的温降分布以及不同方向流股交汇位置的温度差，从而准确预判冷隔缺陷的潜在生成区域[[S24,S36]]。相关仿真结果已在锌合金、铝合金压铸件冷流缺陷防控的行业通用导则中得到验证应用[[S24,S36]]。当充型结束时金属温度低于某一阈值即可能发生冷隔缺陷，这一温度分布可借助k-ε模型耦合仿真进行估算[[S24,S36]]。

### 工艺参数优化

k-ε模型支持在不同压射参数下对充型状态、冷却状态、缺陷及卷气情况进行系统性模拟对比。基于该模型的研究表明，当一次快压射速度为1.5 m/s时，仿真输出铸件几乎无缺陷、无卷气，验证了湍流模型在压铸工艺参数优化中的工程有效性[[S39]]。

## 与相关模型的对比

### RANS框架内对比

| 模型 | 方程数量 | 核心机制 | 优势场景 | 局限 |
|------|----------|---------|----------|------|
| **Standard k-ε** | 双方程 | 求解k和ε输运方程 | 管道、通道等无旋常规湍流 | 逆压梯度/边界层分离预测差，高强旋流/弯曲壁面不适用 |
| **RNG k-ε** | 双方程 | k-ε基础上理论推导修正ε方程 | 复杂剪切流、大应变率、旋涡流、射流 | — |
| **Realizable k-ε** | 双方程 | 约束正应力外加动态Cμ | 回流、分离流、二次流 | — |
| **Standard k-ω** | 双方程 | 求解k和ω（比耗散率） | 粘性底层积分求解，逆压梯度边界层、流动分离 | 对流场外界自由流取值高度敏感，通用性受限 |
| **SST k-ω** | 双方程 | 近壁k-ω+远场k-ε混合 | 逆压梯度分离流、广泛通用 | 实现复杂度高于单模型 |
| **Spalart-Allmaras** | 单方程 | 修正涡粘输运方程 | 航空航天壁面流动、不利逆压梯度边界层 | 自由剪切流（射流）误差大，通用性弱于k-ε |

资料来源：[[S8,S41,S10,S6,S18,S17]]

### 与高级湍流模拟方法的过渡关系

相较于k-ε类RANS模型仅求解时均流动、过滤所有湍流脉动细节的特性，其与高级方法的关系如下[[S29,S15,S38]]：

- **直接数值模拟（DNS）**：直接求解三维N-S方程获取瞬时流场，无需模型封闭，但计算资源要求极高，目前仅能处理低雷诺数简单流动，无法应用于实际工程问题[[S29]]。
- **大涡模拟（LES）**：采用空间滤波分离大尺度可解析涡和小尺度亚格子涡，能捕捉非稳态湍流脉动的多尺度演化特征，但对网格分辨率和计算资源要求远高于k-ε模型[[S29,S15,S38]]。
- **脱体涡模拟（DES）**：RANS与LES的混合方法，近壁区采用RANS计算、远场分离涡区域采用LES计算，兼顾两者的优势和计算成本平衡[[S38]]（注：基于资料中关于RANS与LES关系的讨论，此归类为一般性技术过渡关系）。

## 关键参数设置建议（压铸模拟）

### 入口湍流参数估算

在压铸充型模拟中，入口湍流强度与湍流长度尺度的常用估算方法如下（基于压铸资料中的通用经验）：

- **湍流强度I**：压铸充型过程中金属液流速高、雷诺数大（通常>>10³数量级[[S22]]），入口湍流强度应依据雷诺数和充型工况合理设定。
- **湍流长度尺度l**：常取入口几何特征尺寸（如内浇口直径或浇道水力直径）的约0.07倍。

### 常用边界条件设置建议

压铸模拟中典型的边界条件设置包括[[S13,S23,S26,S25]]：

- **速度入口**：设置压射速度（如1.5~1.6 m/s），注意速度方向设置[[S13,S23]]。
- **压力出口**：排气边界、溢流槽出口。
- **壁面条件**：模具壁面需设定界面换热系数。铸件与模具之间h≈1000~2093.5 W/(m²·K)；模具与模具之间h≈1000 W/(m²·K)；模具与空气h≈10 W/(m²·K)（均为工程推荐值）[[S23,S26,S25]]。

## 可视化证据

### 充型过程液流形态模拟

k-ε双方程紊流模型可用于模拟铸造充型过程在不同时刻的液流形态分布。下图为《中国材料工程大典》第19卷收录的基于k-ε双方程模型计算得到的铸造充型过程0.75 s、1.00 s、1.25 s三个时间点的液流形态[[S27]]。

![k-ε双方程模型模拟铸造充型过程不同时间的液流形态](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b02dfc99-9ee6-4493-bc1d-80b5f51a1393/resource)

### 模型控制方程体系

k-ε湍流模型的控制方程体系在冶金领域连铸中间包钢液流动仿真中已有成熟的数学表达。下图为应用于连铸中间包钢液流动仿真的k-ε湍流模型全套数学控制方程[[S32]]。

![用于连铸中间包钢液流动仿真的k-ε湍流模型控制方程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd3235e9-307a-4987-b47e-fc8062880a7e/resource)

## Sources
- S10: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51877fb7-2102-4137-8f00-1abb68bacf40/resource) (`51877fb7-2102-4137-8f00-1abb68bacf40`)
- S29: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c787a866-9897-4354-b05e-1dccc39cf3e0/resource) (`c787a866-9897-4354-b05e-1dccc39cf3e0`)
- S14: [continuous casting of non ferrous metals and alloys proceedings of a symposium__4a45e8aea3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e89e585-9e8a-4211-9b39-ccf5343c2191/resource) (`6e89e585-9e8a-4211-9b39-ccf5343c2191`)
- S4: [continuous casting of non ferrous metals and alloys proceedings of a symposium__4a45e8aea3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0cbc4d88-ab77-4902-b3f3-693b1c24fb2d/resource) (`0cbc4d88-ab77-4902-b3f3-693b1c24fb2d`)
- S34: [表3-1 雷诺时均方法模型介绍](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddc7c4cc-91b2-48da-bbb9-ffac54b0ddee/resource) (`ddc7c4cc-91b2-48da-bbb9-ffac54b0ddee`)
- S16: [考虑螺旋离心泵水力性能及铸造成型的多目标优化设计研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7686fc11-e5be-4720-98e8-2ff73f1e2966/resource) (`7686fc11-e5be-4720-98e8-2ff73f1e2966`)
- S43: [advanced physical chemistry for process metallurgy__40b302dbe5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe0c9182-9d92-4077-9b13-ba86374f4b7f/resource) (`fe0c9182-9d92-4077-9b13-ba86374f4b7f`)
- S1: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01302f51-aba1-4d87-8356-d6d5ca51f876/resource) (`01302f51-aba1-4d87-8356-d6d5ca51f876`)
- S6: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34fff431-dce0-439a-a6ce-b989c5813875/resource) (`34fff431-dce0-439a-a6ce-b989c5813875`)
- S22: [SCR7000连铸过程温度场模拟与水冷系统优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93f4d483-e474-4aaa-8c82-e187874cfd33/resource) (`93f4d483-e474-4aaa-8c82-e187874cfd33`)
- S37: [改善砂芯干燥炉干燥质量的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6dd8140-3c08-42c7-8fd1-5a9ecbc08a86/resource) (`e6dd8140-3c08-42c7-8fd1-5a9ecbc08a86`)
- S18: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a66e914-20c5-46c1-828c-1e804646ce17/resource) (`8a66e914-20c5-46c1-828c-1e804646ce17`)
- S31: [表2.1 k-ε双方程模型相应的经验参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6a36b25-6eeb-4e48-a20f-9a0aea24ae6c/resource) (`d6a36b25-6eeb-4e48-a20f-9a0aea24ae6c`)
- S3: [表3.1 k-ε双方程模型中的常数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/090a24b5-6017-47fa-8dc0-ef620caabe15/resource) (`090a24b5-6017-47fa-8dc0-ef620caabe15`)
- S28: [表2.1 k-ε双方程模型中参数的经验值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b41247ac-c05a-493f-b55b-b7b52b43bd95/resource) (`b41247ac-c05a-493f-b55b-b7b52b43bd95`)
- S42: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fde8524a-2e4f-4d69-b303-21764535cabc/resource) (`fde8524a-2e4f-4d69-b303-21764535cabc`)
- S20: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90801b90-36c2-4d1a-a3df-141f6518593e/resource) (`90801b90-36c2-4d1a-a3df-141f6518593e`)
- S25: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf/resource) (`a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf`)
- S41: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7/resource) (`fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7`)
- S17: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8465bffe-b784-49a1-8b5f-e3d43522e167/resource) (`8465bffe-b784-49a1-8b5f-e3d43522e167`)
- S35: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S2: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06e30961-bad3-4882-a77b-4fb272a32c2c/resource) (`06e30961-bad3-4882-a77b-4fb272a32c2c`)
- S13: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/689e0bc6-e395-4555-96a5-cd7fddb37759/resource) (`689e0bc6-e395-4555-96a5-cd7fddb37759`)
- S40: [铝合金发动机缸体低压铸造缺陷控制的工艺及机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb53e57f-983b-4bd0-946a-c31383248f32/resource) (`fb53e57f-983b-4bd0-946a-c31383248f32`)
- S33: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd933688-2e6d-4234-acbc-123429e71dec/resource) (`dd933688-2e6d-4234-acbc-123429e71dec`)
- S21: [立式连铸大方坯结晶器内热流耦合模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90a75e74-a27e-4666-8f21-c4e5d25f9779/resource) (`90a75e74-a27e-4666-8f21-c4e5d25f9779`)
- S11: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61c24028-9370-4819-9603-27dffb5c1618/resource) (`61c24028-9370-4819-9603-27dffb5c1618`)
- S23: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/957856b4-035c-4f6f-bf3a-66dba655678f/resource) (`957856b4-035c-4f6f-bf3a-66dba655678f`)
- S26: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af91a708-6114-4255-8b57-94e3aa162c45/resource) (`af91a708-6114-4255-8b57-94e3aa162c45`)
- S30: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb85f63d-d95b-405f-8196-0c984b6582a6/resource) (`cb85f63d-d95b-405f-8196-0c984b6582a6`)
- S9: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cf4c963-9cad-4d4e-986b-e7436cbcab54/resource) (`4cf4c963-9cad-4d4e-986b-e7436cbcab54`)
- S24: [cold flow defects in zinc die casting prevention criteria using simulati__ac8154fe3a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e5a85d4-3062-47ba-9404-eced2e9d4d69/resource) (`9e5a85d4-3062-47ba-9404-eced2e9d4d69`)
- S36: [cold flow defects in zinc die casting prevention criteria using simulati__ac8154fe3a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6573667-6fa5-4e12-ba53-3a5fd0b75324/resource) (`e6573667-6fa5-4e12-ba53-3a5fd0b75324`)
- S39: [表4-5 高压压铸和不同一次快压射速度下半固态压铸的模拟结果汇总表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f899c7cc-db95-43f7-9450-d5f24be57fda/resource) (`f899c7cc-db95-43f7-9450-d5f24be57fda`)
- S8: [铝合金车轮低压铸造模具冷却系统界面换热机理分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47a5e5bc-9940-4223-9647-6142cc98bb46/resource) (`47a5e5bc-9940-4223-9647-6142cc98bb46`)
- S15: [板坯结晶器电磁搅拌条件下钢液多相流动及夹杂物捕获的大涡模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6eea0344-e6cf-45fd-9ef3-1305b96fb85a/resource) (`6eea0344-e6cf-45fd-9ef3-1305b96fb85a`)
- S38: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed51faa8-7858-45aa-b3b4-cba8cadc1113/resource) (`ed51faa8-7858-45aa-b3b4-cba8cadc1113`)
- S27: [K-ε双方程模型模拟铸造充型过程不同时间的液流形态](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b02dfc99-9ee6-4493-bc1d-80b5f51a1393/resource) (`b02dfc99-9ee6-4493-bc1d-80b5f51a1393`)
- S32: [k-ε turbulence model equations for continuous casting tundish melt flow simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd3235e9-307a-4987-b47e-fc8062880a7e/resource) (`dd3235e9-307a-4987-b47e-fc8062880a7e`)