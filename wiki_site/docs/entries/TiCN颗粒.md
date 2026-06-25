---
version: "v1"
generated_at: "2026-06-18T16:44:35+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 15
  source_quality_score: 0.86
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 定义与组成

TiCN颗粒即钛碳氮化物颗粒，属于TiC–TiN体系中形成的无限置换固溶体，其通用化学式可记为 **Ti(C,N)** 或 **TiC₁₋ₓNₓ**，其中碳/氮原子比可在宽区间内连续调节 [[S17,S1,S14]]。该固溶体在晶体学上与NaCl完全同构，具有面心立方晶格，通过改变C、N元素比例，可以在TiC与TiN的性能区间内按需调整其综合特性 [[S14]]。

## 核心物理性能

TiCN颗粒的综合性能介于纯TiC与纯TiN之间：其显微硬度高于TiN，而韧性与化学稳定性优于TiC [[S14]]。下表汇整了若干关键物理属性的典型范围：

| 性能指标 | 数值范围 | 备注 |
|----------|----------|------|
| 密度（g·cm⁻³） | 4.9 ~ 5.4 | 下限对应TiC，上限对应TiN [[S14]] |
| 熔点（℃） | 2930 ~ 3180 | 下限来自TiN，上限来自TiC [[S14]] |
| 线膨胀系数（10⁻⁶ °C⁻¹） | 7.61 ~ 9.4 | 可在TiC与TiN之间调节 [[S14]] |
| 弹性模量（GPa） | 约460 ~ 550 | 通常参照TiC (460 GPa) 与TiN (~600 GPa) 区间；具体因C/N比而异 [[S4,S14]] |

> 注：精确的弹性模量值在现有来源中未单独列出，但可依据TiC（460 GPa）[[S4]]与TiN的更高模量趋势推估其范围，尚待更多独立实验数据支撑。

## 晶体结构与物相特征

Ti(C,N)固溶体继承NaCl型面心立方结构，Ti原子与C/N原子分别占据交替的八面体位置。由于C和N原子半径差异，晶格常数随C/N比连续变化，从而影响硬度、热膨胀系数等物理性质。这一结构特点使得TiCN在高温下仍能保持较高的化学稳定性与抗氧化性 [[S14,S17]]。

## 粒径分类

参照工程陶瓷粉体的通用分类规则，TiCN颗粒可按平均粒径划分为三类 [[S15,S10]]：

- **微米级 TiCN**：粒径 > 1 μm；
- **亚微米级 TiCN**：粒径在 0.1 ~ 1 μm 区间；
- **纳米级 TiCN**：粒径 < 0.1 μm。

粒径更细的TiCN粉末除可明显提升复合材料的导电性外，还能增强复合陶瓷的常温断裂强度 [[S10]]。典型的微米级增强颗粒粒径分布可参考图1，其中平均粒径约4.79 μm，颗粒多集中在2 ~ 4 μm区间 [[S2]]。

![添加MnO₂的复合材料中TiC颗粒粒径分布直方图，平均粒径4.79μm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ac8bfe5-705c-4b99-8a2c-c6b6b43fa95e/resource)

## 制备方法

工业上主流的Ti(C,N)颗粒合成工艺为 **固相扩散法**：将TiC粉末与TiN粉末按目标碳氮比充分混合，在特定氮气压力氛围下进行高温保温处理，完成固溶反应获得Ti(C,N)固溶体粉末 [[S17]]。为降低合成温度并确保固溶完全，需尽可能减少原料粉末的粒度并保证混合均匀性，否则因扩散不完全会导致产物中残余未反应的TiC或TiN [[S17]]。

另一种路线是将TiN、TiC与粘结相（如Ni、Mo等）粉末直接混合，随后在真空或保护气氛下一步烧结合成Ti(C,N)基金属陶瓷；但该工艺存在明显的脱氮倾向，容易影响最终成分与性能 [[S17]]。

## 在压铸铝合金中的应用

### 用作凝固调控剂与增强体

研究表明，微量 **TiCN‑TiB₂** 复合颗粒可添加于亚共晶Al‑Si‑Mg压铸铝合金中，通过有效细化α‑Al晶粒和调控纳米析出相，同步提升合金的综合力学性能 [[S19]]。尽管该工作中的复合颗粒同时含有TiB₂，但TiCN组分的高硬度与高温稳定性对凝固调控起到了重要作用。

在Al‑10Si合金体系中，研究了 **TiC₀.₅N₀.₅**（即TiCN典型组成）颗粒在凝固前沿的行为：当颗粒半径从20 nm增至100 nm时，其临界运动系数α由0.8降至0.35，此曲线可明确区分颗粒被凝固前沿“推送”与被“吞噬”的区域，对压铸工艺中控制TiCN颗粒的分散状态具有直接指导意义 [[S6]]。

![Al-10Si合金中TiC₀.₅N₀.₅颗粒的临界运动系数α随颗粒半径变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41b687fd-fe86-4450-be93-888111f35d9f/resource)

### 压铸工艺适应性

将TiCN颗粒引入压铸铝基体的可行制备路线之一为“**搅拌铸造 + 高压压铸**”复合工艺。借鉴SiC颗粒增强A356合金的成功经验，采用约 **4 m/s** 的注射速度和 **12 MPa** 左右的压铸压力，能有效降低卷入缺陷，获得高致密度且增强颗粒分布均匀的铸件 [[S5,S11]]。该工艺条件可直接迁移用于TiCN/Al复合材料的半固态或高压压铸生产。

### 强化机制

当TiCN颗粒的尺寸 **< 1 μm** 且均匀分散时，可通过 **Orowan位错钉扎** 机制显著提升铝合金的强度；一旦颗粒发生团聚，有效颗粒间距增大，Orowan强化效应将大幅削弱 [[S3]]。此外，添加少量纳米级陶瓷颗粒（不超过0.5 wt.%）可通过增加异质形核点、降低形核过冷度来细化基体晶粒，从而在几乎不损失延伸率的前提下提高屈服强度、抗拉强度和耐磨性 [[S12]]。这一规律完全适用于TiCN颗粒增强压铸铝合金的性能调控。弥散分布的纳米颗粒典型微观组织可参见图2所示（图中颗粒为TiC/TiB₂，但呈现的弥散特征具有普适参考性）。

![添加TiC/TiB₂纳米颗粒后压铸Al-Zn-Si-Cu合金的SEM显微组织，显示颗粒弥散分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7efebf8-0c79-4eb4-9ade-14266c4d422e/resource)

## 与其他陶瓷增强颗粒的对比

当前压铸铝合金常用陶瓷增强颗粒的性能对比见下表 [[S4,S8]]。TiCN的数值范围基于C/N比可调的特性推估。

| 增强颗粒 | 密度 (g/cm³) | 弹性模量 (GPa) | 熔点 (℃) | 热膨胀系数 (10⁻⁶/℃) | 主要特点 |
|----------|--------------|----------------|-----------|----------------------|----------|
| **SiC** | 3.2 | 480 | 2600 | 4.7 | 综合性价比高，已大规模商用 [[S4,S18]] |
| **TiC** | 4.9 | 460 | 3147 | 7.7 | 高硬度、高热稳定性，但成本较高 [[S4]] |
| **Al₂O₃** | 3.9 | 460 | 2050 | 8.6 | 耐熔体腐蚀，但润湿性差、界面热应力大 [[S8]] |
| **TiB₂** | 4.5 | 550 | 2980 | 7.5 | 与铝共格润湿性好，可异质形核细化晶粒 [[S8]] |
| **TiCN** | 4.9 ~ 5.4 | 约460 ~ 550 | 2930 ~ 3180 | 7.61 ~ 9.4 | C/N比可调，兼具高硬度与良好韧性 [[S14]] |

从实际压铸应用角度评估：

- 与 **SiC** 相比：TiCN颗粒的 **高温抗氧化性更好**，但原料成本偏高 [[S8]]；
- 与 **TiB₂** 相比：TiCN的 **硬度更高、耐磨性更优**，但原位共格润湿性不如TiB₂，且大体积分数下的分散难度更大 [[S8]]；
- 与 **Al₂O₃** 相比：TiCN与铝基体的 **界面结合强度更高**，因而增强效率更突出 [[S8]]。

## 局限与挑战

目前TiCN颗粒作为压铸铝合金增强体仍面临以下主要障碍 [[S8]]：

- **成本较高**：原料合成及粉体处理成本显著高于SiC和Al₂O₃；
- **分散困难**：大体积分数添加时，TiCN颗粒较SiC和TiB₂更易团聚，导致力学性能不均；
- **未形成量产工艺体系**：尚无公开报道的 TiCN增强压铸铝基复合材料商业化牌号或专用标准，工艺成熟度远低于SiC/Al体系。

此外，若在高温熔体中长时间停留，TiCN颗粒与铝基体可能发生界面反应生成脆性相（类似TiC/Al体系中可能出现的Al₃Ti或Al₄C₃），但现有证据尚未明确量化其反应动力学，尚待进一步实验验证。

## Sources
- S17: [工程陶瓷材料的加工技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c264a3ef-2bd4-4ed1-9c9f-0e55458ef66a/resource) (`c264a3ef-2bd4-4ed1-9c9f-0e55458ef66a`)
- S1: [机械加工工艺手册第2卷加工技术卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/081e188e-2b91-4516-87ea-6b7b3ee1601e/resource) (`081e188e-2b91-4516-87ea-6b7b3ee1601e`)
- S14: [表 4-1 超硬镀层中常用高硬度化合物的特性](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8c5d234-0b82-4394-9747-4a699e3f7a33/resource) (`a8c5d234-0b82-4394-9747-4a699e3f7a33`)
- S4: [表2.2 常见增强体陶瓷颗粒的力学及物理性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d0ef352-6ce2-43c8-940e-5c573b9a4f5f/resource) (`2d0ef352-6ce2-43c8-940e-5c573b9a4f5f`)
- S15: [工程陶瓷材料的加工技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae57cb2c-64cb-42dd-add7-1b8317980091/resource) (`ae57cb2c-64cb-42dd-add7-1b8317980091`)
- S10: [工程陶瓷材料的加工技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d232ee6-1bdf-4cc2-96f2-3ed05381cc19/resource) (`8d232ee6-1bdf-4cc2-96f2-3ed05381cc19`)
- S2: [添加MnO₂的复合材料中TiC颗粒粒径分布直方图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ac8bfe5-705c-4b99-8a2c-c6b6b43fa95e/resource) (`1ac8bfe5-705c-4b99-8a2c-c6b6b43fa95e`)
- S19: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part02_p200-254](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5c4c7b7-a928-43a7-b304-987380eaa3c6/resource) (`c5c4c7b7-a928-43a7-b304-987380eaa3c6`)
- S6: [Al-10Si合金中TiC₀.₅N₀.₅颗粒的临界运动速度相关参数随颗粒半径的变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41b687fd-fe86-4450-be93-888111f35d9f/resource) (`41b687fd-fe86-4450-be93-888111f35d9f`)
- S5: [effect of die pressure and injection speed on rheo die casting of a356 s__c32cf2baf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3df5b1c6-b4e9-419a-bb4d-7701cc19d077/resource) (`3df5b1c6-b4e9-419a-bb4d-7701cc19d077`)
- S11: [casting and forming of light alloys__9032155482](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a25373e4-ae62-4a92-8743-3d678938df88/resource) (`a25373e4-ae62-4a92-8743-3d678938df88`)
- S3: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c8d8edf-021d-428f-b86f-82f8a15061ea/resource) (`1c8d8edf-021d-428f-b86f-82f8a15061ea`)
- S12: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a329688b-858d-4fa3-ab33-17e3f4de52d3/resource) (`a329688b-858d-4fa3-ab33-17e3f4de52d3`)
- S8: [TiB2_205A铝基复合材料组织性能及制动盘液态模锻成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7345dbfe-4a88-4ab6-8747-c56145ef2081/resource) (`7345dbfe-4a88-4ab6-8747-c56145ef2081`)
- S18: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c35bb0cd-13d6-4e05-b3fc-caee672c9313/resource) (`c35bb0cd-13d6-4e05-b3fc-caee672c9313`)