---
version: "v1"
generated_at: "2026-06-18T09:13:01+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 31
  source_quality_score: 0.87
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述

在免热处理压铸铝合金领域中，“C”即指碳元素杂质，而非碳当量或其他代号[[S4]]。碳属于非金属夹杂物，主要由熔炼、再生料回用及压铸过程带入，即便微量也会显著劣化合金塑性，免热处理高韧性合金对其含量有极为严格的内控要求[[S4,S18]]。

## 存在形式与分类

碳在铝熔体中几乎不以间隙固溶态存在，而是优先与铝反应生成硬脆碳化物相 $Al_4C_3$ ，属于典型的非金属夹杂物[[S2]]。工业精炼可将碳含量降至 ppm 级[[S34]]。$Al_4C_3$ 颗粒尺寸多分布在 0.1 ~ 5 μm，呈六角形或圆盘状，常以孤立的团簇形式出现，也易与 $Al_2O_3$、硼化物等结合成复合夹杂[[S2]]。

此外，当熔体中存在钛元素时，碳可与钛反应生成 TiC 硬质相。TiC 可作为铝液凝固的非自发形核核心，起到细化晶粒的作用，微量碳在特定条件下存在“化害为利”的可能[[S23]]。

## 碳在铝中的溶解度与反应

碳在铝基体中的溶解度极低：
- 在 1000 ~ 1100 ℃ 基本不溶解[[S3,S31]]；
- 在 1300 ~ 1500 ℃ 时液态铝中溶解度估算 < 0.05 wt%[[S31]]；
- 固态铝中最大固溶量约为 0.015 wt%[[S3,S15]]。

过量的碳在铝熔体中主要以游离碳质点和 $Al_4C_3$ 的形式存在，反应为：

$$
4Al(l) + 3C \rightarrow Al_4C_3(s)
$$

$Al_4C_3$ 在水或水蒸气环境下会发生分解，导致铸件表面麻点缺陷[[S34]]。

## 碳杂质的来源

碳进入铝熔体的途径多样，主要涵盖以下环节[[S2,S6,S12,S23]]：

- **电解原铝带入**：石墨阳极机械破损脱落炭粒，或局部过热直接生成 $Al_4C_3$；
- **再生铝及回炉料**：含油污的有机物在高温下分解引入碳；
- **熔炼与压铸工具**：石墨坩埚、石墨搅拌叶轮等与熔体直接接触；
- **压铸柱塞润滑**：柱塞运动所用润滑油高温裂解，与铝反应生成碳化物；
- **燃料不完全燃烧**：天然气、油料等碳氢化合物分解产物进入熔体；
- **SiC 工装**：无保护层的 SiC 工具与铝液反应生成 $Al_4C_3$。

## 对塑性及力学性能的影响

### 硬脆相割裂基体

常规压铸温度下碳在铝中溶解度仅约 0.015 %，大部分以游离碳或 $Al_4C_3$ 相形式悬浮于基体，割裂基体连续性，显著降低延伸率和冲击韧性[[S15,S25]]。$Al_4C_3$ 本身塑性几乎为零，会严重阻碍基体塑性变形[[S34]]。

![碳的质量分数对力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/889602b8-1c0d-4f55-847a-85dc5e39267e/resource)  
**图 1 碳的质量分数对金属力学性能影响的通用规律**  
硬度和抗拉强度随碳含量先升后降，而塑性和冲击韧度持续下降。该规律可类比说明 $Al_4C_3$ 相比例增大时铝合金塑性的持续劣化趋势[[S17]]。

### 临界控制阈值

针对免热处理高塑性压铸铝合金（如 AlSi10MnMg），行业公认的内控临界阈值为 **碳质量分数 ≤ 0.01%**。当碳含量超过该值后，合金延伸率可从 10 % 以上大幅降至 6 % 以下，完全丧失高塑性服役特性[[S18]]。

### 与其他杂质相的协同劣化

碳杂质与 Al‑Fe‑Si 系硬脆相（如 $\alpha$-Fe₃SiAl₁₂、$\beta$-Fe₂Si₂Al₉）之间存在协同效应。两者同时大量存在时，共同形成更多复合硬脆质点，裂纹萌生概率急剧增大，对延伸率和韧性的负面作用远超单一杂质的影响叠加[[S13,S10]]。

炭质夹杂物、$Al_4C_3$ 与氢及 $Al_2O_3$ 夹杂亦存在共生恶化效应：当碳杂质含量升高时，熔体中氢的溶解度同步提高；在相同氢含量条件下，更高的碳/夹杂含量使铸锭针孔率大幅上升，且常规除气除渣难度显著增大，最终共同降低铸件致密性与力学性能[[S19]]。

## 检测方法

| 检测方法 | 特点 | 适用范围 | 参考标准 |
|---------|------|---------|---------|
| 直读光谱分析法 | 速度快、无需复杂前处理，适合炉前快速批量检测 | 压铸车间常规元素在线管控 | 工厂内部作业指导书[[S11,S9]] |
| 红外吸收燃烧法 | 高精度定量，可测固态试样总碳含量 | 炉后最终成分校验，检测范围 0.005 %~ 0.30 % | ASTM E1941‑10 系列[[S28,S22]] |
| 火花检验（定性） | 通过火花形态初步估测碳含量，简易快速 | 现场粗判，需与仪器校准配合使用 | — [[S32]] |

## 工艺控制手段

工业上脱除和控制铝熔体中碳杂质的主要成熟工艺包括[[S14,S21,S24,S7]]：

1. **惰性气体旋转喷吹**：利用 Ar/N₂ 微气泡吸附悬浮的游离碳粒和 $Al_4C_3$ 质点，随气泡上浮至液面变为浮渣去除；
2. **泡沫陶瓷过滤**：在浇道系统中设置过滤板，拦截大尺寸碳质夹杂物；
3. **源头原料管控**：严格限制高碳回炉料加入比例，避免高温下烃类燃烧产物与铝液反应增碳；
4. **工具与辅料清洁**：保持熔炼及压铸工具干燥、无油污，选用有保护层的坩埚和搅拌装置。

![铝合金锭实物图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d441f549-5096-4068-83a1-7b165f950482/resource)  
**图 2 压铸铝合金原材料铝合金锭实物形态**  
原生铝锭中的碳杂质初始水平，直接关系到后续免热处理合金能否满足高塑性要求，是源头管控的第一道关口[[S30]]。

## 标准与限值

现行主流压铸铝合金标准中，均 **未对碳元素设置独立的强制限量**：
- GB/T 15115‑2024（中国）
- ASTM B85（美国）
- EN 1706（欧洲，原 EN AC 系列）
- JIS H5302（日本）

碳被归入通用残余杂质范畴，残余杂质总允许上限通常为质量分数 **≤ 0.15 %**[[S8,S33]]。免热处理高塑性合金的内控标准远严于此值，实际生产中需依靠企业标准或客户技术协议进行更严格的管理[[S18]]。

## 在一体化压铸免热处理部件中的应用

新能源汽车大型一体化压铸件（如后地板、前舱等）要求铸态下即可获得高延伸率和高韧性，对碳杂质尤为敏感。典型免热处理压铸铝合金牌号及其应用包括[[S1,S20,S27,S29]]：
- 特斯拉 Model Y 一体化后地板用自主研发免热处理合金；
- 美铝 EZCAST 系列 C611；
- 德国莱茵菲尔德 Castasil‑37；
- 立中集团、广东鸿图等国内自主牌号。

上述合金均通过严格控制碳含量、避免硬脆碳化物析出，保障在无需热处理的条件下满足汽车车身碰撞安全对塑性和韧性的要求。

## Sources
- S4: [457137_碳](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3202af46-e4a9-4549-b151-4f9cc22c1175/resource) (`3202af46-e4a9-4549-b151-4f9cc22c1175`)
- S18: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cce15c9-13d6-4bc3-a83e-75c736157c17/resource) (`8cce15c9-13d6-4bc3-a83e-75c736157c17`)
- S2: [制冷管铝材中典型夹杂物形成机制及其腐蚀行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/052c2c58-041c-40a0-bcd6-47a358cdec20/resource) (`052c2c58-041c-40a0-bcd6-47a358cdec20`)
- S34: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb713ca6-34fd-4f88-9344-a57d868cb0ba/resource) (`eb713ca6-34fd-4f88-9344-a57d868cb0ba`)
- S23: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f63bb6b-43e6-4f67-b0bc-cce7b880a72c/resource) (`9f63bb6b-43e6-4f67-b0bc-cce7b880a72c`)
- S3: [变形铝合金的细化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1775ac6f-c400-4d77-9f67-a7b8cc2cb737/resource) (`1775ac6f-c400-4d77-9f67-a7b8cc2cb737`)
- S31: [constitution of binary alloys__494ae46018](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dee983b8-76bd-4bcc-9701-8954fc6a1fb9/resource) (`dee983b8-76bd-4bcc-9701-8954fc6a1fb9`)
- S15: [变形铝合金的细化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/742ab96e-ad28-4301-b7eb-3a33b90b6ef5/resource) (`742ab96e-ad28-4301-b7eb-3a33b90b6ef5`)
- S6: [铝及铝合金连续铸轧带坯生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34e2aeef-6f66-48fc-91e2-96de9a629fdc/resource) (`34e2aeef-6f66-48fc-91e2-96de9a629fdc`)
- S12: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/558503c3-43f5-4a3e-99e5-b4082da2fcf5/resource) (`558503c3-43f5-4a3e-99e5-b4082da2fcf5`)
- S25: [铝及铝合金的熔炼与铸锭](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad44e494-5d3b-46ba-8dee-6caefede01ae/resource) (`ad44e494-5d3b-46ba-8dee-6caefede01ae`)
- S17: [图2-34 碳的质量分数对钢力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/889602b8-1c0d-4f55-847a-85dc5e39267e/resource) (`889602b8-1c0d-4f55-847a-85dc5e39267e`)
- S13: [变形铝合金金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/614b50dc-fd58-4fcd-ad3d-0055c8bfde92/resource) (`614b50dc-fd58-4fcd-ad3d-0055c8bfde92`)
- S10: [铝合金热处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cf25dbd-0abb-4367-9e4d-064e92711a67/resource) (`4cf25dbd-0abb-4367-9e4d-064e92711a67`)
- S19: [铝合金熔炼理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e7863a3-5610-4cab-aadf-60dda1d5eb35/resource) (`8e7863a3-5610-4cab-aadf-60dda1d5eb35`)
- S11: [原铝及其合金的熔铸生产问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4dd9fa2f-ae9e-41dc-bd87-4e8a75a14ee1/resource) (`4dd9fa2f-ae9e-41dc-bd87-4e8a75a14ee1`)
- S9: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/443ee54c-0cb7-4eb1-92b8-4453796154f6/resource) (`443ee54c-0cb7-4eb1-92b8-4453796154f6`)
- S28: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/caa0fb24-15a4-4db3-9e5a-f4a7b0b58834/resource) (`caa0fb24-15a4-4db3-9e5a-f4a7b0b58834`)
- S22: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9898173a-402f-40f9-9900-9650c4a2c6bb/resource) (`9898173a-402f-40f9-9900-9650c4a2c6bb`)
- S32: [含碳0.10%左右的火花形态](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1d0e346-c844-4c60-bda5-070e977a79eb/resource) (`e1d0e346-c844-4c60-bda5-070e977a79eb`)
- S14: [铝及铝合金的熔炼与铸锭](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62e3bfd8-427c-42c0-b9c5-e6c4243b9b8d/resource) (`62e3bfd8-427c-42c0-b9c5-e6c4243b9b8d`)
- S21: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92dc5b0d-1dfb-4feb-b5f6-54cbeb73388d/resource) (`92dc5b0d-1dfb-4feb-b5f6-54cbeb73388d`)
- S24: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8fb7cf1-a7be-4b3d-a8d2-50c5344e2599/resource) (`a8fb7cf1-a7be-4b3d-a8d2-50c5344e2599`)
- S7: [aluminum recycling__799280468c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39268486-4868-486e-a548-46def6cfcd4a/resource) (`39268486-4868-486e-a548-46def6cfcd4a`)
- S30: [铝合金锭实物图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d441f549-5096-4068-83a1-7b165f950482/resource) (`d441f549-5096-4068-83a1-7b165f950482`)
- S8: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ed805b5-2ea0-42e3-a291-d5267ecc34fa/resource) (`3ed805b5-2ea0-42e3-a291-d5267ecc34fa`)
- S33: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e42a0f72-0ab5-4ca7-bc1e-68024d6fdd49/resource) (`e42a0f72-0ab5-4ca7-bc1e-68024d6fdd49`)
- S1: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/007fb056-27aa-42a5-8f73-c308a2a9ec14/resource) (`007fb056-27aa-42a5-8f73-c308a2a9ec14`)
- S20: [一体化压铸免热处理铝合金研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9034930d-7153-462b-b9f1-c65ff2cc7b64/resource) (`9034930d-7153-462b-b9f1-c65ff2cc7b64`)
- S27: [免热处理压铸Al-9Si合金成分与工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c259ac37-1c48-4946-a19d-50d1a2bde588/resource) (`c259ac37-1c48-4946-a19d-50d1a2bde588`)
- S29: [免热处理压铸Al-9Si合金成分与工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce144ac9-a4ec-4e15-8004-09eb28d2337c/resource) (`ce144ac9-a4ec-4e15-8004-09eb28d2337c`)