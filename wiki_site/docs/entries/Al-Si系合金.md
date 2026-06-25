---
version: "v1"
generated_at: "2026-06-18T12:03:43+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 85
  source_quality_score: 0.86
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

Al-Si系合金又称硅铝明、铝硅合金，英文称为Aluminum-Silicon alloys（Silumin）或Al-Si system，是以铝为基体、硅为核心合金元素的一类铝合金[[S60,S32,S13]]。该合金覆盖锻造用和铸造用两大类别，其中铸造Al-Si合金是铸造铝合金中应用最广泛、产量最高的类别，典型硅含量区间为4%~22%[[S60,S13]]。Al-Si系合金具备优异的充型流动性、低铸造收缩率、良好的气密性和抗热裂性能，是压铸领域最重要的合金体系[[S60,S32]]。

广义Al-Si系合金涵盖亚共晶、共晶、过共晶全系列合金，衍生出Al-Si-Mg、Al-Si-Cu、Al-Si-Cu-Ni-Mg等多个子牌号体系，包含非热处理可强化和热处理可强化两类；狭义共晶型Al-Si合金特指硅含量接近Al-Si二元共晶点的低合金化二元共晶合金，典型代表为ZL102（AlSi12），几乎不含额外强化合金元素，仅通过变质处理优化组织[[S91,S60,S13]]。

## 分类与成分

### 按硅含量的分类

基于Al-Si二元相图（共晶点：硅含量12.6%，共晶温度577℃），工业Al-Si合金按硅质量分数划分为三类[[S67,S44,S58]]：

| 类别 | 硅含量范围 | 凝固组织特征 |
|------|-----------|-------------|
| 亚共晶Al-Si合金 | <12%（典型4%~11%） | 初生α-Al相 + 共晶组织 |
| 共晶Al-Si合金 | 10%~13%（典型约12%） | α-Al基体 + 共晶硅两相 |
| 过共晶Al-Si合金 | >15%（工业应用15%~24%） | α-Al相 + 共晶硅 + 初生硅相 |

图：Al-Si合金二元相图，标注了共晶温度577.6℃、共晶点硅含量12.6wt.%以及各相区划分[[S51]]。

![Al-Si合金二元相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7720cff8-3f67-48f2-b9c1-16edf9f5df75/resource)

### 中外标准牌号对照

典型Al-Si系合金牌号在GB/T 1173、ASTM B85、EN 1706标准体系中的对应关系如下[[S33,S59,S95]]：

| GB/T 1173（代号） | GB/T 1173（牌号） | ASTM体系 | EN 1706 |
|-------------------|-------------------|---------|---------|
| ZL101 | ZAlSi7Mg | 356.0、A356.0 | AC-42000、AC-42100 |
| ZL102 | ZAlSi12 | AlSi12 | AC-44200 |
| ZL109 | ZAlSi12Cu1Mg1Ni1 | 336.0、339.0 | AC-48000（AlSi12CuNiMg） |

### 主要合金元素的作用

**镁（Mg）**：镁是Al-Si系合金实现热处理强化的核心元素，与硅反应生成Mg₂Si相，该相在固溶处理后时效析出，大幅提升室温力学强度。工业生产中镁含量通常控制在0.25%~1.30%区间；过量镁会导致未溶的粗大Mg₂Si脆性相残留，降低合金塑性[[S68,S55,S1,S11]]。

**铜（Cu）**：铜可实现固溶强化，提升合金的室温、高温力学强度，同时改善切削加工性能。含铜量较高时形成W（Al₃Mg₅Cu₄Si₄）相，弥散分布于晶界，可提升耐热性能。但铜会明显降低耐腐蚀性能，含铜量过高时生成低熔点共晶相，导致热处理过烧缺陷[[S55,S87,S11,S34]]。

**铁（Fe）**：压铸Al-Si合金中通常控制Fe含量≥0.6%，以减少粘模倾向；过量Fe会形成针状β-AlFeSi相，降低合金塑性[[S77,S78]]。

## 显微组织

### 铸态组织特征

Al-Si合金的凝固组织由α-Al固溶体（Si原子溶入面心立方Al晶格形成的置换固溶体）和共晶硅相（金刚石立方结构的Si固溶体，可近似视为纯硅相）组成。共晶温度577℃时Si在Al中的最大溶解度为1.65wt%，室温下溶解度降至0.01wt%以下[[S63,S38,S41]]。

压铸过程冷却速率远高于砂型、金属型铸造。快速凝固下α-Al固溶体呈现细小圆整的等轴晶/梅花状形态，共晶硅尺寸显著细化。当Si含量从7wt%提升至10wt%时，免热处理压铸Al-Si合金的共晶硅面积分数从25.8%升至51.2%，α-Al平均晶粒尺寸从10.1μm降低至5.8μm[[S63,S21,S7,S88]]。

图：高压铸造免热处理Al-Si合金的扫描电镜显微组织，标注了细小圆整的α-Al相、弥散分布的粒状共晶硅及汉字状富铁相[[S83]]。

![压铸Al-Si合金SEM显微组织](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c413bd17-4550-4ace-b1e6-8fc401df0804/resource)

### 硅相形态对性能的影响

硅相形态随硅含量和冷却条件变化。压铸亚共晶Al-Si合金中：Si含量7wt%时共晶硅基本为颗粒状；8wt%时以颗粒状为主并出现短棒状；9wt%时颗粒状减少、短棒状和针片状增多；10wt%时颗粒状基本消失，大量短棒状与针片状共存，最长纤维状共晶硅可达7.5μm[[S7,S15]]。

未变质的粗大针片状共晶硅呈高硬度脆性相，会割裂α-Al基体连续性，在受力时尖角处产生严重应力集中，大幅降低合金伸长率和断裂韧性。当共晶硅被细化为纤维状或颗粒状时，硅相对基体的割裂作用完全消除，合金抗拉强度可提升50%，伸长率可提升5倍左右[[S63,S102,S74,S22]]。

### 变质处理

**钠变质**：机理属于吸附薄膜理论，微量Na作为表面活性物质富集在硅晶核表面形成薄膜，阻碍硅晶体长大、增大结晶过冷度，将粗大针片状共晶硅转变为纤维状。工业上通常以NaF、NaCl等卤素盐混合形式加入，控制熔体中Na质量分数0.01%~0.014%。变质有效时间仅30~60min，易衰退、重熔失效，且易导致熔体吸氢产生皮下气孔，NaF有职业健康危害[[S79,S62,S53,S99]]。

**锶变质**：主流为吸附生长台阶理论，Sr原子吸附在共晶硅的孪晶生长台阶/交界处，阻碍硅原子沿原有结晶方向堆垛，迫使硅相向细纤维状转变。工业上以Al-(5%~10%)Sr中间合金形式加入，控制加入量0.02%~0.05%，变质有效时间可达6~8h，保温重熔后仍可保持变质效果，属于长效变质剂，是当前压铸Al-Si合金生产中应用最广泛的变质剂。缺点是Sr化学性质活泼，易增大铝液吸气倾向导致针孔率上升[[S47,S86,S4,S29]]。

**稀土变质**：核心为多重孪晶诱导理论，RE原子（La、Ce、Eu等）原子半径与Si原子半径比值约为1.65，匹配硅晶体表面孪晶凹坑的作用阈值，吸附在硅{111}晶面上诱导产生大量多重孪晶，迫使共晶硅向细纤维、颗粒状转变。工业上以混合稀土中间合金形式加入，控制加入量0.2%~0.3%，经30~40min孕育期即可完成变质，有效时间可达5~7h，多次重熔仍可保持效果，兼具细化α-Al晶粒、净化铝液、改善高温力学性能的附加作用[[S9,S22,S64,S62]]。

图：变质处理后Al-12.7%Si合金的光学显微组织（120×），显示粗大片状硅相转变为细小弥散颗粒状相的典型特征[[S10]]。

![变质处理后Al-12.7%Si合金显微组织](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/126066dd-6a04-463c-a361-27093f5f6df8/resource)

## 核心性能

### 力学性能

Al-Si系合金的力学性能取决于成分、变质处理状态和热处理工艺。

| 合金/状态 | 抗拉强度(MPa) | 屈服强度(MPa) | 延伸率(%) | 来源 |
|-----------|-------------|-------------|----------|------|
| ZL102铸态（未变质） | 130~140 | — | 1~2 | [[S98,S48]] |
| ZL102钠盐/锶变质处理后 | ≥180 | — | 6 | [[S98,S48]] |
| A356高真空压铸+时效（Sr变质） | 286 | 193 | 7.83 | [[S52]] |
| AlSi10MnMg T7状态本体 | ≥180 | ≥120 | ≥10 | [[S69]] |
| Silafont-38 T6空淬+人工时效 | — | >180 | ~10 | [[S69]] |
| A380（ASTM B85） | 320 | — | 3.5 | [[S92]] |

**热处理影响**：T6热处理（固溶+人工时效）对可强化Al-Si-Mg系合金的作用机制为：固溶阶段让合金元素充分溶入铝基体形成过饱和固溶体，时效阶段析出弥散分布的Mg₂Si等强化相，同时促使共晶硅发生熔断、球化，弱化硅相对基体的割裂作用，同步提升合金强度与韧性[[S46]]。

### 铸造性能

Al-Si系压铸合金相比其他系列铝合金（Al-Mg、Al-Cu、Al-Zn）具有显著更优的铸造性能：结晶温度间隔小，硅相凝固潜热大、比热容高，因此流动性好、充型能力强，线收缩率小，热裂倾向、缩松倾向低。共晶成分合金在凝固点附近仍保持良好塑性，适配薄壁复杂压铸件的生产[[S18,S16,S43,S25]]。

共晶成分附近Al-Si合金的铸造性能达到峰值。ZL102（AlSi12）合金的抗热裂性能、气密性、流动性均为Al-Si系中最优等级，适合浇注大尺寸、形状复杂的薄壁压铸件[[S8,S3]]。硅含量在共晶点（w(Si)=11.7%）时合金凝固温度范围最窄，线收缩率小，不易产生缩松和热裂，适配薄壁复杂型腔的充型需求[[S76,S5]]。

### 物理与化学性能

| 性能 | 典型值/范围 | 来源 |
|------|-----------|------|
| 密度 | 2.5~2.7 g/cm³（AlSi12为2.65 g/cm³，含Cu系如ZL112Y为2.75 g/cm³） | [[S98,S43,S75]] |
| 热导率（室温） | 101~126 W/(m·℃)（ZL112Y为108.8 W/(m·℃)） | [[S32,S75]] |
| 电阻率（20℃） | AlSi12为54.8 nΩ·m；Al-Si-Cu系约为75 nΩ·m | [[S98,S75]] |
| 耐腐蚀性 | 不含铜的二元Al-Si共晶合金耐大气腐蚀性能优良；含Cu合金耐蚀性较差 | [[S98,S75,S90]] |

压铸过程产生的气孔、夹渣、晶格畸变缺陷会降低合金电导率[[S97]]。

## 工艺参数

### 高压压铸通用工艺窗口

铝合金高压压铸通用浇注温度区间为650℃~720℃，模具工作温度按经验公式 t_m = 1/3 × t_j ±25℃ 确定，常规铝硅合金预热模具温度区间为150℃~250℃，常规充填速度为15~30m/s，通用增压压力范围20MPa~100MPa[[S73,S26]]。

### 典型牌号推荐参数

| 合金牌号 | 浇注温度(℃) | 模具温度(℃) | 充填速度(m/s) | 增压压力(MPa) | 来源 |
|---------|------------|------------|-------------|-------------|------|
| A356 | 630~680 | 190~240 | 20~28 | 50~70 | [[S89,S101,S12]] |
| AlSi12（YZAlSi12） | 680~720 | 140~180（预热） | 25~35 | 70~90 | [[S45,S70,S14]] |
| AlSi10MnMg | 640~680 | 180~220 | 20~30 | ~70 | [[S69,S2]] |

### 低压铸造参数

A356合金低压铸造推荐浇注温度720℃，充型压力约2kPa，维持保压压力在85kPa~300kPa区间可显著消除针孔与缩松，提升致密度[[S12]]。常规Al-Si合金低压铸造浇注温度控制在700℃~730℃，充型速度匹配2.0~2.5kg/s[[S12]]。

## 常见缺陷与对策

### 针孔

针孔缺陷的形成分为两类：一类是充型过程湍流裹挟空气、水汽蒸发与润滑剂燃烧产生的气体被封闭在金属液中形成卷气针孔；另一类是凝固过程中氢在固态铝中溶解度骤降析出形成氢气针孔。工业优化数据显示增压压力对针孔占比的影响贡献度约69%，熔体温度、模具温度合计贡献约20%。适当提升增压压力是降低针孔的最有效手段，配合熔体旋转喷吹惰性气体除氢、优化排气系统、设置合理真空度可进一步将针孔占比控制在极低水平[[S24,S27,S42,S49]]。

### 缩松

缩松缺陷形成机理为Al-Si合金凝固过程中液相体积收缩得不到金属液补缩，在铸件热节区域形成不规则连通孔洞。控制措施包括适当提升增压压力、避免铸件局部出现孤立热节、优化内浇口位置保证补缩通道在凝固后期仍通畅。低压铸造工况下通过提升保压压力可大幅降低缩松体积，优化后较常规低压工艺缩松量可降低80%以上[[S31,S66,S12]]。

### 初生硅相聚集

形成机制为高硅Al-Si合金中当浇注温度过高、冷却速率过慢时，硅相在液相中优先形核长大并发生偏聚，形成大块初生硅颗粒分布不均的聚集组织，大幅降低切削加工性能与力学塑性。控制措施包括严格控制合金Si含量不超过12%（普通压铸场景）、避免浇注温度过高导致初晶析出、添加微量P元素进行变质细化、提升凝固冷却速率，禁止在高硅Al-Si合金中采用半固态“粥状”低压压铸工艺[[S73,S54]]。

### 粘模（焊合）

形成机理为高压高速射流直接冲刷模具局部位置，将模具表面保护涂层冲刷脱落，高温铝液与模具钢发生Fe-Al、Fe-Al-Si金属间化合物的扩散反应，导致铝合金与模具表面发生焊合粘连。控制措施包括将合金中Fe质量分数控制在0.6%以上，同时匹配Mn/Fe比例不低于2/3，适当降低内浇口流速以减少金属射流动能，优化模具冷却通道布局降低局部表面温度[[S78,S31,S69]]。

## 应用领域

Al-Si系压铸合金在汽车领域覆盖三大核心品类：

**动力系统零部件**：铝合金压铸缸体相比铸铁导热性更高，可提升发动机热效率、降低整机重量，主流采用Al-Si-Cu或优化过的亚共晶Al-Si合金生产；还包括缸盖、油底壳、活塞、泵体、进气管等[[S94,S57,S84]]。

**传动与底盘一体化结构件**：新能源汽车普及的一体化后地板、前舱减震塔等部件多采用免热处理Al-Si-Mg体系合金（如Silafont-36/38、Aural系列），避免热处理引发的大尺寸构件变形问题，降低制造成本[[S94,S57,S56]]。车身结构件常用AlSi10MnMg压铸合金在T7热处理状态下铸件本体屈服强度≥120MPa、抗拉强度≥180MPa、延伸率≥10%[[S69]]。

**薄壁壳体类零部件**：包括油底壳、3C消费电子散热壳体、仪表壳体等，高硅Al-Si合金适配超薄复杂流道成型需求[[S94,S57]]。

## 与其他合金体系的关系

### Al-Si-Mg系

通过添加Mg元素生成Mg₂Si强化相，在保障良好流动性的同时，抗拉强度、耐蚀性、阳极氧化性能显著提升。低Fe高Mn优化成分的牌号如Silafont-36可实现8%~11%的伸长率，适配汽车减震塔、副车架、电池包壳体等对强韧性和耐候性要求较高的结构件。但Mg元素含量过高会增大热裂倾向、降低压铸充型性能[[S56,S19,S80]]。

### Al-Si-Cu系

铜元素质量分数2.0%~4.0%的主流牌号如A380、ADC12，力学强度、机加工性能、常温抗蠕变性能优异，是全球应用占比最高的通用压铸铝合金（北美市场该类合金占铝压铸件总产量约85%）。但耐蚀性相比Al-Si-Mg体系偏弱，塑性偏低，适配对成本敏感、侧重强度和加工性能的普通壳体、通用机械零部件[[S77,S19,S61]]。

| 体系 | 核心特点 | 典型牌号 | 适用场景 |
|------|---------|---------|---------|
| 二元Al-Si共晶 | 铸造性能最优，不可热处理强化 | ZL102、AlSi12 | 薄壁非承力件、仪表壳体 |
| Al-Si-Mg系 | 可热处理强化，韧性好，耐蚀性好 | A356、Silafont-36/38 | 结构件、减震塔、副车架 |
| Al-Si-Cu系 | 强度高，加工性好，耐蚀性偏弱 | A380、ADC12 | 通用壳体、机械零部件 |

## 现行标准

GB/T 15115-2024《压铸铝合金》为我国Al-Si系压铸合金的通用标准，新增YZAlSi12Fe等牌号适配轻量化行业需求。同步更新的GB/T 15114-2023《铝合金压铸件》强化了内部针孔、缩松缺陷的等级管控要求[[S65,S37]]。国标GB/T 1173、GB/T 15115及配套《铝与铝合金速查手册》收录了完整的Al-Si系压铸合金化学成分、力学性能、物理性能、化学性能对应数据表[[S50]]。

## 图示

铝及铝合金分类框架图，明确标注Al-Si系铸造合金（如ZL102等）在整个铝合金体系中的位置[[S81]]。

![铝及铝合金分类图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2813d2f-e201-45e5-8352-dce277f6fa88/resource)

## Sources
- S60: [铝与铝合金速查手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89fc1f7c-882f-4459-94ad-95190b951cb1/resource) (`89fc1f7c-882f-4459-94ad-95190b951cb1`)
- S32: [9797399_铝硅合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/459bfcfa-4ab0-4fa3-b83e-f7248c229a2d/resource) (`459bfcfa-4ab0-4fa3-b83e-f7248c229a2d`)
- S13: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1676cda4-8182-4faf-88d8-c70645585bf0/resource) (`1676cda4-8182-4faf-88d8-c70645585bf0`)
- S91: [先进航空铝合金材料与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dbaeb5c8-db01-47cc-a1e5-31e4d86a6ed8/resource) (`dbaeb5c8-db01-47cc-a1e5-31e4d86a6ed8`)
- S67: [中国机械工业标准汇编 铸造卷 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a17bfeeb-5bf5-41bd-a79e-d20066b46a17/resource) (`a17bfeeb-5bf5-41bd-a79e-d20066b46a17`)
- S44: [机械基础制造工艺标准汇编 铸造 上](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65aa0475-7435-40f4-ada2-945ac5143fda/resource) (`65aa0475-7435-40f4-ada2-945ac5143fda`)
- S58: [模壁超声振动对铸造铝硅合金流动性及凝固组织的影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86addd13-e74a-4702-bed9-77c2818bc41e/resource) (`86addd13-e74a-4702-bed9-77c2818bc41e`)
- S51: [图1.2 Al-Si合金二元相图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7720cff8-3f67-48f2-b9c1-16edf9f5df75/resource) (`7720cff8-3f67-48f2-b9c1-16edf9f5df75`)
- S33: [Al-Si合金牌号对照表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4743d0b9-0bbf-40b4-859f-d1ff9b4918ba/resource) (`4743d0b9-0bbf-40b4-859f-d1ff9b4918ba`)
- S59: [中外铝合金牌号对照速查手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/88dda7ab-b3f8-4e21-bbb6-463417121330/resource) (`88dda7ab-b3f8-4e21-bbb6-463417121330`)
- S95: [中外铝合金牌号对照速查手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e919ad75-47b6-42be-a362-6fd0ebdf69f8/resource) (`e919ad75-47b6-42be-a362-6fd0ebdf69f8`)
- S68: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a62631fd-207c-48fc-96cc-a012c0e38a5d/resource) (`a62631fd-207c-48fc-96cc-a012c0e38a5d`)
- S55: [有色金属熔炼工工艺学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81900657-3a08-494f-a0f7-fa0a67fed284/resource) (`81900657-3a08-494f-a0f7-fa0a67fed284`)
- S1: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0012012e-1965-4e1c-8d70-2a1938e31a34/resource) (`0012012e-1965-4e1c-8d70-2a1938e31a34`)
- S11: [0101_6d91552966a9339a_Aluminium–silicon_alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1631db39-2a75-47bd-a4b9-95f28929046c/resource) (`1631db39-2a75-47bd-a4b9-95f28929046c`)
- S87: [有色铸造合金及熔炼](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2025921-0b80-46e6-94d1-1e136b786124/resource) (`d2025921-0b80-46e6-94d1-1e136b786124`)
- S34: [aluminum and aluminum alloys introduction and overview__ca28de7c4d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47b6b91f-9f19-4fbd-b7c5-7c437cae2f70/resource) (`47b6b91f-9f19-4fbd-b7c5-7c437cae2f70`)
- S77: [压铸铝合金研究现状与未来发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b33f5626-1f14-4afd-bef1-1eec02f88d21/resource) (`b33f5626-1f14-4afd-bef1-1eec02f88d21`)
- S78: [comparative study on the microstructures and hardness of the alsi106cumg__b188063cb6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8b8a642-c30f-4aed-a4e9-8553413d99c3/resource) (`b8b8a642-c30f-4aed-a4e9-8553413d99c3`)
- S63: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91abf338-dbc0-4792-a7cb-a9139a29e725/resource) (`91abf338-dbc0-4792-a7cb-a9139a29e725`)
- S38: [binary alloy phase diagrams__4d8db6f6f7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/574ba4e7-c35f-421b-a86a-6f0717631b67/resource) (`574ba4e7-c35f-421b-a86a-6f0717631b67`)
- S41: [elements of physical metallurgy__923bb3a713](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fdb0266-86eb-49ed-856a-4c989187fe8b/resource) (`5fdb0266-86eb-49ed-856a-4c989187fe8b`)
- S21: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25d0c53b-ac2c-4a85-af0c-997a356144b1/resource) (`25d0c53b-ac2c-4a85-af0c-997a356144b1`)
- S7: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11f7f91d-75d6-4e77-9ff9-7fea16dd1778/resource) (`11f7f91d-75d6-4e77-9ff9-7fea16dd1778`)
- S88: [四种压铸Al-Si合金的共晶硅面积分数与α-Al平均晶粒尺寸](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d41cb6df-ef35-4bd0-8684-f7cdd5ed507f/resource) (`d41cb6df-ef35-4bd0-8684-f7cdd5ed507f`)
- S83: [压铸Al-Si合金扫描电镜显微组织（标注共晶硅、Fe相、α-Al）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c413bd17-4550-4ace-b1e6-8fc401df0804/resource) (`c413bd17-4550-4ace-b1e6-8fc401df0804`)
- S15: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d23418b-8654-4d0b-a279-9f888ee35d93/resource) (`1d23418b-8654-4d0b-a279-9f888ee35d93`)
- S102: [铸造铝硅合金一体化控性工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb1932f8-6257-402d-995a-c352014b3a3e/resource) (`fb1932f8-6257-402d-995a-c352014b3a3e`)
- S74: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b105eeb2-e948-4fc8-9d9f-98ecc398cbaa/resource) (`b105eeb2-e948-4fc8-9d9f-98ecc398cbaa`)
- S22: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26f6683c-0c50-4191-86eb-be68560a7080/resource) (`26f6683c-0c50-4191-86eb-be68560a7080`)
- S79: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b906cd7a-8083-43d5-82d8-14e65436cfaa/resource) (`b906cd7a-8083-43d5-82d8-14e65436cfaa`)
- S62: [稀土在铝合金中的行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f261427-3e92-46f1-bd53-9a61083cbbc3/resource) (`8f261427-3e92-46f1-bd53-9a61083cbbc3`)
- S53: [铝及铝合金加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8585ca-cdc6-422a-9020-cffe488367d8/resource) (`7b8585ca-cdc6-422a-9020-cffe488367d8`)
- S99: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f03f75df-dd74-499c-b0d4-8fa241c37bc2/resource) (`f03f75df-dd74-499c-b0d4-8fa241c37bc2`)
- S47: [铝合金材料组织与金相图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/682626a2-dbc9-4d50-a751-8224b25ad641/resource) (`682626a2-dbc9-4d50-a751-8224b25ad641`)
- S86: [有色金属熔炼入门与精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1af25e9-6072-490c-b4fe-5faf945e24c7/resource) (`d1af25e9-6072-490c-b4fe-5faf945e24c7`)
- S4: [差压铸造生产技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/088b587c-1f41-4559-a4c6-5cf06ef955ac/resource) (`088b587c-1f41-4559-a4c6-5cf06ef955ac`)
- S29: [免热处理压铸Al-9Si合金成分与工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42bec4d4-a4fa-4c58-94db-eb53f2ae9f1c/resource) (`42bec4d4-a4fa-4c58-94db-eb53f2ae9f1c`)
- S9: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/125708f0-be4a-4c43-9088-0ce672f9536d/resource) (`125708f0-be4a-4c43-9088-0ce672f9536d`)
- S64: [advances in high performance non ferrous materials__3e0a9e299e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/945e048b-9d67-412b-b0fd-7c3100a722d3/resource) (`945e048b-9d67-412b-b0fd-7c3100a722d3`)
- S10: [变质处理过的Al-12.7%Si合金光学显微组织（120×）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/126066dd-6a04-463c-a361-27093f5f6df8/resource) (`126066dd-6a04-463c-a361-27093f5f6df8`)
- S98: [中国航空材料手册第3卷铝合金镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/edb1af7b-b11f-4c24-8d1e-59c6838a7019/resource) (`edb1af7b-b11f-4c24-8d1e-59c6838a7019`)
- S48: [工程材料与热加工技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/698ef55b-9446-41e7-8477-fcb18b826f45/resource) (`698ef55b-9446-41e7-8477-fcb18b826f45`)
- S52: [高真空压铸铝合金的研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b3abf52-f943-4583-adc9-ab962b591d00/resource) (`7b3abf52-f943-4583-adc9-ab962b591d00`)
- S69: [乘用车白车身铝合金压铸结构件及材料应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6775f77-b490-47a4-aa81-d41afa62c1cc/resource) (`a6775f77-b490-47a4-aa81-d41afa62c1cc`)
- S92: [铝材A380性能研究与提升](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd860b63-f9b3-4c20-9743-7d462690046f/resource) (`dd860b63-f9b3-4c20-9743-7d462690046f`)
- S46: [不同成形方式及热处理对A356铝合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67c689df-3190-4b89-b214-8bc4e1bf73b4/resource) (`67c689df-3190-4b89-b214-8bc4e1bf73b4`)
- S18: [压铸铝合金研究现状与未来发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/229dea7d-d879-4251-a364-024bedca3c6c/resource) (`229dea7d-d879-4251-a364-024bedca3c6c`)
- S16: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fab2709-9211-4948-982a-ad13c8ab920e/resource) (`1fab2709-9211-4948-982a-ad13c8ab920e`)
- S43: [立式压铸机用压铸模和挤铸模65例设计应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6130334e-c372-47dc-98a3-f3d3dfce70be/resource) (`6130334e-c372-47dc-98a3-f3d3dfce70be`)
- S25: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2939fd61-31aa-49f2-8b6c-bb719d72e1e9/resource) (`2939fd61-31aa-49f2-8b6c-bb719d72e1e9`)
- S8: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/120ca7ac-6f85-4ecb-8a31-afbddc327073/resource) (`120ca7ac-6f85-4ecb-8a31-afbddc327073`)
- S3: [压铸经验汇编](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/074fc3a5-0d19-4846-8b51-23d42749a99e/resource) (`074fc3a5-0d19-4846-8b51-23d42749a99e`)
- S76: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2d02a6a-be44-4f5f-a314-aaa37ec06a2a/resource) (`b2d02a6a-be44-4f5f-a314-aaa37ec06a2a`)
- S5: [普通高等教育“十三五”规划教材 特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0cb28318-ede7-47c0-a36a-44f820785ccb/resource) (`0cb28318-ede7-47c0-a36a-44f820785ccb`)
- S75: [中国航空材料手册第3卷铝合金镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b15d7331-10af-49e3-b196-e5cf7115cad5/resource) (`b15d7331-10af-49e3-b196-e5cf7115cad5`)
- S90: [压铸工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db30fc78-66f5-443e-891c-66bf7c5026f1/resource) (`db30fc78-66f5-443e-891c-66bf7c5026f1`)
- S97: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed128544-5ce7-421a-a4a2-ade2846272d6/resource) (`ed128544-5ce7-421a-a4a2-ade2846272d6`)
- S73: [压铸模与锻模](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aff11393-c2fb-49c2-910e-ffc6c8c4dbd7/resource) (`aff11393-c2fb-49c2-910e-ffc6c8c4dbd7`)
- S26: [压铸模与其他模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/335f854f-defd-4e3a-8433-74cb5aff273e/resource) (`335f854f-defd-4e3a-8433-74cb5aff273e`)
- S89: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d86e4cff-fb14-4925-adb5-ff3d81a3b787/resource) (`d86e4cff-fb14-4925-adb5-ff3d81a3b787`)
- S101: [effect of holding pressure on microstructure and fracture behavior of lo__95a33a08c7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fac893aa-47e2-4a6e-b5f2-425a89708cf9/resource) (`fac893aa-47e2-4a6e-b5f2-425a89708cf9`)
- S12: [铝合金机匣铸造工艺及数值模拟分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/163f3db4-cec9-45a3-a144-e655317c96e9/resource) (`163f3db4-cec9-45a3-a144-e655317c96e9`)
- S45: [effect of parameters of high pressure die casting on occurrence of casti__2da83bfbfe](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67693223-d435-40c5-a903-091671e0038b/resource) (`67693223-d435-40c5-a903-091671e0038b`)
- S70: [压铸工艺与模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6ce579f-c0db-4426-8596-ea89def96772/resource) (`a6ce579f-c0db-4426-8596-ea89def96772`)
- S14: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1af860e7-9adb-4067-96e7-9fd26760c000/resource) (`1af860e7-9adb-4067-96e7-9fd26760c000`)
- S2: [effect of microstructure and casting defects on the mechanical propertie__7978147656](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04118443-5a6a-4d2a-98e4-3cca5d9fa8ab/resource) (`04118443-5a6a-4d2a-98e4-3cca5d9fa8ab`)
- S24: [a study of porosity formation in pressure die casting using the taguchi__4ac320727f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28220c1a-a3c3-4bae-af04-9e8f13a9c000/resource) (`28220c1a-a3c3-4bae-af04-9e8f13a9c000`)
- S27: [a study of porosity formation in pressure die casting using the taguchi__4ac320727f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/373145fd-0ac2-4c63-bf89-5bc7ecb66dbd/resource) (`373145fd-0ac2-4c63-bf89-5bc7ecb66dbd`)
- S42: [0014_87856067f62dd15d_Hydrogen_gas_porosity](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60f822f1-7b19-48b1-a43b-1f82381729ce/resource) (`60f822f1-7b19-48b1-a43b-1f82381729ce`)
- S49: [铝硅合金半固态压铸成形产品缺陷的形成机理及控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e2aeb4f-a4a9-4c6c-997a-5687b9de2e78/resource) (`6e2aeb4f-a4a9-4c6c-997a-5687b9de2e78`)
- S31: [die cast engineering a hydraulic thermal and mechanical process__e5dfda1a8e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4459cacb-f0bd-4f2a-96da-7e237e3345dc/resource) (`4459cacb-f0bd-4f2a-96da-7e237e3345dc`)
- S66: [铝硅合金半固态压铸成形产品缺陷的形成机理及控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e225a9b-1840-443e-a394-2bc02699d936/resource) (`9e225a9b-1840-443e-a394-2bc02699d936`)
- S54: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8133575e-ab69-4ad3-b5cb-a378ad55b130/resource) (`8133575e-ab69-4ad3-b5cb-a378ad55b130`)
- S94: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e86fe5cb-7dbe-4ea9-b8e3-53f4c1c8b414/resource) (`e86fe5cb-7dbe-4ea9-b8e3-53f4c1c8b414`)
- S57: [压铸铝合金研究现状与未来发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/840eccac-109a-4f78-bb05-6951efd628f4/resource) (`840eccac-109a-4f78-bb05-6951efd628f4`)
- S84: [0007_a4aca2210548531f_Integrated_die_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5faa39d-e0e5-47e3-abd3-603943cea395/resource) (`c5faa39d-e0e5-47e3-abd3-603943cea395`)
- S56: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82013eee-6b17-4059-9384-bca4ce09589a/resource) (`82013eee-6b17-4059-9384-bca4ce09589a`)
- S19: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23d65afd-66a9-43d8-8a8a-6469fcd2d3e6/resource) (`23d65afd-66a9-43d8-8a8a-6469fcd2d3e6`)
- S80: [新能源汽车用铸造铝合金的研究现状和发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb6cbc7a-0c5a-4d14-b863-007d7058ce0c/resource) (`bb6cbc7a-0c5a-4d14-b863-007d7058ce0c`)
- S61: [压铸铝合金技术标准现状及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e25896b-a9f0-4b9a-b1b8-5bb0f33845ce/resource) (`8e25896b-a9f0-4b9a-b1b8-5bb0f33845ce`)
- S65: [64380928_压铸铝合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/946c37f9-0dac-4d06-9c46-873a93dcf173/resource) (`946c37f9-0dac-4d06-9c46-873a93dcf173`)
- S37: [表 C.1 压铸铝合金特点及应用举例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/552e31b3-c97a-44e6-b43f-164be4fa76c1/resource) (`552e31b3-c97a-44e6-b43f-164be4fa76c1`)
- S50: [铝与铝合金速查手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75cdf832-c7ba-4def-a834-92209670b6e0/resource) (`75cdf832-c7ba-4def-a834-92209670b6e0`)
- S81: [铝及铝合金的分类图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2813d2f-e201-45e5-8352-dce277f6fa88/resource) (`c2813d2f-e201-45e5-8352-dce277f6fa88`)