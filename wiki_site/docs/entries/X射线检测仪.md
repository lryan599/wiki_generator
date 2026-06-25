---
version: "v1"
generated_at: "2026-06-18T11:04:26+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 39
  source_quality_score: 0.82
  freshness_score: 0.86
  evidence_coverage_score: 1.0
---

## 概述

X射线检测仪是面向工业压铸领域，利用X射线穿透金属材料的衰减特性，在不破坏压铸件的前提下检测其内部气孔、缩孔、裂纹、夹渣等缺陷的专用无损检测设备[[S9,S7,S46]]。该设备属于工业无损检测（NDT）体系下的工业射线检测（RT）大类，核心组件X光管作为耗材，额定使用寿命约2000小时，主流型号整机成本约50万元[[S9]]。设备完全区别于医用X射线诊疗设备，专门针对金属铸件内部结构成像设计[[S46]]。

## 技术分类体系

压铸场景下的X射线检测体系包含三类主流技术路线，存在清晰的从属包含关系[[S43,S46,S50]]：

- **传统胶片射线照相**：以银卤化物胶片作为探测介质，通过暗室冲洗获得二维投影缺陷影像，检测周期长，底片可长期存档[[S43]]。
- **数字射线成像（DR）**：以平板探测器直接将穿透铸件的X射线信号转化为数字化二维图像，成像速度快，适配实时质检场景[[S14,S43]]。
- **工业计算机断层扫描（工业CT）**：通过多角度扫描与三维重构获得铸件内部断层的空间分布数据，缺陷定位精度最高，但检测耗时较长[[S43,S47]]。

在设备部署形态上，可区分为在线检测设备与离线检测设备两类。

### 在线检测设备

在线压铸件X射线检测设备专门适配压铸生产线大批量连续质检需求，与产线传送带、自动化分拣机构深度集成[[S29,S31]]。典型代表如XR160INLINE机型，配置160kV高频恒压X射线机、高分辨率平板探测器，支持手动/半自动两种工作模式，可实现铸件输送、多位置自动成像、缺陷判定、不合格件自动分拣的半自动化流程[[S29]]。

![铝合金压铸件在线X射线检测平台，配置多自由度机械臂与X射线探测器组件，可自动完成多角度位姿调整](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/007e34fe-c537-43c5-ada8-80f9a6a661b9/resource)

### 离线检测设备

离线压铸件X射线检测设备未与压铸产线直接集成，属于独立质检工位设备，侧重高精度成像与复杂缺陷表征能力，主要应用于压铸工艺研发验证、小批量特殊件抽检、失效分析、缺陷定量定级等场景，支持多视角多角度扫描，可获取更清晰的低对比度缺陷特征[[S13,S8]]。

![压铸场景专用X射线探伤检测仪实物图，展示工业检测环境下的设备布局，配置圆形铸件检测工作台](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a9d68a8-069d-4578-b797-88692674b609/resource)

## 典型设备参数

### 传统胶片射线照相设备

传统胶片射线照相设备面向压铸件检测的典型参数如下[[S40,S18,S2,S10]]：

| 参数项 | 典型值/范围 |
|-------|-----------|
| 管电压 | 60~300kV（便携式如丹东奥龙XYD-1540为80~100kV） |
| 焦点尺寸（Ir192伽马射线探伤机） | 3×2.6mm |
| 成像介质 | 工业X射线胶片，配套Pb材质0.15/0.15mm增感屏 |
| 底片黑度 | 1.5~4.0 |
| 标准透照焦距 | 800mm |
| 单工件检测耗时 | 数小时（含暗室冲洗） |

传统胶片射线照相执行ASTM E1030等铸件射线检测相关标准，采用单胶片观测模式，可识别铝压铸件内气孔、缩松等体积型内部缺陷[[S37,S2]]。

### DR检测设备

DR检测相比传统胶片成像可实现实时动态成像，无需暗室冲洗处理流程，面向中小型铝合金压铸件的单工件平均检测耗时可压缩至数秒级[[S14,S53]]。

| 参数项 | 典型值/范围 |
|-------|-----------|
| 在线专用机型管电压 | 160kV（XR160INLINE高频恒压X射线机） |
| 通用工业DR设备最高管电压 | 450kV（YXLON MG452型号径向射源） |
| 适配铝合金铸件最大透照厚度 | 230mm |

![汽车铝合金压铸件DR检测完整成像系统，标注展示计算机图像处理系统、X射线发射源、机械传动系统、数字平板探测器四大核心组成](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/066f98d6-d096-4872-a1f2-0cc004bade9d/resource)

### 工业CT设备

工业CT面向常规铝合金压铸件的最大穿透厚度可达200mm以上，单工件常规锥束扫描的平均检测耗时为数分钟至数十分钟，可获取无影像重叠的二维断层图像，重建得到三维内部结构信息[[S47,S5,S42]]。

| 参数项 | ZXVoxel D-450机型 | ICT-450机型 | 常规工业CT系统 |
|-------|-------------------|-------------|---------------|
| 管电压 | 400kV | 430kV | — |
| 管电流 | 1.7mA | 1.5mA | — |
| 焦点尺寸 | 0.4mm | 0.4mm | — |
| 空间分辨率 | — | — | 1 lp/mm |
| 密度分辨率 | — | — | 0.1%~0.5% |
| 可识别最小裂纹 | — | — | 0.05mm宽 |

日联科技UNC系列压铸检测CT机型射线管支持160/225/320/450kV多档位可选，可适配不同壁厚铝合金压铸件的检测需求[[S26]]。

## 检测能力

### 可检测缺陷类型

压铸场景下X射线检测可稳定识别的典型内部缺陷类型包括[[S34,S14,S33,S41,S20]]：

| 缺陷类型 | 说明 |
|---------|------|
| 气孔 | 由于气体卷入或析出形成的球形或近球形孔洞 |
| 缩孔 | 凝固收缩过程中形成的形状不规则的孔洞 |
| 缩松 | 呈海绵状或弥散分布的微小收缩孔隙群 |
| 内部裂纹 | 热应力或收缩应力导致的内部断裂 |
| 非金属夹杂/夹渣 | 氧化物膜或熔渣夹入铸件本体 |
| 冷隔 | 两股金属流汇合处未完全熔合 |

上述缺陷类型可完整覆盖GB/T 11346、ASTM E155等压铸件射线检测标准中要求的全部内部缺陷检测项[[S34]]。GB/T 25747（镁合金压铸件）-2022附录E中，针对不同透视厚度分别规定了气孔、冷隔、缩松、夹杂物四类缺陷的级别评定要求[[S41]]。

### 检测灵敏度

常规工业X射线探伤对压铸件的通用检测灵敏度指标为：可检出的最小缺陷尺寸为被透视铸件厚度的1%~2%[[S33]]。采用高精度DR成像设备时可稳定识别≥1mm的微小内部缺陷，工业CT技术可进一步实现亚毫米级的缺陷尺寸定量测量，精准定位缺陷在铸件三维空间内的位置[[S43,S36]]。

## 过程角色与应用

### 全流程质检覆盖

X射线检测在压铸全流程中可覆盖以下三类核心应用场景[[S29,S44,S51]]：

1. **首件工艺验证**：试模阶段用于验证压射参数、模具浇排系统设计的合理性，辅助优化工艺。
2. **生产过程质量抽检**：量产阶段按抽样规则开展过程质量监控，及时发现工艺漂移问题。
3. **批量成品全检**：高安全等级汽车、航空类压铸件采用100%全检模式，拦截不合格品。

### 自动化检测流程

以XR160INLINE半自动化X射线检测平台为例[[S29]]：

- **手动模式**：质检人员完成上下件后，人工控制机械臂完成不同位置成像，人工评估缺陷后分拣不合格件。
- **半自动模式**：机械臂按预设程序自动完成多位置成像，系统可自动根据图像分析结果完成分拣，缺陷定级环节保留人工判定。

面向铝合金压铸件的X射线图像缺陷智能检测研究显示，结合PANet多尺度特征融合与Soft-NMS算法的实验组，缺陷检测mAP可达0.799，召回率达91.69%[[S3]]。

## 与其他NDT方法的比较

### 优势

数字X射线成像检测技术相比磁粉、渗透、超声三类常规NDT方法，具备实时性好、缺陷成像直观易于判别、成像精度高的独有优势，可直接识别复杂薄壁/变截面铝合金压铸件内部的气孔、缩孔、缩松、夹渣等多类隐藏缺陷，是压铸件内部质量排查的主流方法[[S14,S52]]。

### 各方法适用性对比

| NDT方法 | 适用场景 | 限制 |
|---------|---------|------|
| 磁粉检测 | 铁磁性材料近表面缺陷 | 不适用于铝、镁等非铁磁性压铸件内部检测[[S22,S12]] |
| 荧光/着色渗透检测 | 表面开口类微小缺陷 | 无法识别完全闭合的内部隐藏缺陷[[S11]] |
| 超声波检测 | 简单规则形体内部缺陷 | 对结构复杂、壁厚不均匀的异形压铸件适配性差，难以准确判定缺陷类型和几何尺寸[[S52,S11,S54]] |
| X射线检测 | 各类压铸件内部缺陷全面排查 | 实时成像、缺陷直观、精度高[[S14,S52]] |

### 核心局限性

1. **壁厚限制**：常规X射线设备可适配的铝合金压铸件最大常规检测厚度有限，当检测厚度超过35mm时，推荐选用Se-75放射源辅助完成检测[[S23]]。
2. **辐射安全**：X射线检测属于电离辐射类检测作业，必须严格落实专项辐射安全防护管理要求，作业区域需设置隔离屏蔽设施，操作人员需持证上岗[[S46]]。
3. **成本因素**：核心组件X光管额定使用寿命约2000小时，整机成本约50万元，维护成本较高[[S9]]。

## 相关标准与规范

### 国际标准体系

- **ASTM E94**：射线检测通用导则，为压铸件X射线检测国际标准体系的核心工艺基础文件[[S54]]。
- **ASTM E1030**：金属铸件射线检测标准试验方法，通常与E94配合制定铸件射线检测作业流程[[S37]]。
- **ASTM E155**：铝及镁铸件检测用标准参考射线底片，配套完成压铸件内部缺陷的等级评定[[S37]]。
- **ISO 5579**：国际通用金属材料射线检测基础方法标准，适用于各类压铸件的X射线检测作业规范制定[[S23]]。
- **ISO 17636**：国际通用的焊缝及铸件射线检测质量分级标准，规定了不同压铸件服役场景下的内部缺陷允许阈值，需结合供需双方技术协议完成最终内部质量判定[[S35,S49]]。

### 国内标准体系

国内压铸件X射线检测相关标准体系要求[[S38,S23]]：

- **GB/T 3323系列**：国内射线检测标准体系，配套要求在满足射线穿透能力的前提下优先选择较低的射线能量作业，提升检测底片的成像对比度，保障细小缺陷的检出率[[S38]]。
- **射线源要求**：在合规场景下仅允许采用X射线源完成检测，不得使用γ射线源开展作业，部分细分行业标准（如CB/T 1226）还明确要求采用软X射线机开展轻量化薄壁压铸件的检测[[S38]]。

## 应用实例

### 工艺参数优化验证

在不同浇注温度条件下，X射线扫描图像可直观呈现压铸件内部缺陷的对应关系。以镁合金薄壁压铸件为例，对比650℃、670℃、690℃三种浇注温度下的X射线扫描结果表明：650℃时存在欠铸缺陷，670℃充填完整无缺陷，690℃则出现粘料与缩孔缩松缺陷，为工艺调试提供直接依据[[S6]]。

### 工艺改进效果确认

半固态流变挤压铸造工艺中，通过对比不同压力工况下的X射线探伤图可见：30MPa工况下铸件厚壁区域呈现明显密集缺陷，120MPa高压力工况下铸件内部几乎无可见缺陷，有效验证了工艺参数对内部质量的改善效果[[S45]]。

## Sources
- S9: [55816097_X射线检测仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15223a1a-193e-496b-8e56-8ced70c291ed/resource) (`15223a1a-193e-496b-8e56-8ced70c291ed`)
- S7: [压铸工艺及设备模具实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ff12e08-b9e6-4f1a-870a-9cd489c380b5/resource) (`0ff12e08-b9e6-4f1a-870a-9cd489c380b5`)
- S46: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f016da81-4844-4f74-9e3d-1bbaf2933011/resource) (`f016da81-4844-4f74-9e3d-1bbaf2933011`)
- S43: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6aafc15-d5ee-4e7a-a370-81bd4cfa6c58/resource) (`d6aafc15-d5ee-4e7a-a370-81bd4cfa6c58`)
- S50: [钛合金筒形铸件的数字射线检测研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6edd5e1-f78b-4c22-a393-bc75b37bf214/resource) (`f6edd5e1-f78b-4c22-a393-bc75b37bf214`)
- S14: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22162bc4-e3e9-4739-9e76-fc3abebba753/resource) (`22162bc4-e3e9-4739-9e76-fc3abebba753`)
- S47: [2988569_工业CT](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f534c912-33fd-470d-98f5-cce217b845db/resource) (`f534c912-33fd-470d-98f5-cce217b845db`)
- S29: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/756a0f62-8577-445e-979e-9f78c70af401/resource) (`756a0f62-8577-445e-979e-9f78c70af401`)
- S31: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81d8ff94-b13f-4551-b0b8-83e500bb0254/resource) (`81d8ff94-b13f-4551-b0b8-83e500bb0254`)
- S13: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1df7a917-5078-4362-8325-8623107a72ab/resource) (`1df7a917-5078-4362-8325-8623107a72ab`)
- S8: [基于MAGMAsoft的铝合金变速箱壳体压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/126ac154-34ce-4677-8254-096455454bec/resource) (`126ac154-34ce-4677-8254-096455454bec`)
- S40: [1600335_X射线探伤仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bdb3791f-3a93-4096-a239-712a9c698337/resource) (`bdb3791f-3a93-4096-a239-712a9c698337`)
- S18: [压铸技术手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/396346ee-8e57-4980-8231-65834c0eed36/resource) (`396346ee-8e57-4980-8231-65834c0eed36`)
- S2: [表5-5 射线检测条件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/027fd830-c7bf-4ea7-a9e6-56adf4533b2f/resource) (`027fd830-c7bf-4ea7-a9e6-56adf4533b2f`)
- S10: [1745102_X射线检测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18619227-10b7-42be-8b5d-220633edf217/resource) (`18619227-10b7-42be-8b5d-220633edf217`)
- S37: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0066f78-962a-4a94-b885-d173f9607d78/resource) (`a0066f78-962a-4a94-b885-d173f9607d78`)
- S53: [22050155_数字X线摄影](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc69bfdb-387e-4cdc-8a64-4f1b03fc537e/resource) (`fc69bfdb-387e-4cdc-8a64-4f1b03fc537e`)
- S5: [2988569_工业CT](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/085e17a6-601a-4030-a446-6fd12b60dcd3/resource) (`085e17a6-601a-4030-a446-6fd12b60dcd3`)
- S42: [ZL204合金疏松特征及成因分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cea7ab60-b3bc-4d47-a575-d7b72d4e2c05/resource) (`cea7ab60-b3bc-4d47-a575-d7b72d4e2c05`)
- S26: [铝合金水泵座压铸模镶块冷却水道结构改进与压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/678eb6ac-4dd0-4cf0-b4ea-91a2dafe9e9d/resource) (`678eb6ac-4dd0-4cf0-b4ea-91a2dafe9e9d`)
- S34: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/972094cb-2ac5-46e0-9523-cbadbbaca479/resource) (`972094cb-2ac5-46e0-9523-cbadbbaca479`)
- S33: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9671212c-18c5-4ff6-ae4f-4c46f4b990e0/resource) (`9671212c-18c5-4ff6-ae4f-4c46f4b990e0`)
- S41: [GBT+25747（镁合金压铸件）-2022.pdf-f266316c-4e63-4876-881c-0d821dbec4cd](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c740876a-8f7d-428e-8475-a3c7c91cb46e/resource) (`c740876a-8f7d-428e-8475-a3c7c91cb46e`)
- S20: [casting copper base alloys__d5182d5c2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/495ff91f-05f3-4c9a-b421-b2a80a1d5bc7/resource) (`495ff91f-05f3-4c9a-b421-b2a80a1d5bc7`)
- S36: [基于ProCAST的复杂形貌耐热不锈钢薄壁件模拟与工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b3734d4-52c0-4ca6-a95d-acd561ac01cf/resource) (`9b3734d4-52c0-4ca6-a95d-acd561ac01cf`)
- S44: [铝合金水泵座压铸模镶块冷却水道结构改进与压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3fc399c-2b24-4bce-8055-05d23802254d/resource) (`e3fc399c-2b24-4bce-8055-05d23802254d`)
- S51: [0102_4dd5b7cf1506bb03_Automated_X-ray_inspection](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7bb2514-186f-4ab8-b0bd-3686151e5233/resource) (`f7bb2514-186f-4ab8-b0bd-3686151e5233`)
- S3: [表2.5 基于FPN和ResNet101模型提升策略在Soft-IOU指标中的实验结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/02e66dff-fdf6-4327-9104-14d91566714d/resource) (`02e66dff-fdf6-4327-9104-14d91566714d`)
- S52: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb897efc-a6e1-4b49-8bdb-f54197e3db95/resource) (`fb897efc-a6e1-4b49-8bdb-f54197e3db95`)
- S22: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59b12e9d-3275-41ba-aaa9-cf1c092fd2c6/resource) (`59b12e9d-3275-41ba-aaa9-cf1c092fd2c6`)
- S12: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19ff374d-680f-4e32-8fa3-fea57f912f62/resource) (`19ff374d-680f-4e32-8fa3-fea57f912f62`)
- S11: [铝压铸成型及质量控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18e2815a-e884-40cc-87be-97f73661ee7a/resource) (`18e2815a-e884-40cc-87be-97f73661ee7a`)
- S54: [铝合金铸件国内外射线检测标准对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdb4c95c-e8d5-47c9-bd65-47e5bd1b54d0/resource) (`fdb4c95c-e8d5-47c9-bd65-47e5bd1b54d0`)
- S23: [铝合金铸件国内外射线检测标准对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a4721d9-23f1-48fb-94a6-ec7529106962/resource) (`5a4721d9-23f1-48fb-94a6-ec7529106962`)
- S35: [1991 annual book of astm standards section 2 nonferrous metal products volume 0202 die cast metals aluminum and magne...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98b0922b-7de3-4c1d-8e4e-e35b9b49102e/resource) (`98b0922b-7de3-4c1d-8e4e-e35b9b49102e`)
- S49: [1996 annual book of astm standards section 1 lron and steel products vol__4daf73f604](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5e3509c-1145-4ee8-8117-ab5d197793c5/resource) (`f5e3509c-1145-4ee8-8117-ab5d197793c5`)
- S38: [铝合金铸件国内外射线检测标准对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a73ad872-0f9d-4df2-b90d-6226931bb5d7/resource) (`a73ad872-0f9d-4df2-b90d-6226931bb5d7`)
- S6: [图6 不同浇注温度下薄壁压铸件的温度场分布、铸件实物图及X射线扫描图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d46f9cc-594c-44db-b0d5-198d36924f43/resource) (`0d46f9cc-594c-44db-b0d5-198d36924f43`)
- S45: [图4-18 不同压力下半固态流变挤压铸造铸件的X射线探伤图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8624d52-bb4d-42f6-902c-4ca21165fa7f/resource) (`e8624d52-bb4d-42f6-902c-4ca21165fa7f`)