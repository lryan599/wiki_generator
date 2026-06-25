---
version: "v1"
generated_at: "2026-06-18T13:23:55+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 28
  source_quality_score: 0.86
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

LEVEL SET法（水平集方法，Level-set method）是一种用于动态界面隐式描述与追踪的计算流体力学数值方法，其核心思想是将移动变形的相界面作为标量函数φ(x,t)的零等值面嵌入到高一维的空间中，通过求解该标量场的演化方程来间接获得任意时刻界面的位置与几何形态[[S1,S4]]。该方法无需对追踪界面进行参数化重建，可自然处理界面分裂、合并等复杂拓扑变化，已成为计算流体力学领域主流的动态界面描述方法[[S1,S19]]。

在压铸工程领域，LEVEL SET法主要用于充型过程的气-液两相流自由表面追踪，可模拟金属液高速填充时的卷气、氧化膜折叠、液滴破碎与融合等复杂界面行为[[S23,S24]]。

---

## 基本数学原理

### 符号距离函数与零等值面

标量函数φ(x,t)定义为符号距离函数：在初始时刻，计算域内任意点x到初始界面Γ(0)的有向距离为：

- 点位于流体1区域（如液相）：φ(x,0) = d(x,Γ(0))，取正值；
- 点位于界面Γ(0)上：φ(x,0) = 0；
- 点位于流体2区域（如气相）：φ(x,0) = -d(x,Γ(0))，取负值[[S1,S12]]。

任意时刻的运动界面Γ(t)严格对应于φ(x,t)的零等值面，数学表达为：

> Γ(t) = {x ∈ Ω : φ(x,t) = 0} [[S1,S8,S24]]

在压铸充型模拟中，通常约定液相区域对应φ < 0，气相区域对应φ > 0，界面处φ = 0[[S8,S14]]。

![两相流区域划分与水平集零等值面对应关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4c9f2b99-fbaf-4b00-93d2-a1096c68a8bb/resource)

**图1** 计算区域中两相界面的分区示意：左侧子区域Ω¹为流体1（φ > 0），右侧子区域Ω²为流体2（φ < 0），中央运动交界面Γ(t)对应φ = 0的零等值面位置[[S13]]。

### 对流演化方程

界面的运动受流场速度驱动，LEVEL SET函数的演化遵循对流输运方程：

> ∂φ/∂t + u·∇φ = 0 [[S1,S12,S27]]

其中u为流场速度矢量。该方程保证标量函数跟随流体质点同步对流输运，使得零等值面始终保持与实际运动界面一致[[S12]]。对于三维问题，上式可展开为：

> φ_t + uφ_x + vφ_y + wφ_z = 0 [[S12]]

### 重新初始化

在求解对流方程后，因数值耗散会使φ(x,t)逐渐偏离符号距离函数特性，需额外执行重新初始化步骤以恢复该属性。重新初始化可保证界面曲率、法向及表面张力等相关几何量的计算精度[[S8,S6]]。标准数值流程为：

1. 初始化各网格单元的F⁰、φ⁰、压力p⁰、速度ν⁰，其中φ⁰由单元中心到界面的距离计算；
2. 使用高阶WENO等格式求解LEVEL SET对流方程，得到新时刻的φⁿ值；
3. 执行重新初始化运算修正φⁿ，使其重新满足符号距离函数定义[[S6]]。

### 光滑规则化函数

为解决跨界面物性突变引发的数值发散问题，引入光滑赫维赛德（Heaviside）函数H_ε(φ)进行界面附近的密度、粘度等物性参数插值[[S6,S11]]：

| φ 范围 | H_ε(φ) 取值 |
|---------|------------|
| φ < -ε | 0 |
| \|φ\| ≤ ε | (φ+ε)/(2ε) + sin(πφ/ε)/(2π) |
| φ > ε | 1 |

此处ε通常取1.5倍网格步长Δ[[S11]]。

光滑狄拉克delta函数δ_ε(φ)定义为H_ε(φ)的一阶导数，仅在界面附近厚度为ε的薄层内非零。该函数在连续表面力（CSF）模型中用于将界面表面张力等效为体积力源项注入N-S方程[[S11,S27]]。

![水平集函数定义示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/613dd9ee-4aaa-4bc3-93b0-16d2cf81f72f/resource)

**图2** LEVEL SET函数在两相区域的定义示意：蓝色区域为液相（φ < 0），白色区域为气相（φ > 0），黑色曲线为零值界面（φ = 0）[[S14]]。

---

## 方法分类与演变

### 经典LEVEL SET方法

经典LEVEL SET方法通过全域求解符号距离函数的对流方程实现界面追踪。该方法具有以下核心优势：LEVEL SET函数是全域平滑连续的标量场，空间梯度可被高精度直接求解，界面曲率和表面张力的计算精度显著高于传统VOF方法，且天然支持自动处理任意复杂的界面拓扑变化[[S24,S23]]。

### 窄带LEVEL SET方法

窄带LEVEL SET方法仅在界面附近的小范围窄带网格区域内对符号距离函数进行求解计算，而非对全域网格遍历计算。该方法大幅降低了全局数值求解的计算量，适用于大尺寸压铸型腔的低精度快速充型仿真场景[[S23]]。

### 粒子LEVEL SET方法

粒子LEVEL SET方法在基础LEVEL SET框架内引入示踪粒子补充追踪界面局部细节。该方法可显著缓解原生LEVEL SET方法的质量守恒偏差问题，早期多用于铸造充型两相流的非可压缩流仿真[[S24,S7]]。

### CLSVOF(耦合LEVEL SET与VOF）方法

CLSVOF方法是LEVEL SET与VOF(流体体积法）的耦合方案，目前为压铸充型高速两相流模拟的主流高级实现方案[[S5,S20,S24]]。该方法结合了两种方法的优势：

- **保留LEVEL SET的平滑连续特性**：实现高精度的界面曲率和表面张力计算；
- **继承VOF的体积守恒特性**：完全克服了原生VOF方法因体积分数函数不连续而难以准确计算界面导数的缺陷[[S24,S3,S15]]。

Mark Sussman在提出LEVEL SET方法解决气-液两相流计算问题后，又进一步提出了CLSVOF方法以解决传统LEVEL SET方法在输运过程中质量不守恒的缺陷[[S23]]。

国内研究团队已公开了适用于压铸场景的改进型CLSVOF模型，该模型同时考虑液相不可压缩特性与高速充流下空气的可压缩特性，计算得到的卷气位置与实际水模拟试验结果吻合度远高于传统单一流场模型[[S5]]。

---

## 压铸工艺中的角色与软件实现

### 充型模拟中的界面追踪

在压铸充型过程中，LEVEL SET方法将金属液与空气的运动界面定义为标量符号距离函数φ(x,t)的零等值面：液体区域对应φ < 0，空气区域对应φ > 0，界面位置对应φ = 0。该方法无需显式界面重构即可自动处理界面融合、破碎等复杂拓扑变化[[S1,S8,S24,S14]]。

以LEVEL SET为核心的压铸充型模拟可准确复现金属液高速射流场景下液滴的破碎、再融合等全过程拓扑演化，相关水模拟对比实验已验证了其与物理实际的一致性[[S12]]。

### 主流软件实现

| 软件 | LEVEL SET实现方式 | 功能特点 |
|------|------------------|----------|
| ProCAST | 基于有限元框架，默认充型求解器为SOLA-VOF，高级两相流模块集成CLSVOF算法作为可选功能 | 支持LEVEL SET方法进行高精度充型裹气缺陷预测[[S16]] |
| FLOW-3D | 原生核心采用VOF方法，9.0及以后版本新增集成LEVEL SET扩展模块 | 启用该模块可实现空气夹带现象和动态液流聚散行为的高精度仿真[[S18,S30]] |
| AnyCasting | 高级两相流求解模块搭载改进型LEVEL SET算法 | 专为压铸场景优化，可高效捕捉金属液充型前沿的氧化膜折叠和卷入行为[[S10]] |
| Magmasoft | 官方公开的自由表面追踪模块集成了优化版LEVEL SET算法 | 完整支持压铸充型全流程的界面拓扑变化仿真，为压铸充型缺陷预判提供更准确的流场基础[[S32,S9]] |

> 注：商业软件的具体算法实现细节可能因版本而异，上述信息依据公开文献及软件理论手册整理。

---

## 压铸应用实例

### 卷气与氧化膜缺陷预测

国内铸造核心期刊《铸造》于2010年公开了基于投影-LEVEL SET方法的充型过程气-液两相流数值模拟研究，首次将改进型LEVEL SET算法引入压铸充型气液两相流仿真体系，验证了其在复杂型腔场景下的计算稳定性[[S26]]。

《中国有色金属学报》公开的压铸领域LEVEL SET应用案例中，通过LEVEL SET方法实现了铝合金充型过程中氧化膜向金属液内部卷入行为的定量捕捉，可直接用于预测氧化夹杂缺陷的分布位置[[S26]]。

### 高速充型界面行为捕捉

CLSVOF方法在S型通道水模拟验证中展现了良好性能：同时考虑空气可压缩性和表面张力（方案A）的仿真结果与实际水模拟试验结果吻合最好；不考虑表面张力时卷气量偏小，不考虑空气可压缩性时卷气缺陷预测会大于实际情况[[S5,S20]]。

---

## 优势与局限性

### 核心优势

- 界面曲率与表面张力计算精度显著高于传统VOF方法，因为LEVEL SET函数全域平滑连续，空间梯度可被高精度直接求解[[S24,S23,S19,S27]]；
- 天然支持自动处理任意复杂的界面拓扑变化，无需显式构造界面网格[[S24,S23]]；
- 不需重新构建界面即可描述界面的分裂、合并等复杂拓扑变化[[S19,S4]]。

### 固有局限性

- 基础版本不直接追踪流体体积守恒量，长时间输运后会产生明显的质量守恒偏差[[S24,S23,S27]]；
- 界面区域数值求解的离散误差易引发局部物理量梯度的虚假振荡[[S24]]；
- 为保持符号距离函数特性的重新初始化步骤若在全域网格执行，计算成本较高[[S24]]。

---

## 压铸场景下界面追踪方法对比

| 比较维度 | LEVEL SET | VOF | CLSVOF | SIMPLE |
|----------|-----------|-----|--------|--------|
| 界面曲率/表面张力精度 | 高[[S24,S23]] | 较低（体积分数函数不连续）[[S24]] | 高[[S24]] | 不适用于自由表面[[S17]] |
| 计算效率 | 低于VOF[[S23]] | 较高[[S23]] | 略低于原生VOF[[S23]] | 迭代收敛速度慢[[S17]] |
| 体积守恒能力 | 最差[[S24,S23]] | 天然具备完全体积守恒[[S24]] | 良好[[S24]] | 无专属体积守恒机制 |
| 拓扑变化处理 | 自动处理[[S24,S23]] | 需复杂重构[[S19]] | 自动处理[[S24,S3]] | 不适用 |

在压铸充型场景下，CLSVOF方法是当前平衡精度、效率与体积守恒的主流选择，尤其适用于高压高速充型条件下气-液两相界面拓扑变化剧烈的模拟[[S24,S3,S15]]。

---

## 典型操作参数

| 参数 | 典型取值范围/设定 | 说明 |
|------|------------------|------|
| 界面厚度ε | 2~3倍局部网格步长 | 用于光滑Heaviside/Delta函数的过渡区间宽度[[S28,S24]] |
| 时间步长Δt | Δt ≤ min{Δx/\|U_max\|, Δy/\|V_max\|, Δz/\|W_max\|} | 满足CFL稳定性约束，确保一个时间步长内流体流动不超过一个网格[[S28]] |
| 薄壁件网格分辨率 | 单元尺寸 ≤ 1~3 mm | 压铸薄壁件的最低网格要求[[S6]] |
| 表面张力模型 | CSF(连续表面力）模型 | 将界面表面张力等效为体积力源项注入N-S方程[[S11,S27,S3]] |
| 壁面接触角 | 50°~120° | 依据铝合金/镁合金与H13钢模具的材料对特性取值[[S29]] |

---

## 与相关术语的关系

### 界面捕捉与界面追踪

LEVEL SET方法与VOF方法同属欧拉型固定网格框架下的界面捕捉（interface capturing）方法，通过在固定网格上定义标量场变量间接描述界面位置[[S22,S27]]。与之相对的是拉格朗日型界面追踪（interface tracking）方法，后者需将网格建立在移动界面上，界面变化时网格需重新划分[[S1,S4]]。

### 与VOF方法的关联

VOF方法通过体积分数函数F（取值0~1）描述网格内流体占有率，天然具备体积守恒特性，但因函数不连续导致界面曲率和表面张力计算精度受限[[S24]]。LEVEL SET方法的提出恰好弥补了VOF的精度短板，而CLSVOF耦合方法则综合了两者的优势[[S24,S19,S27]]。

### 与SOLA等流场求解算法的关系

LEVEL SET方法负责界面描述与追踪，而流场求解仍需耦合N-S方程的数值求解器。在压铸模拟中，SOLA算法（或其改进版本）常与LEVEL SET搭配使用，SOLA负责压力-速度耦合求解，LEVEL SET负责界面追踪，二者共同构成完整的两相流模拟框架[[S11,S17,S24]]。

### 铸造成型工艺中的应用拓展

除压铸外，LEVEL SET方法已逐步拓展至重力铸造、低压铸造、离心铸造等工艺的充型模拟中，涉及的界面物理现象包括气泡自由上浮、氧化膜折叠卷入、液滴聚散融合等[[S12,S17]]。

## Sources
- S1: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/023e67b7-e6eb-4e94-9c0e-028602a1e0a5/resource) (`023e67b7-e6eb-4e94-9c0e-028602a1e0a5`)
- S4: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18797292-aa92-4621-87e5-0dc95d2021e4/resource) (`18797292-aa92-4621-87e5-0dc95d2021e4`)
- S19: [QCW激光热调控钢铝异种金属焊接特性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77a1ef81-152f-47da-9bb7-560ddaaab48f/resource) (`77a1ef81-152f-47da-9bb7-560ddaaab48f`)
- S23: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97726e24-e029-4370-9696-63b2fe157b62/resource) (`97726e24-e029-4370-9696-63b2fe157b62`)
- S24: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a10cebfa-57da-40d1-8cd0-3ce33a4a83ed/resource) (`a10cebfa-57da-40d1-8cd0-3ce33a4a83ed`)
- S12: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46bc70ae-6f95-4ff2-84fe-2c55da5b5dce/resource) (`46bc70ae-6f95-4ff2-84fe-2c55da5b5dce`)
- S8: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ea0556f-ef4f-4d56-b886-e80ce6719e29/resource) (`2ea0556f-ef4f-4d56-b886-e80ce6719e29`)
- S14: [Level Set function definition schematic](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/613dd9ee-4aaa-4bc3-93b0-16d2cf81f72f/resource) (`613dd9ee-4aaa-4bc3-93b0-16d2cf81f72f`)
- S13: [图6-31 计算区域中的两相界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4c9f2b99-fbaf-4b00-93d2-a1096c68a8bb/resource) (`4c9f2b99-fbaf-4b00-93d2-a1096c68a8bb`)
- S27: [additive manufacturing of metal alloys 1 processes raw materials and numerical simulation__200a158ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afeb066f-a7f4-4e3d-8e66-3c0117f5dd01/resource) (`afeb066f-a7f4-4e3d-8e66-3c0117f5dd01`)
- S6: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25ddadda-586d-41e3-842b-0bae1decf3b9/resource) (`25ddadda-586d-41e3-842b-0bae1decf3b9`)
- S11: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/409f4e1e-fedd-4910-919f-f2b49698d98e/resource) (`409f4e1e-fedd-4910-919f-f2b49698d98e`)
- S7: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2931a091-5ed4-4540-9ee5-864498317345/resource) (`2931a091-5ed4-4540-9ee5-864498317345`)
- S5: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e2e2d01-6685-4e1b-ad66-4a47b428b073/resource) (`1e2e2d01-6685-4e1b-ad66-4a47b428b073`)
- S20: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/835fc4b9-c362-4720-9fe0-03c6caad0f84/resource) (`835fc4b9-c362-4720-9fe0-03c6caad0f84`)
- S3: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d9f7f42-20dd-4c50-a6b8-7470530ce095/resource) (`0d9f7f42-20dd-4c50-a6b8-7470530ce095`)
- S15: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6193ff8d-4832-4e3f-b80f-2d51da65c296/resource) (`6193ff8d-4832-4e3f-b80f-2d51da65c296`)
- S16: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63b3e66c-c55a-4cc4-82e0-b16103a22763/resource) (`63b3e66c-c55a-4cc4-82e0-b16103a22763`)
- S18: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/749d0b51-3857-4a91-9926-d67f29bd8056/resource) (`749d0b51-3857-4a91-9926-d67f29bd8056`)
- S30: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cebf24c0-955e-4e04-a8bf-1cead4723270/resource) (`cebf24c0-955e-4e04-a8bf-1cead4723270`)
- S10: [考虑螺旋离心泵水力性能及铸造成型的多目标优化设计研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3acdb0ec-4437-4905-9108-ced7c332daaf/resource) (`3acdb0ec-4437-4905-9108-ced7c332daaf`)
- S32: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S9: [大重量高精度复杂钛合金机匣整体铸造技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32243198-f474-446d-a8bb-09d29c23d0b6/resource) (`32243198-f474-446d-a8bb-09d29c23d0b6`)
- S26: [风机叶轮的低压铸造工艺模拟研究和模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab36d289-5d01-49bc-8bc9-071fa77b33a9/resource) (`ab36d289-5d01-49bc-8bc9-071fa77b33a9`)
- S17: [钛合金复杂薄壁构件离心熔模铸造充型与凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68683d2d-b213-4aaa-b276-c63ceebfa02d/resource) (`68683d2d-b213-4aaa-b276-c63ceebfa02d`)
- S28: [第三届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd5e7141-07ab-47be-8225-749b691edf98/resource) (`bd5e7141-07ab-47be-8225-749b691edf98`)
- S29: [铝合金水泵座压铸模浇注系统及镶块随形水道设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd080eb8-3294-4dc6-bda7-5cf3e35aba26/resource) (`cd080eb8-3294-4dc6-bda7-5cf3e35aba26`)
- S22: [固定网格方法中的水平集（Level Set）或体积流体（VOF）界面捕捉示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93abf68c-0eda-4f7b-b7c9-ba8b58bd30c2/resource) (`93abf68c-0eda-4f7b-b7c9-ba8b58bd30c2`)