---
version: "v1"
generated_at: "2026-06-18T15:45:37+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 24
  source_quality_score: 0.85
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

Cross-WLF 粘度模型，全称 Cross-Williams-Landel-Ferry 模型，亦称 Cross-WLF 交叉模型、Cross-WLF 七参数模型，是在聚合物流变学中用于描述非牛顿流体粘温特性的半经验粘度模型 [[S12,S4,S10]] 。该模型将 Cross 粘度方程与 WLF 温度–压力叠加方程耦合，可在宽剪切速率和温度范围内同时表征粘度随剪切速率、温度、压力的变化规律，广泛应用于注塑成型充填与后充填过程的计算机仿真 [[S26,S4,S3]] 。

## 定义与分类

Cross-WLF 模型属于广义牛顿流体本构模型，被视为注塑模流仿真领域描述无定形聚合物熔体粘度的主流推荐模型。相较幂律模型和 Cross-Arrhenius 模型，该模型综合温度、剪切速率、压力三类因素对流动粘度的影响，适用温度范围更宽，对温度敏感工况的适应性更优 [[S26,S4]] 。

## 数学模型

Cross-WLF 模型的完整数学形式为一种分层耦合方程组，结合了 Cross 基础模型与 WLF 温度叠加方程，并引入压力对玻璃化转变温度的偏移修正。

### Cross 基础模型

独立基础 Cross 粘度模型表达式为 [[S12,S10]] ：

\[
\eta = \frac{\eta_0}{1+\left(\eta_0 \dot{\gamma} / \tau^*\right)^{1-n}}
\]

式中：

- \(\eta_0\) ——零剪切粘度；
- \(n\) ——非牛顿指数（幂律指数），表征流体偏离牛顿行为的程度；
- \(\tau^*\) ——临界剪切应力，为材料从牛顿平台区过渡到剪切变稀区对应的特征剪切应力水平；
- \(\dot{\gamma}\) ——剪切速率。

### WLF 温度叠加方程

独立的 WLF 方程基于自由体积理论，描述零剪切粘度随温度的变化规律。其基准参考温度为玻璃化转变温度 \(T_g\)，通用经验常数 \(A_1=17.44\)、\(A_2=51.6\,\text{K}\)，适用于 \(T_g < T < T_g+100^\circ\text{C}\) 的无定形聚合物温度区间 [[S19,S11,S23]] ：

\[
\lg a_T = \lg \frac{\eta_0(T)}{\eta_0(T_g)} = -\frac{A_1(T-T_g)}{A_2 + (T-T_g)}
\]

### Cross-WLF 完整耦合方程

将 WLF 型零剪切粘度表达式代入 Cross 模型，形成完整的七参数 Cross-WLF 方程组 [[S4,S3,S10]] ：

1\. 剪切速率—粘度关系：

\[
\eta(\dot{\gamma},T,p) = \frac{\eta_0(T,p)}{1+\left(\dfrac{\eta_0 \dot{\gamma}}{\tau^*}\right)^{1-n}}
\]

2\. WLF 型零剪切粘度：

\[
\eta_0(T,p) = D_1 \exp\left(-\frac{A_1(T-T^*)}{A_2 + (T-T^*)}\right)
\]

3\. 温度—压力耦合项：

\[
T^*(p) = D_2 + D_3 p,\qquad A_2 = \tilde{A_2} + D_3 p,\qquad \tau^* = D_2 + D_3 p
\]

在多数常规注塑工况下（注塑压力 ≤ 100 MPa），压力影响系数 \(D_3\) 可设置为 0，忽略压力对玻璃化转变温度的偏移 [[S4,S10,S22]] 。

## 模型参数

Cross-WLF 模型包含 7 个独立可测的材料常数，所有参数均可通过流变仪测试数据拟合获得 [[S4,S10,S5]] 。各参数的物理含义与单位归纳如下表。

| 参数 | 物理含义 | 单位 | 典型取值或范围 |
|:---|:---|:---|:---|
| \(n\) | 非牛顿（幂律）指数，表征流体偏离牛顿特性的程度 | 无量纲 | 0.2~0.7 [[S10,S5]] |
| \(\tau^*\) | 临界剪切应力，牛顿区过渡到幂律区的特征剪切应力 | Pa | 材料特定 [[S10,S5]] |
| \(D_1\) | 常压玻璃化转变温度下的参考零剪切粘度 | Pa·s | 材料特定 [[S3,S10,S5]] |
| \(D_2\) | 常压下的参考玻璃化转变温度 | K | 材料特定 [[S10,S5]] |
| \(D_3\) | 玻璃化转变温度随压力的变化率 | K/Pa | 常规工况设为 0 [[S10,S5,S22]] |
| \(A_1\) | WLF 常数（与温度相关的无量纲参数） | 无量纲 | 1~100 [[S3,S5]] |
| \(A_2\) | WLF 常数 | K | 1~1000 [[S3,S5]] |

### WLF 常数的获取方法

WLF 常数的常规获取方法为：通过毛细管流变仪在不同温度下采集多组剪切粘度测试数据，结合非线性拟合算法与时温平移方法得到对应材料的专属 WLF 常数。针对通用无定形聚合物，可直接采用经验常数 \(A_1=17.44\)、\(A_2=51.6\,\text{K}\) 进行快速估算 [[S11,S15,S19]] 。

## 适用范围与物理意义

Cross-WLF 模型的适配温度区间为聚合物玻璃化转变温度 \(T_g\) 到 \(T_g+100^\circ\text{C}\)（无定形聚合物），可准确描述该区间内粘度随温度的变化行为 [[S12,S17,S21]] 。模型可完整覆盖从低剪切速率零牛顿区到高剪切速率剪切变稀区的聚合物典型“S”形流变曲线描述 [[S4,S10]] 。

Cross-WLF 模型适用于注塑成型完整的充填/后充填全过程，相比 Cross-Arrhenius 模型可在更低温度下保持精度，能够描述伴随冷却效应的非等温熔体流动行为，在模流仿真中使用该模型可显著降低预测误差 [[S10,S21,S13]] 。

## 局限性

Cross-WLF 模型基于广义牛顿流体假设构建，未包含粘弹性效应的描述项，不适用于需要考虑聚合物弹性回复、挤出胀大等弹性主导的流变场景 [[S25,S10]] 。同时，模型默认忽略剪切时间依赖性（触变效应），无法对高固相含量半悬浮体系的流变行为实现高精度描述 [[S10]] 。

## 与其他粘度模型的对比

- **幂律模型**：仅含 2 个参数，计算效率最高，但仅可在较窄的高剪切速率区间获得合理精度，低剪切速率下预测粘度远高于实际值，且无压力关联项，仅适配常规注塑充填阶段的简化快速仿真场景 [[S12,S10,S18]] 。
- **Bird-Carreau 模型**：含 5 个核心参数，可同时描述零剪切牛顿平台、剪切变稀区、高剪切第二牛顿平台三类流变区域，但未内置温度与压力的耦合关联项，仅适配等温条件下固定压力的宽剪切速率流变预测，在非等温模流仿真中的易用性低于 Cross-WLF 模型 [[S12,S25]] 。
- **Cross-WLF 模型**：7 参数，同时综合温度、剪切速率、压力对聚合物熔体粘度的影响，适用温度范围宽泛，是注塑模流仿真领域主流推荐的粘度模型 [[S26,S4,S3]] 。

## 工业软件实践

Cross-WLF 模型是 Moldflow 等主流模流仿真软件的官方内置粘度模型。在软件材料流变属性配置界面中，提供直接输入 \(n\)、\(\tau^*\)、\(D_1\)、\(D_2\)、\(D_3\)、\(A_1\)、\(A_2\) 共 7 项模型参数的专用对话框，并集成粘度曲线绘制与测试信息查看功能 [[S2,S24,S27]] 。

![Moldflow新版本Cross-WLF粘度模型系数设置界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18e23de3-8e9e-433c-af3f-c61c787ab6e6/resource)  
*图：Moldflow新版本Cross-WLF粘度模型系数设置界面 [[S2]]*

## 拉链链牙注塑应用案例

针对以聚甲醛（POM）为原料的 8 号软布基拉链链牙微小特征精密注塑场景，选用 Cross-WLF 模型可在宽剪切速率范围内精准描述假塑性 POM 熔体的流变特性，同时良好拟合熔体冷却过程中的粘度变化 [[S22,S17]] 。该场景下 POM 材料的 Cross-WLF 模型典型参数 [[S22]] 如下：

| 参数 | 取值 |
|:---|:---|
| \(n\) | 0.1991 |
| \(\tau^*\) | 322899 Pa |
| \(D_1\) | \(1.02742 \times 10^{13}\) Pa·s |
| \(D_2\) | 223.15 K |
| \(D_3\) | 0 |
| \(A_1\) | 28.863 |
| \(A_2\) | 51.6 K |

采用该模型完成模流仿真并结合正交试验优化后，链牙 X 方向翘曲变形量从 3.425 mm 降至 3.148 mm，总收缩变形降低 9.3%，链牙错位问题得到有效改善 [[S22,S16]] 。

![Moldflow中聚甲醛（POM）Cross-WLF粘度模型参数设置界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31c9bdda-5fe1-4869-b1c0-88d211ed9d54/resource)  
*图：Moldflow中聚甲醛（POM）Cross-WLF粘度模型参数设置界面 [[S6]]*

不同成型温度与工艺速度下，经 Cross-WLF 修正后的仿真粘度与实测值偏差远小于原始未修正模型，直观表明该模型在粘度预测精度上的优势 [[S7]] 。

![不同工艺参数下Cross-WLF修正模型的粘度预测与实测值对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47a563eb-d3b9-4ca2-ad57-178325bd7355/resource)  
*图：不同工艺参数下Cross-WLF修正模型的粘度预测与实测值对比 [[S7]]*

## 工程校准流程

精密注塑仿真中 Cross-WLF 模型的常规工程校准流程包括 [[S22,S14,S1]] ：

1. 通过旋转流变仪在不同温度、剪切速率条件下测试聚合物的流变数据，导入 Moldflow 等软件自动拟合得到 Cross-WLF 初始 7 项参数；
2. 针对常规注塑压力不超过 100 MPa 的工况，将 \(D_3\) 参数默认设置为 0，简化非核心压力相关粘度影响计算；
3. 通过多组不同工艺参数下的短射实验，实测型腔填充长度与填充时间，与仿真结果对比微调 \(n\)、\(\tau^*\) 等核心参数，缩小模拟值与实测值偏差；
4. 结合正交试验的实际成型结果，以制品翘曲、填充完整性等实际指标为参考，对全组参数做最终全局校准。

## Sources
- S12: [软布基拉链注塑工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6abfe5a4-3665-493a-8781-9174919115ff/resource) (`6abfe5a4-3665-493a-8781-9174919115ff`)
- S4: [纤维增强聚苯硫醚复合材料的制备及多尺度性能分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f3d0728-9b28-423e-84e4-a982f62d4ecd/resource) (`1f3d0728-9b28-423e-84e4-a982f62d4ecd`)
- S10: [TextNode56](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65ee8e2b-ebd8-40e1-970c-f6aa7ada6ffc/resource) (`65ee8e2b-ebd8-40e1-970c-f6aa7ada6ffc`)
- S26: [注塑模具随形冷却水路优化及增材制造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f70fd79c-dc45-44b8-934d-3d5969f155a0/resource) (`f70fd79c-dc45-44b8-934d-3d5969f155a0`)
- S3: [高密度模块封装模流仿真技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ed1f8c5-8771-488a-8c50-eed69756b36b/resource) (`1ed1f8c5-8771-488a-8c50-eed69756b36b`)
- S19: [现代模具技术注塑成型原理与注塑模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ac013122-72f7-4641-9e09-d351575672bb/resource) (`ac013122-72f7-4641-9e09-d351575672bb`)
- S11: [橡塑挤出模具设计与工程模拟原著](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65f1961e-2cf8-43af-b1c8-05d8cf086d43/resource) (`65f1961e-2cf8-43af-b1c8-05d8cf086d43`)
- S23: [注塑成型原理与注塑模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c37e57fc-1b08-4531-80d0-3c32451cc063/resource) (`c37e57fc-1b08-4531-80d0-3c32451cc063`)
- S22: [软布基拉链注塑工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2a2601d-f3ae-48a3-9135-369774c02dc8/resource) (`c2a2601d-f3ae-48a3-9135-369774c02dc8`)
- S5: [表 8.5 Cross-WLF 黏度模型的材料常数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cd56e4d-f7bc-4929-b837-6a39c4b58782/resource) (`2cd56e4d-f7bc-4929-b837-6a39c4b58782`)
- S15: [注射模具设计工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c561f3e-564e-4bee-8457-ec7c6c9ae50f/resource) (`7c561f3e-564e-4bee-8457-ec7c6c9ae50f`)
- S17: [软布基拉链注塑工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95865a3e-8826-4e1d-b1ae-93b0e69a0823/resource) (`95865a3e-8826-4e1d-b1ae-93b0e69a0823`)
- S21: [高密度模块封装模流仿真技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b31623cd-b5fd-4d70-934f-c23778d719ce/resource) (`b31623cd-b5fd-4d70-934f-c23778d719ce`)
- S13: [汽车发动机底护板复合材料塑件的成型工艺优化及多尺度联合仿真](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79616081-176f-461e-958e-830cb51cb471/resource) (`79616081-176f-461e-958e-830cb51cb471`)
- S25: [2004年中国工程塑料加工应用技术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eff619a1-459e-4e03-a756-5799e4230034/resource) (`eff619a1-459e-4e03-a756-5799e4230034`)
- S18: [中国模具设计大典：第2卷 轻工模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a099800a-f71a-409a-9225-212af4ee3eb6/resource) (`a099800a-f71a-409a-9225-212af4ee3eb6`)
- S2: [Cross-WLF粘度模型系数对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18e23de3-8e9e-433c-af3f-c61c787ab6e6/resource) (`18e23de3-8e9e-433c-af3f-c61c787ab6e6`)
- S24: [Cross-WLF粘度模型系数对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb0e3204-2a3d-4065-a603-5b4278f20214/resource) (`cb0e3204-2a3d-4065-a603-5b4278f20214`)
- S27: [Cross WLF粘度模型系数对话框](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe285711-92f0-4094-9ed1-51caa2818f25/resource) (`fe285711-92f0-4094-9ed1-51caa2818f25`)
- S16: [软布基拉链注塑工艺参数优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/820896dc-1af8-4ee8-8da2-265745d86bc1/resource) (`820896dc-1af8-4ee8-8da2-265745d86bc1`)
- S6: [图5-6 Cross-WLF黏度模型参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31c9bdda-5fe1-4869-b1c0-88d211ed9d54/resource) (`31c9bdda-5fe1-4869-b1c0-88d211ed9d54`)
- S7: [图5.19 不同成型参数下单组分自增强制件的增强熔体粘度分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47a563eb-d3b9-4ca2-ad57-178325bd7355/resource) (`47a563eb-d3b9-4ca2-ad57-178325bd7355`)
- S14: [聚甲醛曲线构型齿轮注塑工艺优化方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c0bd11f-e65b-4303-a122-6a0e205609b5/resource) (`7c0bd11f-e65b-4303-a122-6a0e205609b5`)
- S1: [表 2.2 Cross-WLF 黏度模型常数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14a861df-57b1-41b2-bd02-ef8751c4d9a3/resource) (`14a861df-57b1-41b2-bd02-ef8751c4d9a3`)