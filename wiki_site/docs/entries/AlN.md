---
version: "v1"
generated_at: "2026-06-18T11:06:10+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 21
  source_quality_score: 0.83
  freshness_score: 0.91
  evidence_coverage_score: 1.0
---

## 概述

在铝铜合金体系中，氮化铝（AlN）可作为**原位生成的纳米陶瓷增强相**存在。其形成途径并非外加AlN粉末，而是通过向铝铜合金熔体中引入BN（氮化硼）颗粒，使其与合金中的第二相Al₂Cu发生化合反应而原位生成[[S1,S9,S14]]。与常规粉末冶金法添加的AlN颗粒不同，该原位生成的AlN相与铝基体界面结合紧密，不存在界面杂质或润湿不良问题，可实现纳米级均匀分布[[S18]]。

该相属于**六方晶系纤锌矿型结构**，为共价键构成的类金刚石氮化物，常规热稳定温度可达2200°C[[S12]]。在铝铜合金晶界处，AlN相以晶界强化剂的形式存在，能够阻碍晶界滑移，提升材料的屈服强度与抗蠕变性能[[S9,S12]]。

## 形成机制

### 化学反应

BN颗粒与铝铜合金第二相Al₂Cu之间的化合反应是原位生成AlN的核心路径，完整的反应方程式为[[S1,S9,S14]]：

**2BN + Al₂Cu → AlN + CuN + AlB₂**

该反应同时生成三种增强化合物：AlN、CuN及AlB₂。其中AlB₂为六方结构，CuN为单斜结构[[S9]]。

### 热力学条件

第一性原理计算表明，BN在Al₂Cu(001)表面可发生稳定的化学吸附。在桥位吸附位置，BN的吸附能达到 **-7.94 eV**，吸附反应可自主进行。体系费米能级处的电子态密度分布平缓，反应产物为高稳定性共价金属化物，无明显相变趋势[[S27,S2]]。

### 动力学工艺条件

实验研究表明，使增强相均匀分布、综合力学性能最优的热处理工艺条件为[[S1,S14]]：

| 工艺参数 | 数值 |
|---------|------|
| 固溶温度 | 545°C |
| 固溶时长 | 9 h |
| 时效温度 | 150°C |
| 时效时长 | 8 h |

## 微观结构与成分

### 晶体结构

原位生成的AlN相为**六方晶系纤锌矿结构**（空间群P6₃mc），对应(200)晶面的晶面间距d=0.204 nm[[S9]]。反傅里叶变换（IFFT）图像测得的晶面间距为0.203 nm，与上述结果吻合[[S20]]。高分辨透射电镜（HRTEM）观测显示，样品中存在大量长度约**10 nm**的AlN纳米富集相[[S9]]。

> 图4-15为微纳BN改性铝铜合金的高分辨透射电镜及傅里叶变换（FFT）图，标注了AlN、CuN、AlB₂等增强相及其对应晶面间距，提供了不同反应产物物相鉴定的可视化证据[[S16]]。

![图4-15 高分辨透射电镜图及傅里叶变换（FFT）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7d352bf-c636-401e-99ef-dfbd31a30098/resource)

### 界面取向关系

AlN与铝基体界面为**并行相干**，匹配性良好。AlN-Al界面的取向关系为[[S25]]：

- **[110]Al ∥ [2110]AlN**
- **[111]Al ∥ [0112]AlN**

这种半共格或共格界面有利于有效传递应力，使BN颗粒与铝铜基质界面处表现出很强的化学键合[[S25,S9]]。

### 原子占位特征与晶界结构

在非平衡合成条件下，AlN晶格中可稳定存在**N原子替位占据Al格点的点缺陷**。第一性原理计算表明，N替位Al空位（即三价负电铝空位）在n型AlN中具有最低的形成能[[S21]]。在铝铜合金体系中，该N替位Al格点的占位现象使AlN在晶界处形成特殊的**凹陷结构**，引发AlN晶格畸变，以晶界强化剂的形式阻碍晶界滑移[[S12,S9]]。

## 强化机制

### 力学性能贡献

AlN相嵌入晶界或晶内后，引发晶体结构畸变，增加晶格的应变能，使位错运动和晶界滑移受阻，从而提升材料的屈服强度与抗蠕变性能[[S9]]。在铝基复合材料中，通用的四类强化机制均适用于原位AlN增强铝铜合金体系[[S23]]：

1. **载荷传递效应**
2. **热失配强化**
3. **晶粒细化（晶界）强化**
4. **Orowan位错绕过强化**

### 副产物的辅助作用

- **AlB₂相**：六方结构，(101)晶面间距d=0.208 nm。具有高结晶度和高原子间键合强度，可在再结晶过程中产生晶界强化效应，细化晶粒并增加晶界面积，提升硬度与耐磨性[[S9]]。
- **CuN相**：单斜结构，(-311)晶面间距d=0.202 nm。可通过固溶强化提升材料硬度；但若分布不均，易成为裂纹萌生源，增加合金脆性倾向[[S9]]。

### 高温蠕变行为

AlN增强相可有效阻碍高温下的晶界滑移，提升抗蠕变性能。在铝铜类合金中，随温度升高（从298 K到723 K，即25°C到450°C），总应变中蠕变应变占比逐步上升，弹性和塑性应变占比持续下降[[S15]]。分散均匀的纳米AlN颗粒可通过钉扎位错和晶界，提高合金在高温区的服役能力[[S12]]。

## 工艺关联

### 铸造工艺影响

不同铸造工艺对原位AlN的生成与分布有显著影响[[S22]]：

- **挤压铸造（压铸衍生工艺）**：通过高压下强制冷却获得更高的凝固冷却速率，可抑制AlN相团聚，提升分布均匀性，进一步细化原位生成的AlN平均粒径，减少合金内部孔洞缺陷，获得更高的致密性和综合力学性能[[S22]]。
- **机械搅拌铸造/复合铸造工艺**：通过机械、电磁或超声搅拌将BN颗粒均匀分散到铝铜熔体中，避免重力偏析，减少团聚，适配大批次量产需求[[S22,S17]]。

### BN颗粒添加与熔体处理

BN颗粒具有较好的化学活性和润湿性，在铝液搅拌阶段可提供更好的均质性，使N元素充分溶解于Al中，为后续AlN的析出形核创造条件[[S9]]。最终热处理工艺（固溶+时效）的合理选配对增强相的均匀分布与力学性能优化起关键作用[[S1,S14]]。

## 局限与缺点

1. **塑性与韧性降低**：高体积分数的AlN增强相在铝熔体中润湿性差、分散难度大，会显著降低铝铜合金的塑性与韧性，提升材料脆性断裂倾向[[S10,S19]]。过量生成的AlN作为硬质第二相会在基体中形成应力集中点，诱使微裂纹快速萌生扩展[[S19]]。

2. **组织稳定性**：常规铝铜合金服役温度区间内，分散均匀的AlN增强相无明显粗化行为。仅当AlN发生局部偏聚形成大尺寸团聚区时，才会出现颗粒异常长大现象[[S12]]。

3. **工艺窗口容差**：CuN相等副产物若分布不均，同样会提升合金脆性倾向[[S9]]。未引入BN/AlN增强相的常规铸造Al-Cu合金中，当残余Al₂Cu相大量聚集在晶界时，也会成为裂纹起始点，降低材料韧性[[S6]]。

当AlN体积分数控制在合理区间时，可实现强塑性协同——例如，在350°C条件下，含AlN纳米颗粒的Al-0.9Cu合金强度可达187 MPa、延伸率4.6%[[S19]]。

## 与其他增强相的对比

下表列出铝基复合材料中常见晶界增强相的核心性能参数对比[[S8]]：

| 增强相 | 密度 (g/cm³) | 硬度 (GPa) | 热膨胀系数 (10⁻⁶/°C) | 弹性模量 (1090°C, GPa) |
|--------|-------------|-----------|---------------------|----------------------|
| AlN | 3.26 | 11.8 | 4.84 | 310 |
| Al₂O₃ | 3.99 | 18~21 | 7.92 | 379 |
| TiB₂ | 4.52 | 25~35 | 6.88 | 414 |

AlN在密度和热膨胀系数方面具有优势（低密度、低膨胀系数），但在硬度与高温弹性模量方面低于Al₂O₃和TiB₂。实测高温力学性能对比显示，350°C时TiB₂增强铝基复合材料抗拉强度可达96 MPa（较基体提升8%），Al₂O₃纤维增强铝基复合材料抗拉强度可达98.7 MPa，均优于同体积分数单一AlN增强相的同类表现[[S24]]。

此外，AlN与Al₂O₃对基体晶粒粗化温度的影响亦有所不同，随铝含量提升，含AlN体系的晶粒粗化温度整体呈现与Al₂O₃体系不同的变化趋势，需要根据具体合金成分与服役温度选择匹配的增强相[[S11]]。

## 应用前景

含原位AlN增强相的铝铜合金在以下领域具有潜在应用价值：

- **压铸件**：利用挤压铸造（压铸衍生工艺）可制备致密性好、增强相分布均匀的薄壁构件，适用于对高温强度有要求的壳体类零件[[S22]]。
- **高温部件**：AlN热稳定温度高达2200°C[[S12]]，其增强的铝铜合金可在300°C以上工况保持较高强度，对于发动机活塞等高温承载部件具有开发潜力[[S17]]。

## Sources
- S1: [TextNode51](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12447520-367d-4067-bef7-b75fbc63378d/resource) (`12447520-367d-4067-bef7-b75fbc63378d`)
- S9: [TextNode53](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/758aa246-5162-494c-bcc0-871d86089e39/resource) (`758aa246-5162-494c-bcc0-871d86089e39`)
- S14: [TextNode52](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9a8a87f-ff91-4ffb-825c-6afa3b1caae7/resource) (`a9a8a87f-ff91-4ffb-825c-6afa3b1caae7`)
- S18: [国家知识产权局专利战略推进工程项目研究报告铜合金材料及深加工专利战略研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be586a5d-b8ad-4e81-a374-24bc76bf745e/resource) (`be586a5d-b8ad-4e81-a374-24bc76bf745e`)
- S12: [7498226_氮化铝](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a2e6a923-6578-417a-9181-4e9418cd2642/resource) (`a2e6a923-6578-417a-9181-4e9418cd2642`)
- S27: [微纳BN颗粒改性铝铜合金材料的多尺度模拟及其在壳体中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f68772ad-5bfc-48b2-b06c-f86823a71681/resource) (`f68772ad-5bfc-48b2-b06c-f86823a71681`)
- S2: [微纳BN颗粒改性铝铜合金材料的多尺度模拟及其在壳体中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35b0de24-1a42-440f-9bc6-863000b3af49/resource) (`35b0de24-1a42-440f-9bc6-863000b3af49`)
- S20: [AlN增强相的IFFT图像，标注平面间距0.203nm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1e73daf-5064-4a9f-8eb5-2ce39cb56105/resource) (`d1e73daf-5064-4a9f-8eb5-2ce39cb56105`)
- S16: [图4-15 高分辨透射电镜图及傅里叶变换（FFT）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7d352bf-c636-401e-99ef-dfbd31a30098/resource) (`b7d352bf-c636-401e-99ef-dfbd31a30098`)
- S25: [微纳BN颗粒改性铝铜合金材料的多尺度模拟及其在壳体中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8623f58-3002-4328-817a-60e77f539674/resource) (`e8623f58-3002-4328-817a-60e77f539674`)
- S21: [defects and diffusion in semiconductors xiv__4264e56db2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dae1055a-e182-46db-9216-ab5dabfef572/resource) (`dae1055a-e182-46db-9216-ab5dabfef572`)
- S23: [advances in corrosion control of magnesium and its alloys metal matrix composites and protective coatings__a7f032c4ca](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e44b3640-97dc-42b6-b856-b9bd29e9739f/resource) (`e44b3640-97dc-42b6-b856-b9bd29e9739f`)
- S15: [不同温度下弹性、塑性、蠕变应变分布柱状图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6f35950-8933-4392-b5ec-58dd4408a6b5/resource) (`b6f35950-8933-4392-b5ec-58dd4408a6b5`)
- S22: [微纳BN颗粒改性铝铜合金材料的多尺度模拟及其在壳体中的应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd4afaf8-0cc8-4f79-b062-b9f20afb7657/resource) (`dd4afaf8-0cc8-4f79-b062-b9f20afb7657`)
- S17: [耐热铝合金薄壁构件离心浇注数值仿真及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd8abe37-2f37-47c6-8410-e4057c67a4d6/resource) (`bd8abe37-2f37-47c6-8410-e4057c67a4d6`)
- S10: [casting and solidification of light alloys__06e9012dec](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c9ede93-5971-4bb0-bc6e-25384c931205/resource) (`9c9ede93-5971-4bb0-bc6e-25384c931205`)
- S19: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c71dad81-76ca-4dd7-9402-8dfe7d694cca/resource) (`c71dad81-76ca-4dd7-9402-8dfe7d694cca`)
- S6: [挤压铸造Al-Cu合金显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5478450b-51af-4398-a140-8c1d0ad03bb6/resource) (`5478450b-51af-4398-a140-8c1d0ad03bb6`)
- S8: [表2.1 原位增强颗粒的性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69383841-009f-4ada-8dd5-81d4fe88cbb2/resource) (`69383841-009f-4ada-8dd5-81d4fe88cbb2`)
- S24: [TiCp+TiB2p_铝基复合材料高温力学性能研究及活塞试制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6b31eb9-c973-412f-a9b4-8e39a77626f3/resource) (`e6b31eb9-c973-412f-a9b4-8e39a77626f3`)
- S11: [图17：铝对含铁碳工具钢晶粒粗化温度的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d194341-d6c1-44b1-8ffe-7a9706e0492d/resource) (`9d194341-d6c1-44b1-8ffe-7a9706e0492d`)