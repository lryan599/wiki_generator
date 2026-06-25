---
version: "v1"
generated_at: "2026-06-18T10:07:36+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 32
  source_quality_score: 0.84
  freshness_score: 0.93
  evidence_coverage_score: 1.0
---

## 概述

SiO₂（二氧化硅）在铜及铜合金冶金中属于典型的酸性非金属氧化物夹杂物。其熔点远高于铜的熔化温度，在熔融铜液中呈固态悬浮状态，常规脱氧操作无法将其还原去除，须通过碱性精炼熔剂（如碳酸钠、石灰）与其反应生成低熔点复合硅酸盐化合物，促使其汇聚为大液滴后从铜液中排出[[S22]]。SiO₂夹杂的存在会破坏铜基体组织的连续性，引发局部应力集中，成为裂纹萌生的核心源头，降低铜合金的强度、塑性、韧性及疲劳强度，并损害材料的导电、导热和耐腐蚀性能[[S25,S8,S19]]。

近年来，脉冲电流处理作为一种非接触型物理净化手段受到关注。实验室研究表明，利用SiO₂与铜熔体之间的电导率差异，可驱动该类夹杂物向阴极定向迁移，从而在中部形成净化区。

## 分类与形态

在非金属夹杂物分类体系中，SiO₂归属于铜合金中高熔点、难还原的不溶氧化夹杂物[[S22]]。按化学酸碱性划分，其为酸性氧化物，需配合碱性熔剂造渣去除[[S22]]。

SiO₂在铜合金中的存在形态包含晶态（石英、方石英）和无定形两种。铜合金冶炼过程中生成的SiO₂夹杂大多呈黑色圆整或近椭圆形；在未经电流处理的铜基体中，该类夹杂易形成条状密集聚集、弯曲线段聚集或环形聚集等典型聚集形貌[[S31,S3]]。

**SEM-EDS形貌图示**如下：

![无氧铜基体中SiO₂夹杂物的SEM形貌及Si元素EDS面扫分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50e49c47-9a60-4ba8-affe-4eecf8bbbecb/resource)

图源：实验用高纯无氧铜（TU0）内添加SiO₂夹杂物的SEM和EDS成分分析图像，形貌与面扫结果确认黑色嵌入物为含Si元素的二氧化硅氧化物[[S10]]。

## 来源与形成机制

铜熔炼、保温和浇注全流程中SiO₂夹杂的生成来源主要包含以下三类[[S19,S8]]：

1. **耐火材料侵蚀**：炉衬等耐火材料受高温铜液侵蚀剥落进入熔体；
2. **内生脱氧产物**：铜液中硅元素被氧化生成的脱氧反应产物；
3. **炉渣卷入**：熔炼浇注过程中炉渣意外卷入。

三类路径的具体占比目前无公开明确的实测数据，暂存疑[[S19,S8]]。

## 物理化学特性

### 基本物性

铜液及相关夹杂物的物理性能对比如下表所示[[S16]]：

| 材料 | Cu | C（石墨电极） | Fe₂O₃ | Al₂O₃ | SiO₂ |
|------|-----|-------------|--------|--------|------|
| 密度（g/cm³） | 8.90 | 2.25 | 3.58 | 2.70 | 2.2 |
| 熔点（°C） | 1083 | 3652 | 2852 | 2054 | 1723 |
| 电导率（Ω/m） | 1.7×10⁻⁸ | 8×10⁻⁶ | 绝缘 | 绝缘 | 绝缘 |

SiO₂的电导率为绝缘态，这是其与高导铜熔体在脉冲电场下产生差异化受力、实现定向迁移的核心物理基础[[S16]]。

### 尺寸分布与上浮特性

铜液中SiO₂夹杂的典型尺寸分布以1～3.5 μm为主，部分大尺寸颗粒可达约10 μm，极少数尺寸可超过20 μm。未通电处理的空白铜样顶部区域的SiO₂平均尺寸明显高于中部位置[[S3]]。

基于SEM统计的一项实测数据显示，30个SiO₂夹杂的直径范围为0.50 μm～4.60 μm[[S6]]：

| 项目 | 最大直径（μm） | 最小直径（μm） |
|------|----------------|----------------|
| 范围 | 0.50～4.60 | — |
| 上限 | 4.59 | — |
| 下限 | — | 0.50 |

1100°C高温下熔融铜的密度为7.96 g/cm³，SiO₂的密度（约2.2 g/cm³）显著低于铜液。依据斯托克斯定律，微米级SiO₂颗粒的上浮速度极慢，难以自发完全从铜液中排出，易长时间悬浮在熔体内部[[S29]]。

高温铜液与SiO₂之间的润湿性公开系统实测数据稀缺，暂存疑[[S29]]。

## 压铸相关性

含SiO₂夹杂的铜合金压铸件在机加工打磨过程中，高硬度的SiO₂夹杂物会形成表面硬质点，造成刀具异常磨损、加工面出现不规则撕裂凹坑等打磨缺陷，大幅提升压铸工艺的加工适配难度[[S21]]。

## 脉冲电流处理下的迁移行为

### 迁移方向与驱动机制

在脉冲电场作用下，铜熔体中的SiO₂夹杂向**阴极**定向迁移[[S26,S5]]。这一迁移行为的驱动机制与常规水溶液体系的电泳或电渗流效应存在本质区别：

- SiO₂以氧化硅状态存在于铜液中时，其Si的氧化态有效电荷数为+4，在电场作用下受电子风力驱动而向阴极富集[[S28,S11]]；
- 高导电铜液中，电子风力在夹杂迁移中发挥主导作用，而非电渗流或电泳[[S28,S11]]；
- 现有公开实验尚未直接测得铜熔体与SiO₂界面的Zeta电位及双电层结构参数[[S26,S5,S28]]。

**处理前后夹杂分布对比图**如下：

![脉冲电流处理与未处理无氧铜样品中SiO₂夹杂物的形貌分布对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aef9311c-178e-45cc-af91-634f47c43323/resource)

图源：(a-c) 脉冲电流处理样品中SiO₂夹杂物沿电场方向分散定向分布；(d-f) 未处理空白样品中SiO₂呈条状、弯曲状、圈内聚集的典型聚集态形貌[[S24]]。

### 电流阈值

在1 kg、约1202°C（1475 K）高纯无氧铜（TU0）熔体、石墨电极四分之一插入深度的实验条件下，SiO₂有效定向迁移的特征电流阈值约为**15 A**[[S17,S11]]。电流大小与迁移行为的关联如下：

- 电流低于15 A时：SiO₂沿正负极方向定向迁移规律稳定；
- 电流超过15 A时：过大的电流产生显著的焦耳热，加剧熔融铜原子的不规则热运动，对SiO₂夹杂的定向迁移产生干扰；
- 电流大于50 A时：向阴极的迁移趋势重新显现[[S17]]。

COMSOL多物理场仿真表明，上述铜熔体在15～100 A脉冲电流作用下，内部电流密度区间约为3×10²～6×10³ A/m²，电极附近电流密度最高，中部区域电流密度低于电极附近的一半[[S32]]。

铜熔体自身电导率的波动会直接改变电场驱动力的强度；焦耳热效应随电流增大而快速提升，是形成电流阈值的主要原因[[S7,S17]]。

### 频率的影响

脉冲频率对SiO₂迁移行为的影响规律如下[[S23,S11]]：

| 频率区间 | 迁移特征 | 主导机制 |
|----------|----------|----------|
| < 50 Hz（低频） | 低频共振产生的熔融原子搅拌作用过大，超过电迁移的物理控制范围，无法实现稳定定向迁移 | 热振动干扰 |
| 50 Hz（中频） | SiO₂从铸锭顶端至底端含量逐步递增，势能差作用占主导；负极附近夹杂富集峰值可达1.45 wt% | 势能差主导迁移 |
| 500～2000 Hz（高频） | 向阴极迁移的驱动力进一步提升，电子风力主导驱动 | 电子风力主导 |

在更高频率（如2000 Hz）下，阴极迁移效果可达最佳，但针对SiO₂的整体最佳净化频率参数经二次优化实验确定为**50 Hz**[[S26,S11]]。

### 净化效果（定量）

脉冲电流处理前后的核心净化效果对比数据如下[[S17,S26]]：

| 指标 | 数值 |
|------|------|
| 未通电空白组中心区域SiO₂质量分数 | 0.941 wt% |
| 15 A / 50 Hz / 四分之一插入深度处理后中部SiO₂含量 | 约 0.3 wt% |
| 微米级SiO₂大颗粒夹杂去除率 | 最高可达 70% |

经脉冲电流处理后，铸锭中部形成明显的净化区，而阴极（负极）顶部成为SiO₂的主要富集区域，夹杂含量显著高于其他部位[[S26,S5]]。

### 尺寸分布的电场调控

脉冲电流处理后SiO₂夹杂的尺寸分布呈现以下规律[[S26]]：

- **大尺寸SiO₂**：偏聚于熔体顶部，因较大浮力克服电场力的作用；
- **小尺寸SiO₂**：在中部电场力作用下分布更加均匀；
- **底部区域**：仅残留少量大尺寸SiO₂，系因电势能差最大、电自由能驱动作用所致。

## 工艺参数（最佳净化阈值）

基于1 kg高纯无氧铜熔体的实验室单因素优化实验，针对SiO₂夹杂的最佳脉冲电流净化工艺参数如下[[S26,S11,S13]]：

| 工艺参数 | 最佳值 |
|----------|--------|
| 电极插入深度 | 熔体总高度的**1/4** |
| 迁移电流阈值 | **15 A** |
| 脉冲频率 | **50 Hz** |
| 脉冲波形 | 单向脉冲矩形波 |
| 电压 | 4.8 V |
| 处理时长 | 5 分钟 |
| 熔体温度 | 约1475 K（≈1202°C） |
| 电极材料 | 石墨 |

电极插入深度是影响净化效果的关键工艺因素：全插入电极主要起到均匀化夹杂分布的作用，无法实现高效定向迁移除杂；四分之一插入深度可实现中部净化区的最高去除率[[S17,S12]]。

值得注意的是，针对Fe₂O₃夹杂的最佳净化阈值参数不同，为电流50 A、脉冲频率1000 Hz，表明不同夹杂物类型需匹配不同的工艺参数[[S11,S13]]。

## 工艺比较

脉冲电流净化工艺与传统铜液净化方法的核心对比如下：

| 净化方法 | 优势 | 局限 |
|----------|------|------|
| 脉冲电流处理 | 纯物理过程，不引入新杂质；操作便捷，功耗极低（低频可至0.001 W）；可富集纳米级微小绝缘夹杂 | 目前限于实验室1 kg量级研究，大体积熔体电场分布困难 |
| 气体浮选 | 工艺成熟 | 气体消耗量大，微小夹杂去除效率低 [[S33,S27,S30]] |
| 多孔陶瓷过滤 | 对大尺寸夹杂有效 | 滤芯损耗大，无法过滤尺寸小于滤芯孔径的超细夹杂 [[S33,S27,S30]] |
| 熔剂精炼 | 对酸性夹杂物可形成低熔点复合盐排出 | 引入熔剂杂质元素，降低高纯铜产品最终纯度 [[S33,S27,S30,S22]] |

## 工艺限制与放大挑战

脉冲电流去除铜液中SiO₂夹杂的技术目前仍处于实验室研究阶段，无公开的商用落地记录[[S11,S17]]。现有实验针对1 kg量级无氧铜熔体开展，向大规模量产推广面临以下核心瓶颈[[S15,S1,S9]]：

1. 大体积铜熔体内部难以获得均匀分布的电场；
2. 焦耳热分布不均会导致不同区域的除杂效果差异显著；
3. 难以精准匹配大处理量场景下不同位置的夹杂物迁移阈值参数；
4. 现有实验仅验证了小体积熔态工况，放大后极易出现异常偏析问题。

## 相关标准

**国内标准**：

- **GB/T 13819-2013《铜及铜合金铸件》**：对铜及铜合金铸件中非金属夹杂物提出质量控制要求，通常参照显微金相检测法进行夹杂物评级评定[[S35,S34]]。该标准下SiO₂夹杂的明确允许限值无单独公开条款，暂存疑[[S35,S34]]。
- **GB/T 10561-2005**：可参照用于延伸变形铜材中非金属夹杂物的显微评级；C类硅酸盐类夹杂物中即包含SiO₂相关成分[[S35]]。

**国际标准**：

- **ASTM E45**《钢中非金属夹杂物含量测定方法》及 **ASTM E1245**《通过自动图像分析测定钢和其他金属中内生非金属夹杂物含量的标准实施规程》：均为适用于铜及铜合金的非金属夹杂物通用显微评定标准，包含对SiO₂类氧化物夹杂的评级分类规则[[S2,S20]]。

## Sources
- S22: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9de46bb5-dcd6-450e-83ec-75127dda05bb/resource) (`9de46bb5-dcd6-450e-83ec-75127dda05bb`)
- S25: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b00e3400-0646-42e1-ba3d-15b9d0871a0a/resource) (`b00e3400-0646-42e1-ba3d-15b9d0871a0a`)
- S8: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42e2c36c-a69c-4d8b-b1b1-2bc23803b796/resource) (`42e2c36c-a69c-4d8b-b1b1-2bc23803b796`)
- S19: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91db5a92-4e00-4f8c-94cf-bc4687bec7e5/resource) (`91db5a92-4e00-4f8c-94cf-bc4687bec7e5`)
- S31: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea2481cd-fb2c-4cad-8dc7-e55a008f7502/resource) (`ea2481cd-fb2c-4cad-8dc7-e55a008f7502`)
- S3: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fef6c24-cc71-4234-8fda-6a7c89cf66bf/resource) (`1fef6c24-cc71-4234-8fda-6a7c89cf66bf`)
- S10: [图3.1 无氧铜(TU0)样品内添加的Si类夹杂物的SEM和EDS图像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50e49c47-9a60-4ba8-affe-4eecf8bbbecb/resource) (`50e49c47-9a60-4ba8-affe-4eecf8bbbecb`)
- S16: [表1.1 铜液及主要杂质的物理性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80abb2a4-5a99-4d84-9d02-5268da5b11f8/resource) (`80abb2a4-5a99-4d84-9d02-5268da5b11f8`)
- S6: [表3.1 image pro plus杂质尺寸计算参考表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2dd0e77e-4942-4622-b264-75bbb992eb7b/resource) (`2dd0e77e-4942-4622-b264-75bbb992eb7b`)
- S29: [continuous casting proceedings of the international conference on contin__bf26ef8a84](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0313b18-ee89-477b-b930-05dc5236a5c4/resource) (`c0313b18-ee89-477b-b930-05dc5236a5c4`)
- S21: [die casting metallurgy__322fa9dd3c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/996e306f-c27b-4a80-b1c0-e1cacef360d5/resource) (`996e306f-c27b-4a80-b1c0-e1cacef360d5`)
- S26: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b08752f8-b85b-4dee-8f61-2c045eecb6e4/resource) (`b08752f8-b85b-4dee-8f61-2c045eecb6e4`)
- S5: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d1efdc0-6ac6-4c7e-9f21-d838033d01f3/resource) (`2d1efdc0-6ac6-4c7e-9f21-d838033d01f3`)
- S28: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2685b34-706b-4ddc-84cf-109007d3410a/resource) (`b2685b34-706b-4ddc-84cf-109007d3410a`)
- S11: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55e86128-555e-475b-b779-3b8a11bbdf2b/resource) (`55e86128-555e-475b-b779-3b8a11bbdf2b`)
- S24: [图3.3 SEM显示铜基体中SiO₂夹杂物的形态与分布：(a-c)脉冲电流处理样品的迁移态SiO₂；(d-f)未处理样品的聚集态SiO₂](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aef9311c-178e-45cc-af91-634f47c43323/resource) (`aef9311c-178e-45cc-af91-634f47c43323`)
- S17: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89110fcc-e3ad-42dd-9d9e-d876ca91f49f/resource) (`89110fcc-e3ad-42dd-9d9e-d876ca91f49f`)
- S32: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb38a6ab-c086-4953-8d45-ce4d97e69ebb/resource) (`eb38a6ab-c086-4953-8d45-ce4d97e69ebb`)
- S7: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3f4485da-f342-4300-9529-7bdccd3a7b4e/resource) (`3f4485da-f342-4300-9529-7bdccd3a7b4e`)
- S23: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6cc89d6-ec39-4065-8bb0-c7da68945ac2/resource) (`a6cc89d6-ec39-4065-8bb0-c7da68945ac2`)
- S13: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b78d198-45ae-4b5f-a32d-0861713c73b9/resource) (`5b78d198-45ae-4b5f-a32d-0861713c73b9`)
- S12: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/577d2168-adf0-4bda-9495-35f6bb44fd80/resource) (`577d2168-adf0-4bda-9495-35f6bb44fd80`)
- S33: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efd5cbdb-3c3a-4fcd-88f3-f21d9049049a/resource) (`efd5cbdb-3c3a-4fcd-88f3-f21d9049049a`)
- S27: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1166a66-ed90-465e-9f4a-1f5c297223c2/resource) (`b1166a66-ed90-465e-9f4a-1f5c297223c2`)
- S30: [continuous casting proceedings of the international conference on contin__bf26ef8a84](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2e52cb1-c51b-434c-a610-8cd9370d8555/resource) (`c2e52cb1-c51b-434c-a610-8cd9370d8555`)
- S15: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/704ace30-9a05-43f8-813f-2ae1740e33b4/resource) (`704ace30-9a05-43f8-813f-2ae1740e33b4`)
- S1: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/005deec9-ffe7-494c-9a2b-a0a2238d83c7/resource) (`005deec9-ffe7-494c-9a2b-a0a2238d83c7`)
- S9: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50399d17-cde8-45b3-9546-64c44c8b4dd9/resource) (`50399d17-cde8-45b3-9546-64c44c8b4dd9`)
- S35: [主管道用奥氏体不锈钢组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f2577d13-c150-4622-8e64-af13655b9a60/resource) (`f2577d13-c150-4622-8e64-af13655b9a60`)
- S34: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0255e63-8f14-41e6-81b0-b950582bc7c4/resource) (`f0255e63-8f14-41e6-81b0-b950582bc7c4`)
- S2: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a9e1487-78d2-4ac1-9bd9-3dc5013340f8/resource) (`0a9e1487-78d2-4ac1-9bd9-3dc5013340f8`)
- S20: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94e25254-34cd-4606-b3ad-7de60902f71f/resource) (`94e25254-34cd-4606-b3ad-7de60902f71f`)