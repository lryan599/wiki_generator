---
version: "v1"
generated_at: "2026-06-18T14:14:12+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 22
  source_quality_score: 0.86
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

FT-Star（亦称 FT-STAR、铸造之星）是由清华大学机械系 CFIT 研究室开发的真三维数值凝固模拟软件包 [[S23,S10,S5]]。该软件为国内铸造领域首个实现商品化的自主知识产权 CAE 系统，前身是基于 XENIX 操作系统的 FTSolve6.0，后续升级至 Windows 平台，显著提升了操作友好性与可维护性 [[S23,S10,S5]]。

FT-Star 与华铸 CAE、EasyCast、CASTSOFT 等共同组成国产主流铸造数值模拟软件产品线，其部分功能达到同期国外同类软件水平，相关研究与应用被多部行业手册及核心期刊收录 [[S5,S1,S21]]。

## 版本与发展

目前可查的公开迭代版本为 **FT-Star2003**，于 2006 年在中国大型铸锻件制造技术发展论坛上公开发布 [[S3]]。该版本较此前版本进行了多项功能增强，主要包括 [[S3,S23,S10]]：

- 新增 STL 造型文件处理能力
- 铸钢热裂预测
- 球墨铸铁微观组织模拟
- 缩孔缩松缺陷的 X 射线风格可视化显示

尚无法确认 2003 版之后是否存在更高版本或后续软件更名情况 [待核实]。

## 核心功能与技术特点

### 数值方法与缺陷预测

FT-Star 以**显式有限差分法（FDM）** 为核心数值求解方法，将铸件三维实体离散为有限差分网格单元，进行三维传热计算 [[S6,S23]]。软件内置由日本学者新山英辅提出的 **G/√R（温度梯度/凝固速率平方根）判据**，用于定量预测铸件缩孔、缩松缺陷的分布范围与体积 [[S8]]。该判据亦被 MAGMAsoft、ProCAST 等国际主流软件采用 [[S8]]。研究指出，在实际应用中临界判据取值随铸件尺寸差异较大，可通过补充多种缩孔缩松判据进一步提升预测精度 [[S8]]。

### 功能模块构成

FT-Star 的完整功能架构包含五大模块 [[S23,S10,S16]]：

1. **三维几何实体造型模块** – 支持铸件及铸型系统的三维建模
2. **前处理（有限差分网格自动剖分）模块** – 进行网格划分与单元标识
3. **数据准备模块** – 设置边界条件、初始温度、热物性参数等
4. **计算分析模块** – 执行流场、温度场、应力场、微观组织的数值求解
5. **后置处理模块** – 提供可视化结果展示与分析

### 支持的合金材质

根据公开资料，FT-Star 已可处理的主要合金材质包括 [[S23,S22]]：

- 铸钢
- 球墨铸铁
- 灰铸铁
- 铸造铝合金

该列表尚不完整，对于其他合金（如镁合金、钛合金、铜合金等）的支持情况尚无公开可查细节 [待核实]。

### 图形界面与可视化

软件基于 Windows 原生环境开发，界面良好、操作便捷 [[S23,S10]]。后处理功能支持缩孔缺陷的 X 射线风格可视化，可直观呈现缺陷在铸件内部的三维分布 [[S23,S10]]。软件兼容行业通用的 STL 三维模型接口，可对接 Pro/Engineer、UG、SolidWorks、AutoCAD 等主流 CAD 软件，降低建模适配成本 [[S7,S23]]。

**关于软件界面与模拟结果图像**：目前未检索到公开可引用的 FT-Star 软件主界面、充型流场或温度场模拟结果的高清图像资源。2006 年 FT-Star2003 应用论文虽提及界面及模拟结果图，但尚未公开高清版本 [待核实] [[S3]]。

## 支持的铸造工艺

FT-Star 支持多种常规铸造工艺的模拟分析 [[S23]]：

- 砂型铸造
- 金属型铸造
- 熔模铸造
- 高压/低压铸造
- 精密铸造
- 蜡模铸造
- 连续铸造

### 压铸（die casting）模拟能力说明

FT-Star 在公开文献中被列入可进行压铸工艺下温度场计算的软件范围 [[S26,S22]]，部分资料亦将其归为兼顾高压铸造的国内 CAE 系统 [[S23]]。然而，针对压铸过程特有的**慢压射、快压射、增压阶段模拟**、**压射曲线控制**、**模具热平衡循环分析**等专属于压铸的功能细节，**尚无公开可检索的权威文献、软件官方资料或行业报道予以明确说明** [[S26,S22]]。关于 FT-Star 是否具备上述压铸专属模拟能力的结论需保持审慎，并以软件开发单位的最新声明为准 [待核实]。

## 应用实例与工业验证

### 已见诸报道的应用案例

1. **大型铸钢件工艺优化**  
   2006 年发表的研究中，使用 FT-Star2003 对大型铸钢件进行计算机辅助工艺设计与优化 [[S3]]。

2. **电机机座铸件工艺筛选**  
   2012 年《热加工工艺》刊载的工作中，利用 FT-Star 对电机机座铸件的流动场和温度场进行模拟，对比不同浇注方案，最终确定“中间浇注”为最优工艺，用于指导实际生产 [[S5,S3]]。

### 压铸应用案例缺失

现有公开可检索资料中 **未收录 FT-Star 应用于国内压铸制造企业的落地实例、针对压铸件质量控制的专项验证以及对应的工业效果信息**，该部分内容暂无证可循 [[S14]]。

## 与同类软件的对比

下表将 FT-Star 与几款国内外主流铸造 CAE 软件进行横向比较，资料来源为多项公开文献归纳 [[S16,S11,S12,S17,S15,S19,S23]]。

| 软件名称 | 开发方/国别 | 核心数值方法 | 支持模拟物理场 | 主要功能特点 | 典型适用工艺 |
|----------|--------------|---------------|----------------|--------------|----------------|
| FT-Star (FT-STAR) | 清华大学，中国 | 有限差分法（FDM） | 流场、温度场、应力场、微观组织 | 国内首个商品化铸造模拟软件；G/√R判据缩孔预测；X射线显示缺陷；Windows界面友好 | 砂型铸造、金属型铸造、熔模铸造、高/低压铸造、精密铸造、连续铸造等 |
| ProCAST | ESI，法国 | 有限元法（FEM） | 流场、温度场、应力场、电磁场等 | 多物理场耦合能力强；模拟精度高；适应几乎所有铸造工艺；几何适应性强 | 砂型铸造、熔模铸造、高压铸造、离心铸造、连铸等 |
| MAGMASOFT | MAGMA，德国 | 有限差分法（FDM） | 流场、温度场、应力场、微观组织 | 缺陷预测突出；模块化程度高；计算速度快；薄壁件分析能力强；配备专用工艺模块 | 低压铸造、高压铸造、铸铁、铸钢、半固态等 |
| AnyCasting | AnyCasting，韩国 | 有限体积法（FVM） | 流场、温度场、应力场 | 易用性高；计算速度快；仅限Windows平台；模拟精度略低于ProCAST | 多种典型铸造工艺 |
| 华铸CAE (InteCAST) | 华中科技大学，中国 | 有限体积法（FVM） | 流场、温度场、耦合计算 | 自动网格剖分效率高（可达千万级网格）；支持72种材质序列；后处理可视化丰富；拥有压铸等专用模块 | 砂型铸造、金属型铸造、低压铸造、压铸、熔模铸造等 |

## 技术局限性

### 方法层面的通用局限

FT-Star 所采用的基于欧拉固定有限差分网格的方法存在若干通用性限制：对复杂铸件的网格划分要求较高；无法有效追踪物质质点在流动过程中的运动路径；当网格出现剧烈畸变时，可能导致计算精度下降甚至运算终止 [[S2]]。

### 软件专属局限的公开信息缺失

有关 FT-Star 在 **多物理场耦合能力短板**、**计算效率的量化瓶颈**、**压铸专属功能模块缺陷** 等方面的定制化技术局限性，目前尚无公开可查的权威描述 [[S4]]。关于该软件在对比中的功能缺口与适用边界，尚需进一步从开发方或深度用户案例中获得佐证。

## 相关图示说明

由于当前未能获取可直接引用的 FT-Star 软件界面截图或流场/温度场模拟结果图（见上文“图形界面与可视化”部分），此处暂不提供该类配图。如需为页面补充针对压铸工艺过程的背景示意图，可考虑采用以下两类已公开的图示资源，但须注意它们并非直接来源于 FT-Star 软件：

- **压铸机分类示意图**：清晰展示冷室压铸机（卧式、立式、全立式）与热室压铸机的分类结构，用于辅助理解压铸工艺设备类型，来源为《特种铸造生产工艺与装备入门与精通》（2011）[[S25]]。  
  `![压铸机分类示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dfd750b0-6cb2-447c-ba84-cc863a4655a3/resource)`

- **影响压铸件质量的主要因素示意图**：覆盖压铸机、压铸模具、压铸工艺、金属液等多维度作用关系，适合作为 FT-Star 压铸件质量缺陷预测功能说明的背景支撑图示，来源为《压铸技术与生产》（2008）[[S9]]。  
  `![影响压铸件质量的主要因素示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ae08dd3-820c-4597-9432-0e4f9a16e77d/resource)`

## Sources
- S23: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d34ff37e-1b1e-4988-b2e7-86c3f17e4ff4/resource) (`d34ff37e-1b1e-4988-b2e7-86c3f17e4ff4`)
- S10: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58ea8fb5-232c-48b4-9a7c-03034cd5c0bd/resource) (`58ea8fb5-232c-48b4-9a7c-03034cd5c0bd`)
- S5: [大型铸件铸造工艺及数值模拟研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32eda958-1c7f-4b03-ba14-935876ca4c74/resource) (`32eda958-1c7f-4b03-ba14-935876ca4c74`)
- S1: [材料加工工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/078124b8-4f7e-4a47-a3ec-338bab4a0f15/resource) (`078124b8-4f7e-4a47-a3ec-338bab4a0f15`)
- S21: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad14679d-a737-4681-a5af-3dfc99d408a5/resource) (`ad14679d-a737-4681-a5af-3dfc99d408a5`)
- S3: [大型铸件铸造工艺及数值模拟研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2532d8cf-5e11-42ea-a33c-b604c1a632f3/resource) (`2532d8cf-5e11-42ea-a33c-b604c1a632f3`)
- S6: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39cbaeb5-45df-4980-b35f-54bde14d26f3/resource) (`39cbaeb5-45df-4980-b35f-54bde14d26f3`)
- S8: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3db330a1-c305-46b5-bc9d-2068fd494dd9/resource) (`3db330a1-c305-46b5-bc9d-2068fd494dd9`)
- S16: [表1.1 国内外主流铸造模拟软件[65]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7db5a11c-f301-4cd6-86f1-1813d7ea09ac/resource) (`7db5a11c-f301-4cd6-86f1-1813d7ea09ac`)
- S22: [模具设计基础及模具cad](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4411007-a70c-47a2-b768-9b757d9ba2c9/resource) (`b4411007-a70c-47a2-b768-9b757d9ba2c9`)
- S7: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3d5fe521-b4f2-40a1-9e3d-63068327d83b/resource) (`3d5fe521-b4f2-40a1-9e3d-63068327d83b`)
- S26: [中国模具设计大典 第5卷 铸造工艺装备与压铸模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f75c0f01-61a3-4342-959e-b373e6f28dc5/resource) (`f75c0f01-61a3-4342-959e-b373e6f28dc5`)
- S14: [基于压铸工艺的铝合金车门结构设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7588c853-0f4a-40c7-82b3-348ad9c35789/resource) (`7588c853-0f4a-40c7-82b3-348ad9c35789`)
- S11: [表1.4 国内外主要铸造模拟软件一览表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5d0ebb9c-b830-4b69-ae3c-37b745fe5d10/resource) (`5d0ebb9c-b830-4b69-ae3c-37b745fe5d10`)
- S12: [表2.1 主流铸造数值模拟软件对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62ad51a3-c595-452b-8c7d-bff26d5f2a5f/resource) (`62ad51a3-c595-452b-8c7d-bff26d5f2a5f`)
- S17: [TC4合金非对称翼型受油管熔模精密铸造工艺及凝固特性研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8385eca2-3951-4e3d-a470-d4cedcd6d253/resource) (`8385eca2-3951-4e3d-a470-d4cedcd6d253`)
- S15: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a62dd6c-7a87-47ef-888c-1374e8938011/resource) (`7a62dd6c-7a87-47ef-888c-1374e8938011`)
- S19: [压铸工艺及模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/986bc2e1-cdd8-4be3-87e7-4242aff793d1/resource) (`986bc2e1-cdd8-4be3-87e7-4242aff793d1`)
- S2: [基于SPH法的压铸充型过程模拟及冷隔模型构建](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11112fec-3007-4b46-875d-6e5db2cafb61/resource) (`11112fec-3007-4b46-875d-6e5db2cafb61`)
- S4: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32797bce-62cb-47e9-a56b-d3d717e07bf1/resource) (`32797bce-62cb-47e9-a56b-d3d717e07bf1`)
- S25: [图3-21 压铸机分类](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dfd750b0-6cb2-447c-ba84-cc863a4655a3/resource) (`dfd750b0-6cb2-447c-ba84-cc863a4655a3`)
- S9: [影响压铸件质量的主要因素示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ae08dd3-820c-4597-9432-0e4f9a16e77d/resource) (`4ae08dd3-820c-4597-9432-0e4f9a16e77d`)