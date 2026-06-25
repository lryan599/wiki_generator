---
version: "v1"
generated_at: "2026-06-18T12:54:19+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 43
  source_quality_score: 0.85
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

Hall-Petch公式（Hall-Petch equation），又称Hall-Petch准则、Hall-Petch关系、哈-佩公式、晶界强化经验关系，是20世纪50年代由E. O. Hall和N. J. Petch基于大量金属力学试验归纳得到的，描述多晶材料屈服强度与晶粒尺寸之间定量关联的核心公式。该公式是细晶强化（晶界强化）的理论基础[[S29,S12,S2]]。

## 定义与公式形式

Hall-Petch公式的标准形式为[[S30,S41,S4,S29]]：

$$ \sigma_y = \sigma_0 + k \cdot d^{-1/2} $$

式中各符号的物理意义与典型单位如下表所示：

| 符号 | 名称 | 物理意义 | 单位 |
|------|------|----------|------|
| $\sigma_y$ | 屈服强度 | 多晶材料的宏观屈服强度 | MPa |
| $\sigma_0$ | 摩擦阻力（派纳力） | 与晶粒尺寸无关的强度分量，本质是完整晶格对位错均匀滑移的固有阻力，数值接近对应单晶体的屈服强度，随材料成分、测试温度变化[[S12,S32,S2]] | MPa |
| $k$（或 $k_y$） | Hall-Petch系数（晶界锁止系数） | 表征位错从一个晶粒穿越晶界传导到相邻晶粒的难度，数值与晶界结构、材料晶体类型直接相关[[S12,S32,S46,S48]] | MPa·μm¹/² |
| $d$ | 平均晶粒直径 | 材料的平均晶粒尺寸 | μm |

该线性关系在常规晶粒尺寸区间可同时适配屈服强度、不同应变下的流变应力、断裂应力的晶粒尺寸依赖规律[[S29,S2,S32,S48]]。面向特定应变 $\varepsilon$ 的推广形式为 $\sigma_\varepsilon = \sigma_{0\varepsilon} + k_\varepsilon l^{-1/2}$，其中 $\sigma_{0\varepsilon}$ 为该应变下的晶格摩擦应力，$k_\varepsilon$ 为对应应变下的晶粒尺寸强化系数[[S33]]。

## 物理机制

Hall-Petch公式的核心物理基础是经典位错堆积模型（dislocation pile-up model）。其作用过程如下[[S2,S12,S5,S25]]：

1. **位错源启动**：当施加外部应力时，晶粒内的位错源（如Frank-Read源）启动，生成位错并沿滑移面向晶界运动。
2. **晶界阻碍**：由于晶界两侧晶粒位向不同、滑移系取向不适配，运动位错无法直接穿越晶界，在晶界处逐步堆积，形成位错塞积群（pile-up group），其长度正比于晶粒直径 $d$。
3. **应力集中传递**：塞积群在晶界尖端产生的应力集中随塞积位错数目增大而升高，当该应力足够激活相邻晶粒内的位错源时，宏观材料发生整体屈服。

细晶强化的本质在于：晶粒越细小，相同外部应力下单个晶粒内容纳的位错塞积数目越少，位错塞积产生的尖端应力集中程度越低，因此需要更大的外部加载应力才能触发宏观塑性变形。同时，晶粒细化后单位体积内的晶界总占比大幅升高，晶界对位错运动的总阻碍作用显著提升[[S5,S7,S36]]。细晶强化是唯一能同时提高材料强度、塑性和韧性的强化方法[[S36]]。

## Hall-Petch参数与典型数据

### 压铸铝合金与镁合金的Hall-Petch系数

不同晶体结构的金属其Hall-Petch系数 $k$ 值差异显著。体心立方金属的 $k$ 值通常远高于面心立方金属[[S12,S32,S46,S48]]。镁合金因密排六方（HCP）结构滑移系少，晶粒细化提升强度的效果显著优于面心立方（FCC）结构的铝合金[[S31]]。

| 材料体系 | Hall-Petch系数 $k$（MPa·μm¹/²） | 说明 | 来源 |
|----------|-------------------------------|------|------|
| 铝合金（FCC） | ≈68 | 滑移系数量多，取向因子小 | [[S31]] |
| 压铸铝合金 | ≈68 | 高压铸造免热处理铝合金适用 | [[S27]] |
| 镁合金（HCP） | 280~320 | 滑移系少，取向因子大 | [[S31]] |
| 压铸镁合金 | ≈220 | 耦合铸态组织特征 | [[S27,S5]] |

### 高压压铸AZ91D镁合金的实测关系

高压压铸态AZ91D镁合金的实测Hall-Petch拟合公式为[[S40,S14]]：

$$ \text{TYS} = 75.7 \ \text{MPa} + 257.1 \ \text{MPa·μm}^{1/2} \cdot d^{-1/2} $$

其中 $\sigma_0 = 75.7$ MPa，$k = 257.1$ MPa·μm¹/²。商用高压压铸态AZ91D的典型晶粒尺寸范围为5~100 μm，对应凝固冷却速率范围为10~1000 ℃/s，铸件近模壁区域晶粒尺寸远小于厚大心部区域[[S14]]。晶粒细化是高压压铸镁合金最主要的强化机制[[S14,S40]]。

![高压压铸AZ91D合金的屈服强度-晶粒尺寸Hall-Petch关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c761c80a-aa0e-4a27-8eb7-c75a3530061b/resource)

上图展示了AZ91D镁合金拉伸屈服强度（TYS）与晶粒直径平方根倒数的线性关系，包含多组不同研究的实测数据点，拟合公式为TYS = 75.7 + 257.1·d⁻¹/²，直观验证了Hall-Petch定律在高压压铸镁合金中的适用性[[S40]]。

### 压铸工艺引起的细晶强化增量实例

| 材料 | 工艺对比 | 细晶强化增量（MPa） | Hall-Petch参数 | 来源 |
|------|----------|---------------------|---------------|------|
| Mg-9Al-2Si-0.5Ca-0.2Ce-0.2Mn | 亚快速凝固 vs 重力铸造 | 11.0 | $k=235$ MPa·μm¹/² | [[S37,S44]] |
| Mg-9Al-2Si-0.5Ca-0.2Ce-0.2Mn | 挤压铸造 vs 重力铸造 | 8.8 | $k=235$ MPa·μm¹/² | [[S37,S44]] |
| AZ80-0.5Ce镁合金 | 压射比压60 MPa vs 40 MPa | 从218 MPa提升至252 MPa（总提升34 MPa） | 晶粒尺寸从13.8 μm降至10.0 μm | [[S42]] |
| AZ81镁合金（添加Ti颗粒细化） | Ti细化 vs 未细化 | 10.5 | $k=0.13$ MN·m⁻³/² | [[S51,S38]] |

## 适用范围与局限性

### 经典Hall-Petch公式的位错塞积前提

经典Hall-Petch公式的推导前提是晶粒内容纳至少50个以上的位错形成塞积群。当晶粒尺寸降低到20 nm以下的纳米晶区间时，晶粒无法容纳足够数量的位错完成塞积，此时公式不再成立[[S12,S28]]。

### 反Hall-Petch效应

反Hall-Petch效应（Inverse Hall-Petch effect）指屈服强度随晶粒尺寸进一步减小反而下降的反常规律。该效应已在纳米晶Cu、Pd、Ni-P等材料中被实验观测证实[[S28,S6]]。

反Hall-Petch效应的核心产生机理包括[[S28,S13,S16]]：

1. 晶粒尺寸过小后无法在晶粒内部形成满足要求的位错塞积群；
2. 高占比的晶界发生弛豫，晶界滑移、晶界扩散蠕变成为主导变形机制，弱化了晶界的阻碍强化作用；
3. 纳米尺度下非晶相占比提升，晶界强化效应趋近消失。

已提出的解释模型包括晶界蠕变模型、临界晶粒尺寸模型、改进的位错网模型和三晶粒结点模型[[S28,S13]]。

### 不同材料体系的临界晶粒尺寸

Hall-Petch关系失效的临界晶粒尺寸下限随材料体系不同存在差异[[S8,S1]]：

| 材料体系 | 临界晶粒尺寸 | 说明 | 来源 |
|----------|-------------|------|------|
| 常规多晶体系 | 10~20 nm | 低于此尺寸出现反Hall-Petch效应 | [[S8]] |
| Fe-Mo-Si-B纳米晶合金 | 47 nm | 低于47 nm后强度随晶粒细化持续降低 | [[S8]] |

### 压铸铸态组织非均匀性的影响

压铸场景下典型非均匀铸态组织（枝晶结构、溶质元素偏析、不同尺寸多相混合、气孔/孔隙分布不均）的存在会导致简单使用平均晶粒尺寸代入Hall-Petch公式计算时产生偏差，无法直接套用常规均匀组织的Hall-Petch公式[[S39,S47,S11]]。

针对多尺度非均匀铸态组织，可采用加权平均的Hall-Petch修正公式降低计算误差[[S5,S3]]：

$$ \sigma_{gs} = \sigma_0 + f_1 \cdot k \cdot d_1^{-1/2} + f_2 \cdot k \cdot d_2^{-1/2} + \dots $$

式中 $f_1$、$f_2$ 分别为不同特征尺寸组织对应的体积分数，$d_1$、$d_2$ 分别对应不同尺度组织的特征尺寸。该修正形式已应用于压铸镁合金的细晶强化计算，分别考虑预结晶相、共晶相、等轴细晶区的贡献[[S5,S23]]。

## 与其他强化机制的对比与耦合

### 多重强化机制的线性叠加模型

压铸金属的总屈服强度可通过线性叠加各独立强化贡献得到通用表达式[[S10,S49,S23]]：

$$ \sigma_{total} = \sigma_0 + \sigma_{ss} + \sigma_{HP} + \sigma_{precipitation} + \sigma_{texture} $$

式中各分项含义如下：

| 项 | 名称 | 物理意义 | 来源 |
|----|------|----------|------|
| $\sigma_0$ | 晶格摩擦应力 | 基体晶格对位错运动的固有阻力 | [[S10,S49,S23]] |
| $\sigma_{ss}$ | 固溶强化贡献 | 溶质原子引发的晶格畸变对位错的阻碍 | [[S10,S49,S23]] |
| $\sigma_{HP}$ | 细晶强化贡献 | Hall-Petch晶界强化，$\sigma_{HP} = k \cdot d^{-1/2}$ | [[S10,S49,S23]] |
| $\sigma_{precipitation}$ | 沉淀/第二相强化贡献 | 析出相或弥散相对位错运动的阻碍 | [[S10,S49,S23]] |
| $\sigma_{texture}$ | 织构强化贡献 | 晶体择优取向对强度的影响 | [[S10,S49,S23]] |

该线性叠加模型已被压铸铝合金、压铸镁合金的实测结果验证[[S10,S49,S23]]。

### 压铸条件下固溶强化的辅助计算

压铸非平衡凝固条件下，合金元素过饱和固溶后的固溶强化贡献可采用Fleicher模型计算[[S9,S23]]：

$$ \sigma_{ss} = M \cdot (38.9) \cdot \left[\left(\frac{\varepsilon_b}{0.176}\right)^2 + \left(\frac{\varepsilon_{SFE}}{5.67}\right)^2 - \frac{\varepsilon_b \cdot \varepsilon_{SFE}}{2.98}\right]^{3/2} \cdot C_s^{1/2} $$

式中 $M$ 为泰勒因子（取4.2），$\varepsilon_b$ 为原子尺寸错配度，$\varepsilon_{SFE}$ 为层错能错配度，$C_s$ 为基体中固溶溶质的平均浓度[[S9,S23]]。

### Hall-Petch在含第二相合金中的扩展

Hall-Petch关系的适用范围可扩展至多相合金，对应特征尺寸不局限于晶粒直径。对于不同Si含量的Al-Si合金[[S26]]：

| Si含量范围 | 适用的特征尺寸 | 来源 |
|------------|---------------|------|
| 0% | 纯铝晶粒尺寸 | [[S26]] |
| 1.6%~2.5% | 枝晶胞尺寸（dendrite cell size） | [[S26]] |
| 5.3%~25% | Si粒子平面中心最近邻距离 | [[S26]] |

强度随特征尺寸的-1/2次方线性增长的规律在上述范围内仍成立[[S26,S19]]。下图为过共晶Al-Si合金抗拉强度与硅晶体尺寸平方根倒数的关系[[S20]]：

![过共晶Al-Si合金抗拉强度与硅晶体尺寸平方根倒数的Hall-Petch关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79209198-b500-4434-ab9f-d2db73882e51/resource)

该图标注了不同过共晶Al-Si合金体系的拟合Hall-Petch公式，直观展示了铸态铝合金中第二相粒子间距作为等效特征尺寸时代入扩展Hall-Petch关系的细晶强化规律[[S20]]。

## 工艺关联：压铸工艺参数对Hall-Petch强化的影响

### 工艺参数–晶粒尺寸–强度链条

压铸工艺参数调控合金凝固过程的过冷度与冷却速率，进而调控铸态晶粒尺寸 $d$，通过Hall-Petch公式决定细晶强化贡献 $\sigma_{HP}$；同时压铸非平衡凝固会提升固溶度得到更高的 $\sigma_{ss}$，调控析出相尺寸与分布得到 $\sigma_{precipitation}$，叠加织构强化 $\sigma_{texture}$ 与基体摩擦项 $\sigma_0$，最终得到总屈服强度 $\sigma_{total}$。该链条可作为压铸合金力学性能正向预测的核心路径[[S50]]。

### 主要工艺参数的影响规律

| 工艺参数 | 调整方向 | 对晶粒尺寸的影响 | 对Hall-Petch强化的影响 | 来源 |
|----------|----------|-----------------|----------------------|------|
| 浇注温度 | 降低 | 缩短凝固时间，提升冷却速率，细化晶粒 | 增大 $\sigma_{HP}$ | [[S22]] |
| 增压压力 | 增大 | 增大凝固过冷度，促进形核，细化α-Al/α-Mg晶粒，抑制粗大第二相析出 | 增大 $\sigma_{HP}$ | [[S22,S14]] |
| 模具温度 | 降低 | 提升铸件与模壁的换热效率，加速冷却 | 得到更细小的铸态晶粒，增大 $\sigma_{HP}$ | [[S22,S14]] |
| 压射比压 | 增大（40→60 MPa） | AZ80-0.5Ce平均晶粒尺寸从13.8 μm降至10.0 μm | 屈服强度从218 MPa提升至252 MPa | [[S42]] |
| 冷却速率 | 增大（60→125 ℃/s） | 显著减小晶粒尺寸 | AlSi9Cu3合金变形5%对应的强度从261 MPa提升至335 MPa | [[S22]] |

### 特殊压铸工艺的细晶强化收益

- **半固态流变压铸**：7075铝合金流变压铸的平均晶粒尺寸明显低于普通压铸，可通过Hall-Petch公式计算得到对应的屈服强度提升量[[S24]]。
- **真空压铸**：相比常规压铸，晶界强化贡献提高Δσ = 7.3 MPa（LA42镁合金实例），配合固溶强化增量2.6 MPa，总屈服强度从146.2 MPa提高至154.7 MPa[[S23]]。
- **亚快速凝固/挤压铸造**：通过显著提高凝固冷速或施加凝固压力，使镁合金的细晶强化贡献达到8.8~11.0 MPa[[S37,S44]]。

商用高压压铸铝合金的典型晶粒尺寸范围为5~20 μm，无明显择优取向，可通过添加Ti、Mn等晶粒细化剂进一步降低晶粒尺寸，进而通过Hall-Petch机制提升屈服强度[[S50]]。

## Sources
- S29: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c435213-1498-473e-9af5-7ac769277e1a/resource) (`9c435213-1498-473e-9af5-7ac769277e1a`)
- S12: [金属塑性成形理论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a14a547-931c-4e2e-a688-4e7f031394ae/resource) (`5a14a547-931c-4e2e-a688-4e7f031394ae`)
- S2: [elements of physical metallurgy__5d4ee92381](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0cdf5efb-9c4d-4ac2-b30e-46f5811a0ee4/resource) (`0cdf5efb-9c4d-4ac2-b30e-46f5811a0ee4`)
- S30: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9fbf11fe-984a-4828-85f7-0303abfddd45/resource) (`9fbf11fe-984a-4828-85f7-0303abfddd45`)
- S41: [铝合金组织细化用中间合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c7641aac-8540-4bf1-ae62-2d518a126640/resource) (`c7641aac-8540-4bf1-ae62-2d518a126640`)
- S4: [elements of physical metallurgy__5d4ee92381](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f4b3bb0-c99b-4fe1-a577-eacefb961693/resource) (`1f4b3bb0-c99b-4fe1-a577-eacefb961693`)
- S32: [机械制造基础工程材料及热加工工艺基础上册第2版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a119e6bf-cb7f-4522-8b79-2e828d66c818/resource) (`a119e6bf-cb7f-4522-8b79-2e828d66c818`)
- S46: [alloy steels__2699141544](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3f42983-a05d-401b-b660-c92eb7197897/resource) (`e3f42983-a05d-401b-b660-c92eb7197897`)
- S48: [an introduction to metallurgy__8ba3cc7781](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e63e56a3-1461-45bb-90b9-5466b72328e2/resource) (`e63e56a3-1461-45bb-90b9-5466b72328e2`)
- S33: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad56cf71-c880-4935-b341-c7b4d73ddaef/resource) (`ad56cf71-c880-4935-b341-c7b4d73ddaef`)
- S5: [9694803_细晶强化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cfb290b-5634-496a-9b54-51a7a2e39f3a/resource) (`2cfb290b-5634-496a-9b54-51a7a2e39f3a`)
- S25: [金属塑性成形理论高](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/88749653-1631-4897-98a1-af7c6d8c520c/resource) (`88749653-1631-4897-98a1-af7c6d8c520c`)
- S7: [细晶镁合金制备方法及组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/46d2d225-d4a8-43ca-b75c-f0181f132e2a/resource) (`46d2d225-d4a8-43ca-b75c-f0181f132e2a`)
- S36: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7814263-1b18-47e1-ade1-db6b32e31b5f/resource) (`b7814263-1b18-47e1-ade1-db6b32e31b5f`)
- S31: [镁合金熔体氧化孕育细化行为及其机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a08104f3-de36-4fc9-965b-601e30c2597e/resource) (`a08104f3-de36-4fc9-965b-601e30c2597e`)
- S27: [高压铸造免热处理铝合金的组织和力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e14aec4-d528-4be3-b1ae-538358e23e29/resource) (`8e14aec4-d528-4be3-b1ae-538358e23e29`)
- S40: [图 4：镁合金 AZ91D 的拉伸屈服强度与晶粒直径的 Hall-Petch 关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c761c80a-aa0e-4a27-8eb7-c75a3530061b/resource) (`c761c80a-aa0e-4a27-8eb7-c75a3530061b`)
- S14: [advancements in high pressure die casting of magnesium__5528302407](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ae1c749-504d-4d5f-adfc-2f3dec0ae3d2/resource) (`5ae1c749-504d-4d5f-adfc-2f3dec0ae3d2`)
- S37: [Mg-Al-Si系合金凝固与时效组织演化及力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b957e810-9d62-4847-94bd-68c580688f89/resource) (`b957e810-9d62-4847-94bd-68c580688f89`)
- S44: [Mg-Al-Si系合金凝固与时效组织演化及力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d808a448-e645-4179-b9c8-58ba8cf3b2e2/resource) (`d808a448-e645-4179-b9c8-58ba8cf3b2e2`)
- S42: [执手多型腔压铸工艺及模具优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c76e09fa-cc5a-4b29-b538-19316f26842e/resource) (`c76e09fa-cc5a-4b29-b538-19316f26842e`)
- S51: [Ti颗粒增强AZ81基复合材料的制备及组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe40bedf-828d-486e-bf78-8126ad733cba/resource) (`fe40bedf-828d-486e-bf78-8126ad733cba`)
- S38: [Ti颗粒增强AZ81基复合材料的制备及组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c46b1b73-0a6d-45ea-af62-c81f4e9a39b4/resource) (`c46b1b73-0a6d-45ea-af62-c81f4e9a39b4`)
- S28: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99389931-064c-4258-a9ae-f090a466d5b5/resource) (`99389931-064c-4258-a9ae-f090a466d5b5`)
- S6: [铁铝基纳米复相金属间化合物材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43083b23-5d12-4b4f-994f-e0e7d2819819/resource) (`43083b23-5d12-4b4f-994f-e0e7d2819819`)
- S13: [amorphous nanocrystalline alloys__7757af2db0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ab37bc9-2c72-465c-9e4c-6f53261295e1/resource) (`5ab37bc9-2c72-465c-9e4c-6f53261295e1`)
- S16: [结构钢与铝合金塑性变形的微观机制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/608e8268-75e9-4069-bc6f-3a51c124283a/resource) (`608e8268-75e9-4069-bc6f-3a51c124283a`)
- S8: [amorphous nanocrystalline alloys__7757af2db0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a9e840d-3309-4266-a1d1-9d3284c249aa/resource) (`4a9e840d-3309-4266-a1d1-9d3284c249aa`)
- S1: [0202_1289394ad9dd0e9e_陶瓷工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07a4d041-36ae-4378-9bc0-28d255673f0e/resource) (`07a4d041-36ae-4378-9bc0-28d255673f0e`)
- S39: [design perspectives for creep resistant magnesium die casting alloys__2a57842716](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c64c5db9-1e08-48c1-a6ea-f82c7bd31120/resource) (`c64c5db9-1e08-48c1-a6ea-f82c7bd31120`)
- S47: [冷却速率对6005A、7N01和7A99铝合金组织及性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e604bd9e-b04b-43e7-8284-2ba3727fba0e/resource) (`e604bd9e-b04b-43e7-8284-2ba3727fba0e`)
- S11: [Cu对搅拌摩擦加工高锌镁合金性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/586321ff-327a-448e-9690-66df985042fb/resource) (`586321ff-327a-448e-9690-66df985042fb`)
- S3: [微量纳米颗粒调控铝合金热成形微观组织演变机制__part01_p001-199](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d039fb8-5584-461d-88d1-61aee04be6df/resource) (`1d039fb8-5584-461d-88d1-61aee04be6df`)
- S23: [真空压铸对LA42镁合金热导率和力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8411037d-9e6f-4c24-9a29-e9d389aca035/resource) (`8411037d-9e6f-4c24-9a29-e9d389aca035`)
- S10: [乘用车轻量化及微合金化钢板的应用lightweightofpassengercarandniobiummicroalloyingsteel](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/54d553f2-b8c8-4bae-948a-b6e626fde636/resource) (`54d553f2-b8c8-4bae-948a-b6e626fde636`)
- S49: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f15e53d5-279b-4c2b-8fcd-bd74d0c45006/resource) (`f15e53d5-279b-4c2b-8fcd-bd74d0c45006`)
- S9: [92286_固溶强化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ab6a1b0-78b2-4eed-a41e-64dd10d108e8/resource) (`4ab6a1b0-78b2-4eed-a41e-64dd10d108e8`)
- S26: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8cdd164d-d074-417c-bae9-60ae3a797650/resource) (`8cdd164d-d074-417c-bae9-60ae3a797650`)
- S19: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7885322d-546b-47fd-a4a9-2b3c0134abde/resource) (`7885322d-546b-47fd-a4a9-2b3c0134abde`)
- S20: [Relationship between tensile strength and inverse square root of silicon crystal size for hypereutectic Al-Si alloys](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79209198-b500-4434-ab9f-d2db73882e51/resource) (`79209198-b500-4434-ab9f-d2db73882e51`)
- S50: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f55e9f2d-789c-4eef-bcd1-a514e16e7ec0/resource) (`f55e9f2d-789c-4eef-bcd1-a514e16e7ec0`)
- S22: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/833162ef-324c-42c8-b130-ad937f83897a/resource) (`833162ef-324c-42c8-b130-ad937f83897a`)
- S24: [图6.5 流变压铸和普通压铸件的晶粒尺寸曲线图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8581ea82-a1dc-4fbc-a800-59952748f42c/resource) (`8581ea82-a1dc-4fbc-a800-59952748f42c`)