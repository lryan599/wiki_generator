---
version: "v1"
generated_at: "2026-06-18T18:47:32+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 19
  source_quality_score: 0.82
  freshness_score: 0.94
  evidence_coverage_score: 1.0
---

修正的莫尔-库仑（MMC）断裂失效准则是由 Bai 和 Wierzbicki 提出的一种非耦合型、基于应变的延性断裂判据，通过对经典脆性 Mohr-Coulomb 准则的扩展，同时引入应力三轴度和归一化 Lode 角参数来描述金属材料在不同应力状态下的断裂行为[[S13,S2,S22]]。该准则已被大量试验验证可高精度模拟铝合金等金属材料的延性失效行为[[S13,S12,S2,S11]]。

## 数学模型

MMC 准则建立在对损伤指数 \(D\) 的定义之上：

\[
D = \int_0^{\bar{\varepsilon}} \frac{d\bar{\varepsilon}}{f(\eta, \bar{\theta})}
\]

其中 \(\bar{\varepsilon}\) 为等效应变，\(\eta\) 为应力三轴度，\(\bar{\theta}\) 为归一化 Lode 角参数。当 \(D=1\) 时材料发生断裂，此时的等效应变即为等效塑性断裂应变 \(\bar{\varepsilon}_f\)[[S7,S8]]。

完整的断裂应变表达式为[[S2,S12]]：

\[
\bar{\varepsilon}_f = \left\{ \frac{A}{c_2} \left[ c_\theta^s + \frac{\sqrt{3}}{2-\sqrt{3}} (c_\theta^{AX} - c_\theta^s) (\sec(\frac{\bar{\theta}\pi}{6})-1) \right] \left[ \frac{\sqrt{3}}{3} \cos(\frac{\bar{\theta}\pi}{6}) + c_1 \left( \eta + \frac{1}{3}\sin(\frac{\bar{\theta}\pi}{6}) \right) \right] \right\}^{-\frac{1}{n}}
\]

式中：
- \(A\) 和 \(n\) 为材料的硬化系数（抗拉强度与硬化指数）；
- \(c_1\)、\(c_2\) 和 \(c_\theta^s\) 为三个基础断裂参数；
- \(c_\theta^{AX}\) 定义为：

\[
c_\theta^{AX} = 
\begin{cases}
c_\theta^t = 1.0, & \bar{\theta} \geq 0 \\
c_\theta^c, & \bar{\theta} < 0
\end{cases}
\]

若固定 \(c_\theta^c = 1\)，则 \(c_\theta^{AX} = 1\)，模型仅含三个断裂参数 \(c_1\)、\(c_2\)、\(c_\theta^s\)，称为 **MMC3** 模型；若保留 \(c_\theta^c\) 作为独立参数以考虑断裂轨迹的非对称性，则称为 **MMC4** 模型[[S12]]。

在平面应力状态下，应力三轴度 \(\eta\) 与 Lode 角参数 \(\bar{\theta}\) 之间存在确定关系，代入后可将二元断裂曲面降维为单参数的 MMC 断裂曲线：

\[
\varepsilon^f(\eta) = \left\{ \frac{A}{C_2} f_3 \left[ \sqrt{\frac{1+C_1^2}{3}} \cdot f_1 + C_1 \left( \eta + \frac{f_2}{3} \right) \right] \right\}^{-1/n}
\]

该曲线在 \(\eta = 1/3\) 处存在不可导奇点，左右两支分段光滑[[S20,S6]]。

## 核心参数

**应力三轴度 \(\eta\)**  
定义为静水压力 \(\sigma_m\) 与 Mises 等效应力 \(\bar{\sigma}\) 的比值：

\[
\eta = \frac{\sigma_m}{\bar{\sigma}}
\]

无量纲参数 \(\eta\) 是控制金属材料孔洞形核、长大与聚合过程的核心变量，\(\eta\) 越高，等效塑性断裂应变越低，材料越易失效[[S10,S5,S7]]。

**归一化 Lode 角参数 \(\bar{\theta}\)**  
表达式为：

\[
\bar{\theta} = 1 - \frac{6\theta}{\pi}, \quad \theta = \frac{1}{3}\arccos\left( \frac{27J_3}{2\bar{\sigma}^3} \right)
\]

其中 \(J_3\) 为第三偏应力张量不变量。该参数用于表征偏应力状态的相对特征，弥补了仅用应力三轴度描述应力状态的不足[[S5,S1,S18]]。

**等效塑性断裂应变 \(\bar{\varepsilon}_f\)**  
材料发生断裂时刻对应的累积等效塑性应变，在 MMC 框架下为 \(\eta\) 与 \(\bar{\theta}\) 的二元函数。无量纲损伤积分 \(D\) 达到 1 时对应的 \(\bar{\varepsilon}\) 即为 \(\bar{\varepsilon}_f\)[[S7,S8]]。

## 与经典 Mohr-Coulomb 准则的对比

经典 Mohr-Coulomb 准则假设断裂发生时满足：

\[
\max(\tau + c_1 \sigma_n)_f = c_2
\]

仅通过断裂面上的正应力 \(\sigma_n\) 和剪应力 \(\tau\) 描述脆性断裂[[S22,S2]]。相比之下，MMC 准则有以下三方面根本改进[[S13,S22]]：

1. **适用场景拓展**：从仅适用于脆性断裂延伸至全范围延性断裂，可覆盖纯剪切、单轴拉伸、高颈拉伸等几乎所有常规金属加载路径；
2. **应力状态表征维度**：原始 MC 仅依赖断裂面上的正应力与剪应力，MMC 同时引入应力三轴度和 Lode 角两个独立维度，完整表征偏应力与静水应力对延性断裂的耦合影响；
3. **判据类型**：由应力型脆性判据变为非耦合、基于应变的断裂判据，无需引入复杂损伤演化耦合，即可直接根据应力状态获得断裂临界应变，对铝合金等工程材料的预测精度显著提高。

## 参数标定方法

以 ADC12 压铸铝合金为例，典型的标定流程包括[[S18,S8]]：

- 设计覆盖纯剪切、单轴拉伸、R5 mm 缺口拉伸、R20 mm 缺口拉伸的 4 类试样，应力三轴度范围约为 0 ~ 0.54；
- 利用 DIC 技术采集试样断裂临界时刻的等效塑性应变；
- 通过试验与有限元仿真结合，获取失效单元随时间变化的应力三轴度与 Lode 角参数，取失效时刻的平均应力三轴度；
- 将试验数据代入 MMC 表达式，采用最小二乘法拟合得到 K、C、\(C_{\theta s}\)、f、n 等 5 个系数。

## 压铸铝合金应用案例

公开文献中，针对多种压铸铝材料已完成 MMC 参数标定，下表列出两组典型参数：

| 材料 | 参数值 | 来源 |
|------|--------|------|
| ADC12（免热处理压铸铝合金） | K = 0.057 002, C = 100, \(C_{\theta s}\) = 1.486, f = 0.273 06, n = 0.127 57 | [[S8]] |
| 一体化压铸 Al-Si 合金（无缺陷理想状态） | A = 377.38 MPa, n = 0.280 2, \(C_1\) = 0.650 7, \(C_2\) = 266.22, \(C_3\) = 0.980 1 | [[S14]] |

标定后 ADC12 模型的预测精度：单轴拉伸试样断裂应变误差在 8% 以内，其余三类试样误差均低于 4%，可用于整车碰撞仿真分析[[S8]]。此外，已有针对 A356、Al-10Si-0.3Mg 高压铸造薄壁铝合金等材料的 MMC 模型应用，验证了该准则对压铸铝合金多应力状态下断裂行为的描述能力[[S9]]。

## 考虑铸造缺陷的改进 MMC 模型

传统 MMC 准则未计及压铸铝合金内部随机分布的孔隙、夹杂等缺陷，断裂应变被假定为应力状态的确定性函数。为弥补这一不足，研究者提出了改进形式[[S13,S21]]：

\[
\varepsilon_f = \varepsilon_{fi} \cdot (1 - f^{\,k})
\]

其中 \(\varepsilon_{fi}\) 为无缺陷理想状态下的 MMC 断裂应变，\(f\) 为缺陷面积比例，\(k\) 为待拟合缺陷影响指数。针对某一体化压铸 Al-Si 合金标定得到 \(k = 0.0495\)，理想 UT 试样断裂应变为 0.3473[[S13,S14]]。

## 优势与局限

MMC 准则的核心优势在于：
- 同时考虑应力三轴度与 Lode 角，预测精度高于多数同类模型；对 2024-T351 铝合金失效应变预测误差约 20%，对 TRIP 系列材料误差小于 16%[[S11]]；
- 适用应变比 \(\alpha\) 范围从 -2 延伸至 1，远大于传统 FLD 成形极限图仅覆盖的 -0.5 ~ 1 区间，可准确预测剪切诱发的断裂失效[[S13,S17]]；
- 已被集成到 LS-DYNA、Abaqus 等商用有限元平台，适用于碰撞仿真等工程场景[[S4,S13]]。

固有局限性：
- 未直接考虑内部缺陷，无法描述失效应变的随机分布特性[[S21]]；
- 平面应力 MMC 断裂曲线在 \(\eta = 1/3\) 处存在不可导奇点，奇点附近插值可能引起数值不稳定[[S6,S21]]；
- 超出标定应力三轴度区间外推时，预测误差会显著增大[[S21]]。

上述局限推动了考虑缺陷的改进 MMC 模型的发展[[S13]]。

## 三维断裂轨迹

MMC 准则在应力三轴度–Lode 角–断裂应变空间内定义了一个三维断裂曲面，直观呈现不同应力状态下材料的延性极限。平面应力状态下的投影即为分段光滑的 MMC 断裂曲线。下图为典型的 MMC 三维断裂曲面[[S3]]。

![MMC准则的应力三轴度-罗德角-断裂应变三维空间断裂曲面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2711d218-0859-4e01-b5ea-dfe0c1b41044/resource)

## Sources
- S13: [TextNode7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/897542c8-133a-42c9-80ae-8e6ea6388a49/resource) (`897542c8-133a-42c9-80ae-8e6ea6388a49`)
- S2: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c104f6e-7700-4145-be62-c2a5cbce7f89/resource) (`1c104f6e-7700-4145-be62-c2a5cbce7f89`)
- S22: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fce2679d-934a-4734-9bd7-2591ef929830/resource) (`fce2679d-934a-4734-9bd7-2591ef929830`)
- S12: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f82c037-468b-4e89-b98d-1437708f32b5/resource) (`7f82c037-468b-4e89-b98d-1437708f32b5`)
- S11: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c437040-e36d-468d-bd5d-25500684fc46/resource) (`7c437040-e36d-468d-bd5d-25500684fc46`)
- S7: [SPFH590高强钢异形三通管胀压复合成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61b7095f-9080-4b88-8e64-a3af9a3bc64e/resource) (`61b7095f-9080-4b88-8e64-a3af9a3bc64e`)
- S8: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64b92724-fb78-4acc-917d-29ce6e75cc5c/resource) (`64b92724-fb78-4acc-917d-29ce6e75cc5c`)
- S20: [SPFH590高强钢异形三通管胀压复合成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ece03143-cea1-4e53-89ac-ebe8c2201f33/resource) (`ece03143-cea1-4e53-89ac-ebe8c2201f33`)
- S6: [SPFH590高强钢异形三通管胀压复合成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/557569a3-1c36-4a19-acae-533f4b81d2dd/resource) (`557569a3-1c36-4a19-acae-533f4b81d2dd`)
- S10: [4421751_应力三轴度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72621713-6a07-4e69-a547-945961648289/resource) (`72621713-6a07-4e69-a547-945961648289`)
- S5: [ductile fracture of an al si mg die casting aluminum alloy__a09011b5d3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5432750e-735f-467b-8bfb-58621c899367/resource) (`5432750e-735f-467b-8bfb-58621c899367`)
- S1: [金属塑成形原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a9698c1-a73b-44eb-bb85-7f11c31c4531/resource) (`0a9698c1-a73b-44eb-bb85-7f11c31c4531`)
- S18: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc7ce450-a7b0-4e5c-ac18-f534c0961e9b/resource) (`dc7ce450-a7b0-4e5c-ac18-f534c0961e9b`)
- S14: [TextNode8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/915937f6-6427-42b6-bb5c-ea286673bded/resource) (`915937f6-6427-42b6-bb5c-ea286673bded`)
- S9: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b5af61e-5a83-4008-8b30-5944f2661b67/resource) (`6b5af61e-5a83-4008-8b30-5944f2661b67`)
- S21: [考虑缺陷的一体压铸铝合金弹塑性本构及断裂准则研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8a56f64-68a4-4acf-bbce-40a46b29436c/resource) (`f8a56f64-68a4-4acf-bbce-40a46b29436c`)
- S17: [SPFH590高强钢异形三通管胀压复合成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d62aed20-5e50-46c6-91b5-79013ea89253/resource) (`d62aed20-5e50-46c6-91b5-79013ea89253`)
- S4: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ebfa349-6181-4e0c-9b50-0941db5fcec8/resource) (`4ebfa349-6181-4e0c-9b50-0941db5fcec8`)
- S3: [图3-22 MMC断裂模型中断裂应变ε^f与应力三轴度η、罗德角参数θ̄之间的关系[62]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2711d218-0859-4e01-b5ea-dfe0c1b41044/resource) (`2711d218-0859-4e01-b5ea-dfe0c1b41044`)