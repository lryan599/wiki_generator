---
version: "v1"
generated_at: "2026-06-21T06:35:39+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 26
  source_quality_score: 0.85
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 概述

SIMPLE算法，全称为压力耦合方程组的半隐式方法（Semi-Implicit Method for Pressure-Linked Equations），别名SIMPLE法，是计算流体力学（CFD）领域中一种广泛使用的求解流场的数值方法 [[S28,S2,S11]]。该算法于1972年由明尼苏达大学的S.V. Patankar（苏哈斯·帕坦卡）与D.B. Spalding（布莱恩·斯波尔丁）提出，其开发初衷是解决在联立求解离散后的Navier-Stokes（N‑S）动量方程与连续性方程时，因不存在独立的显式压力方程而导致无法迭代求解的工程问题 [[S2,S28,S12]]。

SIMPLE算法属于压力修正类半隐式求解方法，核心逻辑为“假设‑迭代修正”循环：先假设一个压力场，求解离散动量方程得到试探速度场，再通过连续性方程推导压力修正方程来校正压力与速度，反复迭代直至同时满足动量守恒与质量守恒，最终输出收敛的流场结果 [[S28,S13]]。该算法最初针对不可压缩流场开发，后续也被拓展应用于可压缩流体的流场数值计算 [[S2,S11]]。经典的算法理论体系详见Patankar所著的《Numerical Heat Transfer and Fluid Flow》 [[S2,S12]]。

## 核心原理

### 压力–速度耦合与半隐式假设

在不可压缩流的控制方程中，压力本身没有独立的原始方程，而是以源项形式隐含在动量方程中并通过连续性方程约束 [[S24]]。直接联立离散方程会形成庞大的代数方程组，工程上几乎无法求解 [[S2,S12]]。SIMPLE算法的核心思路是：将压力场与速度场的求解解耦，通过迭代方式交替更新两者，直至满足连续条件 [[S11,S23]]。

推导压力修正方程时，SIMPLE算法做了一个关键的半隐式近似：忽略相邻网格点上的速度修正项，仅保留当前点压力修正对速度的直接影响 [[S20,S23,S4]]。这一近似是算法名称中“半隐式”一词的来源，其优点在于大幅简化了压力修正方程的推导与求解，但代价是收敛速度相对偏慢 [[S4,S20]]。所有的后续SIMPLE类改进算法（SIMPLER、SIMPLEC、SIMPLEX、SIMPLET等）均以该基础框架为出发点，针对该近似假设进行优化 [[S20,S4]]。

### 交错网格技术

SIMPLE算法依托交错网格（Staggered Grid）系统完成流场变量的离散布局。在交错网格中，压力、温度等标量定义在计算单元（主控制容积）的中心，而各方向的速度分量则定义在对应单元界面上，速度控制容积与主控制容积在网格上错位半个步长 [[S7,S9,S24]]。

**交错网格的核心作用** [[S7,S26,S9]]：
*   有效抑制普通非交错网格在离散N‑S方程时容易出现的非物理锯齿形（棋盘格形）压力振荡现象，即将一个均匀合理的压力场与一个高度不均匀的压力场误判为等效，从而保证数值求解的稳定性；
*   相邻网格点之间的压力差直接构成位于该界面上速度分量的自然驱动力，使动量方程的离散具有明确的物理意义；
*   无需额外处理型壁位置的压力边界条件，更容易实现通量守恒，提升计算精度。

![SIMPLE算法典型交错网格结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9a696a3-b59c-4d7c-a864-c403d6b214d5/resource)
*图：SIMPLE算法采用的二维交错网格变量分布示意图，标注了主控制容积节点P、E以及界面速度分量u_w、u_e，清晰地展示了速度与压力的错位存储方式 [[S27]]。*

## 算法步骤

SIMPLE算法的标准迭代求解流程包含以下核心步骤 [[S24,S4,S23]]：

1.  **初始化速度场**：假定一个初始速度分布 u⁰、v⁰、w⁰，以此计算动量离散方程中的系数和常数项。
2.  **猜测压力场**：假定一个待迭代的初始压力场 p*。
3.  **求解动量方程**：将 p* 代入离散后的动量方程，依次求解得到试探速度场 u*、v*、w*。
4.  **求解压力修正方程**：将试探速度场代入离散的连续性方程，构建并求解压力修正量方程，得到压力修正值 p'。
5.  **校正压力与速度**：利用 p' 对试探压力场 p* 和速度场 u*、v*、w* 进行修正，得到经连续性约束后的校正压力 p 与校正速度 u、v、w。
6.  **求解其他标量**：若存在与流场耦合的其他物理量（如温度、浓度），则利用修正后的速度场求解其离散方程；若不与流场直接耦合（不影响流场），则可延后至流场完全收敛后再求解。
7.  **迭代与收敛判断**：将校正后的压力 p 作为下一轮迭代的新压力场 p*，返回第2步重复计算。当所有物理量（速度、压力等）的残差下降至预设的收敛判定阈值以下时，终止迭代计算。

![基于SIMPLE算法的压铸充型模拟完整流程框图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a1ddff1-3909-4dd0-97d9-7e7b073e2e87/resource)
*图：基于SIMPLE算法框架的压铸充型流场求解完整流程框图，覆盖数据输入、前处理、单元标记、速度场迭代、自由表面区计算及结果输出等全环节 [[S16]]。*

## 在压铸模拟中的应用

### 应用适配与算法角色

在压铸充型过程的数值模拟中，金属液通常被视作黏性不可压缩的牛顿流体，其流动严格遵循由连续性方程与N‑S方程描述的物理规律 [[S19,S1]]。由于SIMPLE算法的原生设计目标正是求解不可压缩流场的压力–速度耦合问题，因此其基础适用场景与压铸充型的物理前提完全匹配 [[S19]]。

流场求解完成后，算法输出的速度场与压力场可进一步与温度场计算模块、自由表面追踪模块耦合，支持对压铸充型过程中一系列典型缺陷的预测，包括充型流动模式、卷气、夹渣、冷隔、浇不足等，并为后续凝固分析中缩孔、缩松等缺陷的预测提供准确的初始温度场与流场条件 [[S13,S8,S21,S10]]。

**采用SIMPLE或其变体算法的压铸主流商用软件** [[S29,S10,S18]]：

| 软件名称 | 开发商 | 核心算法类型 | 主要分析能力 |
|---|---|---|---|
| MAGMASOFT | MAGMA（德国） | 基于SIMPLE/有限体积法 | 充型、凝固、应力、热处理 |
| ProCAST | ESI（法国） | 有限元/SIMPLE系列 | 充型、凝固、应力、微观组织 |
| Flow‑3D | Flow Science（美国） | SIMPLE/有限体积法（自带VOF） | 充型、卷气、自由表面、凝固 |

### 关键局限性：自由面问题的天然短板

标准SIMPLE算法及其早期改进型（如SIMPLER）是面向固定求解域（定域）、非定常速度场计算的通用方法 [[S4,S2]]。然而，压铸充型是一个求解域（金属液所占据的空间）随时间动态扩张的非定常过程，天然包含运动的自由表面（金属液流动前沿），这恰恰是原始SIMPLE算法无法直接处理的 [[S4,S14]]。

因此，在压铸充型模拟的实际工程应用中，SIMPLE算法必须搭配自由表面追踪类算法（如VOF，即Volume of Fluid方法）才能构建完整的充型流场求解链路。一个典型的组合是2001年C.P. Hong等人所采用的方案：利用SIMPLE法求解流场速度与压力，同时借助VOF法处理自由表面，从而成功解决了复杂型腔铸件充型过程的数值模拟问题 [[S14]]。

> **工程主流方案说明**：需要指出的是，在当前的工业压铸充型过程模拟中，应用最为广泛且被认为综合性能更优的算法是SOLA‑VOF（Solution Algorithm‑Volume of Fluid）。该算法将显式流场求解与自由表面追踪一体化，具有迭代次数少、计算精度高、收敛域宽（欠松弛因子适应范围0.3~2.0）、收敛曲线平滑稳定等优势，相比SIMPLE系列算法在压铸动态充型场景中表现出更强的鲁棒性 [[S15,S7]]。SIMPLE类算法在此领域的应用更多见于学术研究或作为商用软件的可选配置模块。

## 参数范围与收敛控制

在压铸高速填充工况下，SIMPLE算法的收敛性能对数值参数较为敏感。以下参数值来源于商业化压铸模拟软件《压铸模具设计师手册》的工程实践推荐 [[S6]]：

*   **欠松弛因子（松弛因子）**：一般取值范围为 **1.5 ~ 1.8**，常规工况下的默认推荐值为 **0.8**。当计算网格的长度（空间步长）大于15 mm时，为避免计算发散，应将欠松弛因子调低至 **0.1 ~ 0.5** 区间 [[S6]]。
*   **迭代终止判据**：算法的迭代循环在压力修正绝对值或各物理量残差下降到预设阈值时终止。在充型分析中，常通过充型体积比（如设置计算至铸件体积的95%‑98%，剩余由系统自动填满）来平衡精度与速度[[S6]]。

含欠松弛校正环节的完整CFD迭代求解流程如下所示：

![含欠松弛校正的典型SIMPLE算法迭代流程框图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ad49929-8630-4373-b831-c62155cfd3f7/resource)
*图：含欠松弛校正的典型SIMPLE算法迭代流程框图，包含初始参数赋值、残差误差校验、欠松弛因子动态调整与精度分级控制等核心步骤 [[S3]]。*

## 与同类算法的对比

SIMPLE算法问世后，以该算法框架为基础衍生出了一系列改进变体，各自针对不同的收敛效率瓶颈进行了优化。

**主要变体算法特性对比** [[S4,S20]]：

| 变体算法 | 核心改进点 | 与原始SIMPLE的主要差异 | 对压铸的适用性提示 |
|---|---|---|---|
| **SIMPLER** (SIMPLE‑Revised) | 在推导压力方程时不引入近似假设，可用正确速度场直接求取精确压力 | 大幅提升收敛速度，收敛稳定性优于SIMPLE | 仍仅支持定域流场求解，无法直接处理自由面 [[S4]] |
| **SIMPLEC** (SIMPLE‑Consistent) | 调整速度修正方程中的系数处理方式，使压力–速度耦合更为协调 | 收敛速度更快，对简单流动改进显著 | 同属定域求解框架 |
| **SIMPLEX** / **SIMPLET** | 针对特定问题类型（如网格扭曲、瞬变流等）进行定向优化 | 适用范围收窄，但在目标场景下效率更优 | 需结合实际工况验证 |

**1987年铸造模拟领域的算法比选结论**：中国学者王君卿在对某铸铁三通管进行三维充型与凝固过程模拟时，对SMAC、SIMPLE及SOLA‑VOF三类算法进行了对比。结果表明，在计算精度差异不大的前提下，**SOLA‑VOF算法的计算速度高于SMAC和SIMPLE算法** [[S14]]。该结论与SOLA‑VOF至今仍是压铸充型模拟工业主流方法的技术路线状况一致 [[S15]]。

## 局限性与工程注意事项

在面向压铸件的实际模拟中，SIMPLE系列算法面临以下主要工程限制：

1.  **自由面追踪依赖外部模块**：如上所述，原生的SIMPLE/SIMPLER算法不具备自由表面求解能力，其用于模拟压铸充型过程的前提是必须与VOF等自由面追踪方法深度耦合，这增加了求解器的实现复杂度 [[S4,S14]]。

2.  **非线性耦合导致的收敛困难**：压铸充型属于高压、高速的瞬态过程，熔融金属的雷诺数（Re）通常超过10⁵，流动表现为未充分发展的紊流 [[S11,S19]]。高雷诺数下压力–速度耦合的非线性极强，可能导致SIMPLE算法的迭代求解收敛缓慢，甚至发散。

3.  **薄壁件的网格敏感性**：针对壁厚小于2 mm的压铸薄壁区域，应用SIMPLE类算法进行充型模拟时对网格质量有严格要求 [[S17]]：
    *   薄壁处至少布置 **3层** 计算网格；
    *   网格长宽比建议控制在 **1.1 ~ 1.2** 范围内，最大不得超过 **1.3**；
    *   若不满足上述要求，极易引发数值伪振荡或导致计算直接发散 [[S17]]。

4.  **压力锯齿波问题（无交错网格时）**：若放弃交错网格而使用普通同位网格对SIMPLE算法进行离散，动量方程将无法检测不合理的锯齿形压力分布，可能导致计算输出非物理的振荡压力场。采用交错网格是抑制这一问题、保证数值稳定性的必要手段 [[S24,S26]]。

## Sources
- S28: [7195253_SIMPLE算法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eda3d754-0cc6-4303-a390-ea4a0a238218/resource) (`eda3d754-0cc6-4303-a390-ea4a0a238218`)
- S2: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0685322c-9f46-499e-82b8-3b566665e55c/resource) (`0685322c-9f46-499e-82b8-3b566665e55c`)
- S11: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fc549e6-bd30-494d-9539-91fb93d9a5b4/resource) (`5fc549e6-bd30-494d-9539-91fb93d9a5b4`)
- S12: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/631e886b-6bd0-4508-9f0e-647d9cfb25f5/resource) (`631e886b-6bd0-4508-9f0e-647d9cfb25f5`)
- S13: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b7c68ca-c779-40dd-b2d9-70f943b67af2/resource) (`7b7c68ca-c779-40dd-b2d9-70f943b67af2`)
- S24: [激光立体成形 高性能致密金属零件的快速自由成形](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb5bbf08-0b9c-45bb-a3aa-6e9dc4d4908f/resource) (`cb5bbf08-0b9c-45bb-a3aa-6e9dc4d4908f`)
- S23: [TC4与Inconel 718双丝电弧复合焊数值模拟与微观组织及性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c6529722-1000-4ffe-b33e-a3aaa5512289/resource) (`c6529722-1000-4ffe-b33e-a3aaa5512289`)
- S20: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4a74121-846c-4e0d-9d50-bfcec3bd0b00/resource) (`b4a74121-846c-4e0d-9d50-bfcec3bd0b00`)
- S4: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1550e90e-2dc7-4cec-a2fc-6f9a66f82a81/resource) (`1550e90e-2dc7-4cec-a2fc-6f9a66f82a81`)
- S7: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/337b41ce-f048-422b-8f71-85d1d1d17def/resource) (`337b41ce-f048-422b-8f71-85d1d1d17def`)
- S9: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47ca0c32-a927-405c-baae-6a557cb54c6f/resource) (`47ca0c32-a927-405c-baae-6a557cb54c6f`)
- S26: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4917466-179c-475e-ac89-72aab18d8b6b/resource) (`e4917466-179c-475e-ac89-72aab18d8b6b`)
- S27: [交错网格示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9a696a3-b59c-4d7c-a864-c403d6b214d5/resource) (`e9a696a3-b59c-4d7c-a864-c403d6b214d5`)
- S16: [流动场模拟计算程序流程框图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a1ddff1-3909-4dd0-97d9-7e7b073e2e87/resource) (`8a1ddff1-3909-4dd0-97d9-7e7b073e2e87`)
- S19: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b31cd045-99d1-4556-8db0-c456c7e5bce4/resource) (`b31cd045-99d1-4556-8db0-c456c7e5bce4`)
- S1: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01302f51-aba1-4d87-8356-d6d5ca51f876/resource) (`01302f51-aba1-4d87-8356-d6d5ca51f876`)
- S8: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fd2c9d4-511e-41ce-a97f-4a5dacdfd657/resource) (`3fd2c9d4-511e-41ce-a97f-4a5dacdfd657`)
- S21: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5cd1333-aea8-4263-b751-e1c56b874acb/resource) (`b5cd1333-aea8-4263-b751-e1c56b874acb`)
- S10: [铝合金一体化压铸技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/560cd449-107a-4860-a4ab-64ea9b193148/resource) (`560cd449-107a-4860-a4ab-64ea9b193148`)
- S29: [铝合金低压铸造过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe51c21e-8783-4b9f-a73c-b8354c194671/resource) (`fe51c21e-8783-4b9f-a73c-b8354c194671`)
- S18: [表1.2 国内外主流使用铸造软件[43]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98dd3bca-962a-49d8-9d47-d25b3afeb03f/resource) (`98dd3bca-962a-49d8-9d47-d25b3afeb03f`)
- S14: [基于数值模拟的转向器阀壳体压铸模具结构及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8488982e-e9af-43d2-af10-d5d5d42e463f/resource) (`8488982e-e9af-43d2-af10-d5d5d42e463f`)
- S15: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87a83816-f183-4370-9308-7feae7709688/resource) (`87a83816-f183-4370-9308-7feae7709688`)
- S6: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2569f655-d1db-4211-9b4c-0c7b7b052008/resource) (`2569f655-d1db-4211-9b4c-0c7b7b052008`)
- S3: [图6-20 永久磁铁棒计算程序框图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ad49929-8630-4373-b831-c62155cfd3f7/resource) (`0ad49929-8630-4373-b831-c62155cfd3f7`)
- S17: [铝合金压铸制品缩孔缺陷影响因素分析及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/958df38a-1710-4078-bf90-f3164edc81e2/resource) (`958df38a-1710-4078-bf90-f3164edc81e2`)