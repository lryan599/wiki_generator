---
version: "v1"
generated_at: "2026-06-18T17:17:25+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 30
  source_quality_score: 0.84
  freshness_score: 0.87
  evidence_coverage_score: 1.0
---

## 概述

Gurson-Tvergaard-Needleman（GTN）损伤模型是在原始Gurson多孔材料屈服模型基础上发展而来的耦合型细观力学韧性损伤模型，属于多孔金属塑性框架的重要组成部分。其核心思想是将孔洞体积分数作为损伤变量纳入材料屈服方程，从而描述含孔隙金属材料从孔洞形核、长大、聚合直至最终韧性断裂的完整过程[[S31,S36,S27]]。当孔洞体积分数为零时，GTN模型屈服方程可自然退化为经典的von Mises屈服准则[[S36]]。

原始Gurson模型由Gurson于1975年提出，采用均质化方法研究球形基体内单个球形孔洞的变形行为，其屈服方程为(σ_e/σ_y)² + 2f cosh(3σ_H/(2σ_y)) - (1 + f²) = 0，假设孔洞体积分数达到100%时材料才完全丧失承载能力[[S6,S22,S38]]。然而该模型存在明显局限：仅考虑孤立孔洞，忽略孔洞间相互作用与聚合阶段的加速损伤行为，且失效条件与工程实际严重不符[[S25,S5,S38,S31]]。

针对原始模型的缺陷，Tvergaard于1981年引入三个修正系数q₁、q₂、q₃以表征微孔洞间的耦合作用[[S6,S20]]；1984年，Tvergaard与Needleman共同引入等效孔洞体积分数f*的概念，刻画孔洞聚合阶段的加速损伤行为，正式构建完整的GTN模型，其首个正式发表文献为Tvergaard与Needleman发表于《Acta Metallurgica》的《Analysis of the cup-cone fracture in a round tensile bar》[[S6,S20,S31]]。

## 代表单元图示

Gurson损伤力学模型以包含孔洞的代表性体积单元为基础，分析多孔材料在应力作用下的弹塑性流动行为，该物理图像是理解GTN模型本构方程的基础[[S16]]。

![标注应力分量的Gurson多孔材料损伤单元](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b96b4d8-8415-422d-bc6e-106bfeeaff59/resource)

## 核心屈服方程与修正参数

GTN模型的完整屈服面表达式为[[S35,S29,S12,S4]]：

Φ=(σ_e/σ_y)² + 2q₁f*cosh(3q₂σ_H/(2σ_y)) - (1+q₃(f*)²) = 0

其中σ_e为von Mises等效应力，σ_y为基体流动应力，σ_H为静水应力，f*为等效孔洞体积分数。

三个Tvergaard修正系数具有明确的物理意义：q₁主导材料强度下降效应，q₂控制应力三轴度对屈服面的影响权重，q₃控制孔洞体积分数的耦合效应[[S9,S35,S4]]。多数工程研究中取q₃=q₁²的简化关系[[S9]]。三个系数的典型工程取值范围为q₁=1.2~1.5、q₂≈1.0、q₃≈1.5~2.25，随着q₁、q₂取值增大，屈服面逐渐收缩；当q₁f*取值为1时，屈服面完全收缩为一点，材料丧失承载能力[[S9,S28]]。

## 等效孔洞体积分数与失效判据

等效孔洞体积分数f*采用分段定义以刻画孔洞聚合阶段的加速损伤行为[[S35,S29,S12]]：

- 当f≤f_c时：f*=f
- 当f_c<f<f_F时：f*=f_c + κ(f-f_c)，其中κ=(1/q₁-f_c)/(f_F-f_c)

当等效孔洞体积分数f*达到临界值f_u*=1/q₁时，材料完全丧失承载能力，发生宏观韧性断裂[[S38,S29,S32]]。与此对应，实际材料发生失效时的孔洞体积分数f_F远低于原始Gurson模型所假定的100%[[S38]]。

## 孔洞体积分数演化机制

总孔洞体积分数的演化满足叠加关系[[S29,S32,S10]]：

f_dot = f_dot_growth + f_dot_nucleation

**孔洞长大**基于金属基体塑性变形的质量守恒假设，孔洞长大引发的体积分数变化率仅与塑性应变的静水分量相关[[S35,S22,S29]]：

f_dot_growth = (1-f) ε_dot_kk^p

**孔洞形核**主要源于金属基体内第二相粒子与基体界面的脱黏或脆性断裂，形核率采用基于应变控制的正态分布函数描述[[S35,S32,S29]]：

f_dot_nucleation = [f_N/(S_N√2π)] exp[-1/2((ε̄^p-ε_N)/S_N)²] ε_dot^p

其中f_N为可形核粒子的体积分数，ε_N为形核平均等效塑性应变，S_N为形核应变的标准差。

## 基础模型核心参数

GTN基础模型包含8个核心耦合参数，物理含义如下[[S6,S7,S9,S35]]：

| 参数 | 物理含义 |
|------|----------|
| f₀ | 材料初始孔洞体积分数 |
| f_c | 孔洞开始发生聚合时的临界孔洞体积分数 |
| f_F | 材料完全丧失承载能力时的失效孔洞体积分数 |
| f_N | 参与孔洞形核的第二相/夹杂物体积分数 |
| ε_N | 孔洞形核概率最大时对应的平均塑性应变 |
| S_N | 孔洞形核应变正态分布的标准差 |
| q₁, q₂, q₃ | 微孔洞相互作用的修正系数 |

## 参数标定方法

GTN模型参数之间存在强耦合关系，其标定是模型工程应用的主要挑战。目前主要采用以下四类方法：

**显微表征直接标定**：通过光学显微镜、扫描电镜数字图像处理或X射线显微断层扫描（XCT）直接测量材料内部初始孔洞分布，获得f₀、f_c、f_F等体积参数。该方法操作直接，但存在夹杂物-孔洞体积换算误差大、测试成本高等局限[[S6,S7,S3]]。

**准原位中断拉伸测试**：在不同加载位移下中断实验，通过扫描电镜统计变形区域内第二相断裂或脱粘产生的新孔洞数量，直接确定孔洞形核参数f_N、ε_N、S_N，适用于具有明确第二相形核源的铸造合金体系[[S7,S37,S33]]。

**细观单胞（RVE）数值模拟**：建立包含预设初始孔洞的轴对称单胞模型，在不同应力三轴度下加载，提取最大等效应力时刻对应的孔洞体积分数作为f_c，可建立f₀与f_c的定量关联关系[[S30,S3,S33]]。

**有限元逆向标定**：结合中心复合设计、响应面法与多目标遗传算法，对比多组不同应力状态下的实验载荷-位移曲线与仿真结果，迭代优化得到全部GTN参数。该方法标定精度高，无需复杂微观表征[[S6,S35]]。

### 标定流程示例

针对压铸铝合金的GTN模型标定可采用从XCT表征、单胞模拟、准原位测试到有限元验证的完整流程框架[[S14]]。

![压铸多孔Al-Si合金GTN模型参数校准与验证框架](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5621e6eb-24e7-49dc-b586-d35b6d8de894/resource)

## 压铸铝合金应用实例

针对AlSi10MnMg与Al-10Si-0.3Mg等高压铸造铝合金，GTN模型可量化表征材料内部初始孔隙率、孔洞形核、长大和聚合全过程，用于预测压铸件的延性失效、失效应变/位移及实际断裂位置，适用孔隙率范围为0.054%至0.3%[[S22,S11]]。其参数标定可采用结合中心复合设计、响应面法与多目标遗传算法的有限元反向标定体系完成[[S6]]。

经实验标定的Al-10Si-0.3Mg压铸合金GTN-NT模型完整参数集如下[[S28]]：

| 参数类别 | 参数符号 | 标定值 |
|----------|----------|--------|
| 修正系数 | q₁ | 1.5 |
| 修正系数 | q₂ | 1 |
| 修正系数 | q₃ | 2.25 |
| 初始孔洞体积分数 | f₀ | 0.00047~0.003 |
| 临界聚合孔洞体积分数 | f_c | 0.00068+1.46×f₀ |
| 形核粒子体积分数 | f_N | 0.0087 |
| 形核平均塑性应变 | ε_N | 0.055 |
| 形核应变标准差 | S_N | 0.048 |
| 剪切损伤调节参数 | k_ω | 标定取值 |
| 剪切阈值下限 | η₁ | 0.4 |
| 剪切阈值上限 | η₂ | 0.8 |

## 与其他延性损伤模型的对比

GTN模型与其他主流延性损伤模型在理论框架上存在显著差异[[S2,S26,S31]]：

| 模型 | 类型 | 参数数量 | 核心特征 |
|------|------|----------|----------|
| GTN模型 | 耦合型 | 9个未知参数 | 将孔洞体积分数直接引入屈服方程，自然描述材料软化效应 |
| Johnson-Cook模型 | 非耦合型 | 3个断裂相关参数 | 经验型准则，基于应力三轴度、应变率与温度 |
| 简化Lemaitre模型 | 耦合型 | 3个损伤参数 | 基于连续损伤力学框架，各向同性损伤假设 |

## 优势与局限

GTN模型作为耦合型损伤模型，能够自然描述孔洞演化过程中的材料软化效应，在预测含孔隙金属材料的韧性断裂行为和损伤不确定性方面具有独特优势[[S11,S31]]。然而其应用也面临若干限制：

- **参数标定难度高**：基础模型包含9个未知参数，参数间强耦合导致标定困难[[S31,S11]]。
- **低应力三轴度适用性差**：基于球状孔洞在对称应力状态的假设开发，在低应力三轴度（η<0.33）或非对称剪切应力状态下预测精度不足[[S31]]。
- **参数适用范围窄**：当铸件初始孔隙率超出标定适用范围时，全套模型参数需重新标定[[S11]]。
- **计算效率较低**：相比Johnson-Cook等非耦合模型，同一仿真任务的计算耗时显著更长[[S11]]。

## 剪切修正变体

为克服基础GTN模型在低应力三轴度剪切主导场景下的预测不足，研究者提出了多种剪切修正方案。

**Nahshon-Hutchinson（NH）剪切修正模型**在孔洞体积增长率中额外引入偏应力第三不变量相关的剪切损伤项，补充描述低应力三轴度下的孔洞剪切演化行为。其中k_ω为纯剪切状态下损伤增长率调节参数，金属结构材料典型取值范围为1~3，高强钢场景下取值通常提升至5。该模型已成功应用于铝合金及Weldox钢的剪切失效预测[[S21,S23]]。

**Nielsen-Tvergaard（NT）剪切修正模型**针对NH模型在高应力三轴度下额外放大罗德角影响的缺陷，引入基于应力三轴度阈值η₁、η₂的衰减函数Ω(η)。当η<η₁时等效为GTN-NH模型，当η>η₂时退化为基础版本GTN模型，有效降低了中高应力三轴度（η>0.33）下不合理的剪切损伤项贡献。η₁、η₂可通过三点弯曲测试完成标定，适配压铸铝合金宽应力状态范围下的失效预测场景[[S7,S23,S18]]。

剪切修正GTN可通过用户自定义子程序在Abaqus/Explicit等求解器中部署运行。针对高压铸造Al-Si合金场景，可结合准原位剪切拉伸测试统计硅颗粒断裂形核数据，完成GTN-NT模型全部参数的标定，准确预测压铸试样的失效位移离散度与实际断裂位置[[S7]]。

## Sources
- S31: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4b71803-4379-4022-b336-85f6d5627510/resource) (`c4b71803-4379-4022-b336-85f6d5627510`)
- S36: [中国模具工程大典 第1卷 现代模具设计方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f16c2ebd-f72b-4b7f-8590-f2241345f972/resource) (`f16c2ebd-f72b-4b7f-8590-f2241345f972`)
- S27: [现代模具设计基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a6a9903-a7c6-43c4-aa8e-92ada5e48410/resource) (`9a6a9903-a7c6-43c4-aa8e-92ada5e48410`)
- S6: [基于响应曲面法的AlSi10MnMg压铸铝合金GTN模型参数标定](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d4003bd-84fb-4052-bcc2-43d89b7b1966/resource) (`0d4003bd-84fb-4052-bcc2-43d89b7b1966`)
- S22: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82201a4d-3fdd-448a-b0a0-cd4cb9411bb2/resource) (`82201a4d-3fdd-448a-b0a0-cd4cb9411bb2`)
- S38: [粉末金属成形过程的计算机仿真与成形中的缺陷预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ffae31d3-3da8-4ea9-84f7-821c3548db4e/resource) (`ffae31d3-3da8-4ea9-84f7-821c3548db4e`)
- S25: [粉末金属成形过程计算机仿真与担缺陷预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8faf6d16-5fbe-4b3b-afa1-113d05143b32/resource) (`8faf6d16-5fbe-4b3b-afa1-113d05143b32`)
- S5: [粉末金属成形过程的计算机仿真与成形中的缺陷预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ce2c3a8-fe47-4615-88e7-0bbc4345d442/resource) (`0ce2c3a8-fe47-4615-88e7-0bbc4345d442`)
- S20: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/659eb097-df80-4fd2-a267-df5ad54353e8/resource) (`659eb097-df80-4fd2-a267-df5ad54353e8`)
- S16: [图5-1 Gurson损伤单元](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b96b4d8-8415-422d-bc6e-106bfeeaff59/resource) (`5b96b4d8-8415-422d-bc6e-106bfeeaff59`)
- S35: [基于响应曲面法的AlSi10MnMg压铸铝合金GTN模型参数标定](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eab0b0d5-d82f-4e7b-a6fc-8baedc8dd89a/resource) (`eab0b0d5-d82f-4e7b-a6fc-8baedc8dd89a`)
- S29: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ac2dd974-d39f-46e2-af92-6407c59a306b/resource) (`ac2dd974-d39f-46e2-af92-6407c59a306b`)
- S12: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3abbd976-44a4-439c-be93-766b541a32ee/resource) (`3abbd976-44a4-439c-be93-766b541a32ee`)
- S4: [粉末金属成形过程的计算机仿真与成形中的缺陷预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0a8ab3c4-947e-4ddc-aa32-52ecbb69ca9f/resource) (`0a8ab3c4-947e-4ddc-aa32-52ecbb69ca9f`)
- S9: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/159ac433-832f-44eb-8d84-a995a3a6487f/resource) (`159ac433-832f-44eb-8d84-a995a3a6487f`)
- S28: [表4.3 使用该方法标定的GTN-NT模型参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9bd80205-e748-4a9f-828e-24b213c32cf0/resource) (`9bd80205-e748-4a9f-828e-24b213c32cf0`)
- S32: [基于响应曲面法的AlSi10MnMg压铸铝合金GTN模型参数标定](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc436fc2-38b4-44a0-9eaa-33ca5f37a171/resource) (`cc436fc2-38b4-44a0-9eaa-33ca5f37a171`)
- S10: [金属成形科学与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1cee18df-ea66-471e-94db-71ea2da03667/resource) (`1cee18df-ea66-471e-94db-71ea2da03667`)
- S7: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14aa278d-0821-4099-a540-3a3e63bb3a60/resource) (`14aa278d-0821-4099-a540-3a3e63bb3a60`)
- S3: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08a44c09-9c25-471c-9e8d-ac36fb237699/resource) (`08a44c09-9c25-471c-9e8d-ac36fb237699`)
- S37: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe102194-aa13-44d0-8768-f58cb6c18d5b/resource) (`fe102194-aa13-44d0-8768-f58cb6c18d5b`)
- S33: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1cc5122-5962-48a0-91c2-197869a5ada1/resource) (`d1cc5122-5962-48a0-91c2-197869a5ada1`)
- S30: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba4c7b38-f608-430d-985d-54d117829b4e/resource) (`ba4c7b38-f608-430d-985d-54d117829b4e`)
- S14: [图4.2 对压铸多孔Al-10Si-0.3Mg合金的参数校准与验证框架](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5621e6eb-24e7-49dc-b586-d35b6d8de894/resource) (`5621e6eb-24e7-49dc-b586-d35b6d8de894`)
- S11: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34814be6-82d6-45fc-93ef-97205ee63bf2/resource) (`34814be6-82d6-45fc-93ef-97205ee63bf2`)
- S2: [表1.1 各类主要延性损伤模型总结; Table 1.1 Summary of the primary applied ductile damage models.](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06719f56-1c87-42f6-bd10-22cd2ce68a05/resource) (`06719f56-1c87-42f6-bd10-22cd2ce68a05`)
- S26: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/918369a2-df40-42a3-a372-696087615ab8/resource) (`918369a2-df40-42a3-a372-696087615ab8`)
- S21: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c9904a5-123b-486a-804a-8877bc75b20c/resource) (`6c9904a5-123b-486a-804a-8877bc75b20c`)
- S23: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8379a9d5-496c-46de-8d4e-d603027102c2/resource) (`8379a9d5-496c-46de-8d4e-d603027102c2`)
- S18: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/608612d5-a7b8-416a-8ef2-722885a318fa/resource) (`608612d5-a7b8-416a-8ef2-722885a318fa`)