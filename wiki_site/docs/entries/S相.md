---
version: "v1"
generated_at: "2026-06-18T13:01:24+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.86
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述与定义

S相是Al-Cu-Mg系（2×××系）铝合金中的核心三元强化相，标准化学式为Al₂CuMg，在铝合金相体系中通常直接称为S相（或称S（Al₂CuMg）相）。该术语仅在铝合金语境下使用，需与铁基、镍基等其他合金体系中同名S相明确区分[[S16,S27,S43]]。

在工业化与学术文献中，实际有诸多表述将处于半共格状态的亚稳S'相也简称为“S相”，引发长期的术语混用现象，例如在航空2024铝合金的公开性能资料中其主要强化相常被直接表述为S相而非S'相[[S44,S24]]。

## 化学成分与晶体结构

S相的精确化学计量比为Al₂CuMg，理想晶胞内含8个铝原子、4个铜原子、4个镁原子，对应质量占比约为Al 44.4 wt.%、Cu 32.1 wt.%、Mg 23.5 wt.%[[S14,S10]]。

S相属于面心正交结构，空间群Cmcm，标准晶格常数a=0.400 nm、b=0.923 nm、c=0.714 nm。该相与铝基体保持如下取向关系：\[100\]ₛ∥\[100\]_Al，\[010\]ₛ∥\[021\]_Al，\[001\]ₛ∥\[012\]_Al[[S14,S20,S31]]。

S'相在化学成分上与S相完全一致，为维持沿\[100\]ₛ、\[001\]ₛ方向与Al基体间近乎为零的错配度，其晶格常数为a=0.400 nm、b=0.905 nm、c=0.724 nm，两者仅能通过\[010\]ₛ方向的半共格错配度差异进行辨识[[S20,S31]]。

进一步地，S''相（亦称为GPB2相）为正交或单斜晶系的完全共格过渡结构，其点阵常数处于a=0.400–0.405 nm、b=0.905–0.925 nm、c=0.718–0.724 nm范围内。下表整理了S系列三相的晶体结构与晶格参数[[S31]]：

| 相 | 晶体结构 | a (nm) | b (nm) | c (nm) | 与铝基体的典型取向关系 |
|----|---------|--------|--------|--------|----------------------|
| S″ (GPB2) | 正交或单斜 | 0.400–0.405 | 0.905–0.925 | 0.718–0.724 | (100)_p∥(210)_Al；\[010\]_p∥\[120\]_Al<br>(011)_p∥(031)_Al；\[100\]_p∥\[100\]_Al |
| S′ | 正交 | 0.400–0.404 | 0.923–0.925 | 0.714–0.717 | 有多种取向关系变体，如(121)_p∥(001)_Al等 |
| S | 正交 | 0.401 | 0.935 | 0.715 | — |

作为物相鉴定参考，2024铝合金的X射线衍射图谱中可明确识别Al基体与Al₂CuMg相的特征衍射峰[[S4]]。

![2024铝合金X射线衍射图谱，标注Al与Al₂CuMg相衍射峰](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/092ad19d-f3c9-41c7-b5f2-2180a74c4797/resource)

## 析出序列

在Cu/Mg原子比大于2的Al-Cu-Mg合金中，自500–505 ℃固溶并淬火形成过饱和固溶体后，完整的时效析出序列为：过饱和固溶体 → GPB区（Cu、Mg原子在{100}_Al及{210}_Al面上偏聚）→ 共格S″相（GPB2）→ 半共格S′相 → 平衡S相。该序列是亚稳过渡相逐步向热力学平衡相演变的连续过程[[S37,S28,S3]]。

Al-Cu-Mg三元合金相图表明，当Cu/Mg质量比处于约1.5–4区间时，S相即为合金的支配性平衡相，归属于α+S两相区或α+CuAl₂+S三相区[[S12,S37]]。

2024型合金的时效TTT图（时间—温度—转变图）清晰给出了GPB系列相（S″、S′、S）各自对应的析出温度窗口与硬度响应阶段[[S19]]。

![2024型Al-Cu-Mg铝合金时效的TTT图，标示GPB区及S系列相析出区间](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b9b5026-ea63-4d67-8e0d-0647d6d3ff4a/resource)

### S′相与S相的同一性争议

主流共识倾向于将S″、S′与平衡S相视为同一种Al₂CuMg晶体结构的不同应变耦合状态：三者晶格高度相似，仅因与铝基体的共格/半共格程度不同而存在不同程度的晶格畸变，时效过程中相变是伴随晶格连续旋转与剪切的渐变演化，不存在突变形貌相界面[[S37]]。

然而多项基于高分辨电镜的研究提出了异议，认为S′相是独立的半共格亚稳相异构，平衡S相完全失去与铝基体间的共格关系，属于热力学稳定相；仅当S′继续长大并彻底失去共格后，才最终转化为平衡S相[[S42,S28]]。

工程文献与工业手册仍大量存在将S′直接等同于S相的混用，实践中通常不必对二者刻意区分。

## 力学行为与强化机制

常规服役应变水平下，S′（Al₂CuMg）相是不可剪切析出相。移动位错无法直接切过S′相颗粒，而采用交叉滑移进行Orowan绕过机制：位错在外加切应力作用下弯曲，当曲率半径R达到两相邻S′颗粒间距λ的1/2时，位错即可绕过并留下位错环，其临界切应力由τ=Gb/λ决定。这意味着在给定体积分数下，S′相越细小弥散、颗粒间距λ越小，位错绕过所需的外力越大，合金屈服强度随之显著提高[[S41,S34,S21]]。

时效强化曲线同样呈现位错机制的转变规律：随析出相粒子半径增大，强化机制从位错剪切（可切割小尺寸共格相）转变为Orowan绕过（对应长大至临界尺寸的不可剪切相）[[S13]]。

![剪切机制与Orowan绕过机制强度随析出相半径变化的交叉曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4489c236-c7bc-4fb4-a577-6ed2f72c7faa/resource)

190 ℃人工时效T6态Al-Cu-Mg合金中，密集弥散的S′相板条对位错产生强烈阻碍，使合金屈服应力远高于自然时效状态，是2024铝合金的主要强化来源[[S36]]。

只有在极高真应变（>1.7%）的极端塑性变形条件下，粗大S′相板条才经历局部位错剪切，表现为其断裂与破碎[[S1]]。

## 形态控制及其对疲劳裂纹扩展速率的影响

在低合金化（如1.5% Cu、0.7% Mg）成分条件下，S′相以沿Al基体\[100\]方向、在{100}_Al面上排列的棒状形态析出，自由长大时相互聚集形成细长条状棒束团聚体[[S37]]。

当未对析出相尺寸进行细化调控时，长度方向粗化的不可剪切S′相会在疲劳循环中导致位错在其周围不断积塞，造成持续的不可逆加工硬化，诱发相与基体界面脱粘，导致疲劳裂纹扩展速率异常升高，并在断口上表现为大尺度疲劳台阶、撕裂脊与更宽间距的疲劳辉纹[[S5]]。

引入微量TiC-TiB₂双相纳米颗粒对T6态2024铝合金进行微观组织靶向调控后，可实现S′相的显著细化并使分布更为均匀。这一细化通过两种路径降低疲劳裂纹扩展速率：

1. 细化且均匀分布的S′相大幅增加了疲劳裂纹扩展路径的曲折程度，促使裂纹在相/基体界面处反复偏折、钝化，消耗更多扩展能量[[S8]]。
2. 与此同时，形成“可剪切共格纳米富Cu团簇+细化不可剪切S′相”共析出的双峰析出结构，有效平衡了加载过程中的应力分布，减少了疲劳损伤累积[[S5,S7,S15,S23]]。

在相同循环周次1×10⁷条件下跟踪测试表明，经纳米颗粒调控、S′相细化后的2024铝合金，其在第二个位错增殖阶段的位错密度增长速率明显低于未调控合金，证实细化S′相延缓了服役过程中的位错过度累积、降低了裂纹扩展驱动力[[S2]]。

细化S′相对于高温（200 ℃）疲劳性能同样具有积极作用：细化S′相在高温下更稳定，延缓了服役过程中的析出相粗化，保持了对裂纹扩展的阻碍效果[[S30]]。

![可剪切与不可剪切析出相在疲劳应力循环中裂纹尖端位错运动与损伤累积对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0aecb18-ec87-46e1-95c3-b88d8ae685c3/resource)

![1×10⁷循环周次下未调控与S′相细化2024铝合金的位错密度演变曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0785339b-e303-4ab1-af01-60c70417e441/resource)

## 在压铸领域的关联与参考意义

Al-Si-Cu-Mg系压铸铝合金中，当化学成分匹配时可生成S（Al₂CuMg）相作为额外强化相，该相已收录于铝合金常规金相相类型库[[S39,S6]]。

针对压铸Al-5.5Mg-0.7Mn合金的试验研究证实，Cu元素的加入可诱导沿晶界分布的Al₂CuMg相析出，其数量与尺寸随Cu含量增大同步上升；当Cu质量分数达到1.5%时，断裂面附近开裂的Al₂CuMg相比例可达约69%，成为导致压铸件延伸率大幅下降的核心诱因[[S9]]。

因此，对于压铸用含Cu、Mg合金的设计与后处理，可参考S相的析出调控策略：
- 从成分设计角度，可类比S相的Cu/Mg比阈值（S相中Cu/Mg原子比为2.61），合理调整Cu、Mg添加比例，在压铸快冷带来的高固溶强化基础上预留弥散S相的生成区间，避免形成过多粗大、连续的沿晶界S相割裂基体、恶化韧性[[S22,S10,S25]]。
- 从热处理工艺角度，可参照铸造Al-Si-Cu-Mg系合金采用的T6方案（固溶+淬火+分级时效），使S相以弥散纳米形态分布于铝基体，在提升强度的同时保留合理的塑性。典型参考工艺区间可选为500 ℃左右固溶保温2 h、180 ℃左右时效保温数小时[[S17,S29]]。

在2195铝锂合金铸件X射线衍射谱中，已实际检测到Al₂CuMg相的衍射峰，证明含Cu/Mg的铸造铝合金在适当条件下确实存在S相析出的可行性[[S35]]。

## Sources
- S16: [变形铝合金及其模锻成形技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a3e033a-ba32-4de3-8c12-ce6ceed51752/resource) (`6a3e033a-ba32-4de3-8c12-ce6ceed51752`)
- S27: [铝合金镁合金表面强化技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c26ad9ea-4d25-498c-95eb-e6144feda0a0/resource) (`c26ad9ea-4d25-498c-95eb-e6144feda0a0`)
- S43: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5537c70-629f-4236-acd2-c265937b06ee/resource) (`f5537c70-629f-4236-acd2-c265937b06ee`)
- S44: [aluminium lithium alloys iii proceedings of the third international aluminium lithium conference__658fc7f1f6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f804cb04-0c93-4448-94e8-bfad13e4a7e3/resource) (`f804cb04-0c93-4448-94e8-bfad13e4a7e3`)
- S24: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a55ed804-7eab-4df4-a636-fdfa33048225/resource) (`a55ed804-7eab-4df4-a636-fdfa33048225`)
- S14: [a handbook of lattice spacings and structures of metals and alloys__0d6d7e6946](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/448e90a4-d898-4c79-9898-4b688766d9ce/resource) (`448e90a4-d898-4c79-9898-4b688766d9ce`)
- S10: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38472852-5de5-4fde-afab-3481c39ee720/resource) (`38472852-5de5-4fde-afab-3481c39ee720`)
- S20: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9438db1f-2a4b-4300-adbd-a6517b6d8c76/resource) (`9438db1f-2a4b-4300-adbd-a6517b6d8c76`)
- S31: [Al-Al₂CuMg合金S系列沉淀相的晶体结构与晶格参数等信息](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cabf95f2-6661-428f-8e77-2e77e639299d/resource) (`cabf95f2-6661-428f-8e77-2e77e639299d`)
- S4: [2024铝合金的X射线衍射图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/092ad19d-f3c9-41c7-b5f2-2180a74c4797/resource) (`092ad19d-f3c9-41c7-b5f2-2180a74c4797`)
- S37: [TextNode1517](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d88affc2-e759-4c5f-bf4c-0f7d0d10873c/resource) (`d88affc2-e759-4c5f-bf4c-0f7d0d10873c`)
- S28: [典型航空铝合金塑性成形与蠕变时效成形的工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3b63bea-5c13-4cdd-ac63-da464e8f865d/resource) (`c3b63bea-5c13-4cdd-ac63-da464e8f865d`)
- S3: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08051426-cb01-4e7a-a6a9-a508197dca2c/resource) (`08051426-cb01-4e7a-a6a9-a508197dca2c`)
- S12: [图3-93 Al-Cu-Mg三元系凝固后相区分布图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4128757f-57c0-48dc-a895-68758478d8d6/resource) (`4128757f-57c0-48dc-a895-68758478d8d6`)
- S19: [2024型铝合金时效的TTT图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b9b5026-ea63-4d67-8e0d-0647d6d3ff4a/resource) (`7b9b5026-ea63-4d67-8e0d-0647d6d3ff4a`)
- S42: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efbb1ca0-c813-4049-86c8-a916c67caa0f/resource) (`efbb1ca0-c813-4049-86c8-a916c67caa0f`)
- S41: [熔模铸造2195铝锂合金微观组织及热处理工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea3af507-25f3-4e3a-b7c5-19c4a6fabc19/resource) (`ea3af507-25f3-4e3a-b7c5-19c4a6fabc19`)
- S34: [金属热塑性成形基础理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1ec9c12-016f-499f-a093-54d3e4043d4c/resource) (`d1ec9c12-016f-499f-a093-54d3e4043d4c`)
- S21: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b307cbd-5ec6-4d86-8f2e-b6aacd715f0d/resource) (`9b307cbd-5ec6-4d86-8f2e-b6aacd715f0d`)
- S13: [时效强化中剪切与绕过机制的强度随析出相粒子半径变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4489c236-c7bc-4fb4-a577-6ed2f72c7faa/resource) (`4489c236-c7bc-4fb4-a577-6ed2f72c7faa`)
- S36: [结构钢与铝合金塑性变形的微观机制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d56adb86-bed7-4c97-a49f-b8d1e94ec9bf/resource) (`d56adb86-bed7-4c97-a49f-b8d1e94ec9bf`)
- S1: [结构钢与铝合金塑性变形的微观机制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/071c573d-1cfc-4bea-8be7-68708a3bc6b3/resource) (`071c573d-1cfc-4bea-8be7-68708a3bc6b3`)
- S5: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/108cccff-8c80-4d47-b50c-885a2893f3ed/resource) (`108cccff-8c80-4d47-b50c-885a2893f3ed`)
- S8: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28d01056-9062-4408-a1f2-35eebb0dc763/resource) (`28d01056-9062-4408-a1f2-35eebb0dc763`)
- S7: [TextNode169](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/258da682-4bf4-4ee2-9190-162a913a31bd/resource) (`258da682-4bf4-4ee2-9190-162a913a31bd`)
- S15: [TextNode172](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/679aedbc-7d57-4fc2-ae3b-469506db36b6/resource) (`679aedbc-7d57-4fc2-ae3b-469506db36b6`)
- S23: [TextNode173](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f14541b-abd7-4f90-bd87-1f919814d394/resource) (`9f14541b-abd7-4f90-bd87-1f919814d394`)
- S2: [图5.13(b) 相同循环次数(1×10⁷)下不同疲劳试验阶段未调控和调控合金的位错密度演变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0785339b-e303-4ab1-af01-60c70417e441/resource) (`0785339b-e303-4ab1-af01-60c70417e441`)
- S30: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4b5e263-fc6c-44b9-b897-994eddf714ee/resource) (`c4b5e263-fc6c-44b9-b897-994eddf714ee`)
- S39: [简明铝合金手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db5c09c7-2f37-4592-9611-c1d803b9f9ab/resource) (`db5c09c7-2f37-4592-9611-c1d803b9f9ab`)
- S6: [工程材料及热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/226f1b60-d122-4c61-a6a3-15cc35bbdd10/resource) (`226f1b60-d122-4c61-a6a3-15cc35bbdd10`)
- S9: [effect of cu addition on microstructures and tensile properties of high__15b7a22a5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3295bf30-9218-4fba-b6c8-ea98c962e68d/resource) (`3295bf30-9218-4fba-b6c8-ea98c962e68d`)
- S22: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b8d828b-9b7c-4b1a-9d75-5505c881e499/resource) (`9b8d828b-9b7c-4b1a-9d75-5505c881e499`)
- S25: [压铸铝合金研究现状与未来发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b33f5626-1f14-4afd-bef1-1eec02f88d21/resource) (`b33f5626-1f14-4afd-bef1-1eec02f88d21`)
- S17: [alsicunimg系铸造耐热铝合金组织及其高温性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6cdab040-5feb-4b3a-bc9a-7a71f0bc6774/resource) (`6cdab040-5feb-4b3a-bc9a-7a71f0bc6774`)
- S29: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c40ebc93-2d2e-4fba-9ea9-54a5e0fd9389/resource) (`c40ebc93-2d2e-4fba-9ea9-54a5e0fd9389`)
- S35: [图3-10 2195铝锂合金XRD谱图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4299733-c4d5-48c5-940c-f301db88abc4/resource) (`d4299733-c4d5-48c5-940c-f301db88abc4`)