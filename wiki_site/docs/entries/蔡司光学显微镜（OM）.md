---
version: "v1"
generated_at: "2026-06-18T14:19:13+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.85
  freshness_score: 0.84
  evidence_coverage_score: 1.0
---

## 概述

蔡司光学显微镜（ZEISS Optical Microscope，ZEISS OM）是德国蔡司（ZEISS）公司研发生产的光学显微成像仪器。1877年，蔡司公司生产出全球第一台配备油浸物镜的光学显微镜，相比前代设备可获得更高的金属显微组织检测分辨率[[S28]]。在压铸领域，蔡司光学显微镜是实验室中用于观察压铸件显微组织、孔隙、晶粒特征的常用检测设备，广泛适配铝合金、镁合金等各类压铸金属试样的金相分析需求[[S28,S3,S8,S30,S7]]。

蔡司光学显微镜遵循通用金相光学显微镜的两级放大成像原理：试样放置于物镜焦点外侧附近，物镜将试样微观特征放大生成倒立实像，该实像落在目镜焦点内侧，经目镜再次放大后，人眼可在250mm明视距离处观测到最终放大虚像，总放大倍数为物镜放大倍数与目镜放大倍数的乘积[[S19,S24]]。

## 分类与型号

### 结构形式分类

按物镜与载物台的相对位置，蔡司光学显微镜可分为正置式和倒置式两类[[S15]]：

- **正置式**：物镜位于载物台上方，从试样观察面向上方成像，适用于厚度较小、高度不高的普通金相试样观察。
- **倒置式**：物镜位于载物台下方，试样待测表面朝下放置，无需高度调平即可直接观察，适配大尺寸、未切割的整块压铸构件试样检测。

> 蔡司全系列正置、倒置机型的光路详细参数差异未见权威描述[[S15]]。

### 压铸领域常用型号

压铸实验室已普遍使用的蔡司金相显微镜Axio系列型号包括[[S5,S38,S3,S31,S20]]：

| 结构形式 | 常用型号 | 典型应用场景 |
|---------|---------|------------|
| 倒置式 | Axio Vert A1 | 压铸铝合金、镁合金金相观察；半固态铝合金试样检测 |
| 正置式 | Axio Imager A2m | 铝合金金相组织分析 |
| 正置式 | Axio Scope.A1 | 杂质微观分布观察 |
| 正置式 | ZEISS AXIO Imager A1m | 材料金相组织拍摄 |

此外，Axiovert200等型号也在半固态压铸成形研究中得到应用，常用放大倍率覆盖25、50、100、200、500、1000倍[[S17]]。主流蔡司光学显微镜在压铸领域常用放大倍率覆盖25倍至1000倍，部分型号配备的数码图像采集系统可输出最大尺寸2752pixel × 2208pixel的金相照片，分辨率可达150dpi[[S17]]。

![用于压铸铝合金车轮微观金相分析的蔡司光学显微镜成像工作站](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f94eb182-385f-480a-9c93-b38f61359985/resource)

**图1** 所示蔡司光学金相显微镜成像工作站，用于低压铸造铝合金车轮压铸试样的微观组织观测[[S42]]。

## 核心结构与组件

蔡司光学显微镜核心结构由三大系统构成[[S28,S19,S24,S21,S37]]：

**（一）光学系统**
包含物镜和目镜，是完成金相组织放大并获取清晰图像的核心部分。物镜标注的参数格式为“放大倍数/数值孔径”（如40/0.65），高倍物镜多为油浸系。物镜的优劣直接影响显微镜成像质量，衡量物镜性能的参数包括数值孔径、分辨能力、放大倍数、景深度和像差校正程度[[S19,S24]]。

**（二）机械系统**
包含可移动载物台、粗调焦机构和微调焦机构，用于承载试样并实现精确对焦[[S28,S19]]。

**（三）照明系统**
支持平行光照明，灯丝像先汇聚在孔径光阑上，再成像于物镜后焦面，经物镜射出一束平行光线投射到试样表面，照明均匀且便于扩展暗场、偏光等观测附件[[S21]]。部分机型搭载光电转换模块，配套计算机图像采集系统，可直接对金相图像进行分析、评级、输出打印[[S37]]。

蔡司金相显微镜搭载专属ICCS光学系统，相关详细技术特性未见权威描述[[S22]]。蔡司配套特色LED照明的具体参数与技术细节亦未见权威公开描述[[S28]]。

## 关键技术参数

### 放大倍率

光学显微镜总放大倍率为物镜放大倍数与目镜放大倍数的乘积。压铸金相观察场景下，常规有效放大倍率范围为20X~1000X[[S19,S13]]。主流蔡司光学显微镜在压铸领域常用放大倍率覆盖25倍至1000倍[[S17]]。

### 分辨能力与数值孔径

光学显微镜以波长约500nm的可见光作为成像光源，理论分辨率极限约为200nm[[S19,S33,S39]]。分辨能力的核心决定参数为物镜的数值孔径（N.A.），数值孔径越大，物镜的分辨能力越强[[S19,S33]]。物镜上标注的参数格式如“40/0.65”，其中40表示放大倍数，0.65表示数值孔径[[S19]]。

### 照明方式

| 照明方式 | 原理与适用场景 | 来源 |
|---------|--------------|------|
| 明视场照明 | 垂直照明器将光源光线转向照射试样表面，反射光经物镜/目镜成像；光滑表面呈明亮，漫散射区域呈灰暗 | [[S21]] |
| 暗视场照明 | 入射光束绕过物镜斜射于试样表面，通过环行光阑及环行反射镜实现 | [[S21]] |
| 偏光照明 | 在平行光照明系统中附加偏光附件，用于特定组织特征的衬度提升 | [[S21,S13]] |
| 微分干涉相衬(DIC) | 用于不同高度表面产生亮度差异，提升组织形貌衬度 | [[S13,S21]] |

### 光阑调节

蔡司光学显微镜照明系统中设有孔径光阑和视场光阑两个可变光阑[[S10]]：

- **孔径光阑**：控制射向物镜入射光束的粗细。需调节至刚好使光线充满物镜后透镜，更换不同数值孔径的物镜后必须重新调整，以平衡分辨能力、景深与图像衬度。
- **视场光阑**：改变视场大小，减小镜筒内部反射与炫光以提高映像衬度，调节至边缘刚好完全包围当前观察视场即可。

## 在压铸工艺中的角色与应用

### 试样制备配合流程

蔡司光学显微镜配合压铸金相试样制备的完整流程如下[[S8,S30,S14]]：

1. **取样**：使用线切割设备在压铸件典型缺陷或关注区域切取代表性试样。
2. **镶嵌**：使用XQ-1型等镶嵌机对尺寸过小或形状不规则的试样进行热镶或冷镶。
3. **磨制**：依次使用200#至3000#等梯度砂纸进行粗磨、精磨，将试样表面打磨至无可见划痕。
4. **抛光**：使用金相磨抛机搭配W0.5等规格金刚石抛光膏抛光至镜面状态。
5. **浸蚀**：铝基压铸件采用0.5%HF溶液浸蚀10~30s，镁基压铸件采用4%硝酸酒精溶液浸蚀对应时长。
6. **清洗干燥**：浸蚀后立即用无水乙醇冲洗并吹干。
7. **上机观察**：将制备完成的试样放置在蔡司光学显微镜载物台上进行观测。

各设备衔接需保证试样从抛光结束到浸蚀观测的工序不引入表面氧化、划痕等干扰假象[[S8,S30]]。

### 典型观察内容

蔡司光学显微镜在压铸行业的典型应用场景包含[[S6,S9]]：

- **铸态微观组织观测**：清晰识别α-Al基体、共晶硅相、Mg₁₇Al₁₂相等压铸典型组成相。
- **缺陷识别区分**：气孔呈现光滑边缘和光亮内腔，缩孔呈现不规则边缘和暗色内腔；可识别裂纹、非金属夹杂等缺陷。
- **第二相分布统计与晶粒度评级**：第二相质点性质、尺寸、形状、数量和分布评价。
- **热处理后组织演变分析**：不同固溶、时效工艺下的组织变化追踪。

### 定量金相分析

配合蔡司配套图像分析软件，可开展以下定量金相检测[[S34,S1]]：

| 检测项目 | 操作方法 | 遵循标准示例 |
|---------|---------|------------|
| 孔隙率 | 图像分割算法自动统计指定视场内孔隙面积占比 | GB/T 46786-2025 |
| 晶粒尺寸 | 截线法或截点法完成自动统计 | GB/T 6394 |
| 第二相体积分数 | 网格覆盖法计算相的面积比 | GB/T 46786-2025 |

操作过程中需符合对应金相检测标准的精度要求[[S34]]。

## 操作要点

### 基本操作步骤

蔡司金相显微镜适配压铸试样观察的标准操作流程[[S43,S10]]：

1. 确认压铸试样表面腐蚀液完全干燥无残留，放置时磨面朝向物镜。
2. 开启设备光源，将粗调旋钮转动至物镜接近试样的目测安全位置（无接触风险）。
3. 从目镜中观察，缓慢反向旋动粗调旋钮使载物台逐步远离试样直至组织轮廓初步显现。
4. 旋转微调旋钮获得最佳成像清晰度。
5. 按需调节孔径光阑和视场光阑获得最优成像衬度。
6. 全部观察完成后依次关闭光源、切断设备电源。

### 光源调整

光源调整分为径向调整和轴向调整[[S10]]：
- **径向调整**：将发光点调到光学系统光轴上。
- **轴向调整**：将灯丝通过聚光镜后汇聚在孔径光阑上，以得到平行光照明。

光源精确调整后应达到照明视野明亮且均匀、视野内无灯丝像残留的效果[[S10]]。

### 维护保养要点

蔡司金相显微镜日常维护要点[[S10,S26]]：

1. 操作前必须保证双手和待观察试样清洁，**绝对禁止**将浸蚀剂未完全干燥的压铸试样直接放置于载物台观察，以免腐蚀物镜光学镜片。
2. 设备电源接入必须经过适配变压器；装卸、更换物镜和目镜时必须确认部件放置稳固，防止掉落损坏。
3. 光学镜片表面严禁用手、普通布料擦拭，必须使用专用驼毛刷或镜头纸轻轻清洁。
4. 使用过程中出现故障需立即上报专业维护人员，严禁自行拆解设备。

### 环境要求

金相显微镜是精密光学仪器，在使用和存放中应注意防振、保持洁净，避免灰尘和化学腐蚀气体对光学系统的损害[[S10]]。

## 优势与局限性

### 与扫描电子显微镜（SEM）对比

在压铸微观组织检测场景下，蔡司光学显微镜与扫描电镜的核心性能差异如下表所示[[S40,S11,S39]]：

| 对比维度 | 蔡司光学显微镜（OM） | 扫描电子显微镜（SEM） |
|---------|-------------------|---------------------|
| 成像介质 | 空气 | 高真空环境 |
| 光源类型 | 可见光（~500nm） | 电子束 |
| 分辨率 | 约200nm | 可达1.55nm |
| 操作复杂度 | 简便，检测成本低 | 需真空环境，试样尺寸受限 |
| 试样要求 | 抛光/浸蚀表面即可，无需特殊处理 | 需导电处理，充分脱脂干燥 |
| 优势应用 | 低倍下金相组织全局统计、SDAS定量测量、大视场夹杂物分布筛查 | 纳米级析出相、细小夹杂物、断口微观形貌；可同步EDS完成微区成分分析 |

### 实际检测中的互补使用

压铸铝合金/镁合金实际检测中，蔡司OM多用于低倍下金相组织全局统计、SDAS（二次枝晶臂间距）定量测量、大视场夹杂物分布筛查；SEM多用于对OM识别出的特定微区缺陷开展更高倍率的精细形貌观测和成分分析。两种设备通常搭配使用，完成全尺度的压铸微观表征[[S23,S18]]。

## 相关标准与规范

### 国内GB标准

| 标准编号 | 名称 | 与压铸金相检测的关联 | 来源 |
|---------|------|-------------------|------|
| GB/T 46786-2025 | 锌合金压铸件金相检验 | 规定了锌合金压铸件金相检验的试样制备要求、初生相体积分数与大小的检验方法，配套标准金相图谱，2026年7月1日实施 | [[S34]] |
| GB/T 6394 | 金属平均晶粒度测定方法 | 可用于压铸合金的晶粒度定量评级 | [[S4]] |
| GB/T 10561-2005 / ISO 4967:1998 | 钢中非金属夹杂物含量的测定 标准评级图显微检验法 | 可用于压铸件中夹杂类缺陷的评级 | [[S4]] |

### 国际ISO标准

| 标准编号 | 名称 | 与压铸金相检测的关联 | 来源 |
|---------|------|-------------------|------|
| ISO 10049 | 铝合金铸件针孔度目测评定法 | 规定光学显微镜下铝合金铸件针孔缺陷的评级方法 | [[S25]] |
| ISO 4499 | 硬质合金 金相法测定显微组织 | 显微观测方法可参考用于压铸合金组织分析 | [[S25]] |
| ISO 4505 | 硬质合金 孔隙和未溶碳化物的金相测定 | 孔隙定量检测方法可参考用于压铸合金 | [[S36]] |

### ASTM标准

| 标准编号 | 名称 | 与压铸金相检测的关联 | 来源 |
|---------|------|-------------------|------|
| ASTM E3 | 金相试样制备指南 | 明确适用于压铸合金的试样切割、镶嵌、磨抛操作规范 | [[S2]] |
| ASTM E112 | 金属平均晶粒度测定方法 | 压铸合金晶粒度检测的通用参考方法 | [[S4,S16]] |
| ASTM A247 | 铸铁中石墨组织评价标准 | 可用于压铸铸铁类试样的金相评级 | [[S2,S16]] |

## Sources
- S28: [476558_光学显微镜](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97f3feb8-f38a-4091-998c-159d49c145c4/resource) (`97f3feb8-f38a-4091-998c-159d49c145c4`)
- S3: [铝合金薄壁电机壳材料和消失模铸造相关技术问题研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c2a8992-9491-4e41-a097-ce808b3dd1a4/resource) (`0c2a8992-9491-4e41-a097-ce808b3dd1a4`)
- S8: [基于ProCAST的汽车铝合金机油泵体压铸模具开发及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20ed0842-c7fc-473d-844b-8f1352b1ac70/resource) (`20ed0842-c7fc-473d-844b-8f1352b1ac70`)
- S30: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c7e7af2-ab5f-425f-85a7-e724d438037c/resource) (`9c7e7af2-ab5f-425f-85a7-e724d438037c`)
- S7: [脉冲电流对铜液夹杂物影响与行为机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/200aff7e-e5f8-4b21-bd78-fcadce48a4bc/resource) (`200aff7e-e5f8-4b21-bd78-fcadce48a4bc`)
- S19: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62d99eb1-d53f-4b0f-b736-2c33267956d5/resource) (`62d99eb1-d53f-4b0f-b736-2c33267956d5`)
- S24: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bf47958-e8e3-4d02-85d9-7bcc4816e0a5/resource) (`7bf47958-e8e3-4d02-85d9-7bcc4816e0a5`)
- S15: [a dictionary of metallurgy__dbf7a8d57d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43196b74-dbde-481e-8303-e8acb7bddb06/resource) (`43196b74-dbde-481e-8303-e8acb7bddb06`)
- S5: [铝合金水泵座压铸模镶块冷却水道结构改进与压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12da76cd-2dfe-4092-91c9-9b83e13cc694/resource) (`12da76cd-2dfe-4092-91c9-9b83e13cc694`)
- S38: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da31114f-958f-4c08-8b40-23a3cb62b27b/resource) (`da31114f-958f-4c08-8b40-23a3cb62b27b`)
- S31: [ZK61镁合金大型铸锭半连续铸造成形工艺与组织调控机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7f742e9-32b9-4e14-9fad-74ae0e5047f9/resource) (`a7f742e9-32b9-4e14-9fad-74ae0e5047f9`)
- S20: [development and application of biomedical titanium alloys__506c05efbb](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/681d519f-36e9-4b42-905c-660a60d9b700/resource) (`681d519f-36e9-4b42-905c-660a60d9b700`)
- S17: [铝硅合金半固态压铸成形产品缺陷的形成机理及控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/524656ba-1f75-4033-b14d-08f999ce560f/resource) (`524656ba-1f75-4033-b14d-08f999ce560f`)
- S42: [用于铝合金车轮微观组织分析的蔡司光学显微镜（图3-7(a)）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f94eb182-385f-480a-9c93-b38f61359985/resource) (`f94eb182-385f-480a-9c93-b38f61359985`)
- S21: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a6deb75-de2f-4fb0-acbd-f24f03b8c8cc/resource) (`6a6deb75-de2f-4fb0-acbd-f24f03b8c8cc`)
- S37: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d321b57a-2d22-4545-9446-5c085d768cff/resource) (`d321b57a-2d22-4545-9446-5c085d768cff`)
- S22: [金相显微镜基本信息表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71101eef-7ea9-4ea5-8d34-a947a3454e2e/resource) (`71101eef-7ea9-4ea5-8d34-a947a3454e2e`)
- S13: [copper the science and technology of the metal its alloys and compounds__396e9ac6bb](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ae25083-5e18-42b8-9bc0-66445f40f54e/resource) (`3ae25083-5e18-42b8-9bc0-66445f40f54e`)
- S33: [elements of physical metallurgy__5d4ee92381](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ac3ff907-3111-417b-bf17-a900f08ea3dc/resource) (`ac3ff907-3111-417b-bf17-a900f08ea3dc`)
- S39: [光学显微镜、扫描电子显微镜与透射电子显微镜对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dedc4bbd-aabb-4964-81c1-f82e1e64ffa7/resource) (`dedc4bbd-aabb-4964-81c1-f82e1e64ffa7`)
- S10: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2dcbd527-b068-4ca5-abee-f7dad479e1d9/resource) (`2dcbd527-b068-4ca5-abee-f7dad479e1d9`)
- S14: [基于数值模拟的转向器阀壳体压铸模具结构及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3f5b2978-1afa-44d5-9552-65ce46a7be21/resource) (`3f5b2978-1afa-44d5-9552-65ce46a7be21`)
- S6: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1da9741b-d52b-4750-8e77-e3e893d95604/resource) (`1da9741b-d52b-4750-8e77-e3e893d95604`)
- S9: [Mg、Si质量比与热处理对压铸Al-Mg-Si-Mn-Cu-Zr合金组织性能影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/279eaa69-90c4-4358-b12a-e381c27f8ebe/resource) (`279eaa69-90c4-4358-b12a-e381c27f8ebe`)
- S34: [GBT+46786（锌合金压铸件金相检验）-2025.pdf-455a72c0-f3eb-4fd6-9565-d7b87946075e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8cf468f-d5ee-491b-87c7-18c75a4b84cd/resource) (`b8cf468f-d5ee-491b-87c7-18c75a4b84cd`)
- S1: [3D打印砂型对A356铝合金铸造工艺及铸件性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08b89fb3-386f-471c-8e3b-f23bee7e56d8/resource) (`08b89fb3-386f-471c-8e3b-f23bee7e56d8`)
- S43: [材料成形及机械加工工艺基础实验](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc30ce11-1302-45fa-91ca-4867916c56a4/resource) (`fc30ce11-1302-45fa-91ca-4867916c56a4`)
- S26: [材料基础及成型加工实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90da3350-1024-4766-b9ef-02957529643d/resource) (`90da3350-1024-4766-b9ef-02957529643d`)
- S40: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5865418-ccc4-4fb2-9ce6-eeb72924f131/resource) (`e5865418-ccc4-4fb2-9ce6-eeb72924f131`)
- S11: [磨削加工技术难点与测量技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31f36409-8062-4288-866d-0a147ef67361/resource) (`31f36409-8062-4288-866d-0a147ef67361`)
- S23: [effects of rheo die casting process on the microstructure and mechanical__ecaef97071](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/744985f4-3c27-479d-b3a0-abfa58bf8be0/resource) (`744985f4-3c27-479d-b3a0-abfa58bf8be0`)
- S18: [effects of microstructure and casting defects on the fatigue behavior of__dc0f4bf9cf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58d14484-a751-462e-8cf2-bb7ab9b04eeb/resource) (`58d14484-a751-462e-8cf2-bb7ab9b04eeb`)
- S4: [892911_金相分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ef67196-b935-4004-872c-c4dcc252e2d3/resource) (`0ef67196-b935-4004-872c-c4dcc252e2d3`)
- S25: [1991 annual book of astm standards section 2 nonferrous metal products v__3abfaf437d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ab1b1bb-73f2-4452-b7a8-650d974281f2/resource) (`8ab1b1bb-73f2-4452-b7a8-650d974281f2`)
- S36: [1991 annual book of astm standards section 2 nonferrous metal products v__3abfaf437d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8d7255e-524b-4979-af82-26f0e49b03dc/resource) (`c8d7255e-524b-4979-af82-26f0e49b03dc`)
- S2: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0adc0003-5029-4d9b-8ec9-752ab186ce5b/resource) (`0adc0003-5029-4d9b-8ec9-752ab186ce5b`)
- S16: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a9dd5c1-62ce-4cbe-99ea-e72b0262480c/resource) (`4a9dd5c1-62ce-4cbe-99ea-e72b0262480c`)