---
version: "v1"
generated_at: "2026-06-18T10:52:44+00:00"
confidence_score: 0.82
confidence_level: "high"
confidence_basis:
  cited_sources: 20
  source_quality_score: 0.82
  freshness_score: 0.74
  evidence_coverage_score: 1.0
---

## DAC模具钢

### 定义与品牌归属

DAC模具钢属于**热作模具钢**类别，是压铸专用模具材料。该牌号为**日本日立金属株式会社（Hitachi Metals）**的专有产品，并非如部分资料所述的日本大同特殊钢（Daido Steel）旗下产品。日本大同特殊钢同级别的压铸热作模具钢产品为 **DHA1、DH31** 等牌号，二者在压铸模具材料选型的公开技术文献中常被并列列举[[S21,S20,S1]]。

DAC模具钢是压铸行业公认的常用热作模具钢牌号之一，与H13类热作钢同为压铸模核心成型零件的主流选材[[S16]]。

### 化学成分

DAC模具钢的标称化学成分（质量分数）如下表所示，其成分等效对应JIS标准牌号 **SKD61**，与AISI H13、DIN 1.2344的成分高度匹配[[S21,S3,S9]]。

| 元素 | 质量分数（%） |
|:---|:---|
| 碳 (C) | 0.4 |
| 硅 (Si) | 1.0 |
| 锰 (Mn) | 0.4 |
| 铬 (Cr) | 5.3 |
| 钼 (Mo) | 1.5 |
| 钒 (V) | 1.1 |

**来源：**[[S21]]；另有一项铸铝电机转子压铸模流仿真研究中所列DAC元素含量表格数据显示Cr含量为0.25%（Mn为0.4%），与标称成分存在差异，属于特定仿真研究的个别参数设定，不应视为DAC钢的标准成分[[S3]]。

### 标准与规范

DAC模具钢对应JIS G 4404标准内的 **SKD61** 牌号，属于NADCA压铸模具钢推荐目录覆盖产品，其成分完全符合ISO 4957规定的热作合金工具钢 **4CrMoV5-1** 的指标要求[[S9,S15]]。该材料同时可对应中国国标 **4Cr5MoSiV1**（即H13钢）[[S19,S11,S20]]。

### 微观组织

DAC模具钢经淬火回火后，其典型金相组织为回火马氏体基体上弥散分布的细小碳化物相，晶粒边界清晰。

![压铸模具钢材金相组织显微照片，呈现淬火回火态热作模具钢的典型显微组织特征，可见清晰晶粒边界与弥散分布的细小碳化物相](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1623947-fe42-4361-9f48-6df5f9968cd1/resource)

该显微组织图片出自1987-88年压铸行业公开资料，呈现了合格热作压铸模具钢的典型显微组织特征，对应DAC模具钢经淬火回火后的微观组织状态，可用于解释其耐热裂纹、抗热疲劳的微观机理[[S22]]。

### 关键性能属性

DAC模具钢出厂为退火态，退火硬度为 **HB185**[[S21]]。该材料在高温环境下具备**强度与韧性平衡**的特性，易切削加工，热处理变形小，热稳定性好，可提升压铸模具的使用寿命与可靠性[[S21]]。

DAC、SKD61、国产4Cr5MoSiV1同属5%Cr系H13级热作钢，成分高度接近。DAC作为日立金属的量产牌号，其冶金控制精度优于普通商用SKD61，热处理变形量更小[[S19,S11]]。

### 热处理工艺

#### 淬火工艺

DAC铝压铸模的淬火热处理标准流程如下[[S6,S13]]：

1. **第一段预热**：温度区间 **500~550℃**，保温时长为最终淬火加热保持时间的 **2倍**；
2. **第二段预热**：温度区间 **750~800℃**，保温时长为最终淬火加热保持时间的 **1倍**；
3. **淬火加热**：温度区间 **1000~1050℃**[[S13,S6]]；
4. **冷却**：采用吹风冷却或高压气体冷却，冷却至 **100~150℃** 后即转入回火工序[[S13,S6]]。

壁厚 **50mm以下**、形状简单的小型模具可省略预热步骤[[S6]]。

![日本DAC铝压铸模淬火热处理工艺图，完整呈现两段预热、淬火加热及冷却的全流程温度参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90bb0771-7688-4786-854f-0353efa13eeb/resource)

该工艺图出自《压铸技术手册》，完整呈现了DAC模具钢淬火热处理工艺路径，可为实际生产制定热处理规范提供依据[[S13]]。

#### 回火工艺

DAC模具钢回火保温时长的设置规则如下[[S26]]：

| 回火温度范围 | 保温时长 |
|:---|:---|
| ≥500℃ | 基准值 T |
| 250~500℃ | 1.5 T |
| <250℃ | 2 T |

### 表面处理

DAC模具钢适配多种表面处理工艺[[S26]]：

- **气体氮化**
- **软氮化**
- **离子氮化**
- **PVD类硬质涂层沉积**

上述表面处理可提升型腔表面的耐磨性、耐腐蚀性与抗粘模性能[[S26]]。

### 使用中的去应力处理

采用DAC模具钢制备的压铸模，在服役过程中需定期进行去应力回火[[S26]]：

- **首次去应力**：压铸 **5000~10000次** 后进行；
- **后续处理**：每压铸 **10000~20000次** 进行一次；
- **温度控制**：去应力回火温度需**低于模具最终回火温度30~50℃**。

### 应用场景

DAC模具钢主要应用于以下铸造合金的压铸模具制造[[S21,S11]]：

- 铝合金压铸
- 锌合金压铸
- 镁合金压铸
- 铜合金压铸

此外，该材料同样适用于[[S21,S11]]：

- 低压铸造模具
- 高硬度塑料模具
- 热锻冲头
- 切槽刀等热作刀具

在压铸模具结构中，DAC模具钢可作为模芯（模仁）、滑块、成型镶件等核心成型部件的材料使用[[S27,S16,S24]]。

### 产品系列与变体

DAC产品体系包含以下型号，其中 **DAC55** 为重要改良型号[[S21]]：

| 型号 | 特点 |
|:---|:---|
| DAC | 基础牌号，高温强度与韧性均衡 |
| DAC10 | 产品系列子型号 |
| DAC55 | 改良型，**耐热裂纹抗性显著提升**，适配大型压铸模具、高性能压铸模及挤压模 |

### 牌号对照与差异

DAC与相近热作模具钢的对比关系如下：

| 牌号 | 生产商 | 所属体系 | 主要特点 |
|:---|:---|:---|:---|
| DAC | 日本日立金属 | SKD61 / H13 等级 | 冶金精度优于普通SKD61，热处理变形小[[S19,S11]] |
| SKD61 | JIS标准 | H13基型 | 通用型热作模具钢，碳0.39%、硅1.00%、铬5.40%、钼1.35%、钒1.00%[[S17]] |
| H13 | 多国通用 | 4Cr5MoSiV1 | 碳0.32%~0.45%，热处理后硬度可达HRC47~49[[S7]] |
| 8407 | 瑞典一胜百 | H13改良型 | 采用电渣重熔工艺，各向同性更优，硬度可比普通H13高1~2HRC[[S11]] |
| DH31-S | 日本大同 | 改良H13系 | 耐热裂纹性能优于普通SKD61[[S18]] |
| DHA1 | 日本大同 | SKD61等级 | 大同特殊钢旗下与DAC同级别的产品[[S20]] |

### 局限性

DAC模具钢作为H13同类型热作模具钢，在实际使用中可能面临以下问题[[S25,S5]]：

- **热疲劳裂纹**：服役过程中受反复急冷急热冲击，模具表面易出现热疲劳网状裂纹（龟裂）；
- **大截面淬透性不足**：大尺寸截面下存在淬透性不足的风险；
- **粘模倾向**：若型腔表面加工处理不当，铝合金熔体可能发生粘附；
- **使用温度上限**：常规服役条件下，长期安全使用温度上限约为 **600℃**[[S5]]。

## Sources
- S21: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd70e174-b808-406e-809c-d0878cac4d8b/resource) (`dd70e174-b808-406e-809c-d0878cac4d8b`)
- S20: [日本模具钢牌号介绍](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4997240-dcb3-4862-8d92-323c8addf95a/resource) (`d4997240-dcb3-4862-8d92-323c8addf95a`)
- S1: [日本模具钢牌号介绍](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09c4f347-58c1-4ce4-810e-0d6aec0f1b4b/resource) (`09c4f347-58c1-4ce4-810e-0d6aec0f1b4b`)
- S16: [5613234_压铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5d284c0-f817-405d-9c28-c9a5d9bb7e8b/resource) (`c5d284c0-f817-405d-9c28-c9a5d9bb7e8b`)
- S3: [表3.4 DAC的元素含量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1582d6e6-8398-4a31-9843-57c219fd64d3/resource) (`1582d6e6-8398-4a31-9843-57c219fd64d3`)
- S9: [0197_c95046d5da48befa_Tool_steel_1.2344](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70496189-13fd-4480-91cd-64fa7600ae2b/resource) (`70496189-13fd-4480-91cd-64fa7600ae2b`)
- S15: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc53cb25-5396-484c-be87-4b2a0e144011/resource) (`bc53cb25-5396-484c-be87-4b2a0e144011`)
- S19: [模具材料应用手册第二版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1aa489f-3a8b-4462-837f-e93000961e7e/resource) (`d1aa489f-3a8b-4462-837f-e93000961e7e`)
- S11: [TextNode64](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/750727d2-838b-4110-8237-b89ec44357af/resource) (`750727d2-838b-4110-8237-b89ec44357af`)
- S22: [压铸模具钢材金相组织显微图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1623947-fe42-4361-9f48-6df5f9968cd1/resource) (`e1623947-fe42-4361-9f48-6df5f9968cd1`)
- S6: [TextNode40](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3504b6b8-b980-4202-8d97-d319fdbad8b4/resource) (`3504b6b8-b980-4202-8d97-d319fdbad8b4`)
- S13: [日本DAC铝压铸模淬火热处理工艺图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90bb0771-7688-4786-854f-0353efa13eeb/resource) (`90bb0771-7688-4786-854f-0353efa13eeb`)
- S26: [TextNode41](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc6f472a-284d-4d69-9d77-2fc71b4f9260/resource) (`fc6f472a-284d-4d69-9d77-2fc71b4f9260`)
- S27: [5613234_压铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd295b93-ca8d-4434-9e87-7cb41bf91f51/resource) (`fd295b93-ca8d-4434-9e87-7cb41bf91f51`)
- S24: [压铸成型技术及模具 设计与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f235c1ae-25cd-48d8-8016-0ab8dc799b3f/resource) (`f235c1ae-25cd-48d8-8016-0ab8dc799b3f`)
- S17: [0197_c95046d5da48befa_Tool_steel_1.2344](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb7f0c4e-f468-47c1-b3d4-6913a701f1eb/resource) (`cb7f0c4e-f468-47c1-b3d4-6913a701f1eb`)
- S7: [5368567_H13钢](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b0c8af7-a5cd-452e-b2be-ceb4c50ca11f/resource) (`3b0c8af7-a5cd-452e-b2be-ceb4c50ca11f`)
- S18: [模具材料及其热处理译文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d09fb11f-7bfc-486b-9113-50ff3e7edcbc/resource) (`d09fb11f-7bfc-486b-9113-50ff3e7edcbc`)
- S25: [effect of aluminizing and oxidation on the thermal fatigue damage of hot__64036795bd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa980acd-12d8-49bf-b642-0b508fe544be/resource) (`fa980acd-12d8-49bf-b642-0b508fe544be`)
- S5: [模具失效与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d57d311-a5d4-468f-8b16-1c4de437e23b/resource) (`2d57d311-a5d4-468f-8b16-1c4de437e23b`)