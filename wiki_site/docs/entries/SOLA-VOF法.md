---
version: "v1"
generated_at: "2026-06-18T12:11:11+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 22
  source_quality_score: 0.87
  freshness_score: 0.73
  evidence_coverage_score: 1.0
---

## 概述

SOLA-VOF法是一种用于求解铸造充型过程流场的数值模拟算法，全称为 **解法-体积函数法**（Solution Algorithm - Volume of Fluid），由SOLA压力-速度迭代求解算法与VOF自由表面捕捉算法耦合而成[[S5,S7,S19]]。该方法由美国加利福尼亚大学管理的洛斯阿拉莫斯（Los Alamos）国家实验室在MAC方法基础上发展而来，于1980年通过编号为LA-8355的官方技术报告《SOLA-VOF: A Solution Algorithm for Transient Fluid Flow with Incompressible Flows with Free Surface》正式发布，核心贡献研究者为Hirt、Nichols等[[S5,S8,S13]]。

SOLA-VOF法是铸造充型数值模拟领域应用最广泛的算法之一，覆盖压铸、低压铸造、重力铸造、熔模精密铸造等多种工艺的充型模拟，可求解流场分布、自由表面动态演化、卷气缺陷预测及充型前沿形态识别等物理量[[S4,S21]]。

## 定义与全称

- **SOLA**：Solution Algorithm（解法），是一种压力-速度耦合的迭代求解算法框架[[S5,S7]]。
- **VOF**：Volume of Fluid（体积函数），是一种通过定义单元内流体体积分数来追踪自由表面的方法[[S7,S19]]。
- **SOLA-VOF**：将上述两种算法耦合的充型过程流场数值模拟技术，利用SOLA求解动量方程与连续性方程获取速度场与压力场，利用VOF处理自由表面的位置与形状[[S4,S19]]。

## 起源与发展历史

SOLA-VOF法由美国加利福尼亚大学管理的**洛斯阿拉莫斯（Los Alamos）国家实验室**研发，Hirt、Nichols等为核心贡献研究者，1980年正式发布编号为LA-8355的官方技术报告[[S5,S8,S13]]。该方法是针对早期MAC（Marker and Cell，1965年提出）及SMAC（Simplified MAC）方法中因采用大量示踪粒子追踪自由表面导致的内存消耗大、求解速度慢等问题而开发的改进方案，用体积函数F替代示踪粒子，显著节省内存并提高计算速度[[S13,S23]]。

> **说明**：原始SOLA-VOF代码为有限差分法求解程序，后续已被拓展兼容有限元与有限体积离散框架[[S7]]。

## 分类归属

SOLA-VOF法属于计算流体力学（CFD）中**有限差分框架**下的压力-速度耦合求解与自由表面追踪方法。

- **离散框架**：初始基于交错有限差分网格开发，速度分量定义在网格界面，标量（压力、体积函数F）定义在网格中心[[S13,S23]]。目前已拓展兼容有限元与有限体积离散方案[[S7]]。
- **技术传承关系**：SOLA-VOF法是MAC方法、SMAC方法的迭代优化版本，但与SIMPLE系列算法分属不同的压力-速度耦合技术路线。SOLA-VOF采用单场迭代、直接压力修正；SIMPLE类方法则采用双场同时迭代求解[[S13]]。

## 核心算法原理

### 1. 控制方程

SOLA-VOF法求解的控制方程包含三类[[S3,S19,S20]]：

| 方程类型 | 数学形式 | 说明 |
|---------|---------|------|
| 连续性方程（质量守恒） | \(D = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0\) | 散度D为零是压力校正的收敛判据 |
| Navier-Stokes动量守恒方程（三维） | \(\rho \left(\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} + w\frac{\partial u}{\partial z}\right) = -\frac{\partial P}{\partial x} + \rho g_x + \mu \nabla^{2} u\) （v, w分量同理） | 描述不可压缩粘性流体的动量守恒 |
| 体积函数输运方程 | \(\frac{\partial F}{\partial t} + u\frac{\partial F}{\partial x} + v\frac{\partial F}{\partial y} + w\frac{\partial F}{\partial z} = 0\) | F为单元内流体体积与单元总体积的比值，取值范围0~1 |

### 2. 压力-速度耦合机制（SOLA算法核心）

SOLA采用独特的**单场迭代方案**[[S5,S11,S14]]：
1. 以当前时刻初始条件或上一时刻收敛值为基础，通过离散N-S方程计算当前时刻的试算速度。
2. 对每个单元计算散度 \(D_{i,j,k}\)，检验是否满足连续性方程（收敛阈值通常取 \(10^{-3}\)）。
3. 若不满足，通过压力校正公式 \(\delta p^n = -D_{i,j,k} / \frac{\partial D_{i,j,k}}{\partial p}\) 直接计算校正压力，再校正速度场。
4. 反复迭代校正，无需联立求解压力泊松方程，整个过程只有一场迭代循环，计算速度快[[S5,S9,S13]]。

### 3. VOF自由表面追踪原理

VOF法定义体积函数 \(F =\) 单元内流体体积/单元总体积，根据F值将网格分为三类[[S5,S7]]：

| F值 | 网格状态 | 含义 |
|-----|---------|------|
| \(F = 0\) | 空网格 | 无流体 |
| \(F = 1\) | 满网格 | 内部流体域 |
| \(0 < F < 1\) | 半满网格/边界网格 | 自由表面所在位置 |

为消除普通离散格式的假扩散与界面模糊问题，原始SOLA-VOF提供两类界面优化方案[[S5,S7]]：
- **施体-受体（Donor-Acceptor）法**：同时利用单元边界上游及下游的流率信息重构自由表面形状。
- **Van Leer二阶流率近似**：通过保证算法单调性来抑制高阶差分数值振荡。

### 4. 离散化与网格类型

原始SOLA-VOF采用**交错有限差分网格**，速度分量定义在网格界面，压力与体积函数F等标量定义在网格中心[[S13,S23]]。

## 计算流程

完整算法执行步骤如下[[S10,S11,S14]]：

1. **试算速度计算**：以初始条件或上一时刻收敛结果为基础，通过离散N-S方程计算当前时刻的试算速度场。
2. **散度计算**：对每个单元计算散度 \(D_{i,j,k}\)。
3. **收敛判断**：校验所有单元散度是否小于收敛阈值（一般取 \(10^{-3}\)）。若全部满足，当前时间步计算结束，转至步骤6。
4. **压力校正**：若不满足收敛条件，计算压力修正量 \(\delta p^n\)，更新单元压力 \(p^{n+1} = p^n + \delta p^n\)。
5. **速度校正**：根据校正后的压力更新速度场，返回步骤2继续迭代，直至所有单元满足连续性方程。
6. **体积函数更新**：求解体积函数输运方程，更新每个单元的F值，确定下一时刻流动域与自由表面位置。
7. **时间推进**：进入下一时间步长，重复步骤1~6，直至充型完成。

## 在压铸/铸造中的应用

SOLA-VOF法是当前铸造充型数值模拟领域应用最广泛的算法之一[[S4,S21]]：

- **适用工艺**：覆盖压铸、低压铸造、重力铸造、熔模精密铸造等全品类铸造工艺的充型模拟。
- **模拟功能**：支持求解流场分布、自由表面动态演化、卷气缺陷预测、充型前沿形态识别、飞溅与卷气行为等物理量。

## 优势与局限性

### 优势[[S5,S13]]

- 收敛域范围宽，迭代收敛稳定性好
- 计算CPU时间短，存储占用量远低于MAC、SMAC类算法（用单一F函数代替大量示踪粒子）
- 三维场景适配性强
- 单场迭代，算法实现相对简洁

### 局限性[[S5,S15,S18]]

- 当压力梯度极大或网格数目很多时，收敛速度明显变慢，求解时间大幅延长
- 原始二维拓展至三维时，自由表面方向判定复杂，需分析多种情况确定边界条件
- 原始施主-受主法存在数值假扩散，导致界面模糊；对三维计算不太适合，需采取修正方法

## 与其他方法的对比

### 与MAC/SMAC方法的对比

| 对比维度 | MAC法 | SOLA-MAC法 | SOLA-VOF法 |
|---------|-------|-----------|-----------|
| 迭代机制 | 反复迭代N-S方程和泊松方程 | 势函数一场迭代 | 单场迭代，直接压力修正 |
| 自由表面追踪 | 大量示踪粒子标记 | 少量示踪粒子仅追踪流体边界 | 体积函数F，完全摒弃示踪粒子 |
| 内存占用 | 高 | 中等 | 低 |
| 计算速度 | 慢 | 提升 | 显著提升 |

[[S1,S13]]

### 与Level Set方法的对比

Level Set方法通过求解水平集函数的零等值面来确定自由表面，计算精度和速度均高于原始SOLA-VOF，且无需复杂界面重构即可描述界面的复杂拓扑变化。但Level Set方法天然不具备质量守恒特性，可通过CLSVOF（耦合Level Set和VOF）方法融合两者优势[[S15,S17]]。

## 改进版本与后续发展

SOLA-VOF的主流衍生与改进版本包括[[S2,S17]]：

- **PLIC-VOF**（分段线性界面重构）：改善三维自由表面跟踪精度
- **CLSVOF**（耦合Level Set和VOF）：兼具VOF的质量守恒优势与Level Set的界面几何参数计算精度优势
- **改进压力校正型SOLA算法**：支持高压力梯度下不可压缩-可压缩两相流求解

## 积存软件与实现

主流铸造仿真软件中SOLA-VOF及相关改进方法的集成情况[[S16,S21]]：

- **Flow-3D**：原生采用SOLA-VOF作为核心自由表面求解器
- **AnyCasting**：内置原生SOLA-VOF模块，用于有限差分网格的充型模拟
- **MAGMAsoft、ProCAST**：集成了基于SOLA-VOF改进的VOF类充型求解器

## 图示

SOLA-VOF法中的施主-受主流量法通过同时利用单元边界上游及下游的流率信息来重构自由表面形状，图中标注了计算网格单元、流体流动方向及施主/受主单元[[S12]]。

![图6.2-7 施主-受主流量法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ac0e5cb-5264-436e-9ac4-37ed61e5dc36/resource)

SOLA-VOF在三维空间扩展时，需计算自由表面法向量以确定其取向，图中标注了节点i,j,k及FL、FR、FT、FB各方向的体积分数点，用于法向量计算[[S6]]。

![SOLA-VOF三维自由表面法向量计算示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f0be1f2-e322-4987-b82a-9f9a5ba2c8bf/resource)

## Sources
- S5: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57bb9bfd-f8bb-4dca-bfb1-2da078f1985a/resource) (`57bb9bfd-f8bb-4dca-bfb1-2da078f1985a`)
- S7: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61026234-b5bb-43db-ac9a-9f8bf8c0f99e/resource) (`61026234-b5bb-43db-ac9a-9f8bf8c0f99e`)
- S19: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae6f5d9b-60f8-43b9-b5a2-8776b84cd557/resource) (`ae6f5d9b-60f8-43b9-b5a2-8776b84cd557`)
- S8: [american institute of aeronautics and astronautics 31st thermophysics co__84bde37c6f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61609c96-0c5f-4e01-b461-1c47d2ca7c3c/resource) (`61609c96-0c5f-4e01-b461-1c47d2ca7c3c`)
- S13: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/941e62ab-18ce-4522-a134-0f79f286edf2/resource) (`941e62ab-18ce-4522-a134-0f79f286edf2`)
- S4: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53cdc1b8-02dd-4190-bfff-c3e80c5057b0/resource) (`53cdc1b8-02dd-4190-bfff-c3e80c5057b0`)
- S21: [铝合金压铸充型流态动态演变过程研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd33c10b-de41-47d0-a9cb-ef997fc6a2c4/resource) (`dd33c10b-de41-47d0-a9cb-ef997fc6a2c4`)
- S23: [材料热加工过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f722250c-4a77-4e98-b7de-5932ddef29fa/resource) (`f722250c-4a77-4e98-b7de-5932ddef29fa`)
- S3: [汽车发动机铝合金缸体压铸工艺及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/257e7a35-aae1-40c6-9294-b8701de9fa2c/resource) (`257e7a35-aae1-40c6-9294-b8701de9fa2c`)
- S20: [凝固界面换热系数反求及铝合金薄壁件压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be9898a0-41f7-47ec-9b6f-0b7ce01a7350/resource) (`be9898a0-41f7-47ec-9b6f-0b7ce01a7350`)
- S11: [现代模具设计基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73a91925-e73b-4acf-bdad-d91b37df3e10/resource) (`73a91925-e73b-4acf-bdad-d91b37df3e10`)
- S14: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94502db5-d4a1-4844-b335-04f449644b23/resource) (`94502db5-d4a1-4844-b335-04f449644b23`)
- S9: [半固态金属成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65335625-90d3-4ca0-b231-2555c816f2d3/resource) (`65335625-90d3-4ca0-b231-2555c816f2d3`)
- S10: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69f72864-f01d-418b-b3a0-18bf756088a6/resource) (`69f72864-f01d-418b-b3a0-18bf756088a6`)
- S15: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97726e24-e029-4370-9696-63b2fe157b62/resource) (`97726e24-e029-4370-9696-63b2fe157b62`)
- S18: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/acdd4d48-ad37-40ee-beb8-6c7739829a5f/resource) (`acdd4d48-ad37-40ee-beb8-6c7739829a5f`)
- S1: [充型过程数值模拟方法及其优缺点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03c27de9-90c7-4900-8d71-16034ac48633/resource) (`03c27de9-90c7-4900-8d71-16034ac48633`)
- S17: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a10cebfa-57da-40d1-8cd0-3ce33a4a83ed/resource) (`a10cebfa-57da-40d1-8cd0-3ce33a4a83ed`)
- S2: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d9f7f42-20dd-4c50-a6b8-7470530ce095/resource) (`0d9f7f42-20dd-4c50-a6b8-7470530ce095`)
- S16: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf/resource) (`a0ba7cc7-8e65-43ee-b3d3-147f8153e4bf`)
- S12: [图6.2-7 施主-受主流量法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ac0e5cb-5264-436e-9ac4-37ed61e5dc36/resource) (`8ac0e5cb-5264-436e-9ac4-37ed61e5dc36`)
- S6: [自由表面方向计算示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f0be1f2-e322-4987-b82a-9f9a5ba2c8bf/resource) (`5f0be1f2-e322-4987-b82a-9f9a5ba2c8bf`)