---
version: "v1"
generated_at: "2026-06-18T14:29:58+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 14
  source_quality_score: 0.88
  freshness_score: 0.7
  evidence_coverage_score: 1.0
---

## 概述

RJ-2熔剂是国内定型的镁合金专用覆盖剂兼精炼剂，属于RJ系列中的经典牌号。该熔剂虽然未直接收录于现行国家标准（GB/T）或航空行业标准（HB）体系，但在《航空制造工程手册》《压铸件生产指南》等权威铸造手册中被广泛收录并推荐使用[[S1,S4,S11]]。与仅具备单一除杂功能的普通镁精炼剂不同，RJ-2能够同时完成熔池表面隔氧覆盖与熔体除渣净化双重工艺任务。

## 组成与配制

根据《压铸件生产指南》的记载，RJ-2熔剂有两种标准配料方案[[S5,S1]]：

- 配比一：88 wt% 光卤石 + 7 wt% 氯化钡（BaCl₂） + 5 wt% 氟化钙（CaF₂）
- 配比二：95 wt% RJ-1熔剂 + 3~5 wt% CaF₂

其中，RJ-1熔剂本身由93 wt%光卤石与7 wt%氯化钡构成[[S5]]。RJ-2是在RJ-1基础上引入少量氟化钙而成，其核心组成为富含MgCl₂的氯盐，氟盐仅作为关键添加剂[[S2,S1]]。

配制时，可将已干燥的RJ-1粉体与经过精选、粉碎（20~40号筛）并烘干的CaF₂直接混合制得[[S2]]。所有原料在使用前均须严格控制水分含量；光卤石及RJ-1吸水性强，含水量应≤2%，若超过3%则须重新熔炼、粉碎、过筛方可使用[[S2]]。

## 物理性质

RJ-2熔剂的关键物理参数如下表所示，其数据来源于《铝、镁合金熔炼与成形加工技术》及《有色金属熔炼入门与精通》中的实测对比[[S7,S14]]。

| 参数 | 数值 | 测试条件 / 方法 |
|------|------|---------------|
| 熔点 | 约 435 ℃ | 宏观法 |
| 熔点 | 约 419 ℃ | 差热分析法 |
| 密度 | 2.00 g/cm³ | 600 ℃ |
| 密度 | 1.74 g/cm³ | 700 ℃（加入3~5% CaF₂后） |
| 粘度 | 5.2 Pa·s | 600 ℃ |

熔剂的密度、粘度通过CaF₂的加入得以调控，使其既能在镁液表面形成稳定保护层，又不致因粘度过低而难以维持覆盖。通常推荐将该熔剂用于680~780 ℃的镁液温度区间[[S7,S14,S3]]。

## 作用机理

### 表面覆盖与防氧化

RJ-2中大量的MgCl₂与添加的CaF₂在高温下发生置换反应：

CaF₂ + MgCl₂ → MgF₂ + CaCl₂

生成的MgF₂在氯盐中溶解度极低，且溶解度几乎不随温度变化而改变。未溶解的固态MgF₂质点均匀分布于液相氯盐中，显著提高了熔剂的粘度，使其能够在镁液表面铺展成连续的、致密的密封层，从而有效隔绝空气，阻止镁液氧化燃烧[[S3]]。此外，部分MgCl₂在高温下分解产生的HCl和H₂可在液面上形成微保护气氛，进一步减缓氧化[[S12]]。

![熔剂的覆盖作用示意图（a：接触角θ决定铺展性；b：熔剂在坩埚内同时润湿合金液面与炉壁，形成密封保护层）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d4bc04e-e193-433c-bd8f-dd2d31f6d4b0/resource)
*图1 熔剂覆盖作用示意图，展示熔剂在合金表面铺展及与坩埚壁的润湿状态[[S8]]*

### 除渣精炼

反应生成的MgF₂具有与镁液中氧化物夹杂（MgO）化合的能力，能够吸附悬浮于熔体中的氧化夹杂，并使其随熔剂沉降或附着于液面熔渣中而被清除。这一特性赋予了RJ-2良好的精炼功能[[S3]]。

![熔剂法除渣示意图（上熔剂法与下熔剂法），展示熔剂吸附镁液中夹渣元素的过程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74eb2cbc-afa6-4cf3-8c9d-b5c2297adc87/resource)
*图2 熔剂法除渣示意图，说明上、下熔剂法模式下熔剂与夹渣的结合与去除[[S6]]*

### 潜在负面影响

值得注意的是，若RJ-2熔剂使用过量，残留的氯离子（Cl⁻）有可能进入镁合金熔体形成熔剂夹杂，降低铸件的耐腐蚀性能，并成为服役过程中的腐蚀源[[S12]]。

## 使用工艺与参数

### 撒布时机与方式

在镁合金熔炼过程中，RJ-2主要用于精炼阶段的熔剂覆盖与除渣。当合金液温度升至710~740 ℃时，用搅拌工具深入液面下约2/3深度搅拌5~8 min，同时沿合金液循环流的波峰逐步手工撒入粉状RJ-2熔剂。单次精炼操作所用的RJ-2量约为炉料总质量的1.5%~2.0%；整个熔炼过程（包括覆盖）的熔剂总消耗量通常为炉料总质量的3%~5%，折合约30~50 kg每吨镁液[[S13]]。精炼结束后，清除熔渣并再在液面上均匀覆盖一层RJ-2，随后静置10~20 min即可进行浇注。

### 预处理要求

粉状覆盖熔剂的粒度不应大于1.5 mm，投入使用前须在约300 ℃的烘箱中预烘烤2 h，以彻底脱除吸附水分，避免水分带入引发合金吸气或喷溅[[S13,S11]]。

## 适用范围与限制

RJ-2熔剂适用于AZ系列（如AZ91）、AM系列等常规镁合金牌号的熔炼保护，可兼容砂型铸造、金属型铸造、压力铸造等多种工艺场景[[S4,S9]]。

由于熔剂基体中大量的MgCl₂会与镁合金中的稀土元素发生反应，造成稀土元素的损耗，因此不推荐用于含有高浓度稀土元素的镁合金熔炼[[S9]]。

## 与其他保护方法的对比

RJ系列覆盖剂及几种主要保护方式的特点对比如下[[S10,S12]]：

| 保护方式 | 特性 | 适用场合及限制 |
|----------|------|----------------|
| RJ-1 | 粘度低、流动性好 | 主要用于洗涤坩埚或轻型覆盖；精炼能力不足 |
| RJ-2 | 粘度、精炼性能平衡，兼具覆盖与除渣 | 固定式坩埚熔炼的主流选择；也可用于带隔板的手提坩埚 |
| RJ-3 | 粘度更高，高温下可自行结壳 | 适合可提出式坩埚，高温（>850℃）可扒除硬壳；不适用于固定式坩埚 |
| 硫磺粉 | 燃烧生成SO₂抑制氧化 | 易生成大量MgS夹杂，降低合金质量 |
| SF₆气体保护 | 无熔剂夹杂风险，保护效果稳定 | 运行成本高，SF₆具有极强的温室效应；需配备气体混合控制装置 |

RJ-2在固定式坩埚镁合金熔炼场景下，平衡了覆盖可靠性、精炼效率与操作便利性，因此成为国内长期以来的应用主流。

## 安全与环保

RJ-2熔剂含有氯盐和氟盐，高温使用过程中会释放含有HCl、HF、Cl₂等成分的有毒烟气。熔炼工位必须配置有效的强制通风系统，以保障操作人员安全和作业环境[[S12,S11]]。

熔剂极易吸湿，未开封产品应密封存放于干燥库房中。若发生受潮，需重新熔制并充分脱水，经检测含水量≤2%后方可继续使用[[S2,S11]]。使用后产生的废渣含有氟化物和氯化物，属于危险废弃物，必须按照相关规定进行合规处置，不得随意排放[[S12]]。

## Sources
- S1: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44cef584-f1e1-4ddc-9566-6e2960ac0186/resource) (`44cef584-f1e1-4ddc-9566-6e2960ac0186`)
- S4: [熔剂的化学成分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63180863-53dd-4311-bb5a-c3a1f47fb074/resource) (`63180863-53dd-4311-bb5a-c3a1f47fb074`)
- S11: [压铸工艺及设备模具实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d61c4514-6910-4e79-8db4-9ed358a64677/resource) (`d61c4514-6910-4e79-8db4-9ed358a64677`)
- S5: [熔剂配料成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69c29655-0994-4af1-bd15-63f6ea9479cd/resource) (`69c29655-0994-4af1-bd15-63f6ea9479cd`)
- S2: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ee249fe-8b60-464d-8235-dc28552f1a2e/resource) (`4ee249fe-8b60-464d-8235-dc28552f1a2e`)
- S7: [表 2-8 几种覆盖剂的熔点、密度及粘度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8012ddaf-b34a-4c09-a1c5-29c071227a6b/resource) (`8012ddaf-b34a-4c09-a1c5-29c071227a6b`)
- S14: [几种覆盖剂的熔点、密度及粘度参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fcae1775-6f3e-4dcb-ab8d-eff7da1e14c7/resource) (`fcae1775-6f3e-4dcb-ab8d-eff7da1e14c7`)
- S3: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/507081a6-bdd5-4b61-802d-ed64b7ee84d1/resource) (`507081a6-bdd5-4b61-802d-ed64b7ee84d1`)
- S12: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9d0bd9b-5a7d-4e75-b7ba-4b2640c2a7f7/resource) (`e9d0bd9b-5a7d-4e75-b7ba-4b2640c2a7f7`)
- S8: [熔剂的覆盖作用示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d4bc04e-e193-433c-bd8f-dd2d31f6d4b0/resource) (`8d4bc04e-e193-433c-bd8f-dd2d31f6d4b0`)
- S6: [熔剂法除渣示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74eb2cbc-afa6-4cf3-8c9d-b5c2297adc87/resource) (`74eb2cbc-afa6-4cf3-8c9d-b5c2297adc87`)
- S13: [压铸件生产指南](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef2fcf45-ef8f-47ab-82cd-cdb1ae39150f/resource) (`ef2fcf45-ef8f-47ab-82cd-cdb1ae39150f`)
- S9: [direct chill casting of light alloys science and technology__2cc8c5db62](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c24beb57-caec-4d9d-a390-aeea913c5c58/resource) (`c24beb57-caec-4d9d-a390-aeea913c5c58`)
- S10: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb8278a3-db1b-4409-9bfc-af76c8f99f8b/resource) (`cb8278a3-db1b-4409-9bfc-af76c8f99f8b`)