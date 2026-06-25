---
version: "v1"
generated_at: "2026-06-18T11:47:54+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 30
  source_quality_score: 0.83
  freshness_score: 0.93
  evidence_coverage_score: 1.0
---

## 概述

JMatPro（全称 Java-based Materials Properties）是由英国 Sente Software 公司开发的商用金属材料性能模拟预测软件，基于 CALPHAD（相图计算）方法构建[[S16,S12]]。软件集成了铸造凝固性能计算、热物理及物理性能计算、相转变计算、机械性能计算、稳态和亚稳态相平衡计算等多个功能模块，具备计算快速准确、使用便捷的特点，常被用于为各类有限元铸造仿真软件提供标准材料物理性能参数[[S16,S10]]。在压铸及铸造领域的公开学术文献中，"J-mat 软件""JMatPro 模拟软件""Jmat Pro""JMatPro 热模拟软件"等均为被广泛使用的通用称谓[[S14,S4,S7]]。

## 适用材料体系

JMatPro 内置数据库涵盖几乎所有主流工业金属材料，并细分了独立的材料子库[[S16]]。具体支持的合金体系包括：

- 钢铁材料（细分普通钢、不锈钢、铸铁独立子库）
- 铝合金
- 镁合金
- 钴合金
- 镍基高温合金
- 钛合金
- 锆合金
- 焊料合金
- 高熵合金

数据库由姊妹公司 ThermoTech 提供，与软件完全绑定，用户无需单独配置额外库文件[[S12]]。

## 核心功能与计算能力

### 热物性参数计算

JMatPro 可输出覆盖全温度区间（从室温至液相线以上）的热物性参数，包括比热容、热导率、热焓、密度、热膨胀系数、潜热等随温度连续变化的完整曲线[[S31,S17]]。例如，对 ZL114A 合金的计算可精确给出液相线温度（612°C）、固相线温度（524°C）、液相线温度下的导热系数（87.9 W/(m·K)）、热焓（1023.6 kJ/kg）和密度（2451.7 kg/m³）[[S3]]。

### 力学性能计算

力学性能计算覆盖弹性模量、泊松比、不同温度下屈服强度/抗拉强度、硬度、蠕变参数等，可直接输出随温度变化的连续函数关系[[S31,S12]]。公开的版本 JMatPro 2021 还支持流动应力曲线、断裂强度、蠕变与断裂寿命、加工图、断裂韧性等高级力学性能计算[[S10]]。

### 相组成与凝固路径计算

JMatPro 可计算平衡/亚稳态条件下所有析出相的质量分数或体积分数、析出温度区间、相组成元素占比，包含 T₀ 相变温度、亚稳相稳定区间等特殊热力学参数[[S14]]。凝固相关曲线输出包括液相线温度、固相线温度、Scheil 非平衡凝固固相分数随温度变化曲线、元素微观偏析分布、不同冷却速率下的晶粒生长限制因子[[S23]]。

### 固态相变计算

软件可生成 TTT 曲线（等温转变曲线）、CCT 曲线（连续冷却转变曲线）、淬火相变动力学结果，支持不同热处理工艺下的相变产物预测[[S12]]。

## 凝固模型与方法基础

### 平衡凝固模型

JMatPro 内置 Lever Rule（杠杆定律）模型，假定固相和液相中所有溶质元素无限扩散，处于完全热力学平衡状态，可直接输出完整平衡相图、固液相线温度[[S23]]。

### 非平衡凝固模型

软件内置标准 Scheil-Gulliver 模型，默认假定液相中溶质无限扩散、固相中溶质完全不扩散，可输出常规非平衡凝固路径[[S23]]。针对铸铁类材料，JMatPro 开发了扩展 Scheil-Gulliver 模型：除 C 元素之外的所有元素遵循经典 Scheil-Gulliver 假设，C 元素允许在固相中扩散，更贴合铸铁实际凝固行为[[S23,S1]]。

### 反扩散（Back Diffusion）模型

JMatPro 内置 Back Diffusion（反扩散/溶质有限固相扩散）模型，可量化描述介于完全非平衡 Scheil 和完全平衡 Lever Rule 之间的溶质扩散行为，支持用户自定义固相冷却速率参数，模拟贴近工业实际的凝固微观偏析过程[[S11]]。

### 扩散动力学基础

JMatPro 的扩散动力学继承 Thermo-Calc/DICTRA 体系成熟的原子迁移率计算框架，将多元溶液相中单个组元的原子迁移率定义为温度、压力、局部成分的函数，通过 CALPHAD 方法统一优化迁移率参数，直接输出多元系互扩散系数[[S32]]。

## 在压铸与铸造中的应用

### 压铸合金成分设计与优化

在半固态压铸高强铝合金开发中，JMatPro 被用于研究 Si、Cu、Mg 元素含量（4%~8% 区间）对半固态成形性能的影响，以工艺窗口要求（液相分数 0.5~0.7 对应的温度区间、液相分数 0.6 时温度敏感性 df_L/dT < 0.015 K⁻¹、凝固温度区间小于 130 K）和极限抗拉强度作为评价指标，最终确定适配半固态压铸的优化高强铝合金成分[[S4]]。

在 319s 铝合金半固态压铸成分优化中，通过 JMatPro 计算不同 Si 含量下的液相分数曲线，当 Si 含量为 6% 时获得 27°C 的最优半固态工艺窗口[[S20]]。

在免热处理铸造 Al-Si 系合金优化中，JMatPro 计算结果显示：对比 Al-7Si-0.6Mn-0.5Mg 合金，Al-9Si-0.6Mn-0.5Mg 合金的共晶 Si 相分数提升 36.58%，凝固温度区间缩短 25.23%[[S25]]。

在免固溶处理 Al-Si-Zn-Mg-Cu 压铸铝合金开发中，JMatPro 可模拟对比添加 Mg 和 Zn 前后的合金平衡相含量变化，计算各元素的偏摩尔吉布斯自由能与完整凝固路径，提前预测合金力学性能是否达到设计目标[[S7]]。

### 改性灰铸铁材料属性计算

在 HT250 基础上调整成分（降低 Ni、Cu 含量，增加 Ti 至 0.10wt%、B 至 0.03wt%）的高性能改性灰铸铁研究中，JMatPro 使用 Back Diffusion 模型完成 20~1500°C 全温度区间热物性和流体力学属性计算，输出结果直接对接铸造有限元模拟软件[[S11]]。计算结果表明：改性后固相线从 1078°C 降低至 1072°C，液相线从 1198°C 降低至 1190°C，固液共存区间内固相分数随温度变化趋势更平缓，凝固过程整体体积收缩减小[[S11,S6]]。

### 为铸造有限元模拟提供材料参数

压铸领域典型的应用流程为：JMatPro 计算得到的全温度范围热物性参数曲线可直接导入 ProCAST 的 CAST 模块替换原有默认材料数据，可显著提升铸件缺陷预测与残余应力有限元模拟的准确性[[S15]]。

在球墨铸铁板簧座的压铸缺陷预测中，对比验证表明：JMatPro 计算的 800°C 以下导热系数更符合 100~500°C 球铁导热系数无明显下降的实测规律；固相分数曲线符合过共晶球铁糊状凝固特点；弹性模量、600°C 以下热膨胀系数变化趋势与实测数据吻合度优于 ProCAST 自带参数，可为缩松缩孔、残余应力的精准预测提供更可靠的基础物性支撑[[S15,S1]]。

在稀土镁合金 Mg-10Gd-2Y-1Zn-0.5Zr 的压铸残余应力模拟中，JMatPro 计算的热焓数据因支持更高精度的合金成分输入，被选用为有限元模拟的前置输入[[S2]]。

### 热裂倾向与流动性评估

JMatPro 无直接"热裂倾向"一键专属功能模块，但可通过软件输出的不可补缩温度区间（固相分数 0.003~0.215 对应的温度间隔）、固液两相区线性膨胀系数变化量，结合 Clyne-Davies 热裂敏感性系数计算公式定量评估合金热裂风险。该方法在 GH4975 高温合金、6061/7075/5083 铝合金等研究中已验证有效，热裂倾向排序结果与实际铸造实验完全一致[[S19,S27]]。

JMatPro 无直接"合金流动性"一键专属功能模块，但可通过软件输出的液相线与固相线之间的凝固温度区间 ΔT（Scheil 模型计算）作为合金流动性定量判定指标，凝固温度区间越窄合金流动性越好[[S13,S20]]。

## 输入参数与典型工作流程

JMatPro 的核心输入参数为目标合金的各合金元素质量百分含量[[S26]]。面向压铸场景的典型完整工作流程如下[[S1,S21]]：

| 步骤 | 操作内容 |
|------|----------|
| 1. 模块选择 | 选择对应合金计算模块（如铸铁模块、铝合金模块、镁合金模块等） |
| 2. 成分录入 | 录入目标合金的化学成分（各元素质量分数） |
| 3. 模型选定 | 选定适配该合金凝固特性的非平衡凝固计算模型（如针对铸铁的扩展 Scheil-Gulliver 模型或 Back Diffusion 模型） |
| 4. 计算输出 | 计算输出覆盖液相线、固相线到室温的全温度区间的密度、导热系数、比热容、热焓、固相分数、弹性模量、热膨胀系数等全套热物性与力学性能曲线 |
| 5. 参数导入 | 导出的参数文件直接导入下游铸造模拟软件（ProCAST 等）或通用有限元软件（ABAQUS、ANSYS 等）完成仿真前处理 |

## 与同类软件的关系

### 与 Thermo-Calc 的互补关系

同属 CALPHAD 框架的 Thermo-Calc 软件数据库包含的稳定相、亚稳相总数量多于 JMatPro，但 Thermo-Calc 原生不具备直接模拟合金力学性能的功能。压铸领域实际应用中二者常搭配使用，Thermo-Calc 用于新型合金成分初筛和相平衡计算，JMatPro 进一步输出该成分的全套可直接用于仿真的力学性能参数[[S10]]。

### 与 ProCAST 的数据对接与精度对比

JMatPro 在工程实践中常被用于为 ABAQUS、ANSYS 等主流通用有限元软件提供各类金属材料覆盖全温度区间的热物理、力学性能参数，直接填充有限元软件的自定义材料库[[S16,S29]]。针对球墨铸铁的热物性计算场景，JMatPro 在多个参数上精度优于 ProCAST 默认 Back Diffusion 模型的输出结果[[S15,S33,S5,S22,S9]]。AZ91D 镁合金的热导率、密度、固相分数、比热容计算与实验数据对比也验证了 JMatPro 针对压铸镁合金的较高计算精度[[S24]]。

## 版本信息

公开可查的正式版本包括 JMatPro 2021，该版本除基础相转变计算外，支持的机械性能计算维度包含室温强度/硬度、高温强度/硬度、流动应力曲线、断裂强度、蠕变与断裂寿命、加工图、断裂韧性等[[S10]]。

## 局限性与注意事项

公开研究结果显示，使用 JMatPro 计算纯钛等合金的力学性能时，得到的数值结果与实测值存在一定偏差，但强度等性能变化趋势与实测结果保持一致[[S14]]。软件对力学性能的绝对数值预测需结合实验验证，但其相对变化趋势具有较强的参考价值。

## 图示与计算验证

### 镁合金热物性计算验证

相关文献给出了 AZ91D 镁合金的热导率、密度、固相分数、比热容四个子图，对比 JMatPro、ProCAST 的计算结果与实验实测数据，可直接验证 JMatPro 针对压铸镁合金的热物性参数计算精度[[S24]]。

![JMatPro与ProCAST软件计算的AZ91D镁合金热导率、密度、固相分数、比热容随温度变化结果与实验数据对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5a8e62b-844d-4018-8a02-86a11e07159a/resource)

### 流动应力计算示意

相关文献展示了应变率为 0.1/s 条件下，JMatPro 计算得到的不同温度（200°C 至 1000°C）下金属材料工程流动应力随工程应变的变化曲线，可支撑 JMatPro 机械性能计算能力的相关说明[[S18]]。

![JMatPro不同温度下流动应力计算结果（应变率0.1/s）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b6376a7-5442-4245-8e27-5e5b13640e6c/resource)

## Sources
- S16: [步进加热炉方坯加热特性与性能演变研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e2020ff-dea9-4677-ad06-fa54eeee0a90/resource) (`8e2020ff-dea9-4677-ad06-fa54eeee0a90`)
- S12: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6996a834-5ade-4d09-97be-a649e80e325e/resource) (`6996a834-5ade-4d09-97be-a649e80e325e`)
- S10: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6142121a-0672-4ea2-875e-99acd939b26f/resource) (`6142121a-0672-4ea2-875e-99acd939b26f`)
- S14: [免热处理铸造Al-Si系合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e6ef704-bf3c-4e37-9427-0d5dd2492b32/resource) (`7e6ef704-bf3c-4e37-9427-0d5dd2492b32`)
- S4: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2fc8959e-f594-4578-af11-a74dffd64e8a/resource) (`2fc8959e-f594-4578-af11-a74dffd64e8a`)
- S7: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/577b74a3-571d-43c5-a8de-33cd7e5ee4e7/resource) (`577b74a3-571d-43c5-a8de-33cd7e5ee4e7`)
- S31: [压铸铝合金搅拌摩擦焊接工艺及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9824248-0a2b-4a05-9e6d-351bdbaed863/resource) (`f9824248-0a2b-4a05-9e6d-351bdbaed863`)
- S17: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90349cd0-0ba9-4f99-a36b-49100aeb5abf/resource) (`90349cd0-0ba9-4f99-a36b-49100aeb5abf`)
- S3: [柴油机铝合金缸体铸造工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c30e0ed-92a3-4924-b255-f0efad0dfdf5/resource) (`1c30e0ed-92a3-4924-b255-f0efad0dfdf5`)
- S23: [铸态高强韧性板簧座铸造工艺设计及残余应力的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af298b3a-0253-4a06-a924-060a566f6ac3/resource) (`af298b3a-0253-4a06-a924-060a566f6ac3`)
- S1: [铸态高强韧性板簧座铸造工艺设计及残余应力的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14223897-d64a-4236-b4dd-c2db211c4d16/resource) (`14223897-d64a-4236-b4dd-c2db211c4d16`)
- S11: [高性能改性灰铸铁制动鼓铸造缺陷预测及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64dea739-492b-4b47-855b-c44de4a40b76/resource) (`64dea739-492b-4b47-855b-c44de4a40b76`)
- S32: [铌微合金化h13钢的热疲劳行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd9ea749-d718-4aa0-b701-92416248ad54/resource) (`fd9ea749-d718-4aa0-b701-92416248ad54`)
- S20: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a73a2f9b-9a1b-4131-9a36-698242996354/resource) (`a73a2f9b-9a1b-4131-9a36-698242996354`)
- S25: [免热处理铸造Al-Si系合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b64d5864-3bbf-460c-ad50-3c7a9946205a/resource) (`b64d5864-3bbf-460c-ad50-3c7a9946205a`)
- S6: [高性能改性灰铸铁制动鼓铸造缺陷预测及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ee42db7-26e9-4cda-a3ac-124ef3ab830f/resource) (`3ee42db7-26e9-4cda-a3ac-124ef3ab830f`)
- S15: [铸态高强韧性板簧座铸造工艺设计及残余应力的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/800f7474-b54a-41e8-8c6a-63e42adb3a0e/resource) (`800f7474-b54a-41e8-8c6a-63e42adb3a0e`)
- S2: [稀土镁合金热焓与温度关系的ProCAST和JmatPro计算曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16c063e9-cb5d-4762-bdbe-ab40d6b9d5db/resource) (`16c063e9-cb5d-4762-bdbe-ab40d6b9d5db`)
- S19: [高合金化难变形高温合金GH4975热裂敏感性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f003ab3-68be-4cb7-bab5-cc35e272d233/resource) (`9f003ab3-68be-4cb7-bab5-cc35e272d233`)
- S27: [12716474_凝固收缩](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cda34e40-61be-456d-a7b2-98af4349dc54/resource) (`cda34e40-61be-456d-a7b2-98af4349dc54`)
- S13: [Al-Si-Mg-Cu免热处理铝合金的组织与力学性能调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e45606e-21db-41a6-ba6c-887647380e71/resource) (`7e45606e-21db-41a6-ba6c-887647380e71`)
- S26: [表2-2. JmatPro预测含量极限化的XA铝合金(wt.%)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9818bb0-61ef-48cb-8082-986c2a2ab102/resource) (`c9818bb0-61ef-48cb-8082-986c2a2ab102`)
- S21: [铸造铝硅合金一体化控性工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7ec7d18-dc0d-4ea8-93f1-42cdf47c4c46/resource) (`a7ec7d18-dc0d-4ea8-93f1-42cdf47c4c46`)
- S29: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e7794852-ef7b-4030-a35e-048f34fcfe3c/resource) (`e7794852-ef7b-4030-a35e-048f34fcfe3c`)
- S33: [JMatPro与ProCAST-Back Diffusion计算的球铁导热系数随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe92c7dd-aca5-42a5-94b1-4d293e5914d8/resource) (`fe92c7dd-aca5-42a5-94b1-4d293e5914d8`)
- S5: [球墨铸铁固相分数随温度变化的软件计算对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3508eb51-db97-4e04-8894-46df2beaa15a/resource) (`3508eb51-db97-4e04-8894-46df2beaa15a`)
- S22: [图2.2(e) ProCAST与JMatPro的球墨铸铁热膨胀系数对比图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae42e896-2fb8-4f6d-8025-5524d2abe9ea/resource) (`ae42e896-2fb8-4f6d-8025-5524d2abe9ea`)
- S9: [球墨铸铁弹性模量随温度变化的JMatPro与ProCAST计算结果对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/607f698d-279b-41e7-a6cb-f0a366301561/resource) (`607f698d-279b-41e7-a6cb-f0a366301561`)
- S24: [图3-1 AZ91D镁合金热力学性能参数的计算与试验结果对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5a8e62b-844d-4018-8a02-86a11e07159a/resource) (`b5a8e62b-844d-4018-8a02-86a11e07159a`)
- S18: [FIGURE 15.6 JMatPro analysis: Strain rate is 0.1/s.](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b6376a7-5442-4245-8e27-5e5b13640e6c/resource) (`9b6376a7-5442-4245-8e27-5e5b13640e6c`)