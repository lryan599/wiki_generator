---
version: "v1"
generated_at: "2026-06-18T11:59:18+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 40
  source_quality_score: 0.87
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

X射线衍射分析（XRD, X-Ray Diffraction）是利用X射线在晶体中的衍射现象，分析材料内部原子空间分布状态的表征技术 [[S49]]。该方法可测定晶体结构、晶格参数、晶体缺陷、多相组分含量及内应力等信息，是材料科学与压铸领域无损物理分析的核心手段之一 [[S49]]。在压铸铝合金/锌合金质量控制中，XRD 常用于物相鉴定、晶粒/亚晶尺寸估算、残余应力测定及择优取向分析 [[S9]]。

## 定义与基本原理

XRD 的理论基石为 **布拉格定律（Bragg's law）**[[S35,S11,S16]]：

$$
n\lambda = 2d\sin\theta
$$

其中：

- λ：入射 X 射线波长  
- θ：布拉格角（入射角的一半，散射角 2θ 是可测量值）  
- d：产生衍射的晶面间距  
- n：衍射级数（正整数）

当一束单色（特征波长）X 射线入射到晶体表面时，晶体内规则排列的原子层可视为一组平行“反射面”。若相邻两层散射射线的光程差恰好为波长整数倍，则反射射线相干加强（相长干涉），形成可被探测器检测的衍射峰；若入射角偏离，反射射线将受到破坏性干涉而抵消 [[S11,S16]]。

**XRD 原理核心示意：**  
下图为布拉格衍射原理示意图，标注了入射 X 射线、反射 X 射线、(hkl) 晶面、衍射角 θ 及晶面间距 d，直接支撑布拉格定律推导说明 [[S28]]。

![布拉格定律原理示意图，展示X射线在晶体(hkl)晶面的反射过程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7db48672-1694-41d7-92df-bd8a366b5ded/resource)

## 仪器组成与结构

常规商用 X 射线衍射仪主要由四大核心部分组成 [[S9]]：

| 部件 | 功能 |
|------|------|
| X 射线发生器（含高压控制系统与 X 射线管） | 提供稳定可控的高压电源，驱动 X 射线管发射特征 X 射线 |
| 测角仪 | 精确控制试样、X 射线源和探测器之间的角度关系，实现 θ–2θ 联动扫描 |
| 辐射探测器 | 接收衍射信号，将 X 射线强度转换为电信号 |
| 自动记录与数据处理单元 | 采集、存储、处理和显示衍射图谱，完成峰位识别与物相检索 |

现代多功能自动衍射仪多采用 **Bragg-Brentano 聚焦几何**，X 射线源与探测器对称布置于试样两侧，试样表面位于测角仪旋转中心，以实现高精度衍射角测量与强度采集 [[S9]]。

**常规 XRD 残余应力测量光路示意图：**  
下图为常规 X 射线衍射法表面残余应力测量原理图，展示 X 射线管出射的入射射线穿透试样表层、生成衍射射线被探测器接收的完整光路，标注沿挤压板材厚度方向的测量路径、测量体积、2θ 衍射角及材料三维坐标系（ED/TD/ND）[[S47]]。

![X射线衍射法残余应力测量原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecbabc24-48c1-4151-ba96-89864fe2cc01/resource)

## 工作模式与分类

XRD 依据试样形态、分析深度与衍射几何的不同，主要分为以下四类工作模式 [[S21,S44]]：

| 工作模式 | 英文缩写 | 模式特点 | 适用场景 |
|----------|----------|----------|----------|
| 粉末X射线衍射 | XRPD | 采用多晶粉末试样，常规 θ–2θ 对称扫描 | 物相定性/定量分析、晶胞参数计算、晶粒尺寸估算 |
| 薄膜X射线衍射 | Thin-film XRD | 小角度掠入射模式，降低穿透深度，抑制基底信号干扰 | 纳米级薄膜物相鉴定、膜厚分析 |
| 微区X射线衍射 | Micro-XRD | 微聚焦X射线源搭配直径 <200 μm 准直器 | 毫米/亚毫米尺度微区物相分析 |
| 小角X射线散射 | SAXS | 采集 2θ < 15° 的低角度散射信号 | 1–100 nm 纳米颗粒分布、孔洞结构分析 |

其中，**粉末X射线衍射（XRPD）** 是实验室最常用模式。当多晶试样中晶粒取向随机分布时，满足布拉格条件的各晶面族均能在相应 2θ 位置产生衍射峰，形成可供检索的完整衍射谱 [[S49]]。

常规粉末 X 射线衍射的标准化操作流程包括 [[S3]]：

1. 试样制备与装样  
2. 测试软件参数配置（X 射线管功率、扫描范围、步长、扫描速度）  
3. 开启 X 射线源预热  
4. 执行连续扫描，采集衍射谱  
5. 关闭 X 射线源，导出原始数据  
6. 匹配 PDF 卡片完成物相检索分析

## 关键参数与操作条件

### 靶材与工作条件

Cu 靶 Kα 辐射是 XRD 应用最广泛的靶材类型，其标准波长为 0.154 nm（1.54 Å）[[S25,S10,S45,S32]]。常规推荐工作电压 40–45 kV，工作电流 40–250 mA [[S25,S10,S32]]。

不同靶材的 X 射线穿透深度存在明显差异，按穿透能力从高到低排序：**Cu 靶 > Cr 靶 > Ti 靶** [[S27]]。针对表层残余应力测试等浅表层分析场景，可选择波长更长的 Co 或 Cr 靶材以降低衍射深度、提升测试分辨率 [[S27]]。

### 扫描参数

| 参数 | 典型取值 | 说明 |
|------|----------|------|
| 2θ 扫描范围 | 10°–90°（常规）；30°–110°（残余应力测试）；20°–70°（快速筛查） | 依据分析目的灵活设定 [[S34,S25,S45]] |
| 步长 | 0.01°–0.02° | 细化步长可提升角度分辨率 [[S34,S25,S32]] |
| 连续扫描速度 | 1°/min–20°/min | 高精度扫描 ≤1°/min；快速筛查 5–20°/min [[S34,S25,S32]] |

### 试样制备要求

- **粉末试样**：研磨至粒度低于 10 μm，避免颗粒尺寸过大导致的衍射峰宽化异常或统计偏差；500 目以上的商用粉末可直接装样测试 [[S37]]。
- **块状试样**：测试面需逐级打磨抛光，确保无明显划痕、凹陷或加工诱导残余应力层；试样测试面须与样品台基准面严格齐平，防止因高度偏差引发峰位偏移 [[S32]]。
- **择优取向控制**：采用随机压片、侧向装样或测试中多次旋转试样等手段降低择优取向影响；择优取向严重时，特定晶面的实测衍射强度与标准 PDF 卡片数值出现显著偏差，将严重干扰物相检索判定 [[S8]]。

## 在压铸领域的具体应用

### 物相鉴定

铸造铝合金 / 锌合金的物相鉴定是 XRD 在压铸领域最基础的应用。常见检测物相如下：

| 合金体系 | 可检出的典型物相 | 引用 |
|----------|-------------------|------|
| ADC12 半固态压铸 | α-Al、Si、Al₂Cu | [[S40]] |
| 真空压铸铝合金 | α-Al、共晶硅、Al₂Cu、Al₅FeSi | [[S51]] |
| A356 压铸铝合金 | α-Al、共晶 Si、Mg₂Si、AlFeSi 系富铁相 | [[S7]] |
| 高硅压铸 Al-xZn-8Si-2Cu | α-Al、共晶 Si、富 Zn 相、Al₂Cu | [[S15]] |
| 6xxx 系压铸铝合金 | Al 基体、共晶 Si、Mg₂Si、Al(FeMn)Si、Al₅FeSi、Al₈Fe₂Si | [[S22]] |

**压铸物相鉴定典型图谱示例：**  
下图为 Al-18Si-7Ni 压铸合金的 XRD 物相鉴定典型图谱，横轴为 2θ 衍射角，纵轴为衍射强度（CPS），明确标注了 Al、Al₃Ni、Si 三种物相对应的全部特征衍射峰 [[S5]]。

![Al-18Si-7Ni压铸合金的XRD物相鉴定典型图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d02a108-54d7-4a3c-8da8-331731a7a564/resource)

此外，真空压铸铝合金在不同热处理工艺（铸态、深冷态、T6 态、深冷固溶时效态）下仅改变物相形貌，不会产生新的物相，XRD 图谱可验证相组成的稳定性 [[S51]]。高 Zn 含量压铸铝合金中，随 Zn 固溶度提升，Si(311)、Si(200)、Al(220)、Al₂Cu(322) 等特征衍射峰向高 2θ 方向偏移，对应铝合金基体发生晶格畸变 [[S15]]。

### 晶粒/亚晶尺寸估算（Scherrer 公式）

Scherrer 公式是 XRD 估算纳米级晶粒/亚晶尺寸的经典方法，表达式为 [[S24]]：

$$
D = \frac{0.89\lambda}{\beta \cos\theta}
$$

其中：D 为晶粒尺寸，λ 为 X 射线波长，β 为校正后的衍射峰半高宽（扣除仪器宽化），θ 为衍射角。**该公式仅适用于 100 nm 及以下尺度的纳米级晶粒计算**，且忽略了微观应变对峰宽化的贡献 [[S24]]。

在压铸场景中，半高宽数据需先行扣除仪器本征宽化，再代入公式计算。当晶粒尺寸达到百微米级及以上时，参与衍射的晶粒数量显著减少，衍射峰出现不连续、峰形异常宽化，此时 Scherrer 公式不再适用 [[S12]]。

### 残余应力测量（sin²ψ 法）

XRD 残余应力测量基于晶格应变与宏观应变一致的假设，通过测定不同 ψ 倾斜角度下的衍射角 2θ 变化，利用 sin²ψ 法计算应力值 [[S2]]。压铸场景下使用 sin²ψ 法的限制条件包括 [[S31]]：

- 要求被测材料为各向同性；若内部存在强烈织构，测量结果会严重偏离真实值  
- 优先选取高指数衍射晶面，以弱化晶粒尺寸偏小、织构等因素带来的测量误差  
- X 射线常规检测深度仅为几微米至十几微米，仅能得到表面及近表层残余应力；如需获取深度方向应力梯度，须搭配化学剥层法逐层测试

### 织构/择优取向分析

XRD 织构分析可获得被测区域所有晶粒的全局统计性取向分布结果 [[S48]]。当材料存在明显择优取向时，各衍射面的实测衍射强度严重偏离 PDF 卡片标准值，会直接导致定性相判定错误与定量相分析失准 [[S50,S46]]。

## 数据分析与解读

### 定性相分析

定性相分析的核心原理是将实测衍射峰的晶面间距 d 值与相对衍射强度 I 与 **PDF（Powder Diffraction File）卡片库** 中的标准数据进行比对 [[S49]]。常用检索方法包括 [[S49,S30]]：

- 哈氏无机数值索引  
- 芬克无机数值索引  
- 戴维无机字母索引

目前主流处理软件（如 Jade、X'pert HighScore、Topas 等）可实现自动匹配检索，无需人工逐条比对 [[S30]]。

### 定量相分析

XRD 定量相分析的三类主流方法 [[S46]]：

| 方法 | 原理 | 特点 |
|------|------|------|
| 外标法 | 通过预先绘制已知浓度标准试样的校准曲线，计算待测相含量 | 简便快速，适用于简单体系 |
| 内标法 | 向待测样品中加入已知质量分数的标准纯相，建立强度换算关系 | 可消除基体效应，需制样严谨 |
| Rietveld 全谱拟合法 | 将实验全谱与各相理论计算谱进行多项式拟合迭代得出定量结果 | 精度最高、数据耗时更长，是多相复杂体系定量首选；还可同步计算微晶平均尺寸、微观应变、位错密度等 [[S43,S29]] |

### Scherrer 公式使用限制

- 仅适用于约 100 nm 以下的晶粒/亚晶尺寸估算 [[S24]]  
- 默认峰宽化全部来源于晶粒细化，忽略了微观应变、位错密度等引起的宽化贡献  
- 必须先行扣除仪器半高宽校正，否则计算结果偏小

## 局限性及常见误区

| 局限/误区 | 说明 | 引用 |
|-----------|------|------|
| 对非晶相无效 | 非晶材料无长程有序周期结构，仅在低 2θ 区间产生宽的弥散衍射峰，无法直接高精度定量，仅能半定性判定非晶是否存在 | [[S23]] |
| 晶粒过大导致统计性偏差 | 晶粒尺寸达百微米级以上时，参与衍射的晶粒数量骤减，衍射峰不连续、峰形异常宽化，积分强度计算不准 | [[S12]] |
| 表面应力状态干扰 | 机加工引入的表面残余应力层将导致晶格畸变、峰位偏移，测试前须通过抛光去除 | [[S2]] |
| 择优取向干扰 | 导致衍射强度严重偏离标准值，影响定性匹配与定量精度；宜制备为粉末试样测试 | [[S50,S46]] |
| 探测深度限制 | Cu 靶 Kα 常规穿透仅几微米至几十微米，只能获取表层信息；深层残余应力需逐层剥离+多次测试 | [[S2,S18]] |
| 定量半定量准确度差异 | 外标法/内标法受织构、晶粒度、表面形貌等因素影响；Rietveld 法精度最高但流程复杂 | [[S46]] |

## 关联技术与互补手段

XRD 与其他材料表征技术的协同应用可显著提升分析精度与全面性：

| 互补技术 | 与 XRD 的协同逻辑 | 引用 |
|----------|--------------------|------|
| SEM/EDS | XRD 获取整体结晶相统计结果，EDS 提供微区元素分布，二者结合可将“元素组成”与“物相归属”精准匹配 | [[S39,S1]] |
| XRF | XRF 直接给出元素总含量，无法区分同元素不同物相；XRD 可完成物相归属判定，二者互为补充 | [[S18]] |
| EBSD | XRD 织构分析获取全局统计取向分布，EBSD 可实现微米级分辨率单晶粒取向成像，二者结合掌握宏观-微观织构规律 | [[S1,S48]] |
| TEM 电子衍射 | XRD 给出毫米级区域的统计性物相结果，TEM 选区电子衍射（SAD/CBED）可解析纳米尺度单颗相的晶体结构，避免漏检微量纳米析出相 | [[S1,S14]] |

## 相关标准与规范

| 标准编号 | 范围 | 引用 |
|----------|------|------|
| ASTM E975 | 《Practice for X-ray determination of retained austenite in steel with near random crystallographic orientation》，适用于采用 X 射线衍射法定量测定晶体取向近似随机分布的钢铁材料中残余奥氏体的体积分数 | [[S38]] |
| EN 15305 | X 射线衍射残余应力测定标准（注：本知识库未返回标准原文，无法提供详细条目） | [[S2]] |
| GB/T 30904 | X 射线衍射残余应力测定国家标准（注：本知识库未返回标准原文，无法提供详细条目） | [[S2]] |

## Sources
- S49: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8c50f34-29d7-4cfc-901d-e26446b51b31/resource) (`f8c50f34-29d7-4cfc-901d-e26446b51b31`)
- S9: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/118f5c64-79f2-4ddf-bf91-d88561d1fef0/resource) (`118f5c64-79f2-4ddf-bf91-d88561d1fef0`)
- S35: [arihant chemistry question bank by sanjay sharma for iit jee main solid__dba575c099](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9494eac-7b21-4a35-9cf9-d78f0bf40afa/resource) (`a9494eac-7b21-4a35-9cf9-d78f0bf40afa`)
- S11: [elements of physical metallurgy__d6cd3b1fa0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b00c555-faf0-426f-9092-d5b45ffb77f9/resource) (`1b00c555-faf0-426f-9092-d5b45ffb77f9`)
- S16: [elements of physical metallurgy__923bb3a713](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35efcfcc-d8f9-4ef9-a913-0211eb45f082/resource) (`35efcfcc-d8f9-4ef9-a913-0211eb45f082`)
- S28: [布拉格定律原理示意图，展示X射线在晶体(hkl)晶面的反射过程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7db48672-1694-41d7-92df-bd8a366b5ded/resource) (`7db48672-1694-41d7-92df-bd8a366b5ded`)
- S47: [X射线衍射法残余应力测量原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecbabc24-48c1-4151-ba96-89864fe2cc01/resource) (`ecbabc24-48c1-4151-ba96-89864fe2cc01`)
- S21: [计算机在材料热加工工程中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48189482-c745-4732-a056-2a2a6fca4b49/resource) (`48189482-c745-4732-a056-2a2a6fca4b49`)
- S44: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddf0b34f-14bb-475f-b435-7d987f98961a/resource) (`ddf0b34f-14bb-475f-b435-7d987f98961a`)
- S3: [计算机在材料热加工工程中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/071947da-d660-481e-8e3c-e5d29c70b865/resource) (`071947da-d660-481e-8e3c-e5d29c70b865`)
- S25: [菱镁矿粉为原料制备MgAlCrFeSiTi高熵合金的组织结构及性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/66c87403-d4a9-43c6-9dde-6a227e7b3282/resource) (`66c87403-d4a9-43c6-9dde-6a227e7b3282`)
- S10: [激光熔覆CoCrFeNiMoNb_WC复合涂层及高温服役性能的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1609858e-e5d8-4558-9a81-a1fdd9850ab1/resource) (`1609858e-e5d8-4558-9a81-a1fdd9850ab1`)
- S45: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e09979af-dc3a-41ea-87aa-1f1926fcce4d/resource) (`e09979af-dc3a-41ea-87aa-1f1926fcce4d`)
- S32: [压铸模具钢热机械疲劳行为及损伤机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9cb03500-ef19-4bdd-87ad-60aa6eb88c99/resource) (`9cb03500-ef19-4bdd-87ad-60aa6eb88c99`)
- S27: [工程陶瓷材料的加工技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7157d619-e985-461d-88f9-865c65b60c38/resource) (`7157d619-e985-461d-88f9-865c65b60c38`)
- S34: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7866b2b-bbea-4c2c-9bb8-e7ae19a17d03/resource) (`a7866b2b-bbea-4c2c-9bb8-e7ae19a17d03`)
- S37: [Cr添加对FeNi合金组织及磁性能影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2ef5c06-7f18-4367-ad4f-a785237a816b/resource) (`b2ef5c06-7f18-4367-ad4f-a785237a816b`)
- S8: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/110640a0-e263-48cc-a85e-10c9e36f9441/resource) (`110640a0-e263-48cc-a85e-10c9e36f9441`)
- S40: [低过热度倾斜板流变压铸对ADC12组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb80db8e-2b73-404b-bd71-036327c607d9/resource) (`bb80db8e-2b73-404b-bd71-036327c607d9`)
- S51: [强流脉冲电子束强化真空压铸铝合金的高温摩擦磨损行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc41b47a-e112-40be-81d9-ea796d9d8a3f/resource) (`fc41b47a-e112-40be-81d9-ea796d9d8a3f`)
- S7: [不同成形方式及热处理对A356铝合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e0c7521-284f-4a66-a7eb-a28f340c5466/resource) (`0e0c7521-284f-4a66-a7eb-a28f340c5466`)
- S15: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30bed7da-b3ea-4f59-b22e-2999964c0a52/resource) (`30bed7da-b3ea-4f59-b22e-2999964c0a52`)
- S22: [6xxx系铝合金的XRD相分析图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a692ce2-d81d-478d-a454-a794f9647f2e/resource) (`5a692ce2-d81d-478d-a454-a794f9647f2e`)
- S5: [图3.3Al-18Si-7Ni铸件试样的XRD测试图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d02a108-54d7-4a3c-8da8-331731a7a564/resource) (`0d02a108-54d7-4a3c-8da8-331731a7a564`)
- S24: [溶胶粒子在铝镁合金微弧氧化中的作用机制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/648c894f-1c63-4e1c-aab5-7cb803ad8ac5/resource) (`648c894f-1c63-4e1c-aab5-7cb803ad8ac5`)
- S12: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e244eb1-09dd-4dcc-957b-f8ada0fed322/resource) (`1e244eb1-09dd-4dcc-957b-f8ada0fed322`)
- S2: [铝合金整体结构件铣削加工残余应力及变形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/046f2a13-2d54-4be7-a604-ef2443dd365e/resource) (`046f2a13-2d54-4be7-a604-ef2443dd365e`)
- S31: [AZ91D镁合金构件铸造残余应力有限元模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/88b02cd6-192f-482d-8cdf-3d457efe9b15/resource) (`88b02cd6-192f-482d-8cdf-3d457efe9b15`)
- S48: [激光3D打印多孔锌骨支架及其性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efb75942-eb12-485c-8814-b11b5e7226a8/resource) (`efb75942-eb12-485c-8814-b11b5e7226a8`)
- S50: [表面沉积技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8e50778-b2de-408b-8344-199bceb55bbf/resource) (`f8e50778-b2de-408b-8344-199bceb55bbf`)
- S46: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb693ea6-5e16-4092-996a-ac683398a5e2/resource) (`eb693ea6-5e16-4092-996a-ac683398a5e2`)
- S30: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/85e7d669-dea3-465a-b590-40d136e4cb55/resource) (`85e7d669-dea3-465a-b590-40d136e4cb55`)
- S43: [alloys and composites corrosion and mechanical properties__573c8b2ba2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2e1aa39-2949-4e50-bbd7-62c72c02d900/resource) (`d2e1aa39-2949-4e50-bbd7-62c72c02d900`)
- S29: [creep and high temperature deformation of metals and alloys__3b591a6325](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82743266-3295-4978-909d-8acd2b5c9f4d/resource) (`82743266-3295-4978-909d-8acd2b5c9f4d`)
- S23: [effect of disorder and defects in ion implanted semiconductors electrical and physicochemical characterization__09b14...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b80cb2c-3933-4d22-889f-efe3d801c75a/resource) (`5b80cb2c-3933-4d22-889f-efe3d801c75a`)
- S18: [characterization of metals and alloys 金属与合金的表征__7f81135ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d02a34a-a29a-4a24-b761-2a70c76dcf47/resource) (`3d02a34a-a29a-4a24-b761-2a70c76dcf47`)
- S39: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7642b0d-982b-46a4-a788-f84c901f0381/resource) (`b7642b0d-982b-46a4-a788-f84c901f0381`)
- S1: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0145eb27-8393-47ea-804d-ccf579a0ba51/resource) (`0145eb27-8393-47ea-804d-ccf579a0ba51`)
- S14: [developing a die casting magnesium alloy with excellent mechanical perfo__81e986a15a](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ffa9ba3-47f3-48e8-9e38-5cc5481712bf/resource) (`2ffa9ba3-47f3-48e8-9e38-5cc5481712bf`)
- S38: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b67d4c84-d019-4cd1-b32c-1ab18a0deffc/resource) (`b67d4c84-d019-4cd1-b32c-1ab18a0deffc`)