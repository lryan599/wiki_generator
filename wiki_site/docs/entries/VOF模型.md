---
version: "v1"
generated_at: "2026-06-18T12:34:35+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 51
  source_quality_score: 0.86
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

VOF（Volume of Fluid，流体体积法）是一种欧拉固定网格框架下的隐式多相流界面追踪方法，由Hirt和Nichols于1981年首次提出[[S24,S52]]。该方法通过定义并追踪每个计算网格单元内流体相的体积分数（记为 **α** 或 **F**），间接捕获气‑液两相界面的位置与运动，适用于互不混溶的两种（或多种）流体的流动问题[[S4,S53]]。在压铸领域，VOF方法已广泛应用于模具充型过程的数值模拟，能够预测金属液自由表面的演变、卷气行为以及气孔缺陷的可能位置，是目前商用压铸仿真软件中最核心的充型计算方案之一[[S1,S21,S57]]。

## 定义与基本原理

### 体积分数 α 的定义

在以VOF为基础的多相流模型中，对每一个网格单元引入一个标量 **α**，表示某一相（例如液态金属）占据该单元的体积比率[[S13,S52]]：

> α = 单元内流体的体积 / 单元总体积

因此：
- **α = 0**：单元完全由气相（空气）占据，不含金属液；
- **α = 1**：单元被金属液充满，为内部单元；
- **0 < α < 1**：单元同时包含金属液和空气，即为两相界面所在区域[[S4,S52,S13]]。

在充型过程的任一时刻，只需遍历所有网格单元并求解 α 的值，就能确定铸件型腔中自由表面的几何位置[[S16]]。

### VOF输运方程

体积分数 α 被视作一种跟随流体质点运动的“示踪量”，其输运仅由对流控制，不存在扩散项。对不可压缩流动，VOF的相方程通常写为[[S53,S24,S14]]：

```
∂α/∂t + ∇·(α u) = 0
```

在三维笛卡儿坐标下展开为：

```
∂α/∂t + u ∂α/∂x + v ∂α/∂y + w ∂α/∂z = 0
```

其中 **u**, **v**, **w** 为速度分量。该方程保证当网格内的流体流入流出平衡时，α 值仅随平流运动传递[[S14,S16]]。

### 控制方程组

在压铸充型模拟中，VOF方法通常与不可压缩连续方程及Navier–Stokes（N‑S）动量方程联立求解[[S53,S45]]：

- **连续方程（不可压缩）**：  
  ∇·**u** = 0  
  [[S53]]

- **动量方程**：  
  ∂(ρ**u**)/∂t + ∇·(ρ**u** **u**) = –∇p + μ∇²**u** + ρ**g** + **F_s**  
  其中 ρ 为混合密度（按体积分数加权平均），μ 为混合黏度，**F_s** 为表面张力源项[[S45,S43]]。

固体‑液体混合物的物性通过体积分数进行加权计算[[S43]]：
```
ρ = α ρ_liquid + (1 - α) ρ_gas
μ = α μ_liquid + (1 - α) μ_gas
```

### 表面张力处理：CSF（连续表面力）模型

VOF本身在界面处的体积分数函数不连续，难以直接计算界面曲率和表面张力。通常采用Brackbill提出的**连续表面力（CSF）模型**，将作用于几何界面上的表面张力等效为分布在界面附近网格上的体积力，可直接作为源项加入动量方程[[S26,S44]]：

```
F_s = σ κ ∇α
```

其中 **σ** 为表面张力系数，**κ** 为界面局部曲率，通过下式计算[[S26]]：
```
κ = –∇·(∇α / |∇α|)
```

这一处理避免了显式构造几何界面的复杂操作，使得表面张力的数值计算简洁且易于并行实现[[S26,S45]]。

## 界面重构技术

经典VOF方法在求解纯对流输运方程时，极易产生数值扩散（假扩散），导致界面模糊——大量原本应完全充满或完全为空的单元表现出 0<α<1 的伪界面状态[[S8]]。因此，工程上需要引入高精度的界面重构技术，以保持锐利的气‑液边界。

### 代数类重构方法

早期的代数方法利用相邻网格的流量信息修正界面输运，包括：

- **施主‑受主法（Donor‑Acceptor）**：同时利用界面单元上游（施主）与下游（受主）的流率信息确定自由面移动量，是传统VOF中一直采用的基本方法，但难以避免45°方向的流体体积重叠传递失真[[S8,S18]]。
- **Van Leer二阶格式**：采用单调性保证的二阶差分格式求解偏微分方程的标量输运，减少数值振荡[[S8]]。

代数方法计算简单，但对大曲率、复杂拓扑变化的自由面捕捉精度有限[[S64]]。

### 几何类重构方法：PLIC（分段线性界面计算）

**PLIC（Piecewise Linear Interface Calculation）** 是VOF界面重构的代表性几何方法。在每个含界面的单元内部，用一张任意取向的平面对自由面进行近似，然后依次执行：计算自由面常量、迭代重绘自由面、计算相邻单元间的迁移体积、更新下一时步的体积分数场[[S23]]。PLIC方法不存在Hirt‑Nichols算法在45°方向上的体积重叠失真问题，并且可以处理局部阻塞（如模具壁面）的非规则单元[[S64,S23]]。

在曲折形压铸型腔的充型计算中，多个时间步的对比表明：PLIC重构的气孔位置与实验检测结果高度吻合，而SLIC或Hirt‑Nichols代数重构方法会将连续气孔提前分割为大量伪小气孔，甚至在充型后期生成不真实的气孔[[S59]]。

### 高分辨率差分格式

现代铸造VOF仿真中，常结合高分辨率差分格式进一步抑制数值耗散：

- **HRIC（High Resolution Interface Capturing）**：可将相界面的数值耗散控制在约1个网格单元以内，实现极尖锐的自由面，已在工业级铸造充型软件中广泛应用[[S10]]。
- **CICSAM（Compressive Interface Capturing Scheme for Arbitrary Meshes）**：由Ubbink与Issa提出，适用于任意网格，在高流速、大Courant数工况下能够避免相界面的拖尾现象，尤其适合压铸高速充流过程[[S31]]。

### 重构方法效果对比

在相同粗糙网格（40×40单元）下的平移、充型测试中，不同算法的表现差异明显[[S23,S64,S59]]：

| 算法 | 45°平移失真 | 气孔预测准确性 | 是否产生虚假气孔 | 适用网格 |
|------|-------------|----------------|------------------|----------|
| Hirt‑Nichols | 严重（体积重叠传递） | 差（气孔被过早分割） | 是 | 规则网格 |
| SLIC | 中等 | 一般（气孔后期消失） | 否 | 规则网格 |
| PLIC | 极小，界面光滑 | 高（气孔位置与实验一致） | 否 | 任意网格 |

可见，PLIC方法在保持界面尖锐性和体积守恒方面具有显著优势，是当前高精度压铸VOF仿真的主流界面重构方案[[S64]]。

## VOF与相关界面追踪方法的比较

### VOF vs. Level Set

VOF追踪的是单元内各相的体积分数，天然满足严格的质量守恒。其弱点在于体积分数函数在界面处不连续，导致空间梯度的计算精度低，进而影响界面曲率和表面张力的准确估算[[S38,S27]]。  
**Level Set方法**则通过一个连续、光滑的符号距离函数 φ(x,t) 描述界面位置（φ=0 即界面），可以高精度计算界面曲率和表面张力，但长时间模拟中会出现明显的质量耗散，不能满足质量守恒[[S27,S7]]。

| 特性 | VOF | Level Set |
|------|-----|-----------|
| 变量定义 | 体积分数 α（0→1） | 符号距离 φ（正/负） |
| 质量守恒 | 严格满足 | 需额外校正，否则耗散 |
| 界面曲率计算 | 精度较低（函数不连续） | 精度高（函数光滑） |
| 实现复杂度 | 较低 | 较高 |

### CLSVOF（耦合Level Set与VOF）

CLSVOF方法同时求解VOF的体积分数方程和Level Set的距离场方程，继承VOF的质量守恒优势与Level Set高精度曲率计算的优点[[S7,S38]]。具体做法是先通过VOF方程获取满足守恒性的界面位置，再求解Level Set方程以计算界面法向和曲率，从而得到精确的表面张力项，而无需牺牲体积守恒性[[S7,S19]]。该方法特别适用于高压压铸（HPDC）等界面拓扑剧烈变化、对卷气预测精度要求极高的场景[[S7]]。

### VOF与动网格/显式界面追踪

传统显式界面追踪方法（例如Front Tracking）直接跟踪界面上的几何节点，极难自动处理界面合并、破碎等拓扑变化；任意拉格朗日‑欧拉（ALE）动网格方法则需随自由面移动持续更新网格，仅适用于界面变形较小的流动，无法应对压铸高速充型中频繁发生的飞溅、融合等现象[[S4,S42]]。VOF方法因基于固定欧拉网格，天然具备处理此类复杂拓扑变化的能力，因而成为铸造充型模拟中自由面处理的首选方案[[S4]]。

## 压铸中的应用场景

VOF方法在压铸工艺中主要用于充型过程的数值模拟，预测金属液‑空气两相流动特征，为模具设计和工艺优化提供依据。

### 高压铸造充型与卷气缺陷预测

高压铸造（HPDC）充型过程中，金属液高速注入型腔，极易裹挟空气形成卷气缺陷[[S21]]。基于VOF的气液两相流求解结合**k‑ε 湍流模型**，可还原金属液的紊流充型过程，并通过后处理连通域标记算法和气泡破碎判据定位最终残余的卷气区域[[S10,S29]]。预测结果可与实际铸件的X射线探伤气孔分布高度吻合，适用于铝合金、镁合金、锌合金等压铸合金[[S21,S50]]。

工业实例覆盖汽车曲轴箱、发电机端盖、铝合金薄壁壳体等零部件[[S1]]。相关研究成果已在《中国有色金属学报》等学术期刊发表[[S29]]。

### 低压铸造

在A356铝合金轮毂的低压铸造中，Liu等采用VOF两相流模型对不同压力加载速率下的充型速度场进行模拟，成功识别出易产生涡流的区域，预判氧化夹杂缺陷，并通过水模拟实验验证了仿真结果与实际充型形态的高度吻合[[S28]]。此外，Flow‑3D内置VOF模块也被用于铝合金发动机缸体低压铸造的卷气分布计算，指导充型工艺优化[[S3]]。

### 模具设计与浇注系统优化

借助VOF充型模拟可提前识别充型滞后的远端区域、汇流卷气高风险区，有针对地调整内浇口尺寸、布局以及排气道位置。例如汽车支架压铸模具在修改辅助浇道尺寸后，成功解决了汇流区的卷气缺陷，大幅减少了试模次数[[S46,S9]]。

## 关键参数与设置

### 时间步长

压铸充型VOF仿真中选择时间步长需同时满足四项稳定性约束，取所有约束计算出的最小值[[S17,S48]]：

1. 一个时间步内流体移动距离不超过1个网格：Δt < min(Δx/|u|, Δy/|v|, Δz/|w|) [[S17]]；
2. 动量扩散距离不超过1个网格[[S17]]；
3. 表面张力驱动的流动在单步内不超过1个网格[[S17]]；
4. 库朗数满足权重因子约束（例如 Courant 数 ≤ 1）[[S48,S17]]。

### 网格尺寸

网格划分直接影响VOF仿真的精度与计算成本。工程实践中推荐：薄壁、充型前沿等关键区域网格尺寸控制在 **1~3 mm**；常规主体区域可使用 **6~20 mm** 的网格；不同层级相邻网格的尺寸比不宜超过 **2:1**，以保证网格线对齐并减少界面插值误差[[S5,S12,S22]]。

### 湍流模型耦合

高压铸造的充型金属液流速高、雷诺数大，通常呈现剧烈湍流。VOF计算推荐耦合 **RNG k‑ε** 或 **SST k‑ε** 湍流模型；部分场景下也可采用显式大涡模拟（LES）以获得更高精度的流场细节[[S61,S11,S58]]。

### 表面张力系数

CFS模型中表面张力系数 σ 需根据合金和温度设定，通常取自软件内置的物性数据库或实验数据[[S45]]。

### 典型软件参数实例

以ProCAST软件为例，其压铸充型Flow模块的标准设置中，体积分数更新频率 **VFREQ = 50**，参考压力 **PREF = 1.0132×10⁵ N/m²**，为行业常用推荐值[[S35]]。

## 软件实现

目前主流压铸仿真软件均内置了基于VOF的求解器，但在具体实现和优化程度上有所差别。

| 软件 | VOF模块名称 | 特色 | 适用场景 |
|------|------------|------|----------|
| **FLOW‑3D** | TrueVOF | 由VOF提出者C.W. Hirt博士团队开发的原厂算法，结合FAVOR™隐式几何表征技术，自动将自由表面相邻网格处理为无质量空单元，大幅降低计算量，是行业内公认的压铸充型仿真精度最高的VOF实现之一[[S52,S25,S47]] | 高压/低压铸造、精密自由表面分析 |
| **ANSYS Fluent** | VOF模块（通用CFD） | 支持用户自定义离散格式、表面张力模型、湍流耦合方式，可通过UDF（User Defined Functions）自定义压铸合金物性、卷气判据等，二次开发性强[[S51,S11]] | 研究性压铸仿真、自定义模型开发 |
| **AnyCasting** | 基于SOLA‑VOF的专用求解器 | 针对压铸工艺深度优化，内置全系列常用压铸合金物性数据库，可自动输出卷气、冷隔等缺陷预测结果，无需复杂参数配置，仿真效率远高于通用CFD软件[[S58,S6]] | 工程化压铸模流分析 |
| **OpenFOAM** | interFoam等VOF求解器 | 开源架构，支持自适应网格加密、多相流耦合求解，适合面向压铸场景的二次开发与算法研究[[S34]] | 学术研究、新算法开发 |

## 优点与局限

### 优点

- **严格质量守恒**：体积分数天然满足质量守恒，适合长时间流动模拟[[S38]]。
- **实现简单、计算效率高**：SOLA‑VOF等方法收敛域宽，迭代次数少，是目前铸造充型模拟的主流框架[[S16,S30]]。
- **适用复杂拓扑变化**：能处理界面合并、破碎、飞溅等强非线性自由面行为[[S4]]。
- **工业验证充分**：Hy代、水模拟实验对比表明，VOF对充型宏观流动形态的预测与实验高度吻合[[S33]]。

### 局限

- **数值扩散导致界面模糊**：低阶离散格式下难以保持尖锐界面，必须耦合HRIC、CICSAM或PLIC等高分辨率技术[[S36]]。
- **网格依赖性极强**：对微小流动特征（如薄壁区填充、微气泡），需要将网格细化到特征尺寸的1/5~1/3量级才能获得可靠结果，计算资源消耗随网格数量超线性增长[[S22,S5]]。
- **微小气泡的融合/破碎难以捕捉**：传统VOF对微尺度卷气的演化过程预测能力不足，不如SPH等拉格朗日方法[[S33]]。
- **单独求解时曲率精度低**：体积分数不连续，直接计算界面曲率和表面张力误差较大，常需借助CLSVOF等方法弥补[[S7,S38]]。

## 可视化证据

![高压压铸板模填充过程VOF模拟、实验观测与SPH模拟结果对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/deed832e-877f-450f-9d1a-29f5235fec7b/resource)

Schmid与Klein的水模拟实验对比研究表明：VOF方法对高压压铸充型宏观流动形态的预测与实验吻合度较高，仅在小尺度自由表面结构、微小气泡形貌的捕捉精度上弱于SPH方法[[S33,S54]]。上图直观展示了同一板模在VOF模拟、实验观测及SPH模拟下的填充状态对比，是VOF在压铸领域最经典的验证案例之一。

![SOLA-VOF算法中施主-受主流量法原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ac0e5cb-5264-436e-9ac4-37ed61e5dc36/resource)

在传统SOLA‑VOF框架中，施主‑受主法通过同时利用上游施主单元与下游受主单元的流率信息来计算自由界面移动量[[S8,S18]]。该示意图标注了网格单元、流动方向、施主/受主关系，是早期VOF界面处理的标准原理图[[S32]]。

## Sources
- S24: [注塑成型模拟及模具优化设计理论与方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6de302e2-27cd-4ed4-8d99-1447bb73fdc1/resource) (`6de302e2-27cd-4ed4-8d99-1447bb73fdc1`)
- S52: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cebf24c0-955e-4e04-a8bf-1cead4723270/resource) (`cebf24c0-955e-4e04-a8bf-1cead4723270`)
- S4: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20acdea1-fd2d-4c1b-b532-1047a1233132/resource) (`20acdea1-fd2d-4c1b-b532-1047a1233132`)
- S53: [基于非等温条件下RTM工艺过程与缺陷预测研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0604f0d-c9cf-46e5-8b7e-a5df8bb0fd7f/resource) (`d0604f0d-c9cf-46e5-8b7e-a5df8bb0fd7f`)
- S1: [die casting parameters and simulations for crankcase of automobile using__2a23cb7ad5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/137ba49f-2ae2-483d-9cfd-deda34c621fa/resource) (`137ba49f-2ae2-483d-9cfd-deda34c621fa`)
- S21: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68dc99f8-9be9-40dc-8f20-8f250f352860/resource) (`68dc99f8-9be9-40dc-8f20-8f250f352860`)
- S57: [effects of shot sleeve filling on evolution of the free surface and soli__237f20449f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3ce749f-8bdc-429f-85ed-98470ec1b11f/resource) (`e3ce749f-8bdc-429f-85ed-98470ec1b11f`)
- S13: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53a94f2f-9850-4b33-9fdc-efec519538cb/resource) (`53a94f2f-9850-4b33-9fdc-efec519538cb`)
- S16: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57bb9bfd-f8bb-4dca-bfb1-2da078f1985a/resource) (`57bb9bfd-f8bb-4dca-bfb1-2da078f1985a`)
- S14: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53cdc1b8-02dd-4190-bfff-c3e80c5057b0/resource) (`53cdc1b8-02dd-4190-bfff-c3e80c5057b0`)
- S45: [压铸数值模拟后处理区域可视化及卷气缺陷位置预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b9a7aefe-be4b-46ad-9cf9-9b931cc22e7c/resource) (`b9a7aefe-be4b-46ad-9cf9-9b931cc22e7c`)
- S43: [铝合金车轮低压铸造模具冷却系统界面换热机理分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1b86ebb-aa23-4190-82a2-f82bbb03d251/resource) (`b1b86ebb-aa23-4190-82a2-f82bbb03d251`)
- S26: [american institute of aeronautics and astronautics 31st thermophysics co__84bde37c6f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76cbd368-df3e-4bea-9d95-29d22ce8b174/resource) (`76cbd368-df3e-4bea-9d95-29d22ce8b174`)
- S44: [基于SPH法的压铸充型过程模拟及冷隔模型构建](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b599c007-dc9a-4f3d-b0a5-3ee07eeed185/resource) (`b599c007-dc9a-4f3d-b0a5-3ee07eeed185`)
- S8: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/337b41ce-f048-422b-8f71-85d1d1d17def/resource) (`337b41ce-f048-422b-8f71-85d1d1d17def`)
- S18: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61026234-b5bb-43db-ac9a-9f8bf8c0f99e/resource) (`61026234-b5bb-43db-ac9a-9f8bf8c0f99e`)
- S64: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe8a36dd-c8f8-4654-8b5a-4a5d700cbc1b/resource) (`fe8a36dd-c8f8-4654-8b5a-4a5d700cbc1b`)
- S23: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a75c437-bcf6-4492-a590-f773bb9f5e3e/resource) (`6a75c437-bcf6-4492-a590-f773bb9f5e3e`)
- S59: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9ace8ce-a13d-4d8a-b45f-66337bbc3783/resource) (`e9ace8ce-a13d-4d8a-b45f-66337bbc3783`)
- S10: [cfd modeling and simulation in materials processing 2016 tms cfd simulat__395156bdb3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b78185d-beed-4853-bc86-dfa996fada26/resource) (`4b78185d-beed-4853-bc86-dfa996fada26`)
- S31: [工业级砂型打印机墨滴喷射仿真与供墨系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a8abd63-1905-418b-9fc2-f8b2480d227f/resource) (`8a8abd63-1905-418b-9fc2-f8b2480d227f`)
- S38: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a10cebfa-57da-40d1-8cd0-3ce33a4a83ed/resource) (`a10cebfa-57da-40d1-8cd0-3ce33a4a83ed`)
- S27: [QCW激光热调控钢铝异种金属焊接特性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77a1ef81-152f-47da-9bb7-560ddaaab48f/resource) (`77a1ef81-152f-47da-9bb7-560ddaaab48f`)
- S7: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ea0556f-ef4f-4d56-b886-e80ce6719e29/resource) (`2ea0556f-ef4f-4d56-b886-e80ce6719e29`)
- S19: [asme asme 2015 international mechanical engineering congress and exposit__0000021e5e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6193ff8d-4832-4e3f-b80f-2d51da65c296/resource) (`6193ff8d-4832-4e3f-b80f-2d51da65c296`)
- S42: [additive manufacturing of metal alloys 1 processes raw materials and numerical simulation__200a158ad1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afeb066f-a7f4-4e3d-8e66-3c0117f5dd01/resource) (`afeb066f-a7f4-4e3d-8e66-3c0117f5dd01`)
- S29: [cfd modeling and simulation in materials processing 2016 tms cfd simulat__395156bdb3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c37ec23-efa7-43a9-9ed8-01e51b0e6bba/resource) (`7c37ec23-efa7-43a9-9ed8-01e51b0e6bba`)
- S50: [direct observation of filling process and porosity prediction in high pr__a2c715c3d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4598d5e-0af0-4609-8792-311baa5a1a69/resource) (`c4598d5e-0af0-4609-8792-311baa5a1a69`)
- S28: [铝合金低压铸造过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a16e8d9-c788-464d-969a-b7a80f0adbf9/resource) (`7a16e8d9-c788-464d-969a-b7a80f0adbf9`)
- S3: [aip materials processing and design modeling simulation and applications__d208c48c41](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/187294d6-48bf-4cdb-9e29-a74c314d1d2c/resource) (`187294d6-48bf-4cdb-9e29-a74c314d1d2c`)
- S46: [die casting die design based on the application of cae simulation__42797f6dd3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd1c2689-4c53-4a17-8733-d01ef9e61db4/resource) (`bd1c2689-4c53-4a17-8733-d01ef9e61db4`)
- S9: [design of die casting process of top cover of automobile generator throu__2ef2b83fdd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d59f385-1fa0-45ba-995f-582970e69bf3/resource) (`3d59f385-1fa0-45ba-995f-582970e69bf3`)
- S17: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f70582f-a063-40aa-b1ef-9e8d16149774/resource) (`5f70582f-a063-40aa-b1ef-9e8d16149774`)
- S48: [第三届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd5e7141-07ab-47be-8225-749b691edf98/resource) (`bd5e7141-07ab-47be-8225-749b691edf98`)
- S5: [低压铸造铝合金轮毂工艺参数对缩孔缺陷的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23b0bc48-f6de-4d8e-823e-d168b06f6f41/resource) (`23b0bc48-f6de-4d8e-823e-d168b06f6f41`)
- S12: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5075d9cf-ad72-40d0-8b61-951753311642/resource) (`5075d9cf-ad72-40d0-8b61-951753311642`)
- S22: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/69505a7b-549e-4f04-b2ed-1458f5808d4e/resource) (`69505a7b-549e-4f04-b2ed-1458f5808d4e`)
- S61: [铝合金半固态压铸工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef20cd8d-6176-48ca-95d1-dc347c290431/resource) (`ef20cd8d-6176-48ca-95d1-dc347c290431`)
- S11: [混合坩埚的结构、温度以及浇注条件对受控扩散凝固Al-Si合金微观组织的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4f41a832-034e-45ec-8aff-e2936005c229/resource) (`4f41a832-034e-45ec-8aff-e2936005c229`)
- S58: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S35: [ProCAST铸造模拟流体类参数设置表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/96a4c172-228b-4c93-aa66-89b035c08362/resource) (`96a4c172-228b-4c93-aa66-89b035c08362`)
- S25: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/749d0b51-3857-4a91-9926-d67f29bd8056/resource) (`749d0b51-3857-4a91-9926-d67f29bd8056`)
- S47: [AlSi10MnMg铝合金薄壁件压铸充型能力及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd3925b0-a710-464c-8658-7e1a047df7b8/resource) (`bd3925b0-a710-464c-8658-7e1a047df7b8`)
- S51: [基于非等温条件下RTM工艺过程与缺陷预测研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb2fa8cf-8dae-4f4d-a16e-5c0bb3b687fb/resource) (`cb2fa8cf-8dae-4f4d-a16e-5c0bb3b687fb`)
- S6: [前油封端盖压力铸造工艺与缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/253c6116-36e9-40db-a180-a738c4ae692b/resource) (`253c6116-36e9-40db-a180-a738c4ae692b`)
- S34: [ACE液液分层流动CFD模拟研究参数对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/931642f8-13fa-47d5-8f94-ec696c3b06f2/resource) (`931642f8-13fa-47d5-8f94-ec696c3b06f2`)
- S30: [压铸铝合金平板试样充型流动行为的可视化表征及研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87a83816-f183-4370-9308-7feae7709688/resource) (`87a83816-f183-4370-9308-7feae7709688`)
- S33: [comparison of sph simulations of high pressure die casting with the expe__b04b0e5eb0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f262029-ac8a-4591-b153-55032ba8b5b3/resource) (`8f262029-ac8a-4591-b153-55032ba8b5b3`)
- S36: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97726e24-e029-4370-9696-63b2fe157b62/resource) (`97726e24-e029-4370-9696-63b2fe157b62`)
- S54: [高压压铸板模填充的Schmid & Klein、实验与SPH结果对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/deed832e-877f-450f-9d1a-29f5235fec7b/resource) (`deed832e-877f-450f-9d1a-29f5235fec7b`)
- S32: [图6.2-7 施主-受主流量法示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ac0e5cb-5264-436e-9ac4-37ed61e5dc36/resource) (`8ac0e5cb-5264-436e-9ac4-37ed61e5dc36`)