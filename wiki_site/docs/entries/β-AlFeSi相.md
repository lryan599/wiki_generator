---
version: "v1"
generated_at: "2026-06-18T13:20:25+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 16
  source_quality_score: 0.84
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

β-AlFeSi相属于Al-Fe-Si三元体系中的一种平衡稳定相，在铝富角相图中拥有明确的相区边界[[S4]]。该相是6xxx系变形铝合金（Al-Mg-Si系）中最具危害性的富铁金属间化合物之一[[S13]]。

## 定义与化学计量
β-AlFeSi相存在多个公认的化学计量比表述。β-Al₉Fe₂Si₂与β-Al₅FeSi均为该相的主流表达方式，对应的化学组成范围为25~30 wt.% Fe、12~15 wt.% Si，Fe/Si质量比为2.25~1.6[[S12]]。学术界对该相的确切化学计量比存在争议，两种写法并存于现行文献中[[S12,S1]]。

## 晶体结构
β-AlFeSi相晶体结构的主流共识为单斜晶系，但不同研究给出的晶格参数存在差异。Monall等人报道的参数为a=0.5792 nm、b=1.2273 nm、c=4.313 nm、β=98.93°[[S13]]；Phragmen报道的参数为a=6.11 kX、b=6.11 kX、c=41.4 kX、β=91°[[S14]]。此外，存在部分研究提出该相为正交晶系或四方晶系的结论，晶体结构归属仍有争议[[S13]]。

图1为JSmol生成的β-Al₅FeSi晶胞沿[010]方向的三维结构示意图，橙色原子代表Fe，灰色原子为Al或Si，直观展示了其复杂晶胞内的原子排布特征[[S10]]。

![图1 β-Al₅FeSi晶胞沿[010]方向的三维结构示意图（橙色：Fe，灰色：Al/Si）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c85a623-1b09-42d8-954f-9dea10459eda/resource)

## 分类与所属体系
β-AlFeSi相属于Al-Fe-Si三元系富铝角的稳定相。下表列出了Al-Si系中主要富铁相及其晶体结构[[S1]]。

| 富铁相 | 晶体结构 |
|--------|----------|
| α-Al₁₅Fe₃Si₂ | 六方 |
| β-Al₉Fe₂Si₂（β-Al₅FeSi） | 单斜 |
| δ-Al₃FeSi₂ | 四方 |

## 形成机制与析出条件

### 临界Fe含量与冷却速率
β-AlFeSi相在平衡冷却条件下为稳定相，其析出行为受冷却速率直接调控。冷却速率越高，形成β相的临界Fe含量阈值越高[[S5]]：

| 冷却速率 | 形成β相的临界Fe含量 (wt.%) |
|---------|---------------------------|
| 1 ℃/s | 0.75 |
| 5 ℃/s | 0.9 |
| 10 ℃/s | 1.0 |

冷速降低会导致β相的尺寸与体积分数显著上升[[S5]]。

### 析出温度与热稳定性
AA6005铝合金中β-AlFeSi相的初生析出温度约为608℃[[S6]]。该相热稳定性极强，常规550℃保温2小时的均匀化处理不足以使其溶解[[S7]]，即使在560℃保温12小时仍无法实现该相的完全转变[[S7]]。

### 与Mg、Si元素的相互作用
在含Mg的6xxx系合金凝固过程中，β-AlFeSi相可参与包晶反应转变为π-AlFeMgSi相：L + β-AlFeSi ⇌ αAl + π-AlFeMgSi + Si。该反应发生在约567℃条件下[[S6]]。然而，在550℃保温2小时的均匀化处理过程中，π-AlFeMgSi相又可完全分解为β-AlFeSi相，表明β相在常规均匀化温度下反而是更稳定的含铁相[[S7]]。

## 形貌特征与性能危害

### 微观形貌
β-AlFeSi相在显微组织中的二维截面通常呈现长针状或板条状特征，是典型的硬脆相[[S11,S9]]。

图2为金属型铸造AA6005铝合金经均匀化处理后的SEM背散射电子图像，清晰显示了β-AlFeSi相的针状形貌，标尺为10 μm[[S2]]。

![图2 均匀化处理后AA6005铝合金中针状β-AlFeSi相的SEM背散射图像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b61919f-ed19-4bc4-8b7b-615b63832cdf/resource)

### 力学性能影响
β-AlFeSi相作为应力集中源，直接诱发微裂纹萌生，割裂铝基体连续性，显著降低合金的延伸率与塑性变形能力[[S11,S9]]。在6xxx系铝合金中，该相是挤压变形过程中诱发局部脆性断裂、降低成品良率的核心有害相[[S9]]。

当Fe含量增至1.2 wt.%时，β相呈现粗大板条状，形成温度高于α-Al基体，在凝固过程中优先析出，阻碍残余液相的流动补缩，导致缩孔缩松等凝固缺陷[[S11]]。

### 热遗传性
β-AlFeSi相具备极强的热遗传性。铸锭中存在的粗大棒状β相在后续热轧、冷轧加工过程中几乎无法发生破碎、转变或球化，将一直保留到最终轧制后的铝箔坯料及成品中，持续对合金塑性造成危害[[S15]]。

## 控制手段

### 成分标准
根据EN 573-3和ASTM B221等国际标准，6005A铝合金中Fe的最大允许质量分数为0.35 wt.%，以此严格控制β-AlFeSi粗大相的生成[[S8]]。

### Mn元素变质
添加Mn是抑制β-AlFeSi相、改善其形貌的最有效手段[[S3,S16]]。通过Mn/Fe质量比调控可实现相转变：

- 当Mn/Fe质量比达到约1.2时，合金中几乎所有针状β-AlFeSi相可完全转化为近球形汉字状的α-Al(FeMn)Si相，力学性能显著提升[[S3]]；
- 当Fe含量控制在0.14 wt.%以下时，仅需添加约0.11 wt.%的Mn即可完全消除AA6005合金中的β-AlFeSi相[[S16]]；
- 此外，添加Cr、V等元素也能在一定程度上抑制β-AlFeSi相的形成[[S3]]。

## 相关相与邻接概念

### α-AlFeSi相
与β相相对应，α-AlFeSi相Si含量较低（6~12 wt.%）、Fe/Si质量比较高（5.5~2.75），呈汉字状或球状，危害性远小于β相[[S12,S9]]。在均匀化处理过程中，板条状β-AlFeSi相可在Mn原子参与下转变为球状的α-AlFeMnSi相[[S9]]。

### π-AlFeMgSi相
在含Mg的6xxx系合金中，β-AlFeSi相与π-AlFeMgSi相之间存在可逆转变关系。快速冷却条件下Mg的快速扩散可促进β相向π相的包晶转变；而均匀化处理过程中Mg溶入基体则导致π相分解回归β相[[S6,S7]]。

## Sources
- S4: [三元Al-Fe-Si体系Al角相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32e725cf-7504-4a2c-8333-39548996e839/resource) (`32e725cf-7504-4a2c-8333-39548996e839`)
- S13: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b81f6ec4-4cd3-43b8-a32b-306e6cf6badf/resource) (`b81f6ec4-4cd3-43b8-a32b-306e6cf6badf`)
- S12: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b66f89f8-7476-4c5b-b2e5-b61bd33c7b3b/resource) (`b66f89f8-7476-4c5b-b2e5-b61bd33c7b3b`)
- S1: [表1-1 Al-Si系铸造合金中的主要富铁相](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03b9a289-a9fd-49a9-809e-9b174a978862/resource) (`03b9a289-a9fd-49a9-809e-9b174a978862`)
- S14: [a handbook of lattice spacings and structures of metals and alloys__0d6d7e6946](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6423965-bdf9-456a-aad7-739bd0a6a72b/resource) (`f6423965-bdf9-456a-aad7-739bd0a6a72b`)
- S10: [图3-9 β-Al₅FeSi晶胞沿[010]方向的三维表征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c85a623-1b09-42d8-954f-9dea10459eda/resource) (`9c85a623-1b09-42d8-954f-9dea10459eda`)
- S5: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3862af40-fc9c-4240-a905-56d1397222a7/resource) (`3862af40-fc9c-4240-a905-56d1397222a7`)
- S6: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3f034cb2-b5a6-4ddb-b657-f9b80669453a/resource) (`3f034cb2-b5a6-4ddb-b657-f9b80669453a`)
- S7: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/428f3fc5-d5c1-413e-91b1-7a2743ce5544/resource) (`428f3fc5-d5c1-413e-91b1-7a2743ce5544`)
- S11: [Al-9Si-2Cu-xFe合金的微观组织及力学和导热性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1049ad5-518f-406a-9ac2-2a1077ed48ca/resource) (`a1049ad5-518f-406a-9ac2-2a1077ed48ca`)
- S9: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/976d1685-5daf-4ab4-bea6-7c2fc86efc5c/resource) (`976d1685-5daf-4ab4-bea6-7c2fc86efc5c`)
- S2: [图4.8(d) 金属型铸造AA6005铝合金均匀化处理后的SEM背散射电子图像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b61919f-ed19-4bc4-8b7b-615b63832cdf/resource) (`0b61919f-ed19-4bc4-8b7b-615b63832cdf`)
- S15: [现代铝合金板带投资与设计技术与装备产品与市场](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f85fafb3-b3aa-4549-a734-8a6ec307e7d6/resource) (`f85fafb3-b3aa-4549-a734-8a6ec307e7d6`)
- S8: [0094_992cb3b3e0743028_6005A_aluminium_alloy](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91324363-8480-44cd-9795-00021746d2d8/resource) (`91324363-8480-44cd-9795-00021746d2d8`)
- S3: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c50b561-764b-4f45-b65e-b40edcbec157/resource) (`2c50b561-764b-4f45-b65e-b40edcbec157`)
- S16: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff1a7890-07a7-4d8c-b68a-9fa5939e8c1e/resource) (`ff1a7890-07a7-4d8c-b68a-9fa5939e8c1e`)