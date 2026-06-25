---
version: "v1"
generated_at: "2026-06-18T11:02:51+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 34
  source_quality_score: 0.87
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

## 定义与术语

**电感耦合等离子体发射光谱仪/法**（Inductively Coupled Plasma Optical Emission Spectrometry，简称ICP-OES）是基于常压下氩等离子体为激发源，通过测量自由原子和离子发射的特征光强度来实现元素定量分析的仪器与方法，可同时测定七十余种金属元素及部分非金属元素 [[S32,S15]]。

行业内ICP-AES（Inductively Coupled Plasma Atomic Emission Spectrometry，电感耦合等离子体原子发射光谱法）与ICP-OES为完全等效的常用别名，二者不存在技术层面的本质差异 [[S18,S29,S1]]。AES是原子发射光谱的广义大类，涵盖电子、X射线、光学光子等所有原子发射形式；OES则特指仅测量紫外-可见-红外光学波段发射的子类，因此OES的表述更为精确 [[S18]]。

## 工作原理

ICP-OES的完整分析流程为：金属样品经酸消解制成水溶液后，通过雾化器转化为细气溶胶，送入温度高达8000~10000 °C的氩等离子体高温区。待测物在等离子体中完全蒸发、原子化/离子化并被激发到高能级，当原子或离子从高能级跃迁返回低能级时，发射出对应元素特征波长的光。不同波长的光信号经分光系统分离后由检测器测量，信号强度与待测元素浓度成正比，通过外标校准曲线实现定量分析 [[S18,S2]]。

## 仪器组成

ICP-OES的核心部件包括 [[S32,S27]]：

| 部件 | 功能 |
|------|------|
| 进样系统（雾化器、雾室） | 将液体样品转化为细气溶胶，均匀送入等离子体 |
| 等离子体炬管与水冷铜质射频感应线圈 | 线圈通电产生振荡磁场，用于引燃并维持等离子体 |
| 射频（RF）发生器 | 提供高频能量耦合，维持等离子体稳定运行 |
| 分光系统 | 常用374 线/毫米的中阶梯光栅，将复合发射光色散分离为不同波长的单色光 |
| 信号检测器 | 光电倍增管或CID固态检测器，将光信号转换为线性对应的电信号输出 |

典型顺序（单色器）ICP-OES的结构与光路示意如下，展示从样品进样、等离子体激发到光谱分光与信号检测的完整工作路径 [[S24]]：

![典型顺序（单色器）ICP-OES的结构与光路示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1f9057e-838d-4f95-8b71-7b3c97cc7771/resource)

ICP-OES光学系统光路原理示意如下，依次标注ICP光源、入射狭缝、凹面反射镜、光栅、出射狭缝和探测器的完整光学路径 [[S11]]：

![ICP-OES光学系统光路原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57114605-a555-4b1e-bb8f-191be98d632f/resource)

## 观测方式分类

按等离子体观测方式，ICP-OES可分为三类 [[S32]]：

| 观测方式 | 特点 | 适用场景 |
|----------|------|----------|
| 径向观测（垂直观测） | 从等离子体侧面采集信号，抗基体干扰能力强 | 高浓度常量元素分析 |
| 轴向观测（水平观测） | 沿等离子体轴向采集信号，光程更长，灵敏度更高 | 痕量元素分析 |
| 双向观测（Dual View） | 可同时切换两种观测模式 | 兼顾高浓度和低浓度元素检测 |

## 典型操作条件

ICP-OES实验室环境温度需稳定控制在20~25 °C ± 2 °C [[S37]]。核心操作参数包括RF功率、等离子气流量、辅助气流量、雾化器载气流量和观测高度，不同型号仪器需在厂商推荐范围内调整以获得最佳信号强度 [[S37,S32,S34,S25]]。

ICP-OES典型仪器操作参数量示例如下 [[S34]]：

| 参数 | 数值 |
|------|------|
| 功率 | 按厂商推荐 |
| 等离子气流量 | 按厂商推荐（L/min） |
| 辅助气流量 | 按厂商推荐（L/min） |
| 雾化器流量 | 按厂商推荐（L/min） |
| 重复读取时间 | 仪器设定（s） |
| 仪器稳定延迟 | 仪器设定（s） |
| 样品吸取延迟 | 仪器设定（s） |
| 泵速 | 仪器设定 |
| 快速泵模式 | 开启/关闭 |

## 样品前处理

### 常规酸溶法

压铸合金ICP-OES分析的常规前处理流程为：将金属取样获得的锯屑/碎屑用合适的混合酸完全消解，定容为水溶液后经雾化器生成气溶胶送入等离子体进行分析，常规样品称样量范围为0.01~1 g [[S20,S18]]。

**王水消解标准流程**：称取0.5 ± 0.001 g合金样品，先后加入1 mL硝酸、2 mL盐酸静置反应5 min，置于90~100 °C水浴中加热3.5 h，每20 min摇匀一次，取出补加1 mL盐酸冷却后加6 mL去离子水，离心获得澄清溶液直接用于ICP-OES检测 [[S21,S14]]。

**三酸消解流程（适用于高硅等难溶压铸合金）**：称取0.5 ± 0.001 g合金样品，先后加入10 mL硝酸、10 mL盐酸、4 mL高氯酸，加热至冒高氯酸烟但不可蒸干，冷却后补加10 mL盐酸，在低于90 °C条件下温热10 min，转移定容到50 mL容量瓶后获得澄清待测液 [[S23]]。

**铝合金压铸试样消解**：称取0.05 g样品，采用6 mL 70 wt.%硝酸 + 1 mL 30 wt.%双氧水 + 1 mL 37 wt.%盐酸 + 0.5 mL 40 wt.%氢氟酸的混合酸体系消解，置于180 °C烘箱中加热8 h，定容后即可获得澄清待测溶液 [[S8]]。

### 标准分析流程

ICP-OES测定的完整标准分析流程包含称样、酸消解、离心澄清、仪器测量和质量控制判定等环节，检测过程中需同步运行标准物质（CRM）样品与校准标准系列，若质控样检测结果偏差超出允许范围则需重新测定，所有质控数据合格后方可输出最终检测报告 [[S21,S14,S23]]。

## 定量方法

### 外标标准曲线法

以多元素一级标准物质配制系列梯度校准溶液，建立浓度-发射强度的线性拟合关系进行定量。ICP-OES校准曲线的线性动态范围可达10⁴~10⁸，可覆盖压铸合金从主量元素到痕量杂质的全浓度检测需求 [[S18,S19]]。

### 内标法

当待测压铸合金样品总溶解固体（TDS）含量大于1%时，需采用内标法校正不同样品间黏度、表面张力差异带来的物理传输误差。通用的内标元素可选用Sc、Sr、Y、In、Ge、Mo，可显著提升高浓度基体样品的检测稳定性 [[S32]]。

## 性能特点

### 检测能力与精度

ICP-OES的方法检出限定义为3倍空白背景信号的标准偏差，常规压铸合金检测场景下检出限为亚ppb~100 ppb级别，检测性能优于FAAS，部分场景稍逊于ICP-MS [[S32,S2]]。

径向观测型仪器检出限可达μg/L级，轴向观测型仪器检出限比径向型低5~10倍，部分痕量元素如Cd检出限可达0.09 × 10⁻⁹，Pb、Sb、Se检出限可达1.5 × 10⁻⁹级别 [[S10,S31]]。方法测量不确定度为3%~5%，元素覆盖范围可从Li到U [[S31,S32]]。

### ICP-OES与ICP-MS对比

| 参数 | ICP-OES | ICP-MS |
|------|---------|--------|
| 检测原理 | 特征光学发射信号 | 离子的质荷比信号 |
| 检测范围 | ppm至wt.%级别 | ppt至ppm级别 |
| 检出限 | 亚ppb~100 ppb级 | 比ICP-OES低10~100倍 |
| 线性动态范围 | 10⁴~10⁸ | 10⁵~10⁸ |
| 测量不确定度 | 3%~5% | 约4% RSD |
| 同位素分析 | 不支持 | 支持 |
| 仪器成本 | 较低 | 较高，部分需超净间环境 |

数据来源：[[S12,S31,S19]]

## 干扰与校正

### 干扰分类

ICP-OES的干扰可分为五大类 [[S22,S17]]：

1. **基体效应**：共存组分改变给定浓度待测元素的谱线强度，存在抑制或增强两种效应
2. **光谱干扰**：待测元素谱线与其他元素谱线重叠导致的强度偏差
3. **散射影响**：颗粒散射光造成的背景信号抬升
4. **化学干扰**：包含离解干扰、氧化物解离干扰、电离干扰
5. **物理干扰**：包含雾化干扰、液相干扰、溶质挥发干扰、气相干扰

### 校正手段

通过选择合适的待测元素分析谱线、基体匹配法、同步背景校正法，可消除钛基、铝基等压铸基体的谱线重叠干扰与基体效应。通过加入内标元素可校正样品溶液黏度、表面张力等差异导致的物理传输效应。采用高分辨率大面积衍射光栅可消除大部分光谱干扰 [[S33,S10,S32]]。

## 压铸合金成分分析应用

### 镁元素分析谱线选择

压铸场景下镁元素的推荐分析谱线适配规则 [[S6]]：

| 镁含量范围 | 推荐分析谱线 | 注意事项 |
|-----------|-------------|----------|
| 低含量（≤ 0.05%） | Mg 2776.69、Mg 2852.13 | — |
| 中高含量 | Mg 2779.83 | 当样品中Fe含量较高时，受Fe 2779.91谱线干扰，可改用Mg 2790.79谱线 |

### LA42（Mg-Li-Al系）合金检测

LA42（Mg-Li-Al系）压铸合金的ICP-OES成分检测具备工程可行性。可选用锂、铝的对应特征分析谱线搭配镁基体内标，采用基体匹配与同步背景校正法，有效消除高镁基体带来的光谱干扰与物理干扰，获得准确的Li、Al主量元素和杂质元素含量结果 [[S15,S33,S3]]。

### 典型应用案例

1. 真空压铸Cu-Ni-Si-Co-Zr合金制备研究中，采用Thermo Scientific ICAP 7200型ICP-OES对合金全组分进行测定，获得了各主量和微量元素的质量分数结果，为后续热处理工艺优化提供了可靠的成分依据 [[S16]]。

2. 高压力铸造Al-10Si系列压铸铝合金力学性能研究中，采用Optima 7300DV型ICP-OES测定不同组分配比的压铸铝合金实际化学成分，验证了配料设计值与实际成分的一致性 [[S30]]。

3. 高性能压铸镁合金开发研究中，采用ICP-OES对Mg-3.5Al-4.2La-0.3Mn等压铸镁合金的实际成分进行标定，为合金微观组织和力学性能调控提供了精确的成分数据支撑 [[S9]]。

## 相关标准

现行有效的ASTM标准中，涉及ICP-OES/I CP-AES测定金属化学成分的标准共两项 [[S26,S28]]：

| 标准编号 | 名称 | 适用材料 |
|----------|------|----------|
| ASTM E1277-14 | Standard Test Method for Analysis of Zinc-5% Aluminum-Mischmetal Alloys by ICP Emission Spectrometry | 锌铝混合稀土压铸合金 |
| ASTM E2371-13 | Standard Test Method for Analysis of Titanium and Titanium Alloys by Direct Current Plasma and Inductively Coupled Plasma Atomic Emission Spectrometry | 钛及钛合金 |

## 压铸车间检测方法对比

压铸车间三种常用成分检测方法的核心差异 [[S4,S7,S35]]：

| 对比项 | ICP-OES | 火花直读光谱（OES） | X射线荧光光谱（XRF） |
|--------|---------|---------------------|---------------------|
| 样品形态 | 需经酸消解制成液体溶液 | 块状固体金属，仅需打磨抛光 | 固体、粉末、液体、薄膜等多种形态 |
| 分析速度 | 顺序型约5元素/分钟，同时型不到1分钟可完成60元素 | 数秒完成多元素检测 | 分析速度快 |
| 破坏性 | 需消解样品 | 微破坏（表面烧灼） | 非破坏性分析 |
| 适用场景 | 未知样全元素多痕量杂质高精度仲裁检测 | 炉前快速成分分析的主流手段 | 来料复验、批次常量元素确认 |
| 炉前适用性 | 不适合直接炉前快速检测 | 适合 | 适合 |

选型参考：炉前熔炼过程的实时成分管控优先选用火花直读光谱；来料复验、批次常量元素确认可选用XRF；未知样全元素多痕量杂质高精度仲裁检测优先选用ICP-OES。搭配SSEA固体进样（激光烧灼）技术可部分实现ICP在压铸现场的直接检测需求 [[S4,S35]]。

## Sources
- S32: [TextNode216](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddd4b96c-8582-4031-8386-1cd05aa02ac4/resource) (`ddd4b96c-8582-4031-8386-1cd05aa02ac4`)
- S15: [6151653_ICP-OES](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73b5b4d3-d531-49dd-9687-1349b6ae45fd/resource) (`73b5b4d3-d531-49dd-9687-1349b6ae45fd`)
- S18: [TextNode215](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80bcc399-e456-44e1-a9cd-a52389657e26/resource) (`80bcc399-e456-44e1-a9cd-a52389657e26`)
- S29: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5a52824-8949-43a7-8880-6dd20fd91a10/resource) (`d5a52824-8949-43a7-8880-6dd20fd91a10`)
- S1: [9925179_电感耦合等离子体原子发射光谱法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08c46702-9fa4-4e68-826b-c7f8f482dbb5/resource) (`08c46702-9fa4-4e68-826b-c7f8f482dbb5`)
- S2: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fbc02c9-4565-4e4d-a350-1ca6349fb4ad/resource) (`1fbc02c9-4565-4e4d-a350-1ca6349fb4ad`)
- S27: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c253519c-0bb5-407d-9cff-a35ad8027822/resource) (`c253519c-0bb5-407d-9cff-a35ad8027822`)
- S24: [图 6.2.3：典型顺序（单色器）ICP-OES](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1f9057e-838d-4f95-8b71-7b3c97cc7771/resource) (`b1f9057e-838d-4f95-8b71-7b3c97cc7771`)
- S11: [ICP-OES 光谱仪的光路示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57114605-a555-4b1e-bb8f-191be98d632f/resource) (`57114605-a555-4b1e-bb8f-191be98d632f`)
- S37: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f20f2365-23f0-4e98-a555-3cfac2f5fbbd/resource) (`f20f2365-23f0-4e98-a555-3cfac2f5fbbd`)
- S34: [ICP-OES 仪器操作参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec0c390d-696c-45a1-99c9-2237cae399e4/resource) (`ec0c390d-696c-45a1-99c9-2237cae399e4`)
- S25: [ICP-OES 仪器运行参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bdff8171-82fd-4483-98b3-d059ff242505/resource) (`bdff8171-82fd-4483-98b3-d059ff242505`)
- S20: [冷硬铸铁轧辊防开裂与白口层控制技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a36ab26-ad36-434d-9c2b-ce5c36784fbd/resource) (`8a36ab26-ad36-434d-9c2b-ce5c36784fbd`)
- S21: [图 6.2.5：通过三种酸消解后 ICP-OES 测定痕量元素的流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97235c76-44ce-43a0-b1ea-41dd7d41eca1/resource) (`97235c76-44ce-43a0-b1ea-41dd7d41eca1`)
- S14: [图 6.2.4：通过 ICP-OES 测定矿物和矿石中金属含量的流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72831222-9400-41db-9173-8d1905912834/resource) (`72831222-9400-41db-9173-8d1905912834`)
- S23: [Figure 6.2.5: Determination of Trace Elements by Three Acids Digestion followed by ICP-OES](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae41979d-5e7d-46d8-841f-6b3e19ea2848/resource) (`ae41979d-5e7d-46d8-841f-6b3e19ea2848`)
- S8: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3f8983a4-8548-47ee-958e-ba467c852a2c/resource) (`3f8983a4-8548-47ee-958e-ba467c852a2c`)
- S19: [表 6.2.1：ICP-MS、ICP-OES、FAAS 与 GF-AAS 性能对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/861a79df-6682-4036-ad42-1b4547d76c66/resource) (`861a79df-6682-4036-ad42-1b4547d76c66`)
- S10: [铝及铝合金连续铸轧带坯生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/482847f6-98b9-4c32-95d3-2e7ee2b09b29/resource) (`482847f6-98b9-4c32-95d3-2e7ee2b09b29`)
- S31: [ICP-OES 与 ICP-MS 参数对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcb3702d-4d32-40b8-91ca-6b23ee1f0b80/resource) (`dcb3702d-4d32-40b8-91ca-6b23ee1f0b80`)
- S12: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58747f15-2451-4941-9762-f138254b2801/resource) (`58747f15-2451-4941-9762-f138254b2801`)
- S22: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5781d6c-f48d-45f6-b585-2405c5464ce9/resource) (`a5781d6c-f48d-45f6-b585-2405c5464ce9`)
- S17: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7559af31-3bf5-4281-91ce-6b5bf2951cd4/resource) (`7559af31-3bf5-4281-91ce-6b5bf2951cd4`)
- S33: [有色金属熔炼入门与精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6332f73-071e-44a8-975c-e62cf1797ac8/resource) (`e6332f73-071e-44a8-975c-e62cf1797ac8`)
- S6: [铜镍铝银及其合金的光谱分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/341e3b2a-d865-41c5-9a9a-011c2386f720/resource) (`341e3b2a-d865-41c5-9a9a-011c2386f720`)
- S3: [表 10 某些元素共振谱线的波长](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26ba8326-57c6-4ed9-8103-66c7efbfac60/resource) (`26ba8326-57c6-4ed9-8103-66c7efbfac60`)
- S16: [热处理工艺对真空压铸Cu-Ni-Si-Co-Zr合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73d2b4b9-8e55-43f9-a6c8-74d7b6e6382a/resource) (`73d2b4b9-8e55-43f9-a6c8-74d7b6e6382a`)
- S30: [effect of chemical compositions on tensile behaviors of high pressure di__7b422b5dd4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5d8cec8-9209-4191-92fc-8356761175d1/resource) (`d5d8cec8-9209-4191-92fc-8356761175d1`)
- S9: [developing a die casting magnesium alloy with excellent mechanical perfo__81e986a15a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/478dc1ef-433c-44f9-935f-397343731e45/resource) (`478dc1ef-433c-44f9-935f-397343731e45`)
- S26: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfebb027-bfb0-483d-bcfb-ed0d97cfc61b/resource) (`bfebb027-bfb0-483d-bcfb-ed0d97cfc61b`)
- S28: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/caa0fb24-15a4-4db3-9e5a-f4a7b0b58834/resource) (`caa0fb24-15a4-4db3-9e5a-f4a7b0b58834`)
- S4: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30f634b0-8805-4ca6-a9db-dbfd1a359a80/resource) (`30f634b0-8805-4ca6-a9db-dbfd1a359a80`)
- S7: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35f488f6-ae93-4b51-aef6-93ad6efa6553/resource) (`35f488f6-ae93-4b51-aef6-93ad6efa6553`)
- S35: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1408307-4437-42a6-bb1e-f87932c83369/resource) (`f1408307-4437-42a6-bb1e-f87932c83369`)