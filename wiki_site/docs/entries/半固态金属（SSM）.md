---
version: "v1"
generated_at: "2026-06-18T15:57:12+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 63
  source_quality_score: 0.86
  freshness_score: 0.78
  evidence_coverage_score: 1.0
---

## 概述

半固态金属（Semi-Solid Metal, SSM）是指处于固相线与液相线温度之间、具备非枝晶近球状显微组织的金属材料，其理想固相体积分数通常为30%~65%[[S62,S31]]。该概念的工艺应用潜力在20世纪70年代初首次被研究者确认[[S62,S31]]。与全液态金属相比，半固态金属含有大量近球形固相颗粒悬浮于液相基体中；与全固态金属相比，其变形抗力显著降低，可在较低载荷下实现复杂形状的近净成形[[S62,S17]]。

## 核心定义与术语区分

半固态金属是宏观材料大类概念，泛指所有处于固液两相共存区间、具备非枝晶球状晶组织的金属材料。与以下术语存在明确的层次关系[[S29,S26]]：

- **半固态浆料**：半固态金属在制备过程中呈现的固液混合流体形态，是流变成形（一步法）的直接加工对象。按固相率可分为低固相率型（5%~20%）和高固相率型（40%~60%）[[S29]]。
- **半固态坯料**：半固态浆料完全凝固后得到的、具备完整非枝晶球状显微组织的固态预制棒材或块材，常规尺寸为φ38~φ152 mm、长度1.5~6 m，是触变成形（二步法）的中间原料。未受剪切时表观黏度可达10⁷ Pa·s，可直接用普通机械方式搬运[[S10,S27,S26]]。
- **触变金属**：特指具备触变性的半固态金属材料，是触变成形工艺的直接加工对象，属于半固态金属的子集[[S31,S61]]。触变成形合金指专门针对触变成形工况设计的合金牌号，如半固态专用A356、A357等[[S78]]。

> 值得注意的是，并非所有合金都适用于半固态成形。纯金属和完全共晶合金仅存在单一熔点或共晶温度，无明显的固-液两相区间，因此无法进行半固态加工[[S54]]。

## 核心组织特征

半固态金属区别于普通铸造金属的关键在于其非枝晶/球状晶显微组织。普通铸造凝固过程中初晶以枝晶方式长大，当固相率达20%~30%时即形成连续网络骨架并丧失宏观流动性。半固态金属经强烈搅拌或特殊控冷处理后，初生相转变为球状、椭球状或蔷薇状的独立分散颗粒，在固相率达50%~60%时仍具备良好的流变性[[S32,S60,S75]]。

![半固态加工组织典型微观形貌，大量均匀细小的近球形初生相悬浮于液相基体中](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48590627-2894-445f-bc57-353a22e158ec/resource)

半固态组织来源于枝晶，搅拌作用阻止初始小枝晶向粗大枝晶发展，同时晶体的等轴生长和合并生长促使初生相向球形或椭球形演变[[S32]]。实验对比表明，半固态挤压铸造制备的A356铝合金共晶硅的圆度最高、长径比最低，球化效果远优于金属型铸造和液态挤压铸造[[S21]]。

## 流变特性

### 触变性

触变性是半固态金属的核心流变特性：当切应力恒定时，材料表观黏度随切变时间延长逐步降低；停止剪切静置后，黏度又逐步恢复至初始数值，呈现“受剪切即流动、静置后复凝为类固体”的特征[[S32,S31,S49]]。触变性的量化表征通常采用滞后环法——记录剪切速率从0升至最大值再降至0过程中形成的封闭滞回曲线面积，面积越大对应触变性越强[[S66,S33]]。

### 黏度-剪切速率关系

全液态合金属于牛顿流体，黏度为不随切变速率变化的常数；半固态金属属于伪塑性（剪切变稀）非牛顿流体，表观黏度随剪切速率增大显著降低[[S32,S79]]。半固态A356铝合金稳态表观黏度符合幂律关系：

η = c · γ^m

其中m取值范围为-1.2~-1.3（或更宽泛的-1.2~+1.3），η为表观黏度，γ为剪切率，c为稠度系数[[S60,S34]]。

### 表观黏度与固相分数的关系

表观黏度与固相分数之间存在强烈的耦合关系，可用经验公式表示：

η_a = A exp(B f_s)

其中A、B为与合金类型相关的常数。Sn-Pb合金的B值为20，镁合金的B值为15[[S66,S6]]。

按固相分数区间，半固态金属浆料的流变行为呈现阶段性转变[[S1]]：

| 固相分数范围 | 流变行为特征 |
|---|---|
| f_s < 20% | 可按牛顿黏性流体处理 |
| 20% ≤ f_s ≤ 60% | 明显的非牛顿假塑性特征 |
| f_s ≥ 60%~70% | 固相颗粒形成连续骨架，呈浸满液相的多孔固体特性，易发生固-液相分离偏析 |

半固态金属进行正常成形的通用固相分数范围为30%~60%。流变成形适配固相分数0.3~0.4区间，触变成形适配固相分数0.6~0.7区间，工业量产半固态压铸常规采用的固相分数区间为50%~60%[[S1,S42,S38]]。

## 常用合金体系与关键参数

### 铝合金

A356和A357是半固态成形商业生产中应用最广泛的两类铝合金，化学成分核心差别在于镁含量不同[[S41,S18,S54]]：

| 元素（质量分数%） | A356 | A357 |
|---|---|---|
| Si | 6.50~7.50 | 6.50~7.50 |
| Fe | <0.20 | <0.15 |
| Cu | <0.20 | <0.05 |
| Mg | 0.25~0.45 | 0.45~0.60 |
| Zn | <0.10 | <0.05 |
| Ti | <0.20 | <0.20 |

A356半固态铝合金固相线温度为555 °C，液相线温度为615 °C，适配半固态加工温度区间为570~590 °C，对应固相体积分数35%~55%，典型坯料预热温度为580~585 °C[[S63,S18,S76]]。两者的共晶体固相体积分数均约为45%，将加热温度控制在共晶温度以上即可较容易获得固相率50%的浆料[[S54,S18]]。

半固态加工用A319和A355合金并非完全等同于常规铸造用牌号。Pechiney公司开发的半固态专用版本对应常规铸造牌号为SSM319和SSM355，两者Si含量均为6%，在相近重熔条件下与A356/A357具备基本一致的固相体积分数和流变行为[[S2,S54,S11]]。

半固态常用的A356、A357牌号与ASTM标准下的常规铸造牌号一一对应。国内半固态成形可引用的铸造合金标准体系包括GB/T 1173（铸造铝合金）、GB/T 1177（铸造镁合金）、GB/T 13818（压铸锌合金）、ASTM B26（铝合金砂型铸件）、ASTM B85（铝合金压铸件）、ASTM B94（镁合金压铸件）、ISO 209（铝合金牌号规则）、ISO 301（锌合金铸锭标准）等[[S30,S51,S35,S67]]。

### 镁合金

AM60半固态镁合金固相线温度为540 °C，液相线温度为615 °C，半固态压铸推荐浇注温度区间为570~600 °C[[S14]]。AZ91D镁合金半固态流变成形典型温度区间为550~590 °C[[S1]]。

### 温度窗口

半固态成形温度处于合金液相线与固相线之间，铝合金半固态可操作温度窗口可达约50 °C，而窄熔点区间铜合金仅为零点几摄氏度[[S31]]。

## 半固态浆料/坯料制备方法

半固态非枝晶球状组织的制备方法分为两大类：外场/外力破碎枝晶类和固相调控组织类[[S58,S73,S59]]。工业应用最广泛的四类工艺如下：

### 机械搅拌法

最早的半固态合金制备工艺，通过对凝固过程中的金属熔体施加持续强剪切作用，破碎初生树枝晶，得到分散的球状固相颗粒悬浮于液相的半固态浆料，固相颗粒尺寸通常为50~100 μm[[S58,S77]]。优点是设备结构简单、工艺参数易于调控，适配绝大多数合金体系的实验室研发；缺点是存在搅拌死角导致浆料均匀性差，搅拌构件易腐蚀污染合金液、易卷入气体，生产效率低，仅适合实验室使用[[S24,S72,S57]]。

### 电磁搅拌法

非接触式制备工艺，依靠旋转磁场在金属熔体内感应出电流，在洛伦兹力驱动下使熔体产生可控运动，实现枝晶破碎和球化。主流实现方式包括传统交变电流感应法和1993年提出的旋转永磁体法[[S58,S24]]。优点是浆料无外源污染、气体卷入少、工艺调控自由度高，是当前工业量产半固态坯料的主流技术；缺点是设备投资大、能耗高，大尺寸坯料内部搅拌力衰减严重，表层与心部球化均匀性存在偏差[[S24,S72,S77]]。

电磁搅拌连铸技术可大规模生产φ38~φ152 mm的A356和A357铝合金坯料，美国阿卢马克斯工程金属工艺公司年产能已达1.6万吨[[S27]]。

![半固态金属制备的四种搅拌模式：机械搅拌、被动搅拌、垂直电磁搅拌、水平电磁搅拌](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2243059e-f530-4986-9ea3-1a2fa437dedb/resource)

### 单辊旋淬法（SCR）

属于改进型机械搅拌类工艺，通过旋转的带冷却功能的辊轮将弧状结晶壁上生长的初生晶不断碾下、破碎，与剩余液相混合得到均匀的流变半固态浆料。核心控制参数为辊轮转速、冷却壁与辊轮间隙、冷却速率[[S80]]。

### 应变诱导熔化激活法（SIMA）

固相处理类半固态坯料制备工艺：将常规铸锭先通过挤压、滚压等预变形得到带强烈拉长形变组织的半成品棒料，再升温至固液两相区保温，形变晶粒通过再结晶和部分熔化转变为细小球状非枝晶组织。球状晶粒尺寸可控制在约20 μm，坯料纯净度高，适配高低熔点全合金体系，尤其适合不锈钢、铜合金等高熔点半固态坯料制备。受预变形工序限制，仅适合生产小直径坯料[[S58,S24,S5,S31]]。

## 在半固态成形工艺中的角色

半固态成形工艺分为流变成形（Rheocasting，一步法）和触变成形（Thixoforming，二步法）两大路线[[S44,S53,S65]]：

- **流变成形**：将制备好的预定固相分数的半固态浆料直接送往成形设备完成铸造或锻造成形，无需先铸锭冷却后二次加热。可直接使用常规压铸合金为原料，生产中去除的浇道、废料和不合格铸件可在车间内直接闭环回收[[S36,S43,S74]]。意大利Stampal SpA公司采用NRC流变成形设备生产A357铝合金发动机支座，生产成本比触变成形低22%，金属损耗仅1%（触变成形为10%）[[S56,S64,S37]]。

- **触变成形**：将剧烈搅拌获得的球状晶半固态浆料完全凝固成锭坯，分切后重新加热至固液两相区，再送入成形设备完成成形。坯料输送方便，易于实现自动化操作[[S45]]。触变成形细分工艺包括[[S22]]：

| 工艺类型 | 核心优势 |
|---|---|
| 半固态触变射铸 | 铸件表面和内部质量高，成形尺寸精度高 |
| 半固态触变压铸 | 成形温度低、凝固时间短、生产周期短、组织均匀 |
| 半固态触变挤压成形 | 显著降低变形抗力，适配复杂构件成形 |
| 半固态触变轧制成形 | 固液相变形均匀，板材厚度方向组织均匀 |

触变成形必须使用通过剧烈搅拌制备的非枝晶组织专用预铸锭坯，要求内部初生固相为均匀近球形结构，对合金洁净度和氧化夹杂含量要求高[[S43]]。

## 应用领域

### 汽车领域

典型应用构件包括Jeep Wrangler半固态触变射铸备胎支架、镁合金电驱壳体、20寸级大型轮毂、汽车副车架、发动机支座、悬挂结构件等[[S43,S15,S40]]。采用A357铝合金半固态成形制备的汽车悬挂构件经T5热处理后抗拉强度可达319 MPa[[S15]]。半固态铝合金相比传统液态压铸可节能35%，半固态轧制的轧制力仅为传统热轧的40%[[S20]]。

### 航空航天领域

半固态成形可制备直升机传动系统机匣、转子壳体等轻量化高强构件。C70S6钢半固态触变压铸连接件性能显著优于传统成形工艺生产的同材质构件[[S20]]。

### 3C电子领域

半固态触变射铸镁合金构件广泛用于笔记本电脑外壳、手机壳体、通讯设备薄壁件等产品，兼具高电磁屏蔽性能和薄壁高精度优势，可成形最小厚度约1.5 mm的薄壁结构[[S39,S40]]。

### 力学性能优势

半固态挤压铸造制备的A356铝合金，相比常规金属型铸造同材质合金，抗拉强度、延伸率、硬度三项力学性能指标全面提升[[S46]]。ZGK521镁合金半固态压铸试样相比常规金属型铸造试样，抗拉强度、屈服强度、伸长率均实现显著提升[[S25]]。

## 局限性与常见缺陷

### 液相偏析

半固态浆料充型过程中，由于剪切梯度和速度梯度作用，固相颗粒从型腔壁面向中心迁移，引发固液相分离。存在液相偏析缺陷的A357铝合金构件整体强度低于无偏析的A356构件[[S19,S15]]。

### 卷气与鼓泡

充型控制不当会引发卷气缺陷，后续固溶热处理时表层/亚表层气体受热膨胀，在铸件表面形成鼓泡[[S19]]。

### 卷入性缺陷

半固态浆料制备过程中流动卷入空气、氧化膜折叠可导致孔洞类缺陷和氧化物双层膜缺陷，显著降低铸件力学性能的一致性。通过添加低熔点金属如Bi或增大挤压比，可实现对卷入性缺陷的钝化[[S48,S16]]。

## 图示辅助理解

不同成形方式下A356铝合金共晶硅的圆度与长径比对比显示，半固态挤压铸造的共晶硅球化效果最优，直观反映了半固态金属微观组织的优势特征[[S21]]。

## Sources
- S62: [0008_c123fb97521d886c_Semi-solid_metal_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3451a41-1eee-4bcd-9744-080e628aeda9/resource) (`c3451a41-1eee-4bcd-9744-080e628aeda9`)
- S31: [0008_c123fb97521d886c_Semi-solid_metal_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f96f393-bd00-4eae-8adb-c21255b45bec/resource) (`5f96f393-bd00-4eae-8adb-c21255b45bec`)
- S17: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/36861d36-3d26-4499-9123-e05c00e991e8/resource) (`36861d36-3d26-4499-9123-e05c00e991e8`)
- S29: [Mg-5Zn-xGd-0.6Zr合金半固态工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/565707bc-2c8f-4ce2-871d-6712dede5e19/resource) (`565707bc-2c8f-4ce2-871d-6712dede5e19`)
- S26: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5214ea5a-c9af-49bb-8266-3ce8248ac3b4/resource) (`5214ea5a-c9af-49bb-8266-3ce8248ac3b4`)
- S10: [半固态金属成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28ab72fe-d194-43fb-98de-2ef23980e175/resource) (`28ab72fe-d194-43fb-98de-2ef23980e175`)
- S27: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5225168d-ed95-46e1-bd94-4af677bec9a6/resource) (`5225168d-ed95-46e1-bd94-4af677bec9a6`)
- S61: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c193e5bc-d1c4-4dfd-a363-42851211608c/resource) (`c193e5bc-d1c4-4dfd-a363-42851211608c`)
- S78: [材料成形新技术及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/face24ec-20e7-4dc4-bc5e-472547961581/resource) (`face24ec-20e7-4dc4-bc5e-472547961581`)
- S54: [TextNode297](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a74d79f4-3a00-4dd4-8de5-5dcdb88422d0/resource) (`a74d79f4-3a00-4dd4-8de5-5dcdb88422d0`)
- S32: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/603970f0-eff2-41d8-8c5d-379028f99304/resource) (`603970f0-eff2-41d8-8c5d-379028f99304`)
- S60: [特种铸造与先进铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf8a2165-c7c2-43cc-b3f2-0af9c6b911dd/resource) (`bf8a2165-c7c2-43cc-b3f2-0af9c6b911dd`)
- S75: [先进镁合金制备与加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1c1f7fe-bcc7-426f-81de-9e9b3173ac82/resource) (`f1c1f7fe-bcc7-426f-81de-9e9b3173ac82`)
- S21: [图5.6b T4热处理后不同成形方式A356铝合金共晶硅的圆度及长径比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4684e60f-4ff2-4467-8c97-6213968de3f7/resource) (`4684e60f-4ff2-4467-8c97-6213968de3f7`)
- S49: [automotive alloys 1999__dbd41f2733](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92d342ae-9fc7-4c3f-b0ae-61062dc6a746/resource) (`92d342ae-9fc7-4c3f-b0ae-61062dc6a746`)
- S66: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d8ade86d-e9dc-4488-90bf-9c8575151574/resource) (`d8ade86d-e9dc-4488-90bf-9c8575151574`)
- S33: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61761755-9306-40df-ab63-6617ede23224/resource) (`61761755-9306-40df-ab63-6617ede23224`)
- S79: [金属精密液态成型技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb796092-c487-48f5-864d-5871779bdfaa/resource) (`fb796092-c487-48f5-864d-5871779bdfaa`)
- S34: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65dd17fb-f4ec-49bc-89d9-e060a486b28e/resource) (`65dd17fb-f4ec-49bc-89d9-e060a486b28e`)
- S6: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1552260a-cef5-4ee1-954e-fe262b246345/resource) (`1552260a-cef5-4ee1-954e-fe262b246345`)
- S1: [半固态镁合金铸轧成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0150603f-606f-4d73-94dc-2c639b5de3d3/resource) (`0150603f-606f-4d73-94dc-2c639b5de3d3`)
- S42: [a study of die design of semi solid die casting according to gate shape__c6840e4468](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7197cb98-3480-46cb-9bac-9246cc0b9fc1/resource) (`7197cb98-3480-46cb-9bac-9246cc0b9fc1`)
- S38: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e4cf684-c14e-4f44-aa97-005b69e6a452/resource) (`6e4cf684-c14e-4f44-aa97-005b69e6a452`)
- S41: [表 14-3 A356 和 A357 合金主要元素含量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ffdf1d1-3eec-4be5-adc4-2efa1b4f6b06/resource) (`6ffdf1d1-3eec-4be5-adc4-2efa1b4f6b06`)
- S18: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b03ba4b-674c-415c-8194-d1cc7bd5856e/resource) (`3b03ba4b-674c-415c-8194-d1cc7bd5856e`)
- S63: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8462a2d-7239-4b63-a8bc-bdaa3f3f3a98/resource) (`c8462a2d-7239-4b63-a8bc-bdaa3f3f3a98`)
- S76: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6892e38-f136-4752-8fd6-9513dd9d51af/resource) (`f6892e38-f136-4752-8fd6-9513dd9d51af`)
- S2: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01bb4240-523b-4046-a5f0-47864eb75111/resource) (`01bb4240-523b-4046-a5f0-47864eb75111`)
- S11: [普通高等教育“十三五”规划教材 特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2bcc5a96-00b8-4266-bf3e-e6828d706152/resource) (`2bcc5a96-00b8-4266-bf3e-e6828d706152`)
- S30: [中国机械工业标准汇编 铸造卷 下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59482905-c963-49b3-a9ca-dce97e368f89/resource) (`59482905-c963-49b3-a9ca-dce97e368f89`)
- S51: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f7ccfbe-2b2c-401d-b742-2ff294e0f103/resource) (`9f7ccfbe-2b2c-401d-b742-2ff294e0f103`)
- S35: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67f69341-4184-447a-8d49-e48c40cad9c0/resource) (`67f69341-4184-447a-8d49-e48c40cad9c0`)
- S67: [ASTM 与 ISO 铝合金及热处理状态等效对照表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/deff5640-2705-446e-8a76-7c4424874b8c/resource) (`deff5640-2705-446e-8a76-7c4424874b8c`)
- S14: [aip conference proceedings authors advances in energy science and enviro__2ca0c84302](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e952d6a-f350-48c2-b032-ee112ceada8a/resource) (`2e952d6a-f350-48c2-b032-ee112ceada8a`)
- S58: [特种铸造与先进铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be05ac6d-2a7c-4230-ba8e-49d60222d726/resource) (`be05ac6d-2a7c-4230-ba8e-49d60222d726`)
- S73: [金属液态成型原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec121209-09eb-44e1-a45c-7e172e42b6ac/resource) (`ec121209-09eb-44e1-a45c-7e172e42b6ac`)
- S59: [材料成形新技术及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf0e3b3d-e34a-4c15-8a96-08e1a99ccfb0/resource) (`bf0e3b3d-e34a-4c15-8a96-08e1a99ccfb0`)
- S77: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7a755fa-2c37-4043-9462-e261fd7af2ff/resource) (`f7a755fa-2c37-4043-9462-e261fd7af2ff`)
- S24: [半固态镁合金铸轧成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50065010-c045-4c9c-b07c-903ab88580b2/resource) (`50065010-c045-4c9c-b07c-903ab88580b2`)
- S72: [半固态镁合金铸轧成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eacaa9c3-eac2-4ba4-99d6-3dee0d69545c/resource) (`eacaa9c3-eac2-4ba4-99d6-3dee0d69545c`)
- S57: [铝硅合金半固态压铸成形产品缺陷的形成机理及控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b51475f9-6fb0-4d08-bb8b-5934ae827b97/resource) (`b51475f9-6fb0-4d08-bb8b-5934ae827b97`)
- S80: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdcae020-14db-43b0-ad11-3b512b70ca88/resource) (`fdcae020-14db-43b0-ad11-3b512b70ca88`)
- S5: [随流半固态流变模锻技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c974621-1041-43c2-946f-c6e9cbc3bce8/resource) (`0c974621-1041-43c2-946f-c6e9cbc3bce8`)
- S44: [半固态金属成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7d070e72-c92c-493a-a0db-2b27761fb337/resource) (`7d070e72-c92c-493a-a0db-2b27761fb337`)
- S53: [金属热塑性成形基础理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a2e67503-0ba2-4393-a897-031acb3c7b2d/resource) (`a2e67503-0ba2-4393-a897-031acb3c7b2d`)
- S65: [9060474_半固态成形](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc6d39e2-72c9-4e68-96b0-44278dbcf9e1/resource) (`cc6d39e2-72c9-4e68-96b0-44278dbcf9e1`)
- S36: [0008_c123fb97521d886c_Semi-solid_metal_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/685cc473-7562-46e5-9e96-bf492c9f15cc/resource) (`685cc473-7562-46e5-9e96-bf492c9f15cc`)
- S43: [0008_c123fb97521d886c_Semi-solid_metal_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79d9c817-222b-4ed9-a4ac-ea004dd175f9/resource) (`79d9c817-222b-4ed9-a4ac-ea004dd175f9`)
- S74: [casting alloy design and characterization__2702a787cd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f18254ff-a6a1-4c3f-9bc2-c37c09440cec/resource) (`f18254ff-a6a1-4c3f-9bc2-c37c09440cec`)
- S56: [铝合金流变挤压铸造成形技术基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b28cc22f-c470-48a6-8d4f-ac1b5e56023e/resource) (`b28cc22f-c470-48a6-8d4f-ac1b5e56023e`)
- S64: [液态模锻与挤压铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb8d8203-24cc-4c9f-a583-5f9a1c1503b1/resource) (`cb8d8203-24cc-4c9f-a583-5f9a1c1503b1`)
- S37: [表 18-1 S. p. A 公司采用触变和流变成形生产发动机支架工艺参数对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6cae044c-e5af-4416-8668-6c1b8c5cd414/resource) (`6cae044c-e5af-4416-8668-6c1b8c5cd414`)
- S45: [金属半固态成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f597d5c-b1dc-4f2a-bee4-95a0447fa031/resource) (`7f597d5c-b1dc-4f2a-bee4-95a0447fa031`)
- S22: [表1.3 触变成形工艺分类; Tab 1.3 Classification of thixoforming process](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/468fa71d-2638-4764-8cc0-5a52263bae61/resource) (`468fa71d-2638-4764-8cc0-5a52263bae61`)
- S15: [effects of die shape and injection conditions proposed with numerical in__3b17a2f483](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30618d4b-4b6f-42c5-8775-3835d883613b/resource) (`30618d4b-4b6f-42c5-8775-3835d883613b`)
- S40: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ff60a63-0b37-4035-8ee1-4b55ef4873f8/resource) (`6ff60a63-0b37-4035-8ee1-4b55ef4873f8`)
- S20: [金属半固态成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46221e7e-27c1-4a52-9eab-f0080ac75a28/resource) (`46221e7e-27c1-4a52-9eab-f0080ac75a28`)
- S39: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f0ad2a2-cb30-4c6a-898f-f6b3a9c1bd61/resource) (`6f0ad2a2-cb30-4c6a-898f-f6b3a9c1bd61`)
- S46: [图4.11 不同成形方式制备A356铝合金力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80abb385-cf04-40e0-9d72-676a25844f40/resource) (`80abb385-cf04-40e0-9d72-676a25844f40`)
- S25: [图4.12不同状态下ZGK521合金力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51f6c9a8-58d2-433e-a19a-2abf4d1a28ac/resource) (`51f6c9a8-58d2-433e-a19a-2abf4d1a28ac`)
- S19: [application of multiphase modelling in semi solid die casting blister pr__0f4c7b64b9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b8ced70-e279-41ea-9ffc-165a45b96004/resource) (`3b8ced70-e279-41ea-9ffc-165a45b96004`)
- S48: [铝合金流变铸造卷入性缺陷及其钝化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/921e300e-9f12-4bcf-8dae-82e2a6432df2/resource) (`921e300e-9f12-4bcf-8dae-82e2a6432df2`)
- S16: [铝合金流变铸造卷入性缺陷及其钝化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/361cca9d-b669-44d2-8fd2-fe107e5395cb/resource) (`361cca9d-b669-44d2-8fd2-fe107e5395cb`)