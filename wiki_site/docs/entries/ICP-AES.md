---
version: "v1"
generated_at: "2026-06-18T06:38:45+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 29
  source_quality_score: 0.88
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

ICP-AES 的标准中文译名为**电感耦合等离子体原子发射光谱法**，属于以电感耦合等离子体为激发光源的原子发射光谱分析技术[[S5,S25]]。广义的原子发射光谱涵盖原子产生的全波段辐射形式，而 ICP-OES 特指仅在紫外-可见-红外光学波段进行测量的相关技术，属于 AES 的子集。由于当前商用 ICP-AES 设备全部仅采集光学波段信号，行业内 ICP-AES 和 ICP-OES 是完全可通用的互换术语，没有实际应用层面的区别[[S17,S28,S3]]。

电感耦合等离子体发射光谱仪是基于高温氩等离子体作为激发光源，通过测定自由原子和离子的发射光强度实现元素定性定量的分析仪器，工作在常压条件下，可同时测定七十多种金属元素及部分非金属元素[[S28,S15]]。

## 技术原理

经过酸消解后的样品水溶液通过雾化器转化为气溶胶，被送入 8000~10000 ℃ 的电感耦合氩等离子体高温区域，完成去溶剂、汽化、原子化、离子化步骤，待分析元素被激发至高能级。当处于高能级的原子或离子跃迁返回基态或低能级时，会发射出对应元素特征波长的光学辐射，该特征辐射的强度与样品中该元素的浓度成正比，经过校准后即可实现定量分析[[S17,S3]]。

## 设备组成与分类

### 核心部件

**等离子体炬**：核心结构包含水冷铜感应线圈、三层石英炬管、用于防止电弧生成的玻璃法兰 Bonnet。其中感应线圈通入射频电源后会产生交变振荡磁场，依托该磁场可在常压下维持稳定的高温氩等离子体作为激发光源[[S28]]。

**分光系统**：由入射狭缝、高分辨率色散光栅组成。部分型号采用 374 线/毫米的中阶梯光栅将不同波长的复合特征光进行二维色散，形成分离的 echellogram（二维光谱图案），实现不同元素特征波长的精准分离[[S28,S1]]。

**检测器**：作用是将接收到的光辐射能量转换为与辐射强度成正比的电信号。传统型号采用光电倍增管作为检测元件，新型全谱直读型号采用 CCD 面阵半导体像素芯片，单块芯片可集成数百个微米级像素，可同时采集上百条不同波长的特征谱线，大幅缩小仪器体积并提升检测效率[[S28,S32]]。

### 常见类型

| 类型 | 结构特征 | 分析特点 |
|------|----------|----------|
| 顺序扫描型 | 单只单色器+单通道移动检测器 | 逐波长依次扫描采集不同元素特征谱线，结构成本较低，多元素分析速度较慢[[S17,S28]] |
| 全谱直读型 | 二维中阶梯光栅+CCD 面阵检测器 | 同时一次性捕获全部所需元素特征光谱，无需机械移动扫描，多元素分析速度快，是当前主流商用形态[[S2,S30,S8]] |

![典型顺序（单色器）ICP-OES 整机组成及工作流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1f9057e-838d-4f95-8b71-7b3c97cc7771/resource)

上图展示了从雾化器、喷雾室、高频等离子体发生装置到检测部分的全路径，可直观说明顺序扫描型设备的整机组成[[S21]]。

![ICP-OES 光谱仪光路示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57114605-a555-4b1e-bb8f-191be98d632f/resource)

该图标注了 ICP 光源、入口狭缝、色散光栅、出口狭缝、检测器的完整光路走向，用于说明特征光谱的色散分离过程[[S9]]。

## 关键参数与性能

### 常规运行参数

| 参数 | 典型值/范围 |
|------|-------------|
| 射频功率 | 1.2 kW |
| 冷却气（等离子气）Ar 流量 | 15 L/min |
| 辅助气 Ar 流量 | 1.5 L/min |
| 雾化器（载气）Ar 流量 | 0.5~1.0 L/min |

[[S22]]

### 分析性能

| 性能指标 | 典型范围 |
|----------|----------|
| 可测元素数 | 70 余种金属元素及部分非金属元素 |
| 检出限 | 亚 ppb 至 100 ppb 量级 |
| 线性动态范围 | 10⁴ 至 10⁸ |
| 常规可分析含量区间 | 50 ppm ~ 50% 质量分数 |
| 最高耐受总溶解固体 | 可达 30%（部分高性能径向观测型） |

[[S15,S27,S7]]

## 在压铸中的角色与应用场景

ICP-AES 已作为主流定量分析设备在有色冶金行业广泛使用，可适配压铸全流程铝、锌、镁等压铸合金的不同检测环节需求[[S24,S17]]。

1. **原材料进厂成分检验**：将金属试样经硝酸、盐酸等酸体系消解为澄清溶液后，可同时测定全部主量和微量杂质元素[[S12]]。
2. **熔炼过程成分控制**：可用于熔炼过程中熔体取样制成的合金碎屑的成分快速分析，指导熔体成分调整，保障后续压铸批次合金成分合规[[S20]]。
3. **最终产品元素合规性验证**：精度可达 0.5%~3% 相对误差，满足压铸成品检测的精度要求[[S27]]。

![ICP-OES/ICP-AES 样品分析标准工作流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72831222-9400-41db-9173-8d1905912834/resource)

该图展示 0.5 g 样品经硝酸+盐酸消解、90~100 ℃ 水浴加热 3.5 小时、离心获得澄清溶液、上机测试、质量控制校验的全流程，不合格结果可触发重测，合格结果生成实验室报告[[S14]]。

## 与相关技术比较

| 比较维度 | ICP-AES/OES | Spark OES | ICP-MS |
|----------|-------------|-----------|--------|
| 样品前处理 | 需酸消解为澄清溶液 | 仅需将固体待测面打磨平整，无需消解 | 需消解为总溶解固体<0.4% 的澄清溶液，前处理难度最高 |
| 单样分析速度 | 4 分钟内完成 5~30 种元素 | 数十秒完成全元素分析 | 2~6 种元素/分钟 |
| 可测元素范围 | Li 到 U，除大气组分及稀有气体外 | 以金属元素为主，适配常规合金元素 | 除 S、大气组分及稀有气体外，覆盖 Li 到 U 全部元素 |
| 检出限 | 亚 ppb~100 ppb | 数十 ppm 量级 | 较 ICP-AES 低 10~100 倍，最优 |
| 购置及运行成本 | 中等偏高 | 最低 | 最高，需配套洁净实验室 |
| 适用场景 | 合金主量元素精准定量、合金成分身份识别、常规杂质检测 | 炉前快速无损筛查、大批量固体样品快速检测 | 超痕量有害杂质超高灵敏度检测、同位素分析 |

[[S27,S29,S13,S10]]

## 局限性与注意事项

ICP-AES 应用于压铸铝/锌/镁高基体合金检测时存在以下主要局限：

| 干扰类型 | 说明 | 消除方案 |
|----------|------|----------|
| 基体效应（物理干扰） | 压铸合金高基体会改变溶液的雾化效率和进样特性，导致检测强度产生非目标元素相关的偏移[[S16,S30]] | 基体匹配标准溶液、同步背景校正 |
| 谱线重叠干扰（光谱干扰） | 不同压铸合金中共存元素的发射谱线可能部分重叠在待测元素的分析线区间[[S26,S6]] | 选择合适分析谱线、元素间校正因子 |
| 样品前处理 | 铝、镁基压铸合金专属前处理可采用 HF-HNO₃-HCl 混酸体系的微波消解工艺：5 分钟升温至 130 ℃ 保温 3 min，再 5 分钟升温至 200 ℃ 保温 10 min 即可完全消解[[S30]] | — |

## 相关标准与方法

| 标准编号 | 标准名称 | 说明 |
|----------|----------|------|
| ISO 17025:2017 | 检测和校准实验室能力的通用要求 | 金属分析实验室开展 ICP-AES 检测的通用资质基础标准[[S4]] |
| ASTM E2857-11 | 化学和光谱分析实验室的分析方法验证通用导则 | 方法验证指导[[S23]] |
| ASTM E1277-14 | 锌-5% 铝-稀土合金的 ICP 发射光谱分析方法 | 压铸锌合金相关专用方法[[S23]] |
| GB/T 1467-1978 | 冶金产品化学分析方法标准的总则及一般规定 | 覆盖轻金属合金化学分析通用技术要求[[S18]] |
| GB/T 4470-1998 | 火焰发射、原子吸收和原子荧光光谱分析法术语 | 涵盖 ICP-AES 相关基础术语定义[[S18]] |

## Sources
- S5: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2f958c6b-4d36-4225-a5a4-c8d0d75d796e/resource) (`2f958c6b-4d36-4225-a5a4-c8d0d75d796e`)
- S25: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5a52824-8949-43a7-8880-6dd20fd91a10/resource) (`d5a52824-8949-43a7-8880-6dd20fd91a10`)
- S17: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80bcc399-e456-44e1-a9cd-a52389657e26/resource) (`80bcc399-e456-44e1-a9cd-a52389657e26`)
- S28: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddd4b96c-8582-4031-8386-1cd05aa02ac4/resource) (`ddd4b96c-8582-4031-8386-1cd05aa02ac4`)
- S3: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fbc02c9-4565-4e4d-a350-1ca6349fb4ad/resource) (`1fbc02c9-4565-4e4d-a350-1ca6349fb4ad`)
- S15: [6151653_ICP-OES](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73b5b4d3-d531-49dd-9687-1349b6ae45fd/resource) (`73b5b4d3-d531-49dd-9687-1349b6ae45fd`)
- S1: [简明铝合金手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08621e86-5648-409a-a26c-0164f83be861/resource) (`08621e86-5648-409a-a26c-0164f83be861`)
- S32: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0c1a9e1-d5a8-4660-ab7e-0b7bdfe02688/resource) (`f0c1a9e1-d5a8-4660-ab7e-0b7bdfe02688`)
- S2: [9925179_电感耦合等离子体原子发射光谱法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08c46702-9fa4-4e68-826b-c7f8f482dbb5/resource) (`08c46702-9fa4-4e68-826b-c7f8f482dbb5`)
- S30: [有色金属熔炼入门与精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6332f73-071e-44a8-975c-e62cf1797ac8/resource) (`e6332f73-071e-44a8-975c-e62cf1797ac8`)
- S8: [铸造方法对Al-Li-Cu-Mg-Sc-Zr合金组织和性能影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a8e1dac-f54f-412d-821b-654b7b36c7ae/resource) (`4a8e1dac-f54f-412d-821b-654b7b36c7ae`)
- S21: [图 6.2.3：典型顺序（单色器）ICP-OES](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1f9057e-838d-4f95-8b71-7b3c97cc7771/resource) (`b1f9057e-838d-4f95-8b71-7b3c97cc7771`)
- S9: [ICP-OES 光谱仪的光路示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57114605-a555-4b1e-bb8f-191be98d632f/resource) (`57114605-a555-4b1e-bb8f-191be98d632f`)
- S22: [ICP-OES 仪器运行参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bdff8171-82fd-4483-98b3-d059ff242505/resource) (`bdff8171-82fd-4483-98b3-d059ff242505`)
- S27: [ICP-OES 与 ICP-MS 参数对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcb3702d-4d32-40b8-91ca-6b23ee1f0b80/resource) (`dcb3702d-4d32-40b8-91ca-6b23ee1f0b80`)
- S7: [铝及铝合金连续铸轧带坯生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/482847f6-98b9-4c32-95d3-2e7ee2b09b29/resource) (`482847f6-98b9-4c32-95d3-2e7ee2b09b29`)
- S24: [铜及铜合金熔炼与铸造技术问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb9af849-fe6f-4f66-b642-60365276d946/resource) (`cb9af849-fe6f-4f66-b642-60365276d946`)
- S12: [TextNode222](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/658eed98-0f4a-465d-8e04-06c6c9abf42e/resource) (`658eed98-0f4a-465d-8e04-06c6c9abf42e`)
- S20: [钛合金TC4真空自耗熔炼铸锭质量控制基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5b23fe1-85eb-44be-89f9-9a13d8df19d0/resource) (`a5b23fe1-85eb-44be-89f9-9a13d8df19d0`)
- S14: [图 6.2.4：通过 ICP-OES 测定矿物和矿石中金属含量的流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72831222-9400-41db-9173-8d1905912834/resource) (`72831222-9400-41db-9173-8d1905912834`)
- S29: [Table 6.2.3: Advantages and Limitations of various instrumental methods](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e395a7cc-bd99-433a-beb8-fbbd104609e8/resource) (`e395a7cc-bd99-433a-beb8-fbbd104609e8`)
- S13: [SPECTRO ARC/SPARK OES光谱分析设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69308a52-3d49-4a1a-acbc-5553276af48e/resource) (`69308a52-3d49-4a1a-acbc-5553276af48e`)
- S10: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58747f15-2451-4941-9762-f138254b2801/resource) (`58747f15-2451-4941-9762-f138254b2801`)
- S16: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7559af31-3bf5-4281-91ce-6b5bf2951cd4/resource) (`7559af31-3bf5-4281-91ce-6b5bf2951cd4`)
- S26: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d857c55f-1466-4293-844e-256345704dac/resource) (`d857c55f-1466-4293-844e-256345704dac`)
- S6: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/310011e3-86d7-4f28-9fa2-d45118e291e1/resource) (`310011e3-86d7-4f28-9fa2-d45118e291e1`)
- S4: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20ed4470-d365-4ea8-9ab2-e9601c642992/resource) (`20ed4470-d365-4ea8-9ab2-e9601c642992`)
- S23: [analytical testing methods in non ferrous extractive metallurgy__4a6443daa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bfebb027-bfb0-483d-bcfb-ed0d97cfc61b/resource) (`bfebb027-bfb0-483d-bcfb-ed0d97cfc61b`)
- S18: [有色金属工业标准汇编轻金属及其合金化学分析方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/902152e9-bffe-466f-a4fb-8d8a413cbdaa/resource) (`902152e9-bffe-466f-a4fb-8d8a413cbdaa`)