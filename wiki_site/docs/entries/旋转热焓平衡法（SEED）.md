---
version: "v1"
generated_at: "2026-06-18T13:45:19+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 13
  source_quality_score: 0.83
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

旋转热焓平衡法，英文全称为 Swirl Enthalpy Equilibration Device，缩写为 SEED，是一种借助热焓控制直接在金属熔体冷却凝固过程中制备半固态浆料的工艺方法 [[S9,S1,S8]]。该方法由加拿大铝业公司（STAS）提出并完成商业化推广 [[S9]]，其核心思想是通过坩埚偏心旋转产生的剪切力与热平衡协同作用，使初生相在无搅拌构件直接接触的条件下实现球化，从而获得适用于流变成形或触变成形的半固态浆料。

## 分类地位

在众多半固态流变制浆工艺中，SEED 法属于“形核 + 搅拌剪切法”的范畴 [[S4]]。与纯枝晶破碎类的机械搅拌法和电磁搅拌法不同，该法首先通过熔体与坩埚之间的激冷实现快速形核（形核长大控制），再借助坩埚旋转施加低强度剪切（搅拌剪切），促进初生相球化长大。其工艺路线与纯低过热度浇注促进形核的 SSR（Semi-Solid Rheocasting）法、无主动剪切的 NRC（New Rheocasting）法以及双螺杆强剪切的 RDC（Rheo-Diecasting）法均有明显差异 [[S4]]。SEED 法无侵入式搅拌部件，可有效避免二次污染，提高浆料的纯净度 [[S10,S8]]。

## 核心工艺原理与操作流程

SEED 法制备半固态浆料主要分为三个阶段 [[S9,S10,S8,S2,S6]]：

1. **倾斜浇注与激冷形核**  
   将具有指定初始温度的金属熔体倾斜倒入圆柱形金属坩埚。坩埚吸收熔体热量，使熔体温度迅速下降，初生相开始形核并逐渐长大。

2. **旋转热平衡与球化**  
   将坩埚垂直摆正后，以设定转速进行偏心旋转。旋转产生的离心力在合金内部施加剪切应力，使浆料整体温度逐步均匀，初生相在剪切力作用下完成球化长大。

3. **排液提高固相率**  
   旋转达到指定时长后静置 5~10 s，通过排出坩埚底部部分液相，获得固相率在 **0.3~0.6** 区间内的半固态浆料。

![SEED半固态浆料全工艺流程（含直接对接高压压铸环节）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f58f183-bd4b-4709-8b9f-b8471e6362e6/resource)

图：SEED 半固态浆料全工艺流程，依次展示倾斜浇注、旋流、排液、脱模转移及高压压铸五个步骤 [[S3]]。

## 工艺参数

SEED 工艺的关键控制参数包括浇注温度、坩埚温度、旋转频率以及浆料压铸温度等。以 ZGK521 合金（Mg-5Zn-xGd-0.6Zr 系）半固态流变压铸为例，典型工艺参数如下表所示 [[S11]]。

| 参数名称 | 数值 | 单位 |
|---|---|---|
| SEED 浇注温度 | 730 | ℃ |
| SEED 旋转频率 | 45 | Hz |
| SEED 坩埚温度 | 450 | ℃ |
| 浆料压铸温度 | 600 | ℃ |
| 压铸机压射速度 | 4.0 | m/s |
| 压铸机模具温度 | 275 | ℃ |
| 增压压力 | 100 | MPa |

通过调整浇注温度、旋转速度与旋转时间，可以调控所制得半固态浆料的微观组织形态 [[S9]]。

## 设备与结构特征

SEED 制浆设备主要由制浆坩埚、控制仪表及操作部件组成 [[S5]]。图 1 展示了量产型 SEED 装置的基本结构，其整体设计简洁，便于集成到自动化生产线中，具有设备简易、浆料输送方便、操作过程易实现自动化的特点 [[S10]]。

![商用SEED半固态制浆设备实物图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e77bcdd-bf1b-4cda-ad31-0e7cd8d418b8/resource)

图：铝硅合金半固态制备用旋转热焓平衡法制浆设备实物，可见制浆坩埚及控制仪表 [[S5]]。

## 适用合金与应用

SEED 法适用于多种合金体系。在铝合金方面，可用于 A201、A356/357、319s 等铸造铝合金的半固态制浆 [[S13,S7]]；在镁合金方面，已成功应用于 Mg-Zn-Gd-Zr 系（如 ZGK521）合金的流变压铸 [[S11,S10]]。该方法的另一优势在于可用于半固态温度区间较窄的合金浆料制备 [[S8]]。

SEED 法可直接与高压压铸（HPDC）产线对接，实现从半固态浆料制备到压铸成形的连续生产 [[S3]]。

## 优势与局限

**主要优势**  
- 无搅拌构件直接接触金属熔体，避免二次污染，提高浆料纯净度 [[S10,S8]]。  
- 设备简易、浆料输送方便、操作流程易实现自动化 [[S10]]。  
- 温度控制相对简单，适用于半固态温度区间窄的合金 [[S8,S10]]。

**主要局限**  
- 操作流程较繁琐 [[S8]]。  
- 浆料成分的精确控制难度较高 [[S8]]。

## 演变与发展

SEED 工艺的起源可追溯至 2002 年由 D. Doutre、G. Hay、P. Wales 等人提交的美国专利 US7140419 B2 [[S1]]。2004 年，S. Nafisi、R. Ghomashchi、A. Charette 以及 J. Langlais 等在第 66 届世界铸造大会上发表了题为《Effects of Grain Refining on Morphological Evolution of Al-7%Si in the Swirled Enthalpy Equilibration Device (SEED)》的论文，完成了该方法的早期学术公开 [[S1,S12]]。此后，Cote P、Larouche M E 与 Chen X G 于 2013 年在 *Solid State Phenomena* 期刊发表了《New Developments with the SEED Technology》，介绍了 SEED 技术的后续改进与发展 [[S13]]。

## Sources
- S9: [357铝合金半固态浆料在流变压铸过程中流动行为的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d26c51e-32d5-4f85-af0c-7b8a6bd116b1/resource) (`8d26c51e-32d5-4f85-af0c-7b8a6bd116b1`)
- S1: [倾转-振动法制备半固态浆料及微观组织的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03b869e6-bdd6-4a1f-a06b-1938d0546387/resource) (`03b869e6-bdd6-4a1f-a06b-1938d0546387`)
- S8: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84a84f83-b161-4c93-a43a-497bd3687134/resource) (`84a84f83-b161-4c93-a43a-497bd3687134`)
- S4: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/273aaddc-9797-4162-8a03-e400f76ffd88/resource) (`273aaddc-9797-4162-8a03-e400f76ffd88`)
- S10: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea3a1a52-5dfe-4764-b6ca-055963f61654/resource) (`ea3a1a52-5dfe-4764-b6ca-055963f61654`)
- S2: [SEED（旋转焓平衡）制备半固态浆料工艺流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c2b2403-ebcc-424f-9264-ec28a01d245b/resource) (`1c2b2403-ebcc-424f-9264-ec28a01d245b`)
- S6: [SEED（旋转焓平衡）法制备半固态浆料工艺流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61c8512f-a617-4ce0-976e-44e80ce9d05a/resource) (`61c8512f-a617-4ce0-976e-44e80ce9d05a`)
- S3: [图2.3 SEED浆料制备工艺示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f58f183-bd4b-4709-8b9f-b8471e6362e6/resource) (`1f58f183-bd4b-4709-8b9f-b8471e6362e6`)
- S11: [表4.3 半固态压铸参数; Tab. 4.3 Process parameters of SSM die casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f77ba487-f13f-4152-abf3-7fde2f263427/resource) (`f77ba487-f13f-4152-abf3-7fde2f263427`)
- S5: [图2.8 流变制浆设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e77bcdd-bf1b-4cda-ad31-0e7cd8d418b8/resource) (`3e77bcdd-bf1b-4cda-ad31-0e7cd8d418b8`)
- S13: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa19e8ee-9fc3-4f25-baf7-e3884a031fdb/resource) (`fa19e8ee-9fc3-4f25-baf7-e3884a031fdb`)
- S7: [表1.2 常见的铝合金半固态金属降温制备方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6580acd4-2f8c-417f-85be-c1b77ad27e28/resource) (`6580acd4-2f8c-417f-85be-c1b77ad27e28`)
- S12: [铝合金铸锻一体化装备及工艺开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9dd9042-f067-42bb-8e38-f370ee91579a/resource) (`f9dd9042-f067-42bb-8e38-f370ee91579a`)