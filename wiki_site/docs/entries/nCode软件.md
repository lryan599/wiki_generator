---
version: "v1"
generated_at: "2026-06-18T17:23:25+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 34
  source_quality_score: 0.84
  freshness_score: 0.91
  evidence_coverage_score: 1.0
---

## 概述

ANSYS nCode是深度集成于ANSYS Workbench环境下的高级疲劳寿命分析平台，基于断裂力学与材料疲劳损伤理论，构建了完整的疲劳寿命预测与结构耐久性评估体系[[S30]]。该平台深度融合材料科学、计算力学与数据处理技术，通过多物理场耦合仿真手段，实现对复杂工况下构件疲劳行为的精准预测与优化设计[[S30]]。

nCode并非独立软件套件，而是作为ANSYS生态体系内的专业模块，与ANSYS结构分析环境紧密协作，在汽车、通用机械、航空航天及模具工程等领域有广泛应用。

## 核心功能与算法

### 高周疲劳分析（S-N应力寿命法）

针对高周疲劳问题，nCode严格遵循应力寿命（S-N）理论，通过Miner线性损伤累积法则，结合材料S-N曲线数据库，实现对循环应力幅值与疲劳寿命关系的定量计算[[S30]]。DesignLife模块可以根据材料的极限抗拉强度和弹性模量近似自动生成S-N曲线，为缺乏实验数据的材料提供初始疲劳评估依据[[S32]]。

![设计S-N曲线及Miner累积损伤规则示意图，展示标注应力范围S与循环次数N的设计S-N曲线及Miner线性累积损伤规则的计算公式与失效判定条件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d8ba29d-1039-40c5-8b9c-7bbfcdbf8a23/resource)

### 低周疲劳分析（E-N局部应变法）

对于低周疲劳工况，nCode基于应变寿命（E-N）理论，引入Coffin-Manson方程与Smith-Watson-Topper（SWT）参数，充分考虑塑性应变能与疲劳损伤的关联，解决材料在大应变循环载荷下的寿命预测问题[[S30]]。

### 裂纹扩展分析

nCode内置的裂纹扩展分析模块基于Paris定律开发，通过计算应力强度因子及其变化率，对裂纹萌生、扩展直至失稳断裂的全过程进行仿真，为结构剩余寿命评估提供关键依据[[S30]]。

### 平均应力修正方法

nCode支持三类典型的平均应力修正方法[[S30]]：

| 修正方法 | 公式特征 |
|---------|---------|
| Goodman | 结果居中，工程实践中最常用 |
| Gerber | 相同平均应力下疲劳极限最高 |
| Solonberg | 相同平均应力下疲劳极限最低 |

工程实践中Goodman关系式最为常用[[S30]]。

### 多轴疲劳分析

nCode支持多轴疲劳分析，可基于临界平面法、应力应变不变量等理论完成非比例加载条件下的复杂疲劳工况计算，对应多轴载荷疲劳评估的五类主流技术体系[[S18,S5]]。

## 典型分析流程

nCode通用疲劳分析典型全流程包含六个步骤[[S41,S32,S8]]：

1. **导入有限元结果**：将ANSYS或其他有限元软件的应力/应变场结果（如.rst、.OBD格式）导入nCode；
2. **载荷谱构建**：将实测或仿真载荷数据预处理，转换为nCode可识别的s3t格式，生成疲劳载荷谱；
3. **材料属性定义**：定义并映射材料疲劳属性，完成S-N/E-N曲线的参数配置与必要修正；
4. **载荷映射配置**：配置温度载荷（temperature load provider）、时间步载荷（time step load provider）、时序载荷（time series load provider）等多源输入的加载映射规则[[S8]]；
5. **疲劳计算**：选定对应疲劳分析理论完成计算；
6. **后处理输出**：输出疲劳寿命分布云图及关键结果。

![nCode流图式热-机耦合疲劳分析工作界面示例，清晰展示功能节点的连接逻辑与操作流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f159d4a8-f8ec-42c3-afba-3e2be704353a/resource)

## 别名澄清：nCode与FE-Safe的关系

### 重要区分

FE-Safe与ANSYS nCode**不存在同一产品不同命名的关系**，二者分属不同厂商体系[[S16,S30]]：

| 对比维度 | ANSYS nCode | FE-Safe |
|---------|-------------|---------|
| 所属厂商 | ANSYS | 达索SIMULIA |
| 集成环境 | ANSYS Workbench | Abaqus |
| 功能定位 | 集成于ANSYS生态的疲劳分析平台 | SIMULIA产品线中的疲劳仿真模块 |

行业内常见混淆场景包括：大量学术文献将FE-Safe描述为Abaqus内嵌疲劳模块，将nCode等同于ANSYS内置免费功能，错误地将两款软件的算法体系完全等同，忽略二者分属不同厂商体系的授权差异[[S20,S3,S26]]。

在压铸模具热疲劳仿真工程场景中，FE-Safe常作为Abaqus配套模块使用，内置Seegers Method算法用于估算和修正材料S-N曲线，导入ProCAST热应力仿真结果后计算得到压铸模具热疲劳寿命分布云图[[S16,S14,S25]]。

## “注塑-结构-疲劳耦合分析”术语说明

“注塑-结构-疲劳耦合分析”**并非nCode官方指定的产品/功能别名**。该术语是国内工程研究文献中对注塑仿真（如Moldflow/Moldex3D）→ 结构分析（如Ansys/Abaqus）→ 疲劳评估（如nCode/FE-safe）全链路协同流程的通用命名[[S26,S40,S22]]。该术语在工程应用场景中表述准确可用，但不属于nCode原生模块的官方专属名称。

### 基于Moldex3D的耦合分析路径

基于Moldex3D的注塑-结构-疲劳耦合分析全链路操作流程为[[S2,S4,S26,S19]]：

1. 使用UG软件完成注塑模具3D模型简化；
2. 将模型导入Moldex3D，设置注塑工艺参数、完成网格划分开展模流分析；
3. 通过Moldex3D的FEA介面模组导出带有节点载荷、材料属性的INP文件传入Abaqus，完成结构分析；
4. 将Abaqus输出的OBD结果文件导入nCode（原FE-safe，已整合进nCode产品线），设置疲劳分析参数完成疲劳寿命计算。

### 基于Moldflow的耦合分析路径

基于Moldflow的注塑-结构-疲劳耦合分析全链路操作流程为[[S40,S36,S37]]：

1. 使用Moldflow完成模流分析，提取纤维取向、残余应力、填充不均匀性等结果；
2. 通过Advanced Material Exchange/Helius PFA或Digimat-MAP模块完成模流网格与结构分析网格的映射对齐，将注塑工艺诱导的材料各向异性属性传递至Ansys有限元模型；
3. 在Ansys中完成含成型工艺影响的结构应力应变求解，输出.rst格式结果文件；
4. 将.rst文件导入nCode，构建疲劳载荷谱与应力修正模型，结合热机械循环特征完成多轴疲劳仿真，输出疲劳寿命分布图谱。

nCode本身无直接对接Moldflow、Moldex3D的原生独立接口，需借助Ansys生态中间映射模块实现数据传递[[S37,S13,S29,S19]]。

### 典型应用案例

青岛科技大学2021年公开学位论文中完成了平板支架注塑模具与桶形凹腔注塑模具的注塑-结构-疲劳耦合分析：以Moldex3D输出的型腔压力载荷为输入，通过Abaqus完成结构求解后导入FE-safe开展疲劳寿命计算，结合正交试验与响应面试验明确了保压压力、型腔腔壁厚度、型腔腔底厚度三个因素对注塑模具疲劳寿命的影响规律，构建了疲劳寿命预测回归方程并通过实际生产模具的服役次数验证了准确性[[S26,S22,S23]]。

2025年公开的自行车中轴轴碗注塑模具优化研究中完成了基于nCode的注塑模具型芯疲劳分析：通过Moldflow完成轴碗塑件模流分析得到成型工艺参数，结合特殊点映射理论将Moldflow输出的温度、压力载荷映射至模具型芯结构网格，通过Ansys完成热-压耦合应力求解后导入nCode构建疲劳载荷谱与应力修正模型，开展多轴疲劳仿真得到型芯疲劳寿命分布图谱[[S40,S36,S9]]。

## 压铸/铸造领域的应用说明

### 当前证据情况

现有检索证据中**未发现nCode针对压铸件或铸造件有专门的直接应用案例或功能模块**。nCode对压铸构件的疲劳分析能力主要体现在其**通用疲劳分析能力**层面，包括[[S41,S8]]：

- 基于S-N的高周疲劳计算
- 基于E-N的低周疲劳计算
- Paris定律为基础的裂纹扩展分析
- 支持通过外部时序载荷转换的s3t格式文件导入自定义载荷谱
- 支持Goodman等主流平均应力修正方法

### 铸造缺陷对疲劳评估的影响

针对压铸件疲劳评估，以下几方面结论值得关注：

压铸铝合金中表面孔洞与内部孔洞均为优先萌生疲劳裂纹的核心位置，压铸件内部的气孔、缩松、氧化膜等典型缺陷会显著降低构件的疲劳性能，造成同批次合格铸件的疲劳寿命出现高离散性[[S17,S15]]。针对ADC12压铸件的孔隙率-疲劳关联研究表明，在不同试样孔隙率差值不超过1%的条件下，压铸件的疲劳寿命可相差一个数量级，同时存在关联孔洞等效直径、应力水平的专用疲劳寿命预测公式可用于压铸铝合金疲劳评估校准[[S34]]。

铸钢构件疲劳特性研究表明，表面铸造缺陷会主导疲劳裂纹的萌生过程，内部缩孔类缺陷则会显著延长裂纹萌生阶段的占比，不同类型缺陷对应的疲劳S-N曲线梯度存在明显差异。仅使用nCode默认通用材料库对含铸造缺陷的压铸构件开展疲劳评估会得到偏于保守且精度不足的结果，需导入匹配对应压铸工艺的定制化S-N数据集提升预测精度[[S21,S24,S33]]。

### 与铸造仿真结果的潜在集成路径

nCode可对接铸造/注塑仿真输出的温度场、应力场等结果进行构件疲劳寿命分析，其信息传递路径为[[S30,S8]]：

1. **铸造仿真输出**：从ProCAST、MAGMA等铸造仿真软件获取温度场、热应力场、残余应力场等结果；
2. **结构分析求解**：将铸造仿真结果导入Abaqus/ANSYS作为初始载荷条件，完成结构应力应变求解；
3. **缺陷场映射**：铸造仿真输出的空间分布孔隙率场（如铝合金铸件总收缩孔隙率分布热力图所示[[S7]]）可作为映射输入导入nCode，为每个有限元单元匹配对应孔隙率的疲劳降级系数，实现考虑非均匀孔隙分布效应的全域疲劳寿命评估[[S7]]；
4. **疲劳寿命计算**：导入nCode完成疲劳评估。

残余应力水平的升高会显著降低构件的疲劳寿命，这为将铸造仿真得到的残余应力场导入nCode开展耦合寿命评估提供了重要理论参考[[S39]]。基于合金密度差值的压铸合金孔隙百分率量化数据可作为nCode对不同区域材料匹配疲劳降级系数的校准输入参考[[S31]]。

## 同类软件对比

| 对比维度 | ANSYS nCode | FE-Safe（SIMULIA） | MSC Fatigue |
|---------|-------------|-------------------|-------------|
| 厂商体系 | ANSYS Workbench | 达索SIMULIA | MSC Software |
| 兼容有限元 | ANSYS | Abaqus | MSC.Nastran、MSC.Marc、ANSYS、Abaqus等多款软件[[S6,S27]] |
| 高周疲劳 | S-N + Miner | 支持 | S-N全寿命分析[[S6,S27]] |
| 低周疲劳 | E-N + Coffin-Manson + SWT[[S30]] | 支持 | E-N裂纹萌生分析[[S6,S27]] |
| 裂纹扩展 | Paris定律[[S30]] | 支持 | 线弹性断裂力学[[S6,S27]] |
| 焊接疲劳 | 未明确提及 | 未明确提及 | 支持焊接/点焊疲劳分析[[S6,S27]] |
| 振动疲劳 | 未明确提及 | 未明确提及 | 支持频域/时域振动疲劳[[S6,S27]] |

MSC Fatigue采用“五盒技术”架构开展分析，前处理需输入载荷状况、材料属性、解决方案三类必要条件[[S6,S27]]。

## 局限性与适用边界

1. **铸造缺陷处理能力有限**：nCode缺乏针对铸造缺陷的专用处理模块，默认通用材料库对含铸造缺陷的构件进行疲劳评估会得到偏于保守且精度不足的结果，需导入定制化S-N数据集[[S24,S33]]；
2. **无直接模流仿真接口**：nCode无直接对接Moldflow、Moldex3D的原生独立接口，需借助中间映射模块实现数据传递[[S37,S13]]；
3. **S-N曲线依赖**：当缺乏材料疲劳试验数据时，通过极限抗拉强度和弹性模量近似生成的S-N曲线仅代表近似结果，工程应用中材料实测S-N曲线更为可靠[[S32,S9]]；
4. **仿真简化误差**：实际仿真过程中对模型和工作条件的简化处理会导致理论预测与实际寿命存在偏差[[S8]]。

## Sources
- S30: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0260dac-7ab1-437f-91f3-56fb35a4ea88/resource) (`c0260dac-7ab1-437f-91f3-56fb35a4ea88`)
- S32: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d257e6d4-5fb1-46c0-a0e9-ea25cc364a74/resource) (`d257e6d4-5fb1-46c0-a0e9-ea25cc364a74`)
- S18: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d57828c-db85-43bc-972c-92c17cff18ec/resource) (`8d57828c-db85-43bc-972c-92c17cff18ec`)
- S5: [alloy steel properties and use__f8ed38d799](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/262c7c7a-cb5e-449f-ad27-5ebb2dc39d45/resource) (`262c7c7a-cb5e-449f-ad27-5ebb2dc39d45`)
- S41: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdf4e900-f715-496a-84dc-ab9f21e957a5/resource) (`fdf4e900-f715-496a-84dc-ab9f21e957a5`)
- S8: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/505942a2-8f18-4f29-b2a7-8099f4e1252d/resource) (`505942a2-8f18-4f29-b2a7-8099f4e1252d`)
- S16: [金属体积成形工艺及数值模拟技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b37ef4b-5a95-4f97-a1be-4f5a9e11613f/resource) (`7b37ef4b-5a95-4f97-a1be-4f5a9e11613f`)
- S20: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91550229-e571-44c2-90da-86a88cb176e9/resource) (`91550229-e571-44c2-90da-86a88cb176e9`)
- S3: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16b1f7e9-730e-4ab4-8926-be5c1257cb05/resource) (`16b1f7e9-730e-4ab4-8926-be5c1257cb05`)
- S26: [基于Moldex3D与Abaqus_FE-safe的注塑模具结构及疲劳寿命分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af9270e2-edc9-46f6-a905-a6ed5ba7bbeb/resource) (`af9270e2-edc9-46f6-a905-a6ed5ba7bbeb`)
- S14: [基于有限元的压铸模寿命预测和工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7823f300-5a61-4b1b-bc44-9b2517f1634b/resource) (`7823f300-5a61-4b1b-bc44-9b2517f1634b`)
- S25: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aca855db-491a-4294-ac75-47c561eb1aec/resource) (`aca855db-491a-4294-ac75-47c561eb1aec`)
- S40: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f549a101-cf28-4d61-9e11-c54c17cf01ea/resource) (`f549a101-cf28-4d61-9e11-c54c17cf01ea`)
- S22: [基于Moldex3D与Abaqus_FE-safe的注塑模具结构及疲劳寿命分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/965dc616-eeb4-4315-8f9d-2f06b346d228/resource) (`965dc616-eeb4-4315-8f9d-2f06b346d228`)
- S2: [图4-10 注塑-结构耦合分析流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15f645f0-0388-4338-b78c-8be6970c96e3/resource) (`15f645f0-0388-4338-b78c-8be6970c96e3`)
- S4: [图5-1 疲劳分析流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1b10ebb3-4ecc-49a6-9a60-f7c88bff9b5a/resource) (`1b10ebb3-4ecc-49a6-9a60-f7c88bff9b5a`)
- S19: [基于Moldex3D与Abaqus_FE-safe的注塑模具结构及疲劳寿命分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d69f67b-dfbe-42ab-84ab-d36e45e6c54c/resource) (`8d69f67b-dfbe-42ab-84ab-d36e45e6c54c`)
- S36: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df5f5393-d1e6-484d-88e3-9e946512c0c8/resource) (`df5f5393-d1e6-484d-88e3-9e946512c0c8`)
- S37: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e1e8cf8a-5dcb-4883-905a-4ea277f1d22c/resource) (`e1e8cf8a-5dcb-4883-905a-4ea277f1d22c`)
- S13: [基于Moldex 3D与ABAQUS的注射模结构分析与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fc3dca3-eee6-45b1-8245-29c8bd9c3a8f/resource) (`6fc3dca3-eee6-45b1-8245-29c8bd9c3a8f`)
- S29: [Moldflow注塑模流分析从入门到精通](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc1c86c1-ec4d-44f5-9928-747d44d1017c/resource) (`bc1c86c1-ec4d-44f5-9928-747d44d1017c`)
- S23: [基于Moldex3D与Abaqus_FE-safe的注塑模具结构及疲劳寿命分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a72fdfde-f130-46e2-a0ee-b68aa98dc807/resource) (`a72fdfde-f130-46e2-a0ee-b68aa98dc807`)
- S9: [自行车中轴轴碗注塑模具设计优化及其疲劳失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59a46e7f-6473-473b-a648-4fb281aefe73/resource) (`59a46e7f-6473-473b-a648-4fb281aefe73`)
- S17: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c39dcbe-e7b5-4133-935c-d15ebf4ce456/resource) (`8c39dcbe-e7b5-4133-935c-d15ebf4ce456`)
- S15: [casting defects and fatigue strength of a die cast aluminium alloy a com__cf3b41f369](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/782e9c7f-c9ab-410a-a0d3-0b10525cfbbf/resource) (`782e9c7f-c9ab-410a-a0d3-0b10525cfbbf`)
- S34: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d83d1347-f05f-4750-a6f3-b9050fd7ce08/resource) (`d83d1347-f05f-4750-a6f3-b9050fd7ce08`)
- S21: [design of cast steel components under cyclic loading__2549607551](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/919554ab-df6b-4b6a-906d-c0bb9dff410f/resource) (`919554ab-df6b-4b6a-906d-c0bb9dff410f`)
- S24: [design of cast steel components under cyclic loading__2549607551](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8bcb1f6-db3c-438d-bd73-2beff949a30e/resource) (`a8bcb1f6-db3c-438d-bd73-2beff949a30e`)
- S33: [design of cast steel components under cyclic loading__2549607551](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d69415c0-9182-4676-9fe7-9b3d22abc307/resource) (`d69415c0-9182-4676-9fe7-9b3d22abc307`)
- S7: [铸件总收缩孔隙率分布热力图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a163846-4d8d-439e-986f-d3a9e10536fa/resource) (`4a163846-4d8d-439e-986f-d3a9e10536fa`)
- S39: [图 6：预测疲劳寿命与残余应力的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1c93cf3-9577-4980-b04b-ed84f8891240/resource) (`f1c93cf3-9577-4980-b04b-ed84f8891240`)
- S31: [压力铸造合金孔隙率计算与测量方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8f21fb2-3437-4bd7-9d89-5c3dbda0502c/resource) (`c8f21fb2-3437-4bd7-9d89-5c3dbda0502c`)
- S6: [纤维金属层板的力学性能及成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2bbff662-048c-467a-90fe-d44103c9d9b1/resource) (`2bbff662-048c-467a-90fe-d44103c9d9b1`)
- S27: [纤维金属层板的力学性能及成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b11851bf-f947-4992-b6cd-2675b4c94695/resource) (`b11851bf-f947-4992-b6cd-2675b4c94695`)