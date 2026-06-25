---
version: "v1"
generated_at: "2026-06-19T09:23:08+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 45
  source_quality_score: 0.88
  freshness_score: 0.75
  evidence_coverage_score: 1.0
---

## 概述

型砂pH值，在国家标准GB/T 5611-2017中明确定义为“型砂的沸水滤液的pH值”，是控制型砂性能的重要指标[[S49,S27]]。在压铸工艺中，虽然金属模具是主要成型方式，但当压铸件内部存在复杂腔体时，常需使用砂芯来成形——此时型砂（尤其是芯砂）的pH值对铸件质量具有不可忽视的影响。型砂pH值本质上反映了砂-粘结剂-水混合体系中可溶于水的酸性或碱性物质所表现出的氢离子浓度，pH=7为中性，pH<7为酸性，pH>7为碱性[[S9,S10]]。

## 测量方法与标准

### 国内标准方法

**沸水提取法**：称取50g已烘干的型砂试样置于150mL烧杯中，注入100mL蒸馏水加热至沸腾，搅拌10min，冷却沉淀后过滤，取滤液用pH计测定[[S22,S27]]。该方法是GB/T 5611-2017规定的标准参考方法。

**常温悬浮液法**：先用标准缓冲溶液标定pH计，称取25g±0.1g烘干型砂试样置于200mL烧杯，加入100mL蒸馏水，磁力搅拌器搅拌5min，停止搅拌后将电极插入上清液测定pH，每30s读取一次数值直至读数稳定不变，每次读数后需将电极浸入干净蒸馏水中清洗[[S16,S37]]。

### AFS方法

取25g待测型砂置于烧杯，加入100mL蒸馏水进行振荡/搅拌提取，待pH计读数稳定后完成测定[[S9]]。

### 现场快速检测

生产现场可采用精密pH试纸法直接测定型砂浸出液的pH值，操作简便但检测精度低于实验室pH计测定法，适用于生产工况的快速巡检[[S40]]。

### 测量注意事项

测试前需使用对应pH区间的缓冲溶液标定仪器；避免使用暴露在空气中吸收了过量CO₂导致酸化的蒸馏水；pH电极需定期维护，长期闲置时建议将电极浸泡在蒸馏水中保存[[S9]]。常见测量误差来源包括：普通蒸馏水存放过程中吸收大气CO₂导致测试水本身pH下降，以及pH电极长期使用未维护导致内部KCl电解液泄漏失效[[S10]]。

> **图** 铸造用型砂酸耗值测定标准操作流程。酸耗值是独立于pH值的另一关联检测指标，两者无直接相关性，但常配套用于评价原砂碱性物质含量[[S14]]。
>
> ![铸造用型砂酸耗值测定标准操作流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25988b58-309b-469c-b991-ddcdc3dc6b54/resource)

## 分类体系与推荐范围

### 膨润土分类

根据行业标准JB/T 9227-1999，铸造用膨润土按pH值分为酸性（S型）和碱性（J型）两类[[S23,S39]]。天然钠基膨润土自然pH为8~10（弱碱性），天然钙基膨润土自然pH为6~7（弱酸性）[[S20,S23]]。

### 不同粘结剂体系的pH特征

| 粘结剂体系 | 典型pH区间 | 特征说明 |
|-----------|-----------|---------|
| 钙基膨润土（天然） | 6~7 | 弱酸性[[S23]] |
| 钠基膨润土（天然） | 8~10 | 弱碱性[[S23]] |
| 呋喃树脂（酸自硬） | 6.5~7.5（储存期） | pH过低树脂快速变稠，缩短储存期[[S32]] |
| 酸自硬体系（通用） | <2~4（硬化过程） | 强酸硫酸单酯pH<2，弱酸磷酸pH≈3~4[[S24]] |
| 碱性酚醛树脂 | 12~14 | 强碱性，用液态有机酯固化[[S42,S46]] |
| CO₂硬化钠水玻璃 | 12~13（初始） | 吹CO₂后pH持续降低至8~9时强度峰值[[S51,S57]] |
| 硅溶胶 | 8.5~10（稳定区间） | 超出该范围硅溶胶易胶凝，存放稳定性下降[[S55]] |
| 铝镁合金型砂（JB2755） | 4.5~6.5 | 低发气性、适配轻合金铸造[[S4]] |

## 对型砂性能的影响

### 膨润土体系

钠基膨润土砂的热湿拉强度、干压强度显著高于钙基膨润土砂，钙基膨润土砂的透气性优于钠基膨润土砂。天然状态下钠基膨润土pH更高，高温强度更高，但溃散性相对更差[[S54,S48]]。

钙基膨润土活化处理时，用碳酸钠作为活化剂，体系pH从6.5逐步上升至9.0区间时，钙基向钠基的转化效率最高，对应型砂湿压强度、热湿拉强度达到峰值；当pH超过9.5后，体系中游离碱含量过高，会显著提升铸件气孔缺陷的发生概率[[S54,S35,S21]]。

> **图** 含8%膨润土的型砂，不同含水量下干压强度与湿压强度的变化规律。该曲线反映了含水量与膨润土水化程度对强度的耦合影响，而pH值通过控制膨润土活化程度间接影响这一关系[[S56,S36]]。
>
> ![8%膨润土型砂干压强度与湿压强度随含水量变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7761e81-a9bc-4e4d-bdc7-8bacdfeca894/resource)

### 树脂砂体系

酸自硬呋喃树脂的理想储存pH区间为6.5~7.5，若pH过低树脂在存放过程中会快速变稠，大幅缩短储存期[[S32]]。在呋喃树脂酸自硬体系中，体系pH值越低（酸性越强），固化反应速度越快，但终强度越低：强酸硫酸单酯对应体系pH<2，固化速度最快但终强度最低；弱酸磷酸对应体系pH≈3~4，固化速度最慢，起模时间可达180min，但终强度最高[[S24,S19,S29]]。

当原砂碱度较高时，添加的酸性固化剂会与碱性物质中和生成盐和水，额外增加体系总含水量，进一步稀释砂粒表面的固化剂浓度与粘结剂浓度，延缓硬化速率、降低最终型砂强度[[S15]]。

铸造用自硬碱性酚醛树脂的pH控制区间为12~14，呈强碱性，采用液态有机酯作为固化剂，游离酚和游离甲醛含量低，旧砂回用性能优异[[S42,S46]]。

### 水玻璃砂体系

未反应的CO₂硬化钠水玻璃初始体系pH为12~13，通入CO₂后碳酸与硅酸钠发生反应，体系pH持续降低；当pH降至8~9区间时，硅酸凝胶生成量最高，此时硬化后砂型的即时强度达到峰值；若过度吹入CO₂导致体系pH低于7，大量生成碳酸氢钠结晶，砂型存放过程中强度不升反降[[S51,S57]]。水玻璃模数越高，同等固含量下体系pH略低，残留强度第二峰值会向更高温度区间后移，砂型高温溃散性显著提升，落砂难度降低[[S38,S47,S41]]。

## 在压铸砂芯中的作用

### pH值与砂芯质量控制

砂芯pH值的标准检测定义为砂芯的沸水滤液pH值，是控制砂芯综合性能的核心工艺指标。当砂芯pH值小于7呈酸性时，易诱发铸件夹砂结疤类缺陷，该规律可迁移至压铸砂芯场景用于砂芯基础性能管控[[S1,S27]]。

### 不同粘结剂体系的压铸砂芯推荐pH

| 粘结剂体系 | 适配铸件材质 | 推荐控制pH值 |
|-----------|------------|------------|
| 酚醛尿烷砂 | 灰铁类压铸件 | 8[[S52]] |
| 呋喃树脂砂 | 铝/铜合金压铸件 | 6[[S52]] |
| 树脂覆膜砂 | 多材质压铸件 | 8[[S52]] |
| CO₂法水玻璃砂 | 多材质压铸件 | 11[[S52]] |

### 金属-砂芯界面反应

酸性砂芯会破坏部分碱性砂芯粘结体系的表面惰性层，在压铸高速高压充射下更易促使金属氧化物与砂粒发生反应生成高附着力的硅酸铁类物质，提升化学粘砂风险；碱性较强的砂芯（如高pH水玻璃砂）在压铸充型高温下若表面涂层破损，更易发生砂粒向金属液内部渗透的机械粘砂[[S34,S11,S50]]。

### 气孔缺陷影响

砂芯pH值异常偏酸时，易加速酸性固化剂残留分解，提升砂芯内部残存可反应水分占比，在压铸高温金属液作用下，水与金属铝发生反应生成大量氢原子并在界面富集，最终诱发压铸件皮下反应性气孔；当砂芯pH值过高呈强碱性时，易加大砂芯发气速率，在压铸高压环境下提升侵入性气孔生成概率[[S26,S18,S6]]。

### 脱芯性能

适配压铸场景的酚醛树脂覆膜砂芯常规pH控制在8左右，其树脂粘结体系在压铸充型完成后经过510℃保温30min的热处理工艺即可完全软化，实现无残留清砂脱芯，获得内腔光洁无粘砂的压铸件，避免后续焊接加工过程中出现鼓泡缺陷[[S8,S28]]。

## 调控方法与添加剂

工业上常用的型砂pH调节剂包括两类：提升pH的碱性添加剂以碳酸钠为代表，添加占膨润土质量3%~5%可实现钙基膨润土活化，调整体系碱度[[S44]]；降低pH的酸性调节剂覆盖不同强度的磺酸（对甲苯磺酸、二甲苯磺酸等）和磷酸，作为呋喃树脂自硬砂的固化剂，控制酸硬化反应速率[[S44,S24]]。

## 与其他参数的关联

型砂pH值和它的需酸量（酸耗值）是性质完全不同的两个独立指标，两者无直接关联。例如部分砂样实测pH显示偏酸性，但其需酸量仍然处于较高水平，不能通过pH值直接推导砂样的总碱性杂质含量[[S10]]。

型砂体系的pH值与环境温度呈负相关，随温度升高pH值逐步下降，温度是现场pH控制精度的重要干扰变量[[S43]]。

## 常见误区与局限性

片面严格控制pH在极窄范围难以稳定实现。例如在熔模铸造硬化体系中，目标pH 5~6的控制区间无法长期维持，正常硬化作业后体系pH会快速回升至7附近，过度追求该指标会额外增加操作成本，无实际生产意义[[S58]]。pH测量过程中，普通蒸馏水存放过程吸收CO₂导致的酸化、pH电极维护不当等因素均为常见误差来源[[S10]]。

## Sources
- S49: [GBT+5611（铸造术语）-2017.pdf-dd5ce1f8-c5b9-4d94-87e7-fc40cbfe0347](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4c7a7e4-00f0-4b81-a861-d39fa03eff02/resource) (`d4c7a7e4-00f0-4b81-a861-d39fa03eff02`)
- S27: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5dffb8a9-ba48-460b-92e3-67cce2a5a06d/resource) (`5dffb8a9-ba48-460b-92e3-67cce2a5a06d`)
- S9: [造型材料试验手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d1390c3-940a-466a-8b35-c694f5005f7c/resource) (`1d1390c3-940a-466a-8b35-c694f5005f7c`)
- S10: [造型材料试验手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d34bb84-9f14-4947-82b3-607b41ad662c/resource) (`1d34bb84-9f14-4947-82b3-607b41ad662c`)
- S22: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42b3105d-8fbf-432d-9cb4-bb5d332c9d8f/resource) (`42b3105d-8fbf-432d-9cb4-bb5d332c9d8f`)
- S16: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2753c335-89e3-4b1d-955d-eb86d7dc2508/resource) (`2753c335-89e3-4b1d-955d-eb86d7dc2508`)
- S37: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/981117d1-a7bb-4b25-b400-d203131dae8b/resource) (`981117d1-a7bb-4b25-b400-d203131dae8b`)
- S40: [低压及差压铸造理论与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a60928bb-3f68-436e-8ea5-9870ed3cd264/resource) (`a60928bb-3f68-436e-8ea5-9870ed3cd264`)
- S14: [图3-4酸耗值实验步骤; Fig. 3-4 Acid Consumption Test Steps](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25988b58-309b-469c-b991-ddcdc3dc6b54/resource) (`25988b58-309b-469c-b991-ddcdc3dc6b54`)
- S23: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49e7d3f3-2766-4bbe-ad73-33a0723e13d8/resource) (`49e7d3f3-2766-4bbe-ad73-33a0723e13d8`)
- S39: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e0b9802-299d-4795-8323-4e2f47eabaf7/resource) (`9e0b9802-299d-4795-8323-4e2f47eabaf7`)
- S20: [最新铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/332c068e-0b9c-4b52-8f39-4ee4fc9460f4/resource) (`332c068e-0b9c-4b52-8f39-4ee4fc9460f4`)
- S32: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81597c2a-b9de-405c-91bc-87da4ec0be57/resource) (`81597c2a-b9de-405c-91bc-87da4ec0be57`)
- S24: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4be231b3-c043-4794-a617-0438e354ea7a/resource) (`4be231b3-c043-4794-a617-0438e354ea7a`)
- S42: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a99a8c8b-6dc0-4a58-bfb2-731fd36362d4/resource) (`a99a8c8b-6dc0-4a58-bfb2-731fd36362d4`)
- S46: [GBT+5611（铸造术语）-2017.pdf-dd5ce1f8-c5b9-4d94-87e7-fc40cbfe0347](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ca957a23-c44f-4b84-a780-cf25059f622c/resource) (`ca957a23-c44f-4b84-a780-cf25059f622c`)
- S51: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db32c993-e50b-4392-8eda-eb528a7dc5ac/resource) (`db32c993-e50b-4392-8eda-eb528a7dc5ac`)
- S57: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbba3fb6-07b3-4905-ad50-3d4b90ada192/resource) (`fbba3fb6-07b3-4905-ad50-3d4b90ada192`)
- S55: [消失模铸造及实型铸造技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6d88892-b7be-41c5-bf72-79806029017f/resource) (`f6d88892-b7be-41c5-bf72-79806029017f`)
- S4: [表 10.22 型（芯）砂的技术要求](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ac831c6-39ee-401a-b3e1-fb76a9b0f0f6/resource) (`0ac831c6-39ee-401a-b3e1-fb76a9b0f0f6`)
- S54: [金属材料液态成型工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f278be7a-180f-4b8d-be12-275274457dcf/resource) (`f278be7a-180f-4b8d-be12-275274457dcf`)
- S48: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3be903c-39c1-4b90-bd64-3bd1145b0ad2/resource) (`d3be903c-39c1-4b90-bd64-3bd1145b0ad2`)
- S35: [金属材料液态成型实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ff3a2b3-6aca-4260-8a17-7503cb14e127/resource) (`8ff3a2b3-6aca-4260-8a17-7503cb14e127`)
- S21: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39935c3b-f396-49d2-af95-9549e1ab4249/resource) (`39935c3b-f396-49d2-af95-9549e1ab4249`)
- S56: [8%膨润土型砂干压与湿压强度关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7761e81-a9bc-4e4d-bdc7-8bacdfeca894/resource) (`f7761e81-a9bc-4e4d-bdc7-8bacdfeca894`)
- S36: [含8%膨润土的型砂干压强度与湿压强度随含水量及紧实度变化的关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ff56f3a-c0a2-40b4-b712-c9d651333928/resource) (`8ff56f3a-c0a2-40b4-b712-c9d651333928`)
- S19: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/321d6459-578a-4a0b-a1fe-d11dbd1b3ce5/resource) (`321d6459-578a-4a0b-a1fe-d11dbd1b3ce5`)
- S29: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76639f15-6428-4521-883f-210f68cfb2fd/resource) (`76639f15-6428-4521-883f-210f68cfb2fd`)
- S15: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26689995-0a2e-4c8c-a155-b4e11fe49bf2/resource) (`26689995-0a2e-4c8c-a155-b4e11fe49bf2`)
- S38: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/999486c8-fac8-4899-8e45-9f89bbc0083a/resource) (`999486c8-fac8-4899-8e45-9f89bbc0083a`)
- S47: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d137126e-7299-4a09-80fd-729940a05d6f/resource) (`d137126e-7299-4a09-80fd-729940a05d6f`)
- S41: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a79c5357-9c41-4a38-95ae-84c1204c2192/resource) (`a79c5357-9c41-4a38-95ae-84c1204c2192`)
- S1: [GBT+5611（铸造术语）-2017.pdf-dd5ce1f8-c5b9-4d94-87e7-fc40cbfe0347](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07129215-daa7-402a-a128-dab438a0337d/resource) (`07129215-daa7-402a-a128-dab438a0337d`)
- S52: [再生砂质量控制指标表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2a1c81c-d0e3-4113-af71-e029fb6d415a/resource) (`e2a1c81c-d0e3-4113-af71-e029fb6d415a`)
- S34: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f32c7a5-a9ab-41c9-a5fc-7a72942727fd/resource) (`8f32c7a5-a9ab-41c9-a5fc-7a72942727fd`)
- S11: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/229e1936-8bd4-4f4b-87fc-789b0a004fa6/resource) (`229e1936-8bd4-4f4b-87fc-789b0a004fa6`)
- S50: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5230520-8c61-44de-8a51-b889e9d57fa8/resource) (`d5230520-8c61-44de-8a51-b889e9d57fa8`)
- S26: [金属型重力铸造铝合金缸盖的“皮下气孔”研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/576cbbeb-bf47-49a4-85cd-01c212b6505a/resource) (`576cbbeb-bf47-49a4-85cd-01c212b6505a`)
- S18: [金属型重力铸造铝合金缸盖的“皮下气孔”研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31fe475f-23cc-48ed-a931-61873942e6f8/resource) (`31fe475f-23cc-48ed-a931-61873942e6f8`)
- S6: [气缸体气孔缺陷产生原因及预防措施](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16817ce6-40b7-405f-9889-079e8125cd08/resource) (`16817ce6-40b7-405f-9889-079e8125cd08`)
- S8: [基于匀加速料筒孕育半固态压铸制备薄壁复杂空腔手模的研究与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b812fcf-85d7-454f-9a53-71c1bd8ae973/resource) (`1b812fcf-85d7-454f-9a53-71c1bd8ae973`)
- S28: [压力铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/637113ec-9a1d-46ae-bd93-04d678a3a144/resource) (`637113ec-9a1d-46ae-bd93-04d678a3a144`)
- S44: [机械工程手册试用本第39篇铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb334f7a-5907-4f3f-92ed-2c423926b550/resource) (`bb334f7a-5907-4f3f-92ed-2c423926b550`)
- S43: [硬化液温度与pH关系曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8d9cb5d-0b30-4407-bf09-fcbff018447d/resource) (`b8d9cb5d-0b30-4407-bf09-fcbff018447d`)
- S58: [熔模铸造 论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff924666-82c1-49bb-8af9-c787449ae3b6/resource) (`ff924666-82c1-49bb-8af9-c787449ae3b6`)