---
version: "v1"
generated_at: "2026-06-18T10:18:19+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 35
  source_quality_score: 0.86
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述与定义

**EPS**，全称可发性聚苯乙烯（Expanded Polystyrene），是消失模铸造（Lost Foam Casting, LFC）中最先应用、也是目前最通用的泡沫模样材料 [[S12,S21]]。在专业铸造文献中，正式规范名称为“EPS模样”或“聚苯乙烯泡沫模样”，行业通用的日常称呼为“白模”；“EPS模型”属于口语化非专业表述，正式使用场合建议避免 [[S24,S33]]。

EPS是一种高分子碳氢化合物，分子式为 (C₆H₅·C₂H₃)ₙ，碳元素质量占比约92%，氢元素约8%，仅含极少量发泡过程带入的氧、氮杂质 [[S12,S34]]。未发泡的原生聚苯乙烯密度为1.05 g/cm³ [[S30]]。

## 成分与结构

### 化学组成

EPS由苯乙烯单体经悬浮聚合得到聚苯乙烯基体，生产过程中加入低沸点饱和烃作为发泡剂，最常用的是戊烷（沸点36.7°C）或其异构体异戊烷（沸点27.9°C），发泡剂在成品未发泡珠粒中的质量占比为4%~5% [[S6]]。部分配方会添加少量辅助改性添加剂以改善泡孔结构均匀性 [[S6]]。

### 微观结构

经发泡后的EPS内部呈蜂窝状封闭泡孔结构，单位体积内约含10000个互不连通的独立泡孔，泡孔平均直径约50 μm，泡孔壁厚度仅为0.3~1.0 μm [[S6,S29]]。未发泡原始EPS珠粒密度为640 kg/m³，常规消失模铸造用EPS经预发泡后表观密度仅为15~25 kg/m³，发泡后固态聚苯乙烯的实际体积占比不足泡沫总体积的2% [[S34,S39]]。

## 核心性能参数

消失模铸造用典型EPS材料的主要性能参数如下表所示 [[S20]]：

| 性能名称 | 性能值 |
|---|---|
| 密度/(kg/m³) | 16~19 |
| 抗压强度/MPa | 0.11~0.14 |
| 抗拉强度/MPa | 0.27~0.37 |
| 热变形温度/°C | 75 |
| 热导率/[W/(m·K)] | ≤0.041 |
| 吸水性/(kg/m³) | ≤1.0 |

通用场景下，消失模铸造用EPS白模密度通常控制在16~25 kg/m³，仅为钢铁铸件密度的1/250~1/350 [[S21]]。EPS的玻璃化转变（软化）温度约为80°C [[S30,S20]]。1000°C条件下，EPS的发气量为105 cm³/g，完全热解后非挥发固态残留物的质量占比仅为0.015%，在所有常规泡沫模样材料中发气量最低 [[S15,S21]]。

## 白模制造工艺

EPS白模的完整制备流程包含三个核心工序：预发泡→熟化→成形发泡 [[S12,S19]]。大批量生产时通过模具直接发泡成型，小批量时可先制备EPS板材再经数控加工拼接 [[S19,S10]]。

### 预发泡

预发泡分为真空预发和蒸汽预发两种主流工艺 [[S10,S36]]：

| 工艺类型 | 关键参数 | 说明 |
|---|---|---|
| 真空预发 | 负压度-60~-80 kPa；抽真空时间20~30 s | 可制备最低密度达16 kg/m³的极低密度珠粒；珠粒含水量低 |
| 蒸汽预发 | 蒸汽压力0.10~0.12 MPa；发泡温度85~90°C；发泡倍率40~60 | 珠粒含水率约10%，需额外干燥工序 |

### 熟化

熟化温度控制在20~25°C区间，熟化时长随预发珠粒密度降低、含水率升高而延长。熟化完成后泡孔内外压力达到平衡，残留发泡剂质量分数保持在3.5%以上，以保障后续成形发泡的膨胀性能 [[S36,S19]]。

### 成形发泡

向填充预发珠粒的密闭模腔通入饱和蒸汽，蒸汽压力通常控制在0.03~0.15 MPa区间，加热时长依模腔壁厚动态调整。珠粒完成二次膨胀并完全熔接为一体，随后水冷强制冷却至白模完全定型后脱模 [[S25]]。

## 热分解行为与产物

### 温度阶段特性

EPS在不同温度区间经历一系列相变与化学分解过程 [[S27,S26,S35]]：

| 温度区间 | 状态变化 |
|---|---|
| ~75°C | 开始进入玻璃态软化 |
| >100°C | 体积大幅收缩，进入高弹态 |
| ~164°C | 完全转变为无定形黏流态液态 |
| ~316°C | 起始解聚反应 |
| ~350°C | 开始大量分解 |
| ~420°C | 分解速率达到峰值 |
| >700°C | 进入完全深度裂解区域 |

![EPS受热后体积收缩的实物形态，展示70°C~150°C区间白模未完全裂解前的宏观物理收缩特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa04a3c7-e70b-4a4f-ad92-f5a0279a071f/resource)

### 分解产物组成

EPS热分解产物组成随温度变化呈现明显规律 [[S16,S37]]：

- **500°C以下**：苯乙烯单体为主要液相产物，同时生成苯、甲苯等低聚物；
- **温度升高**：低聚物进一步断链生成小分子气态产物；
- **750°C以上**：低分子气态产物占比显著提升；
- **1000°C时**：EPS完全裂解生成CH₄、C₂H₄、H₂等小分子气体和游离活性碳。

不同合金浇注温度下EPS热解产物占比差异显著 [[S37]]：

| 浇注场景 | 浇注温度 | 小分子气体体积分数 | 主要产物形态 |
|---|---|---|---|
| 铝合金 | ~750°C | 11.42% | 以液态EPS为主 |
| 铸铁 | ~1350°C | 32.79% | 液态与气态并存 |
| 铸钢 | ~1600°C | 38.57% | 几乎完全裂解为气态产物和残碳 |

## 与金属液的相互作用及缺陷机理

### 热解产物排出路径

EPS与高温金属液接触后，沿远离金属液前沿的方向依次划分出熔化区、分解区、燃烧区三个连续相变区域 [[S18]]。热解生成的液态、气态产物首先通过金属液与EPS之间的薄间隙向周围耐火涂层渗透，随后穿过涂层孔隙进入干砂型空隙，最终随排气通道排出铸型。无法及时排出的产物会在型腔内部累积形成上升背压 [[S23]]。

产物排出效率直接决定金属液充型前沿的稳定性：当涂层透气性与浇注负压度适配时，热解产物可顺利排出，金属液充型流动平稳；若排出受阻则型腔背压陡增，金属液流动速度大幅下降甚至断流 [[S37]]。

### 典型缺陷

热解产物滞留可导致三类典型铸件缺陷 [[S28,S32]]：

1. **气孔**：未及时排出的气态产物滞留在金属液-涂层界面，被包裹进铸件内部形成气孔；
2. **皱皮**：大量液态EPS低聚物无法正常排出，在铸件表面富集沉积形成亮碳褶皱层，多分布在充型末端、铸件顶部；
3. **表面增碳**：铸钢等高熔点合金浇注时，游离活性碳向钢液内部扩散形成表面增碳，增碳量可达0.1%~0.3%。

## 与其他泡沫材料的对比

EPS与EPMMA（可发性聚甲基丙烯酸甲酯）、STMMA（苯乙烯-甲基丙烯酸甲酯共聚树脂）是消失模铸造三种主要模样材料。三者核心性能差异如下 [[S22,S11,S33]]：

| 对比项目 | EPS | STMMA | EPMMA |
|---|---|---|---|
| 碳质量分数 | 92% | 69.6% | 60% |
| 碳渣生成量 | 高 | 中 | 低 |
| 单位质量发气量 | 低（基准） | 约为EPS的1.9倍 | 显著高于EPS |
| 发气速率 | 低 | 介于两者之间 | 高，易反喷 |
| 材料成本 | 最低（EPMMA约60%） | 中 | 高 |
| 充型速度适配 | 5~20 cm/s | <5 cm/s | 约2.5 cm/s |

EPS的主要应用局限在于 [[S3,S11]]：不适用于厚大断面铸件和低碳钢件生产（增碳量可达0.1%~0.3%）；球墨铸铁件中EPS分解的游离碳无法被饱和碳铁液吸收，易形成亮碳片状夹渣；铝合金铸件易出现表面皱皮缺陷。

## 应用领域

EPS白模可稳定适配灰铁、球铁、普通碳钢、铝合金、铜合金等常规合金的消失模生产，广泛应用于汽车缸体、管道阀门、工程机械耐磨件等工业场景 [[S1,S33,S17]]。SC46材质叶轮类复杂精密铸件可直接采用EPS白模替代传统蜡模进行消失模铸造，获得与泡沫模样外形完全匹配的高精度成品铸件 [[S31]]。

## 关系网络

EPS在消失模铸造体系中的工艺效果与以下因素密切相关：

- **耐火涂料**：不同组分涂料对液态EPS热解产物的渗透排出效率存在显著差异。高透气性高润湿性复合涂料（如含膨胀石墨+铝矾土熟料）可形成连续大尺寸排气通道，液态EPS流动速率是低透气性普通涂料的2~3倍，可大幅降低型腔背压，减少碳渣、气孔缺陷 [[S8,S38]]；
- **真空度**：适当提高浇注系统真空度，可加快EPS热解小分子产物的排出速度，缩短热解产物在高温区的停留时间，减少深度裂解生成的游离碳量 [[S40]]；
- **模样密度**：泡沫密度直接影响热解残留物总量，密度越低，热解产物越少，对铸件质量的负面影响越小，但需兼顾模样搬运强度需求 [[S5,S21]]。

## 视觉证据

![消失模铸造用EPS珠粒堆积形态示意图，展示预发泡前原始珠粒的预处理状态](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41e15cbe-2c1e-4aab-b1e4-b9b0c8da82a5/resource)

上图展示了消失模铸造用EPS珠粒的堆积形态，是EPS白模预发泡、成形发泡等工艺环节的起始物料状态 [[S14]]。发泡后的EPS内部微观结构为典型的闭孔蜂窝状，泡孔直径约50 μm、壁厚约1 μm，这一微观结构是其低密度、低热导率特性的来源 [[S29]]。

## Sources
- S12: [金属精密液态成型技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37ee3f4b-43a5-4863-a27d-5b554468c8dc/resource) (`37ee3f4b-43a5-4863-a27d-5b554468c8dc`)
- S21: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f8ea4b6-95dc-4121-b72f-8261c5a6d2d2/resource) (`9f8ea4b6-95dc-4121-b72f-8261c5a6d2d2`)
- S24: [6310855_发泡聚苯乙烯](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1f19ee0-9961-47bd-8fdd-7cc2ee33e821/resource) (`a1f19ee0-9961-47bd-8fdd-7cc2ee33e821`)
- S33: [塑料制作铸型及其实用铸造工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5466505-7f24-485d-955e-7cf129c8a241/resource) (`d5466505-7f24-485d-955e-7cf129c8a241`)
- S34: [负压实型铸造及铸件质量](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6037392-6806-4780-a32e-05b4ad7e821f/resource) (`d6037392-6806-4780-a32e-05b4ad7e821f`)
- S30: [泡沫聚乙烯模铸造法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8b802d4-4d3f-4a70-9622-371fae80d62c/resource) (`c8b802d4-4d3f-4a70-9622-371fae80d62c`)
- S6: [泡沫聚乙烯模铸造法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1cf741ce-7b55-4c27-a56a-f43b16ca659a/resource) (`1cf741ce-7b55-4c27-a56a-f43b16ca659a`)
- S29: [聚苯乙烯的蜂窝状组织显微图像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5284d8e-0feb-4698-8c19-f38f35c2b514/resource) (`c5284d8e-0feb-4698-8c19-f38f35c2b514`)
- S39: [国外实型铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea5870d1-925a-4f64-a21a-bba5361c34cb/resource) (`ea5870d1-925a-4f64-a21a-bba5361c34cb`)
- S20: [表5.1 EPS材料性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e4685d7-a353-4c93-aaad-e84fb8872f11/resource) (`9e4685d7-a353-4c93-aaad-e84fb8872f11`)
- S15: [最新铸造模具设计制造应用图集与产品造型设计典范及生产常用数据实用手册 第2卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6eff3bab-7002-4818-89ec-4ce47b4b89ce/resource) (`6eff3bab-7002-4818-89ec-4ce47b4b89ce`)
- S19: [金属材料液态成型工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89e03ec2-dd9f-4de6-ab40-bbf2cc699228/resource) (`89e03ec2-dd9f-4de6-ab40-bbf2cc699228`)
- S10: [金属精密液态成型技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/327d0018-5bfa-42c5-b651-f305046f207e/resource) (`327d0018-5bfa-42c5-b651-f305046f207e`)
- S36: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dba150ba-1bc3-4649-9ad6-94bed551551d/resource) (`dba150ba-1bc3-4649-9ad6-94bed551551d`)
- S25: [模具制造手册原著](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5d46058-7d93-41c8-8f3c-d2bf4f4bc273/resource) (`a5d46058-7d93-41c8-8f3c-d2bf4f4bc273`)
- S27: [有色合金消失模铸造原理与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0e334b8-45c1-4658-a100-3a85dec4f876/resource) (`b0e334b8-45c1-4658-a100-3a85dec4f876`)
- S26: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6e7c46d-82a1-4750-9f13-51652b999302/resource) (`a6e7c46d-82a1-4750-9f13-51652b999302`)
- S35: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9d25741-72ca-4f5c-8567-53bbc174d66e/resource) (`d9d25741-72ca-4f5c-8567-53bbc174d66e`)
- S16: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7186d498-bbf6-4f14-839a-eeabb953f069/resource) (`7186d498-bbf6-4f14-839a-eeabb953f069`)
- S37: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0de37f2-eebe-4f62-ae1b-b66a20394eca/resource) (`e0de37f2-eebe-4f62-ae1b-b66a20394eca`)
- S18: [模样在金属液作用下的状态示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8484e72f-90a0-41fc-8ebe-fc0075bbfb0d/resource) (`8484e72f-90a0-41fc-8ebe-fc0075bbfb0d`)
- S23: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1bcb9dd-6083-4f41-853b-6c02d45a9092/resource) (`a1bcb9dd-6083-4f41-853b-6c02d45a9092`)
- S28: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2743e82-6e85-4c57-b408-cbcf5079b850/resource) (`b2743e82-6e85-4c57-b408-cbcf5079b850`)
- S32: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3258e22-e2b6-4618-9a0b-3d797a3ad5c0/resource) (`d3258e22-e2b6-4618-9a0b-3d797a3ad5c0`)
- S22: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0e81e81-75db-44d6-816e-6fcfb0c03f59/resource) (`a0e81e81-75db-44d6-816e-6fcfb0c03f59`)
- S11: [最新铸造模具设计制造应用图集与产品造型设计典范及生产常用数据实用手册 第2卷](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37a6ed26-8cf6-486e-8a50-60284b8a433c/resource) (`37a6ed26-8cf6-486e-8a50-60284b8a433c`)
- S3: [消失模铸造生产实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1489b732-905e-4f0d-9bee-54a74af85999/resource) (`1489b732-905e-4f0d-9bee-54a74af85999`)
- S1: [实型铸造用泡沫聚苯乙烯模样](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ac84041-8818-4e70-9781-17d9f5b73fe4/resource) (`0ac84041-8818-4e70-9781-17d9f5b73fe4`)
- S17: [0050_2d0bd9289516bb61_Lost-foam_casting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78cb7010-4e4f-45de-8d39-757a7222d5dd/resource) (`78cb7010-4e4f-45de-8d39-757a7222d5dd`)
- S31: [叶轮的模样与铸件对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf1aeeea-a3b0-404b-b7d3-7d1ddad83b6d/resource) (`cf1aeeea-a3b0-404b-b7d3-7d1ddad83b6d`)
- S8: [图5.6 液态聚苯乙烯在涂料样品（a）BG-A、（b）BL-B、（c）BE-C中的模拟流速分布图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25e3d0a3-433d-4e23-9286-bd4a8f9f105c/resource) (`25e3d0a3-433d-4e23-9286-bd4a8f9f105c`)
- S38: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e300e032-da81-4720-87a2-aac6eb59d8da/resource) (`e300e032-da81-4720-87a2-aac6eb59d8da`)
- S40: [有色合金消失模铸造原理与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eaa234c6-1c7b-424c-8f42-5895cb2c6fc0/resource) (`eaa234c6-1c7b-424c-8f42-5895cb2c6fc0`)
- S5: [消失模铸造原理及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b8a8f15-be46-4122-8cab-138474be7ec2/resource) (`1b8a8f15-be46-4122-8cab-138474be7ec2`)
- S14: [消失模铸造用EPS珠粒堆积示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41e15cbe-2c1e-4aab-b1e4-b9b0c8da82a5/resource) (`41e15cbe-2c1e-4aab-b1e4-b9b0c8da82a5`)