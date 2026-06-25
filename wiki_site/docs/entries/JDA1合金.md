---
version: "v1"
generated_at: "2026-06-18T12:33:36+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 15
  source_quality_score: 0.83
  freshness_score: 0.95
  evidence_coverage_score: 1.0
---

## 概述

JDA1（亦称JDA1b）是由上海交通大学自主研发的Al-Si系免热处理高压压铸铝合金[[S20,S5]]。该合金隶属于JDA系列（JDA1x），在免热处理压铸铝合金谱系中与德国Silafont-36/37、Aural系列同属国际主流的Al-Si-X类材料[[S10]]。其核心特征是压铸完成后无需进行固溶或人工时效热处理，仅需在室温下经历4~72小时自然时效，即可获得与德国Silafont36合金经T6热处理后同等水平的力学性能，属于高强高韧压铸铝合金[[S8,S5,S20]]。JDA1b是JDA1的同一系列材料，在学术文献中两者常被交替使用以指代该款材料[[S1,S20,S5]]。研究资料中，JDA1指代该系列材料时侧重于对标应用与车企认证，JDA1b则更常出现在详细力学性能、微观组织及工艺参数的实证研究中[[S8,S17,S1]]。在目前可获取的研究成果中，未发现两者在成分体系、工艺规范或性能表现层面存在本质性矛盾，可认为JDA1与JDA1b为同种合金在不同研究语境下的命名差异。

## 合金成分与微观组织

JDA1b属于铝硅系合金，其成分设计通过高占比的Si与Mg元素保障力学性能及熔融态流动性，并添加稀土元素实现晶粒细化强化，从而适配大型复杂结构件对强度与塑性的严苛要求[[S5,S1]]。

在75MPa压力下压铸成形的3mm厚JDA1b板材呈现出压铸铝合金的典型分层金相形貌[[S1]]：
*   **边缘层（过冷层）**：试样边缘存在明显的过冷层区域。
*   **次边缘层**：α-Al基体与硬质共晶Si相均匀分布。
*   **心部**：同时存在两种α-Al组织形态，一种为细小圆整的球状初生组织，另一种为尺寸较大（平均晶粒尺寸20~30μm）的预结晶组织（ESC），后者因熔融金属在料筒中降温后随充型进入型腔并继续长大而形成[[S1]]。

## 力学性能与对标数据

JDA1系列合金的突出优势在于其铸态力学性能即可等效替代经T6或T7热处理的Silafont-36合金，省去了后续热处理工序，大幅降低能耗与生产成本[[S8,S14]]。

### 基础力学性能

对厚度为3mm的JDA1b压铸试样，在无预变形、室温自然时效24小时后的准静态力学测试结果为[[S17]]：
*   屈服强度（YS）：137.6 MPa
*   抗拉强度（UTS）：291.2 MPa
*   断后伸长率（E）：15.3%

### 对标性能对比

下表直接呈现了铸态JDA1与经T6、T7热处理的Silafont-36合金在主要力学指标上的对比[[S14,S8]]：

| 合金状态 | 抗拉强度 / UTS (MPa) | 屈服强度 / YS (MPa) | 伸长率 / E (%) |
| :--- | :--- | :--- | :--- |
| Silafont-36 (T6) | 290~340 | 210~280 | 7~12 |
| Silafont-36 (T7) | 200~240 | 120~170 | 15~20 |
| **铸态 JDA1** | **260~340** | **160~196** | **6~10** |
| 铸态 HL-111 | 280~299 | 120~130 | 10~12 |

数据显示，铸态JDA1在抗拉强度上与Silafont-36 T6态相当，在屈服强度上接近T7态，展现了免热处理状态下优异的综合力学性能[[S14]]。

### 预变形对力学性能的影响

JDA1b具备显著的应变强化效应[[S2]]。对试样进行不同预应变量（2%, 4%, 6%）处理并在室温下放置24小时自然时效后，其力学性能变化规律如下[[S17]]：
*   **强度提升**：随预应变量增加，屈服强度和抗拉强度同步显著提升。6%预应变后，屈服强度可从基态的137.6 MPa跃升至305.7 MPa，抗拉强度提升至359.4 MPa。
*   **塑性下降**：伸长率随预应变量增加而相应下降，6%预应变后从15.3%降至10.4%。
*   **总硬化值**：随预应变量增加线性上升，6%预应变时达到168.1 MPa。

此外，在不同应变率下，JDA1b的流动应力随应变率提升而同步升高[[S2]]。其熔点为875 K，室温（约27℃）下的Johnson-Cook (J-C) 本构模型参数已得到确定，可用于工程仿真[[S2]]。

## 高压压铸工艺窗口

JDA1b合金在一体化大型汽车结构件上已实现量产应用，其适配的典型高压压铸（HPDC）工艺窗口参数如下[[S12]]：
*   **模具预热温度**：150 ℃
*   **合金液浇注温度**：720 ℃
*   **低速压射速度**：0.2 m/s
*   **高速压射速度**：6.5 m/s
*   **压射比压**：35 MPa
*   **所需最低锁模力**：69060 kN

此参数基于尺寸为1591mm×1311mm×777mm的一体化汽车后舱结构件的实际生产设定，选用72000kN规格压铸机进行制造[[S12]]。

在工艺参数优化与缺陷控制方面，压铸模CAD系统可辅助确定包括合金种类、密度、投影面积、内浇口速度与面积、充型时间等关键工艺参数[[S19]]。同时，基于压铸仿真软件（如Anycasting）可对铸件充型末端的缺陷概率分布进行预判，用于指导工艺优化[[S18]]。

![JDA系列铝合金压铸工艺参数CAD确定界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec2d2367-43ed-45b5-9356-93e7be41db39/resource)

**图注**：压铸模CAD系统中用于确定JDA系列免热处理铝合金铸件属性、压铸机参数及浇注系统推荐参数的工艺参数对话框界面[[S19]]。

## 连接性能

JDA1b合金本身具备良好的焊接性[[S12]]。在异种材料连接方面，针对JDA系列铝合金与高强度钢板的自冲铆接（SPR）工艺研究显示[[S13]]：
*   JDA组铆接接头的峰值载荷和能量吸收值整体优于常规AlSi系压铸铝合金（如AlSi10MnMg-T7）接头。
*   在剪切与剥离工况下，选用1.2mm厚度下层高强度钢板可获得最优成形质量与力学性能。
*   在十字拉伸工况下，则以2.0mm厚度下层高强度钢板组合的铆接效果最佳。
*   需要注意的是，在钢-钢-铝三层板自冲铆接工艺中，JDA1b接头的下层板在受载时相对常规AlSi压铸铝接头更易出现裂纹缺陷[[S3]]。

## 应用与认证

JDA1合金已被通用汽车公司纳入旗下凯迪拉克CT6车型的官方材料清单，这是国内高校自主研发的非标压铸铝合金首次被国际主流顶级车企认可并实现装车应用[[S8]]。2015款凯迪拉克CT6白车身中，压铸铝合金占比高达17%，覆盖减震塔、柱内/外板、前扭力盒、中通道、后纵梁等多个车身结构件，JDA1合金可适配上述高集成度零件的制造需求[[S8,S15]]。JDA系列免热处理铝合金的合作方包括华人运通等，是上海交通大学轻合金中心拥有自主知识产权的成果体系[[S6]]。

## Sources
- S20: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1b1883b-df7f-49da-8f8f-69fcc234c838/resource) (`f1b1883b-df7f-49da-8f8f-69fcc234c838`)
- S5: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ec99dc6-93d7-4292-aaee-3bf6e20f6ee7/resource) (`5ec99dc6-93d7-4292-aaee-3bf6e20f6ee7`)
- S10: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cce15c9-13d6-4bc3-a83e-75c736157c17/resource) (`8cce15c9-13d6-4bc3-a83e-75c736157c17`)
- S8: [免热处理铝合金大型结构件一体压铸研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e3d2613-0205-4b27-953e-ef0887894422/resource) (`7e3d2613-0205-4b27-953e-ef0887894422`)
- S1: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27d7482f-21a5-4501-85dd-d9923ec35764/resource) (`27d7482f-21a5-4501-85dd-d9923ec35764`)
- S17: [TextNode4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3a611b9-4451-4978-9953-4768b103b2c2/resource) (`c3a611b9-4451-4978-9953-4768b103b2c2`)
- S14: [表2 铸态JDA1、HL-111与T6、T7热处理后Silafont-36合金性能对比[16, 19, 36]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b72149df-7afc-41fe-a108-e55d02eb60b5/resource) (`b72149df-7afc-41fe-a108-e55d02eb60b5`)
- S2: [TextNode5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31ffeda2-c5c8-45bf-8e59-279aefc0a04a/resource) (`31ffeda2-c5c8-45bf-8e59-279aefc0a04a`)
- S12: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3c99480-14c0-4100-b6d0-1f61b5313c13/resource) (`a3c99480-14c0-4100-b6d0-1f61b5313c13`)
- S19: [压铸模CAD系统的工艺参数确定对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec2d2367-43ed-45b5-9356-93e7be41db39/resource) (`ec2d2367-43ed-45b5-9356-93e7be41db39`)
- S18: [图7 U1V1W1-转向器伺服壳体典型截面X的缺陷概率分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd29c4db-5f97-4441-a9b0-933b89e4f701/resource) (`cd29c4db-5f97-4441-a9b0-933b89e4f701`)
- S13: [压铸铝与高强度钢自冲铆接成形质量与力学性能的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b25a016b-9c15-4cd8-94c0-e12f037804ce/resource) (`b25a016b-9c15-4cd8-94c0-e12f037804ce`)
- S3: [钢-钢-铝三层板自冲铆接成形质量及力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b278c2b-a706-4571-9081-ff274e6885dc/resource) (`3b278c2b-a706-4571-9081-ff274e6885dc`)
- S15: [乘用车白车身铝合金压铸结构件及材料应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bef051ea-7bf0-49d3-b8df-e0c4d6faf378/resource) (`bef051ea-7bf0-49d3-b8df-e0c4d6faf378`)
- S6: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d217161-f10d-4dc0-a6c7-c0bfc2200ff7/resource) (`6d217161-f10d-4dc0-a6c7-c0bfc2200ff7`)