---
version: "v1"
generated_at: "2026-06-18T13:43:30+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 45
  source_quality_score: 0.87
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

铁（Fe）在铸造铝合金中是极为常见的伴生元素，因其在铝基体中的平衡固溶度极低而几乎全部以第二相形式析出。在压铸铝合金中，Fe兼具“有益工艺元素”与“有害杂质”的双重属性：适量Fe可显著减轻合金熔体对模具钢的焊合粘模倾向，改善脱模性；但过量Fe则生成硬脆的针状或片状富铁金属间化合物，严重割裂铝基体，导致合金塑性、韧性和耐蚀性急剧下降[[S4,S10,S11]]。在钛合金领域，Fe作为TC4（Ti-6Al-4V）中的β稳定型杂质元素，受到严格限量控制，并呈现特定的正偏析行为。

## Fe在铝合金中的存在形式与基本特征

Fe在室温下于纯铝中的平衡固溶度仅为约0.02%，共晶温度（655 °C）下的最大固溶度为0.052%，因此工业铝合金中的Fe几乎全部以金属间化合物形式存在于基体中[[S4]]。

常用压铸铝合金中生成的含Fe金属间化合物可归为以下主要类型[[S4,S9,S23]]：

- **二元相Al₃Fe**：呈针状或细条状，显微硬度可达约960 HV，性质硬脆。
- **三元相α-Fe₂SiAl₈（α-Fe相）**：呈骨骼状、汉字状或不规则形状，属于六方晶系，对基体割裂程度相对较轻。
- **三元相β-Al₅FeSi（β-Fe相）**：二维截面呈长针状或针片状，属单斜晶系，与铝基体共格度低，是割裂基体、严重降低合金塑性与冲击韧性的最主要有害相。

下表总结了铝合金中主要富铁相的晶体学特征[[S52]]：

| 富铁相类型 | 化学式（示例） | 典型形貌 | 晶系特征 |
|:---|:---|:---|:---|
| α-Fe相 | α-Fe₂SiAl₈、α-Al₁₅(Fe,Mn)₃Si₂ | 汉字状、骨骼状 | 六方/立方 |
| β-Fe相 | β-Al₅FeSi、β-Al₉Fe₂Si₂ | 针状、针片状 | 单斜 |
| 非平衡相 | — | 多面体状、块状、团状 | 随工艺而异 |

## Fe在不同合金体系中的影响与工业控制区间

### Al-Si系与Al-Si-Cu系压铸合金

在压铸Al-Si及Al-Si-Cu合金中，Fe是最为关键的工艺调控元素之一。铝合金对模具钢具有强烈的亲和粘附倾向，当合金中Fe含量过低时，铝熔体与模具界面之间产生显著的化学势梯度，驱动铁原子由模具向铝液扩散，形成Fe-Al或Fe-Al-Si金属间化合物层，导致严重粘模[[S25,S65]]。

工业实践表明[[S11,S22,S43]]：

- 当Fe质量分数低于0.6%时，粘模现象显著加剧；
- Fe质量分数达到0.6%以上时，粘模风险明显降低；
- 常规压铸铝合金将Fe含量控制在0.8%～0.9%区间时，抗粘模效果最优；
- 工业压铸生产因冷却速度高，可使铝合金中Fe允许质量分数放宽至约1.2%。

但从力学性能与切削加工性角度考量，Fe含量的升高亦伴随负面效应：

- Fe含量处于0.25%～1.7%区间时均可有效抑制焊合粘模，但当Fe超过1.7%时会大幅降低合金延性，生成大量硬脆富铁相，劣化力学性能[[S24]]。
- 压铸铝合金抗拉强度随Fe含量升高呈下降趋势[[S27]]。
- 过量Fe形成硬质点相，加剧刀具磨损，对切削加工性产生不利影响[[S39]]。据报道，当Fe含量由0.7%升高至1.4%时，自动铣削加工刀具寿命出现显著下降[[S57]]。

针对Al-Si-Cu系（如ADC12类合金），工业上将Fe含量控制在0.6%～1.2%作为经验区间：低于0.6%易粘模拉伤，高于1.2%则合金因硬脆而开裂风险增大[[S61]]。

### 高导热铸造Al-Si合金

高导热铸造Al-Si合金对Fe含量有更严格的限值要求。Fe元素会以高硬度富铁相形式分布在基体中，破坏铝基体的连续导热通路，显著降低合金的导热系数[[S16]]。在此类合金设计中，Fe需作为杂质元素加以严格控制。

### 免热处理亚共晶Al-Si合金

免热处理高压铸造Al-Si合金（如AlSi10MnMg类型）为获得高延性，必须严格控制Fe含量。这类合金中Fe含量通常限制在极低水平（部分牌号要求Fe≤0.25 wt.%），但同时需要额外搭配较高的Mn含量以补偿低Fe带来的粘模风险[[S1]]。

当前免热处理压铸铝合金多基于Al-7Si至Al-10Si成分窗口设计，通过精准控制Fe、Mn、Sr、V、Zr等微合金元素的协同配比，将针状铁相转化为危害更小的汉字状/等轴状形貌，在免去热处理工序的条件下获得高延伸率与优良的铸造充型性能[[S20]]。

### Al-Mg系与Al-Mg-Sc系合金

在Al-Mg系压铸合金中，Fe是严格控制的有害杂质元素[[S4]]：

- 一般要求Fe含量控制在0.4%以下，部分高耐蚀牌号进一步要求Fe + Si总量不超过0.4%。
- 过量Fe会形成硬脆富铁相，显著降低合金塑性与耐腐蚀性能。

对于Al-Mg-Sc系高性能铝合金而言，Fe作为杂质元素需控制在极低水平。过量Fe会与Al、Sc等元素形成硬脆金属间化合物，抵消Sc元素的细晶强化效果，并降低合金的焊接性能与低温韧性[[S64]]。

## 过量Fe的有害作用与组织表现

当铝合金中Fe含量超出允许上限时，主要产生以下有害作用[[S10,S11,S59]]：

- **降低塑性与冲击韧性**：Fe以FeAl₃、β-Al₅FeSi等片状或针状组织分布于基体中，形貌粗大，严重削弱基体连续性，使合金塑性显著下降。
- **增大热裂倾向**：过量Fe降低合金流动性，增加凝固过程中的热裂风险。
- **降低耐蚀性**：富铁相的电极电位高于铝基体，破坏铝表面氧化膜的连续性，降低合金耐腐蚀性能[[S2,S4]]。
- **劣化切削加工性与表面质量**：粗大的初生富铁相形成硬质点，降低机加工表面质量并加速刀具磨损[[S39]]。

关于富铁相形貌与Fe含量的关系，在Al-Si合金中[[S32]]：

- Fe含量为0.2～0.5 wt.%时，富铁相主要为细小针状β-Fe相，分布于α-Al基体晶界处，典型长度约20 μm；
- Fe含量达到1.2 wt.%左右时，出现粗大板条状β-Fe相，长度可超过100 μm，贯穿多个初生α-Al晶粒和共晶区。

此外，冷却速率对富铁相形貌尺寸影响显著：冷却速度越快，富铁相越细，长度显著降低，但在合金成分固定的前提下，冷却速率改变不会改变富铁相的物相类型，仅对其形貌和分布产生作用[[S29]]。

图1展示了富铁相的X射线面分布特征，可直观反映Fe元素在基体中的二维分布轮廓和富集形态，为富铁相鉴别与表征提供基础依据[[S55]]。

![铝合金中铁元素面分布X射线映射结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da1520f3-c93c-4b56-8480-e8ff9c1dd612/resource)

## 主要工业牌号中的Fe限量标准

不同铸造工艺与性能要求下，各合金体系对Fe上限的限定存在显著差异。下表汇总了典型工业牌号的Fe含量限量要求：

| 合金体系/牌号 | 对应标准 | Fe限量（最大值，wt.%） | 说明 |
|:---|:---|:---|:---|
| ADC12 | JIS H5302-2006 | ≤1.3 | 低管控版本可降至≤0.9 [[S30]] |
| A380 | ASTM B85-1996 | ≤2.0 | 压铸专用，较高铁含量利于脱模 [[S19,S33]] |
| A356 | ASTM B26/B26M-1988 | ≤0.2 | 砂型铸造，高塑性要求，严格限铁 [[S63]] |
| A319 | ASTM B26/B26M-1988 | ≤1.0 | 砂型铸造 [[S56]] |
| YL113（对应ADC12） | GB/T 15115 | ≤1.3 | 国内压铸铝合金标准 [[S12,S18]] |
| TC4钛合金 | GB3620-83 | ≤0.40 | Fe为β稳定型杂质元素 [[S28,S47]] |

## Fe与模具粘模/脱模性的定量关系

Fe元素调控是抑制压铸铝合金粘模缺陷的核心冶金手段。其机制在于：合金中Fe含量越接近工作温度下其在铝中的饱和溶解度时，铁元素的化学势梯度大幅降低，熔融金属向模具钢焊合的驱动力显著减弱[[S65]]。

在常规非高韧性压铸铝合金中，当Fe含量控制在0.8～1.1 wt.%时，可有效抑制焊合趋势，Fe含量为1.1%合金的粘模倾向远低于Fe含量为0.8%的合金[[S65]]。

低Fe含量的高韧性免热处理压铸铝合金无法依靠自身Fe元素抑制粘模，需额外搭配较高Mn含量来实现防粘模效果[[S1]]。

图2展示了通过控制Fe含量来抑制粘模缺陷的压铸系统结构示意，其中模具与铸件的界面结合状态直接受合金Fe含量调控影响[[S7]]。

![通过控制铁含量抑制粘模的铝硅镁合金压铸系统结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e9f66b6-0f67-44b1-bc87-5885036f5201/resource)

## Fe元素的偏析行为

### 铝合金铸锭中的Fe偏析

铝合金铸锭中Fe元素的分布呈现典型的径向偏析特征：铸锭外围区域表现为负偏析（Fe含量低于名义成分），芯部区域表现为正偏析（Fe含量高于名义成分）。此种偏析分布会使铸锭沿径向不同位置的成分均匀性下降，从而影响后续加工产品的力学性能一致性[[S45]]。

### TC4钛合金铸锭中的Fe偏析

在TC4（Ti-6Al-4V）钛合金真空自耗熔炼铸锭中[[S49]]：

- Fe属于正偏析元素且偏析程度最为显著（同样为正偏析的还有V，Al则为负偏析元素）。
- Fe元素在铸锭截面上呈现钟形分布特征：外层区域为负偏析，心部区域为正偏析，不同铸锭高度位置的Fe浓度分布存在差异。
- 一次铸锭的宏观偏析对二次铸锭的偏析具有遗传效应，一次铸锭顶部偏析较为严重。

国标GB3620-83对TC4钛合金中Fe杂质含量规定为最高不超过0.40 wt.%[[S28,S47]]。

## 富铁相的中和变质调控

### Mn元素的变质作用

Mn是工业上应用最广、成本最低的铝合金富Fe相中和变质元素。Mn的原子半径和晶体结构与Fe相近，可通过扩大α-Fe相区，将针状β-Al₉Fe₂Si₂相转变为形貌更为缓和的汉字状、鱼骨状、花卉状甚至多面体状的AlSiFeMn四元相，大幅降低针状富铁相割裂铝基体的危害，起到恢复合金强度与延伸率的作用[[S6,S31]]。

w(Mn)/w(Fe)比值对富铁相形貌的转变具有决定性影响[[S36]]：

| w(Mn)/w(Fe) 比值 | 富铁相形貌特征 |
|:---|:---|
| 0.5 | 以针状相为主，出现极少量汉字状铁相 |
| 0.8 | 汉字状铁相占比提升，仍残留大量针状相 |
| 1.1 | 汉字状铁相大量分布，针状相数量显著减少、尺寸缩小 |
| 1.4 | 几乎全部转变为汉字状相 |

压铸工业中推荐的Mn中和Fe质量比为w(Mn)/w(Fe) = 0.67～0.83，在此区间内可在较低合金添加成本下实现富铁相的有效变质[[S2,S10,S17,S59]]。从铁相形貌调控的通用准则来看，维持Mn/Fe比值大于0.5即可产生有效的相转变效应[[S9]]。

### Cr元素的变质作用

Cr元素同样可实现对铝合金富Fe相的中和变质作用。当Cr含量逐步增大时，富铁相形貌会依次由针状向汉字状、块状、团状转变，推荐的工业配比为w(Cr)/w(Fe) = 0.35:1。经Cr变质后形成的Al₁₂(CrFe)₃Si复杂耐热相不仅消除了针状相的危害，还可同步提升合金的高温性能[[S13,S59]]。

### Be元素的变质作用

少量Be添加（质量分数0.05%～0.1%）亦可将原本针状的β-Fe相转变为点状的Al₅BeFeSi相，消除硬脆针状相的脆性危害。但Be单质及其氧化物存在毒性，工业应用时需做好严格职业防护[[S2]]。

## Fe对高温性能的双重作用

在部分高温铝硅合金体系中，适量Fe形成的热稳定富铁相可钉扎晶界，阻碍高温条件下晶界滑移，从而提升合金的高温抗蠕变性能；但过量粗大的铁相则会作为裂纹源，加速蠕变过程中微裂纹的萌生与扩展，反而降低合金的长期高温服役寿命[[S8]]。

## 富铁相的检测与表征

在金相观察中，仅通过形貌鉴别富铁相种类容易出现误判。例如，同为汉字状形貌的Al₆(FeMn)相与α-Fe相在光学显微及扫描电镜下高度相似，必须借助EDS能谱分析加以区分：不含Si元素的为Al₆(FeMn)相，含Si元素的则为α-Fe相[[S37]]。

富铁相金相观测与EDS表征的标准操作要点参考如下[[S44]]：

- **试样制备**：依次使用#600、#1200、#2000 SiC砂纸粗磨和精磨，分别以0.5 μm和2.5 μm金刚石抛光剂粗抛，再以0.05 μm二氧化硅抛光液精抛至无划痕；使用0.5%氢氟酸溶液腐蚀约30 s后，清水冲洗，无水乙醇超声清洗，冷风吹干。
- **SEM-EDS设置**：加速电压20 kV，工作距离8.5 mm，可通过点扫描和面扫描确定物相元素分布。

对于Al-9Si-2Cu-1.2Fe压铸铝合金，在不同工艺条件下合金中的针状富铁相经EDS能谱分析均被标定为β-Al₅FeSi（β-Fe相），表明挤压处理及冷却速率变化未改变该体系富铁相的物相类型[[S29,S54]]。

## Sources
- S4: [船用铝合金焊接及其船体建造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10834ff0-4bcb-43c0-87a9-36529610601a/resource) (`10834ff0-4bcb-43c0-87a9-36529610601a`)
- S10: [金属压铸模设计技巧与实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22f48744-dd53-4cbb-be01-eae48e663dec/resource) (`22f48744-dd53-4cbb-be01-eae48e663dec`)
- S11: [压铸模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24502175-a504-4d7c-bec4-f97afb0faff9/resource) (`24502175-a504-4d7c-bec4-f97afb0faff9`)
- S9: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/216c1631-0033-4344-ab76-f708ee2a6076/resource) (`216c1631-0033-4344-ab76-f708ee2a6076`)
- S23: [铝合金材料组织与金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48061ca6-76db-4861-b055-dd6c3e38d6ba/resource) (`48061ca6-76db-4861-b055-dd6c3e38d6ba`)
- S52: [表1-2 铝合金中主要富铁相及其晶体学特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9fc6144-7af8-4402-88ce-87de7258df53/resource) (`c9fc6144-7af8-4402-88ce-87de7258df53`)
- S25: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4acee2fb-bd23-4d91-a703-06ced9271984/resource) (`4acee2fb-bd23-4d91-a703-06ced9271984`)
- S65: [die soldering effect of process parameters and alloy characteristics on__f5bc200f9a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fab50f48-98f5-4d56-8ba0-7d60fd6c45ee/resource) (`fab50f48-98f5-4d56-8ba0-7d60fd6c45ee`)
- S22: [压铸工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44a11233-e187-4aed-b494-392b1e2305ba/resource) (`44a11233-e187-4aed-b494-392b1e2305ba`)
- S43: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96c653e0-ccfe-4266-8bf9-870deeb6c07d/resource) (`96c653e0-ccfe-4266-8bf9-870deeb6c07d`)
- S24: [die cast engineering a hydraulic thermal and mechanical process__e5dfda1a8e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a48277f-f365-490a-8af2-3239515af4a7/resource) (`4a48277f-f365-490a-8af2-3239515af4a7`)
- S27: [图3 压铸铝合金抗拉强度与铁含量的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4c7dd419-8b15-459f-b6ed-a646aafc7335/resource) (`4c7dd419-8b15-459f-b6ed-a646aafc7335`)
- S39: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8133575e-ab69-4ad3-b5cb-a378ad55b130/resource) (`8133575e-ab69-4ad3-b5cb-a378ad55b130`)
- S57: [压铸冶金学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df41d41a-8769-4985-845e-8baf044790f8/resource) (`df41d41a-8769-4985-845e-8baf044790f8`)
- S61: [压铸铝合金ADC12产品抛丸起皮原因分析及解决方案推荐](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec9dd8db-d8b9-4b5d-985a-e8a9d8ecd563/resource) (`ec9dd8db-d8b9-4b5d-985a-e8a9d8ecd563`)
- S16: [原铝及其合金的熔炼与铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/380a132b-1e28-4edf-9b68-ce42946363d4/resource) (`380a132b-1e28-4edf-9b68-ce42946363d4`)
- S1: [effect of microstructure and casting defects on the mechanical propertie__7978147656](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04118443-5a6a-4d2a-98e4-3cca5d9fa8ab/resource) (`04118443-5a6a-4d2a-98e4-3cca5d9fa8ab`)
- S20: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/418c41aa-d0e6-40cd-a172-d03a610caabd/resource) (`418c41aa-d0e6-40cd-a172-d03a610caabd`)
- S64: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7e44c89-9c39-4865-816b-0612d0c4a9ff/resource) (`f7e44c89-9c39-4865-816b-0612d0c4a9ff`)
- S59: [铝合金车轮制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e86da82f-1d63-4d0f-b4fc-26aed19b4201/resource) (`e86da82f-1d63-4d0f-b4fc-26aed19b4201`)
- S2: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06731c2f-0d22-4a2f-9d1b-5af683a087a4/resource) (`06731c2f-0d22-4a2f-9d1b-5af683a087a4`)
- S32: [高Fe含量Al-9Si-2Cu合金的微观组织、力学性能与导热性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63b66fb7-757d-4450-aae7-2701f62a4c30/resource) (`63b66fb7-757d-4450-aae7-2701f62a4c30`)
- S29: [高Fe含量Al-9Si-2Cu合金的微观组织、力学性能与导热性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52fd7571-631f-48f8-a5f5-710d39d88b7b/resource) (`52fd7571-631f-48f8-a5f5-710d39d88b7b`)
- S55: [合金中铁元素的X射线映射图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da1520f3-c93c-4b56-8480-e8ff9c1dd612/resource) (`da1520f3-c93c-4b56-8480-e8ff9c1dd612`)
- S30: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S19: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ed805b5-2ea0-42e3-a291-d5267ecc34fa/resource) (`3ed805b5-2ea0-42e3-a291-d5267ecc34fa`)
- S33: [美国标准ASTM B85-96压铸铝合金化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6638f144-4c28-4473-955c-5a9cccd87cac/resource) (`6638f144-4c28-4473-955c-5a9cccd87cac`)
- S63: [美国砂型铸造铝合金的牌号及化学成分（ASTM B26/B26M）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f44baf5f-2925-45ef-b4ae-27f1df18316a/resource) (`f44baf5f-2925-45ef-b4ae-27f1df18316a`)
- S56: [铝合金砂型铸件化学成分表（ASTM B26/B26-88）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da773407-2617-47f9-834d-61e7e241b211/resource) (`da773407-2617-47f9-834d-61e7e241b211`)
- S12: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ac5ad75-6c7f-415e-b4f0-13c0a39b8240/resource) (`2ac5ad75-6c7f-415e-b4f0-13c0a39b8240`)
- S18: [压铸模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d0213f2-a834-47c4-99e7-9a13798a23c8/resource) (`3d0213f2-a834-47c4-99e7-9a13798a23c8`)
- S28: [工程材料实用手册3铝合金镁合金钛合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/503987bc-6fed-4cdb-8adf-98258ae48f53/resource) (`503987bc-6fed-4cdb-8adf-98258ae48f53`)
- S47: [TC4钛合金化学成分表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4ef5472-b89b-4bc3-bb5b-bd902df7072f/resource) (`b4ef5472-b89b-4bc3-bb5b-bd902df7072f`)
- S7: [铝硅镁合金压铸示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e9f66b6-0f67-44b1-bc87-5885036f5201/resource) (`1e9f66b6-0f67-44b1-bc87-5885036f5201`)
- S45: [图5-12 熔炼结束铸锭不同位置处铁元素偏析变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3c4fdee-ee26-4658-bd30-2182aae56470/resource) (`a3c4fdee-ee26-4658-bd30-2182aae56470`)
- S49: [钛合金TC4真空自耗熔炼铸锭质量控制基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0d6c502-8e97-4588-84ec-29d5d66b5fee/resource) (`c0d6c502-8e97-4588-84ec-29d5d66b5fee`)
- S6: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1947ad13-5149-4a60-a8e5-1c18d7f0a600/resource) (`1947ad13-5149-4a60-a8e5-1c18d7f0a600`)
- S31: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59a7de32-aa74-46c7-a2d0-91caf0fdf7b3/resource) (`59a7de32-aa74-46c7-a2d0-91caf0fdf7b3`)
- S36: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6ee75788-569b-4804-ac74-097e2a72b3aa/resource) (`6ee75788-569b-4804-ac74-097e2a72b3aa`)
- S17: [压铸手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a0b49bd-9b4c-412b-bc6e-d2f3118774fb/resource) (`3a0b49bd-9b4c-412b-bc6e-d2f3118774fb`)
- S13: [轻合金车轮制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2fbf784a-e40a-4022-8064-a900234814d1/resource) (`2fbf784a-e40a-4022-8064-a900234814d1`)
- S8: [铁铝金属间化合物合金化与成分设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/213969b7-bb3b-456b-a06a-70a7b776af89/resource) (`213969b7-bb3b-456b-a06a-70a7b776af89`)
- S37: [超声熔体处理和Al-Ti-B协同作用下Al-Cu合金的显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ae594a9-897a-4946-8a79-63ca486bb600/resource) (`7ae594a9-897a-4946-8a79-63ca486bb600`)
- S44: [超声熔体处理和Al-Ti-B协同作用下Al-Cu合金的显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ffcb976-16de-4060-8fdf-a7438ea7fa94/resource) (`9ffcb976-16de-4060-8fdf-a7438ea7fa94`)
- S54: [表3-2 1.2Fe合金富铁相能谱分析结果（at.%）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6329fe8-715e-4bc0-9caa-64840959dfe9/resource) (`d6329fe8-715e-4bc0-9caa-64840959dfe9`)