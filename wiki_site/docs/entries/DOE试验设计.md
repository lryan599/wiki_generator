---
version: "v1"
generated_at: "2026-06-18T13:25:55+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 39
  source_quality_score: 0.84
  freshness_score: 0.87
  evidence_coverage_score: 1.0
---

## 概述

试验设计（Design of Experiments，简称DOE）是以概率论和数理统计为理论基础，经济地、科学地安排试验的技术，其核心优势是用较少的试验次数、较短的试验周期和较低的试验成本，获得理想的试验结果和正确结论[[S13,S35]]。在压铸领域，DOE广泛应用于产品和工艺参数稳健性设计、工艺过程优化与铸件缺陷管控[[S13]]。

压铸行业传统基于经验的单因素试错优化模式效率低、对工艺人员经验依赖度高。DOE可结合CAE数值模拟技术快速识别压铸缩孔、气孔等缺陷的关键影响因子，快速定位不同工艺参数对铸件质量的影响权重，实现工艺参数协同优化，显著降低试制成本、缩短开发周期、提升铸件良品率[[S13,S15,S35]]。

DOE是一套系统的统计试验设计框架，通过正交试验等方式以最少的试验次数采集数据，借助统计分析识别压铸过程中影响铸件质量的关键因素及其交互作用，最终高效获取优化后的工艺参数，实现降低缺陷率、缩短研发周期、控制生产成本的目标[[S35,S12,S31]]。

![DOE正交试验标准实施流程图，展示从发现问题、确定影响因素、选定因子、生成正交表、开展试验、采集结果、数据分析、筛选最优方案直至完成闭环的全流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/000f30fe-e046-4ab6-9e35-ebe3a1fa3a5c/resource)

## 核心方法分类

压铸行业常用DOE子方法覆盖全因子试验设计、部分因子试验设计、正交试验设计、田口方法、响应面法五大类，适用于不同压铸场景下的工艺优化需求[[S3,S13,S15]]。

| 方法 | 核心特点 | 压铸典型应用场景 |
|------|----------|-----------------|
| 全因子试验设计 | 覆盖所有因子与所有水平的全部组合，获得完整交互作用信息 | 明确流道高度、氢含量等关键参数对铸件力学性能的影响规律[[S15]] |
| 部分因子试验设计 | 减少试验次数，快速筛选显著性因子 | 从支架结构、浇注温度、铸造压力、冷却参数等6个因子中筛选4个显著性因子，大幅降低仿真与试验工作量[[S13,S9]] |
| 正交试验设计 | 基于规范化正交表安排多因子多水平试验，试验次数少、分析简便 | 以L27(3⁷)正交表针对A380合金薄壁壳体同时优化速度、比压、增压时间等7个参数[[S20,S27]] |
| 田口方法 | 引入信噪比(S/N)评价指标，实现稳健性优化 | 在显著降低试验次数的前提下分析工艺参数对铸件缺陷的方差贡献，降低气孔率、冷金属缺陷率[[S39,S10,S15]] |
| 响应面法（RSM） | 基于二次多项式回归拟合工艺参数与质量目标的函数关系，支持Box-Behnken设计(BBD)、中心复合设计(CCD) | 精准预测并优化铝合金减震塔缩孔率、调控外壳收缩孔隙缺陷[[S18,S30,S45,S15]] |

部分因子试验设计可在减少总试验次数的前提下快速筛选出影响压铸缺陷的显著性因子。在铝合金发动机缸体缩孔缺陷优化场景中，可从支架结构、浇注温度、铸造压力、冷却管道换热系数等6个因子中快速筛选出4个显著性因子[[S13,S9]]。

正交试验设计基于规范化正交表安排多因子多水平试验，以L9(3³)等标准化正交表为典型代表，试验次数少、分析简便，可快速判断不同压铸工艺参数对铸件质量的影响权重[[S20,S27]]。

田口方法属于DOE体系下的稳健性优化方法，核心引入信噪比(S/N)评价指标，包含望大、望目、望小三类不同场景的信噪比计算规则。优化后可将高压压铸铝合金齿条壳体的气孔率、法兰铸件冷金属缺陷率等指标大幅降低[[S39,S10,S15]]。

响应面法可在正交试验筛选显著因子的基础上进一步在连续参数区间内寻找全局最优解，支持Box-Behnken设计(BBD)、中心复合设计(CCD)等典型方案[[S18,S30,S45]]。

## 典型试验因子与响应变量

### 常见可控因子

压铸DOE研究中常见的可控工艺因子包括[[S29,S13,S11,S43,S33]]：

- **温度参数**：熔体（浇注）温度、模具预热温度、冷却介质入口温度
- **速度参数**：快速/慢速压射速度、充型速度
- **压力参数**：增压/保压压力、压射比压
- **时间参数**：充型时间（注射时间）、保压时间、增压时间、冷却时间、整体成型周期
- **其他参数**：点冷管通水时间、模具冷却管道换热系数、铸件结构

### 常见响应变量

压铸DOE的典型响应变量及观测方式包括[[S19,S23,S14,S6]]：

| 响应变量类别 | 具体指标 | 典型获取方式 |
|------------|---------|-------------|
| 内部缺陷 | 缩孔/缩松/卷气率 | 数值模拟统计缺陷体积、工业CT扫描、机加工后人工评级、阿基米德密度换算 |
| 力学性能 | 抗拉强度、硬度 | 力学试验 |
| 尺寸与形貌 | 翘曲变形量、尺寸精度 | 三坐标测量 |
| 表面质量 | 表面粗糙度、表面品质 | 目视评级、粗糙度仪 |
| 显微组织 | 二次枝晶臂间距(SDAS) | 金相观测 |
| 物理性能 | 铸件密度 | 阿基米德法、工业天平 |

## 实施流程与步骤

正交试验DOE完整工作流程包含9个核心步骤[[S1]]：

![DOE正交试验标准流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/000f30fe-e046-4ab6-9e35-ebe3a1fa3a5c/resource)

### 问题定义与目标确定

针对现场存在的特定质量缺陷（如缸体局部缩孔）明确优化量化目标，例如将铸件报废率降低至0.5%以下，同步筛选可调整的可控变量范围、确认待优化的核心响应指标[[S13]]。

### 因子与水平选择

根据现有工艺经验从全量可控变量中筛选核心影响因子，排除影响极弱的变量，针对每个因子设置3个及以上水平，覆盖现场工艺允许的全部可行区间，同时可纳入预设的因子交互作用项作为考察对象[[S11,S2]]。

### 试验方案设计与实施

压铸领域DOE常用正交阵列（L9、L27等）、全因子设计、中心复合设计（CCD）安排试验组，每组试验设置3次以上重复以降低随机误差。可结合MAGMA、ProCAST等铸造仿真软件虚拟执行试验大幅降低试模成本[[S29,S6,S19,S37]]。

以下为典型的5因子4水平压铸改进DOE试验参数矩阵表示例[[S40]]：

| 试验号 | 型腔表面温度 | 熔体温度 | 熔体充型时间 | 保压压力 | 保压时间 |
|--------|------------|---------|------------|---------|---------|
| 1 | 水平1 | 水平1 | 水平1 | 水平1 | 水平1 |
| 2 | 水平1 | 水平2 | 水平2 | 水平2 | 水平2 |
| ... | ... | ... | ... | ... | ... |
| 16 | 水平4 | 水平3 | 水平2 | 水平1 | 水平4 |

### 数据分析方法

配套数据分析方法包括三类[[S4,S29,S32,S24]]：

1. **极差分析**：计算不同因子各水平下响应/信噪比均值的差值，差值越大说明因子影响程度越高。

2. **方差分析（ANOVA）**：通过计算各因子的偏差平方和、自由度、均方、F值，与对应显著性水平下的F临界值对比，定量得到各因子的贡献占比、判断因子影响是否统计显著。通常取α=0.05作为显著性判定阈值。

3. **信噪比（S/N）分析**：针对不同优化目标选择对应公式——优化值越小越好用望小公式、优化值越大越好用望大公式、优化值趋近固定目标值用望目公式，用于降低不可控噪声因素对响应的干扰，提升工艺鲁棒性。

![DOE试验分析的标准化效应Pareto图，响应为评估区域缩孔体积，α=0.10，可直观识别影响缩孔体积的显著因子排序](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c47c159-a5aa-49f2-801b-184affa0c7e9/resource)

### 最优组合确定与验证试验

结合主效应图、响应面结果、响应优化器输出筛选出各因子的最优水平组合，该组合无需包含在原有试验组中。随后开展不少于1批次的小批量试生产验证，确认优化后响应指标达到预设目标[[S24,S13]]。

![DOE流程中输出的响应优化器结果图，直观展示各因子取值与复合合意性、缩孔体积响应的关联曲线，标注推荐的最优参数组合数值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7529f814-c576-4431-a804-b015d739ed9c/resource)

## 压铸领域应用案例

### 发动机缸体缩孔缺陷优化

基于铸造过程数值模拟技术，采用DOE方法分析某铝合金1.5T发动机缸体发电机支架的缩孔缺陷关键影响因素。通过部分因子试验方法从支架结构、浇注温度、铸造压力、浇口下方冷却管道HTC、点冷管1通水时间、点冷管2通水时间6个因子中，确定A（支架结构）、B（浇注温度）、C（铸造压力）、E（点冷管1通水时间）为显著影响因子，产品报废率得到有效控制[[S13,S9]]。

### 铝合金压铸件密度优化

针对AlSi9Cu13铝合金压铸的DOE应用研究，通过对活塞运动速度（第一阶段0.02–0.34 m/s、第二阶段1.2–3.8 m/s）、金属液温度（610–730℃）、填充时间（40–130 ms）、液压压力（120–280 bar）等参数开展基于L27正交表的试验，方差分析表明液压压力对铸件密度的贡献占比达47.749%，可显著提升铸件密度，有效控制内部孔隙类缺陷[[S16,S24]]。

### 冷室压铸工艺参数建模

采用DOE联合Minitab工具针对铝合金冷室压铸过程进行优化，以孔隙率、铸件硬度、表面粗糙度为目标输出建立二阶响应面模型，通过31组中心复合设计（CCD）试验加12组随机验证试验，完成压铸工艺-质量关系的精准预测，无需重复物理试模即可快速得到不同参数组合下的铸件质量表现[[S19]]。

### 锌合金压铸件表面缺陷改善

面向高外观要求锌合金压铸件的DOE优化研究，选定注射速度、冷却介质温度、润滑剂喷涂时间三个参数进行试验验证，成功将型腔填充末期温度控制在合理区间，实现表面冷流缺陷的大幅降低[[S46]]。

### 六西格玛框架下的DOE应用

结合DOE的压铸机缸盖铸件质量改进项目，在六西格玛DMAIC框架下对浇注温度、浇注时间开展两因子两水平DOE试验，将铸件废品率从9.3%降低至1.92%，年直接经济效益超过33万元[[S8]]。

![铝合金减震塔DOE优化后的缺陷分布热力图，展示设置定点水冷后铸件孔隙分布，总孔隙体积为1.015cc，相较于优化前缺陷显著降低](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e03b5bbe-831c-476c-a463-79f1a6fcc137/resource)

## 优势与局限性

### 相比单因子实验（OFAT）的优势

DOE相比传统单因子试验（OFAT/One Factor At A Time）的明确优势包括：无需逐一遍历所有参数组合即可识别多因子交互作用对压铸质量的影响，大幅减少所需物理试验次数，降低试模阶段的材料与人工消耗，所得优化工艺参数的鲁棒性更强，可覆盖更宽的稳定工艺窗口[[S35,S38]]。

### 实际生产中的限制因素

DOE在实际压铸量产场景下存在明确应用限制[[S7,S17]]：

- **试验成本约束**：压铸试模的金属材料、模具损耗、机台占用成本较高，大批量的物理试验直接推高研发投入。
- **生产节拍约束**：高节拍量产线常规班次仅能安排有限数量的参数调整试验，长时间中断正常生产开展DOE试验会严重影响产能交付。

## 相关概念与工具

### 与田口方法的关系

田口方法是DOE体系下面向稳健性优化的分支技术，属于质量工程的核心工具。在压铸场景中以信噪比作为评价指标，可高效筛选出对噪声扰动（如模具温度波动、合金成分小幅偏移）不敏感的最优参数组合，实现量产过程中铸件质量的稳定输出[[S26,S42]]。

### 与六西格玛的关系

六西格玛DMAIC改进流程将DOE作为核心分析工具，在压铸质量改进的分析阶段用于量化识别关键影响因子的显著性，建立因子与缺陷率的映射关系，为后续的参数固化和管控提供数据支撑[[S34,S25,S12]]。

### 常用软件工具

| 软件工具 | 典型特性 | 压铸适用场景 |
|---------|---------|-------------|
| Minitab | 支持全因子、部分因子、田口设计、中心复合设计等几乎所有主流DOE设计类型，操作门槛低 | 压铸行业应用最广泛，适合现场工艺工程师使用[[S8,S19]] |
| JMP | 自带交互式可视化分析能力，支持高阶响应面优化和多目标协同寻优 | 适合复杂压铸结构件的多维度工艺优化项目，可权衡孔隙率、表面质量、模具热疲劳寿命等多个冲突目标[[S23]] |
| Design-Expert | 支持自定义非标准试验设计方案，精准拟合非线性响应关系 | 适用基于响应面法的高精度非线性建模，指导高精度密封类压铸件批量生产[[S23,S43]] |

## Sources
- S13: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/33fdbc27-e654-48df-a3bb-bd9a4f043c41/resource) (`33fdbc27-e654-48df-a3bb-bd9a4f043c41`)
- S35: [不锈钢泵体的熔模铸造工艺设计及参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dec94d90-91e0-4bb8-bac8-bf2d87609ebb/resource) (`dec94d90-91e0-4bb8-bac8-bf2d87609ebb`)
- S15: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/529ab0e8-61fa-49b9-b619-70e29fd386e3/resource) (`529ab0e8-61fa-49b9-b619-70e29fd386e3`)
- S12: [die cast engineering a hydraulic thermal and mechanical process__e5dfda1a8e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30037ae5-1b6a-4e99-97b5-6b5d063594e3/resource) (`30037ae5-1b6a-4e99-97b5-6b5d063594e3`)
- S31: [职业标准导向下的《压铸工艺及模具设计》课程建设](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa322169-d135-46ec-a5d9-d11fdc499228/resource) (`aa322169-d135-46ec-a5d9-d11fdc499228`)
- S3: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12329c9c-3261-4c58-a1b4-f4faafee1036/resource) (`12329c9c-3261-4c58-a1b4-f4faafee1036`)
- S9: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26d6cda7-b096-455a-94a1-1fd83c1ca886/resource) (`26d6cda7-b096-455a-94a1-1fd83c1ca886`)
- S20: [A380合金薄壁壳体压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/70274273-cde1-442e-a779-da9132cc60e2/resource) (`70274273-cde1-442e-a779-da9132cc60e2`)
- S27: [表4.9 L9(3³)正交试验表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8aec532b-3c72-4c96-b0ab-7be8513e2d7d/resource) (`8aec532b-3c72-4c96-b0ab-7be8513e2d7d`)
- S39: [基于CAE的某生化仪内支架注塑成型过程模拟及工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e58a8b46-94fe-49be-985a-995182514a1f/resource) (`e58a8b46-94fe-49be-985a-995182514a1f`)
- S10: [基于CAE的某生化仪内支架注塑成型过程模拟及工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/29a3b0d3-ad62-4a7d-930b-4e6a6b83ae9f/resource) (`29a3b0d3-ad62-4a7d-930b-4e6a6b83ae9f`)
- S18: [基于CAE的某生化仪内支架注塑成型过程模拟及工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68ee9679-3783-4983-9730-4072e8d0ff09/resource) (`68ee9679-3783-4983-9730-4072e8d0ff09`)
- S30: [基于Moldex3D与Abaqus_FE-safe的注塑模具结构及疲劳寿命分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6481d9c-db5c-400d-b239-25ae5b455a93/resource) (`a6481d9c-db5c-400d-b239-25ae5b455a93`)
- S45: [面向薄壁结构件的压铸模温预测及调控技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd5332bb-3196-4308-b0fc-c8741c08f17f/resource) (`fd5332bb-3196-4308-b0fc-c8741c08f17f`)
- S29: [镁合金汽车抬头显示支架压铸工艺模拟与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90957368-6b33-460e-858a-f0cababca921/resource) (`90957368-6b33-460e-858a-f0cababca921`)
- S11: [die casting process optimization using taguchi methods__eca7652172](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/29f38cea-127b-4999-9a88-7ec6134087d4/resource) (`29f38cea-127b-4999-9a88-7ec6134087d4`)
- S43: [aip conference proceedings aip international conference on modeling opti__9dbb7b9ee0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efc07a83-2d43-43f2-b842-bbd550fdeb2d/resource) (`efc07a83-2d43-43f2-b842-bbd550fdeb2d`)
- S33: [基于Moldflow的超薄壁外壳翘曲变形分析及工艺参数优选](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c888b505-2da4-4096-8d40-ec41cb39b02b/resource) (`c888b505-2da4-4096-8d40-ec41cb39b02b`)
- S19: [aip conference proceedings aip international conference on modeling opti__9dbb7b9ee0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6967b44c-57c8-4b2c-8958-41da01f91c35/resource) (`6967b44c-57c8-4b2c-8958-41da01f91c35`)
- S23: [a multiple objective decisionmaking approach for assessing simultaneous__b40edcb5cb](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c9235f6-847b-419a-8aa1-800e2ce24eb4/resource) (`7c9235f6-847b-419a-8aa1-800e2ce24eb4`)
- S14: [基于正交试验与信噪比分析的铝合金钳体支架压铸工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39e66fdc-ab64-4c49-9012-06d83f476e8e/resource) (`39e66fdc-ab64-4c49-9012-06d83f476e8e`)
- S6: [汽车机油泵体压铸工艺数值模拟与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/211f26c5-f889-45eb-8b83-2fd022d344e1/resource) (`211f26c5-f889-45eb-8b83-2fd022d344e1`)
- S1: [图1.2 DOE正交试验流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/000f30fe-e046-4ab6-9e35-ebe3a1fa3a5c/resource) (`000f30fe-e046-4ab6-9e35-ebe3a1fa3a5c`)
- S2: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e980880-f708-4825-9d19-844afebb972a/resource) (`0e980880-f708-4825-9d19-844afebb972a`)
- S37: [Table 1: Three-level orthogonal array design for die casting process parameters and interactions](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1d10ebc-f5ad-4189-86d6-5fc3a35b28e7/resource) (`e1d10ebc-f5ad-4189-86d6-5fc3a35b28e7`)
- S40: [表4.2 改进DOE试验表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9a2e083-a768-488b-8a54-e7101498c1ae/resource) (`e9a2e083-a768-488b-8a54-e7101498c1ae`)
- S4: [汽车发动机底护板复合材料塑件的成型工艺优化及多尺度联合仿真](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19518b7a-e9cd-4b9f-9e6a-facf3baf2443/resource) (`19518b7a-e9cd-4b9f-9e6a-facf3baf2443`)
- S32: [a study of porosity formation in pressure die casting using the taguchi__4ac320727f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b39a2f1e-51df-4e3e-bdf9-1f2235c7ded2/resource) (`b39a2f1e-51df-4e3e-bdf9-1f2235c7ded2`)
- S24: [die casting process optimization using taguchi methods__eca7652172](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7cb4672a-3d72-4904-b3ad-203d23c02f20/resource) (`7cb4672a-3d72-4904-b3ad-203d23c02f20`)
- S16: [die casting process optimization using taguchi methods__eca7652172](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c62dcfe-e025-41bf-99e6-8025833afecc/resource) (`5c62dcfe-e025-41bf-99e6-8025833afecc`)
- S46: [cold flow defects in zinc die casting prevention criteria using simulati__ac8154fe3a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fee911d7-2d5b-436b-b2f9-5a157d081f64/resource) (`fee911d7-2d5b-436b-b2f9-5a157d081f64`)
- S8: [基于DMAIC模型的缸盖铸件废品率改进研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25119a84-be4a-40cd-855b-2eea87bb02fa/resource) (`25119a84-be4a-40cd-855b-2eea87bb02fa`)
- S38: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1facb7e-52d3-4aba-9939-3314632319f9/resource) (`e1facb7e-52d3-4aba-9939-3314632319f9`)
- S7: [基于集成学习与改进灰狼算法的铝合金压铸件仿真与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/241a44b0-a9a2-4d74-a456-4aef917ba727/resource) (`241a44b0-a9a2-4d74-a456-4aef917ba727`)
- S17: [automotive alloys 1999__dbd41f2733](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5d116df5-e219-45c1-b920-af42b028a880/resource) (`5d116df5-e219-45c1-b920-af42b028a880`)
- S26: [6511383_田口方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80f4d2b2-8f8a-4055-a7c3-c0b44f73f6fb/resource) (`80f4d2b2-8f8a-4055-a7c3-c0b44f73f6fb`)
- S42: [铸铝电机转子压铸模具设计与工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed181ae5-e843-4877-9c95-ed2535cbaa37/resource) (`ed181ae5-e843-4877-9c95-ed2535cbaa37`)
- S34: [六西格玛质量分析工具在H3NG缸盖铸造工艺优化中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d179e414-acde-4485-996d-423666db9038/resource) (`d179e414-acde-4485-996d-423666db9038`)
- S25: [基于DMAIC模型的缸盖铸件废品率改进研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e8d43d6-69a6-4dd0-a897-865238ce7144/resource) (`7e8d43d6-69a6-4dd0-a897-865238ce7144`)