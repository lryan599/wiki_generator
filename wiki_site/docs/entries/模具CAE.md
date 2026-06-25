---
version: "v1"
generated_at: "2026-06-19T03:57:06+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 60
  source_quality_score: 0.85
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

模具CAE在压铸领域特指**压铸模具计算机辅助工程**（Computer-Aided Engineering for Die Casting Molds），是以计算力学、传热学、流体力学等为理论基础，面向高压压铸（HPDC）场景的数值模拟技术 [[S17,S52,S59]]。其核心范畴包含三大模拟模块：压铸件充型流动场数值模拟、压铸模与压铸件温度场数值模拟、压铸模与压铸件应力场数值模拟 [[S17]]。

压铸CAE与塑料模具CAE存在本质差异：前者面向高温金属液高速高压充型，求解高雷诺数金属湍流、大潜热凝固相变、循环热疲劳等物理场；后者面向低黏度聚合物充型，侧重收缩率适配与保压应力变形分析，二者在边界条件、材料物性库与核心算法上显著区分 [[S12,S50,S56]]。

## 工艺作用

压铸CAE可替代传统经验试错法，直接覆盖多项典型试模痛点 [[S17,S52,S59]]：

- **缺陷预判**：提前预测流痕、浇不足、气孔、缩孔缩松等缺陷的类型、位置与严重程度 [[S46,S13,S3]]
- **系统优化**：完成浇排系统迭代优化 [[S13,S46]]
- **模具评估**：辅助评估模具热疲劳裂纹、冲蚀失效风险与服役寿命 [[S17,S3,S13]]
- **效率提升**：大幅减少试模迭代次数，缩短开发周期 [[S13]]

## 工作流程

压铸CAE的行业通用流程分为三大阶段 [[S30,S19,S62]]：

### 前处理

- 导入压铸装配体STL等中性格式几何模型 [[S30,S62]]
- 进行面网格与体网格划分 [[S19,S62]]
- 指定合金与模具材料的热物性参数、力学属性 [[S19,S30]]
- 设置充型边界、温度边界、压力边界等工艺条件 [[S19,S30]]

![压铸CAE系统总体组成架构，展示三维实体建模、前处理、温度场计算、流场计算、后处理五个核心模块](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ccb8195-3297-451e-b995-00b9619c3184/resource) [[S27]]

### 求解计算

- 充型流场求解（速度场、压力场、温度场）
- 凝固温度场求解
- 热应力耦合求解
- 循环多周期计算以获得模具准稳态热平衡状态 [[S44,S16]]

### 后处理

- 充型过程动画回放
- 云图渲染（温度场、速度场、应力场等）
- 特征点温度/压力/应力曲线提取
- 缺陷判据判定与结果输出 [[S19,S30]]

**简化求解策略**：对于流动长度小于300 mm、临界壁厚1.4 mm的镁合金压铸件，可采用纯充型求解与纯凝固求解的分阶段计算策略，在保证精度的前提下大幅降低计算耗时 [[S4]]。

## 工艺参数与边界条件

### 常用合金密度参数

压铸CAE材料库默认参考的合金热物性密度参数 [[S26]]：

| 合金种类 | 默认密度 (kg/m³) |
|---------|---------------|
| 铝合金 | 2700 |
| 锌合金 | 6500 |
| 镁合金 | 1700 |
| 铜合金 | 8400 |

### 镁合金工艺参数推荐范围

镁合金压铸CAE工艺参数的行业推荐取值范围 [[S51]]：

| 参数 | 推荐范围 |
|------|---------|
| 浇注温度 | 640~730 ℃（常规工况优先640~690 ℃） |
| 模具预热温度 | 180~260 ℃ |
| 压射速度 | 0.3~5 m/s |
| 增压比压 | 30~50 MPa |

### 典型验证级输入参数

ALSI9CU3铝合金薄壁件压铸CAE参考输入参数示例：熔体浇注温度650 ℃，铸型初始温度150 ℃，合金最小流动温度610 ℃，平均壁厚3 mm工况下理论充型时间0.083 s，推荐压射比压50 MPa [[S42]]。

Mg-AM50镁合金压铸CAE实测校准参数：模具材料H13钢，界面换热系数1000 W/(m²·K)，铸型外表面空冷边界（室温20 ℃），浇注温度670 ℃，模具预热温度200 ℃，压射速度1.6 m/s，压射压力50 MPa，模拟终止温度350 ℃ [[S49,S51]]。

### 界面换热系数

压铸CAE中不同界面的换热系数通用参考取值区间 [[S2,S41,S18,S31,S15]]：

| 界面类型 | 换热系数范围 [W/(m²·K)] |
|---------|-------------------|
| 铸件−模具界面 | 1000~20000 |
| 模具装配接触面 | 1000~1500 |
| 模具−自然空气 | 10~20 |
| 模具−脱模剂 | 100~1000 |
| 模具−冷却水（常规流速） | ≈5000 |

界面换热系数受铸件壁厚与模具初始温度影响：铸件壁厚越大，换热系数越高；模具预热温度越高，换热系数越低 [[S15]]。

### 大型一体化压铸专用参数

大型一体化压铸后车体CAE模拟专用工艺参数示例 [[S57]]：

| 参数项 | 数值 |
|--------|------|
| 合金材料 | HA1-H铝合金 |
| 真空度 | 50 mbar |
| 压室直径 | 250 mm |
| 增压压力 | 28 MPa |
| 浇注温度 | 690 ℃ |
| 模具初始温度 | 180 ℃ |
| 压室填充率 | 41.2% |

## 缺陷预测

### 卷气/裹气缺陷

高精度判定方案：采用同时考虑空气可压缩性与熔体表面张力的两相流模型，仿真结果与实测水模拟试验吻合度最高。该方案可将卷入空气分类为宏观气泡与弥散微观气泡，分别追踪输出，准确标记宏观卷气缺陷的空间位置与体积占比 [[S68,S32]]。

### 缩孔缩松缺陷

通用定量预测方法 [[S61,S23,S55]]：

1. **Niyama判据**：满足 G/√R ≤ C<sub>Niyama</sub> 时判定缩松风险，其中G为局部温度梯度，R为冷却速度 [[S61]]
2. **残余熔体模数法**：AnyCasting等商用软件的Probabilistic Defect Parameter模块直接输出区域缺陷概率分布，预测结果与实际探伤吻合度高 [[S23,S55]]

### 流动类缺陷

充型时序结果中最后填充的区域为卷气、冷隔、浇不足高风险位置，应在对应区域设置溢流槽与排气通道；若熔体前沿分流后汇合处过冷度高于合金固相线温度，判定冷隔风险；若熔体前沿未到达型腔远端即提前凝固，判定浇不足缺陷 [[S29,S37]]。

### 热应力与模具寿命评估

需完成至少5个连续压铸生产循环的仿真计算，使模具温度场达到准稳态后再开展评估，重点关注浇注系统正对型腔区域的温度梯度峰值及喷涂阶段模具表面最大拉应力，直接支撑模具热疲劳寿命预判与热裂纹风险评估 [[S44,S16]]。

## 仿真验证规范

### 温度场验证

在模具目标测点预埋热电偶，连续采集多轮压铸生产周期的模具温度数据，迭代修正金属-模具界面换热系数，最终使仿真温度与实测值误差控制在5%~10%，以保证模拟精度 [[S36]]。

![压铸模具测点温度CAE仿真结果与实测值对比曲线，两者温度波动趋势高度吻合，CAE计算温度整体略高，平均温度波动差约15℃](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f7ab938-737e-444b-a822-19e52ea8a1bf/resource) [[S7]]

### 镁合金HPDC验证对标

140×100×1 mm AZ91D镁合金平板件、高外观要求薄壁壳体件、平均壁厚2.5 mm无泄漏要求变速箱壳体的仿真预测卷气/流态缺陷位置与实际铸件匹配度高于90%，仅部分缺陷受充型末期残余流场漂移影响存在位置偏移 [[S14,S33]]。

![不同快压射速度下镁合金压铸件仿真流态与实际缺陷对照](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22b27094-6a5a-4055-859d-1e7d3c824e9e/resource) [[S11]]

## 与压铸工艺设计的集成关系

压铸CAE与压铸全流程设计存在双向协同关系 [[S22,S38,S25,S60]]：

- **浇排系统优化**：CAE基于充型仿真反馈迭代优化内浇口截面尺寸、横浇道布局、溢流槽位置与体积 [[S22]]
- **冷却系统设计**：基于温度场仿真指导冷却/加热水道的位置、间距、通径参数 [[S25,S60]]
- **顶出系统校核**：基于应力场仿真校核顶出力与顶杆布局合理性 [[S25]]
- **模型无缝传递**：CAE优化后的设计结果可直接输出用于模具加工，避免跨平台模型失真问题 [[S22,S38,S60]]

![板类压铸件压铸CAE三维几何模型（AnyCasting软件生成）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91edba03-b570-47f9-a8bd-7eb2e3694ca6/resource) [[S48]]

## 常用软件平台

当前压铸行业通用的主流商用压铸CAE软件共7款：MAGMASOFT（德国）、ProCAST（美国）、AnyCasting（韩国）、FLOW-3D CAST（美国）、NovaFlow&Solid（瑞典）、华铸CAE（中国）、Cast-Designer [[S8]]。

### 主要软件功能对比

| 软件 | 开发商 | 核心算法 | 定位与特点 |
|------|-------|---------|----------|
| MAGMASOFT | 德国MAGMA | FDM/FEM混合 | 全流程铸造工艺优化，内置MAGMA hpdc压铸专用模块，覆盖压铸机参数与材料属性完备数据库，薄壁件模拟精度高、计算速度快 [[S8,S39]] |
| ProCAST | 美国ESI集团 | 纯FEM | 全场景多物理场耦合仿真，几何特征保留能力突出，支持应力与热流完全耦合计算，内置基于成分自动生成热物性参数的热力学数据库，适用于复杂异形、大型一体化压铸件 [[S20,S66,S64]] |
| AnyCasting | 韩国AnyCasting | FDM + SOLA-VOF + RNG k-ε湍流模型 | 界面友好、操作门槛低，对铝合金薄壁件充型流场还原度高，适用于中小零部件常规压铸件快速工艺迭代 [[S8]] |
| FLOW-3D CAST | 美国Flow Science | FVM/FDM | 自由表面流动与湍流模拟优势显著，能高精度捕捉压铸高速充型的飞溅、卷气行为，适用于真空压铸、薄壁高流动性件的充型缺陷专项分析 [[S25,S54,S8]] |
| 华铸CAE | 中国华中科技大学 | 复合网格 | 国产高性价比方案，自动网格剖分速度快，支持多周期全流程模拟，对卷气、缩孔类缺陷预测精度可达95%，全中文操作界面，已在航空航天、大飞机项目相关铸件研制中应用 [[S69,S1,S43]] |

![变速器壳体压铸CAE缩孔缺陷预测与工艺优化前后对比（AnyCasting生成）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc427616-eea1-450f-868e-e25da0cceee1/resource) [[S63]]

## 相关标准

国内正在研制的铸造工艺仿真行业标准覆盖压铸仿真场景，规范了仿真环境要求、工作内容、工作流程与结果应用 [[S58,S34,S9,S5]]：

- **环境要求**：需预先建立并经验证包含液相线/固相线温度、潜热、比热等热力学参数的材料数据库，明确缺陷判据、温度/应力等物理量测试方法 [[S34]]
- **工作内容**：覆盖充型流场模拟、凝固温度场模拟、热应力模拟、微观组织模拟四大模块 [[S9,S34]]
- **标准工作流程**：仿真模型构建→前处理设置→数值仿真计算→仿真结果分析；要求输出充型自由表面/速度/压力变化曲线、凝固固相率分布、缺陷定位与定量预测结果 [[S9,S34,S5]]

## 典型应用案例

| 应用对象 | CAE工具 | 关键效果 | 来源 |
|---------|---------|---------|------|
| 新能源汽车4腔A380铝合金动力电池包下壳体 | CAE集成系统 | 仿真与实测型腔温差优化后误差≤3.5%，关键尺寸精度达±0.05 mm，生产节拍较原方案缩短12% | [[S47]] |
| 奥迪5倍速镁合金变速箱体 | MAGMASOFT | 完成充型可行性、凝固过程及复杂冷却系统热平衡仿真，优化浇注系统后直接投入量产，配套用于Passat、奥迪A4/A6 | [[S65]] |
| 福特5.4L Triton发动机壳体 | ProCAST | 流动场-温度场耦合分析，完成产品结构与浇注系统优化，大幅缩短开发周期 | [[S65]] |
| 真空压铸镁合金散热器 | FLOW-3D | 真空压铸模式下氧化夹杂全部集中于溢流槽区域，抗拉强度与伸长率较普通压铸分别提升14.1%和42.1% | [[S53]] |

## 优势与局限性

### 优势

- 缩短模具开发周期，减少试模迭代次数 [[S13,S59]]
- 降低生产成本，提高一次试模成功率 [[S59]]
- 预判并改善铸件品质缺陷 [[S17,S46]]
- 辅助模具寿命评估与热疲劳风险控制 [[S16,S17]]
- 实现工艺方案的虚拟验证与多方案对比优化 [[S52]]

### 局限性

- 仿真精度依赖材料热物性参数、界面换热系数等输入的准确性 [[S15,S56]]
- 求解模型常采用简化假设（如定值换热系数、等温流动等），可能偏离实际 [[S15,S29]]
- 部分复杂物理现象（如充型中凝固、微观组织演化）的全耦合模拟仍面临计算资源与精度挑战 [[S56]]
- 仿真结果的解读与工艺决策仍依赖工程人员的经验 [[S37]]

## Sources
- S17: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38325002-b308-4ab2-9d5f-2317bebdcd11/resource) (`38325002-b308-4ab2-9d5f-2317bebdcd11`)
- S52: [压铸模具简明设计手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab1d0aa4-e987-45d7-be84-a7206c6d60e1/resource) (`ab1d0aa4-e987-45d7-be84-a7206c6d60e1`)
- S59: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3a5bc51-6f28-4ae2-a5d6-632911f9fe5d/resource) (`c3a5bc51-6f28-4ae2-a5d6-632911f9fe5d`)
- S12: [橡塑模具优化设计技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/246cbf51-9d29-44f7-9f5e-3c2fa8ad9043/resource) (`246cbf51-9d29-44f7-9f5e-3c2fa8ad9043`)
- S50: [中国模具工程大典 第3卷 塑料与橡胶模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a7447e9-e7da-4789-9551-3ac58eab1bbe/resource) (`9a7447e9-e7da-4789-9551-3ac58eab1bbe`)
- S56: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b64615da-3fc1-45de-9804-7666f9cf257d/resource) (`b64615da-3fc1-45de-9804-7666f9cf257d`)
- S46: [汽车发动机前盖压铸模浇注系统及排溢系统设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87777c05-6710-406e-8cba-8ce1bd19fd74/resource) (`87777c05-6710-406e-8cba-8ce1bd19fd74`)
- S13: [轴承盖压铸缺陷分析及工艺优化_杨匀龙](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2df93374-f169-48d7-84c0-e040986618f1/resource) (`2df93374-f169-48d7-84c0-e040986618f1`)
- S3: [铝合金水泵座压铸模浇注系统及镶块随形水道设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09448fc3-1210-4b74-8f48-823f39384616/resource) (`09448fc3-1210-4b74-8f48-823f39384616`)
- S30: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/623893ef-612c-40a3-b1d6-9861dbbf9c9a/resource) (`623893ef-612c-40a3-b1d6-9861dbbf9c9a`)
- S19: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c1603cf-1be4-4bca-b6df-6bf644a57b69/resource) (`3c1603cf-1be4-4bca-b6df-6bf644a57b69`)
- S62: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb9822e6-dbe7-428b-83fd-0ece263fd1be/resource) (`cb9822e6-dbe7-428b-83fd-0ece263fd1be`)
- S27: [压铸数值模拟总体框图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ccb8195-3297-451e-b995-00b9619c3184/resource) (`5ccb8195-3297-451e-b995-00b9619c3184`)
- S44: [a numerical and an experimental investigation of a high pressure die cas__76acfbd839](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84f47a0c-d9f5-4f1e-a6be-7c4b72e71e2b/resource) (`84f47a0c-d9f5-4f1e-a6be-7c4b72e71e2b`)
- S16: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/381f8a1e-a12b-43ad-a67b-6c3da51bff04/resource) (`381f8a1e-a12b-43ad-a67b-6c3da51bff04`)
- S4: [asme asme 2003 international mechanical engineering congress and exposit__70cb56cc77](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c637989-9e0d-41d6-ab1a-65d7eed5331c/resource) (`0c637989-9e0d-41d6-ab1a-65d7eed5331c`)
- S26: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5578076a-f43a-4d15-bbf0-49cd85333975/resource) (`5578076a-f43a-4d15-bbf0-49cd85333975`)
- S51: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a07cf7d6-e6bc-4fcb-8278-67113ef1f426/resource) (`a07cf7d6-e6bc-4fcb-8278-67113ef1f426`)
- S42: [压铸模具工程师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8173787d-e277-425e-ae33-c632bfaae9fe/resource) (`8173787d-e277-425e-ae33-c632bfaae9fe`)
- S49: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/957856b4-035c-4f6f-bf3a-66dba655678f/resource) (`957856b4-035c-4f6f-bf3a-66dba655678f`)
- S2: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0425734d-bdc0-4556-adbc-91a45d745bef/resource) (`0425734d-bdc0-4556-adbc-91a45d745bef`)
- S41: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7ed975ba-ba93-46b3-8d7d-1ca4b28c6a37/resource) (`7ed975ba-ba93-46b3-8d7d-1ca4b28c6a37`)
- S18: [执手多型腔压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3a3b6131-7ca2-4b52-a126-9db634490607/resource) (`3a3b6131-7ca2-4b52-a126-9db634490607`)
- S31: [凝固界面换热系数反求及铝合金薄壁件压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a690b93-54db-4d6f-87e7-8803e254b099/resource) (`6a690b93-54db-4d6f-87e7-8803e254b099`)
- S15: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3802d82c-cd25-4066-b9e9-462ba35bdafa/resource) (`3802d82c-cd25-4066-b9e9-462ba35bdafa`)
- S57: [表一 CAE 模拟工艺参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bab5a516-80f5-4be1-87e5-117c44549974/resource) (`bab5a516-80f5-4be1-87e5-117c44549974`)
- S68: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef558392-9433-40e1-8e6a-3e06c2c40510/resource) (`ef558392-9433-40e1-8e6a-3e06c2c40510`)
- S32: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b380485-2c1d-4fe4-af9f-f13ef7f06b8c/resource) (`6b380485-2c1d-4fe4-af9f-f13ef7f06b8c`)
- S61: [铸铝电机转子压铸模具设计与工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ca175477-1c07-4399-ad8f-a85b443a3e6d/resource) (`ca175477-1c07-4399-ad8f-a85b443a3e6d`)
- S23: [轴承盖压铸缺陷分析及工艺优化_杨匀龙](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4bdb7977-ce10-44a5-a125-fa3113b01f06/resource) (`4bdb7977-ce10-44a5-a125-fa3113b01f06`)
- S55: [浅述铝合金压铸件模流分析与验证](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b63bc244-81cd-40f6-b30f-a066d570cd9e/resource) (`b63bc244-81cd-40f6-b30f-a066d570cd9e`)
- S29: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6036fc9e-b11f-4f35-9c1e-d0b419319c14/resource) (`6036fc9e-b11f-4f35-9c1e-d0b419319c14`)
- S37: [职业标准导向下的《压铸工艺及模具设计》课程建设](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71b12ed3-c1cd-42c6-bb50-2524f88342c9/resource) (`71b12ed3-c1cd-42c6-bb50-2524f88342c9`)
- S36: [determination of the heat transfer coefficient at the metal die interfac__3400c99740](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c84e570-3542-4322-a72c-e4cee55a1711/resource) (`6c84e570-3542-4322-a72c-e4cee55a1711`)
- S7: [图4.10 冷却阶段A点温度对比曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f7ab938-737e-444b-a822-19e52ea8a1bf/resource) (`1f7ab938-737e-444b-a822-19e52ea8a1bf`)
- S14: [asme asme 2003 international mechanical engineering congress and exposit__70cb56cc77](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/36e3d89c-244e-4fcd-8c06-ebb82a440311/resource) (`36e3d89c-244e-4fcd-8c06-ebb82a440311`)
- S33: [asme asme 2003 international mechanical engineering congress and exposit__70cb56cc77](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b5aac6b-d577-45c4-a1d0-45b5f3548d77/resource) (`6b5aac6b-d577-45c4-a1d0-45b5f3548d77`)
- S11: [图9 不同快压射速度下AZ91D镁合金薄壁压铸件的温度场和速度场分布以及铸件实物图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22b27094-6a5a-4055-859d-1e7d3c824e9e/resource) (`22b27094-6a5a-4055-859d-1e7d3c824e9e`)
- S22: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43ab30f5-c6ab-4556-a92e-10f38e38c62b/resource) (`43ab30f5-c6ab-4556-a92e-10f38e38c62b`)
- S38: [基于NX的压铸数值模拟集成与溢流槽快速建模系统研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/78da845e-7044-4441-8da2-dac797fca164/resource) (`78da845e-7044-4441-8da2-dac797fca164`)
- S25: [application of an integrated cad cae cam system for die casting dies__96a43cb0a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4d4649ff-c3d2-4a72-94b2-09dafe778a34/resource) (`4d4649ff-c3d2-4a72-94b2-09dafe778a34`)
- S60: [基于NX的压铸工艺设计CAD_CAE集成系统关键技术的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ca01fea3-3215-4592-80d6-b9137b095ffd/resource) (`ca01fea3-3215-4592-80d6-b9137b095ffd`)
- S48: [平板压铸件模拟计算图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91edba03-b570-47f9-a8bd-7eb2e3694ca6/resource) (`91edba03-b570-47f9-a8bd-7eb2e3694ca6`)
- S8: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848/resource) (`1fff50f1-9ff6-4934-bdb0-e0ab6fbe0848`)
- S39: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a62dd6c-7a87-47ef-888c-1374e8938011/resource) (`7a62dd6c-7a87-47ef-888c-1374e8938011`)
- S20: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ef11554-2e86-4f0f-8f90-4908a7c498b4/resource) (`3ef11554-2e86-4f0f-8f90-4908a7c498b4`)
- S66: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3c80f3d-68be-4532-a6ce-b6f98094967a/resource) (`e3c80f3d-68be-4532-a6ce-b6f98094967a`)
- S64: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd273b06-cd96-497f-ac47-0861037cc35f/resource) (`dd273b06-cd96-497f-ac47-0861037cc35f`)
- S54: [asme asme 2014 12th biennial conference on engineering systems design an__a15afb75a5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af752c87-83cb-498a-8dc3-04dd07b39d6d/resource) (`af752c87-83cb-498a-8dc3-04dd07b39d6d`)
- S69: [压铸成型技术及模具 设计与实践](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbcf1cba-b440-49e4-a6fb-85eaf54e607f/resource) (`fbcf1cba-b440-49e4-a6fb-85eaf54e607f`)
- S1: [2505109_华铸CAE](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/019777af-e28f-44e2-9962-ccde177bf179/resource) (`019777af-e28f-44e2-9962-ccde177bf179`)
- S43: [压铸成形工艺与模具](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82c247df-f495-4969-93e6-79b08c89f519/resource) (`82c247df-f495-4969-93e6-79b08c89f519`)
- S63: [改进前后变速器壳体铸件缩孔、缩松模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc427616-eea1-450f-868e-e25da0cceee1/resource) (`dc427616-eea1-450f-868e-e25da0cceee1`)
- S58: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bcd9c895-af26-4ae8-bee1-ff9d2b1e1344/resource) (`bcd9c895-af26-4ae8-bee1-ff9d2b1e1344`)
- S34: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b8bbf98-2fa7-4f6d-bf13-b01d1ec47916/resource) (`6b8bbf98-2fa7-4f6d-bf13-b01d1ec47916`)
- S9: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20163983-c676-4b09-8202-b0195cdc9b74/resource) (`20163983-c676-4b09-8202-b0195cdc9b74`)
- S5: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ee1b068-5015-4915-b250-fcdef91d9905/resource) (`0ee1b068-5015-4915-b250-fcdef91d9905`)
- S47: [多腔压铸模成型精度控制技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8fd8a356-e12e-4090-9114-27bf6406c836/resource) (`8fd8a356-e12e-4090-9114-27bf6406c836`)
- S65: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddae80b0-ef21-478a-a6c6-330499b00087/resource) (`ddae80b0-ef21-478a-a6c6-330499b00087`)
- S53: [执手多型腔压铸工艺及模具优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad27d26f-c0f7-40f3-bc3a-262bed5164db/resource) (`ad27d26f-c0f7-40f3-bc3a-262bed5164db`)