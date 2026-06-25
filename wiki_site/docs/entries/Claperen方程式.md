---
version: "v1"
generated_at: "2026-06-18T14:04:06+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 40
  source_quality_score: 0.86
  freshness_score: 0.73
  evidence_coverage_score: 1.0
---

## 正名

“Claperen”是标准命名 **Clapeyron** 的常见拼写变体或笔误，不存在独立命名为 Claperen 的专属相变热力学方程。所有指向该名称的相变平衡关系均对应 **Clapeyron 方程**（克拉佩龙方程）。[[S19,S43]]

正确的中文规范名称：
- **克拉佩龙方程**（原始未引入近似的基础形式）
- **克拉佩龙–克劳修斯方程**（含气相近似的简化形式）
- **克劳修斯–克拉佩龙方程**（俗称“饱和蒸气压公式”）

对应英文别名包括：Clapeyron’s equation、Clapeyron–Clausius equation、Clausius–Clapeyron relation。[[S9,S40,S27,S21,S22]]

---

## 概述

克拉佩龙方程是热力学中描述 **单组分体系任意两相平衡** 时平衡压力与相变温度关系的核心基础公式，属于化学热力学与相变理论的核心内容。方程的原始推导由 Clapeyron 提出，后由 Clausius 完成含气相近似的补充与优化。[[S8,S3,S37,S29]] 在压铸领域，该方程是定量描述压力对金属/合金凝固点影响的核心理论基础。[[S9,S39,S7,S36,S10]]

---

## 定义与数学表达式

克拉佩龙方程在平衡相变 \( \alpha \rightarrow \beta \) 条件下的标准微分形式为：[[S9,S40,S43,S20]]

\[
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{\Delta_{\alpha}^{\beta} H_{\mathrm{m}}}{T \;\Delta_{\alpha}^{\beta} V_{\mathrm{m}}}
\]

式中：
- \( \frac{\mathrm{d}p}{\mathrm{d}T} \) — 相平衡条件下平衡压力随温度的变化率；
- \( \Delta_{\alpha}^{\beta} H_{\mathrm{m}} \) — 由 \( \alpha \) 相向 \( \beta \) 相转变的摩尔相变潜热；
- \( T \) — 相变对应的绝对热力学温度；
- \( \Delta_{\alpha}^{\beta} V_{\mathrm{m}} \) — \( \alpha \) 相与 \( \beta \) 相之间的摩尔体积差。[[S9,S21,S43]]

**应用于固–液熔化（凝固）过程的改写形式：**

描述外压对熔点影响的克拉佩龙方程为：[[S9,S40,S16]]

\[
\frac{\mathrm{d}T}{\mathrm{d}p} = \frac{T \;\Delta_{\mathrm{fus}} V_{\mathrm{m}}}{\Delta_{\mathrm{fus}} H_{\mathrm{m}}}
\]

**压铸/挤压铸造常用针对凝固过程的实用形式：**

\[
\frac{\mathrm{d}T_{\text{熔}}}{\mathrm{d}p} = \frac{T_{\text{熔}} \,(v_{\text{液}} - v_{\text{固}})}{Q_{\text{熔}}}
\]

在低压区间内的近似计算式为：[[S25,S26,S9]]

\[
\Delta T_{\text{熔}} = \frac{T_{\text{熔}} \,(v_{\text{液}} - v_{\text{固}})}{Q_{\text{熔}}} \,\Delta p
\]

式中：
- \( p \) — 压力（MPa）；
- \( T_{\text{熔}} \) — 金属或合金在常压下的熔点（K）；
- \( v_{\text{液}} \)、\( v_{\text{固}} \) — 单位质量液相、固相金属的体积（m³/kg）；
- \( Q_{\text{熔}} \) — 单位质量金属的熔化潜热（J）。

---

## 核心参数与物理意义

### 体积变化方向决定压力对熔点的定性影响

熔化时凝固体积收缩的金属满足 \( v_{\text{液}} - v_{\text{固}} > 0 \)，代入方程得 \( \frac{\mathrm{d}T}{\mathrm{d}p} > 0 \)，压力升高时熔点/凝固点同步升高。绝大多数常见金属与压铸合金属于此类型，如铝、铁、镁、铜、镍、锡、铅、锌、镉。[[S9,S46,S34]]

熔化时体积膨胀的反常金属满足 \( v_{\text{液}} - v_{\text{固}} < 0 \)，代入方程得 \( \frac{\mathrm{d}T}{\mathrm{d}p} < 0 \)，压力升高时凝固点反而降低。典型实例包括水、铋、锑、硅、Fe–石墨共晶合金。[[S9,S10,S46,S6]]

上述物理本质可总结为：**相变过程中增加压力有促进形成比体积小的相、阻碍形成比体积大的相的作用**。[[S25,S28]]

### 潜热与体积变化

\( Q_{\text{熔}} \) 越大或 \( \Delta v \) 越小，熔点对压力变化的灵敏度越低。在低压力区间，金属熔点与压力呈线性关系，\( \frac{\mathrm{d}T_{\text{熔}}}{\mathrm{d}p} \) 近似为常数。[[S28,S25]]

---

## 克劳修斯–克拉佩龙方程（简化形式）

### 推导与适用条件

原始克拉佩龙方程在推导过程中未引入任何关于共存相性质的假定，可适用于单组分体系的 **任意两相平衡**（固–固、固–液、固–气、液–气）。[[S9,S40]]

对于有气相参与的相平衡（蒸发、升华），引入两项假设后可得到简化形式：[[S9,S27,S21,S11,S30,S29]]

1. 凝聚相（固态/液态）的摩尔体积远小于气相的摩尔体积，近似忽略；
2. 气相满足理想气体状态方程 \( pV_{\mathrm{m}} = RT \)。

简化后得到克劳修斯–克拉佩龙方程的微分形式：

\[
\frac{\mathrm{d} \ln p}{\mathrm{d} T} = \frac{\Delta_{\text{vap}} H_{\mathrm{m}}}{R T^{2}}
\]

定积分后：

\[
\ln \frac{p_2}{p_1} = \frac{\Delta_{\text{vap}} H_{\mathrm{m}}}{R} \left( \frac{1}{T_1} - \frac{1}{T_2} \right)
\]

### 适用限制

克劳修斯–克拉佩龙简化形式仅适用于 **有气相参与的相平衡**（蒸发、升华），且要求压力低于约 1 mbar、温度远离物质临界点（建议 \( T < T_c - 30\;\mathrm{K} \)），在临界区域内该近似不再成立。[[S9,S18,S30]]

可扩展应用于等量吸附热的测定：在保持吸附量不变的条件下，通过 \( \ln p \) 对 \( 1/T \) 的线性拟合，由斜率计算等量吸附热，等效于将吸附视为气体在固体表面液化的相变过程。[[S22]]

---

## 工艺作用：压力对压铸合金凝固点的影响机制

### 凝固过冷度与形核细化

在压铸与挤压铸造工艺中，施加的高压通过克拉佩龙效应抬升合金的固相线、液相线位置，产生的凝固过冷度增量可按下式计算：[[S31]]

\[
\Delta T_{\mathrm{L}} = \frac{T_{\mathrm{L}} \,(V_{\mathrm{L}} - V_{\mathrm{s}})}{Q_{\mathrm{L}}} \,\Delta p
\]

压力升高可获得更大的过冷度，降低临界形核尺寸，促进大量形核，从而细化铸件晶粒。[[S31]]

### 强制补缩与缺陷削减

高压驱动金属液穿透树枝晶通道实现强制补缩，显著降低缩松、缩孔缺陷；同时压力提升带来的额外凝固过冷度可收窄合金凝固区间，降低热裂倾向性，最终获得组织致密的优质铸件。[[S24,S42,S5,S32]]

### 界面换热强化

压力可强化金属液与模具壁面的接触，减小界面空气间隙，提升界面换热效率，加快凝固速度并进一步细化组织。[[S39,S31,S41]]

---

## 工艺参数（实测数据）

### 纯金属压力–熔点变化系数

以下数据来源于挤压铸造领域权威文献：[[S44,S1]]

| 金属 | 熔点 \( T_{\text{熔}} \) / ℃ | \( \frac{\mathrm{d}T_{\text{熔}}}{\mathrm{d}p} \)\ 计算值<br>(10⁻³ ℃·cm²/kg) | \( \frac{\mathrm{d}T_{\text{熔}}}{\mathrm{d}p} \)\ 实验值<br>(10⁻³ ℃·cm²/kg) | 结晶体积变化率 / % |
|:---:|:---:|:---:|:---:|:---:|
| 镉 | 320 | +5.9 | +6.2 | −5.64 |
| 铝 | 660 | +5.59 | +6.4 | −6.5 |
| 铁 | 1539 | +2.7 | +3.0 | −2.2 |
| 镁 | 650 | +6.3 | +7.5 | −5.1 |
| 铜 | 1083 | +3.3 | +4.2 | −4.1 |
| 镍 | 1455 | +2.6 | +3.7 | — |
| 锡 | 232 | +3.2 | +4.3 | −2.8 |
| 铅 | 327 | +8.3 | +11.0 | −3.5 |
| 锌 | 419 | +3.7 | +4.5 | −4.2 |
| 铋 | 271 | −3.6 | −0.38 | +3.3 |
| 锑 | 630 | −2.8 | −0.5 | +0.95 |
| 硅 | 1430 | −5.8 | — | — |

> 注：正值表示增压使熔点升高，负值表示增压使熔点降低。

### 共晶合金压力–熔点变化系数

| 共晶合金系 | \( \frac{\mathrm{d}T_{\text{熔}}}{\mathrm{d}p} \)\ 计算值<br>(10⁻³ ℃·cm²/kg) | 实验值 |
|:---|:---|:---|
| Al–Si 共晶合金 | +2.6 ~ +3.0 | +3.1 ~ +3.4（Al–12%Si 柱塞挤压铸造）[[S28,S23,S6]] |
| Fe–Fe₃C 共晶合金 | +4.0 | — [[S10,S23]] |
| Fe–石墨共晶合金 | −2.34 | — [[S10,S23]] |

### 压力–熔点变化量的具体算例

- **1000 kg/cm²（约98.1 MPa）** 下，Al–Si 共晶温度升高约 **7.5 ℃**；1500 kg/cm²（约147 MPa）下纯铝熔点上升约 **11 ℃**。[[S24,S38,S6,S13]]
- **1000 kg/cm²** 下纯铝熔点升高 **5.69 K**，20 碳钢在相同压力下熔点升高 **2.65 K**。[[S38,S10]]

---

## 与合金相图的关联

压力不仅改变熔点，还导致合金状态图中 **共晶点**、**固相线**、**液相线** 发生移动。以 Al–Si 系为例：

- 常压下共晶温度 577 ℃，压力升至 1000 MPa 时共晶温度升至 640 ℃，2500 MPa 时达 677 ℃；[[S13]]
- 共晶成分随压力升高向富硅方向移动，压力升至 5000 MPa 时共晶成分由常压下的 Al–12%Si 增至约 30%Si（原子分数）；[[S23,S6]]
- 硅在铝中固溶体的 \( \alpha \) 相区随压力扩大，最大固溶点（A）同共晶点一样向高温、富硅方向移动。[[S23]]

在 Fe–C 系中，压力升高使 Fe–Fe₃C 共晶点向高温方向移动，而 Fe–石墨共晶点向温度降低和富碳方向移动；共析点（S 点）则向温度降低和碳含量降低的方向移动。[[S23,S4]]

---

## 相关概念辨析

### Clapeyron 方程与 Clausius–Clapeyron 方程的区别

| 对比维度 | 克拉佩龙方程 | 克劳修斯–克拉佩龙方程 |
|:---|:---|:---|
| 推导假设 | 无任何相性质假定 | ① 忽略凝聚相体积<br>② 气相视为理想气体 |
| 适用范围 | 单组分体系任意两相平衡 | 仅限有气相的相平衡（蒸发、升华） |
| 压铸应用形式 | \( \frac{\mathrm{d}T}{\mathrm{d}p} = \frac{T (v_l - v_s)}{Q_m} \) | 不适用于固–液相变计算 |
| 压力条件 | 无特殊限制 | 建议 \( p < 1 \)\ mbar，远离临界点 |

> 二者为同一理论体系的 **原始形式** 与 **简化形式** 关系，并非独立方程。[[S9,S40,S43]]

---

## 局限性

1. **理想热力学平衡假设**：方程基于相平衡条件下吉布斯自由能相等的严格推导，对非平衡快速凝固过程的适用性需谨慎评估。[[S9,S40]]
2. **物性参数恒定性**：推导过程中假定在考虑温度范围内相变潜热 \( Q_{\text{熔}} \)、体积差 \( \Delta v \) 近似不变，实际高温高压下潜热与密度均随温度与压力变化。[[S9,S28]]
3. **多元合金凝固适用性限制**：方程严格适用于单组分体系两相平衡；工业压铸合金系多组元、凝固区间宽的合金体系，不同相析出次序与溶质偏析会造成局部成分与相变温度偏离简单方程预测。[[S9,S40]]
4. **克劳修斯–克拉佩龙形式限制**：简化形式不适用于高压、近临界区或含缔合作用的蒸气体系。[[S18,S30]]

---

## 图示

### 纯金属熔点随压力变化曲线

多种典型纯金属在低压力区间的熔点与压力呈线性关系：Al、Zn、Pb、Sn 的熔点随压力升高而上升，Sb 的熔点随压力升高而下降，与克拉佩龙方程符号判断一致。[[S12]]

![图 多种典型纯金属熔点随压力变化曲线（压力不高于5×10⁴ MPa区间）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38b65e0f-2ef0-4adf-bb24-5ac909499447/resource)

Fe、Ni、Cu 三种压铸常用基体纯金属的熔点同样随压力升高呈线性上升趋势，可补充说明铁族常用压铸金属的压力–熔点变化特征。[[S35]]

![图 Fe、Ni、Cu纯金属熔点随压力变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4896ceb-406c-4466-8905-32bc3c8e530e/resource)

### 压力对合金相图的影响

压力升高可使 Al–Si 合金共晶点向高温、富硅方向移动，使 Fe–石墨共晶合金共晶点向低温方向移动；对于 Fe–C 合金，压力升高时 Fe–Fe₃C 体系共析点向温度降低、碳含量降低的方向移动，固相线和液相线发生整体偏移。[[S4]]

![图 不同压力下Fe–C合金相图共析点附近固相线/液相线偏移示意](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19dd581c-10a1-481a-a0eb-bee36201609c/resource)

## Sources
- S19: [a concise encyclopedia of metallurgy__7738f01cf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5e27ea0c-7100-4359-8fc8-33ba4d818b18/resource) (`5e27ea0c-7100-4359-8fc8-33ba4d818b18`)
- S43: [chemical metallurgy principles and practice__65ecbc7c8d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df1984c3-25e3-4162-b7bb-2af9d65d330a/resource) (`df1984c3-25e3-4162-b7bb-2af9d65d330a`)
- S9: [物理化学机械热加工及金属材料专业用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2be4ec6a-454f-4a63-b25f-f99852e02e26/resource) (`2be4ec6a-454f-4a63-b25f-f99852e02e26`)
- S40: [物理化学机械热加工及金属材料专业用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc2d3fb5-67be-4cfc-8977-2d06a166196a/resource) (`cc2d3fb5-67be-4cfc-8977-2d06a166196a`)
- S27: [物理化学机械热加工及金属材料专业用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/865f3594-70d6-44a6-a937-a110fdbbe51c/resource) (`865f3594-70d6-44a6-a937-a110fdbbe51c`)
- S21: [表面与薄膜处理技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/689f4cf8-222e-4865-b18c-a2536e8727c4/resource) (`689f4cf8-222e-4865-b18c-a2536e8727c4`)
- S22: [表面预处理实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71227596-6a4a-4ef7-b33e-bab68b4013f7/resource) (`71227596-6a4a-4ef7-b33e-bab68b4013f7`)
- S8: [物理化学机械热加工及金属材料专业用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b6d9448-77b5-43c2-993c-e3c901313436/resource) (`2b6d9448-77b5-43c2-993c-e3c901313436`)
- S3: [5936757_相变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19857dbf-0ec6-458f-b415-e88617ad38e2/resource) (`19857dbf-0ec6-458f-b415-e88617ad38e2`)
- S37: [crystallographic data on metal and alloy structures__c4e1b3d1b7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf770e31-5b58-4b3e-9e4c-012fbf7180da/resource) (`bf770e31-5b58-4b3e-9e4c-012fbf7180da`)
- S29: [an introduction to metallurgy__8ba3cc7781](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9701336b-19b6-43aa-9b5d-01b6dbcb721e/resource) (`9701336b-19b6-43aa-9b5d-01b6dbcb721e`)
- S39: [铝、镁合金熔炼与成形加工技术.pdf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c92c8904-78ea-4920-bd11-cf85b905d119/resource) (`c92c8904-78ea-4920-bd11-cf85b905d119`)
- S7: [挤压铸造Al-Cu合金显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/28fcafea-6f8d-4a4d-b155-4f26798dc87b/resource) (`28fcafea-6f8d-4a4d-b155-4f26798dc87b`)
- S36: [挤压铸造Al-Cu合金显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/baa279bb-41a5-4f34-baec-dc9a9b8f75b8/resource) (`baa279bb-41a5-4f34-baec-dc9a9b8f75b8`)
- S10: [液态模锻与挤压铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31737003-2778-48d1-bb6b-d39f89d0fed7/resource) (`31737003-2778-48d1-bb6b-d39f89d0fed7`)
- S20: [chemical thermodynamics for process simulation__8d02380aa6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60b6f407-0b52-4782-8492-b91c09ad2d35/resource) (`60b6f407-0b52-4782-8492-b91c09ad2d35`)
- S16: [0245_a8ecdab1ef0892a6_熔点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4dff1b49-b63f-4764-bdc7-8d26913bea9d/resource) (`4dff1b49-b63f-4764-bdc7-8d26913bea9d`)
- S25: [差压铸造生产技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7edea1d4-8ac0-4ac8-87cb-03987e169a7c/resource) (`7edea1d4-8ac0-4ac8-87cb-03987e169a7c`)
- S26: [TextNode9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f22cc55-524b-4d1f-a13b-25467053cad7/resource) (`7f22cc55-524b-4d1f-a13b-25467053cad7`)
- S46: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdfce506-6317-4142-939a-6554057de495/resource) (`fdfce506-6317-4142-939a-6554057de495`)
- S34: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad940d1a-5949-47b9-947d-e6e0881c16d0/resource) (`ad940d1a-5949-47b9-947d-e6e0881c16d0`)
- S6: [差压铸造生产技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2892c50c-8382-4df9-9add-fb79ff2e8baa/resource) (`2892c50c-8382-4df9-9add-fb79ff2e8baa`)
- S28: [TextNode11](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c4a5f61-6d38-4756-9d37-a2b84b09683f/resource) (`8c4a5f61-6d38-4756-9d37-a2b84b09683f`)
- S11: [chemical thermodynamics for process simulationjurgen gmehilingbarbel kol__902a642526](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3570a532-c147-46a1-b3d9-fc70058b4b05/resource) (`3570a532-c147-46a1-b3d9-fc70058b4b05`)
- S30: [chemical thermodynamics for process simulationjurgen gmehilingbarbel kol__902a642526](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c46e93b-b7e8-4f51-a392-4219ca10512c/resource) (`9c46e93b-b7e8-4f51-a392-4219ca10512c`)
- S18: [chemical thermodynamics for process simulation__8d02380aa6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5d12ec34-081f-491f-b87a-8f3f7d6b5b2d/resource) (`5d12ec34-081f-491f-b87a-8f3f7d6b5b2d`)
- S31: [Mg-Al-Si系合金凝固与时效组织演化及力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8a619e6-65fe-49bc-bb16-f1503b1a5625/resource) (`a8a619e6-65fe-49bc-bb16-f1503b1a5625`)
- S24: [液态金属模压铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c77994d-dc3e-4ec9-af38-3461cbd69794/resource) (`7c77994d-dc3e-4ec9-af38-3461cbd69794`)
- S42: [镁合金汽车控制臂铸锻复合成形工艺的研究开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5505130-303c-45bb-bcac-403777210ac9/resource) (`d5505130-303c-45bb-bcac-403777210ac9`)
- S5: [an investigation on the microstructure and tensile properties of direct__92ab752052](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24b5801d-8da6-4220-81ac-d598b041a521/resource) (`24b5801d-8da6-4220-81ac-d598b041a521`)
- S32: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8d37ae2-b7d8-4351-8e81-0778c309fc64/resource) (`a8d37ae2-b7d8-4351-8e81-0778c309fc64`)
- S41: [铝合金大壁厚差支架挤压铸造工艺设计及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2811db8-3727-4ba1-8867-c695ab142c4e/resource) (`d2811db8-3727-4ba1-8867-c695ab142c4e`)
- S44: [常用金属熔点与附加压力的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df7d2557-c690-4502-b12e-ee3893f7be4b/resource) (`df7d2557-c690-4502-b12e-ee3893f7be4b`)
- S1: [TextNode10](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08236d39-f61e-47f3-b374-e0f7086b7c6b/resource) (`08236d39-f61e-47f3-b374-e0f7086b7c6b`)
- S23: [差压铸造生产技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/734096bb-8678-47b9-98d0-77a78221cbc8/resource) (`734096bb-8678-47b9-98d0-77a78221cbc8`)
- S38: [液态模锻与挤压铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8749c9d-07a4-4bd6-b119-07ea23c31676/resource) (`c8749c9d-07a4-4bd6-b119-07ea23c31676`)
- S13: [金属材料固-液成形理论与技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/392d51be-ec54-4087-a614-b93cbfc20e5a/resource) (`392d51be-ec54-4087-a614-b93cbfc20e5a`)
- S4: [压力对Fe-C合金相图的影响（共析点附近）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19dd581c-10a1-481a-a0eb-bee36201609c/resource) (`19dd581c-10a1-481a-a0eb-bee36201609c`)
- S12: [部分纯金属的熔点随压力变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38b65e0f-2ef0-4adf-bb24-5ac909499447/resource) (`38b65e0f-2ef0-4adf-bb24-5ac909499447`)
- S35: [Fe、Ni、Cu纯金属的熔点随压力变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4896ceb-406c-4466-8905-32bc3c8e530e/resource) (`b4896ceb-406c-4466-8905-32bc3c8e530e`)