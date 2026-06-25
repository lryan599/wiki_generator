---
version: "v1"
generated_at: "2026-06-18T14:53:43+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 49
  source_quality_score: 0.84
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 定义与基本原理

黏结剂喷射打印（Binder Jetting，简称BJP），又称三维喷涂粘接快速成形、三维黏结印刷、选择性粉末黏结快速成形，通用行业别名为3DP（Three Dimensional Printing，三维印刷/三维打印）。该工艺于1989年由美国麻省理工学院Emanuel M. Sachs团队发明并获得专利，是一种以粉末床为基础的增材制造工艺，其核心特征在于无需激光等高能热源介入，通过喷头选择性喷射黏结剂来黏结粉末材料实现成形，属于物理粘接过程，这与SLS依靠激光烧结粉末的化学/熔融过程有本质区别[[S34, S15, S35, S19, S3]]。

BJP的标准成形流程为：
1. 用铺粉装置在成形活塞上方铺设一层设定厚度的粉末材料（金属、陶瓷、塑料、砂、石膏等均可）；
2. 喷头根据三维CAD模型导出的当前层二维截面轮廓信息，在已铺好的粉层上有选择性地喷射黏结剂，使目标区域的粉末粘接形成单层截面；
3. 成形工作台下降一个等同于单层厚度的高度；
4. 重复铺粉、喷射黏结剂的循环，直至完成整个三维生坯的构建；
5. 清理未被黏结的松散粉末。后续可根据需要通过浸蜡、浸渍树脂、脱脂、烧结等后处理工序进一步提升制件强度[[S34, S22, S55, S58]]。

在该工艺中，未被喷射黏结剂的松散粉末直接在成形过程中起支撑作用，因此无需额外设计或打印支撑结构，能够直接制造含悬臂及复杂内腔的结构件。其高度方向成形速度可达25~50 mm/h，设备成本远低于采用激光热源的SLM等工艺，粉末原材料成本低，成形过程无污染，可在普通办公环境下部署。常规制件生坯精度约为0.1~0.2 mm，原始生坯强度较低[[S34, S19, S23, S8]]。

![图：黏结剂喷射打印核心结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf8a07b9-9424-4b97-b9c6-125787061c42/resource)

**图：黏结剂喷射打印核心结构示意图**，呈现喷头喷射黏结剂到粉末床的核心结构[[S41]]。

## 工艺发展与变体

黏结剂喷射打印技术的产业化应用大致经历了三个阶段：1990年代的石膏基材料模型快速打印阶段；2010年代的陶瓷铸造型芯制造阶段；2020年代的多材料金属间接增材制造阶段[[S8]]。

不同衍生技术路线具有各自侧重的应用领域：
- **通用3DP工艺**：基于MIT原创专利的通用版本，可适配塑料、陶瓷、金属、石膏等多类粉末，面向快速原型制造场景，部分商业化版本支持彩色模型打印。
- **PCM工艺（Patternless Casting Manufacturing，无木模铸型制造技术）**：清华大学基于MIT 3DP专利自主研发的本土化衍生工艺，采用双喷头同路径二次扫描的方式，分别喷射树脂黏结剂与催化剂，直接实现铸造砂型/砂芯的自动化制造，现已由峰华卓立等企业实现产业化，量产设备最大成型空间可达2200mm×1000mm×800mm。
- **DSPC工艺（Direct Shell Production Casting，直接壳型铸型工艺）**：美国Soligen Technology Inc.基于MIT 3DP专利开发的面向精密铸造的衍生工艺。
- **其他衍生路线**：GS铸型制造工艺、ZCast Direct Metal Casting工艺等为同期基于3DP专利开发的面向砂型铸造的工业化路线[[S18, S16, S54, S3, S28]]。

## 喷射驱动方式

在黏结剂喷射成形工艺中，打印头的驱动方式直接影响液滴生成精度、材料适应性和工艺稳定性。三类主流驱动方式及其对比见下表[[S9, S47]]：

| 驱动方式 | 喷射频率 | 液滴体积/pL | 黏度适应性 | 典型适用场景 | 主要局限 |
|---------|---------|------------|-----------|-------------|---------|
| 热发泡式 | 10~30 kHz | 5~30 | 较低 | 薄壁蜡模、精密砂芯等超高分辨率场景 | 易导致黏结剂热降解、喷头空蚀磨损，长时间作业维护成本高 |
| 气动式 | ≤5 kHz | 20~200 | ≤30 cPs | 高黏度、高温黏结剂场景，如陶瓷铸型 | 喷射频率低，液滴轨迹易偏移，设备能耗与运维成本偏高 |
| 压电式 | 1~80 kHz | 10~90 | 较低 | 中大型砂型的高速稳定制造 | 高黏度黏结剂易堵塞流道，精密元件长期可靠性有待验证 |

## 砂型/砂芯制造中的应用

BJP技术在砂型铸造领域已实现从实验室研究到工业化应用的跨越，其核心价值在于突破了传统工艺的几何复杂度限制，使铸造砂型/砂芯可通过数字化方式直接成形，完全免除了传统木质/金属母模的制备环节。全球领先企业如ExOne（现属Desktop Metal）、Voxeljet、宁夏共享（KOCEL）、峰华卓立等已将3D打印砂型设备广泛应用于汽车、航空航天等领域[[S39, S12, S50, S54, S56]]。

面向压铸及近净成形铸造的典型应用场景涵盖：汽车缸体/缸盖、涡轮增压器蜗壳、转向节、大流量液压多路阀等复杂铸件的砂型及内置细孔砂芯制备，以及航空领域复杂结构砂芯的快速试制[[S39, S12, S50, S54, S56]]。

![黏结剂喷射3D打印砂型逐层成形工艺流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb9f01ab-cf6e-46d6-b6e3-ffd35b17cc80/resource)

**图：黏结剂喷射3D打印砂型逐层成形工艺流程**，依次呈现铺粉材料、选择性喷射黏结剂、工作台下降的完整循环过程[[S57]]。

## 核心工艺参数

### 层厚

层厚是BJP工艺的基本参数之一，需与粉末粒度及渗透性协同设定[[S29]]。不同应用场景的典型层厚区间如下：

| 应用场景 | 推荐层厚 | 说明 |
|---------|---------|------|
| 砂型3D打印 | 0.2~0.3 mm | 适配50/100目粒度砂材 |
| 水玻璃基砂型 | 0.2 mm | 适配50%黏结剂饱和度 |
| 金属基BJP（316L不锈钢） | 50 μm | 配合压实工艺 |
| 钨合金BJP | 50~100 μm | 需协同饱和度设定 |

过厚的层厚会导致底层粉末难以充分润湿，过薄虽有利于提高分辨率，但容易放大铺层缺陷并引发翘曲[[S43, S46, S55, S32, S29]]。

### 黏结剂饱和度

黏结剂饱和度定义为喷射黏结剂体积与对应粉层空隙体积的比值，是影响生坯强度的关键参数[[S55]]。不同材料体系的饱和度参考范围：

| 材料体系 | 推荐饱和度 | 备注 |
|---------|-----------|------|
| WC-12%Co（50~70μm层厚） | 50%~75% | 强度随饱和度升高而提高 |
| WC-12%Co（100μm层厚） | 60%~100% | 层厚较大时需更高饱和度 |
| 水玻璃基砂型 | 50% | 配合10wt.%水玻璃粉添加量 |
| 类煤岩砂型 | 50% | 兼顾强度与成型性能 |

水玻璃体系在50%饱和度、0.2 mm层厚条件下制备的砂样抗拉强度可达4.5 MPa，最大发气量为8.1 L/kg[[S55, S32, S48]]。

### 固化与烘烤参数

| 材料体系 | 固化/烘烤条件 | 说明 |
|---------|-------------|------|
| 316L不锈钢BJP生坯 | 180℃，4h预固化 | 确保生坯具有足够转运强度 |
| 砂型烘烤工艺 | 175℃保温2h，自然冷却2h | 提升砂型强度 |
| ExOne改性水玻璃无机黏结剂 | 微波固化 | 砂型最终强度250~400 N/cm² |

### 打印速度

BJP无热源3DP工艺的高度方向成形速度常规为25~50 mm/h，批量化场景下可达100 L/h以上[[S34, S39]]。钨合金BJP打印的干燥及铺展速度推荐为10 mm/s[[S55]]。

## 材料体系

### 原砂

砂型3DP打印的核心基础材料为原砂，其质量与体积占比在98%以上。常用三类原砂的特性对比如下[[S14, S44, S2, S53, S6]]：

| 原砂类型 | 主要成分 | 粒度 | 流动性 | 发气量(850℃) | 烘烤后抗拉强度 | 适用场景 |
|---------|---------|------|--------|-------------|-------------|---------|
| 石英砂（高硅砂） | SiO₂≥97% | 50/100目 | 较低 | 最高（≥10 mL/g级） | 最低 | 常规有色合金、铸铁铸造，成本最低 |
| 陶瓷砂 | Al₂O₃、SiO₂复合氧化物 | 50/100目 | 优 | 8.9 mL/g | 最高（可达3.3 MPa） | 对铸件质量要求高的场景 |
| 再生砂 | SiO₂≥80% | 50/100目 | 优（与陶瓷砂相同） | 8.7 mL/g | 介于两者之间 | 成本可控，适配中小铸件 |

三类砂的三筛（50目/70目/100目）集中度均可达到75%以上[[S44]]。从综合性能看，80~140目区间的原砂打印性能最优[[S36, S12]]。

### 有机黏结剂

| 黏结剂类型 | 特性 | 适用场景 |
|-----------|------|---------|
| 呋喃树脂 | 适配绝大多数常规砂型打印场景，发气量中等，固化工艺成熟，热分解过程平稳 | ExOne、Voxeljet、宁夏共享、峰华卓立等主流打印设备的标准兼容黏结剂 |
| 改性甲阶酚醛树脂 | 树脂加入量低，硬化速度可调，环保无刺激性气味，二次硬化特性显著，旧砂再生率高（硅砂≥95%，宝珠砂/陶粒砂≥98%） | 对铸件表面质量要求高的场景 |

### 无机黏结剂

为克服有机黏结剂在打印过程中产生刺激性气体、发气量大等问题，无机黏结剂已成为行业发展的重要方向[[S27]]。

| 类型 | 代表性产品/方案 | 特性 | 强度 |
|------|---------------|------|------|
| 改性水玻璃基 | ExOne公司 | pH=12，密度1.3g/cm³，配套微波固化 | 250~400 N/cm² |
| 冷固化无机黏结剂 | Voxeljet（2023年推出） | 打印后无需额外加热即可完全固化 | — |
| 双组分热硬化无机黏结剂 | 宁夏共享 | 组分A黏度8~12 mPa·s（20℃），环保低发气量 | — |

在环境保护方面，无机黏结剂具有显著优势：有机黏结剂的BTEX排放量约为20.44 mg/g，而无机黏结剂仅为0.043 mg/g，排放量降低了约475倍[[S20]]。

## 砂型性能

### 尺寸精度

采用BJP工艺制备的砂型尺寸精度可达到GB/T 6414-2017规定的CT11级。通过灰度打印调控黏结剂渗透量及层厚补偿策略后，局部尺寸精度可达±0.1mm[[S1, S12]]。

### 表面粗糙度

原始打印砂型的表面粗糙度Ra约为25μm级别，经耐火涂层处理后Ra可降至3~5μm，有效抑制铸件粘砂缺陷[[S13]]。

### 力学性能

- 采用呋喃树脂体系并经烘烤后，砂型抗拉强度≥2.4MPa；陶瓷砂基质的BJP砂型抗拉强度最高可达3.3MPa[[S40]]。
- 改性水玻璃基砂型的常温抗压强度为250~400 N/cm²[[S32]]。

### 发气量与导热性能

- 采用80~140目陶瓷砂或再生砂制备的BJP砂型，在850℃条件下的发气量仅为8.7~8.9 mL/g，较大气量高硅砂砂型低1.5 mL/g以上，可有效降低铝合金/镁合金铸造过程中的气孔缺陷率[[S40, S53]]。
- 呋喃树脂砂型的室温导热系数约为0.5 W/(m·K)，其树脂热分解过程平缓，可使铝合金铸件凝固时间延长约12.5%，有利于优化铸件内部致密度[[S40, S12]]。

当树脂喷墨量保持固定时，3DP砂型的发气量几乎不受固化剂加入量（0.2%~0.4%区间）和打印层厚（0.2mm~0.45mm区间）的显著影响，这为低发气量BJP砂型的工艺优化提供了重要依据[[S10]]。

## 后处理流程

工业级BJP砂型制备的典型后处理流程依据黏结剂体系的不同分为两种路径[[S32, S27, S5]]：

**有机黏结剂体系（呋喃树脂/酚醛树脂）路径**：
1. 打印完成后在室温下完成黏结剂与预混固化剂的交联反应；
2. 送入加热工位进行二次固化提升整体强度；
3. 通过吹净、负压抽吸去除未粘接的散砂；
4. 在砂型表面浸涂/喷涂耐火涂料完成表面精整。

**无机改性水玻璃黏结剂体系路径**：
1. 打印完成后将工作箱直接转运至微波工位进行快速固化；
2. 转至脱砂工位去除浮砂；
3. 送入精整区修整边缘毛刺。

Voxeljet推出的冷固化无机黏结剂技术则可在打印成形后无需微波固化即可形成砂型和砂芯，进一步简化了后处理流程[[S32]]。

## 工艺优势与局限性

### 核心优势

1. **低设备成本**：无需高能热源介入，室温即可成形，设备成本低于传统SLM工艺的40%，粉末材料价格低廉[[S8, S34]]。
2. **高成形效率**：高度方向成形速度达25~50 mm/h，批量化场景下单台设备工件加工能力可超过100 L/h，月加工量可超过10吨[[S34, S42, S39]]。
3. **无支撑结构要求**：未粘接粉末自然构成支撑，可实现复杂镂空、带内腔构件的直接制造[[S34, S19, S23]]。
4. **材料广泛性**：理论上任何可制备成粉末的材料均可适用于该工艺，对粉末球形度要求低[[S8, S34]]。
5. **环境友好性**：成形过程无有害气体排放，可在办公室环境下作业[[S34]]。

### 主要局限性

1. **原生精度与强度较低**：生坯精度仅为0.1~0.2mm，表面粗糙度较差，原生强度低[[S34, S42]]。
2. **后处理流程长**：打印后通常需经脱脂、烧结等工序，整体制备流程较长，后处理过程易引入孔隙缺陷[[S55]]。
3. **大尺寸金属件公差控制难**：烧结过程存在高维向收缩效应，商业化致密金属打印件单重普遍不超过400g，精度最高仅能维持在0.1~0.2mm区间[[S37]]。
4. **可商业化金属材料牌号有限**：主流仅包含316L、17-4PH不锈钢等少数品种，钛合金、高温合金仍处于推广阶段，铝合金部分牌号适配难度高[[S37]]。
5. **喷头固有技术瓶颈**：热发泡驱动存在热降解与空蚀磨损问题；气动驱动喷射频率低、液滴轨迹易偏移；压电驱动对高黏度黏结剂适应性差，流道易堵塞[[S9]]。

## 设备与供应商

### 国外供应商

| 供应商 | 代表设备 | 成型空间 | 黏结剂体系 | 适配材料 | 定位 |
|-------|---------|---------|-----------|---------|------|
| Voxeljet（德国） | VX200 | 小型 | 呋喃树脂、酚醛树脂、无机黏结剂 | 砂材 | 实验室/高校研究 |
| | VX1000 | 通用型 | 同上 | 砂材 | 砂型铸造厂及研发部门 |
| | VX4000 | 超大成型空间 | 同上 | 砂材 | 连续化工业量产 |
| ExOne（美国） | S-Print, S-Max, S-Max Pro | 系列覆盖多尺寸 | 呋喃树脂、酚醛树脂、无机黏结剂 | 砂材、金属、陶瓷 | 原型设计到批量生产全覆盖 |

### 国内供应商

| 供应商 | 代表设备 | 成型空间 | 黏结剂体系 | 技术来源 |
|-------|---------|---------|-----------|---------|
| 峰华卓立 | PCM 800, PCM 1800, PCM 2200 | 最大2200×1000×800 mm | 呋喃树脂、酚醛树脂 | 清华大学PCM技术 |
| 宁夏共享（KOCEL） | AJS 800A, AJS 1800A, IDream系列 | IDream-2515: 2500×1500×1400 mm | 呋喃树脂、酚醛树脂、双组分热硬化无机黏结剂 | 自主研发，全链条国产化 |

宁夏共享AJS 1800E机型的打印分辨率大于300dpi，打印层厚范围0.2~0.5mm，打印精度可达±0.35mm[[S24, S30]]。

## 与其他增材制造工艺的对比

BJP与SLS、SLA三大主流增材制造工艺的量化对比如下[[S34, S42, S45, S51, S7, S21, S11]]：

| 对比维度 | BJP（黏结剂喷射） | SLS（激光选区烧结） | SLA（立体光刻） |
|---------|-----------------|-------------------|----------------|
| 成形原理 | 喷射黏结剂物理粘接粉末 | 激光烧结/熔融粉末 | 紫外激光固化液态光敏树脂 |
| 精度 | 0.1~0.2 mm | 常规±0.1 mm左右，整体±(0.05~2.5)mm | ±0.1 mm，高精场景可达0.1%公差 |
| 生产速率 | 高度方向25~50 mm/h | 介于两者之间 | 制模速度约7 mm/h |
| 设备成本 | 最低（无需昂贵激光源） | 居中 | 较高（紫外激光管寿命仅2000h，运行成本高） |
| 可制造尺寸 | 砂型可达米级，致密金属件单重≤400g | 主流可达330×381×432 mm | 可通过分块拼接实现大尺寸 |
| 适用材料 | 塑料、砂、陶瓷、大多数金属粉末，粉末球形度要求低 | 热塑性塑料、金属、陶瓷等可烧结粉末 | 仅液态光敏树脂 |
| 支撑结构 | 不需要（松散粉末自支撑） | 不需要（松散粉末自支撑） | 需要设计并打印支撑 |
| 后处理 | 需脱脂、烧结，复杂度最高 | 仅需清粉、可选浸渗，复杂度居中 | 需清洗、去支撑、二次紫外固化，复杂度居中 |

## Sources
- S34: [模具表面处理与表面加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7ddd8be-4532-4a00-b63f-68e318c891d0/resource) (`b7ddd8be-4532-4a00-b63f-68e318c891d0`)
- S15: [0220_535b2369e5404b96_快速成型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a5fe165-6f30-4484-82df-7f37cbb7576a/resource) (`4a5fe165-6f30-4484-82df-7f37cbb7576a`)
- S35: [中国材料工程大典第25卷材料特种加工成形工程下册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7fc0f2a-4124-4be9-a4a5-5b3c1535671c/resource) (`b7fc0f2a-4124-4be9-a4a5-5b3c1535671c`)
- S19: [模具制造技术问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68101b71-f1e0-4583-b125-e0e74ab47d24/resource) (`68101b71-f1e0-4583-b125-e0e74ab47d24`)
- S3: [中国材料工程大典第25卷材料特种加工成形工程下册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d837b86-189e-4b19-9d06-d59fb7b462fe/resource) (`0d837b86-189e-4b19-9d06-d59fb7b462fe`)
- S22: [快速模具设计与制造技术高级](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77d68267-0328-42dc-8d61-e9e1018acd61/resource) (`77d68267-0328-42dc-8d61-e9e1018acd61`)
- S55: [增材制造钨合金及其强韧化研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f143f23a-3d01-4250-8baa-47708730fd3a/resource) (`f143f23a-3d01-4250-8baa-47708730fd3a`)
- S58: [机械加工工艺手册第3卷系统技术卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd140ec6-8405-4c3c-88cd-b2ee0f5e3092/resource) (`fd140ec6-8405-4c3c-88cd-b2ee0f5e3092`)
- S23: [快速成型与快速模具制造技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7905b173-f8ca-496b-96fd-588b6de39e35/resource) (`7905b173-f8ca-496b-96fd-588b6de39e35`)
- S8: [粘结剂喷射成形在铸造领域的应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a207616-e972-45dd-ad84-bddb7a44fa76/resource) (`2a207616-e972-45dd-ad84-bddb7a44fa76`)
- S41: [喷射黏结剂的立体打印快速成形机原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf8a07b9-9424-4b97-b9c6-125787061c42/resource) (`cf8a07b9-9424-4b97-b9c6-125787061c42`)
- S18: [机械加工工艺手册第3卷系统技术卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c9cf82d-2d86-4f4e-9116-55730048676d/resource) (`5c9cf82d-2d86-4f4e-9116-55730048676d`)
- S16: [中国材料工程大典第25卷材料特种加工成形工程下册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a8a8d8f-b227-4b84-bfdf-5e46ca518a8a/resource) (`4a8a8d8f-b227-4b84-bfdf-5e46ca518a8a`)
- S54: [工业级砂型打印机墨滴喷射仿真与供墨系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eea433e3-02c7-4a84-935a-2b8f91f10e88/resource) (`eea433e3-02c7-4a84-935a-2b8f91f10e88`)
- S28: [金属精密液态成型技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d06fb51-9b78-44ba-bfd4-95e4fce57e0a/resource) (`9d06fb51-9b78-44ba-bfd4-95e4fce57e0a`)
- S9: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ebbfe0d-7687-44e7-8f3a-75c0a8a38cc0/resource) (`2ebbfe0d-7687-44e7-8f3a-75c0a8a38cc0`)
- S47: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d7d3e519-0965-4517-8464-c9a03a551111/resource) (`d7d3e519-0965-4517-8464-c9a03a551111`)
- S39: [粘结剂喷射成形在铸造领域的应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bcdbce3e-1095-4fd4-9732-b871846eeb56/resource) (`bcdbce3e-1095-4fd4-9732-b871846eeb56`)
- S12: [粘结剂喷射成形在铸造领域的应用研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3dcfe696-cc45-4625-aea5-45d2436f2b43/resource) (`3dcfe696-cc45-4625-aea5-45d2436f2b43`)
- S50: [工业级砂型打印机墨滴喷射仿真与供墨系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e02313fc-b81b-439d-8c8a-ff1b06087027/resource) (`e02313fc-b81b-439d-8c8a-ff1b06087027`)
- S56: [基于3D打印工艺的整体式液压阀快速制造技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4c48dec-2573-4a75-9343-090005cb0a2e/resource) (`f4c48dec-2573-4a75-9343-090005cb0a2e`)
- S57: [喷射黏结剂的立体打印快速成形机工作原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb9f01ab-cf6e-46d6-b6e3-ffd35b17cc80/resource) (`fb9f01ab-cf6e-46d6-b6e3-ffd35b17cc80`)
- S29: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1b5e09d-b420-46ad-8450-7753daae2ec3/resource) (`a1b5e09d-b420-46ad-8450-7753daae2ec3`)
- S43: [黏结剂改性对黏结剂喷射3D打印316L不锈钢显微组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d20cadbf-9ea9-412f-904b-549cde93d6cf/resource) (`d20cadbf-9ea9-412f-904b-549cde93d6cf`)
- S46: [3D打印类岩体内置充填裂隙强度控制方法及其影响规律研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5745be3-bbe1-4044-ab6d-498c7c4219e1/resource) (`d5745be3-bbe1-4044-ab6d-498c7c4219e1`)
- S32: [TextNode10](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b00c1f25-ab4e-4db4-bf97-f521f2a2862d/resource) (`b00c1f25-ab4e-4db4-bf97-f521f2a2862d`)
- S48: [表 4 不同后处理方式试样打印参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d816219b-2a1e-4ffc-8b94-cfbc9bdf4aa4/resource) (`d816219b-2a1e-4ffc-8b94-cfbc9bdf4aa4`)
- S14: [3D打印砂型对A356铝合金铸造工艺及铸件性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47567324-6bb3-4186-9b13-c86b8d97408c/resource) (`47567324-6bb3-4186-9b13-c86b8d97408c`)
- S44: [3D打印砂型对A356铝合金铸造工艺及铸件性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2e7cd6a-5258-465a-9e44-c41da4ec28dd/resource) (`d2e7cd6a-5258-465a-9e44-c41da4ec28dd`)
- S2: [3D打印砂型对A356铝合金铸造工艺及铸件性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07e6d88c-ff66-41e1-93c5-6be6fc3df711/resource) (`07e6d88c-ff66-41e1-93c5-6be6fc3df711`)
- S53: [图3-7 三种砂型发气量对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb56cbfd-0b89-4003-bc81-360156820bda/resource) (`eb56cbfd-0b89-4003-bc81-360156820bda`)
- S6: [图3-5 烘烤前、后抗拉强度测试变化关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1bb9e482-4c27-465d-acda-e157a3124324/resource) (`1bb9e482-4c27-465d-acda-e157a3124324`)
- S36: [基于3D打印多层壳镂空砂型的铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/baadfa74-8c26-45a1-a950-6b395be61c89/resource) (`baadfa74-8c26-45a1-a950-6b395be61c89`)
- S27: [TextNode9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/947df99e-b92a-41f6-8183-02df30623523/resource) (`947df99e-b92a-41f6-8183-02df30623523`)
- S20: [图2 有机黏结剂与无机黏结剂在铸造生产中BTEX排放对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f5a6812-7f55-4c68-b2a9-999a676cf298/resource) (`6f5a6812-7f55-4c68-b2a9-999a676cf298`)
- S1: [一种奥氏体不锈钢的四缸柱塞泵的铸造工艺研发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/060b8f4e-b149-4987-901a-a12c20cb46da/resource) (`060b8f4e-b149-4987-901a-a12c20cb46da`)
- S13: [水可溃散砂质芯模设计及其在中空异形碳纤维复合材料成型中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43c5ed4f-4e76-4f84-8217-590260293ce5/resource) (`43c5ed4f-4e76-4f84-8217-590260293ce5`)
- S40: [3D打印砂型对A356铝合金铸造工艺及铸件性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ca962fbd-5379-49fc-aabf-9c5e67667c9c/resource) (`ca962fbd-5379-49fc-aabf-9c5e67667c9c`)
- S10: [图3-12(c) 固化剂加入量与打印层厚对打印砂型发气量的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/328d13d3-da9b-4df3-9e51-216ac65a8e00/resource) (`328d13d3-da9b-4df3-9e51-216ac65a8e00`)
- S5: [基于3D打印多层壳镂空砂型的铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12e3887d-7ab0-4cec-bb31-7338b743bd5e/resource) (`12e3887d-7ab0-4cec-bb31-7338b743bd5e`)
- S42: [模具制造技术问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1e9dc0b-41e2-42df-89bf-55d266903b83/resource) (`d1e9dc0b-41e2-42df-89bf-55d266903b83`)
- S37: [additive manufacturing of metal alloys 1 processes raw materials and numerical simulation__200a158ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc8bb06c-dd5b-480d-9d9e-e8a214ff7f4e/resource) (`bc8bb06c-dd5b-480d-9d9e-e8a214ff7f4e`)
- S24: [工业级砂型打印机墨滴喷射仿真与供墨系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7db1d150-a2ee-4639-aec9-cc6964d935b2/resource) (`7db1d150-a2ee-4639-aec9-cc6964d935b2`)
- S30: [Mg-10Gd-2Y-1Zn-0.5Zr镁合金基座件基于有限元模拟的铸造残余应力研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aaa41689-180e-4999-8604-4d65f2d84a88/resource) (`aaa41689-180e-4999-8604-4d65f2d84a88`)
- S45: [特种铸造与先进铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3b15384-8e2b-4fbc-b1c2-0a1ba99cf369/resource) (`d3b15384-8e2b-4fbc-b1c2-0a1ba99cf369`)
- S51: [模具设计与制造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e02bd211-e0fb-4099-9c24-7b8dd1bb1b91/resource) (`e02bd211-e0fb-4099-9c24-7b8dd1bb1b91`)
- S7: [模具材料及制造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c554cea-53c2-49a9-be19-946eccb2052c/resource) (`1c554cea-53c2-49a9-be19-946eccb2052c`)
- S21: [现代模具制造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/741da16f-5742-4fb7-b76b-1ff63f695c3f/resource) (`741da16f-5742-4fb7-b76b-1ff63f695c3f`)
- S11: [0220_535b2369e5404b96_快速成型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34287220-fedf-4ba1-b9d6-b09db5f39ab5/resource) (`34287220-fedf-4ba1-b9d6-b09db5f39ab5`)