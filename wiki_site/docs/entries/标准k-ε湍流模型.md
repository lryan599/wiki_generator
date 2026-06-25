---
version: "v1"
generated_at: "2026-06-18T14:22:46+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 28
  source_quality_score: 0.85
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 概述

标准k-ε湍流模型是基于Boussinesq涡粘性假设构建的雷诺平均Navier-Stokes（RANS）半经验两方程模型，由Jones和Launder于1972年提出，并于1974年经Launder和Spalding完善定型[[S11,S36]]。该模型依据局部湍流各向同性假设，通过求解流动能耗散率（ε）两个独立输运方程来求解湍流粘性系数μ_t，进而闭合时均N-S方程组[[S17,S33]]。作为工程计算流体动力学（CFD）领域应用最广泛的湍流模型之一，它在各类工业流动仿真中拥有超过二十年的应用积累[[S26,S15]]。

## 命名与分类定位

标准k-ε模型属于涡粘模型（eddy-viscosity model）大类下的两方程模型。涡粘模型均基于湍流脉动可通过修正流体粘度来近似表达的基本思想，其中标准k-ε模型直接建立湍动能（k）和耗散率（ε）两个物理量的偏微分方程，形成完整的两方程封闭体系。与之平行的RANS两方程涡粘模型体系，还包括RNG k-ε模型和可实现的k-ε模型等改进方案，这些模型均在标准k-ε框架基础上进行了不同程度的数学约束或系数修正[[S17,S32]]。

标准k-ε模型与其他两方程模型之间的核心区别与联系可归纳如下[[S32,S35]]：

- **RNG k-ε模型**：基于重整化群的数学方法推导，在ε方程中新增降低湍流粘性过预测的附加源项，并能更好地处理低雷诺数和近壁流动问题；
- **可实现的k-ε模型**：通过对雷诺应力施加数学约束的方式，解决了标准k-ε模型在大应变率条件下出现非物理的负正应力问题；
- **SST k-ω模型**：近壁区域采用对低雷诺数流动处理更好的k-ω模型，远场自动过渡为标准k-ε模型，兼具近壁流动模拟精度和远场计算效率。

## 核心数学描述

### 控制方程体系

标准k-ε模型的原始形式由湍动能k输运方程和湍动能耗散率ε输运方程两个偏微分方程组成。在不可压缩流动假设下，写成指标形式的通用方程如下[[S36]]：

**湍动能k输运方程**：

\[\frac{\partial k}{\partial t} + U_i \frac{\partial k}{\partial x_i} = \frac{\partial}{\partial x_i} \left( \frac{\nu_t}{\sigma_k} \frac{\partial k}{\partial x_i} \right) + \nu_t \left( \frac{\partial U_i}{\partial x_j} + \frac{\partial U_j}{\partial x_i} \right) \frac{\partial U_i}{\partial x_j} - \varepsilon\]

**湍动能耗散率ε输运方程**：

\[\frac{\partial \varepsilon}{\partial t} + U_i \frac{\partial \varepsilon}{\partial x_i} = \frac{\partial}{\partial x_i} \left( \frac{\nu_t}{\sigma_\varepsilon} \frac{\partial \varepsilon}{\partial x_i} \right) + C_{1} \frac{\varepsilon}{k} P - C_{2} \frac{\varepsilon^2}{k}\]

湍流粘性系数由下式封闭[[S36]]：

\[\mu_t = C_\mu \rho \frac{k^2}{\varepsilon}\]

考虑可压缩效应和浮力影响的完整形式方程为[[S7,S32]]：

| 物理量    | 输运方程完整形式                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 湍动能k   | \(\frac{\partial (\rho k)}{\partial t} + \frac{\partial (\rho u_i k)}{\partial x_i} = \frac{\partial}{\partial x_j} \left[ (\mu + \frac{\mu_t}{\sigma_k}) \frac{\partial k}{\partial x_j} \right] + G_k + G_b - \rho\varepsilon - Y_M + S_k\) |
| 耗散率ε   | \(\frac{\partial (\rho \varepsilon)}{\partial t} + \frac{\partial (\rho u_i \varepsilon)}{\partial x_i} = \frac{\partial}{\partial x_j} \left[ (\mu + \frac{\mu_t}{\sigma_\varepsilon}) \frac{\partial \varepsilon}{\partial x_j} \right] + C_{1\varepsilon} \frac{\varepsilon}{k} G_k + C_{3\varepsilon} G_b - C_{2\varepsilon} \frac{\rho\varepsilon^2}{k} + S_\varepsilon\) |

方程各项的物理意义[[S7,S17,S32]]如下：瞬态项（\(\partial / \partial t\)）描述物理量随时间的局地变化；对流项（含 \(u_i\) 一阶导数的项）表示湍流输运引起的物理量迁移；扩散项（含 \(\partial / \partial x_j\) 的二阶导数项）表示分子粘性及湍流输运共同作用引起的物理量空间扩散；生成项 \(G_k\) 是由平均速度梯度产生的湍动能，浮力生成项 \(G_b\) 则代表由浮力引起的湍动能增量；耗散/破坏项（含 \(-\rho\varepsilon\) 或含 \(-\varepsilon^2/k\) 的项）表示粘性作用下湍动能的耗散率和耗散率自身的耗散；\(Y_M\) 代表可压缩湍流中脉动膨胀对耗散率的贡献，\(S_k\) 和 \(S_\varepsilon\) 为自定义源项。

### 标准模型常数

标准k-ε模型包含五个经验常数，取值由Launder和Spalding在1974年通过经典实验标定，目前学术界和商业软件基本达成共识[[S36,S27,S31]]：

| 常数 | 标准取值 | 标定依据                                           |
|------|----------|----------------------------------------------------|
| Cμ   | 0.09     | 由近壁区域湍流对流传质可忽略假设下简化边界条件推导[[S36]] |
| C1ε  | 1.44     | 通过近壁湍流对数律速度剖面拟合确定[[S36]]               |
| C2ε  | 1.92     | 参考格栅后各向同性湍流的衰减实验数据[[S36]]              |
| σk   | 1.0      | 湍动能k的湍流Prandtl数                             |
| σε   | 1.3      | 耗散率ε的湍流Prandtl数                             |

需要注意的是，Cμ并非对整个湍流场给出严格恒定值，而是由实验所得的Cμ–P/ε曲线在工程实用范围内平均给出的经验取值[[S10]]。

![实验测得的Cμ–P/ε关系曲线，标有Cμ=0.09参考水平线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47b1a2f5-ac2f-455b-834b-a52d18ca7206/resource)

## 近壁处理机制

标准k-ε模型本身仅适用于高雷诺数、充分发展的旺盛湍流区域，不能直接应用于近壁粘性底层和过渡区。为在不显著增加网格数量的前提下处理近壁影响，工程模拟通常采用壁面函数法。该方法将第一内节点布置在y⁺ > 30的旺盛湍流区内，不再在粘性底层和过渡区划分极细网格。通过以壁面摩擦速度u*为基础的经验映射关系，计算出第一内节点处时均速度、k和ε的边界值，实现对近壁湍流效应的近似模拟[[S19]]。

壁面函数法将壁面区的复杂求解全部压缩到第一内节点所在的控制体内，虽在速度梯度计算时采用一阶差分近似，但合理地选择边界扩散系数或第一内节点边界值后，仍能反映近壁区的整体影响，大幅降低计算成本[[S19]]。

![壁面函数法近壁离散网格示意图，标注壁面节点B、第一内节点I及法向距离y](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73345f5d-39b9-4057-8748-417ad2c39589/resource)

## 假设与适用范围

标准k-ε模型建立在高雷诺数、湍流局部各向同性的基本假设之上[[S17,S32]]。其主要适用前提：流动雷诺数Reₜ远大于1，处于充分发展湍流状态；湍流脉动的三维统计分布假定在空间均匀，即各方向的湍流强度近似相等。

该模型适用于压铸充型等体积填充流动场景，尤其适合高速填充条件下以填充前沿推进和宏观流态为主导的工程模拟。在下列流动场景中模型精度显著下降[[S7,S21,S13,S17]]：

- 高旋流及强曲率壁面流动；
- 三维分离流和弯曲流线运动；
- 各向异性占主导的非对称流动；
- 小尺度瞬态涡旋结构丰富的混合过程；
- 逆压梯度作用下的壁面分离流。

针对上述不足，工程实践中通常选择RNG k-ε模型或SST k-ω模型作为补充替代方案[[S35,S21]]。

## 压铸工艺中的应用

### 典型模拟用途

标准k-ε模型在高压铸造和挤压铸造充型模拟中已有广泛使用，主要用于预测宏观填充流态、卷气分布、氧化夹杂缺陷趋势等关键缺陷特征[[S23,S25,S30]]。具体应用案例包括：ZL301复合材料T型件充型过程的流态仿真、铝合金大壁厚差支架挤压铸造充型状态模拟、以及普通与真空压铸工艺条件下氧化夹杂分布的对比分析[[S23,S25,S30]]。

### 商业软件设置入口

当前主流压铸仿真软件均内置标准k-ε湍流模型选项，用户可在物理模型或流场求解器配置界面直接启用[[S34,S2,S14]]：

- **ProCAST**：流动模块下的PreCAST配置界面默认加载标准k-ε系数集，属于流场求解配置的一部分[[S34,S22]]；
- **FLOW-3D**：物理选项面板中"粘度与紊流"分类下提供勾选启用项，系统默认调用标准k-ε系数[[S2,S20]]；
- **Magmasoft**：工艺参数输入模块的流动求解器子菜单中内置换为压铸定制的标准k-ε湍流系数配置[[S14]]。

![FLOW-3D物理选项设置界面，包含粘度与紊流（Viscosity and turbulence）选项](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97cfcc0f-9ebb-4f52-af2f-655d31ead991/resource)

### 入口湍流参数估算

压铸充型模拟中需在内浇口位置提供湍流强度I和湍流长度尺度L（或水力直径）等入口边界条件。常规估算规则如下[[S28,S8]]：

| 参数         | 典型取值范围或估算方法                         |
|--------------|------------------------------------------------|
| 湍流强度 I   | 一般取3%～5%                                   |
| 湍流长度尺度L | 取内浇口水力直径的0.05～0.1倍                  |
| 水力直径     | 按内浇口等效截面尺寸计算                        |

## 优势与局限

标准k-ε模型在压铸工业仿真中的主要优势与局限可总结为以下对照表[[S26,S15,S21,S13,S17]]：

| 优势                                                         | 局限                                                         |
|--------------------------------------------------------------|--------------------------------------------------------------|
| 计算量远低于DNS和LES，单案例平均耗时可低于11秒[[S15]]           | 仅适用于充分发展的湍流区，近壁预测精度不足，必须搭配壁函数[[S21]] |
| 工业应用成熟度高，已累积二十余年验证经验[[S26]]                 | 对旋流、分离流等复杂流动捕捉能力差[[S13]]                       |
| 参数少、数值稳定性好，软件内置默认系数普遍适用                  | 存在数值过度扩散，小尺度涡结构模拟精度低于RNG模型[[S21]]         |
| 在压铸体积填充场景下计算经济性优异                            | 逆压梯度流动预测误差较大，各向异性流场表现不佳[[S17]]           |

## 图示与算例

![S形模具高压压铸充型过程的实验与标准k-ε类模型预测流动形态对比（t=53.64 ms）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03539d6a-9b45-425b-b3f1-a1a05a9c8742/resource)

大型一体化压铸电池托盘充型模拟中，采用标准k-ε模型计算的填充前端湍流区可通过红圈标注清晰辨识（图示见内部存储资源）[[S4]]，其对应的充型压力分布也给出了7～35 MPa梯度范围的模拟结果[[S12]]，表明标准k-ε模型可耦合压力场并有效识别压力瓶颈和湍流异常区域。

![不对称槽流时均速度分布示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ffbec21-11be-4159-b3f5-06ca95f4230b/resource)

在模型局限性分析中，经典的左右两侧壁面粗糙度不同的不对称平面槽流算例，常被用于对比标准k-ε模型与雷诺应力模型在非对称各向异性流场下的计算偏差[[S9]]。此类算例揭示了涡粘模型在各向异性占主导流动中普遍存在的预测偏差机理。

## Sources
- S11: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51877fb7-2102-4137-8f00-1abb68bacf40/resource) (`51877fb7-2102-4137-8f00-1abb68bacf40`)
- S36: [advanced physical chemistry for process metallurgy__40b302dbe5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe0c9182-9d92-4077-9b13-ba86374f4b7f/resource) (`fe0c9182-9d92-4077-9b13-ba86374f4b7f`)
- S17: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e4d61cf-fb18-4079-aada-4be0aad864ab/resource) (`7e4d61cf-fb18-4079-aada-4be0aad864ab`)
- S33: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec0e64f7-ca99-4e37-9b29-576d3f80f530/resource) (`ec0e64f7-ca99-4e37-9b29-576d3f80f530`)
- S26: [混合坩埚的结构、温度以及浇注条件对受控扩散凝固Al-Si合金微观组织的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc680e34-600a-4ef8-a141-f23c5a83f1b0/resource) (`cc680e34-600a-4ef8-a141-f23c5a83f1b0`)
- S15: [表 4 不同压铸模拟对样本试件模拟平均耗时分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71d0721d-0be9-4c29-93b5-52c552ecf862/resource) (`71d0721d-0be9-4c29-93b5-52c552ecf862`)
- S32: [改善砂芯干燥炉干燥质量的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6dd8140-3c08-42c7-8fd1-5a9ecbc08a86/resource) (`e6dd8140-3c08-42c7-8fd1-5a9ecbc08a86`)
- S35: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7/resource) (`fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7`)
- S7: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34fff431-dce0-439a-a6ce-b989c5813875/resource) (`34fff431-dce0-439a-a6ce-b989c5813875`)
- S27: [表2.1 k-ε双方程模型相应的经验参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6a36b25-6eeb-4e48-a20f-9a0aea24ae6c/resource) (`d6a36b25-6eeb-4e48-a20f-9a0aea24ae6c`)
- S31: [k-ε湍流模型常数推荐值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e00bb476-610e-4458-b14f-afef079c90a6/resource) (`e00bb476-610e-4458-b14f-afef079c90a6`)
- S10: [图3-10 实验测得 cμ~P/ε 曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47b1a2f5-ac2f-455b-834b-a52d18ca7206/resource) (`47b1a2f5-ac2f-455b-834b-a52d18ca7206`)
- S19: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90801b90-36c2-4d1a-a3df-141f6518593e/resource) (`90801b90-36c2-4d1a-a3df-141f6518593e`)
- S21: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf/resource) (`a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf`)
- S13: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/689e0bc6-e395-4555-96a5-cd7fddb37759/resource) (`689e0bc6-e395-4555-96a5-cd7fddb37759`)
- S23: [真空压力浸渗Cf_Al复合材料T型件的成形工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab6be752-9e8d-4d52-a6e3-0104cbc32e98/resource) (`ab6be752-9e8d-4d52-a6e3-0104cbc32e98`)
- S25: [图4-1 充型模拟结果（t=3.16s）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5acbdec-9ddc-4520-a1fc-4412be772fa3/resource) (`c5acbdec-9ddc-4520-a1fc-4412be772fa3`)
- S30: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd933688-2e6d-4234-acbc-123429e71dec/resource) (`dd933688-2e6d-4234-acbc-123429e71dec`)
- S34: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S2: [压铸成形工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01717533-a579-4c46-bdf0-11f9359fa3e7/resource) (`01717533-a579-4c46-bdf0-11f9359fa3e7`)
- S14: [determination of the heat transfer coefficient at the metal die interfac__3400c99740](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c84e570-3542-4322-a72c-e4cee55a1711/resource) (`6c84e570-3542-4322-a72c-e4cee55a1711`)
- S22: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1a53deb-94cb-46cd-9906-31cf334a2897/resource) (`a1a53deb-94cb-46cd-9906-31cf334a2897`)
- S20: [物理选项设置界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97cfcc0f-9ebb-4f52-af2f-655d31ead991/resource) (`97cfcc0f-9ebb-4f52-af2f-655d31ead991`)
- S28: [表 2.7：计算域边界条件分类与具体设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9af0155-5e1e-4c68-9a77-e00776c79225/resource) (`d9af0155-5e1e-4c68-9a77-e00776c79225`)
- S8: [图2-7 各向异性湍流测量中湍流强度比值沿流程的变化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/375deea7-4039-47bb-b94f-7f646621b255/resource) (`375deea7-4039-47bb-b94f-7f646621b255`)
- S4: [(c) 压力瓶颈部位填充过程中铝液前端湍流现象标注图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e137369-e8bd-46f8-b188-431634387354/resource) (`0e137369-e8bd-46f8-b188-431634387354`)
- S12: [图9 填充过程压力分布模拟图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/582ae6d3-6aec-4fc3-a932-b81bf62332c4/resource) (`582ae6d3-6aec-4fc3-a932-b81bf62332c4`)
- S9: [图3-17 平面不可在槽洞示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ffbec21-11be-4159-b3f5-06ca95f4230b/resource) (`3ffbec21-11be-4159-b3f5-06ca95f4230b`)