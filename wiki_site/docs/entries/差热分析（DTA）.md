---
version: "v1"
generated_at: "2026-06-18T10:21:47+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.86
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

差热分析（Differential Thermal Analysis, DTA）是一种在程序控制温度条件下，测量待测物质与参比物之间的温度差随温度或时间变化的热分析技术[[S9,S38]]。该技术诞生于20世纪50年代末，是热分析领域的核心非等温量热方法之一[[S2]]。在压铸领域中，DTA主要用于测定合金的熔化与凝固特性，包括液相线温度、固相线温度、凝固区间以及过冷度等关键热物性参数，为压铸工艺参数的制定提供科学依据[[S21,S29]]。

## 定义与基本原理

### 定义

按照1977年第五届国际热分析协会（ICTA）的规定，差热分析属于热分析大类，是在程序控制温度下，测量物质的物理性质随温度变化的一类技术。DTA通过记录样品与参比物之间的温差随温度或时间的变化关系，捕捉样品在加热或冷却过程中伴随的物理化学变化所产生的热效应[[S43,S9]]。

### 工作原理

当试样发生伴随吸热或放热效应的物理化学变化（如熔化、凝固、晶型转变、分解、氧化还原等）时，试样与参比物之间出现温差，热电偶产生对应的电动势差，记录仪绘出差热曲线[[S17,S9]]。测试时，试样与在测试温度范围内无热效应的惰性参比物置于相同热环境中，采用反接串联的热电偶组直接插入试样和参比物中。当两者温度一致时，热电偶电动势差为零，记录基线；当试样发生热效应时，两者出现温差，记录仪绘出偏离基线的差热峰[[S17]]。

### DTA曲线的关键温度点

从差热曲线上可确定三个关键温度[[S43,S14]]：

- **反应起始温度 Ta**：DTA曲线开始偏离基线处对应的温度
- **峰值温度 Tb**：差热峰最高点所对应的温度，代表反应速率达到最大值[[S5,S42]]
- **热力学平衡温度 Te**：曲线陡峭部分切线与基线交点对应的温度

![DTA曲线示意图，标注反应开始点Ta、峰值点Tb及热力学平衡温度Te](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/623e2539-d0c4-4cf1-9495-d19b15354db2/resource)

## 与DSC（差示扫描量热法）的区别与联系

DTA与DSC同属热分析领域的核心非等温量热技术，均诞生于20世纪50年代末，都需要在程序控温环境下完成测试[[S2]]。两者均可用于相变特征温度的判定[[S36]]，但在测量原理、定量能力及适用温度范围上存在本质区别。

### 核心区别

| 对比维度 | DTA | DSC |
|---------|-----|-----|
| 测量物理量 | 试样与参比物之间的温差 ΔT | 进出试样的热流量（或维持温差所需的补偿功率差）[[S17,S10]] |
| 定量热分析能力 | 峰面积正比于反应焓和样品质量，反比于样品热导率，需对不同样品和温度区间进行专门校准才能获得定量热焓数据[[S2,S17]] | 曲线下面积直接与试样吸收或放出的总热量成正比，无需复杂校准即可直接输出定量焓变结果[[S17,S10]] |
| 测温上限 | 最高可达1500℃，适合高熔点铸造合金[[S2,S22]] | 常规商用设备上限不超过铝合金熔化温度（约700℃）[[S2,S3]] |
| 基线稳定性 | 存在基线漂移问题[[S24]] | 功率补偿型DSC通过热零态设计消除了基线漂移[[S24]] |

### DSC的技术分支

主流DSC分为热流型DSC和功率补偿型DSC[[S4,S18]]。功率补偿型DSC采用双独立低质量炉，维持试样与参比物始终处于热零态，其相变峰面积与样品热阻无关，无需校准热阻即可直接获得潜热，灵敏度和分辨率更高，是铝合金相变研究的首选设备[[S33,S4]]。热流型DSC测试上限可超过700℃[[S33]]。

## 设备组成

差热分析仪通常由五大核心系统组成：加热系统、温度控制系统、信号放大系统、差热系统、记录系统。高端型号可额外配置气氛控制系统和压力控制系统，炉温上限最高可达2400℃[[S8]]。

![差热分析仪系统结构框图，展示电炉单元（含样品S和参比物R）、温度程序控制单元、稳压电源、差热放大单元及记录仪单元的组成与信号流向](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b56981e-de96-46d0-9d0e-a02376dbe673/resource)

### 差热系统

差热系统是整个装置的核心部分，由样品室、试样坩埚、热电偶等组成。其中热电偶是关键元件，既是测温工具，又是传输信号工具[[S8]]。差热单元的具体构造包括对称布置的两个相同样品/参比物坩埚托架、嵌入托架内部的测温热电偶以及坩埚均温保持器，样品与参比物热电偶反向串联输出温差电信号[[S18,S4,S2]]。

### 温度控制系统与记录系统

温度控制系统用于控制测试时的加热条件（如升温速率、温度测试范围等），一般由定值装置、调节放大器、可控硅调节器（PID-SCR）、脉冲移相器等组成，现代化设备多已采用微电脑控制[[S8]]。记录系统早期采用双笔记录仪，目前已普遍使用微机进行自动控制和记录，并可对测试结果进行分析[[S8]]。

## 在压铸中的角色

### 液相线与固相线温度的测定

使用DTA测定压铸合金液相线温度的常规方法为：合金冷却DTA曲线上初晶相析出的外推起始点（onset点）对应的温度即为液相线温度[[S25,S41]]。测定固相线温度的常规方法为：合金加热DTA曲线上最后一个熔化吸热峰回到基线的温度点即为固相线温度[[S41,S25]]。

### 凝固区间与过冷度

压铸合金的凝固区间为DTA测得的液相线温度减去固相线温度，代表合金从开始析出固相到完全凝固的温度范围[[S21,S11]]。凝固过冷度为平衡液相线温度减去DTA冷却曲线测得的实际形核起始温度，反映合金凝固形核时偏离平衡相变点的程度[[S40,S20]]。

### 指导压铸工艺参数

1. **浇注温度**：通常基于DTA实测的液相线温度，叠加30~70℃的过热度作为推荐的浇注温度范围，避免合金液在充型阶段过早发生凝固引发冷隔、浇不足等缺陷[[S26,S44]]。

2. **模具温度**：凝固区间较宽的压铸合金需要匹配更高的模具预热温度，减缓糊状区固液共存的凝固速度，降低分散性缩松、枝晶偏析等缺陷的产生倾向[[S21,S29]]。

3. **半固态浆料控制**：基于DTA测得的液相线、固相线温度，可计算半固态浆料的固相分数。GB/T 40809-2021《铸造铝合金-半固态流变压铸成形工艺规范》中给出了基于差热分析数据的固相分数计算公式，为流变压铸的浆料温度控制提供依据[[S1]]。

## 典型测试条件与参数

### 压铸铝合金DTA测试的常规参数

| 参数项 | 典型值/要求 | 说明 |
|-------|-----------|------|
| 升温/降温速率 | 5~25 K/min，常用10 K/min | 特征温度随升温速率升高向高温侧偏移[[S32,S19,S30]] |
| 样品质量 | 10~30 mg | 过大则增大温度滞后偏差，过小则降低信噪比[[S30,S37,S32]] |
| 试样形态 | Φ3×2 mm 薄圆片 | 上下表面打磨平整，超声波清洗吹干[[S32,S30,S37]] |
| 坩埚材质 | 氧化铝（Al₂O₃）陶瓷坩埚 | 需加盖以减少气氛对流和热辐射带来的热损耗[[S32]] |
| 保护气氛 | 高纯氩气 | 全程开启氩气吹扫保护，防止高温氧化[[S32,S19,S30]] |
| 参比物 | Al₂O₃（高纯氧化铝）粉末/块体 | 在整个测试温度区间内无任何吸热或放热的物理、化学变化[[S19,S28,S17]] |

## 结果解读

### 相变起始温度的外推确定法

国际热分析协会推荐采用外推法确定相变起始点（onset）：将DTA相变峰上升段斜率最大处作切线，切线与基线的交点对应的温度即为相变起始点。该方法得到的温度值重复性最佳[[S25,S5]]。

### 峰值温度与相变热焓

DTA峰值温度定义为相变峰最高点对应的温度，代表该相变过程的反应速率达到最大值[[S42,S5]]。相变热焓的确定方法为：DTA相变峰与基线之间包围的积分面积与相变热焓成正比，经过标样校准后可定量计算出对应相变过程吸收或释放的总热量[[S5]]。

### 凝固曲线解读

压铸合金DTA凝固曲线可依次识别初晶相析出放热峰、共晶反应放热峰、最后一个相变结束后曲线回归基线的特征点，依次对应凝固过程中初晶形核长大、共晶相析出、合金完全凝固的三个阶段，完整还原合金的全路径凝固行为[[S40,S20]]。

## 相关标准

ASTM发布的热分析相关标准包括ASTM E473《热分析术语标准》、ASTM E1142《热物理性能相关术语标准》等，为DTA测试的术语统一、试验流程规范提供参考依据[[S6]]。

## 优缺点与局限性

### 主要优点

1. **高温适用性**：DTA的工作温区最高可达1500℃，远高于常规商用DSC的700℃上限，更适合高熔点铸造合金的相变测试[[S2,S22]]
2. **结构简单**：仪器结构相对简洁，操作便捷，适合工业实验室常规使用

### 主要局限

1. **定量能力受限**：DTA仅测量试样与参比物之间的温度差，无法直接获得热流和焓变的定量数据，需要经过系统标定后才能计算相变焓[[S17]]
2. **温度滞后效应**：特征温度随升温速率升高而向高温侧偏移[[S25,S32]]
3. **热灵敏度与温度分辨率的矛盾**：测得的峰值温差信号ΔT_max与系统热阻正相关，提升热灵敏度会增大热阻进而展宽相变峰、降低温度分辨率，提升温度分辨率又会降低热灵敏度，两者存在参数权衡[[S16]]
4. **试样尺寸效应**：DTA的峰值面积正比于试样质量，反比于试样的导热系数。过大的试样尺寸会造成热传导路径延迟，进一步增大温度滞后偏差；过小的试样则会降低弱吸热/放热相变的信号信噪比[[S2]]

## 应用实例

### ADC12铝合金的DTA分析

以ADC12铝合金为例，采用φ3 mm×2 mm、质量19.67 mg的试样，在流量50 mL/min的氩气保护气氛中以5℃/min的升温速率从450℃加热至650℃。DTA曲线显示：合金从539℃开始熔化，578℃完全熔化，凝固起始点为590℃，固液区间为539~590℃。可明确识别Al-Si二元共晶反应及L→α-Al+Si+Al₂Cu三元共晶相变的特征吸热峰[[S34]]。

### A380铝合金中共晶温度的定位

A380合金为Al-Si-Cu系压铸铝合金，在Al-Si二元相图中对应的标准共晶温度为577℃[[S39]]。通过DTA/DSC测试可精准识别该体系下的共晶相变特征。研究表明，添加0.6%稀土La/Y的A380合金相比未添加组，共晶Si相变峰值对应的过冷度从47.30℃提升至50.97℃，初生α-Al相变过冷度从21.55℃提升至25.25℃[[S35]]。这一结果可用于表征变质元素对凝固形核过程的调控作用。

## Sources
- S9: [铝合金热轧及热连轧技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40ad8610-f852-4694-a094-f095cbb808fc/resource) (`40ad8610-f852-4694-a094-f095cbb808fc`)
- S38: [16991063_差示热分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0816f3b-3fdc-40d5-9162-0a772c189e9c/resource) (`e0816f3b-3fdc-40d5-9162-0a772c189e9c`)
- S2: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ef79a61-549d-45ae-b5a5-8966783697c8/resource) (`0ef79a61-549d-45ae-b5a5-8966783697c8`)
- S21: [压铸冶金学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7d8747a5-c566-46b4-9439-4f69cba4efc2/resource) (`7d8747a5-c566-46b4-9439-4f69cba4efc2`)
- S29: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f7cd35f-7d01-470d-9691-6b16fc49e53e/resource) (`9f7cd35f-7d01-470d-9691-6b16fc49e53e`)
- S43: [熔盐电解镁锂合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2a00272-8f79-41b0-b547-b2c07e45df3a/resource) (`f2a00272-8f79-41b0-b547-b2c07e45df3a`)
- S17: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bb76973-e525-4988-9e33-c212c97d10d7/resource) (`6bb76973-e525-4988-9e33-c212c97d10d7`)
- S14: [图2.5 DTA法相变温度的确定](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/623e2539-d0c4-4cf1-9495-d19b15354db2/resource) (`623e2539-d0c4-4cf1-9495-d19b15354db2`)
- S5: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1614f23a-20a7-4d82-bf97-a3056cf45261/resource) (`1614f23a-20a7-4d82-bf97-a3056cf45261`)
- S42: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2458774-04b5-4ba8-93cd-278b43c3de26/resource) (`f2458774-04b5-4ba8-93cd-278b43c3de26`)
- S36: [1543734_热分析仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4957c9c-54e0-408e-91c5-354d9f1fce54/resource) (`c4957c9c-54e0-408e-91c5-354d9f1fce54`)
- S10: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40f793de-f672-451f-b97a-e4ad8f245229/resource) (`40f793de-f672-451f-b97a-e4ad8f245229`)
- S22: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/833a01f5-ef4d-46b8-9d84-3210122f9743/resource) (`833a01f5-ef4d-46b8-9d84-3210122f9743`)
- S3: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f8a07f2-f259-4126-bafc-43c7a3941e6e/resource) (`0f8a07f2-f259-4126-bafc-43c7a3941e6e`)
- S24: [10451127_差式扫描量热仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f5b0222-a588-4c20-9c09-c61ecb0293b5/resource) (`8f5b0222-a588-4c20-9c09-c61ecb0293b5`)
- S4: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15c59022-8e49-4616-9ab1-d0c77726e32c/resource) (`15c59022-8e49-4616-9ab1-d0c77726e32c`)
- S18: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fc40c17-5e20-48f8-aafe-d3038ae9c4d0/resource) (`6fc40c17-5e20-48f8-aafe-d3038ae9c4d0`)
- S33: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8ac4d0b-abd7-49cd-b9cf-9800406e94f3/resource) (`b8ac4d0b-abd7-49cd-b9cf-9800406e94f3`)
- S8: [铝合金热轧及热连轧技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cdeea19-abdc-4063-a23b-64027ed631fc/resource) (`2cdeea19-abdc-4063-a23b-64027ed631fc`)
- S25: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92052760-f295-4ea4-a59b-d76e4d86ab59/resource) (`92052760-f295-4ea4-a59b-d76e4d86ab59`)
- S41: [casting alloy design and characterization__2702a787cd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0e3ef90-6825-4ec1-8e59-e3eba02700f3/resource) (`f0e3ef90-6825-4ec1-8e59-e3eba02700f3`)
- S11: [aluminum for engine applications__90cbafbda9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5303a0fb-a9b4-4340-86c8-17013f8cfe83/resource) (`5303a0fb-a9b4-4340-86c8-17013f8cfe83`)
- S40: [effect of cooling rate on the solidification characteristics and dendrit__6faf5dac8a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e48d0af6-5965-460d-87ed-448ac7f8c69f/resource) (`e48d0af6-5965-460d-87ed-448ac7f8c69f`)
- S20: [characterization of magnesium automotive components produced by super va__b8e1b095ec](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77b27e1c-57c2-4673-9476-02c703a52c20/resource) (`77b27e1c-57c2-4673-9476-02c703a52c20`)
- S26: [压铸条件下合金流动停止机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/949ef888-8a01-403a-ae86-f1c5e6ab1790/resource) (`949ef888-8a01-403a-ae86-f1c5e6ab1790`)
- S44: [die cast engineering a hydraulic thermal and mechanical process__e5dfda1a8e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa9eac25-0316-4d00-ab91-449baeceb099/resource) (`fa9eac25-0316-4d00-ab91-449baeceb099`)
- S1: [GBT+40809（铸造铝合金-半固态流变压铸成形工艺规范）-2021.pdf-092c2199-e4b0-4fac-8e79-3ecf32ce3519](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00f6c9d9-e172-430d-b0db-45aa2fe7b472/resource) (`00f6c9d9-e172-430d-b0db-45aa2fe7b472`)
- S32: [铸型材质对锆基块体非晶合金性能的影响及铸造成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7ae8114-f3ab-4273-a701-1eb6777d00e8/resource) (`b7ae8114-f3ab-4273-a701-1eb6777d00e8`)
- S19: [铸造铝硅合金一体化控性工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/741a8803-1bae-4719-8122-b39a15c733a4/resource) (`741a8803-1bae-4719-8122-b39a15c733a4`)
- S30: [冷却速率对6005A、7N01和7A99铝合金组织及性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae2e3977-b935-463b-ae7e-dcefcaf3b1c9/resource) (`ae2e3977-b935-463b-ae7e-dcefcaf3b1c9`)
- S37: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9f18e0d-26be-4f79-9338-cf00d2e5a2cf/resource) (`c9f18e0d-26be-4f79-9338-cf00d2e5a2cf`)
- S28: [铝熔体中杂质Fe扩散行为及熔剂润湿行为的分子动力学模拟与试验](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/969e99ff-50d4-41b7-b59c-ac812ad54bdb/resource) (`969e99ff-50d4-41b7-b59c-ac812ad54bdb`)
- S6: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27c9bc4b-69dc-4c54-a132-8076f4425019/resource) (`27c9bc4b-69dc-4c54-a132-8076f4425019`)
- S16: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68349ff4-5738-4e60-a06f-af3833044e0c/resource) (`68349ff4-5738-4e60-a06f-af3833044e0c`)
- S34: [低过热度倾斜板流变压铸对ADC12组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb80db8e-2b73-404b-bd71-036327c607d9/resource) (`bb80db8e-2b73-404b-bd71-036327c607d9`)
- S39: [Al-Si合金温度-成分相图，标注A356、A380合金的成分与对应温度点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e211ed92-b7e9-4108-9941-2a673533501a/resource) (`e211ed92-b7e9-4108-9941-2a673533501a`)
- S35: [La/Y 添加对 A380 铝合金共晶 Si 与初生α-Al 峰值温度及过冷度的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c37b4f9a-44f8-4444-9732-2d10643a86b2/resource) (`c37b4f9a-44f8-4444-9732-2d10643a86b2`)