---
version: "v1"
generated_at: "2026-06-18T14:35:36+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 33
  source_quality_score: 0.86
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述

应变诱导熔化活化技术（Strain-Induced Melt Activation，SIMA），又称应变诱发熔体激活法、新SIMA法，是一种固相类半固态坯料成熟制备工艺[[S16]]。该技术由Young于1987年首次提出并获专利[[S1,S18,S29]]，属于半固态金属坯料制备领域的高固相分数制浆方法，对高熔点合金如不锈钢、工具钢、铜合金等具有独特适配性[[S5,S16]]。

SIMA法的核心原理是通过机械储能调控相变实现显微组织重构：将常规铸锭经预变形破碎枝晶、储存应变能，再加热至固液两相区间保温，经动态再结晶与部分熔化后获得球状初生相的高固相分数半固态浆料[[S1,S22,S27]]。该方法具备浆料纯净无额外污染、无需添加细化剂、设备兼容性强、固相分数可控的优势[[S1,S16]]。然而，传统SIMA法存在坯料尺寸受限（仅适配直径小于37 mm的坯料）、预变形工序能耗高、工艺窗口窄等局限性[[S5,S17,S29]]。

![SIMA工艺示意图，展示铸造、热挤压、盐浴淬火阶段的温度-时间变化路径（标注RT、Tr、Ts、Tl关键温度节点）及对应微观组织演变过程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46b7ebe0-bd1f-4705-8e97-9e85042dd6ee/resource)[[S7]]

## 定义与原理

### 英文术语

- Strain-Induced Melt Activation (SIMA)
- Strain-Induced Melt Activation Process
- Stress Induced Melt Action（见部分早期文献）[[S13]]

### 核心机理

SIMA工艺的机理可从动力学层面拆解为两阶段过程[[S1]]：

1. **应变诱发阶段**：对铸态合金实施预变形（如挤压、锻造、轧制），使铸造态的粗大枝晶组织破碎，并在材料内部储存应变能；
2. **熔体激活阶段**：将变形后的坯料加热至固相线与液相线之间的半固态温度区间进行等温保温。升温过程中，首先由存储的应变能驱动动态再结晶，形成细小亚晶粒和亚晶界；随后，在界面能主导下，通过熟化作用使晶粒演变为球状或近球状形态，最终获得组织均匀、晶粒细小的球状非枝晶半固态坯料[[S1,S27,S9]]。

部分文献描述为：熔化的液相首先渗入小角度晶界，使枝晶侧枝熔断而成为初生球状晶粒[[S12,S16]]。该工艺无需额外添加晶粒细化剂即可实现组织重构[[S1]]。

### 传统SIMA与新SIMA法的差异

传统SIMA法的完整流程为：在再结晶温度区间对铸态坯料进行热变形破碎枝晶→补充冷变形工序以储存充足应变能→快速加热至半固态区间保温完成再结晶与部分熔化[[S29,S9,S14]]。该方法的局限性在于对低塑性材料（如密排六方结构的镁合金，仅3个滑移系，铸态伸长率仅约1%）难以实现大变形量，应变储能不足导致晶粒细化和球化效果差，且制备流程长、能耗高、坯料尺寸受限[[S38,S9]]。

新SIMA法由哈尔滨工业大学罗守靖、姜巨福团队针对低塑性镁合金开发[[S35,S41]]，核心改进为将传统冷变形替换为等径道角挤压（ECAE，亦称ECAP）等剧烈塑性变形工艺。通过多道次挤压可在低塑性合金中引入大应变，实现晶粒大幅细化，制备得到的半固态坯料中固相颗粒显著细化、球化程度高[[S35,S41]]。

## 工艺步骤与参数

传统SIMA法分为两大核心阶段[[S27,S14]]：
- **第一阶段（应变诱发预变形）**：在再结晶温度范围内对铸态坯料通过锻造、轧制、挤压等方式实施大变形，破碎粗大枝晶组织并储存内部应变能；
- **第二阶段（熔体激活半固态等温处理）**：将变形后坯料加热至固-液相线之间的半固态温度区间等温保温，驱动细小晶粒通过熟化作用演变为球状或近球状组织。

预变形可分为热变形与冷变形两类：传统完整工艺先后实施高温大变形热加工+室温小变形冷加工两个工序；简化型工艺可省略冷变形环节，仅在再结晶温度以上直接实施大应变热加工后进入半固态重熔工序[[S9,S5,S41]]。

![SIMA法典型工艺流程图，展示金属材料冷变形→加热至半固态区→再结晶→部分熔化→初生相转变成颗粒→半固态金属坯料的全流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/135524ce-6bac-41b0-8a67-28f730f231f1/resource)[[S2]]

### 预变形处理典型参数

| 工艺类型 | 预变形方式 | 典型工艺参数 | 适用材料 | 来源 |
|---------|-----------|-------------|---------|------|
| 传统SIMA | 热挤压/锻造+冷变形 | 再结晶温度区间热变形+室温冷变形 | 铝合金、不锈钢、铜合金 | [[S29,S5]] |
| 新SIMA | 等径道角挤压（ECAE） | AZ91D：坯料加热温度300℃，模具预热温度300℃，连续挤压4道次，每道次后坯料沿同一方向旋转90°，通道交角90° | AZ91D镁合金 | [[S35,S38]] |

### 半固态等温处理典型参数

| 合金体系 | 工艺类型 | 保温温度 | 保温时间 | 关键观察 | 来源 |
|---------|---------|---------|---------|---------|------|
| 7075铝合金 | 传统SIMA | 600℃（球化起始温度） | — | 起始球化温度高于RAP | [[S1,S41]] |
| 7075铝合金 | RAP | 590℃（球化起始温度） | — | 球化温度更低，球化效果更显著，但晶粒更粗大 | [[S1,S41]] |
| AZ80镁合金 | 新SIMA | 530~560℃ | — | 随等温温度升高，固相分数降低，粗化和球化速率提高 | [[S41]] |
| AZ91D镁合金 | 新SIMA | 530~545℃ | 20 min（峰值） | 保温＜14 min时伸长率未达峰值，＞26 min后晶粒粗化导致下降 | [[S3,S15]] |

### 适用合金体系

SIMA法已成功工业化应用的合金体系包括[[S16,S5,S24]]：
- 铸造铝合金
- 变形铝合金（涵盖2017、A356、A2618、7075等牌号）
- 镁合金（以AZ系列为主）
- 不锈钢
- 工具钢
- 铜合金

制备获得的非枝晶组织合金晶粒尺寸可达到约20 μm[[S5,S16]]。

![SIMA法组织演变显微图，展示预变形后破碎的枝晶在半固态等温重熔阶段逐步球化的过渡状态，标尺20μm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8b042f8-531d-4a61-936b-90c50eb7259b/resource)[[S25]]

## 工艺优势与局限性

### 核心优势

1. **浆料纯净度高**：无额外熔炼工序，可减少合金氧化现象，无搅拌工具带来的熔体污染[[S12,S13,S26]]；
2. **无需添加晶粒细化剂**：通过预变形引入的应变能驱动再结晶即可实现组织细化[[S1]]；
3. **设备兼容性强**：可利用常规热机械加工设备（挤压机、轧机等）[[S1]]；
4. **固相分数可控**：可通过温度参数调节固相分数[[S1]]；
5. **适用于高熔点合金**：对不锈钢、工具钢、铜合金等常规搅拌法难以高效制备高固相分数半固态浆料的合金具有独特优势[[S5,S12,S21]]；
6. **组织均匀细化**：非枝晶组织晶粒尺寸可达到约20 μm[[S5,S16]]；
7. **生产效率高**，适用于工业化生产[[S26]]。

### 局限性

1. **坯料尺寸受限**：仅适配直径小于37 mm的坯料，不适用于大规格半固态构件的批量制备[[S5,S17]]；
2. **预变形工序成本高**：需要额外增加大变形量工序，ECAE、多向锻造等预变形工艺成本高、生产效率低[[S5,S13,S41]]；
3. **工艺复杂度高**：流程长、能耗高，需至少两次加热处理，整体复杂度高于搅拌类制浆方法[[S29,S27,S26]]；
4. **对低塑性材料实施困难**：传统镦粗类大变形工艺对密排六方结构镁合金难以实施[[S38]]。

### 与其他半固态制浆工艺对比

| 对比维度 | SIMA法（应变诱发熔体激活法） | 机械搅拌法 | 电磁搅拌法 |
|---------|---------------------------|-----------|-----------|
| **作用原理** | 预变形储存应变能+半固态等温再结晶球化 | 搅拌棒直接破碎枝晶 | 旋转电磁场驱动熔体对流剪切 |
| **熔体污染** | 无（固相法，不接触搅拌器） | 显著（搅拌棒腐蚀、卷入气体夹杂） | 小（非接触式，气体卷入少） |
| **组织均匀性** | 均匀，球化程度高 | 存在搅拌死区，易出现蔷薇状晶 | 横断面不均：表层细小枝晶，心部球化 |
| **坯料尺寸** | 仅小尺寸（＜37 mm直径） | 中等 | 受集肤效应限制（通常≤150 mm直径） |
| **生产效率** | 高（适用于工业化） | 低 | 中等 |
| **设备投资** | 中（利用常规热加工设备） | 低 | 高（电磁装置功率大、能耗高） |
| **适用范围** | 高/低熔点合金广谱适配，对高熔点合金独特优势 | 多为低熔点合金 | 工业应用广泛，但仅适配特定合金 |
| **主要缺陷风险** | 液相偏析风险 | 熔体污染、气孔 | 表层枝晶组织 |
| **综合工艺复杂度** | 高（多道次变形+加热） | 简单 | 工艺参数可调范围宽 |

综合自[[S12,S5,S11,S13,S26,S31,S32,S36]]。

## 分类与演变

### 三类主要工艺变体

| 工艺名称 | 提出者/团队 | 核心特征 | 与传统SIMA的区别 | 局限性 | 来源 |
|---------|------------|---------|-----------------|--------|------|
| **传统SIMA** | Young (1987) | 再结晶温度区间热变形+冷变形+半固态等温处理 | — | 低塑性材料大变形困难，流程长，能耗高 | [[S29,S9]] |
| **新SIMA法** | 哈工大罗守靖、姜巨福团队 | 以等径道角挤压（ECAE）替代传统冷变形，多道次剧烈塑性变形引入大应变 | 坯料尺寸可至φ58×120 mm，晶粒细化显著，触变成形后力学性能大幅提升 | ECAE等预变形工序成本高、效率低，限制大规模产业化 | [[S35,S41,S38]] |
| **RAP（再结晶部分熔化法）** | 谢菲尔德大学D.H.Kirkwood团队 | 在亚再结晶温度以下实施温变形，仅需单次变形工序，流程更短、能耗更低 | 起始球化温度更低（7075铝合金为590℃ vs SIMA 600℃），球化效率更高；仅需一次塑性变形处理 | 最终晶粒尺寸相比常规SIMA更粗大 | [[S1,S27,S41]] |

三者本质上均属于SIMA法体系的工艺改良[[S41]]。RAP的优势在于简化工艺流程（仅需一次变形处理），适用于Cr-V-Mo钢、SKD61等高熔点合金[[S27]]。新SIMA法的优势在于对低塑性合金（尤其镁合金）的适应能力更强，触变成形后的力学性能显著提升[[S35,S6]]。

### 新SIMA法力学性能提升量化对比

新SIMA法制备的AZ91D镁合金半固态坯料成形制件相对于传统SIMA法制备制件的力学性能提升幅度[[S42,S28,S6,S33]]：

| 性能指标 | 提升幅度范围 | 各试件具体提升幅度 | 来源 |
|---------|------------|------------------|------|
| 室温抗拉强度 | 最高提高128% | 1号：76%；2号：91%；3号：73%；4号：128% | [[S6,S42]] |
| 室温伸长率 | 最高提高343% | 1号：343%；2号：178%；3号：334%；4号：271% | [[S6,S28]] |
| 100℃高温抗拉强度 | 最高提高74.3% | 1号：38.4%；2号：37.3%；3号：74.3%；4号：31.8% | [[S33]] |
| 150℃高温抗拉强度 | 最高提高87.5% | 1号：87.5%；2号：56.4%；3号：55.6%；4号：70.1% | [[S33]] |

![传统SIMA与新SIMA法制备的半固态坯触变模锻制件在100℃下的抗拉强度对比柱状图，新SIMA组强度显著高于传统SIMA组](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a858e4e2-6536-4cba-845f-f8f9b438e0c1/resource)[[S23]]

## 应用领域

SIMA法制备的半固态坯料主要应用于触变成形（Thixoforming）工艺，包括[[S21,S3]]：
- 触变压铸
- 触变模锻（触变锻造）
- 触变挤压

### 典型商业化零件案例

**AZ91D镁合金托弹板**：采用新SIMA法制备的半固态坯料经触变模锻成形，工艺参数为坯料加热温度530~545℃、保温20 min、模具温度400~450℃、保压时间90 s[[S3,S6]]。成形后微观组织晶粒最大尺寸小于50 μm，整体组织均匀，无明显固液分离现象[[S3]]。新SIMA法制备的坯料成形后抗拉强度较传统SIMA法提升最高可达128%，伸长率最高提升271%[[S6]]。

美国Alumax公司已利用该专利技术生产部分军用航天零部件[[S29,S14]]。

![新SIMA法制备的AZ91D镁合金半固态坯料微观组织，晶粒细小、圆整、分布均匀，标尺50μm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cf7149a-61be-419a-acf3-19819f96adf7/resource)[[S20]]

## 相关工艺概念关系

- **触变成形（Thixoforming）**：将SIMA法等制备的半固态坯料先冷却凝固，再根据产品尺寸下料，重新加热至半固态温度后进行成形加工，是目前生产条件下的主导工艺路径[[S21]]。
- **流变成形（Rheoforming）**：将搅拌获得的半固态金属浆料在保持半固态温度的条件下直接进行成形加工，与触变成形并列为半固态加工的两条主要技术路线[[S21]]。
- **再结晶部分熔化法（RAP）**：属于SIMA体系改良工艺，降低预变形温度至亚再结晶温度以下，流程更短[[S27,S41]]。
- **电磁搅拌法（MHD）**：非接触式半固态制浆主要方法，工业应用广泛，与SIMA法在制浆路径上属于搅拌法与非搅拌法两大类别[[S13,S31]]。

## Sources
- S16: [半固态镁合金铸轧成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6399c809-1ba1-48de-a8eb-eac765f8d55a/resource) (`6399c809-1ba1-48de-a8eb-eac765f8d55a`)
- S1: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/005723b3-2b70-465c-8158-3b90db14f995/resource) (`005723b3-2b70-465c-8158-3b90db14f995`)
- S18: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69b117b2-435e-494d-8400-ab767d112ad8/resource) (`69b117b2-435e-494d-8400-ab767d112ad8`)
- S29: [金属半固态成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b99ea0b0-e682-45d1-972d-cd57d4aec5cb/resource) (`b99ea0b0-e682-45d1-972d-cd57d4aec5cb`)
- S5: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d91e72d-7786-430f-b45d-f54a3848b536/resource) (`3d91e72d-7786-430f-b45d-f54a3848b536`)
- S22: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3377c6a-7afe-4935-abdc-e2a9c55efbee/resource) (`a3377c6a-7afe-4935-abdc-e2a9c55efbee`)
- S27: [随流半固态流变模锻技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b46157ce-38e1-4e4e-9b49-c78a923d8ed4/resource) (`b46157ce-38e1-4e4e-9b49-c78a923d8ed4`)
- S17: [0008_c123fb97521d886c_Semi-solid_metal_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/685cc473-7562-46e5-9e96-bf492c9f15cc/resource) (`685cc473-7562-46e5-9e96-bf492c9f15cc`)
- S7: [图1-7 SIMA工艺示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46b7ebe0-bd1f-4705-8e97-9e85042dd6ee/resource) (`46b7ebe0-bd1f-4705-8e97-9e85042dd6ee`)
- S13: [倾转-振动法制备半固态浆料及微观组织的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56ed11f1-3164-446a-aa66-1dd7e674927e/resource) (`56ed11f1-3164-446a-aa66-1dd7e674927e`)
- S9: [液态模锻与挤压铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4835040f-959a-4050-9d91-9dcf0ed05334/resource) (`4835040f-959a-4050-9d91-9dcf0ed05334`)
- S12: [半固态镁合金铸轧成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50065010-c045-4c9c-b07c-903ab88580b2/resource) (`50065010-c045-4c9c-b07c-903ab88580b2`)
- S14: [金属液态成型原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b12b587-959a-47c7-b8e6-2b5266209497/resource) (`5b12b587-959a-47c7-b8e6-2b5266209497`)
- S38: [TextNode116](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e216e151-ced6-4f35-af99-db8375f1a1bc/resource) (`e216e151-ced6-4f35-af99-db8375f1a1bc`)
- S35: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c97fb34b-74de-4223-92b9-0d6d7f8cba39/resource) (`c97fb34b-74de-4223-92b9-0d6d7f8cba39`)
- S41: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc56766e-e057-4445-96bf-bf98117ed9eb/resource) (`fc56766e-e057-4445-96bf-bf98117ed9eb`)
- S2: [应变诱导熔化激活法（SIMA）工艺过程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/135524ce-6bac-41b0-8a67-28f730f231f1/resource) (`135524ce-6bac-41b0-8a67-28f730f231f1`)
- S3: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1794b91c-6f37-474b-b28d-ba8e9ec55da2/resource) (`1794b91c-6f37-474b-b28d-ba8e9ec55da2`)
- S15: [图4-54 不同保温时间条件下的托弹板伸长率](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c5d88d9-c595-4d69-9439-d29a10ec2b54/resource) (`5c5d88d9-c595-4d69-9439-d29a10ec2b54`)
- S24: [表1.1 常见的铝合金半固态金属升温制备方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a89a31bb-281b-473b-9e5c-9790ed9c05bb/resource) (`a89a31bb-281b-473b-9e5c-9790ed9c05bb`)
- S25: [图3-28 SIMA法组织演变示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8b042f8-531d-4a61-936b-90c50eb7259b/resource) (`a8b042f8-531d-4a61-936b-90c50eb7259b`)
- S26: [表1.4 半固态浆料的制备工艺及优缺点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aedf3c0a-46cb-4b1f-83fb-f574815611f5/resource) (`aedf3c0a-46cb-4b1f-83fb-f574815611f5`)
- S21: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f0dca5b-98ff-44bc-b5f9-1547fe5c8c6a/resource) (`8f0dca5b-98ff-44bc-b5f9-1547fe5c8c6a`)
- S11: [材料成形新技术及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e53bf02-1785-4bfa-a207-ca58223bd10e/resource) (`4e53bf02-1785-4bfa-a207-ca58223bd10e`)
- S31: [特种铸造与先进铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be05ac6d-2a7c-4230-ba8e-49d60222d726/resource) (`be05ac6d-2a7c-4230-ba8e-49d60222d726`)
- S32: [材料成形新技术及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf0e3b3d-e34a-4c15-8a96-08e1a99ccfb0/resource) (`bf0e3b3d-e34a-4c15-8a96-08e1a99ccfb0`)
- S36: [22226491_电磁搅拌法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ca79184d-5dc9-46aa-b23d-fca8795c359f/resource) (`ca79184d-5dc9-46aa-b23d-fca8795c359f`)
- S6: [TextNode117](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40ed7ffd-69cb-47b7-badb-8b567c058a73/resource) (`40ed7ffd-69cb-47b7-badb-8b567c058a73`)
- S42: [图4-55 不同方法制备的半固态坏成形制件的抗拉强度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff194eb2-e08a-40b6-8d26-f48957ba46aa/resource) (`ff194eb2-e08a-40b6-8d26-f48957ba46aa`)
- S28: [图4-56 不同方法制备的半固态坏成形托弹板的伸长率](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6b567f8-c107-438a-926f-4772e6f562f4/resource) (`b6b567f8-c107-438a-926f-4772e6f562f4`)
- S33: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c35a33df-2974-43f0-afe4-d976ad30a452/resource) (`c35a33df-2974-43f0-afe4-d976ad30a452`)
- S23: [图4-57 不同方法制备的半固态坏成形托弹板在100℃时的抗拉强度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a858e4e2-6536-4cba-845f-f8f9b438e0c1/resource) (`a858e4e2-6536-4cba-845f-f8f9b438e0c1`)
- S20: [图14-9(c) 新SIMA制备的AZ91D镁合金半固态坏料微观组织](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cf7149a-61be-419a-acf3-19819f96adf7/resource) (`8cf7149a-61be-419a-acf3-19819f96adf7`)