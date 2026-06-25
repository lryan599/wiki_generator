---
version: "v1"
generated_at: "2026-06-21T05:50:35+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 17
  source_quality_score: 0.87
  freshness_score: 0.76
  evidence_coverage_score: 1.0
---

GP-II 区是 Al-Zn-Mg(-Cu) 系铝合金（如 7000 系）时效早期形成的一种盘状 Guinier-Preston 区亚类，属于完全共格的预脱溶原子偏聚区。它在铝基体的 {111} 惯习面上析出，仅几个原子层厚，并带有明显的长径比 [[S4,S22]]。该区是 η' 亚稳相的主要前驱体，在过饱和固溶体 → GP-I 区 → GP-II 区 → η' → η (MgZn₂) 的标准析出序列中处于第二共格阶段，因此文献中常将其标记为 G·P₂ 或 η'' 相，也可称为空位富集团簇 [[S6,S11]]。GP-II 区的形成必须依赖高温淬火（≥450 ℃）所保留的过饱和空位，并随后在 70 ℃ 以上进行时效，其本质是由富 Mg 的 GP‑I 区演化而来的富 Zn 偏聚区 [[S4,S22,S25]]。

## 晶体学特征
- **惯习面与取向**：在 Al-Zn-Mg 合金中，GP‑II 区沿基体的 {111}Al 面析出，典型的观察带轴为 [110]Al [[S22,S5]]。
- **尺寸与形貌**：厚度为几个原子层，呈盘状/片状并带有长径比。在经微量纳米颗粒调控后的 7 系合金 T73 状态下，GP‑II 区的平均尺寸约为 4.5 nm [[S25]]。
- **共格与畸变**：GP‑II 区与铝基体保持完全共格，但在界面附近会引起可观测的局部晶格畸变，这一特征可通过高分辨透射电镜（HRTEM）及其反傅里叶变换（IFFT）图像清晰分辨 [[S22,S5]]。

![沿[110]Al晶带轴观察的Al-Zn-Mg合金GP-II区高分辨透射电镜图像及对应逆傅里叶变换图，红色三角指示GP-II区引发的晶格畸变位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42d0bcb0-7bfa-4b7b-be56-e23d36288a15/resource)

## 形成条件与析出序列
GP‑II 区的析出需要两个必要条件：固溶淬火温度高于 450 ℃，以保证基体中保留足够的过饱和空位；后续人工时效温度需高于 70 ℃ [[S4,S22]]。它不能直接从过饱和固溶体中析出，而是由先在 {100}Al 面析出的富 Mg GP‑I 区演化而来 [[S22,S4]]。

完整的时效析出序列为 [[S9,S18,S11]]：
```
过饱和固溶体 → GP‑I 区 → GP‑II 区 → η' 亚稳相 → 平衡 η 相 (MgZn₂)
```
这一序列中，GP‑II 区的临界转变/溶解温度约为 435 K（约 162 ℃）；超过该温度后，GP‑II 区将直接向 η' 相转变或完全溶入基体 [[S19,S10]]。

## 强化机制
GP‑II 区对合金强度的贡献十分突出。当 GP‑II 区单独存在于基体中时，可通过**共格应变强化**和**位错切过机制**提高屈服强度，对应的额外屈服强度增量可达约 7 kg/mm²（约 68.6 MPa）[[S24,S8]]。由于 GP‑II 区非常细小，位错可直接切过粒子，在实现高强度提升的同时保留较好的塑性。一旦尺寸粗化或转变为半共格的 η' 相，强化机制逐渐变为 Orowan 位错绕过机制，所提供的强度增量将低于 GP‑II 区 [[S24,S22]]。

## 与 GP‑I 区的对比
| 特性 | GP‑I 区 | GP‑II 区 |
|------|---------|----------|
| 形貌 | 近似圆形/球形，尺寸 1~2 nm [[S4]] | 薄片状/盘状，带有长径比 [[S4,S22]] |
| 惯习面 | 基体 {100} 面 [[S4]] | 基体 {111} 面 [[S4,S22]] |
| 成分 | 富 Mg 偏聚区 [[S22]] | 富 Zn 偏聚区 [[S22,S25]] |
| 形成温度区间 | 室温至 150 ℃，不依赖淬火温度 [[S4]] | 需 ≥450 ℃ 淬火后，≥70 ℃ 时效 [[S4,S22]] |
| 共格与畸变 | 完全共格，无明显晶格畸变 [[S22]] | 完全共格，伴随可观测的晶格畸变 [[S22,S5]] |

## 对压铸工艺的适应性
压铸工艺极快的冷却速率可获得比普通铸造更高浓度的过饱和空位，这为 GP‑II 区的均匀形核提供了有利条件 [[S13]]。通过**两段时效**（100~110 ℃ 低温预时效 + 150~160 ℃ 时效）可在压铸 Al‑Zn‑Mg 合金中生成高密度且分布均匀的 GP‑II 区，同时减小晶界无析出区（PFZ）的宽度 [[S13,S22]]。国产 ZL 系列 Al‑Zn 系压铸合金（如 ZL401）在适配的压铸快冷 + 时效工艺下亦能析出 GP‑II 区，实现组织强化 [[S20]]。此外，配合 -50~-70 ℃、2~3 h 的冷处理及冷热循环时效，可进一步稳定 GP‑II 组态、降低残余应力，从而大幅提升精密压铸件的长期尺寸稳定性 [[S23,S17]]。

## 热稳定性与过时效
GP‑II 区的热稳定性存在明确阈值：当时效温度超过约 120 ℃ 且保温时间超过临界时长后，GP‑II 区会逐步溶解、粗化，并向半共格的 η' 亚稳相转变，最终完全丧失共格，导致合金进入过时效状态，强度明显下降 [[S15,S6,S13]]。

## 等义术语
GP‑II 区的中英文等义名称包括：GP2 区、GPII 区、Guinier‑Preston II 区、G·P₂（η'' 相）以及空位富集团簇 [[S6,S11]]。

## Sources
- S4: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ba7154d-77c2-4fa6-af0b-348b375a3bbc/resource) (`3ba7154d-77c2-4fa6-af0b-348b375a3bbc`)
- S22: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1f458a3-2b4b-4ab4-809d-99d9c20556a7/resource) (`d1f458a3-2b4b-4ab4-809d-99d9c20556a7`)
- S6: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f469917-acc3-445e-b87d-4943e690056f/resource) (`4f469917-acc3-445e-b87d-4943e690056f`)
- S11: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7d354c94-0fef-4c0c-8668-9bcc74f67d4d/resource) (`7d354c94-0fef-4c0c-8668-9bcc74f67d4d`)
- S25: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part02_p200-254](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f87b01ef-8ca2-4249-a7c3-68d850babb2f/resource) (`f87b01ef-8ca2-4249-a7c3-68d850babb2f`)
- S5: [图4.14 (b) 调控后7系铝合金型材中GP-II区的HRTEM照片及IFFT图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42d0bcb0-7bfa-4b7b-be56-e23d36288a15/resource) (`42d0bcb0-7bfa-4b7b-be56-e23d36288a15`)
- S9: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e893bc9-5dfa-488a-846b-a8697b89c9b0/resource) (`6e893bc9-5dfa-488a-846b-a8697b89c9b0`)
- S18: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be593f60-b040-4271-a2e5-9c9c737b47a1/resource) (`be593f60-b040-4271-a2e5-9c9c737b47a1`)
- S19: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb39f4d1-d93f-40dd-a1d4-e5b2969723a0/resource) (`cb39f4d1-d93f-40dd-a1d4-e5b2969723a0`)
- S10: [aluminum alloys structure and properties__ce35257e2f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f8aaf36-1277-4bb8-a4e0-e41e2065b053/resource) (`6f8aaf36-1277-4bb8-a4e0-e41e2065b053`)
- S24: [elements of mechanical metallurgy__32226e152e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e97ca89a-31f0-4ce3-9bd9-d3de60fcaab8/resource) (`e97ca89a-31f0-4ce3-9bd9-d3de60fcaab8`)
- S8: [elements of mechanical metallurgy__32226e152e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63db03b7-b139-432a-a6dc-d67e6c3cbe02/resource) (`63db03b7-b139-432a-a6dc-d67e6c3cbe02`)
- S13: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8daa0511-ff51-48e5-a504-9773e984da87/resource) (`8daa0511-ff51-48e5-a504-9773e984da87`)
- S20: [中国航空材料手册第3卷铝合金镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd405dcd-de1b-4dc4-aa49-f31f2a4e6ff6/resource) (`cd405dcd-de1b-4dc4-aa49-f31f2a4e6ff6`)
- S23: [材料延寿与可持续发展铝合金选用与设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3ea6909-db98-4e67-a75f-9bef4c7455bd/resource) (`e3ea6909-db98-4e67-a75f-9bef4c7455bd`)
- S17: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae77e217-0b11-4b68-a2fd-754c46b3e6d6/resource) (`ae77e217-0b11-4b68-a2fd-754c46b3e6d6`)
- S15: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5424a2b-e8a5-4e4f-8b01-dfe4017e9c7c/resource) (`a5424a2b-e8a5-4e4f-8b01-dfe4017e9c7c`)