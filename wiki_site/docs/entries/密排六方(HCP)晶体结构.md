---
version: "v1"
generated_at: "2026-06-18T15:36:30+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 42
  source_quality_score: 0.87
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述

密排六方（Hexagonal Close-Packed，HCP）晶体结构是金属材料中三种最常见的晶体结构之一，属于六方晶系的简单六方布拉维点阵[[S46,S31,S41]]。其晶胞呈正六棱柱体，原子排列高度致密，配位数为12，原子堆积因子（致密度）为0.74，与面心立方（FCC）结构并列属于最密堆结构[[S46,S31,S39,S33]]。原子层沿c轴方向按ABABAB…顺序交替堆垛，这是与FCC结构ABCABC…堆垛方式的根本区别[[S15,S41]]。

在工业压铸领域，具有HCP结构的典型金属包括镁、锌，部分钛合金在常温下亦为HCP结构[[S46,S31,S28]]。其中，镁及其合金因其极低的密度和优良的压铸工艺适配性，已成为重要的轻量化压铸材料[[S43]]。然而，HCP结构的低对称性导致镁合金在室温下可开动的独立滑移系数目有限，是决定其室温塑性差、压铸过程中易产生热裂等缺陷的根本微观原因[[S21,S32]]。

## HCP晶体结构的定义与几何特征

HCP晶胞属于六方晶系，晶格常数由正六边形底面的边长a和棱柱体高度c两个参数确定[[S9,S15]]。晶胞包含12个顶角原子、上下底面中心各1个原子以及晶胞内部的3个原子，每个晶胞实际占有原子数为：12 × 1/6 + 2 × 1/2 + 3 = 6个[[S46,S31,S24]]。

基于等径刚性球最密堆积模型，理想HCP结构的理论轴比c/a = √(8/3) ≈ 1.633，此时原子堆垛达到几何上的紧密接触[[S41,S22,S11]]。实际HCP金属的轴比因原子并非完美的刚性球而偏离理想值，一般分布在1.57~1.89范围内[[S41,S22,S6,S24]]。

**典型HCP金属的室温轴比（c/a）实例：**

| 金属 | c/a轴比 | 与理想值的偏离方向 |
|------|--------|------------------|
| 理想HCP | 1.633 | — |
| Mg（纯镁） | 1.624 | 略低于理想值 |
| Be | ~1.58 | 显著低于理想值 |
| Cd | ~1.89 | 显著高于理想值 |
| Zn | 高于理想值 | 高于理想值 |
| α-Ti | 低于理想值 | 低于理想值 |

*数据来源*：镁的轴比 ≈1.624 [[S41]][[S40]][[S37]]；Be约1.58，Cd约1.89 [[S41]][[S6]][[S11]]；其他金属来源于[[S41]][[S22]]。

![展示密排六方晶格的晶胞结构，包含六方柱体线框图、原子堆积立体图及原子占据空间示意图，标注晶格常数a和c，用于描述金属晶体结构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afa41abd-acdc-494f-9959-e7119038a069/resource)

**图1** 密排六方（HCP）晶胞结构的三类表达方式：六方柱体线框模型、刚球堆积模型及原子占据空间比例模型，图中标注了晶格常数a（底面边长）与c（柱体高度）[[S34]]。

## 纯镁的HCP晶体学参数

室温下纯镁的密排六方点阵常数测量值为[[S47,S37]]：

- 点阵常数a = 0.32092 nm
- 点阵常数c = 0.52105 nm
- 实际轴比c/a = 1.6236

该值略低于理想轴比1.633，但极为接近，表明镁的原子堆积状态非常接近理想的紧密堆积[[S47,S40]]。有研究指出，通过向镁中添加Li、In、Ag等合金元素可进一步降低c/a比值（如降至1.618以下），从而提高晶格对称性，有助于激活棱柱面等非基面滑移系，改善HCP镁合金的室温塑性变形能力[[S47]]。

## 三种典型晶体结构的对比

金属材料中三种典型晶体结构的关键参数对比如下[[S46,S31,S39,S33,S50]]：

| 结构类型 | 配位数 | 致密度 | 晶胞原子数 | 原子堆垛顺序 | 典型金属 |
|---------|--------|--------|----------|------------|---------|
| 体心立方（BCC） | 8 | 0.68 | 2 | — | α-Fe、Cr、W |
| 面心立方（FCC） | 12 | 0.74 | 4 | ABCABC… | Al、Cu、γ-Fe |
| 密排六方（HCP） | 12 | 0.74 | 6 | ABABAB… | Mg、Zn、Be、α-Ti |

*数据来源*：[[S46]][[S31]][[S39]][[S9]][[S33]][[S26]][[S50]]。

HCP与FCC虽同为最密堆积结构（致密度均为0.74，配位数均为12），但二者的密排面堆垛顺序截然不同：HCP为ABABAB…交替，FCC则为ABCABC…循环[[S15,S41]]。这一差异导致两类结构在塑性变形行为上表现出显著的不同。

## HCP镁合金的滑移系

### 滑移系分类与晶体学参数

在HCP镁合金中，滑移按滑移面分为基面滑移、棱柱面滑移和锥面滑移，按位错柏氏矢量类型分为〈a〉位错滑移和〈c+a〉位错滑移[[S48,S45,S29]]。镁合金的4类主流滑移系参数如下表所示[[S48,S45,S29,S23,S14]]：

| 滑移系类型 | 滑移面 | 滑移方向 | 柏氏矢量 | 独立滑移系数量 |
|-----------|--------|---------|---------|--------------|
| 基面〈a〉滑移 | {0001} | ⟨11<span style="text-decoration: overline;">2</span>0⟩ | a/3⟨11<span style="text-decoration: overline;">2</span>0⟩ | 2 |
| 棱柱面〈a〉滑移 | {10<span style="text-decoration: overline;">1</span>0} | ⟨11<span style="text-decoration: overline;">2</span>0⟩ | a/3⟨11<span style="text-decoration: overline;">2</span>0⟩ | 2 |
| 一阶锥面〈a〉滑移 | {10<span style="text-decoration: overline;">1</span>1} | ⟨11<span style="text-decoration: overline;">2</span>0⟩ | a/3⟨11<span style="text-decoration: overline;">2</span>0⟩ | 4 |
| 二阶锥面〈c+a〉滑移 | {11<span style="text-decoration: overline;">2</span>2} | ⟨11<span style="text-decoration: overline;">2</span>3⟩ | a/3⟨11<span style="text-decoration: overline;">2</span>3⟩ | 5 |

*数据来源*：[[S48]][[S45]][[S29]][[S23]][[S40]][[S14]]。

**重要说明**：基面〈a〉滑移{0001}⟨11<span style="text-decoration: overline;">2</span>0⟩是镁合金中最基本的滑移系，其实质是柏氏矢量为a/3⟨11<span style="text-decoration: overline;">2</span>0⟩的单位位错滑移[[S48]]。虽然基面上存在三个滑移方向（[1120]、[<span style="text-decoration: overline;">1</span>2<span style="text-decoration: overline;">1</span>0]、[2110]），但第三个方向可由前两个方向叠加而成，因此基面滑移在晶体学上仅能提供2个独立滑移系[[S48,S45]]。同样，棱柱面〈a〉滑移也仅提供2个独立滑移系。一阶锥面〈a〉滑移虽提供4个独立滑移系，但从晶体学角度看可视为基面与棱柱面交滑移的综合结果，并不能提供真正新的独立滑移系[[S29]]。**只有二阶锥面〈c+a〉滑移{11<span style="text-decoration: overline;">2</span>2}⟨11<span style="text-decoration: overline;">2</span>3⟩能提供完整的5个独立滑移系，并且其滑移方向⟨11<span style="text-decoration: overline;">2</span>3⟩可协调沿c轴方向的变形**[ [S29,S23,S17,S14]]。

### 各滑移系的临界分切应力（CRSS）特征

室温下（单晶纯镁数据）各滑移系的临界分切应力（Critical Resolved Shear Stress，CRSS）如下[[S23,S17]]：

| 滑移系类型 | 室温CRSS（单晶纯镁） | 相对基面滑移的比值 |
|-----------|-------------------|------------------|
| 基面〈a〉滑移 | 0.5~0.7 MPa | 1（基准） |
| 棱柱面〈a〉滑移 | > 40 MPa | > 60倍 |
| 一阶锥面〈a〉滑移 | ~ 70 MPa | ~ 100倍 |
| 二阶锥面〈c+a〉滑移 | > 100 MPa | > 140倍 |

*数据来源*：[[S23]][[S17]]。

室温下非基面滑移的CRSS是基面滑移的数十至上百倍，导致非基面滑移几乎无法被激活[[S32]]。基面滑移和棱柱面滑移均为〈a〉型位错滑移，其滑移方向⟨11<span style="text-decoration: overline;">2</span>0⟩平行于基面而垂直于c轴，无法协调c轴方向的应变[[S48]]。因此，HCP镁合金在室温下变形时缺乏足够的独立滑移系来满足von Mises准则[[S21,S32]]。

对于细晶多晶镁合金，非基面滑移与基面滑移的CRSS比值（约3~17）远低于单晶水平，说明晶粒细化可有效促进非基面滑移在晶界附近的激活[[S23]]。

随着温度升高（≥498K，即225℃以上），非基面滑移的CRSS大幅降低。573K（300℃）时棱柱面滑移的CRSS已与基面滑移接近，锥面〈c+a〉滑移可通过热激活顺利开动，镁合金塑性变形能力显著提升[[S12,S5]]。

![展示镁合金HCP结构的不同滑移系、孪晶系的晶体结构，以及各类滑移与孪生的临界分切应力（CRSS）对比柱状图，用于说明镁合金室温变形机制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bd1d877-9d73-4fee-a576-6453f23ff7a7/resource)

**图2** 镁合金HCP结构中各类滑移系与孪晶系的晶体结构及室温临界分切应力对比[[S20]]。柱状图直观呈现了基面滑移（CRSS最低）、其余非基面滑移系（CRSS高数倍至数十倍）及各类型孪晶的激活门槛差异。

## HCP镁合金的孪生系

### 孪生类型与晶体学参数

当滑移不足以协调变形时，孪生（Twinning）成为镁合金补充变形的重要机制。孪生对总应变的直接贡献有限（通常不超过10%，部分研究指出约7%[[S17]][[S12]]），但其可通过改变晶粒取向使原本难以滑移的晶粒转为有利取向，促进后续滑移的进行[[S12]]。

镁合金两类主流孪生系的晶体学参数如下[[S10,S12,S35,S40]]：

| 孪生类型 | 孪生面 K₁ | 孪生方向 η₁ | 激活条件 | 作用 | 切变量 | 室温CRSS |
|---------|----------|------------|---------|------|-------|---------|
| {10<span style="text-decoration: overline;">1</span>2} 拉伸孪晶 | {10<span style="text-decoration: overline;">1</span>2} | ⟨10<span style="text-decoration: overline;">1</span><span style="text-decoration: overline;">1</span>⟩ | c轴方向受拉或垂直c轴方向受压 | 实现c轴方向延伸 | 0.13 | 2~3 MPa |
| {10<span style="text-decoration: overline;">1</span>1} 压缩孪晶 | {10<span style="text-decoration: overline;">1</span>1} | ⟨10<span style="text-decoration: overline;">1</span><span style="text-decoration: overline;">2</span>⟩ | c轴方向受压或垂直c轴方向受拉 | 实现c轴方向压缩 | 0.14 | 110~140 MPa |

*数据来源*：[[S10]][[S12]][[S35]][[S40]][[S17]]。

**晶体学表示的重要纠正**：用户提供的描述提示中将孪晶表示为“{1012}<1120>锥面孪生”——该表示存在严重错误。HCP镁合金中最常见的拉伸孪晶的准确晶体学表示为{10<span style="text-decoration: overline;">1</span>2}⟨10<span style="text-decoration: overline;">1</span><span style="text-decoration: overline;">1</span>⟩[[S10,S12,S35]]，压缩孪晶的准确表示为{10<span style="text-decoration: overline;">1</span>1}⟨10<span style="text-decoration: overline;">1</span><span style="text-decoration: overline;">2</span>⟩[[S10,S12,S35]]。⟨11<span style="text-decoration: overline;">2</span>0⟩是滑移方向，不是孪生方向。

{10<span style="text-decoration: overline;">1</span>2}拉伸孪晶在镁合金中切变量最小（0.13），CRSS最低（2~3 MPa），是最容易发生的孪生模式。拉伸孪晶发生后，孪晶内基面绕⟨1<span style="text-decoration: overline;">2</span>10⟩轴旋转约86°，使原本硬取向的晶粒转为软取向，有利于后续基面滑移[[S12,S40]]。{10<span style="text-decoration: overline;">1</span>1}压缩孪晶的CRSS约为拉伸孪晶的数十倍，室温下难以开动[[S12,S17]]。

### 孪晶的晶体学关系

在HCP金属中，孪生主要发生在锥面上，孪生模式及要素均受c/a值的影响[[S10]]。{10<span style="text-decoration: overline;">1</span>2}拉伸孪生是几乎所有HCP金属在适当条件下均可发生的孪生模式[[S10]]。对于不同轴比的HCP金属，孪生切变量和激活行为有所不同，例如当c/a = √3时，{10<span style="text-decoration: overline;">1</span>2}孪生切变量s = 0，此时该模式将无法发生[[S10]]。

## HCP结构导致镁合金室温塑性差的根本机制

HCP镁合金室温塑性差的根本原因在于独立滑移系严重不足，可概括为以下三个层次[[S21,S32,S48,S14]]：

1. **独立滑移系数量不足**：室温下仅基面〈a〉滑移的2个独立滑移系易于开动。根据von Mises准则，多晶体材料实现均匀协调变形至少需要5个独立滑移系。仅靠基面滑移远不能满足该要求[[S21]]。

2. **c轴方向应变无法协调**：基面〈a〉滑移和棱柱面〈a〉滑移的滑移方向⟨11<span style="text-decoration: overline;">2</span>0⟩均平行于基面且垂直于c轴，无法提供沿c轴方向的应变分量[[S48]]。虽然二阶锥面〈c+a〉滑移可协调c轴应变且提供5个独立滑移系，但其室温CRSS极高（> 100 MPa），实际上无法激活[[S23,S17,S29]]。

3. **非基面滑移的CRSS过高**：室温下棱柱面滑移的CRSS约为基面滑移的60倍以上，锥面〈c+a〉滑移的CRSS更是高达140倍以上[[S23,S17]]。变形过程中位错运动受阻，易在晶界等障碍处产生高度应力集中，导致微裂纹萌生[[S32]]。

室温下仅{10<span style="text-decoration: overline;">1</span>2}拉伸孪晶（CRSS约2~3 MPa）可辅助协调变形，但其应变贡献有限（仅约7%~10%）[[S17,S12]]，无法弥补滑移系的根本不足。

## 温度对HCP镁合金变形行为的调控

温度是调控HCP镁合金塑性变形能力的关键外部因素。高温下非基面滑移系的CRSS显著降低[[S12,S5,S17,S44]]：

- 在498K（225℃）以上，棱柱面滑移和锥面滑移的CRSS大幅下降，独立滑移系总数可超过5个，满足von Mises准则要求[[S21,S44]]。
- 573K（300℃）时，棱柱面滑移的CRSS已与基面滑移接近，锥面〈c+a〉滑移可通过热激活开动，镁合金塑性显著提升[[S12,S5]]。
- 高温条件下变形机制趋于复杂化，涉及位错滑移、晶界滑移、交滑移等多种机制协同作用[[S5]]。

## HCP结构特征与镁合金压铸工艺的关联

### 室温塑性差对压铸充型与脱模的影响

镁合金压铸以高压高速将熔融金属充填模具型腔，随后快速凝固成型[[S16]]。HCP结构的低对称性对压铸过程产生以下直接影响：

- **室温变形受限与热裂倾向**：镁合金因独立滑移系少，室温塑性远低于FCC结构的压铸铝合金。在凝固收缩阶段，若局部温度已降至较低水平而收缩受阻，晶界处因位错运动困难产生应力集中，易萌生热裂纹[[S32,S16,S21]]。
- **脱模过程的变形风险**：压铸件在顶出阶段承受脱模力，若此时铸件表面温度已降至基面滑移难以协调变形的区间，局部变形不均可能导致顶出开裂[[S43]]。

### 高温工艺窗口与塑性改善

压铸过程中熔融金属在充型和初始凝固阶段处于高温区间（通常远高于225℃）。在此温度范围内[[S16,S44]]：

- 非基面滑移（棱柱面、锥面〈c+a〉滑移）可被热激活充分开动，总独立滑移系超过5个，满足von Mises准则要求[[S21,S44]]。
- 补缩阶段的变形协调能力增强，有利于减少热裂缺陷[[S16]]。
- 脱模阶段铸件仍具有一定温度时，变形协调性较好，脱模阻力分布更均匀[[S43,S16]]。

**工艺指导意义**：通过适当提高浇注温度和模具预热温度，可扩展压铸过程中材料处于高塑性状态的工艺窗口，改善充型流动性、降低热裂缺陷率、提高脱模质量[[S25]]。

### 镁合金HCP结构对压铸的有利因素

相比FCC铝合金和BCC钢铁材料，镁合金HCP结构在压铸中还具有以下工艺优势[[S43,S25,S42]]：

1. **与钢铁模具的亲和力较低**：镁合金不易粘附模具型腔表面，脱模阻力小，可减少粘模缺陷，无需像铝合金那样反复喷涂防粘模涂料[[S43]]。
2. **熔点较低**：有利于延长压铸模的使用寿命[[S25,S42]]。
3. **流动性良好**：液态填充性能优良，尺寸稳定性好[[S43,S25]]。

## 常见HCP压铸镁合金牌号及微观组织

压铸用镁合金牌号基于Mg-Al系合金体系，其基体均为HCP结构的α-Mg固溶体。以下为几种典型压铸镁合金的组成与组织特征[[S27,S30,S8]]：

| 合金牌号 | 合金系 | 基体相 | 主要第二相 | 合金特点 | 数据来源 |
|---------|-------|-------|-----------|---------|---------|
| AZ91D | Mg-Al-Zn | HCP α-Mg | Mg₁₇Al₁₂（晶界析出） | 高Al含量，强度高，塑性较低 | [[S27]] |
| AM50 | Mg-Al-Mn | HCP α-Mg | Mg₁₇Al₁₂、Al₈(Mn,Fe)₅ | 降低Al含量，延伸率和冲击韧性优于AZ91D | [[S27,S30]] |
| AM60 | Mg-Al-Mn | HCP α-Mg | Mg₁₇Al₁₂、Al₈(Mn,Fe)₅ | 与AM50类似，综合力学性能优良 | [[S27,S8]] |
| AS21 | Mg-Al-Si | HCP α-Mg | Mg₂Si（热稳定相） | 低Al量，Mg₂Si提高抗蠕变性；慢冷时易形成汉字状脆性相 | [[S8]] |
| AE44 | Mg-Al-RE | HCP α-Mg | Al₁₁RE₃（针状，热稳性好） | RE添加消除Mg₁₇Al₁₂，室温和高温性能优异 | [[S8]] |

*说明*：上述各类镁合金的HCP基体相α-Mg具有相同的晶体结构特征，但其力学行为因第二相种类、形态和分布的不同而存在显著差异。AM系列通过降低Al含量减少脆性Mg₁₇Al₁₂相的析出，改善了塑性[[S27]]；AS系列通过Mg₂Si热稳定相提高抗蠕变性能，但需控制Si含量和冷却速率以避免形成恶化强韧性的粗大Mg₂Si相[[S8]]。

## 与FCC和BCC结构的压铸工艺对比

| 对比维度 | HCP（镁合金） | FCC（铝合金） | BCC（钢铁材料） |
|---------|------------|------------|--------------|
| 室温独立滑移系 | <5，塑性差，依赖高温 | >>5，室温塑性优良 | >5，室温塑性较好 |
| 压铸热裂倾向 | 低温段较高 | 较低 | 极高（模具寿命极低） |
| 粘模倾向 | 低（与钢亲和力低） | 高（与钢亲和力高） | — |
| 模具寿命 | 较长（熔点低） | 一般（型腔温度~600℃） | 极低（型腔温度~1000℃以上） |
| 工艺适配性 | 优良（流动性好、密度小、尺寸稳定） | 优良（应用最广泛） | 差（极少工业应用） |

*数据来源*：[[S7,S18,S25,S42,S43]][[S32]]。

FCC结构的压铸铝合金在室温下可开动的独立滑移系数目远超5个，满足von Mises协调变形要求，室温塑性显著优于HCP镁合金，常规压铸工艺下热裂倾向较低。但铝合金与钢模亲和力更高，粘模倾向大于镁合金，需额外喷涂防粘模涂料[[S43,S18]]。BCC结构的钢铁材料熔点远高于镁和铝合金，压铸过程中模腔表面温度可达1000℃以上，模具热疲劳、腐蚀和磨损问题极为严重，模具寿命极低，工业规模化应用程度远低于镁、铝压铸[[S25,S3,S42]]。

## 研究前沿：通过合金化改善HCP镁合金的变形能力

当前针对HCP镁合金的增塑研究集中于以下方向[[S47,S23,S12,S5]]：

- **调控c/a轴比**：添加Li、In、Ag等合金元素使c/a < 1.618，提高晶格对称性，可激活棱柱面滑移系[[S47]]。
- **激活锥面〈c+a〉滑移**：适当添加稀土元素（如Y），可促进〈c+a〉位错的交滑移与增殖，降低其CRSS，显著提高塑性变形能力[[S5,S23]]。
- **细化晶粒**：晶粒细化至10 μm以下时棱柱面滑移可贯穿整个晶粒，且通过Hall-Petch效应同步提高强度与塑性[[S23,S16]]。

## Sources
- S46: [工程材料及热加工工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea2ec108-9a5b-4647-98c2-ab2fa8e7ebcf/resource) (`ea2ec108-9a5b-4647-98c2-ab2fa8e7ebcf`)
- S31: [工程材料及金属热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9afb2e70-bc41-486c-8d42-a64915ac9c7d/resource) (`9afb2e70-bc41-486c-8d42-a64915ac9c7d`)
- S41: [crystallography and crystal defects second__21c720b611](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/daabc970-e439-48ad-9f36-55b073c08cf4/resource) (`daabc970-e439-48ad-9f36-55b073c08cf4`)
- S39: [工程材料与热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d29d6d7e-1919-4d7a-9529-20b4d49ddc82/resource) (`d29d6d7e-1919-4d7a-9529-20b4d49ddc82`)
- S33: [civil engineering materials__02d83efc13](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab53ab42-1e96-4596-82d6-a1e63dafd9c4/resource) (`ab53ab42-1e96-4596-82d6-a1e63dafd9c4`)
- S15: [金属塑性成形原理下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e8066cc-18e0-439d-a6f7-c0a69816641f/resource) (`4e8066cc-18e0-439d-a6f7-c0a69816641f`)
- S28: [工程材料及加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91807dff-6c7c-4f0c-9638-4b53221a43fb/resource) (`91807dff-6c7c-4f0c-9638-4b53221a43fb`)
- S43: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd3c812c-1f26-4d75-8c37-584100670786/resource) (`dd3c812c-1f26-4d75-8c37-584100670786`)
- S21: [镁合金熔体氧化孕育细化行为及其机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c831011-1f3b-43fa-b1e0-3b04b0c58ccd/resource) (`6c831011-1f3b-43fa-b1e0-3b04b0c58ccd`)
- S32: [AlN_ZK60镁基复合材料的热变形行为与强韧化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f40fc65-6078-411e-a90f-de22ddf4f943/resource) (`9f40fc65-6078-411e-a90f-de22ddf4f943`)
- S9: [工程材料及加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2acabe95-dab0-4469-84c0-56401d471f7e/resource) (`2acabe95-dab0-4469-84c0-56401d471f7e`)
- S24: [工程材料与金属热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76a416f2-e963-4da7-8f6d-b1319ea3239c/resource) (`76a416f2-e963-4da7-8f6d-b1319ea3239c`)
- S22: [crystallography and crystal defects__8f193169ed](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e29e9fe-7699-45a7-bad8-7e24486c941f/resource) (`6e29e9fe-7699-45a7-bad8-7e24486c941f`)
- S11: [工程材料与热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/375466d8-421d-46e0-800f-25f8494b1f2f/resource) (`375466d8-421d-46e0-800f-25f8494b1f2f`)
- S6: [机械制造基础工程材料及热加工工艺基础上册第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20b7638b-c319-48b2-9664-ee87b55ba621/resource) (`20b7638b-c319-48b2-9664-ee87b55ba621`)
- S40: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d44034f4-252b-4494-9e2c-0294a75acf56/resource) (`d44034f4-252b-4494-9e2c-0294a75acf56`)
- S37: [a handbook of lattice spacings and structures of metals and alloys__0d6d7e6946](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ccb6bbba-0214-4a9e-ac90-422194c53d66/resource) (`ccb6bbba-0214-4a9e-ac90-422194c53d66`)
- S34: [图2-5 密排六方晶格的晶胞示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afa41abd-acdc-494f-9959-e7119038a069/resource) (`afa41abd-acdc-494f-9959-e7119038a069`)
- S47: [先进镁合金制备与加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f017fd73-4c88-4f67-8fdc-31417b439cb0/resource) (`f017fd73-4c88-4f67-8fdc-31417b439cb0`)
- S50: [表2-1 三种典型金属晶体结构小结](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff008ca5-700a-4b66-b8be-4d498dcc0fee/resource) (`ff008ca5-700a-4b66-b8be-4d498dcc0fee`)
- S26: [模具设计与制造专业英语](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80cd76d2-d962-4a82-8437-f1276bcca473/resource) (`80cd76d2-d962-4a82-8437-f1276bcca473`)
- S48: [变形镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5c0e0f3-0436-4031-8374-e80c960aed60/resource) (`f5c0e0f3-0436-4031-8374-e80c960aed60`)
- S45: [变形镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e71f633e-06cd-4475-909f-f2a493d95238/resource) (`e71f633e-06cd-4475-909f-f2a493d95238`)
- S29: [变形镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91ecb4b1-058d-4719-9ea0-5f9fa89c1ea5/resource) (`91ecb4b1-058d-4719-9ea0-5f9fa89c1ea5`)
- S23: [az31b钛镁合金组织调控及成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74841654-434b-4522-b216-318fdb6fcd30/resource) (`74841654-434b-4522-b216-318fdb6fcd30`)
- S14: [表2-3 镁合金的主要滑移系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45c0d2dc-e22d-4dee-9ced-d0fa765a4e9e/resource) (`45c0d2dc-e22d-4dee-9ced-d0fa765a4e9e`)
- S17: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f11d2af-c657-4782-9b57-9f7bb74fedef/resource) (`5f11d2af-c657-4782-9b57-9f7bb74fedef`)
- S12: [az31b钛镁合金组织调控及成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3dcf2362-b3dd-4ad6-8049-9b4158520002/resource) (`3dcf2362-b3dd-4ad6-8049-9b4158520002`)
- S5: [压铸耐热镁合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e5bebc2-8e2a-4687-9090-7aebfc54c543/resource) (`1e5bebc2-8e2a-4687-9090-7aebfc54c543`)
- S20: [镁合金HCP结构的滑移系与孪晶系的临界分切应力对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bd1d877-9d73-4fee-a576-6453f23ff7a7/resource) (`6bd1d877-9d73-4fee-a576-6453f23ff7a7`)
- S10: [变形镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3138ed61-a167-41df-9c16-6e43b98907ef/resource) (`3138ed61-a167-41df-9c16-6e43b98907ef`)
- S35: [镁晶体中主要孪生与双孪生模式的晶体学参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b942b83d-85e7-45ea-bbd0-9d7a4753b5fd/resource) (`b942b83d-85e7-45ea-bbd0-9d7a4753b5fd`)
- S44: [advances in wrought magnesium alloys fundamentals of processing properties and applications__b1eb9cd50a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2be2229-ce9d-424d-804b-3b724c20ecbb/resource) (`e2be2229-ce9d-424d-804b-3b724c20ecbb`)
- S16: [advancements in high pressure die casting of magnesium__5528302407](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ae1c749-504d-4d5f-adfc-2f3dec0ae3d2/resource) (`5ae1c749-504d-4d5f-adfc-2f3dec0ae3d2`)
- S25: [实用压铸模设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7fd77c41-ffbb-43a9-8070-325feacd7160/resource) (`7fd77c41-ffbb-43a9-8070-325feacd7160`)
- S42: [实用压铸模设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dccec5cb-a56a-41cc-8984-b6e8177cf409/resource) (`dccec5cb-a56a-41cc-8984-b6e8177cf409`)
- S27: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bbff97d-4da2-4d0e-9ea7-9367a74777db/resource) (`8bbff97d-4da2-4d0e-9ea7-9367a74777db`)
- S30: [RDC工艺AM50合金的显微组织图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96b5d556-dea1-4428-8ed8-2217f43447b5/resource) (`96b5d556-dea1-4428-8ed8-2217f43447b5`)
- S8: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24ded62c-1fa2-4c47-bacf-c202a19ac9dc/resource) (`24ded62c-1fa2-4c47-bacf-c202a19ac9dc`)
- S7: [不同金属的晶体结构及滑移参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/21647f6a-dd43-4b90-9c9f-61e73d70a0bc/resource) (`21647f6a-dd43-4b90-9c9f-61e73d70a0bc`)
- S18: [立式压铸机用压铸模和挤铸模65例设计应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6130334e-c372-47dc-98a3-f3d3dfce70be/resource) (`6130334e-c372-47dc-98a3-f3d3dfce70be`)
- S3: [模具表面处理与表面加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12619655-bea3-427e-9532-d86a29624131/resource) (`12619655-bea3-427e-9532-d86a29624131`)