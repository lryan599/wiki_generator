---
version: "v1"
generated_at: "2026-06-21T05:55:17+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 18
  source_quality_score: 0.83
  freshness_score: 0.92
  evidence_coverage_score: 1.0
---

## 概述

EasyCast是中北大学有色金属液态成型中心（教育部共建铝镁材料研发应用协同创新中心）赵宇宏教授、侯华教授团队自主开发的铸造过程数值模拟软件，属于国内主流自主研发铸造CAE软件之一，与华铸CAE、FT-Star等软件同列国内自主可控仿真产品序列[[S13,S3,S9]]。该软件集三维实体造型文件接口、计算网格剖分、铸造过程仿真、铸造缺陷预测及结果VTK显示为一体，可为砂型铸造、金属型铸造、熔模精密铸造、压力铸造、低压铸造、差压铸造、消失模铸造等多种铸造工艺提供充型流场与凝固温度场的全流程仿真支持[[S7,S9,S1]]。

## 产权与历史

EasyCast的计算机软件著作权首次登记于2009年5月25日，登记号为2009SR019211，软件全称"金属铸造模拟系统软件"，曾用简称EMC软件，著作权人为赵宇宏、侯华、牛晓峰[[S15]]。该证书在2012版《液态成型工艺及CAD》教材中以扫描件形式正式收录[[S15]]。

![图9-36 中北大学液态成型技术研究中心注册的铸造过程模拟及优化集成系统软件EASYCAST软件著作权登记证书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7862dcb3-7a8c-4862-b9a1-78e47866c3bd/resource)

截至2012年，EasyCast已形成7个独立商用CAE模块，分别对应砂型重力铸造、砂型低压铸造、金属型重力铸造、金属型低压铸造、熔模精密铸造、压力铸造、差压铸造、消失模铸造共8类铸造工艺场景[[S1]]。

## 核心技术

### 数值方法与网格剖分

EasyCast核心数值方法为有限差分法（FDM），将偏微分方程中的微分操作离散为相邻网格之间的差商，以此完成三维模型的网格剖分与物理场求解[[S4,S8]]。公开测试场景中，采用4mm均匀网格尺寸对镁合金薄壁铸件剖分时，可支持约160万单元规模的计算，铸件最小壁厚位置至少分布2～3层网格，满足仿真精度要求[[S20]]。

### 后处理与可视化

EasyCast的后处理模块基于VTK（Visualization Toolkit）作为底层技术开发可视化功能，采用隐式算法充分调用3D加速卡硬件性能，通过双缓冲技术实现视图自由操作与高速渲染[[S4]]。后处理可对充型流场、凝固温度场、缺陷分布结果完成可视化输出，并配套完整的铸件质量评估体系[[S4]]。

![EasyCast模拟铝合金舱体铸件凝固过程（凝固20%）可视化结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/435033aa-0b87-4465-ae3e-72af7c28354a/resource)

## 功能与能力

### 物理场与缺陷预测

EasyCast支持充型流场与凝固温度场的耦合计算，可预测的典型铸造缺陷包括浇不足、冷隔、缩孔、缩松，可辅助完成铸造工艺方案的量化评价与迭代优化[[S1,S4]]。

### 材料数据库

软件内置开放材料数据库，预存200余种铸钢、铸铁、铸造有色合金等材质的温度相关热物理性能参数，预置ZM5镁合金、ZL101A铝合金等常见工业铸造合金的完整参数，同时支持用户自主添加新材料参数[[S1,S18]]。

### 边界条件与充型参数设置

在边界条件设置方面，EasyCast在Boundary Selection对话框中可按铸件不同接触界面类型直接指定预设传热系数。实测场景中，镁合金铸件-砂型接触界面选C600档位，铸件-冷铁接触界面选C10000档位完成赋值[[S20]]。

在充型参数方面，以低压铸造为例：保压压力一般在充型压力的基础上增加6～30kPa；保压时间以金属液凝固后浇道残留长度约为20mm为判定依据。公开测试案例中，当充型压力取20kPa时，对应保压压力取40kPa、保压时间取130s[[S20]]。

### 系统环境

2012年公开版本的推荐硬件配置为PIV2.8以上CPU、内存≥512MB、硬盘≥40GB，适配Windows2000、WindowsNT、WindowsXP等主流操作系统，全中文界面友好[[S1]]。

## 应用范围与用户

EasyCast覆盖航空、汽车、军工、通用机械等领域，截至2012年已拥有40余家工业及科研用户[[S1]]。国内用户包括西安飞机制造集团、成都飞机制造集团、哈尔滨东安发动机集团、东风汽车精密铸造公司、兵总山西大同70研究所等；海外用户包括日本埼玉工业大学[[S1]]。

## 工业验证与对比

### 独立验证案例

EasyCast在多类工业场景中已获得公开验证：
- 对580kg铸钢阀体件进行模拟优化，实现一次性浇注成功[[S16]]；
- 镁合金隔板低压铸造模拟结果与NovaCAST的温度场、缺陷预测结果一致[[S6,S9]]；
- 大型复杂铝合金舱体低压铸造模拟结果与ProCAST的流场、凝固场、缩孔分布计算结果近似，充型过程无飞溅，顺序凝固特征匹配度高，缺陷定位吻合[[S4]]。

![NovaCAST、EasyCast、JSCast三款软件大型铸件凝固温度场模拟及缺陷预测对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8be92f3-4501-4d64-88d3-3bbee638a6da/resource)

### 国内主流软件对比

EasyCast所属CASTsoft系列与国内其他主流铸造模拟软件的技术参数对比如下[[S8]]：

| 软件名称 | 开发单位 | 模拟算法 | 核心功能 | 适用铸造工艺 |
|---------|---------|---------|---------|------------|
| CASTsoft（EasyCast） | 中北大学 | FDM | 传热、流动 | 砂型、消失模、离心、压铸等多种工艺 |

## EasyCast-AI变体

EasyCast-AI（也称EasyCastAI智能平台）是在基础版EasyCast数值模拟能力之上新增全链路AI辅助设计模块的高级变体版本，包含以下五大核心功能[[S22,S11,S2]]：

1. **ML建模**：支持DT、RF、SVM、LASSO、LightGBM、XGBoost共6种机器学习算法，通过填充空值、one-hot编码完成数据预处理，支持PCA降维（保留90%关键特征），采用遗传算法GA自动搜索最优超参数，以R²、MSE、MAE多维度评估模型精度，支持模型以pkl格式保存[[S11]]；

2. **相似工艺检索**：基于铸件几何特征与工艺特征匹配历史数据库中的成功案例，快速生成参考工艺方案[[S11,S2]]；

3. **智能浇注系统**：仅需输入铸件体积即可通过遗传算法自动计算合理浇道尺寸与内浇道数量（目前仅支持差压铸造）[[S11,S2]]；

4. **材料性能预测**：基于成分与工艺条件预测合金抗拉强度UTS[[S11]]；

5. **铸造工艺优化**：采用LHS采样与贝叶斯迭代的方式自动遍历参数空间，迭代得到最优铸造工艺参数组合[[S11,S2]]。

![EasyCast-AI智能辅助铸造工艺设计操作界面（ML建模、浇注系统设计、UTS预测模块）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9f93270-dc7f-401d-917a-b05efe40b4af/resource)

基础版EasyCast与EasyCast-AI的核心差异在于：基础版聚焦于基于FDM的数值模拟与后处理可视化[[S4,S9]]，EasyCast-AI在此基础上融入机器学习驱动的智能设计、检索与优化能力，形成从数据预处理到自动迭代优化的完整智能工作流[[S11,S2]]。

## 优势与局限

### 与国际主流软件的对比

EasyCast作为国产FDM架构软件，其模拟精度与MAGMA、ProCAST、AnyCasting、Flow-3D等国际主流商业铸造仿真软件处于同一水准[[S4,S21]]。与其他主流软件的技术特征对比如下[[S10,S19]]：

| 软件 | 算法架构 | 核心优势 | 局限 |
|------|---------|---------|------|
| MAGMA（德国） | 全FDM | 计算速度快，薄壁件分析能力强，不同工艺有专用模块 | — |
| ProCAST（美国/法国） | 有限元法 | 热-流动-应力全耦合，多物理场耦合精度高 | 前处理网格划分效率偏低 |
| AnyCasting（韩国） | — | 网格生成快，整体计算效率高 | — |
| Flow-3D（美国） | — | 自由表面追踪精度高 | 计算耗时偏长 |
| EasyCast（中国） | FDM | 计算效率优于ProCAST，使用与运维成本远低于国外同级别商用软件 | 计算效率低于MAGMA与AnyCasting |

EasyCast可完全覆盖上述国际主流软件对普通工业铸件的基础仿真能力（流场、温度场、缺陷预测），可作为低成本的国产替代方案使用[[S19,S4,S21]]。

### 局限性

两软件对比研究中指出，EasyCast与NovaCAST在缩孔预测尺寸和形状上存在细微差异，可能原因包括：边界条件设置方式不同（EasyCast采用传热系数，NovaCAST通过气隙尺寸等效计算传热系数）、充型参数设置差异（EasyCast需设置保压时间和保压压力，NovaCAST需设置加压时间和保压压力）、以及底层数值方法不同（EasyCast采用FDM，NovaCAST采用有限体积法）[[S6]]。这些差异不影响工艺改进结论的一致性，但需在工程应用中予以关注。

## Sources
- S13: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a7635ac-7a17-4bac-8382-e8460379042a/resource) (`4a7635ac-7a17-4bac-8382-e8460379042a`)
- S3: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11acc015-c1cd-4f4b-8106-56e763e77b18/resource) (`11acc015-c1cd-4f4b-8106-56e763e77b18`)
- S9: [大型铸件铸造工艺及数值模拟研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32eda958-1c7f-4b03-ba14-935876ca4c74/resource) (`32eda958-1c7f-4b03-ba14-935876ca4c74`)
- S7: [镁合金隔板铸件低压铸造工艺数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e0eb03c-961a-487b-b348-78dd1b1bcb68/resource) (`2e0eb03c-961a-487b-b348-78dd1b1bcb68`)
- S1: [TextNode198](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b9c25de-1a1a-4eaa-aa14-5044db9030da/resource) (`0b9c25de-1a1a-4eaa-aa14-5044db9030da`)
- S15: [图9-36 中北大学液态成型技术研究中心注册的铸造过程模拟及优化集成系统软件EASYCAST](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7862dcb3-7a8c-4862-b9a1-78e47866c3bd/resource) (`7862dcb3-7a8c-4862-b9a1-78e47866c3bd`)
- S4: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c692f6c-504d-412e-8d09-f277231ccc90/resource) (`1c692f6c-504d-412e-8d09-f277231ccc90`)
- S8: [表1.4 国内主流铸造模拟软件及应用范围简介](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32636b5d-5308-473d-a977-6ab2c366d4cf/resource) (`32636b5d-5308-473d-a977-6ab2c366d4cf`)
- S20: [镁合金隔板铸件低压铸造工艺数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b9c0502c-5ac7-4d35-a08b-39195e78b333/resource) (`b9c0502c-5ac7-4d35-a08b-39195e78b333`)
- S18: [Fig.3-11(c) CLIP-PDK_B模型低压铸造铝合金轮毂缩孔分布模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95902f58-6ca7-4b04-8b8c-8616f56e1896/resource) (`95902f58-6ca7-4b04-8b8c-8616f56e1896`)
- S16: [特种铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/88a7b1d5-63a5-4d42-99ad-4b7962b710b3/resource) (`88a7b1d5-63a5-4d42-99ad-4b7962b710b3`)
- S6: [镁合金隔板铸件低压铸造工艺数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cc321eb-d978-4c9e-a2c0-8f738f652998/resource) (`2cc321eb-d978-4c9e-a2c0-8f738f652998`)
- S22: [图6-6 ML建模、浇注系统设计和UTS预测界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9f93270-dc7f-401d-917a-b05efe40b4af/resource) (`f9f93270-dc7f-401d-917a-b05efe40b4af`)
- S11: [TextNode74](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/359772cd-4861-45c8-9653-3165d2fb9fcc/resource) (`359772cd-4861-45c8-9653-3165d2fb9fcc`)
- S2: [TextNode75](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/108e9018-4c23-4aa5-835c-d3d8161972b0/resource) (`108e9018-4c23-4aa5-835c-d3d8161972b0`)
- S21: [图4 不同铸造CAE软件模拟铸件凝固过程及缺陷预测结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8be92f3-4501-4d64-88d3-3bbee638a6da/resource) (`c8be92f3-4501-4d64-88d3-3bbee638a6da`)
- S10: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34173a8e-f6f1-4181-9188-514d82f794e5/resource) (`34173a8e-f6f1-4181-9188-514d82f794e5`)
- S19: [铸造过程数值模拟软件对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af04200c-5399-432a-a5e0-5f748075c706/resource) (`af04200c-5399-432a-a5e0-5f748075c706`)