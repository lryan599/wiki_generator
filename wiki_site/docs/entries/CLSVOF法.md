---
version: "v1"
generated_at: "2026-06-18T18:27:10+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 20
  source_quality_score: 0.85
  freshness_score: 0.78
  evidence_coverage_score: 1.0
---

## 概述

CLSVOF（Coupled Level Set and Volume of Fluid，耦合水平集-流体体积法）是一种针对两相流界面追踪的耦合型数值方法[[S22,S6,S15]]。该方法于2000年由Mark Sussman与E.G. Puckett在《Journal of Computational Physics》上首次正式发表，核心提出人为Mark Sussman[[S10,S20]]。CLSVOF法同时继承了两类主流界面追踪方法的优势——既保留了传统流体体积法（VOF）天然具备的质量守恒特性，又能像水平集法（Level Set）那样连续、光滑地计算界面法向量与曲率，被认为有效克服了纯VOF方法在相界面附近相函数不连续、曲率计算精度低，以及纯Level Set方法在输运过程中质量不守恒的各自缺陷[[S22,S2,S15,S20,S19]]。

在高压压铸（HPDC）领域，CLSVOF法通过与不可压缩液态金属-可压缩气相两相流模型结合，可精确捕捉高速充型过程中气液两相界面的复杂拓扑变化，能够同时预测宏观气团与微观弥散气泡两类卷气缺陷[[S3,S18]]。目前，该方法在铸造模拟中的应用仍主要基于学术研究层面二次开发的求解器，主流商用压铸模拟软件ProCAST、MAGMASOFT的公开文档中未见内置原生CLSVOF求解模块的明确说明[[S23,S24]]。

## 基本原理与核心算法

CLSVOF方法的核心思想在于通过同时维护体积分数场与水平集函数两套变量，将VOF的守恒特性与Level Set的高精度几何计算能力融合在同一求解框架内[[S15,S7]]。

### 体积分数输运

方法首先求解守恒形式的VOF体积分数输运方程：

$$
\frac{\partial F}{\partial t} + \vec{v} \cdot (\nabla F) = 0
$$

其中，$F$ 为控制体内液相的体积占比，取值0对应纯气相单元、1对应纯液相单元、0到1之间对应两相混合单元[[S15,S7]]。通过对体积分数的显式跟踪，该方法天然保证了体系的质量守恒。

### Level Set函数输运

随后求解Level Set函数的对流输运方程：

$$
\frac{\partial \phi}{\partial t} + \vec{v} \cdot (\nabla \phi) = 0
$$

Level Set函数$\phi$定义为网格中心到两相界面的带符号距离：液相区域$\phi<0$，气相区域$\phi>0$，界面位置$\phi=0$[[S7]]。基于该连续光滑函数，可直接高精度计算界面法向量与曲率，从而准确求解表面张力，解决了纯VOF方法因相函数在界面处不连续而难以精确计算曲率的缺陷[[S7,S22]]。

### 高阶格式与重新初始化

为降低数值耗散，CLSVOF方法采用5阶加权本质无振荡格式（WENO）同时求解VOF与Level Set的对流输运方程。完成输运步骤后，还需对Level Set函数执行重新初始化操作，以维持其带符号距离函数的物理属性[[S7]]。

### 跨界面物理量插值

借助Level Set函数的连续光滑特性，采用平滑的Heaviside函数对界面附近的密度、粘度等物理量进行插值，消除纯VOF方法在界面区域物理量不连续的问题，使CLSVOF能够适配大密度比（如1000:1）、大粘度比的气液两相流场景[[S7]]。

**图1：CLSVOF方法体积分数场离散分布示意图**
![CLSVOF方法中体积分数场的离散化网格分布，网格单元数值对应液相与气相体积占比，蓝色区域代表液相，数值从1（纯液相）到0（纯气相）渐变，直观呈现液气界面拓扑结构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fce1538c-5136-438d-a741-69b9cf458f50/resource)

## 方法对比

以下从多维度系统比较纯VOF法、纯Level Set法与CLSVOF法的特性差异：

| 对比维度 | VOF法 | Level Set法 | CLSVOF法 |
|---------|-------|------------|----------|
| 质量守恒性 | 天然满足，直接跟踪体积分数[[S22,S13,S8]] | 存在明显质量/体积损失，无天然保障[[S22,S1]] | 保留VOF的天然质量守恒优势[[S2,S15]] |
| 界面连续性 | 相函数$F$在跨界面位置不连续[[S22]] | Level Set函数连续光滑[[S22]] | 界面附近物理量连续[[S7]] |
| 曲率计算精度 | 差，因相函数不连续导致空间导数计算困难[[S22]] | 高，由连续函数直接计算[[S22]] | 高，基于Level Set函数计算[[S2]] |
| 数值扩散 | 普通离散格式下易出现界面模糊[[S13,S8]] | 相对较低 | 数值扩散水平低[[S15]] |
| 实现难度 | 低，已有成熟代码基础[[S13]] | 中等 | 高，需同时维护两套变量[[S2,S15]] |
| 计算成本 | 低 | 中等 | 高于单一方法[[S15]] |
| 复杂拓扑处理 | 中等 | 能够描述复杂拓扑变化[[S1]] | 可准确描述复杂两相界面拓扑变化[[S2]] |

## 优势与局限性

### 突出优势

公开学术文献明确验证了CLSVOF方法具备以下核心优势[[S22,S2]]：

1. **质量守恒与界面精度的双重保障**：通过耦合VOF与Level Set，在天然保证质量守恒的同时实现高精度曲率计算与连续物理量插值，克服了纯VOF法曲率不准、界面处物理量不连续的缺陷，以及纯Level Set法质量不守恒的问题。
2. **大物性比适应能力**：可精准模拟密度比达1000:1、粘度比达10:1的两相流问题，并已通过标准破坝算例验证[[S4,S19]]。
3. **可改造性**：可基于现有成熟的VOF、Level Set与SOLA代码进行二次开发实现[[S2]]。

### 主要局限性

1. **算法复杂度较高**：需要同时求解并维护VOF体积分数场与Level Set距离函数两套变量的对流输运及重新初始化，整体开发复杂度和计算成本均高于单一的VOF或纯Level Set方法[[S2,S15]]。
2. **网格依赖性**：针对高速水充型场景的数值验证表明，需采用约3mm级别的网格尺寸才能获得满足网格无关性要求的收敛解，以保证气液界面追踪精度[[S4]]。
3. **三维与多物理场耦合待完善**：公开研究中，CLSVOF方法在三维场景下耦合湍流、凝固全过程模型的扩展开发工作目前仍处于推进阶段，尚未完全成熟落地[[S2]]。

**图2：破坝算例在无量纲时间$t^*=0.5$时刻的瞬态仿真结果**
![破坝问题的瞬态数值模拟结果，包含水波演化轮廓、气液两相静压云图及流速矢量，用于验证CLSVOF方法在大密度比、大粘度比两相流场景下的仿真能力](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7da82f9e-4edf-42f7-9297-1c03fb958eec/resource)

## 技术演进与变体

CLSVOF方法的技术演进脉络可简要归纳如下[[S6,S20,S2]]：

- **前身基础**：SOLA-VOF方法在铸造充型模拟中已获得广泛应用。
- **原型提出**：2000年，Mark Sussman与E.G. Puckett首次发表CLSVOF基础原型[[S10]]。
- **铸造场景适配**：后续衍生出面向铸造充型场景的同源变体，如Pang等人提出的SOLA粒子水平集耦合方法，进一步提升了铸造充型过程两相流求解的鲁棒性[[S6]]。
- **压铸专用改进**：Bi C等人于2015年在《China Foundry》上发表成果，将CSF（Continuum Surface Force）模型与CLSVOF方法结合，进一步优化了高压压铸场景下表面张力的计算精度[[S5,S9]]。

当前，CLSVOF方法在铸造模拟领域以学术研究的二次开发版本为主，主流商用压铸模拟软件（如ProCAST、MAGMASOFT）的公开官方文档中暂未提及内置该求解模块[[S23,S24]]。

---

## 在压铸及两相流领域的应用

### 充型过程气液两相流模拟

CLSVOF在高压压铸充型模拟中的首次工程化适配，是通过与不可压缩液态金属-可压缩气相两相流模型相结合实现的。该模型采用改进的ESOLA（Extended SOLA）算法求解控制方程，同时考虑空气的可压缩性与相界面的表面张力，可以精确捕捉高速压铸充型过程中气液两相之间的相互作用与相界面演化[[S3,S16,S18]]。水模拟试验与仿真对比结果表明，该模型的预测结果与实验吻合度显著优于仅假设气相不可压缩的传统模型[[S3]]。

针对不同物理假设的对比仿真（方案A：同时考虑空气可压缩性和表面张力；方案B：仅考虑空气可压缩性；方案C：两者均不考虑）表明：不考虑表面张力时，卷气量预测偏小；而不考虑空气可压缩性时，预测的卷气缺陷大于实际情况；仅方案A的模拟结果与实际水模拟试验吻合良好[[S3]]。

### 卷气缺陷预测

CLSVOF方法支持的压铸两相流模拟能够同时预测两类卷气缺陷[[S3,S18]]：

| 缺陷类型 | 特征描述 |
|---------|---------|
| 宏观气泡 | 可长时间保持宏观形态，随自由界面在金属液内移动的宏观气团 |
| 微观气泡 | 因外部压力作用破碎后弥散分布在金属液内部的气体 |

通过追踪充型过程中的气相演变，CLSVOF方法可为卷气缺陷的定量评估与模具工艺优化提供有效数值支撑[[S3,S18]]。

### 典型算例参数参考

下表汇总了压铸充型模拟的典型基准工艺参数，可作为CLSVOF方法在压铸场景验证计算的标准输入参考[[S14]]：

| 参数项 | 数值 |
|-------|------|
| 模具材料 | 8418 |
| 模具初始温度 | 150°C |
| 压铸合金 | AlSi9Cu3 |
| 铝液温度 | 650°C |
| 低速速度 | 0.2 m/s |
| 高速速度 | 4.65 m/s |
| 高速切换位置 | 浇口处 |
| 浇口面积 | 1637 mm² |
| 冲头直径 | 170 mm |

## Sources
- S22: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a10cebfa-57da-40d1-8cd0-3ce33a4a83ed/resource) (`a10cebfa-57da-40d1-8cd0-3ce33a4a83ed`)
- S6: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a535a41-b2f3-4e7c-9c98-214067d8d234/resource) (`2a535a41-b2f3-4e7c-9c98-214067d8d234`)
- S15: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6193ff8d-4832-4e3f-b80f-2d51da65c296/resource) (`6193ff8d-4832-4e3f-b80f-2d51da65c296`)
- S10: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fd5f4f1-4e71-4e34-975d-b0609759aedb/resource) (`3fd5f4f1-4e71-4e34-975d-b0609759aedb`)
- S20: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97726e24-e029-4370-9696-63b2fe157b62/resource) (`97726e24-e029-4370-9696-63b2fe157b62`)
- S2: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d9f7f42-20dd-4c50-a6b8-7470530ce095/resource) (`0d9f7f42-20dd-4c50-a6b8-7470530ce095`)
- S19: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/964ee5b0-bd8f-41cf-a325-3666234cdb4a/resource) (`964ee5b0-bd8f-41cf-a325-3666234cdb4a`)
- S3: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e2e2d01-6685-4e1b-ad66-4a47b428b073/resource) (`1e2e2d01-6685-4e1b-ad66-4a47b428b073`)
- S18: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/835fc4b9-c362-4720-9fe0-03c6caad0f84/resource) (`835fc4b9-c362-4720-9fe0-03c6caad0f84`)
- S23: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad6c9c60-152c-47f8-8f2b-e5f6673bf7a5/resource) (`ad6c9c60-152c-47f8-8f2b-e5f6673bf7a5`)
- S24: [0089_15b9d2296937bddc_铸造模拟软体](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b79f26d4-1fec-47be-b039-91daa3282688/resource) (`b79f26d4-1fec-47be-b039-91daa3282688`)
- S7: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ea0556f-ef4f-4d56-b886-e80ce6719e29/resource) (`2ea0556f-ef4f-4d56-b886-e80ce6719e29`)
- S13: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57bb9bfd-f8bb-4dca-bfb1-2da078f1985a/resource) (`57bb9bfd-f8bb-4dca-bfb1-2da078f1985a`)
- S8: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/337b41ce-f048-422b-8f71-85d1d1d17def/resource) (`337b41ce-f048-422b-8f71-85d1d1d17def`)
- S1: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/023e67b7-e6eb-4e94-9c0e-028602a1e0a5/resource) (`023e67b7-e6eb-4e94-9c0e-028602a1e0a5`)
- S4: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ea6e133-cf5f-4766-adb5-6f564e6c461b/resource) (`1ea6e133-cf5f-4766-adb5-6f564e6c461b`)
- S5: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2931a091-5ed4-4540-9ee5-864498317345/resource) (`2931a091-5ed4-4540-9ee5-864498317345`)
- S9: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3be60a15-8b26-43b4-b63c-b389f5207c92/resource) (`3be60a15-8b26-43b4-b63c-b389f5207c92`)
- S16: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b380485-2c1d-4fe4-af9f-f13ef7f06b8c/resource) (`6b380485-2c1d-4fe4-af9f-f13ef7f06b8c`)
- S14: [表1 模拟分析工艺参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59e747c6-c680-411e-b2d0-82d2625cd5fe/resource) (`59e747c6-c680-411e-b2d0-82d2625cd5fe`)