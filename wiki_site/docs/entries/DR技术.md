---
version: "v1"
generated_at: "2026-06-18T07:15:54+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 30
  source_quality_score: 0.84
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

DR技术在压铸工业领域指数字射线成像技术（Digital Radiography，DR），是射线无损检测（NDT）类别中的一种数字成像检测方法[[S7,S35]]。DR通过X射线透照被检压铸件，由平板探测器直接捕获穿透后的射线信号并转换为数字图像，经计算机图像处理与分析系统实现缺陷检测与评定[[S7,S13]]。

与传统胶片射线照相相比，DR省去了暗室处理环节，具备实时性强、检测结果易于数字化存储与分析的特点；与计算机射线照相（CR）依靠成像板间接读出的路线不同，DR采用平板探测器完成“X射线→电信号”的一步直接转换[[S13,S24]]。DR系统既可作静态单帧成像，也支持工件运动状态下的动态（实时）连续成像，后者被视为DR较其他射线检测手段更为先进的突出优势之一[[S8]]。

---

## 设备组成与系统架构

工业压铸DR检测系统典型由四大硬件核心构成：**X射线发射源、机械传动检测工作台、数字平板探测器、计算机图像处理分析系统**[[S2,S29]]。

### X射线发射源

面向较大壁厚压铸件检测，工程中可选YXLON品牌的MG452型工业X射线径向源（X射线机），主要公开参数如下[[S8,S28]]：

| 参数项 | 参数值 |
|--------|--------|
| 最大管电压 | 450 kV |
| 额定最大功率 | 4.5 kW |
| 阳极靶材 | 钨质靶材，嵌装在铜质阳极基座 |
| 冷却方式 | 强制水冷 |
| 适用最大厚度（黑色金属/复杂铝合金压铸件） | 约230 mm |

### 检测工作台

配套的ϕ500 mm检测工作台台面直径为500 mm，支持工件夹紧后沿X轴、Y轴双向平移以及360°全周旋转运动，运行平顺稳定以避免产生衍射斑纹干扰面型缺陷识别；同时配备专用快速定位夹具。行业通用机械参数主要包括[[S28]]：

| 机械参数 | 指标要求 |
|----------|----------|
| X/Y轴行程 | ≥±200 mm |
| 额定负载 | ≥50 kg |
| 旋转定位精度 | ≤±0.1° |
| 平移重复定位精度 | ≤±0.05 mm |

### 数字平板探测器

压铸DR检测中广泛采用非晶硅（amorphous silicon）平板探测器。此类探测器无需图像增强环节，可将入射X射线能量直接转换为电信号，其成像质量可达到AGFA C7胶片系统的水平[[S13,S24]]。典型探测器参数范围如下[[S24,S32]]：

| 探测器参数 | 典型值/范围 |
|------------|--------------|
| 像素尺寸 | 127 μm ~ 200 μm |
| 动态范围 | ≥14 bit |
| 实时成像帧速率 | 5 ~ 30 fps |
| 常用积分时间 | 400 ms（可满足多数压铸缺陷识别要求） |

探测器正式检测前需预热30 min以上，并依次完成暗场校正、增益校正与坏像素校正[[S24]]。

### 原理示意与系统布局配图

- 图1示意了X射线透射检测的基本路径：X射线源 → X射线束 → 待检T型件 → DR平板探测器[[S1]]。

![压铸DR系统透射检测原理示意图（常规垂直照射方向）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03414165-6d3f-4f8f-a2a1-d21ea022d586/resource)

- 图2展示了面向汽车铝合金压铸件检测的工业DR检测系统整机实物布局，直观标明了X射线发射源、机械传动系统、数字平板探测器与计算机图像处理系统四大模块的相对位置[[S2]]。

![面向汽车铝合金压铸件检测的工业DR检测系统整机实物布局图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/066f98d6-d096-4872-a1f2-0cc004bade9d/resource)

---

## 工作原理与关键工艺参数

### 成像流程

工业DR系统成像基本流程为：X射线源产生可控X射线 → 射线穿透压铸件并携带工件内部衰减信息 → 平板探测器将接收的X射线光子能量直接转换为模拟电信号 → 模数转换生成原始数字灰度图像 → 依次进行暗场校正、增益校正、坏像素剔除、缺陷识别标注等多项数字图像处理与分析操作，最终输出检测结果[[S8,S13,S28]]。

### 动态成像实现方式

DR的动态（实时）成像依赖以下三方面条件[[S8,S24]]：

1. 采用高稳定X射线源（如MG452型），保证在工件运动期间射线输出强度的一致性；
2. 平板探测器工作在RAD高速采集模式，以400 ms及以下短积分时间连续读取信号；
3. 探测器内置实时校正模块，能够在铸件随检测工作台旋转/平移时，同步完成运动状态下的图像校正，实现不用等工件完全静止即可获得清晰连续的多角度扫描图像。

### 代表性检测工艺示例

以钛合金筒形铸件的DR检测为例，公开试验工艺参数如下[[S24]]：

| 工艺参数 | 设定值/要求 |
|----------|-------------|
| 几何焦距（源到探测器距离） | 875 mm |
| 探测器工作模式 | RAD模式 |
| 探测器积分时间 | 400 ms |
| 单部位采集帧数 | 10帧 |
| 图像处理方法 | 中值法 |
| 目标区域图像灰度要求 | >5000 |
| 探测器预热时间 | ≥30 min |
| 像质计类型 | Ti丝型像质计（HB7684-2000），置于源侧 |

---

## 检测能力与适用对象

### 可检缺陷类型

DR可有效检出压铸件内部的典型缺陷，包括：气孔（gas porosity）、缩孔（shrinkage cavity）、缩松（shrinkage porosity / sponge）、裂纹（crack）、冷隔（cold shut）、夹杂（金属夹杂与非金属夹杂）以及偏析（segregation）等[[S7,S11,S19,S34]]。

### 适用材料

DR检测适用于常见压铸合金材料，包括铝合金、镁合金和锌合金等[[S22,S37]]。

### 适用工件类型

DR可检测的代表性工件包括T型件、汽车结构件及缸体等，可用于分析T型件内部纤维分布及孔隙缺陷[[S37]]。

在铝合金压铸件DR检测中，单壁扫描成像质量最优；双壁扫描时图像质量虽有下降，但缺陷图像与正常图像仍可清晰区分；当工件出现三层及以上重叠壁结构时，空间分辨率会明显降低，并出现阴影图像效应，此时可酌情改用胶片照相检测[[S25]]。

### 检出能力验证

在钛合金筒形铸件的验证试验中，预制28个缺陷（14个孔型缺陷、14个线型缺陷），除1个Φ2 mm气孔处于最厚壁区域（非检测区）外，其余27个缺陷均能被DR检出，DR的检测能力与AGFA C7传统胶片射线照相相当[[S24,S3,S6]]。但对厚壁极限区域的小尺寸缺陷（如该试验中的Φ2 mm气孔），DR同样存在识别上限[[S24,S6]]。

对于1 mm壁厚的ZL114A铝合金铸件，DR仍可分辨不同灰度级别，表明对应的灰度灵敏度可达毫米级壁厚差异的识别水平[[S8]]。

---

## 动态DR检查的优势

与静态DR及传统胶片法相比，动态/实时DR在压铸件检测中具有以下突出优势：

- **快速在线筛查**：工件在检测工作台上旋转/平移时，DR即可实时成像，无需工件完全静止；对一个直径600 mm、长度1100 mm的铝合金筒形铸件，全扫检测大约仅需58 min，检测效率大幅提升[[S25,S22]]。
- **缺陷动态识别**：双壁扫描中，前后两壁在不同旋转方向下成像各异的“动态呈现”，有助于清晰区分缺陷，而静态成像则难以获得同样效果[[S25]]。
- **自动化兼容性好**：动态DR更容易嵌入压铸件大批量在线自动检测系统，满足现代压铸车间的客观、可重复且高效的质量控制需求[[S8,S35]]。

---

## 局限性

1. **二维投影限制**：DR输出二维灰度投影图像，无法像工业CT那样提供断层的三维立体信息，难以直接确定缺陷在厚度方向上的精确位置与真实体积尺寸[[S20]]。
2. **复杂结构制约**：当压铸件存在三层及以上重叠墙体结构时，空间分辨率和缺陷识别能力均明显下降，此时需要考虑替代检测方案[[S25]]。
3. **穿透与分辨率折中**：在厚壁区或接近设备穿透极限时，小型缺陷（如Φ2 mm气孔）可能无法识别[[S6,S24]]。

---

## 辐射安全要求

工业DR检测涉及电离辐射，必须遵守三项基本防护原则：辐射实践正当化、辐射防护最优化（照射量应保持在可合理达到的尽可能低的水平）、个人剂量限值制度；外照射防护应综合运用时间防护、距离防护与屏蔽防护三项措施[[S30]]。

**检测室与设备安全要求**[[S30]]包括：
- 高压接通时须配置外部报警/指示装置，控制台设钥匙开关并配备检测室联锁接口；
- 屏蔽墙外300 cm处空气比释动能率不得大于2.5 μGy/h；
- 检测室须安装门-机联锁安全装置；无迷路检测室的门防护性能应与同侧屏蔽墙完全等效；
- 移动式X射线装置控制器与射线管头连接电缆长度不得短于20 m。

**作业人员安全要求**[[S27,S5,S17]]包括：
- 必须持有国家主管部门颁发的相应等级NDT资格证书，并完成专项辐射安全培训；
- 作业时须配备辐射巡检仪、报警式剂量计与个人累积剂量片三类基础安全监测设备；
- 流动作业透照现场应划定安全警示区、设置明显警示标志；夜间作业须加装红色警示灯。

---

## 相关标准

在压铸及工业DR检测领域，主要参考标准体系如下[[S16,S21,S12]]：

| 标准/规范 | 适用范围 |
|-----------|----------|
| GB/T 5677-2007（等同采用ISO 4993:1987） | 铸钢件射线照相检测通用要求[[S16,S23]] |
| ISO 17636-2 | 焊接数字探测器射线检测（DR）工艺与评级要求[[S12]] |
| ASTM E94 | 射线检测工艺指南[[S21]] |
| ASTM E1030 | 金属铸件射线检测试验方法[[S21,S38]] |
| ASTM E155 | 铝、镁铸件参考射线底片[[S21,S38]] |

铝合金铸件缺陷评定时，ISO 9915规定5 cm×5 cm评定单元内的组合验收规则：同一单元内同时存在两种缺陷且每种均达到最大允许级别时，判定为不合格；存在三种及以上缺陷时，若至少两种达到最大极限值则直接判不合格；若仅一种缺陷达到最大值，需其余缺陷中至少一种比其限定级别低一级方可合格；同一单元内出现四种及以上不同缺陷直接判不合格[[S18,S36]]。

---

## 别名与术语整理

在压铸DR检测领域，正式术语为“数字射线成像技术（Digital Radiography, DR）”，行业中可出现以下叫法：

- 电子成像DR系统
- DR检测系统
- 数字射线检测工艺
- 实时射线成像（强调动态成像功能）
- 工业数字射线照相

其中，“mg452类型X射线径向射源”和“ϕ500 mm检测工作台”为具体设备部件规格术语，非DR技术的通用别名[[S28,S37]]。

## Sources
- S7: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22162bc4-e3e9-4739-9e76-fc3abebba753/resource) (`22162bc4-e3e9-4739-9e76-fc3abebba753`)
- S35: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f016da81-4844-4f74-9e3d-1bbaf2933011/resource) (`f016da81-4844-4f74-9e3d-1bbaf2933011`)
- S13: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64d3e169-3901-47f1-9ca2-cd1a8a3c9f4a/resource) (`64d3e169-3901-47f1-9ca2-cd1a8a3c9f4a`)
- S24: [钛合金筒形铸件的数字射线检测研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a967cef3-d5ca-44d9-852c-e718ff477963/resource) (`a967cef3-d5ca-44d9-852c-e718ff477963`)
- S8: [TextNode0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/275908b2-f8d5-46df-be8a-fd1183e6be81/resource) (`275908b2-f8d5-46df-be8a-fd1183e6be81`)
- S2: [图2.11 X射线图像检测系统](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/066f98d6-d096-4872-a1f2-0cc004bade9d/resource) (`066f98d6-d096-4872-a1f2-0cc004bade9d`)
- S29: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6aafc15-d5ee-4e7a-a370-81bd4cfa6c58/resource) (`d6aafc15-d5ee-4e7a-a370-81bd4cfa6c58`)
- S28: [低压铸造水冷机壳X射线检测图像技术分析与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cdd11783-750b-4fe5-a283-80dba82e54a1/resource) (`cdd11783-750b-4fe5-a283-80dba82e54a1`)
- S32: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8ffc81a-4da0-446b-b6d5-dfca4099b5b2/resource) (`e8ffc81a-4da0-446b-b6d5-dfca4099b5b2`)
- S1: [复合材料T型件的DR无损检测示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03414165-6d3f-4f8f-a2a1-d21ea022d586/resource) (`03414165-6d3f-4f8f-a2a1-d21ea022d586`)
- S11: [TextNode2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/573339a9-c4a9-4525-a167-20b3484693ae/resource) (`573339a9-c4a9-4525-a167-20b3484693ae`)
- S19: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/972094cb-2ac5-46e0-9523-cbadbbaca479/resource) (`972094cb-2ac5-46e0-9523-cbadbbaca479`)
- S34: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef389a96-eb48-4959-bee3-37047f189437/resource) (`ef389a96-eb48-4959-bee3-37047f189437`)
- S22: [2118301_铸造铝合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1dc4c74-ebb5-46ac-8f03-a9b0d9590a81/resource) (`a1dc4c74-ebb5-46ac-8f03-a9b0d9590a81`)
- S37: [22050155_数字X线摄影](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc69bfdb-387e-4cdc-8a64-4f1b03fc537e/resource) (`fc69bfdb-387e-4cdc-8a64-4f1b03fc537e`)
- S25: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aaef9152-affc-42c2-b8ea-f8a164de4ce2/resource) (`aaef9152-affc-42c2-b8ea-f8a164de4ce2`)
- S3: [钛合金筒形铸件的数字射线检测研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ac4f45b-0d0b-4918-868a-efd8eb5239c7/resource) (`0ac4f45b-0d0b-4918-868a-efd8eb5239c7`)
- S6: [表4 工件缺陷检测结果统计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20172fb3-de04-4ebe-bb27-b6eb08c93456/resource) (`20172fb3-de04-4ebe-bb27-b6eb08c93456`)
- S20: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/989ee977-c7c1-4cd1-8458-b668a099de6b/resource) (`989ee977-c7c1-4cd1-8458-b668a099de6b`)
- S30: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e18207c4-1619-4359-ac8e-56c8d75c6829/resource) (`e18207c4-1619-4359-ac8e-56c8d75c6829`)
- S27: [中国机械工业标准汇编 铸造卷 下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c28e3df2-ae21-4bc4-8da6-f56ea1a1a07f/resource) (`c28e3df2-ae21-4bc4-8da6-f56ea1a1a07f`)
- S5: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d1ea1d5-3fed-4fbb-9da4-5f70ef3763a4/resource) (`1d1ea1d5-3fed-4fbb-9da4-5f70ef3763a4`)
- S17: [api recommende practice 577 welding inspection and metallurgy dowstream__191da2d5fa](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f5a8447-f913-4115-8581-3090998c39ac/resource) (`8f5a8447-f913-4115-8581-3090998c39ac`)
- S16: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f0141e2-b76f-4dd9-a163-cbad98381f06/resource) (`7f0141e2-b76f-4dd9-a163-cbad98381f06`)
- S21: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0066f78-962a-4a94-b885-d173f9607d78/resource) (`a0066f78-962a-4a94-b885-d173f9607d78`)
- S12: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58981e05-ccb0-4455-9a5c-b127f8162831/resource) (`58981e05-ccb0-4455-9a5c-b127f8162831`)
- S23: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a68aaf5a-dd6d-4daf-98ee-2e147104e994/resource) (`a68aaf5a-dd6d-4daf-98ee-2e147104e994`)
- S38: [铝合金铸件国内外射线检测标准对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdb4c95c-e8d5-47c9-bd65-47e5bd1b54d0/resource) (`fdb4c95c-e8d5-47c9-bd65-47e5bd1b54d0`)
- S18: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/955713a6-115a-4ce9-8885-cc04a2d6b6b8/resource) (`955713a6-115a-4ce9-8885-cc04a2d6b6b8`)
- S36: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0ef2ed6-b7e8-4be5-9c5f-ed738140d758/resource) (`f0ef2ed6-b7e8-4be5-9c5f-ed738140d758`)