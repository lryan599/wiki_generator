---
version: "v1"
generated_at: "2026-06-18T14:55:36+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 41
  source_quality_score: 0.87
  freshness_score: 0.71
  evidence_coverage_score: 1.0
---

六氯乙烷（Hexachloroethane），化学式 C₂Cl₆，CAS 号 67-72-1，分子量 236.76，在铸造行业中常称作 **C₂Cl₆ 精炼剂**、六氯乙烷除气剂或简称为精炼剂，是一种铝合金熔炼中广泛使用的氯盐类固态除气精炼剂 [[S14,S20,S12]]。需注意，中文资料中偶尔出现的“Ar2”并非六氯乙烷的别名：所有公开的铸造冶金文献中均不存在牌号为 Ar2 的商用精炼剂，氩在工业精炼中仅以单原子气体 Ar 形式出现，不存在 Ar₂ 分子；因此“Ar2”实为氩气（Ar）类精炼工艺的录入错误，与本条目无关 [[S15,S42,S10]]。

## 化学本质与分类
六氯乙烷属于卤代烃类氯化物型除气剂，与四氯化碳（CCl₄）、四氯乙烯（C₂Cl₄）等同属**吸附式除气精炼剂**范畴，而非覆盖剂 [[S17,S28,S20]]。它在高温下通过热分解和化学反应生成不溶于铝液的气态产物，起到除气与除渣的双重作用。

## 物理性质
六氯乙烷常温下为白色或无色斜方结晶，关键物性如下 [[S14,S12,S24,S19]]：

| 性质 | 数值 / 描述 |
|---|---|
| 密度 | 2.09 g/cm³（约 2.091 g/cm³） |
| 熔点 | 约 186 ℃（事实上直接升华） |
| 升华温度 | 184.4 ~ 185.5 ℃ |
| 吸湿性 | 不吸湿，无需预脱水处理 |
| 溶解性 | 几乎不溶于水，可溶于醇、醚、苯 |
| 毒性 | 中等毒性，加热分解释放刺激性氯系烟气 |

## 工艺作用与机理
六氯乙烷投入铝合金/锌合金熔液后发生以下反应 [[S37,S14,S33,S12]]：
1. 热分解：  
   \[
   \mathrm{C_2Cl_6 \rightarrow C_2Cl_4\!\uparrow + Cl_2\!\uparrow}
   \]
2. 与铝反应：  
   \[
   \mathrm{2Al + 3Cl_2 \rightarrow 2AlCl_3\!\uparrow}
   \]
   \[
   \mathrm{3C_2Cl_6 + 2Al \rightarrow 3C_2Cl_4\!\uparrow + 2AlCl_3\!\uparrow}
   \]

反应生成的 C₂Cl₄（沸点 121 ℃）和 AlCl₃（沸点 183 ℃）在熔炼温度下均为气态、不溶于铝液，形成大量弥散气泡。溶解在铝液中的氢在分压差驱动下扩散进入气泡，随气泡上浮排出液面，实现**除气**；同时上浮气泡可吸附 Al₂O₃ 等氧化夹杂带至熔渣层，实现**除渣** [[S37,S14,S33]]。

对于含镁铝合金，Cl₂ 及 AlCl₃ 会优先与 Mg 反应生成 MgCl₂。MgCl₂ 的除气能力远低于 AlCl₃，且其熔点为 715 ℃。若精炼温度低于该值，MgCl₂ 呈固态残留为夹杂；因此必须将精炼温度提高至 725 ℃以上，使 MgCl₂ 保持液态发挥辅助精炼作用 [[S39,S33]]。

## 工艺参数与操作要求
### 纯六氯乙烷精炼
- **加入量**：炉料总重的 0.2% ~ 0.7%（通常 0.3% ~ 0.6%）[[S14,S9,S21,S27]]。
- **加入方式**：将纯 C₂Cl₆ 或压制块分 2 ~ 5 次用钟罩压入熔池中心，深至距坩埚底 100 ~ 150 mm，每份不超过总量的 30% [[S14,S8]]。
- **精炼温度**：无镁合金（如 ZL102）推荐 700 ~ 720 ℃；含镁合金（如 ZL101、ZL104）推荐 730 ~ 750 ℃ [[S33,S14,S4]]。
- **精炼时间**：总作用时间 8 ~ 15 min，静置 5 ~ 12 min 后浇注 [[S14,S27]]。

### 复合精炼剂（加缓冲剂）
为延缓反应速度、提高气泡上浮净化效果，常在 C₂Cl₆ 中掺入 Na₂SiF₆、NaBF₄ 或 TiO₂ 等缓冲剂，压制成 50 ~ 100 g 饼块后一次加入 [[S18,S14,S8,S23]]。其工艺规范如下 [[S14,S17]]：

| 参数 | 纯 C₂Cl₆ | 复合 C₂Cl₆（含缓冲剂） |
|---|---|---|
| 加入量（占炉料总重） | 0.2% ~ 0.7% | 0.4% ~ 0.7% |
| 精炼温度 | 700 ~ 750 ℃（含镁合金偏高） | 730 ~ 750 ℃ |
| 精炼总时间 | 8 ~ 15 min | 12 ~ 15 min |
| 静置时间 | 5 ~ 12 min | 10 ~ 12 min |

常见缓冲剂配方及适用体系 [[S18,S23,S8]]：
- 添加 Na₂SiF₆ 或 NaBF₄ 的配方多用于 **Al-Si 系合金**；
- 添加 TiO₂ 的配方多用于 **Al-Cu 系合金**；
- 推荐配比（体积或质量）如 1/2 C₂Cl₆ + 1/2 Na₂SiF₆，或 2/3 C₂Cl₆ + 1/3 TiO₂ 等。

向制块模具中填入精炼剂的操作如图所示（可用于复合精炼剂制备）[[S16]]：
![向制块用模具模体中填入精炼剂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7822bdf2-8b59-4749-a47a-5f584bc43305/resource)

熔炼全流程中精炼工序所在位置可参见示意图 [[S32]]：
![铝合金熔炼工艺流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9c0c183-0b36-4746-8e48-25473844c2bb/resource)

### 含镁合金的特殊考虑
高镁铝合金无绝对禁用六氯乙烷的禁忌，但必须注意 [[S39,S14,S4,S17]]：
1. Mg 元素会与 Cl₂、AlCl₃ 反应生成 MgCl₂，导致镁烧损，配料时 Mg 成分应取上限，且 C₂Cl₆ 用量需相应增加。
2. 精炼温度必须控制在 725 ~ 750 ℃，以保证 MgCl₂ 为液态，避免固态夹杂。

## 应用范围与限制
- **适用合金**：适用于所有铸造铝合金体系（如 Al-Si、Al-Cu、Al-Mg 等），通过调整缓冲剂可适配不同合金 [[S39,S18,S1,S6]]。亦可用于镁合金的除气与变质处理 [[S1,S22,S35]]。
- **适用工艺**：适配金属型铸造、砂型铸造、石膏型精密铸造、低压铸造、重力铸造等场景下的中小容量坩埚式熔炼 [[S26,S2,S7]]。
- **不适用场景**：>20 t 级大型反射炉批量精炼，因气泡上浮路径短、除气效率低，效果不稳定 [[S26,S2,S7]]。

六氯乙烷精炼后的合格镁合金铸件实物示例 [[S22,S35]]：
![六氯乙烷处理镁合金工艺生产的铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96f0175b-b59b-4b79-b9c3-0c4db8955f8e/resource)

## 除气/除杂效果曲线
ZL101 铝合金中，随六氯乙烷加入量增加，合金含氢量显著下降；当添加量达到约 0.7% 时可获得完全致密、无明显针孔的铸件 [[S3]]。
![ZL101合金含氢量与六氯乙烷精炼剂用量的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3393591a-8acf-48da-807f-a39a0f57d8b5/resource)

采用复合改性（如 NK-C₂Cl₆）的六氯乙烷精炼剂在除钙效率上明显优于纯 C₂Cl₆，同等添加量下可使铝熔体中钙含量更低 [[S38]]。
![普通六氯乙烷与NK-C2Cl6复合精炼剂除钙效果对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea1b0023-d87f-493b-b451-b2b3002791a1/resource)

## 优缺点对比
六氯乙烷与其它常见除气方法的相对特性如下：

| 对比项 | 六氯乙烷 | 氯气 / CCl₄ 类 | 旋转喷吹惰性气体（Ar、N₂） |
|---|---|---|---|
| 除气效率 | 与氯气接近，显著高于 N₂ 旋转除气 [[S11,S5,S31]] | 相似，但 C₂Cl₆ 气体产物体积为 MnCl₂ 的 1.5 倍 [[S31]] | 效率较低，需长时间处理 |
| 操作便利性 | 固态不吸潮，无需脱水；用钟罩压入即可，无需旋转设备 [[S14,S40,S30]] | CCl₄ 为液态，需载体浸泡加入 [[S28,S34]] | 需专用旋转除气装置，设备投资高 [[S40,S30]] |
| 夹杂去除 | 气泡吸附夹杂，兼具除渣效果 [[S14,S33]] | 类似 | 对小夹杂效果有限，经旋转除气后熔体纯净度更高 [[S40]] |
| 含镁合金影响 | Mg 烧损，需上调配料、增加用量，但可通过工艺控制 [[S39,S17,S34]] | CCl₄ 精炼时 Mg 损失更大 [[S17,S34]] | 无化学反应，Mg 损失少 |
| 环保与安全 | 热分解生成 Cl₂、C₂Cl₄ 等有毒刺激性气体，需强力排风净化 [[S36,S25,S29]] | 同样产生有害氯系气体 [[S17,S28]] | 纯惰性气体基本无害，长期环保更优 [[S40,S29]] |
| 适用规模 | 中、小容量坩埚熔炼，不适用大型反射炉 [[S26,S2]] | 类似 | 可连续处理大容量熔体，适用性更广 |
| 存储与预处理 | 自身不吸潮，密封干燥保存即可；缓冲剂需烘烤脱水 [[S14,S13,S8,S18]] | CCl₄ 吸湿性低；其他氯盐多易吸潮需脱水 | 气体来源需纯化，无固态剂存放问题 |

## 安全与环保
六氯乙烷在高温分解中释放 Cl₂、C₂Cl₄、AlCl₃ 等腐蚀性刺激性气体，属于压铸/铝合金熔化工部重点管控的废气源。**必须**配备可靠的抽风净化设备，保证有害气体被有效收集处理，排放符合环保标准，以保障作业人员职业健康 [[S36,S25,S39,S29]]。

## 存储与保管
- **六氯乙烷本身**：白色晶体，不吸潮，无需预烘干，密封放置于常规干燥容器内即可稳定保存 [[S14,S13]]。
- **复配添加剂**（如 Na₂SiF₆、NaBF₄、TiO₂ 等）：具有吸湿性，使用前须在 350 ~ 400 ℃ 下烘烤 3 ~ 5 h 脱水，冷却后密封存放 [[S14,S13,S8,S18]]。

## Sources
- S14: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75775de5-ba01-4fed-a477-706965ad98ab/resource) (`75775de5-ba01-4fed-a477-706965ad98ab`)
- S20: [铝合金金属型铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bb646cb-73bc-4ae2-95b0-1c338acfe90d/resource) (`8bb646cb-73bc-4ae2-95b0-1c338acfe90d`)
- S12: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/647ef119-a156-45e9-b862-a3947e230816/resource) (`647ef119-a156-45e9-b862-a3947e230816`)
- S15: [12730948_精炼剂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77d6e999-abaa-43cb-8fec-b54aa92447d5/resource) (`77d6e999-abaa-43cb-8fec-b54aa92447d5`)
- S42: [原铝及其合金的熔铸生产问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f231a7f3-0263-4584-9474-33cd7bb2810b/resource) (`f231a7f3-0263-4584-9474-33cd7bb2810b`)
- S10: [aluminum recycling__884cb2d971](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e39c4b1-11bd-4963-989e-922dfe31548b/resource) (`5e39c4b1-11bd-4963-989e-922dfe31548b`)
- S17: [轻有色金属及其合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a3a13f2-849d-40b5-8629-09644ebb32c6/resource) (`7a3a13f2-849d-40b5-8629-09644ebb32c6`)
- S28: [铝合金熔铸问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc5b0e67-a702-406d-a565-0bf5e1976043/resource) (`bc5b0e67-a702-406d-a565-0bf5e1976043`)
- S24: [engineering design handbook military pyrotechnics series part three prop__65a1021877](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7a294c3-4216-4c01-a65e-4522ac19bfaf/resource) (`a7a294c3-4216-4c01-a65e-4522ac19bfaf`)
- S19: [engineering design handbook military pyrotechnics series part three prop__65a1021877](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8167ffc7-1c4f-44dd-a434-3037759f3a5a/resource) (`8167ffc7-1c4f-44dd-a434-3037759f3a5a`)
- S37: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9714c2e-8d3d-4f15-ba37-2deba0ed3065/resource) (`e9714c2e-8d3d-4f15-ba37-2deba0ed3065`)
- S33: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d01a9521-5f48-48e8-a51a-f8df969dcc1f/resource) (`d01a9521-5f48-48e8-a51a-f8df969dcc1f`)
- S39: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea4218c5-2d84-48f9-982c-cba8f40c0679/resource) (`ea4218c5-2d84-48f9-982c-cba8f40c0679`)
- S9: [铝合金金属型铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5376dd1c-f5bb-46e0-9ea0-9f6606d8a34a/resource) (`5376dd1c-f5bb-46e0-9ea0-9f6606d8a34a`)
- S21: [中国航空材料手册第3卷铝合金镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94825934-fb51-483a-9f96-cb5e3dc7ef81/resource) (`94825934-fb51-483a-9f96-cb5e3dc7ef81`)
- S27: [实用有色合金铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbce77b4-6b00-4e1d-8390-653b9a62a5ce/resource) (`bbce77b4-6b00-4e1d-8390-653b9a62a5ce`)
- S8: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45b08eb3-2cff-40a2-b44e-aae4b8ec04fd/resource) (`45b08eb3-2cff-40a2-b44e-aae4b8ec04fd`)
- S4: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3601e861-6820-4de5-8d65-69b3e822981c/resource) (`3601e861-6820-4de5-8d65-69b3e822981c`)
- S18: [铝及铝合金工艺与设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e9281ff-de47-485e-a8e7-923834b8c092/resource) (`7e9281ff-de47-485e-a8e7-923834b8c092`)
- S23: [铝合金熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a78d79f7-a473-404e-9ebe-e07c3e83bcd7/resource) (`a78d79f7-a473-404e-9ebe-e07c3e83bcd7`)
- S16: [向制块用模具模体中填入精炼剂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7822bdf2-8b59-4749-a47a-5f584bc43305/resource) (`7822bdf2-8b59-4749-a47a-5f584bc43305`)
- S32: [图4-19 铝合金熔炼工艺流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9c0c183-0b36-4746-8e48-25473844c2bb/resource) (`c9c0c183-0b36-4746-8e48-25473844c2bb`)
- S1: [有色合金铸造经验选编](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b20020f-8fdb-4a12-ab99-e6e38f15ddd7/resource) (`0b20020f-8fdb-4a12-ab99-e6e38f15ddd7`)
- S6: [铝合金常用精炼剂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b98628d-a1c3-44a8-be58-a6174c616ad2/resource) (`3b98628d-a1c3-44a8-be58-a6174c616ad2`)
- S22: [六氯乙烷处理镁合金工艺生产的铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96f0175b-b59b-4b79-b9c3-0c4db8955f8e/resource) (`96f0175b-b59b-4b79-b9c3-0c4db8955f8e`)
- S35: [六氯乙烷处理镁合金工艺生产的铸件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d586dcad-5d34-43ed-af22-c6a3e1d819a5/resource) (`d586dcad-5d34-43ed-af22-c6a3e1d819a5`)
- S26: [铝合金石膏型精密铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b64045ce-fc69-491e-9dd5-c6c575c6d87b/resource) (`b64045ce-fc69-491e-9dd5-c6c575c6d87b`)
- S2: [b0724 effects of hydrogen in aluminium and its alloys__c7ea403511](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2841d29e-8c6f-4ad7-9d0c-a3e1723b341b/resource) (`2841d29e-8c6f-4ad7-9d0c-a3e1723b341b`)
- S7: [铸造铝合金用精炼剂表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/459794b8-faff-4553-825d-ce9263e065bb/resource) (`459794b8-faff-4553-825d-ce9263e065bb`)
- S3: [图1-1 ZL101合金含氢量与六氯乙烷精炼剂用量的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3393591a-8acf-48da-807f-a39a0f57d8b5/resource) (`3393591a-8acf-48da-807f-a39a0f57d8b5`)
- S38: [图7.3 C₂Cl₆对铝熔体中钙含量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea1b0023-d87f-493b-b451-b2b3002791a1/resource) (`ea1b0023-d87f-493b-b451-b2b3002791a1`)
- S11: [die casting metallurgy metal melting treatments__79af757f26](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63e40055-dbfa-4875-89cf-e9f0352450be/resource) (`63e40055-dbfa-4875-89cf-e9f0352450be`)
- S5: [die casting metallurgy__8f9e04f2f0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b0a9bd8-114d-4e31-a5a9-090df9eea2a3/resource) (`3b0a9bd8-114d-4e31-a5a9-090df9eea2a3`)
- S31: [铝合金无缝管生产原理与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c6224439-3c35-40ec-91af-4d0ca101a9cb/resource) (`c6224439-3c35-40ec-91af-4d0ca101a9cb`)
- S40: [castings practice the 10 rules of castings__f50e38f53d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb199dfe-f660-4f85-aa05-7f5ba66c1468/resource) (`eb199dfe-f660-4f85-aa05-7f5ba66c1468`)
- S30: [castings practice the ten rules of castings__89e66a79d0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c41e5f0d-e96d-4216-b857-f0f7198f3ae4/resource) (`c41e5f0d-e96d-4216-b857-f0f7198f3ae4`)
- S34: [铝与铝合金材料生产技术500问](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2f804ff-93c8-4f10-b3bd-af60509b7210/resource) (`d2f804ff-93c8-4f10-b3bd-af60509b7210`)
- S36: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3bc31c4-7539-4459-b966-17c4f51b1793/resource) (`e3bc31c4-7539-4459-b966-17c4f51b1793`)
- S25: [实用压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab3e03a7-2d53-4f2e-8987-538eee32befd/resource) (`ab3e03a7-2d53-4f2e-8987-538eee32befd`)
- S29: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd423316-a69c-444a-902d-0976c1cd6573/resource) (`bd423316-a69c-444a-902d-0976c1cd6573`)
- S13: [有色金属熔炼工基本操作技能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c12880c-86b0-4cf0-bd53-902d944f4641/resource) (`6c12880c-86b0-4cf0-bd53-902d944f4641`)