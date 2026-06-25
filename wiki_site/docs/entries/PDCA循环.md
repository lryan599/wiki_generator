---
version: "v1"
generated_at: "2026-06-18T09:38:33+00:00"
confidence_score: 0.83
confidence_level: "high"
confidence_basis:
  cited_sources: 25
  source_quality_score: 0.86
  freshness_score: 0.69
  evidence_coverage_score: 1.0
---

## 概述

PDCA循环，又称戴明环（Deming Cycle）、休哈特循环（Shewhart Cycle），是质量管理领域中最基础、应用最广泛的持续改进工作方法之一[[S6,S27,S11]]。该循环由美国质量管理专家沃特·阿曼德·休哈特（W.A. Shewhart）提出最初构想，后经爱德华兹·戴明（W. Edwards Deming）采纳、宣传并在二战后引入日本工业体系，最终发展为正式的PDCA循环模型[[S6,S27,S11]]。

PDCA循环将质量管理活动划分为计划（Plan）、执行（Do）、检查（Check）、行动/处置（Act）四个首尾衔接的闭环阶段，形成周而复始、螺旋式上升的改进过程[[S6,S15,S9]]。PDCA循环是ISO 9001、GB/T 19001质量管理体系所规定的核心运行方法，IATF 16949汽车行业质量管理体系亦完全继承该逻辑作为体系框架基础[[S5,S18,S22]]。

## 四个阶段与八个步骤

PDCA循环可进一步拆解为四个阶段、八个细分步骤，形成从问题识别到成果固化的完整闭环[[S15,S9,S12]]。

### P阶段（计划，Plan）

P阶段的任务是制定计划、确定质量目标及达标措施，包含四个步骤[[S15,S9]]：

1. **分析现状，找出质量问题**——运用排列图等方法定位核心问题；
2. **分析产生质量问题的所有原因**——从人、机、料、法、环五个维度全面排查[[S15,S9]]；
3. **从各种原因中筛选核心主要原因**——运用因果分析图等方法确定关键因素[[S15,S9]]；
4. **针对主要原因制定对策方案**——明确应对措施并预估实施效果[[S15,S9]]。

### D阶段（执行，Do）

D阶段为第五步，任务是将P阶段所制定的计划和措施付诸实施[[S15,S9]]。

### C阶段（检查，Check）

C阶段为第六步，任务是检查计划的执行情况和实施效果，比对预期目标，找出尚未解决的问题[[S15,S9]]。

### A阶段（处置，Act）

A阶段是PDCA循环的核心关键环节，起承上启下的作用，包含两个步骤[[S15,S9]]：

7. **总结经验，纳入标准**——将成功经验标准化、制度化，巩固已有成果，防止问题复发[[S15,S9]]；
8. **提出遗留问题，转入下一循环**——将本循环未能解决的问题转入下一轮PDCA循环继续攻关[[S15,S9]]。

![PDCA四阶段八步骤完整运行流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ef2cd78-2911-46f9-8f47-62e715f08038/resource)

图：PDCA循环四阶段及八个步骤示意——图中将P、D、C、A四个阶段进一步拆分为八个细分操作步骤，直观展示了PDCA从问题识别到成果固化的完整运行逻辑[[S13]]。

## 循环运转特征

PDCA循环在实际运转中呈现三个显著特征：

**1. 大环套小环、小环保大环**：企业整体层面的大PDCA循环可嵌套各部门、车间、班组的小PDCA循环乃至个人层面的微循环。大环是小环的目标依据，小环是大环的落地保证，彼此协调、相互促进，形成层级联动的质量管理体系[[S2,S22,S15]]。

![PDCA大环套小环运转示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0ae196d-65eb-45d6-9b7f-2a0f8c03c835/resource)

图：PDCA循环大环套小环层级联动特征示意——外层大循环嵌套多个内部小循环，箭头指示整体循环推动方向，直观说明企业级质量目标与各部门、车间级细化执行的协同关系[[S28]]。

**2. 阶梯式逐级上升**：每完成一轮完整的PDCA循环，解决一批质量问题，整体质量水平便提升一个层级，随即转入新的更高层次的循环，并非在同一水平上往复[[S2,S22,S20]]。

**3. 综合运用科学管理方法**：PDCA循环配套使用以QC七大手法（排列图、因果图、控制图、直方图、调查表、分层法、相关图）为主的统计处理方法及工业工程方法，作为进行工作、发现问题和解决问题的工具集合[[S22,S25]]。

## 配套工具：QC七大手法

PDCA循环各阶段配套使用的主流工具以QC七大手法（亦称QC七种工具）为主，二者属于配套使用的并列质量工具集合[[S22,S25]]：

| 工具名称 | 主要用途 | 适用PDCA阶段 |
|---------|---------|------------|
| 排列图（巴雷特图） | 找出影响质量的主要因素 | P阶段（步骤1） |
| 因果分析图（鱼刺图/树枝图） | 分析问题原因 | P阶段（步骤2、3） |
| 控制图 | 监控过程是否受控 | C阶段 |
| 直方图 | 显示数据分布状态 | C阶段 |
| 调查表 | 系统收集数据 | P、C阶段 |
| 分层法 | 对数据进行分类分析 | C阶段 |
| 相关图（散布图） | 分析两变量间关系 | P阶段 |

## 与其他质量管理方法的关系

PDCA循环是质量管理方法体系的底层逻辑基础，多种主流方法在其基础上衍生发展[[S6,S18,S8]]：

**SDCA循环（标准化-执行-检查-处置）**：与PDCA循环构成协同配对关系。PDCA的核心作用是驱动质量改进以实现水平提升；SDCA的核心作用则是固化维持已改进的标准化成果。二者结合可实现"改进→固化→再改进"的持续质量提升循环[[S6,S4]]。

**DMAIC（六西格玛改进方法）**：DMAIC（定义-测量-分析-改进-控制）是在PDCA循环底层逻辑基础上衍生出的更聚焦统计数据分析的质量改进框架，二者核心逻辑同源[[S18,S8]]。

**8D问题解决法**：8D是PDCA循环在生产故障归零场景下的结构化衍生应用，针对已发生的不合格品问题提供标准化的八步故障分析与整改流程[[S6,S23]]。

## 在压铸领域的典型应用

### 双PDCA循环案例——薄壁压铸件成型攻关

1991年，扬州曙光仪器厂针对壁厚仅0.9±0.1 mm、外表面积约114 cm²的01-44ZJ ZL104铝合金薄壁压铸件开展双PDCA循环质量改进[[S26,S17]]。初始三次试模共90件全部不合格，存在欠铸、四角开裂、组织疏松、冷隔、花纹等缺陷[[S26,S16,S17]]。

**第一个PDCA循环**：从人、机、料、法、环五个维度绘制因果图，定位核心影响因素为模具、材料、工艺三类，并实施相应改进对策。采取措施后铸件成型情况好转，但仍无法完全合格[[S26,S17]]。

**第二个PDCA循环**：引入L₉(3⁴)正交试验设计，以压射比压、浇注温度、压射速度、模具温度四大核心参数为变量开展三水平试验，最终确定最优工艺参数如下[[S26,S16,S17]]：

| 工艺参数 | 最优值 |
|---------|--------|
| 压射比压 | 100 MPa |
| 浇注温度 | 710 ℃ |
| 压射速度（调节螺杆长） | 43 mm |
| 模具温度 | 180 ℃ |

经试生产验证，量产阶段铸件成品率可达90%以上，力学性能与尺寸精度全部满足图纸要求[[S26,S16,S17]]。

### 多轮PDCA迭代——冷隔缺陷降低案例

某压铸企业针对铝压铸件冷隔高废品率问题开展多轮PDCA迭代改进。初始阶段通过排列图（巴雷特图）定位冷隔为最主要质量缺陷，再通过因果分析图从人、机、料、法、环维度排查出核心影响因素集中在压射参数方面[[S21]]。

针对性改进措施包括：提高压射比压、匹配合理压射速度、增厚内浇口厚度、修整模具圆角半径、精准控制金属液与模具温度等。经过几个PDCA工作循环的验证，冷隔缺陷占比大幅下降，铸件整体废品率显著降低[[S21]]。

### PDCA全流程优化——化油器本体漏气问题

针对ADC12铝合金汽车化油器本体加工后漏气废品率超40%的问题，采用PDCA全流程排查优化[[S14]]：

| 排查维度 | 发现问题 | 改进措施 |
|---------|---------|---------|
| 合金成分 | Zn含量约2%、Fe含量约3%，严重超标 | 控制合金原料杂质含量 |
| 金相分析 | 基础组织晶体粗大，存在气孔、缩孔 | 工艺调整 |
| 熔炼工艺 | 金属液含气量高 | 氩气脱气处理15 min |
| 模具方案 | 排气不充分 | 加大排气槽尺寸、增设辅助浇口 |
| 压铸工艺 | 浇注温度、模温偏高 | 浇注温度由680~690 ℃降至670±5 ℃，模温由200 ℃降至160 ℃ |

实施上述改进措施后，漏气废品率降至5%以下[[S14]]。

### PDCA与田口方法（正交试验）结合的工艺优化

在压铸工艺参数的系统优化中，PDCA循环常与实验设计方法（DOE）结合使用。以AlSi9Cu3铝合金压铸件孔隙率优化为例：采用五因素三水平L₂₇正交试验设计，核心变量包含保温炉温度、模具温度、一阶段压射速度、二阶段压射速度、增压压力[[S1]]。经过PDCA全流程迭代优化后，预测最优条件下铸件孔隙率仅0.25%，较优化前降低48.6%，对应铸件缺陷相关成本可降低71.4%[[S1]]。

## 压铸行业PDCA实施规范

压铸行业PDCA落地的通用实施规范要求：企业须按照PDCA"计划-执行-检查-行动"四阶段逻辑构建压铸质量体系运行架构，配套完整的标准化质量文件体系[[S15,S19,S24]]。核心文件包括以下六类[[S19]]：

1. 潜在失效模式及后果分析（PFMEA）文件
2. 控制计划文件
3. 压力铸造工艺流程文件
4. 压铸作业指导书
5. 压铸工艺卡
6. 清理加工工艺过程卡

体系运行需明确企业-车间-班组三级PDCA循环落地权责，配套压铸班组质量责任制，实现大环套小环的逐级质量管控[[S15,S19,S24]]。

## 局限性

在压铸生产场景下，PDCA循环存在以下适用边界与局限性：

1. **循环周期较长，难以适配快速换型**：PDCA属于渐进式迭代改进方法，完整四阶段循环周期较长，无法满足压铸快速换型场景下短时间内完成新产品压铸工艺参数快速调试的节拍要求[[S6]]。

2. **人工经验依赖性强，存在主观偏差风险**：PDCA的原因分析环节强烈依赖压铸技术人员人工经验来绘制因果图、判断主次因素。人工主观判断偏差容易导致核心工艺因素漏判，直接影响改进效果[[S6]]。

3. **数据处理能力与高速生产节拍不匹配**：大规模连续压铸生产场景下每秒会产生大量实时工艺传感数据，传统PDCA人工采集分析模式效率较低，难以匹配压铸高速生产节拍下的实时异常告警需求[[S6]]。

为克服上述局限，PDCA循环需与SDCA标准化循环协同配合，方能在量产阶段维持工艺稳定性，有效巩固改进成果[[S6]]。

## Sources
- S6: [5091521_PDCA循环](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/33fa7739-6425-44cc-b2e9-fa25ad34df61/resource) (`33fa7739-6425-44cc-b2e9-fa25ad34df61`)
- S27: [design for manufacturability__79c3ec77d8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efef3a6b-719a-4e40-b8a9-5aca523eb899/resource) (`efef3a6b-719a-4e40-b8a9-5aca523eb899`)
- S11: [PDCA 循环核心要素与定义表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f332025-55d1-4fe4-bec4-87ab2184ee17/resource) (`4f332025-55d1-4fe4-bec4-87ab2184ee17`)
- S15: [工程材料及机械制造基础机械加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81e82637-ca4c-4ffe-a770-5aef70fc7f9a/resource) (`81e82637-ca4c-4ffe-a770-5aef70fc7f9a`)
- S9: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40d65934-6dc8-4d0c-9af4-9604a2dddfda/resource) (`40d65934-6dc8-4d0c-9af4-9604a2dddfda`)
- S5: [现代模具设计制造理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/33440c73-6735-41a6-833d-ee1b4705bd73/resource) (`33440c73-6735-41a6-833d-ee1b4705bd73`)
- S18: [advances in manufacturing systems selected peer reviewed papers from the__4041064e88](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9070d07e-d098-45df-aff7-21ceebcb60ac/resource) (`9070d07e-d098-45df-aff7-21ceebcb60ac`)
- S22: [模具钳工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c111a97d-f652-4a0f-aec3-f3c1db095444/resource) (`c111a97d-f652-4a0f-aec3-f3c1db095444`)
- S12: [PDCA 循环八个步骤详解](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ce2888d-c50d-401b-bde7-a61fe039ec32/resource) (`5ce2888d-c50d-401b-bde7-a61fe039ec32`)
- S13: [PDCA科学程序四个阶段及八个步骤示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ef2cd78-2911-46f9-8f47-62e715f08038/resource) (`5ef2cd78-2911-46f9-8f47-62e715f08038`)
- S2: [工程材料及机械制造基础机械加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03e661e3-a952-4074-b8eb-e392d7cbf697/resource) (`03e661e3-a952-4074-b8eb-e392d7cbf697`)
- S28: [PDCA管理循环大环套小环示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0ae196d-65eb-45d6-9b7f-2a0f8c03c835/resource) (`f0ae196d-65eb-45d6-9b7f-2a0f8c03c835`)
- S20: [PDCA管理循环逐级上升示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7e7dde6-0851-42d5-befb-a1878adcc2dd/resource) (`a7e7dde6-0851-42d5-befb-a1878adcc2dd`)
- S25: [解决质量问题的PDCA循环步骤与方法表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cad5de3a-be7d-4546-bfbe-75b0c20f9ee7/resource) (`cad5de3a-be7d-4546-bfbe-75b0c20f9ee7`)
- S8: [advances in manufacturing systems selected peer reviewed papers from the__4041064e88](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c7f62c9-a6bf-429c-83f5-a483ed1902a3/resource) (`3c7f62c9-a6bf-429c-83f5-a483ed1902a3`)
- S4: [转动戴明环示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c6ed6d6-f0c9-4423-816f-31bac07f76f0/resource) (`1c6ed6d6-f0c9-4423-816f-31bac07f76f0`)
- S23: [模具失效分析与故障处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c1d4a459-42cb-408e-b6ad-71123dba15ea/resource) (`c1d4a459-42cb-408e-b6ad-71123dba15ea`)
- S26: [应用QC方法解决薄壁件压铸成型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cccda49a-96a0-47f1-9cc7-da13cbfaf2f8/resource) (`cccda49a-96a0-47f1-9cc7-da13cbfaf2f8`)
- S17: [应用QC方法解决薄壁件压铸成型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cf663f1-8666-4ada-8853-0d16f36a16a2/resource) (`8cf663f1-8666-4ada-8853-0d16f36a16a2`)
- S16: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87ca51cc-fba4-4a07-9572-924113ef3023/resource) (`87ca51cc-fba4-4a07-9572-924113ef3023`)
- S21: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9dbb840-fe40-43d3-abe1-12ef95ac55db/resource) (`a9dbb840-fe40-43d3-abe1-12ef95ac55db`)
- S14: [卧式冷室压铸机技术教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/600a1e5d-d058-44f0-8ccf-5b988049e00a/resource) (`600a1e5d-d058-44f0-8ccf-5b988049e00a`)
- S1: [a study of porosity formation in pressure die casting using the taguchi__4ac320727f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00f609b3-d4ba-43f7-9e98-de6b5eb7d280/resource) (`00f609b3-d4ba-43f7-9e98-de6b5eb7d280`)
- S19: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9408f1f3-dbc9-4314-b31d-7de574cf9ed2/resource) (`9408f1f3-dbc9-4314-b31d-7de574cf9ed2`)
- S24: [模具钳工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3650e71-0687-4dc7-b7bb-2726baa74899/resource) (`c3650e71-0687-4dc7-b7bb-2726baa74899`)