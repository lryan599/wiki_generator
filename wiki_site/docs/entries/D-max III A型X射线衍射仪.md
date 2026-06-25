---
version: "v1"
generated_at: "2026-06-18T16:06:30+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 10
  source_quality_score: 0.86
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

D/max III A 型 X 射线衍射仪是由日本理学（Rigaku）生产的多晶 X 射线衍射仪，隶属于 Rigaku D/max 系列[[S8]]。该设备适配粉末与块状两类样品的检测，在材料科学与冶金领域被广泛用于物相定性分析、定量分析、晶格参数计算及微观结构表征[[S6,S5]]。在压铸合金研究中，该设备可直接用于合金试样的第二相物相鉴别，已有公开文献将其用于 Mg-5Zn-xGd-0.6Zr 压铸合金的微观组织表征[[S8]]。

> **参数勘误**：部分公开实验记录中标注该设备工作电压为“40V”，经核实为笔误；结合 Rigaku D/max 同系列产品通用参数，真实管电压为 **40 kV**[[S9,S4]]。

## 核心技术参数

经实验记录验证的实测运行参数如下[[S8,S9,S4]]：

| 参数项 | 规格 |
|--------|------|
| X 射线管靶材 | Cu 靶，Kα 射线 |
| 特征波长 | λ = 1.54056 Å（Cu Kα） |
| 管电压 | 40 kV |
| 管电流 | 40 mA |
| 常规扫描范围（2θ） | 20°～90° |
| 常规扫描速度 | 4°/min |

## 结构与组成

多晶 X 射线衍射仪的通用核心结构由四大模块组成[[S2]]：

- **X 射线发生器**：包含高压控制系统与 X 光管，可发射连续 X 射线与特征 X 射线两类信号[[S2]]。
- **测角仪**：支持 θ/2θ 联动同步旋转，X 射线光焦点与计数管窗口均分布在测角仪圆上，试样及试样台位于测角仪圆正中心位置[[S2]]。
- **辐射探测器**：通用配置包含正比计数器（PC）和闪烁计数器（SC）两种类型。正比计数器脉冲分辨时间约 10⁻⁶ s，能量分辨率高；闪烁计数器分辨时间约 10⁻⁵ s，计数效率高[[S2,S5]]。
- **记录与自动控制单元**：将电脉冲信号放大处理后描绘成衍射图，输出衍射强度随 2θ 角的变化[[S2]]。

### 测角仪光路示意

![X射线衍射仪测角仪结构示意图，标注了衍射仪圆、样品台、探测器、刻度盘等关键部件及光路走向](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/016e666c-a1b5-4ad6-8bb0-b23ee83ed405/resource) [[S1]]

该示意图出自 X 射线衍射专业教材，标注了衍射仪圆（G）、试样（D）、X 射线光源（S）、试样台（H）、接收狭缝（F）、计数管（C）、支架（E）及刻度尺（K）等关键部件，完整呈现了衍射测量的光路走向[[S1,S2]]。

## 应用领域

### 通用应用

该类衍射仪在材料科学、冶金、地质领域的通用功能覆盖[[S10,S5,S6]]：

- 晶体结构测定与晶格参数计算
- 晶粒尺寸分析与晶体缺陷表征
- 物相定性分析：通过比较衍射花样区分不同物质
- 物相定量分析：利用衍射线强度确定各物相相对含量
- 织构检测与残余应力测量

在数据处理方面，配合 Jade 等专业分析软件可完成 PDF 标准卡片的自动检索匹配，大幅提升物相分析效率[[S6]]。

### 压铸合金相分析

在压铸领域，D/max III A 型衍射仪的典型应用场景为压铸合金试样的第二相物相鉴别[[S8]]。将衍射数据导入 Jade 6 软件，可分析并确定合金中的第二相组成，为压铸工艺开发与质量控制提供微观组织依据[[S8]]。

## 同系列产品性能对比

Rigaku D/max 2500PC 为 D/max 系列的后续升级型号，性能显著优于 D/max III A[[S9,S3]]：

| 参数项 | D/max III A | D/max 2500PC |
|--------|-------------|--------------|
| 最大功率 | 3 kW 级别 | 18 kW |
| 管电压 | 40 kV | 40 kV |
| 最大管电流 | 40 mA | 250 mA |
| 扫描速度 | 4°/min | 4°/min（可调） |
| 扫描范围 | 20°～90° | 20°～80°（可调） |
| 靶材 | Cu Kα | Cu Kα |
| 特殊功能 | 常规物相分析 | 支持位错密度、微应变高精度定量检测 |

注：D/max 2500PC 参数来自文献[[S9,S3]]；同类经典型号的一般性能区间参考[[S7]]。

## 局限性与演化

D/max III A 作为 Rigaku D/max 系列中的经典型号，具备满足常规物相分析需求的基本性能，但与后续升级型号相比存在明显局限：管电流上限较低（40 mA），扫描速度固定且较慢，不具备阵列探测器等现代化配置，无法胜任需要高精度微观结构定量检测（如位错密度、微应变测量）的先进分析任务[[S9,S3]]。当前该型号在服役文献中已较少出现，多为历史留存设备或特定教学、基础研究场景使用。

## Sources
- S8: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd873cbb-128d-474d-80c2-c74866083ce0/resource) (`bd873cbb-128d-474d-80c2-c74866083ce0`)
- S6: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/85e7d669-dea3-465a-b590-40d136e4cb55/resource) (`85e7d669-dea3-465a-b590-40d136e4cb55`)
- S5: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c1cfd94-1605-43f7-819d-fcb25b4fb8d0/resource) (`7c1cfd94-1605-43f7-819d-fcb25b4fb8d0`)
- S9: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd2879e9-f15d-4c69-8d01-fb99aa292821/resource) (`dd2879e9-f15d-4c69-8d01-fb99aa292821`)
- S4: [先进轻合金修复与强化技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/798b0e53-d521-4346-adea-a0c072cb2b49/resource) (`798b0e53-d521-4346-adea-a0c072cb2b49`)
- S2: [现代电化学表面处理专论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22a73477-8d17-4881-ad61-9d66fb911ebf/resource) (`22a73477-8d17-4881-ad61-9d66fb911ebf`)
- S1: [X射线衍射仪结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/016e666c-a1b5-4ad6-8bb0-b23ee83ed405/resource) (`016e666c-a1b5-4ad6-8bb0-b23ee83ed405`)
- S10: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8c50f34-29d7-4cfc-901d-e26446b51b31/resource) (`f8c50f34-29d7-4cfc-901d-e26446b51b31`)
- S3: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fe9921e-df0e-492d-9653-31d61de45a7a/resource) (`6fe9921e-df0e-492d-9653-31d61de45a7a`)
- S7: [表2.6 X射线衍射仪的性能指标; Tab. 2.6 Property index of X-ray diffraction instrument](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8fc2c482-fb3b-4eb9-aecc-a4d72d63f73e/resource) (`8fc2c482-fb3b-4eb9-aecc-a4d72d63f73e`)