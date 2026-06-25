---
version: "v1"
generated_at: "2026-06-18T17:43:30+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 17
  source_quality_score: 0.84
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

Realizable k‑ε 模型（可实现 k‑ε 模型）是一种双方程雷诺平均湍流模型，其核心设计目的是解决标准 k‑ε 模型在大时均应变率工况下产生非物理负湍流正应力的缺陷[[S9,S10,S17]]。该模型通过在雷诺应力项中引入严格的数学约束，动态调整湍流粘性系数 Cμ，并对耗散率 ε 的输运方程源项进行重构，使计算结果符合真实流动的物理规律[[S9,S17]]。相比标准 k‑ε 模型，Realizable k‑ε 模型对回流、流动分离、复杂二次流动等现象的预测精度有显著提升[[S9,S18]]。

## 控制方程

Realizable k‑ε 模型包含湍动能 k 和耗散率 ε 两个输运方程。

**湍动能 k 方程**[[S9]]：

\[
\frac{\partial (\rho k)}{\partial t} + \frac{\partial (\rho k u_j)}{\partial x_j} = \frac{\partial}{\partial x_j} \left[ \left( \mu + \frac{\mu_t}{\sigma_k} \right) \frac{\partial k}{\partial x_j} \right] + G_k - \rho \varepsilon
\]

式中，σk = 1.0，Gk 为由平均速度梯度产生的湍动能生成项。

**耗散率 ε 方程**[[S9]]：

\[
\frac{\partial (\rho \varepsilon)}{\partial t} + \frac{\partial (\rho \varepsilon u_j)}{\partial x_j} = \frac{\partial}{\partial x_j} \left[ \left( \mu + \frac{\mu_t}{\sigma_\varepsilon} \right) \frac{\partial \varepsilon}{\partial x_j} \right] + \rho C_1 \bar{S} \varepsilon - C_2 \rho \frac{\varepsilon^2}{k + \sqrt{\nu \varepsilon}}
\]

其中 C₂ = 1.9，σ_ε = 1.2。系数 C₁ 按下式计算[[S9]]：

\[
C_1 = \max \left[ 0.43, \frac{\eta}{\eta + 5} \right],\quad \eta = \sqrt{2 \bar{S}_{ij}\bar{S}_{ij}} \, \frac{k}{\varepsilon}, \quad \bar{S}_{ij} = \frac{1}{2} \left( \frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial \bar{u}_j}{\partial x_i} \right)
\]

**涡粘性系数**仍保持 μt = ρ Cμ k² / ε 的形式[[S9]]，但 Cμ 不再是固定常数，而是与平均应变率张量及旋转率张量相关的函数[[S9,S17]]：

\[
C_\mu = \frac{1}{A_0 + A_s \, U^* k / \varepsilon}
\]

式中 A₀ = 4.0，A_s = √6 cosφ，φ = ⅓ arccos(√6 W)，W 为应变率张量三阶不变量与二阶不变量的组合；U* 为平均应变率与旋转率的组合量[[S9]]。这一可变的 Cμ 是实现雷诺应力数学约束、消除负正应力的关键机制。

![k-ε 湍流模型在连铸/压铸熔体流动模拟中的控制方程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd3235e9-307a-4987-b47e-fc8062880a7e/resource)

图1 适用于铸造熔体流动数值模拟的 k‑ε 湍流模型数学方程[[S14]]。

## 模型优势与适用场景

Realizable k‑ε 模型对强流线弯曲、旋涡回流、边界层分离、离散流动及复杂二次流动等工况的预测结果比标准 k‑ε 模型更贴近实验实测值[[S9]]。当流场涉及明显的离散流动或复杂二次流时，通常优先采用该模型进行计算[[S9,S18]]。

在压铸工艺的数值模拟中，该模型的优势场景包括：
- 压铸充型过程中熔池内的流动分离与回流[[S18]]；
- 排气系统内部的气液两相复杂分离流[[S4]]；
- 高压压铸充型时的空气卷入多相混沌流动[[S7]]；
- 窑炉类等涉及复杂分离流的高温气体湍流流动[[S17]]。

## 限制与不足

Realizable k‑ε 模型仍基于湍流各向同性假设，因此在强各向异性、高强度旋流场景下适应性不足[[S8,S2]]。该模型属于高雷诺数湍流模型，仅适用于远离壁面的充分发展湍流区，近壁区域（含黏性子层和过渡区）必须配合壁面函数进行处理[[S2,S8]]。此外，为获得可靠的计算结果，对网格质量（尤其是近壁第一层网格的布置与正交性）有一定要求。

## 与可扩展壁面函数（SWF）的联合使用

### 壁面函数的基本原理

壁面函数法的思想是：不在壁面附近的黏性子层内划分大量细密网格，而将计算域的第一内节点直接布置在旺盛湍流区内；通过半经验关系将近壁区对时均流动的全部影响集中映射到该节点所在的控制体中[[S11,S16]]。无因次速度 u⁺ 和无因次壁面法向距离 y⁺ 定义为[[S11]]：

\[
u^+ = \frac{u}{u^*},\quad y^+ = \frac{y u^* \rho}{\mu},\quad u^* = \sqrt{\frac{\tau_w}{\rho}}
\]

![壁面函数使用区网格划分示意](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8e92f61-e71e-4c1e-96eb-aeaed1bb221b/resource)

图2 湍流数值计算中壁面函数使用区的网格划分示意，标注了层流子层、近壁湍流区与旺盛湍流区，以及第一排格点的位置[[S12]]。

### 联合使用的优势

在 Realizable k‑ε 模型中搭配可扩展壁面函数（SWF），可以有效放宽对第一层网格 y⁺ 的严格要求，提升高雷诺数、大应变率流动模拟的数值稳定性与收敛速度[[S4,S7]]。已公开的工业案例表明：
- 针对排气系统内部气液两相复杂分离流，使用 Realizable k‑ε + SWF 组合方案，仿真残差收敛更快，流场无异常非物理涡流[[S4]]。
- 高压压铸的空气卷入模拟中，采用 Realizable k‑ε 搭配自适应 y⁺ 壁面模型（可扩展壁面函数的工业实现形态），可以稳定充型混沌流动，并为湍流耗散计算提供额外自由度，改善空气卷吸预测精度[[S7]]。

## 模型常数与推荐设置

Realizable k‑ε 模型的推荐常数如下：

| 参数 | 取值 | 说明 |
|------|------|------|
| σk | 1.0 | 湍动能 k 的湍流普朗特数[[S9]] |
| σε | 1.2 | 耗散率 ε 的湍流普朗特数[[S9]] |
| C₂ | 1.9 | ε 方程耗散项系数[[S9]] |
| C₁ | max[0.43, η/(η+5)] | ε 方程生成项系数，随应变率动态变化[[S9]] |
| Cμ | 函数形式（见上文） | 涡粘性系数中的变量，受应变率与旋转率实时影响[[S9,S17]] |

标准 k‑ε 模型的固定常数（如 Cμ=0.09, C₁=1.44, C₂=1.92, σk=1.0, σε≈1.3[[S1,S3]]）在许多铸造行业模拟中仍被用作参考基准，但其在大应变率下的非物理行为推动了 Realizable k‑ε 模型的应用。

## 与其他湍流模型的对比

三种主流双方程 RANS 湍流模型的特性和适用性对比如下：

| 项目 | Realizable k‑ε | RNG k‑ε | SST k‑ω |
|------|----------------|---------|---------|
| 核心改进 | 雷诺应力数学约束，动态 Cμ，修改 ε 方程源项[[S9,S17]] | 基于重整化群理论推导常数，ε 方程附加修正项，低 Re 近壁自适应[[S10,S20]] | 近壁 k‑ω 与远场 k‑ε 混合，考虑湍流剪切应力输运[[S19,S20]] |
| 优势场景 | 回流、分离流、复杂二次流[[S9]] | 普通旋流、低 Re 近壁剪切流[[S10,S20]] | 壁面约束的边界层、射流、混合层[[S20]] |
| 近壁处理 | 依赖壁面函数[[S8,S2]] | 低 Re 近壁能力增强[[S10]] | 近壁求解能力强，可自动切换壁面函数[[S19,S20]] |
| 相对计算成本 | 中（≈ RNG k‑ε）[[S13]] | 中[[S13]] | 略高（因混合函数插值）[[S13]] |

在实际工程中，若模拟对象以分离流、回流或复杂二次流为主，Realizable k‑ε 通常是精度与成本兼顾的首选；若近壁边界层本身就是主要关注量，则 SST k‑ω 更具优势。

## 典型应用案例

### 铸轧工艺熔池流动模拟

针对 2099 铝锂合金铸轧过程，公开研究选用 Realizable k‑ε 作为指定湍流模型，并结合焓‑孔隙率技术处理糊状区凝固相变。模拟结果表明，该模型能够准确捕捉铸轧区熔池内的流动分离与回流特征，且无需对近壁区进行全加密即可获得合格精度[[S18,S9]]。

### 排气系统内部复杂分离流

氢燃料电池汽车排气系统的气液两相流仿真中，采用 Realizable k‑ε 模型搭配可扩展壁面函数（SWF），在 80 kW 额定工况下稳定预测了排气系统背压（约 5.67 kPa），流场通畅，无异常涡流，各项残差收敛良好[[S4]]。

### 高压压铸空气卷入预测

基于 STAR‑Cast 平台的高真空高压压铸充型模拟，使用 Realizable k‑epsilon 湍流模型配合自适应 y⁺ 壁面模型，可以稳定高雷诺数下的混沌充型过程，同时为能量耗散计算提供额外自由度，提升空气卷吸的预测精度[[S7]]。

### 窑炉类气体湍流流动

在砂芯干燥炉干燥质量的数值研究中，Realizable k‑ε 模型被用于描述炉内复杂的湍流流动，以正确反映回流和分离现象对温度场与组分输运的影响[[S17]]。

---

图1 来源于连铸中间包钢液流动模拟的 k‑ε 模型方程图示[[S14]]；图2 为壁面函数使用区域与网格划分示意[[S12]]。这些可视化资料可帮助理解 Realizable k‑ε 模型的控制方程结构及其与壁面函数的配合逻辑。

## Sources
- S9: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8465bffe-b784-49a1-8b5f-e3d43522e167/resource) (`8465bffe-b784-49a1-8b5f-e3d43522e167`)
- S10: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a66e914-20c5-46c1-828c-1e804646ce17/resource) (`8a66e914-20c5-46c1-828c-1e804646ce17`)
- S17: [改善砂芯干燥炉干燥质量的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6dd8140-3c08-42c7-8fd1-5a9ecbc08a86/resource) (`e6dd8140-3c08-42c7-8fd1-5a9ecbc08a86`)
- S18: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8c0aca6-c9c3-43bf-9d0b-99f719f1892d/resource) (`e8c0aca6-c9c3-43bf-9d0b-99f719f1892d`)
- S14: [k-ε turbulence model equations for continuous casting tundish melt flow simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd3235e9-307a-4987-b47e-fc8062880a7e/resource) (`dd3235e9-307a-4987-b47e-fc8062880a7e`)
- S4: [氢燃料电池汽车排气口布置方案设计与安全性分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50493d20-2edf-44bf-bf1c-90767de094f2/resource) (`50493d20-2edf-44bf-bf1c-90767de094f2`)
- S7: [cfd modeling and simulation in materials processing 2016 tms cfd simulat__395156bdb3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c37ec23-efa7-43a9-9ed8-01e51b0e6bba/resource) (`7c37ec23-efa7-43a9-9ed8-01e51b0e6bba`)
- S8: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e4d61cf-fb18-4079-aada-4be0aad864ab/resource) (`7e4d61cf-fb18-4079-aada-4be0aad864ab`)
- S2: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/340a9b3c-a435-48f8-8614-8edddb026de9/resource) (`340a9b3c-a435-48f8-8614-8edddb026de9`)
- S11: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90801b90-36c2-4d1a-a3df-141f6518593e/resource) (`90801b90-36c2-4d1a-a3df-141f6518593e`)
- S16: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0587892-3043-49e0-b1b2-d50c870584cf/resource) (`e0587892-3043-49e0-b1b2-d50c870584cf`)
- S12: [图3-15 壁面函数使用区](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8e92f61-e71e-4c1e-96eb-aeaed1bb221b/resource) (`b8e92f61-e71e-4c1e-96eb-aeaed1bb221b`)
- S1: [表3.1 k-ε双方程模型中的常数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/090a24b5-6017-47fa-8dc0-ef620caabe15/resource) (`090a24b5-6017-47fa-8dc0-ef620caabe15`)
- S3: [2099铝锂合金铸轧工艺计算机模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34fff431-dce0-439a-a6ce-b989c5813875/resource) (`34fff431-dce0-439a-a6ce-b989c5813875`)
- S20: [基于数值模拟的受控扩散凝固中熔体混合过程与形核率的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7/resource) (`fb6d2ed1-9cbe-4e9b-b6e3-550b9f9652f7`)
- S19: [铝合金车轮低压铸造模具冷却系统界面换热机理分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f830b2aa-a7cb-4c72-8f0b-d55fa9fb11d9/resource) (`f830b2aa-a7cb-4c72-8f0b-d55fa9fb11d9`)
- S13: [混合坩埚的结构、温度以及浇注条件对受控扩散凝固Al-Si合金微观组织的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc680e34-600a-4ef8-a141-f23c5a83f1b0/resource) (`cc680e34-600a-4ef8-a141-f23c5a83f1b0`)