---
version: "v1"
generated_at: "2026-06-18T18:34:40+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 41
  source_quality_score: 0.88
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

显微维氏硬度（HV0.1）是材料微区力学性能表征的核心参数之一，属于小载荷维氏硬度范畴。其试验力为0.9807 N（100 gf），依据GB/T 4340.1、ISO 6507-1、ASTM E384等标准方法，通过测量金刚石正四棱锥压头在试样表面形成的压痕对角线长度，计算出硬度值[[S12,S25]]。因压痕尺寸极小，HV0.1特别适用于压铸件中不同物相、薄壁区域、表面改性层及微区组织不均匀性的硬度评价[[S43,S9]]。

## 定义与测试原理

HV0.1表示采用0.9807 N试验力进行的显微维氏硬度测定。当试验力保持时间为10～15 s时，无需在符号中标注保持时间；若超出该范围，则需在符号后补充保持秒数（例如450HV0.1/30表示在0.9807 N试验力下保持30 s测得的硬度值为450）[[S12,S25]]。

测试使用两相对面夹角为136°±0.25°的金刚石正四棱锥压头，四个面对压头轴线的倾斜度误差控制在±0.3°以内，顶端横刃长度不大于0.5 μm[[S21,S41]]。在选定的试验力F作用下，压头压入试样表面并保持规定时间，卸除试验力后测量正方形压痕两条对角线d₁、d₂的平均长度d（mm），硬度值按以下公式计算[[S25,S20,S12]]：

- 当试验力单位采用kgf时：**HV = 1.8544 F / d²**
- 当试验力单位采用N时：**HV = 0.1891 F / d²**

试验原理示意如图1所示。

![图1 金属显微维氏硬度试验压入原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9a4298b-5111-4964-882c-2429ce67e28d/resource)

图1展示试验力F作用下，136°金刚石正四棱锥压头压入试样表面，形成压痕后测量对角线长度以计算硬度值[[S51]]。

## 相关标准与试验力范围

显微维氏硬度试验主要依据以下标准：

- **GB/T 4340.1—2012**《金属材料 维氏硬度试验 第1部分：试验方法》（等效采用ISO 6507-1）[[S38]]
- **ISO 6507-1:2018** *Metallic materials — Vickers hardness test — Part 1: Test method*
- **ASTM E384** *Standard Test Method for Microindentation Hardness of Materials*

按照试验力大小，维氏硬度分为三类[[S25,S42]]：

| 类别 | 试验力范围（N） | 典型符号示例 |
|------|----------------|------------|
| 常规维氏硬度 | ≥49.03 | HV5, HV10, HV30 |
| 小负荷维氏硬度 | 1.961～49.03 | HV0.2, HV0.3, HV0.5 |
| 显微维氏硬度 | <1.961 | HV0.01, HV0.05, **HV0.1** |

HV0.1即属于显微维氏硬度范畴，其试验力为0.9807 N（100 gf），推荐用于金属箔、极薄表面层及微观组织组成相的硬度测定[[S25,S42]]。

## 试样要求与最小厚度

HV0.1测试对试样表面质量要求极为严格[[S30,S25]]：

- 试验面必须平整光滑，无氧化皮、外来污物和油污；
- 表面粗糙度Ra不得大于**0.10 μm**（常规维氏硬度要求Ra≤0.40 μm，小负荷维氏硬度要求Ra≤0.20 μm）；
- 制备过程中应尽量减少过热或冷作硬化对表层硬度的干扰，优先采用精细抛光或电解抛光工艺[[S30,S38]]；
- 小截面或异形试样应采用热固性塑料镶嵌或专用夹具固定，必要时可通过轻腐蚀识别目标待测微区相[[S30,S5,S14]]。

试样或待测层的**最小厚度**需满足以下条件[[S25,S11,S49]]：

- 厚度应不小于压痕对角线平均长度的1.5倍；
- 同时不低于压痕深度的10倍（HV0.1压痕深度约为对角线长度的1/7）[[S44]]；
- 测试后试样背面不得出现可见变形痕迹。

图2为试样最小厚度列线图，可针对HV0.01～HV100范围内的硬度值和选定的试验力，直接查出符合要求的试样最小厚度。图中标注了HV0.1对应的0.9807 N试验力档位，适用于压铸薄层、表面改性层的试样厚度校核[[S34]]。

![图2 维氏硬度试样最小厚度图（HV0.01～HV100）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2bdabea-f848-4219-9fb5-b694959aa049/resource)

## 压痕测量精度与试验要点

HV0.1属于低载荷显微硬度测试，压痕尺寸极小，对角线测量系统的精度要求为±0.5%[[S40,S13]]。不同硬度范围对应的测试重复性阈值如下[[S8]]：

| 硬度范围 | 机器重复性要求 |
|---------|--------------|
| 100～240 HV | ≤6% |
| ≥650 HV | ≤3% |

由于低载荷下相同的对角线测量误差会导致更大的硬度计算偏差，HV0.1测试结果的离散性高于大载荷维氏硬度。根据ASTM相关数据，其同实验室重复性和跨实验室再现性限值明显高于更高载荷的试验[[S24,S47]]。

试验时需遵守以下压痕间距要求[[S13,S29,S10]]：

- 相邻两压痕的中心距不小于2.5倍压痕对角线长度；
- 压痕中心与试样边缘距离不小于2.5倍压痕对角线长度（轻金属为3倍）；
- 压痕应避开孔隙、夹杂物等缺陷，单个测点硬度与周边点差值超过2倍时该点应舍弃重测[[S13,S36]]。

## 在压铸中的应用

### 微区相硬度鉴别

HV0.1可针对压铸件不同物相区进行针对性硬度测试，区分基体相、共晶相及金属间化合物相的硬度差异。例如，铝合金中常见的FeAl₃相显微维氏硬度可达960 HV，Si相可达1320 HV，通过HV0.1可直接测得这些高硬强化相的硬度值，进而反映合金强化相的分布特征[[S43,S23]]。

### 薄壁区域与壁厚效应表征

HV0.1压痕尺寸极小，适合表征厚度不足1 mm的压铸薄壁部位硬度，不受常规大载荷压痕穿透效应的影响。实测ADC12压铸件薄壁区域平均硬度为99.1 HV，厚壁区域平均为96.9 HV，薄壁比厚壁高出约2.2 HV，这与薄壁处更快的冷却速率导致的晶粒细化效应直接相关[[S9]]。因此HV0.1可用于识别铸件不同壁厚位置的硬度梯度，间接反映冷却速率分布。

### 表面改性层硬度检测

HV0.1能准确测量极薄的渗层、镀层或表面强化层的硬度分布，不会因压痕穿透改性层接触基体而影响测试结果[[S43]]。

### 组织不均匀性评价

通过HV0.1多点分布测试，可直接反映压铸件的组织不均匀性，识别不同充型路径位置的硬度差异。例如，A360压铸冷却盖板不同流线点位的HV0.1值存在明显差异，工艺优化前各点硬度分布于90.85～95.42 HV之间，优化后提升至95.68～105.72 HV，表明组织均匀性随工艺改善而提高[[S19,S32]]。

## 典型压铸合金的HV0.1范围

以下为常见压铸合金在铸态下的HV0.1实测或参考范围：

| 合金牌号 | 铸态HV0.1范围 | 说明 | 来源 |
|---------|-------------|------|------|
| ADC12 | 92.8～99 HV（平均96.7 HV） | 压铸水泵座实测，最低硬度≥85 HV符合工业要求 | [[S4,S35,S9]] |
| A360（A380系列） | 90.85～105.72 HV | 工艺优化前90.85～95.42 HV，优化后95.68～105.72 HV | [[S19,S32]] |
| AZ91D | 平均约84 HV（高压压铸） | 相比树脂模铸造（102 HV）硬度较低 | [[S28]] |
| AZ91-0.5Ce | 61.6～65.3 HV | 随浇注温度升高先增后降，675℃时达峰值 | [[S39]] |
| Zamak 3（锌合金） | 93～102 HV（参考） | 由97 HB换算近似区间，非直接HV0.1实测 | [[S48,S18]] |

注意：仅在相同试验力条件下，维氏硬度值可直接进行精确比较。不同载荷下的硬度值换算需通过对应材料的对比试验建立专属校正关系，不存在通用的HV0.1与宏观维氏硬度跨力值精确换算方法[[S12,S10,S52]]。

## 工艺参数对HV0.1的影响

### 冷却速率与壁厚效应

冷却速率与HV0.1呈正相关。薄壁区域冷却速率远高于厚壁区域，对应更细小的晶粒组织，实测薄壁区HV0.1比厚壁区可高出约2～6 HV。冷却速率更高的铸件无明显大尺寸晶粒和粗大第二相，硬度均匀性更好[[S46,S9]]。

### 压力与晶粒细化

热室压铸的方差分析表明，第二相增压压力对铸件维氏硬度的贡献占比高达82.48%，远高于开模时间（9.24%）和金属浇注温度（6.78%），是影响整体硬度水平的核心工艺参数。压力提升可细化晶粒、减少缩孔缺陷，显著提升HV0.1测试值[[S17]]。

### 晶粒尺寸关系

根据Hall-Petch定律，压铸件显微维氏硬度与晶粒尺寸呈反比关系。工艺优化（如改善充型、调整增压压力）后晶粒细化，可直接提升铸件整体HV0.1水平。A360冷却盖板工艺优化后平均晶粒尺寸由最大13.12 μm降至12.79 μm，相应HV0.1最低值由90.85 HV提升至95.68 HV[[S19,S32]]。

## 与其他硬度测试方法的对比

压铸场景下不同硬度测试方法的适用范围对比如下[[S50,S26,S45]]：

| 硬度方法 | 压头类型 | 特点与适用场景 | 局限性 |
|---------|---------|--------------|--------|
| 布氏硬度（HB） | 硬质合金球 | 压痕面积大，适合整体基体平均硬度检测，可关联抗拉强度 | 不适用于薄小件和微区测量 |
| 洛氏硬度（HR） | 金刚石圆锥/淬火钢球 | 操作简便、直接读数，适合大批量压铸成品快速检测 | 不适合微区、极薄渗层测量 |
| 显微维氏硬度（HV0.1） | 136°金刚石正四棱锥 | 适合微区、析出相、偏析相、薄层改性层的硬度表征，是压铸微观组织力学性能表征的核心方法 | 测试效率较低，对表面制备要求高 |
| 努氏硬度（HK） | 细长菱形金刚石压头 | 压入深度仅为HV0.1的约65%，更适合极薄脆性镀层硬度测试 | 在各向异性小的压铸铝合金微区测试中，维氏正方形压痕的两对角线测量一致性更好，通用性更强 |

努氏硬度的压痕长对角线长度约为维氏硬度的2.8倍，而压入深度仅为其65%，因此在测量极薄镀层时具有优势[[S44]]；但对于各向异性较小的压铸铝合金微区，维氏压痕的两条对角线测量一致性更好，操作更便捷[[S6]]。

## 局限性及注意事项

- **数据分散性**：低载荷下压痕尺寸小，相同对角线测量误差导致更大的硬度偏差，HV0.1测试结果的分散性明显高于大载荷维氏硬度[[S24,S47]]。
- **表面制备依赖性**：表面粗糙度、冷作硬化层、抛光损伤等均会影响HV0.1结果，制备过程需严格控制[[S30,S38]]。
- **无通用换算关系**：仅在相同试验力条件下方可直接比较硬度值；HV0.1与布氏、洛氏、抗拉强度之间不存在通用换算方法，所有转换需基于特定材料的对比试验建立[[S12,S10,S52]]。
- **压痕避开缺陷**：测试时必须避开可见缺陷或孔隙，否则结果无效且可能导致数据失真[[S13,S36]]。
- **均匀材料力值一致性**：在硬度不超过450 HV的均匀材料中，不同载荷下的维氏硬度值基本一致；但HV0.1所测微区常涉及组织非均匀性，因此力值对结果的影响需要谨慎对待[[S12,S43]]。

## Sources
- S12: [最新铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fdfc306-977d-4bca-a9e8-520a433cd2b9/resource) (`3fdfc306-977d-4bca-a9e8-520a433cd2b9`)
- S25: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/85197c46-c4da-4bc4-ac85-f22d532098f0/resource) (`85197c46-c4da-4bc4-ac85-f22d532098f0`)
- S43: [工程材料与热加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df163a39-7c63-45b1-a7dc-7ef1f1b70f38/resource) (`df163a39-7c63-45b1-a7dc-7ef1f1b70f38`)
- S9: [图5-31 A、B区域不同位置处的显微硬度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d0b5fe8-df9e-4848-9c46-f79a7b0c4663/resource) (`2d0b5fe8-df9e-4848-9c46-f79a7b0c4663`)
- S21: [表面处理技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ca4d77b-41bb-4144-87d9-74ac53e7ddf2/resource) (`6ca4d77b-41bb-4144-87d9-74ac53e7ddf2`)
- S41: [0271_236026785bf23cf9_材料硬度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccbc0c9f-9748-4e84-97c8-71d6b724e4d7/resource) (`ccbc0c9f-9748-4e84-97c8-71d6b724e4d7`)
- S20: [材料工艺学机械工程材料与热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bfec21d-7a5c-48e4-bb11-0c0f4c19dfa8/resource) (`6bfec21d-7a5c-48e4-bb11-0c0f4c19dfa8`)
- S51: [金属显微维氏硬度试验压入原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9a4298b-5111-4964-882c-2429ce67e28d/resource) (`f9a4298b-5111-4964-882c-2429ce67e28d`)
- S38: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc6e7943-bf37-4f91-9d5c-9c87441c9902/resource) (`bc6e7943-bf37-4f91-9d5c-9c87441c9902`)
- S42: [表 36-5 维氏硬度实验应选用的实验力](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d60baa25-470c-4a73-bb91-58e1247dab0a/resource) (`d60baa25-470c-4a73-bb91-58e1247dab0a`)
- S30: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4e629c9-a6af-44f8-b89c-b4bd441bc50f/resource) (`a4e629c9-a6af-44f8-b89c-b4bd441bc50f`)
- S5: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14942d76-f7fe-42fa-bc50-71384b72dd66/resource) (`14942d76-f7fe-42fa-bc50-71384b72dd66`)
- S14: [粉末冶金模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44ee53b5-4807-4533-8240-e3f82991aaf2/resource) (`44ee53b5-4807-4533-8240-e3f82991aaf2`)
- S11: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ee3ccc8-f592-4665-84eb-5205dbbd2627/resource) (`3ee3ccc8-f592-4665-84eb-5205dbbd2627`)
- S49: [简明铝合金手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f722c96e-047b-4749-9877-d6311a4c4723/resource) (`f722c96e-047b-4749-9877-d6311a4c4723`)
- S44: [表面沉积技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e241d4d9-04be-4a93-a212-885ebd87e1fb/resource) (`e241d4d9-04be-4a93-a212-885ebd87e1fb`)
- S34: [试样最小厚度图（HV0.01～HV100）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2bdabea-f848-4219-9fb5-b694959aa049/resource) (`b2bdabea-f848-4219-9fb5-b694959aa049`)
- S40: [粉末冶金模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5ea6c67-7c35-4f04-9d73-3968c288a70c/resource) (`c5ea6c67-7c35-4f04-9d73-3968c288a70c`)
- S13: [粉末冶金模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40ab49b1-a2d8-47ff-935a-41bc1193e1df/resource) (`40ab49b1-a2d8-47ff-935a-41bc1193e1df`)
- S8: [标准化测试块硬度范围与机器重复性要求](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27eda1e5-50a1-48a2-b2f3-3a7ea9ba9cac/resource) (`27eda1e5-50a1-48a2-b2f3-3a7ea9ba9cac`)
- S24: [1991 annual book of astm standards section 2 nonferrous metal products v__3abfaf437d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80eda0b9-9ad7-4511-8e7f-9cdd6bfca1d9/resource) (`80eda0b9-9ad7-4511-8e7f-9cdd6bfca1d9`)
- S47: [粉末冶金模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f56a707d-b06e-4f29-b952-7649863fccd7/resource) (`f56a707d-b06e-4f29-b952-7649863fccd7`)
- S29: [粉末冶金模具设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4989395-6f8f-4b4b-b813-bfa6a0ec01d5/resource) (`a4989395-6f8f-4b4b-b813-bfa6a0ec01d5`)
- S10: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30253050-091f-43a1-b9c1-42076fd0de3e/resource) (`30253050-091f-43a1-b9c1-42076fd0de3e`)
- S36: [1991 annual book of astm standards section 2 nonferrous metal products v__3abfaf437d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8136339-5126-4f3e-9632-dc8fc8ef506c/resource) (`b8136339-5126-4f3e-9632-dc8fc8ef506c`)
- S23: [表 14-7 金属间化合物及其显微维氏硬度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71b6c8c9-88f3-4119-ac88-365b66cd79ab/resource) (`71b6c8c9-88f3-4119-ac88-365b66cd79ab`)
- S19: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62b035e4-e374-42be-b4df-8eedc16945df/resource) (`62b035e4-e374-42be-b4df-8eedc16945df`)
- S32: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/adb10828-a4fa-47c9-af67-4c17325c5062/resource) (`adb10828-a4fa-47c9-af67-4c17325c5062`)
- S4: [铝合金水泵座压铸模镶块冷却水道结构改进与压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/142c94a8-0012-4539-91a1-b7a776bec821/resource) (`142c94a8-0012-4539-91a1-b7a776bec821`)
- S35: [表5.1 显微硬度实验数据表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b74f15e0-7aba-46e3-9fe1-9e23f7cd8118/resource) (`b74f15e0-7aba-46e3-9fe1-9e23f7cd8118`)
- S28: [AZ91D合金RM与HPDC工艺的硬度测试对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a37d40f8-3019-4269-8e9d-129e6960a73d/resource) (`a37d40f8-3019-4269-8e9d-129e6960a73d`)
- S39: [图5.7不同浇注温度下压铸AZ91-0.5Ce合金的硬度影响曲线图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be9e4770-db76-47c7-9e70-214eb419cfee/resource) (`be9e4770-db76-47c7-9e70-214eb419cfee`)
- S48: [0023_1723c0e84400287c_Zamak](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5b6764e-2a6c-4500-88e9-8d33e727fcb7/resource) (`f5b6764e-2a6c-4500-88e9-8d33e727fcb7`)
- S18: [0023_1723c0e84400287c_Zamak](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ba33081-5841-4639-997e-8952e2c7c508/resource) (`5ba33081-5841-4639-997e-8952e2c7c508`)
- S52: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcbf84b3-9cd6-424d-bb06-9bf4fe3a6cd6/resource) (`fcbf84b3-9cd6-424d-bb06-9bf4fe3a6cd6`)
- S46: [casting and forming of light alloys__9032155482](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f10a2956-bc6f-4af1-8703-78de3d027558/resource) (`f10a2956-bc6f-4af1-8703-78de3d027558`)
- S17: [effect of some parameters on the cast component properties in hot chambe__f90849e697](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57b1554c-9526-4f8f-a9a0-1e59a0636e70/resource) (`57b1554c-9526-4f8f-a9a0-1e59a0636e70`)
- S50: [工程材料及热成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7cfa12e-0185-4a00-a70f-237d58f5e979/resource) (`f7cfa12e-0185-4a00-a70f-237d58f5e979`)
- S26: [工程材料及加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c8139cf-b983-4121-9ca8-dfaa75b0c82d/resource) (`8c8139cf-b983-4121-9ca8-dfaa75b0c82d`)
- S45: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecdf7a69-732e-41cf-abe5-057acf26534a/resource) (`ecdf7a69-732e-41cf-abe5-057acf26534a`)
- S6: [中国轻工业标准汇编日用五金卷上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22808556-c790-43f8-9626-7fb7c538de61/resource) (`22808556-c790-43f8-9626-7fb7c538de61`)