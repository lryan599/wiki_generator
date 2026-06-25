---
version: "v1"
generated_at: "2026-06-18T17:44:50+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 23
  source_quality_score: 0.86
  freshness_score: 0.74
  evidence_coverage_score: 1.0
---

## 概述

SMAC法（简化标示粒子法），全称Simplified Marker And Cell，是MAC（Marker and Cell）法的简化版本，属于基于示踪粒子的压力修正型自由表面追踪方法，在计算流体力学（CFD）自由表面模拟体系中处于原始MAC法向SOLA-VOF法演进的过渡优化位置，是压铸充型流动数值模拟的常用方法之一[[S15,S18,S7]]。

原始MAC法由美国加利福尼亚大学的F.H.Harlow和J.E.Welch于1965年提出，用于求解带自由表面的粘性不可压缩流体的Navier-Stokes方程[[S27,S14,S22,S26]]。SMAC法由Amsden和Harlow针对原始MAC法求解过程复杂、压力泊松方程迭代效率低的问题提出简化版本，现有公开文献中未记载其精确首次提出年份[[S14,S10,S26]]。

## 技术原理

### 核心思想

原始MAC法的求解逻辑为对Navier-Stokes方程取散度得到压力泊松方程，将连续性方程作为约束条件对其变形，同步迭代求解Navier-Stokes方程与变形后的泊松方程，最终得到速度场和压力场，该过程需要同时迭代速度场与压力场，步骤繁琐且计算效率极低[[S27,S14,S22]]。

SMAC法的核心改进是引入势函数概念替代MAC法中需要反复迭代的压力泊松方程，在计算速度场时，离散后差分方程的迭代中没有压力项计算，校正压力项由校正势函数来替代，并用校正势函数来校正速度场。由于不求解压力泊松方程，迭代求解过程中迭代次数大幅减少，数值求解速度显著提高[[S27,S14,S15,S18,S26]]。

### 自由表面追踪

SMAC法沿用MAC法的无质量随流示踪粒子（标识点）体系，标识点不参与速度场、压力场的力学量计算，仅用于标记流体占据区域和追踪自由表面位置[[S26,S27,S22]]。标识点的速度分量通过相邻节点对应速度分量的二阶泰勒展开加权平均求得，计算中取泰勒展开阶数m=2以保证计算精度[[S26]]。

通过标识点分布将网格分为三类[[S4]]：

| 网格类型 | 判定规则 |
|---------|---------|
| 空网格 | 不含任何标识点 |
| 自由表面网格 | 包含标识点，且至少有一个相邻空网格 |
| 内部充满流体网格 | 包含标识点，且所有相邻网格均不为空 |

### 边界条件

自由表面区域的动力学边界条件满足[[S18]]：若外部气体为常值压力P₀，则液气交界面处法向应力Pₙₙ = -P₀，切向应力Pₙₜ = 0。

### 分步求解流程

SMAC法的速度-压力解耦策略分为三步[[S14,S27,S18]]：

1. **生成试算速度场**：将当前时刻已知的压力场代入离散后的Navier-Stokes方程，生成试算速度场；
2. **势函数迭代**：将试算速度代入连续性方程判断是否满足散度为零的条件，若不满足则迭代求解势函数方程；
3. **校正速度场与压力场**：通过势函数同时校正速度场和压力场，反复迭代直到计算速度场满足质量守恒要求。

全程无需反复联立N-S方程与压力泊松方程，实现“一场迭代”的高效求解模式[[S14,S27,S18]]。

## 数值方法

### 网格离散

SMAC法采用直角坐标系下的交错网格进行空间离散：速度变量定义在网格界面位置，其余标量物理量定义在网格中心位置[[S27,S9]]。对流项离散采用介于中心差分和上风方案之间的混合差分格式，时间项采用向前差分格式求解[[S9]]。

### 时间步长约束

SMAC法的时间步长需满足CFL约束条件[[S8]]：

| 约束类型 | 约束条件 |
|---------|---------|
| CFL主约束 | 一个时间步长内流体运动不超过一个完整网格单元，实际取值一般为理论最大允许步长的1/4~1/3 |
| 动量扩散约束 | 一个时间步长内动量扩散不能超过一个单元 |
| 表面张力约束 | 阻止表面张力波在一个时间步长内穿过一个以上网格单元 |

## 与MAC法的对比

| 对比维度 | MAC法（原始） | SMAC法（简化） |
|---------|-------------|--------------|
| 求解方式 | 压力场与速度场同时迭代，需反复迭代压力泊松方程与N-S方程 | 通过势函数一场迭代，不求解压力泊松方程 |
| 计算效率 | 低，迭代步骤繁琐 | 高，计算速度相比MAC法提升40%以上[[S16]] |
| 体积守恒精度（二维） | 误差10%~12% | 误差2%~3%[[S8]] |
| 自由表面追踪方式 | 无质量示踪粒子 | 无质量示踪粒子（一致） |
| 三维存储消耗 | 极大 | 极大（与MAC法一致）[[S27,S26,S10]] |

## 压铸领域的应用

### 研究应用实例

SMAC法在压铸充型模拟领域有多项代表性应用：

- **沈阳铸造研究所卢宏远团队**：基于SMAC法开发自定义计算程序，模拟压铸充型流动全过程，通过水力模拟实验验证了流场预测结果的合理性[[S25]]；
- **日本东北大学安斋浩一等（1988年）**：采用三维SMAC方法完成铝合金压铸件充型流动计算，成功实现冷隔缺陷的预测，模拟结果通过水力模拟实验完成验证比对[[S5,S21]]；
- **Lee WB团队**：采用SMAC方法模拟压铸充型阶段的流体流动，发现型腔内的流动模式和卷气模式对空腔壁厚的变化高度敏感，通过可视化水模拟实验完成验证[[S25]]；
- **南洋理工大学周文团队**：基于SMAC方法采用有限差分法求解完整Navier-Stokes方程，完成AM60B镁合金压铸充型过程的数值模拟，验证该方法可准确跟踪自由表面，可预测镁熔体以直喷形态进入模具型腔的流动行为[[S25]]。

### 工业应用

日立制作所早年推出的商用HICASS/FLOW压铸流动模拟工业系统，核心求解器基于三维SMAC法开发，以ADC12铝合金液压缸压铸充型为实测对象，通过模拟预测出合流位置的缺陷风险，实测发泡实验确认缺陷实际出现位置与模拟结果吻合度高，通过在预测缺陷区域增设溢流口即可显著提升铸件质量[[S24]]。

### 缺陷预测能力

SMAC法可支撑压铸充型过程中卷气、冷隔、浇不足三类典型流动相关缺陷的预测[[S16]]，在早期轻量化工业算例中自由表面追踪误差可控制在10%~15%区间[[S16]]。

## 改进与衍生

SMAC法的核心改进方向为Marker Surface（标记面元法），放弃全域分散的示踪粒子系统，直接采用离散标记面单元代表自由表面，大幅降低存储开销，结合自适应网格技术后在压铸充型模拟中可精准识别复杂型腔内部残留的卷气区域，预测结果与水模拟实验吻合度优于原始SMAC法[[S6]]。

后续SMAC技术逐步与SOLA求解框架融合，吸收VOF体积输运的优点，最终演变为面向工业场景的SOLA-VOF主流压铸求解体系，成为现代商用仿真软件的核心技术底座[[S6]]。

## 与同类方法的横向对比

| 对比维度 | SMAC法 | SOLA-VOF法 | 原始MAC法 |
|---------|--------|-----------|----------|
| 计算效率 | 中等，仅需单步势函数迭代 | 高，一场迭代，压力随机假设修正 | 低，需反复迭代压力泊松方程 |
| 自由表面捕捉精度 | 较高，示踪粒子定位界面准确，无明显数值扩散，小界面细节保真度优于基础VOF | 中等，VOF函数存在界面模糊问题 | 较高，与SMAC法机制一致 |
| 计算资源消耗 | 较高，三维场景下每个网格需配置多个示踪粒子，同规模算例内存占用为VOF法的2~3倍[[S14,S27]] | 低，体积函数替代大量示踪粒子 | 高，与SMAC法机制一致 |
| 剧烈大变形流动适应性 | 较差，示踪粒子在液面撕裂破碎场景下易出现分布错位[[S14,S27]] | 中等 | 较差 |

## 主流商业软件中的集成情况

目前主流压铸数值模拟商业软件原生核心求解器均以SOLA-VOF方法为主，未原生集成SMAC求解器[[S25,S1,S11,S3,S20]]：

| 软件 | 默认自由表面处理方法 | SMAC集成状态 |
|------|------------------|-------------|
| FLOW-3D | SOLA-VOF | 未原生集成，开放FORTRAN接口支持用户自定义二次开发[[S25,S1]] |
| MAGMASOFT | SOLA-VOF | 未原生集成[[S11]] |
| AnyCasting | VOF类算法 | 未原生集成[[S3,S20]] |
| OpenFOAM（interFOAM） | VOF框架 | 无原生SMAC求解器，可基于interFOAM二次开发定制类SMAC求解模块[[S19]] |

## 局限性

SMAC法存在以下公认局限性[[S27,S23]]：

1. **三维大规模计算存储瓶颈**：三维算例中示踪粒子总数量随网格数线性增长，超大规模压铸件仿真内存占用量远高于VOF法，存储开销过大限制其在工业级全尺寸算例的推广[[S27]]；
2. **剧烈变形流动适应性缺陷**：对湍流流动、气液掺混卷气夹杂渣相的多相流动场景适应不足，原始SMAC法未内置多相流耦合求解框架，无法直接追踪气泡形态演化和夹杂相运移过程[[S23]]；
3. **液面剧烈破碎时标识点追踪精度丢失**：压铸充型过程中出现金属液高速撕裂、液滴飞溅破碎工况时，分散的示踪粒子容易出现缺失、错位分布，无法连续重构断裂的自由表面，界面追踪精度显著下降[[S23]]。

## Sources
- S15: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b7c68ca-c779-40dd-b2d9-70f943b67af2/resource) (`7b7c68ca-c779-40dd-b2d9-70f943b67af2`)
- S18: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/941e62ab-18ce-4522-a134-0f79f286edf2/resource) (`941e62ab-18ce-4522-a134-0f79f286edf2`)
- S7: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30f61cb0-dedf-4d26-b9af-2f4753d7d468/resource) (`30f61cb0-dedf-4d26-b9af-2f4753d7d468`)
- S27: [材料热加工过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f722250c-4a77-4e98-b7de-5932ddef29fa/resource) (`f722250c-4a77-4e98-b7de-5932ddef29fa`)
- S14: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e2047a9-d219-406b-90c5-4eb8d94093db/resource) (`6e2047a9-d219-406b-90c5-4eb8d94093db`)
- S22: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4a74121-846c-4e0d-9d50-bfcec3bd0b00/resource) (`b4a74121-846c-4e0d-9d50-bfcec3bd0b00`)
- S26: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e18f7de3-184d-4019-8b7f-ce3592e7962b/resource) (`e18f7de3-184d-4019-8b7f-ce3592e7962b`)
- S10: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61026234-b5bb-43db-ac9a-9f8bf8c0f99e/resource) (`61026234-b5bb-43db-ac9a-9f8bf8c0f99e`)
- S4: [注塑成型模拟及模具优化设计理论与方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e038220-90da-406d-a8c5-b047c45720a4/resource) (`1e038220-90da-406d-a8c5-b047c45720a4`)
- S9: [材料热加工过程的数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c834314-52f5-4a4b-8ad2-506e054c4530/resource) (`5c834314-52f5-4a4b-8ad2-506e054c4530`)
- S8: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/529afef8-b98f-49be-8dcf-d773c555fb77/resource) (`529afef8-b98f-49be-8dcf-d773c555fb77`)
- S16: [流动解析中预测铸造缺陷的方法[3-8]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/83e8bbfb-e115-4606-96fd-f55e29579163/resource) (`83e8bbfb-e115-4606-96fd-f55e29579163`)
- S25: [铝合金压铸充型流态动态演变过程研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd33c10b-de41-47d0-a9cb-ef997fc6a2c4/resource) (`dd33c10b-de41-47d0-a9cb-ef997fc6a2c4`)
- S5: [压铸与液态模锻复合成形车用空调头盖技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22f36feb-b065-4cea-9bc8-1194309dbde0/resource) (`22f36feb-b065-4cea-9bc8-1194309dbde0`)
- S21: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2083306-7825-4577-a28a-09c409fc7760/resource) (`b2083306-7825-4577-a28a-09c409fc7760`)
- S24: [国外铸锻件制造新技术资料汇编](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cab2fa81-8124-425f-be9a-4c5b0f5e15a9/resource) (`cab2fa81-8124-425f-be9a-4c5b0f5e15a9`)
- S6: [application of an adaptive grid refinement technique to three dimensiona__31a3a80cd3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/231d1307-2fa2-4895-bffa-49ec0d0e62eb/resource) (`231d1307-2fa2-4895-bffa-49ec0d0e62eb`)
- S1: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/112a7bab-6f8f-48c8-8749-731180dc6620/resource) (`112a7bab-6f8f-48c8-8749-731180dc6620`)
- S11: [不同型腔真空度对铸件组织和性能的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/666a4caa-0a9e-4e1f-a7e6-c019ad4c40be/resource) (`666a4caa-0a9e-4e1f-a7e6-c019ad4c40be`)
- S3: [表1-1 国外主要的铸造模拟软件[46]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b8110ac-cc84-431c-98ef-fb7ed2823f1c/resource) (`1b8110ac-cc84-431c-98ef-fb7ed2823f1c`)
- S20: [5.8 截面 L 处的缺陷预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afadac5d-c420-4a80-9731-51d5d567b375/resource) (`afadac5d-c420-4a80-9731-51d5d567b375`)
- S19: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b3b6c4c-8a35-4a37-9b12-4525d0d17fad/resource) (`9b3b6c4c-8a35-4a37-9b12-4525d0d17fad`)
- S23: [湍流模型及有限分析法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be606064-c308-452a-af65-8cc1e31ad736/resource) (`be606064-c308-452a-af65-8cc1e31ad736`)