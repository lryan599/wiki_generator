---
version: "v1"
generated_at: "2026-06-18T14:17:06+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 27
  source_quality_score: 0.86
  freshness_score: 0.79
  evidence_coverage_score: 1.0
---

P-Q²图（亦称PQ2图、p-Q²图、P·Q²图）是压铸领域专门用于同时反映压铸机特性、模具特性及系统工艺特性的分析线图[[S27,S2,S13]]。其核心原理基于流体力学伯努利定律：纵轴代表压射比压（P，常用单位MPa），横轴代表金属液流量的平方（Q²，常用单位(L/s)²）[[S9,S27]]。通过将原本的二次曲线关系转换为两条相交直线，P-Q²图大幅简化了人工判读的复杂度，为压铸机与压铸模之间的能量供需匹配分析提供了直观、科学的理论基础[[S1,S9]]。

## 构成与原理
P-Q²图主要由两条核心特性线构成。

**压铸机特性线（ML线，又称压力供给线/有效压力特性线）** 表征压铸机压射系统能够提供的压射能量供给能力[[S19,S18]]。其数学表达式为 P = P_max - (P_max/Q_max²)·Q²，是一条同时与纵轴（P轴）和横轴（Q²轴）存在截距的直线。其中，P_max为压射系统无液流运动时对应的最大压射比压，Q_max为压射系统空打时的等效最大金属液流量[[S28]]。该线所围成的区域可视作压铸机的理论可操作区域；调整储能器压力、速度阀开度或压射冲头直径，均会改变该直线的截距与斜率，从而改变机器的可操作范围[[S19]]。

**模具浇注系统需求线（DL线，又称压力需求线/模具特性线）** 表征指定浇注系统在不同充型流量下所需的压射压力需求[[S1,S23]]。其数学表达式为 P = ρ/(2·C_d²·A_g²)·Q²，是一条过坐标原点的直线。式中 ρ 为液态金属密度，C_d 为浇注系统流量系数，A_g 为内浇口截面积[[S1,S2]]。浇注系统流动效率越高、内浇口截面积越大，该直线的斜率越小[[S1]]。

当ML线与DL线绘制于同一坐标系中，两直线的交点即为系统工作点。该点定义了实际压射时的工作比压与流量，据此可进一步推导出充填时间、内浇口速度等关键工艺参数[[S28,S13]]。

## 图示
压铸P-Q²特性图（图示1）显示了计算机辅助模具设计场景下的典型构型：纵轴为金属压力Pm，横轴为流量平方Q²，图中两条交叉直线分别为压铸机特性线和模具需求线[[S9]]。

![计算机辅助设计中的压铸P-Q²特性图：压铸机特性线与模具需求线交点示意](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ec17461-e43e-4daf-80d9-1a34f332421a/resource)

更为完整的图表（如图示2）通常会叠加由充型速度和充型时间边界所界定的工艺窗口，以直接判定工作点是否落在合理参数范围内[[S11]]。

![完整压铸工艺pQ²特性曲线图：包含工艺窗口、压铸机特性线、模具特性线等标注区域](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bade4a7-d5ea-4ebe-8c25-9b6dbf43076a/resource)

## 核心工艺参量关联
P-Q²图的构建与判读依赖以下基本物理关系：
*   **内浇口速度与压力**：v_g = C_d·√(2P/ρ) [[S2,S12,S24]]
*   **流量、内浇口速度与面积**：Q = v_g·A_g [[S2,S26,S14]]
*   **流量、冲头速度与冲头面积**：Q = V_冲头·A_冲头 [[S6,S19,S24]]

## 工艺作用与应用
P-Q²图将压铸机、压铸模和压铸工艺有机地联系在一起，为合理选择压铸机、设计浇注系统、优化工艺参数提供了可靠的理论依据[[S1]]。其应用贯穿模具开发全流程：
*   **模具设计初期**：预判浇注系统与压铸机的能量匹配性，避免事后反复修模[[S27,S13]]。
*   **试模前校验**：核实所选压铸机型号与吨位能否满足模具的充型能量需求[[S4]]。
*   **批量生产优化**：精调压射工艺参数（如快压射速度）以拓宽工艺窗口[[S27]]。
*   **缺陷诊断**：当铸件出现质量问题时，反向定位模具浇口设计或机器参数设置上的不足[[S13]]。

## 判读准则与工艺窗口
P-Q²图的标准判读准则为：**压铸机特性线（ML）与模具特性线（DL）的交点（工作点），必须落在由最大/最小充填速度与最大/最小充填时间四条边界围成的工艺窗口（矩形区域）内**[[S4,S8]]。若工作点落入窗口内，则判定机模能量匹配，对应的工艺参数可接受[[S16]]；若工作点落在窗口之外（例如窗口左上侧），则表明压力过高，能量不匹配[[S10]]。

修正方法通常包括三种途径：
1.  **调整压射速度（二速阀开度）**，改变ML线位置[[S4]]。
2.  **更换压射冲头直径**，改变ML线斜率与截距[[S4]]。
3.  **修改内浇口截面积**，改变DL线斜率。适当增大内浇口面积可延长模具线在工艺窗口内的有效长度，提升系统工艺柔性，降低参数波动导致的废品风险[[S10,S4]]。

## 相关图表的区别
在压铸工艺分析中，存在几种相近的压力-流量图表，需加以区分：

| 图表类型 | 横轴参量 | 曲线形态 | 主要用途与特点 |
| :--- | :--- | :--- | :--- |
| **P-Q²图** | Q²（流量平方） | 两条均为直线 | 主流分析方法，判读便捷，专用于机模匹配与浇口面积优化[[S3,S2]] |
| **普通P-Q图** | Q（一次方流量） | 抛物线 | 早期简易参数粗校核工具，不便于精确匹配分析[[S15,S3]] |
| **PQ³图** | Q³ | - | 对应液压系统功率特性，用于压射系统动力性能深度标定，不直接用于浇口匹配[[S3]] |

## 合金适配参数
不同压铸合金因密度和流动特性差异，在P-Q²图计算中采用不同的流量系数C_d。该系数取值范围通常为0.4～0.8，其对模具需求线的斜率有直接影响[[S2,S1]]。

| 合金种类 | 典型流量系数 (C_d) |
| :--- | :--- |
| 铝合金 | 0.5 [[S2,S7]] |
| 镁合金 | 0.5 [[S2,S7]] |
| 锌合金 | 0.6 [[S2,S7]] |
| 铜合金 | 0.45 [[S7]] |

## 版本与软件实现
P-Q²图的应用经历了从手工到计算机辅助的演变：
*   **经典手动计算版本**：需人工代入伯努利公式、根据合金选定参数手绘两条直线。计算门槛高，结果精度受制于人工绘图[[S10]]。
*   **现代计算机辅助版本**：通过内置压铸机数据库与合金物性参数库，自动生成ML/DL线和工艺窗口，大幅降低使用门槛[[S10,S14]。市面上的商用或研究用工具包括：
    *   **DC-CALC**：基于Excel的PQ2专用压铸计算软件，可一键生成图表，并附带排气、合模力等计算功能[[S22]]。
    *   **C++版P-Q²绘图系统**：由国内高校自主开发，用于铝合金压铸工艺优化场景[[S10]]。
    *   **MAGMAsoft、AnyCasting等集成模块**：通用铸造CAE软件内置的PQ2分析功能，可结合充型模拟结果输出匹配结论[[S25]]。
    *   **压铸机厂商配套工具**：如Bühler等主流厂商随机附带的压射系统PQ2分析工具[[S4]]。

## 局限性
P-Q²图作为一种稳态分析工具，其应用存在一定边界：
*   **工艺覆盖范围有限**：P-Q²图专注于高速充填阶段，未涉及增压比压、增压速度、增压时间延时等后续的补缩与压实工艺维度，无法完整表征压铸全流程[[S13,S4]]。
*   **参数取值依赖性**：流量系数C_d是构建DL线的核心参数，但其准确值难以精确计算。实践中多依赖经验估算，其主观性会直接影响匹配分析的精度[[S4,S13]]。
*   **理想化假设**：该理论基于稳态、湍流、流体不可压缩等假设推导而来，在充填起始和结束的高速加/减速阶段，动态效应可能导致实际值与静态图线产生偏差[[S5]]。

## 行业引用
P-Q²图方法已被国内外权威专业文献采纳为标准分析手段。国内《压铸模具工程师手册》《压铸实用技术》《铝压铸成型及质量控制》《中国模具设计大典》等出版物均系统收录了其绘制步骤与机模匹配校验流程[[S17,S13]]。在国际上，ASM铝合金百科全书、NADCA关联技术文献、《Die Casting Engineer》期刊刊发的D. Zabel系列研究论文，以及澳大利亚CSIRO的原研技术文档，均明确推荐将此技术应用于浇口系统设计与压铸机选型[[S20,S5]]。

## Sources
- S27: [PQ2图对大型汽车压铸模具设计的验证及工艺的优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8eab351-f040-42e2-ae6d-ce9c2ebecd7c/resource) (`f8eab351-f040-42e2-ae6d-ce9c2ebecd7c`)
- S2: [PQ2图对大型汽车压铸模具设计的验证及工艺的优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0027172b-a065-42e1-afcd-c4e214a715fb/resource) (`0027172b-a065-42e1-afcd-c4e214a715fb`)
- S13: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e76b522-5a21-4668-b436-f3f301ac4fb0/resource) (`8e76b522-5a21-4668-b436-f3f301ac4fb0`)
- S9: [压铸机P-Q²特性图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ec17461-e43e-4daf-80d9-1a34f332421a/resource) (`5ec17461-e43e-4daf-80d9-1a34f332421a`)
- S1: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/001b38c3-f628-4cd4-ad16-7595e419ec87/resource) (`001b38c3-f628-4cd4-ad16-7595e419ec87`)
- S19: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b1a8e1de-9c2e-4763-8bbc-2fb847ae3ec1/resource) (`b1a8e1de-9c2e-4763-8bbc-2fb847ae3ec1`)
- S18: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afb6dff4-7505-4180-a43e-79abde8b6de9/resource) (`afb6dff4-7505-4180-a43e-79abde8b6de9`)
- S28: [computer aided injection mold design and manufacture__e9a0863baa](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa058087-ef65-460d-8ce1-a10838653285/resource) (`fa058087-ef65-460d-8ce1-a10838653285`)
- S23: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db8a436f-c12a-4079-96ac-07664556f28a/resource) (`db8a436f-c12a-4079-96ac-07664556f28a`)
- S11: [压铸工艺pQ²特性曲线图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bade4a7-d5ea-4ebe-8c25-9b6dbf43076a/resource) (`6bade4a7-d5ea-4ebe-8c25-9b6dbf43076a`)
- S12: [压力铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/783493ed-a55f-4311-a989-5f877f5c53f6/resource) (`783493ed-a55f-4311-a989-5f877f5c53f6`)
- S24: [铝合金压铸成型缺陷控制的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2d7f615-5f8b-4c2f-ab5b-c0b3e2661b29/resource) (`e2d7f615-5f8b-4c2f-ab5b-c0b3e2661b29`)
- S26: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebce70ec-8f31-472f-ba31-6ab43bfd9077/resource) (`ebce70ec-8f31-472f-ba31-6ab43bfd9077`)
- S14: [a constructed pq2 chart for calculating the optimized process parameters__19bf79e1c2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a62d5c5-51ba-4cc1-9ed6-581fbed3e057/resource) (`9a62d5c5-51ba-4cc1-9ed6-581fbed3e057`)
- S6: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a6bed9f-0f3a-4421-a492-e70381d9a72e/resource) (`4a6bed9f-0f3a-4421-a492-e70381d9a72e`)
- S4: [PQ2图对大型汽车压铸模具设计的验证及工艺的优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12430cce-8d10-4eed-a87f-52af6103404f/resource) (`12430cce-8d10-4eed-a87f-52af6103404f`)
- S8: [图3.10 P-Q²图的工艺窗口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b6dd4c9-e116-493c-906a-25bf8208ae54/resource) (`5b6dd4c9-e116-493c-906a-25bf8208ae54`)
- S16: [图4.4压铸P-Q图表分析图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab271901-48bf-442f-a565-78b00039162b/resource) (`ab271901-48bf-442f-a565-78b00039162b`)
- S10: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f9cdf10-a328-4dfc-b35a-59f9c6fa5567/resource) (`5f9cdf10-a328-4dfc-b35a-59f9c6fa5567`)
- S3: [a constructed pq2 chart for calculating the optimized process parameters__19bf79e1c2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0af9d779-0d29-4231-925b-6d937594a434/resource) (`0af9d779-0d29-4231-925b-6d937594a434`)
- S15: [压铸工艺中充填过程压力与流量关系的P-Q图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1c40e06-5fda-4ca6-a9eb-5a719c33f019/resource) (`a1c40e06-5fda-4ca6-a9eb-5a719c33f019`)
- S7: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b9e8a36-548e-4c0d-b40e-a0adddb1b79a/resource) (`4b9e8a36-548e-4c0d-b40e-a0adddb1b79a`)
- S22: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3db0f7e-ced8-42c6-b7fb-fc52141175ae/resource) (`d3db0f7e-ced8-42c6-b7fb-fc52141175ae`)
- S25: [CAE技术在厚壁铸件压铸工艺中的应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e95fb472-80ee-4a24-85de-f1d7e3f4dd09/resource) (`e95fb472-80ee-4a24-85de-f1d7e3f4dd09`)
- S5: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1dc854ee-15f3-4051-8192-887027b4c864/resource) (`1dc854ee-15f3-4051-8192-887027b4c864`)
- S17: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af7ad1f5-a1bf-4af4-bad8-59bd25a7ff80/resource) (`af7ad1f5-a1bf-4af4-bad8-59bd25a7ff80`)
- S20: [a review of design parameters and machine performance for improved die c__7ef893f873](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5af68c5-9ab7-4e84-9867-9f9b021c951e/resource) (`c5af68c5-9ab7-4e84-9867-9f9b021c951e`)