---
version: "v1"
generated_at: "2026-06-18T14:35:15+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 32
  source_quality_score: 0.86
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述与定义

差示扫描量热法（Differential Scanning Calorimetry, DSC）是一种在程序控温条件下，测量输入至试样与参比物的功率差（或热流差）随温度或时间变化的热分析技术[[S30,S28,S19]]。其核心在于直接获取与相变潜热和比热容变化相对应的热流信号，从而实现对材料热效应的定量表征[[S15,S4]]。在压铸铝合金、镁合金等金属材料的研究与生产中，DSC 被广泛用于相变温度、熔化焓、比热容的测定，以及热处理工艺的优化与质量控制[[S10,S24]]。

依据测量原理，DSC 可分为热流型（Heat Flux DSC, HF‑DSC）和功率补偿型（Power Compensated DSC, PC‑DSC）。热流型 DSC 将样品与参比物对称放置于高导热圆盘上，通过测量二者温差换算为热流差值；功率补偿型 DSC 则为样品和参比物分别配备独立的加热回路，通过主动调节加热功率使二者温度始终一致，直接记录输入的功率差[[S9,S8]]。

DSC 曲线以吸热方向向上（Endo Up）为常见约定：向上的峰对应熔化、固溶等吸热过程，向下的峰对应析出、结晶等放热过程；峰下的面积与试样吸收或放出的总焓值成正比，因此可直接用于定量计算相变潜热[[S15,S29]]。

> **术语说明**：国家标准与专业手册统一采用“差示扫描量热法”作为正式名称。“差热扫描量热分析”与“示差扫描量热法”属于行业内通用的合规俗称，正式文档建议优先使用规范名称[[S30,S35,S15]]。

## 仪器组成与结构

DSC 仪器的核心组件包括[[S7,S19]]：

- **加热炉**：提供程序控温环境，根据测试需求可覆盖从低温（ < 250 ℃）到超高温（可达 2400 ℃）的区间，但商用 DSC 的上限温度通常不超过铝合金的熔点（约 1200 ℃），更高温度需借助差热分析（DTA）[[S4,S6]]；
- **样品盘与参比盘**：分别盛放待测试样与惰性参比物（如纯铝或空坩埚），要求与传感器保持良好热接触[[S2]]；
- **传感器**：由热电偶或铂热敏电阻组成，用于高精度采集样品与参比侧的实时温度及热流差值[[S19,S7]]；
- **气氛控制系统**：向炉腔通入高纯氩气或氮气等保护气，防止试样氧化并稳定基线信号[[S12,S3]]。

典型热流型 DSC 的结构如图 1 所示。

![热流型 DSC 装置结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2ed08ad-8457-4146-a263-8e21c53eee05/resource)

图 1：热流型差示扫描量热装置结构示意图，样品与参比单元对称分布于高导热圆盘上，标注了炉温 Tf 及各点温度参数[[S26]]。

## 测试参数与校准

### 典型操作参数

针对金属/合金样品，常规 DSC 测试的参数范围如下[[S2,S3,S12]]：
- **升温/降温速率**：0.1 K/s 至 25 K/min（约 6 K/s 以下为常规设备，更高速率需采用快速扫描量热仪 Flash DSC）；
- **温度范围**： −120 ℃ 至 1200 ℃ 以上（视设备型号与冷却附件而定）；
- **试样质量**：10 mg 至 24 g，铝合金试样常用约 90 mg；
- **坩埚材质**：常温测试可用铝坩埚，高温测试（接近或超过铝合金熔点）须使用氧化铝陶瓷坩埚或石墨坩埚；
- **吹扫气体**：高纯氩气或氮气，推荐流量 10 ~ 50 mL/min。

### 校准与基线处理

在定量测量之前必须进行仪器校准[[S20,S5]]：
- **温度校准**：采用高纯度标准金属（如 99.999 % 铟、锌）的熔融峰进行标定；
- **热流/焓值校准**：记录标准物质（如铟）的熔化峰面积，标定仪器的热流系数，积分得到相变焓值，再根据样品质量换算为单位质量的反应焓（J/g）；
- **基线校正**：在相同程序下进行空坩埚扫描，扣除系统固有热流差；再利用二次扫描消除不可逆热效应，或采用多项式拟合扣除残余曲率，以提升基线平稳度与焓值计算准确性[[S20]]。

## 相关测试标准

适用于金属材料 DSC 测试的主要国际与中国标准包括[[S18,S1]]：
- ASTM E793：差示扫描量热法测定熔化和结晶焓值的标准测试方法；
- ASTM E794：热流型 DSC 通用操作与温度校准要求；
- ISO 11357 系列 / GB/T 19466 系列：差示扫描量热法通用测试规范，涵盖相变温度、焓值、比热容的测定。

## 在压铸中的核心应用

### 固相线与液相线温度的测定

DSC 可准确标定压铸合金的固相线（Ts）与液相线（Tl）温度，这是制定固溶处理工艺、避免过烧的直接依据。以 ADC12 压铸铝合金为例，实测 Ts = 515 ℃、Tl = 580 ℃，该结果直接用于界定其固溶温度窗口[[S34,S17]]。对于 Al‑Si 系压铸合金，典型的升温 DSC 曲线呈现两个吸热峰：低温峰对应共晶相熔化，其外推起始温度即为固相线；高温峰对应 α(Al) 相熔化，其峰值温度为液相线[[S29]]。图 2 给出了 319s 与 357 两种半固态压铸铝硅合金的升降温 DSC 曲线对比，直观反映了半固态温度区间的差异。

![319s、357半固态压铸铝硅合金升温/降温DSC曲线对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7c51448-211b-463c-bcf5-0bdfcac4c521/resource)

图 2：319s 与 357 半固态压铸铝硅合金升温与降温过程的 DSC 曲线（功率密度差），可用于判定合金的半固态温度区间[[S27]]。

部分压铸合金的实测固液相线温度见表 1。

| 合金牌号 | 固相线温度 Ts (°C) | 液相线温度 Tl (°C) | 来源 |
|----------|-------------------|-------------------|------|
| ADC12 | 515 | 580 | [[S34,S17]] |
| Cu‑7Ni‑7Al‑4Fe‑2Mn | 1050 | 1120 | [[S13]] |

表 1：两种压铸合金的固相线/液相线 DSC 实测值

### 固溶与时效过程中的相变分析

在压铸镁合金（如 AZ91、AM60）的固溶‑时效热处理中，DSC 可清晰检测 β‑Mg₁₇Al₁₂ 金属间化合物的溶解吸热峰，以及后续时效阶段亚稳态 β 相从过饱和 α‑Mg 基体中析出的放热峰，从而为优化固溶温度与时效时间提供定量依据[[S23,S21]]。类似地，在 Al‑Si‑Cu‑Mg 系压铸合金中，对比铸态、固溶态、时效态的 DSC 曲线，铸态试样通常出现明显的非平衡共晶熔化吸热峰，固溶态试样该峰消失，时效态则出现亚稳相析出的特征放热峰，可用于快速判定热处理工艺的合规性[[S24,S11]]。

### 热物性参数与模拟输入

DSC 可直接测量压铸合金的熔化焓及全温区比热容数据，这些参数可导入 ProCAST 等压铸热力学与流动模拟软件，显著提高充型、凝固及缺陷预测的精度[[S10,S37]]。实际应用中，DSC 的实测值还可用于修正 Scheil 模型等非平衡凝固计算的结果，例如 Cu‑7Ni‑7Al‑4Fe‑2Mn 合金的实测固相线（1050 ℃）比模型计算值（1008 ℃）高出约 42 ℃，说明实测数据对校准模拟输入的必要性[[S13,S25]]。

### 半固态成形与合金设计

通过 DSC 获得的液相率 − 温度曲线，可确定合金中 50 % 液相对应的温度 T₁、液相率随温度变化的斜率，以及固相开始熔化的温度 T₂ 等关键参数，这些参数是优化半固态压铸工艺和设计新型半固态合金的重要依据[[S35]]。

## 曲线解读与特征点判定

压铸合金 DSC 曲线的特征点遵循统一的判定规则[[S25,S20]]：
- **起始点（Onset）**：外推基线与吸热峰左侧最大斜率切线的交点；
- **峰值温度（Peak）**：热流信号的极值点；
- **终止点（Endset）**：热流曲线返回基线处。

峰面积与焓变的换算步骤为：先用高纯标准样标定热流系数，再对相变峰区间的热流信号积分，得到总热量 Q；Q 除以试样质量即得该反应的焓变（ΔH，J/g）[[S5,S20]]。

## 局限性及注意事项

DSC 在压铸合金测试中存在以下局限性：
- **加热/冷却速率的影响**：提高升降温速率会使相变峰向高温方向偏移，同时可能造成邻近峰的叠加，降低分辨率；过低速率则降低灵敏度[[S2,S4]]；
- **样品氧化**：若保护气纯度不足或流量不当，高温下合金表面生成的 Al₂O₃ 等氧化膜会改变热传导路径，干扰热流信号，导致相变温度和焓值偏差[[S12]]；
- **动力学滞后**：压铸合金快速凝固形成非平衡组织，其相变温度与其平衡相图理论值存在固有滞后，且升温速率越高，滞后越明显[[S4]]；
- **多相合金的峰重叠**：如 Al‑Mg‑Si 系压铸合金（6061 等）在 DSC 曲线上可出现多达 8 个特征峰，分别对应 GP 区、β″、β′、β 相的溶解/析出及游离 Si 析出，多个峰相互叠加，显著增加了解析难度[[S16]]；
- **组织不均匀性**：压铸快速凝固产生的第二相尺寸分布极宽，不同尺寸粒子的溶解/析出温度区间差异大，致使 DSC 峰显著宽化、基线漂移，引入系统误差[[S24]]。

## 与其他热分析技术的关系

差示扫描量热法（DSC）、差热分析（DTA）和热重分析（TGA）是三种常见的热分析技术，其核心区别为[[S15,S4,S22]]：
- **DTA**：测量样品与参比物之间的温差（ΔT）随温度/时间的变化，ΔT 信号与焓变仅存在间接关系，基线漂移较大，定量校核复杂；
- **DSC**：直接测量功率差/热流差，可获得绝对焓值，基线稳定性和灵敏度显著优于 DTA，能够精准识别压铸合金中少量低熔点相的非平衡熔化峰，并直接计算焓变和比热容；
- **TGA**：监测样品质量随温度的变化，仅适用于伴随质量增减的过程，完全不能检测压铸合金中不发生质量变化的相变，如熔化/凝固、固溶/析出等，因此不适用于合金相变温度测试。

在压铸合金的热表征中，DSC 凭借其定量性、灵敏度和直接输出焓值的能力，成为成分优化与热处理工艺开发的首选方法[[S10]]。值得注意的是，商用 DSC 设备的最高测试温度通常不超过铝合金的熔点（约 1200 ℃），而 DTA 的测试上限可达 1500 ℃，对于更高温度的铜合金等体系需结合 DTA 使用[[S6]]。

## Sources
- S30: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d460ecfc-2ce3-4193-91c0-ef576259c999/resource) (`d460ecfc-2ce3-4193-91c0-ef576259c999`)
- S28: [pvdf膜表面改性及其在水处理中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5fd7c01-f429-42da-b63e-a2f4ce2f7f9e/resource) (`c5fd7c01-f429-42da-b63e-a2f4ce2f7f9e`)
- S19: [10451127_差式扫描量热仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f5b0222-a588-4c20-9c09-c61ecb0293b5/resource) (`8f5b0222-a588-4c20-9c09-c61ecb0293b5`)
- S15: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bb76973-e525-4988-9e33-c212c97d10d7/resource) (`6bb76973-e525-4988-9e33-c212c97d10d7`)
- S4: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ef79a61-549d-45ae-b5a5-8966783697c8/resource) (`0ef79a61-549d-45ae-b5a5-8966783697c8`)
- S10: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45e92267-9b70-48e8-9ad0-ea85d194a573/resource) (`45e92267-9b70-48e8-9ad0-ea85d194a573`)
- S24: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b067ebd3-1726-4dd1-9cac-d14e269b3ca0/resource) (`b067ebd3-1726-4dd1-9cac-d14e269b3ca0`)
- S9: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41c73b2f-2252-4b65-9394-d876ecc300fe/resource) (`41c73b2f-2252-4b65-9394-d876ecc300fe`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37de08f4-c48c-4249-864f-ee8b83a46bc8/resource) (`37de08f4-c48c-4249-864f-ee8b83a46bc8`)
- S29: [两种常用免热处理压铸铝合金的对比研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc09f6ef-ddff-4d18-9c30-46956a4b3dc2/resource) (`cc09f6ef-ddff-4d18-9c30-46956a4b3dc2`)
- S35: [金属半固态成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea61c309-923b-4475-9943-7a1cda20bbf7/resource) (`ea61c309-923b-4475-9943-7a1cda20bbf7`)
- S7: [铝合金热轧及热连轧技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cdeea19-abdc-4063-a23b-64027ed631fc/resource) (`2cdeea19-abdc-4063-a23b-64027ed631fc`)
- S6: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a89c5a4-33b9-47b2-8bc5-a26696e1fb34/resource) (`2a89c5a4-33b9-47b2-8bc5-a26696e1fb34`)
- S2: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0575b25a-36fe-492e-94be-5d1a64e20e7c/resource) (`0575b25a-36fe-492e-94be-5d1a64e20e7c`)
- S12: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c4c77fd-83cb-4c5e-9628-3cce43a94170/resource) (`5c4c77fd-83cb-4c5e-9628-3cce43a94170`)
- S3: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0afcee01-a84c-4d9b-834e-973ec0ddc959/resource) (`0afcee01-a84c-4d9b-834e-973ec0ddc959`)
- S26: [差示扫描量热法（DSC）装置示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2ed08ad-8457-4146-a263-8e21c53eee05/resource) (`b2ed08ad-8457-4146-a263-8e21c53eee05`)
- S20: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94c9887f-a6c5-4042-9dce-64fba4664aee/resource) (`94c9887f-a6c5-4042-9dce-64fba4664aee`)
- S5: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1614f23a-20a7-4d82-bf97-a3056cf45261/resource) (`1614f23a-20a7-4d82-bf97-a3056cf45261`)
- S18: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89e014b0-8c7b-49c1-9cd9-1c45ec0ab23a/resource) (`89e014b0-8c7b-49c1-9cd9-1c45ec0ab23a`)
- S1: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/003604b0-5ba5-4973-ad30-a5bc98049281/resource) (`003604b0-5ba5-4973-ad30-a5bc98049281`)
- S34: [effects of die temperature of sss die casting on the microstructure and__d27a8b10b6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e90e96bb-9aef-4d33-ad46-645d0916debf/resource) (`e90e96bb-9aef-4d33-ad46-645d0916debf`)
- S17: [effects of die temperature of sss die casting on the microstructure and__d27a8b10b6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75a97bcc-de43-4a17-ab9a-4b13197ddfd3/resource) (`75a97bcc-de43-4a17-ab9a-4b13197ddfd3`)
- S27: [图2.1 319s铝合金、357铝合金在升温降温过程中的吸热放热曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7c51448-211b-463c-bcf5-0bdfcac4c521/resource) (`b7c51448-211b-463c-bcf5-0bdfcac4c521`)
- S13: [表3-2 合金固液相线实验测量值与计算值的比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68432f2d-ef29-448c-aa02-d9bef49f238b/resource) (`68432f2d-ef29-448c-aa02-d9bef49f238b`)
- S23: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9310e91-8e28-40c6-a7a3-64f04001cc93/resource) (`a9310e91-8e28-40c6-a7a3-64f04001cc93`)
- S21: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5556f20-1e29-4a36-bc94-b1b02a0d7869/resource) (`a5556f20-1e29-4a36-bc94-b1b02a0d7869`)
- S11: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/596cd4c3-043d-4449-8a7f-3fa39b5dc9a6/resource) (`596cd4c3-043d-4449-8a7f-3fa39b5dc9a6`)
- S37: [一体压铸用免热处理铝合金自主研发及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb6be324-5b4d-4719-b2d0-33ec2e532fcc/resource) (`fb6be324-5b4d-4719-b2d0-33ec2e532fcc`)
- S25: [铜镍铝合金通海阀铸造缺陷预测及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b13ae393-8f91-400b-97e1-2e84ca03c077/resource) (`b13ae393-8f91-400b-97e1-2e84ca03c077`)
- S16: [Al-Mg-Si 和 Al-Si-Mg 合金 DSC 曲线峰值与析出/溶解反应对应关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71c85972-b233-4369-b18f-886d94f71598/resource) (`71c85972-b233-4369-b18f-886d94f71598`)
- S22: [adhesive bonding of aluminum alloys__3de44d7277](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a66c6627-c253-4b62-8a92-53c1a05d4c37/resource) (`a66c6627-c253-4b62-8a92-53c1a05d4c37`)