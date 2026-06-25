---
version: "v1"
generated_at: "2026-06-18T05:38:31+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 57
  source_quality_score: 0.86
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

X射线探伤（又称X光探伤、X射线无损检测）是利用X射线可穿透物质且在穿透过程中存在衰减的特性，检测出被检测对象内部缺陷的无损检测方法[[S21,S41,S34]]。在压铸领域，X射线探伤是检测铸件内部气孔、缩孔、缩松、裂纹及夹杂等缺陷最直观有效的手段之一[[S8,S43]]。

## 基本原理

X射线探伤的核心工作机制基于射线衰减原理：当强度均匀的X射线束穿透被检铸件时，不同密度、不同厚度的基体材料及内部缺陷对X射线的吸收程度存在差异，穿透后剩余射线强度分布的差异可被检测介质捕获，以此判定缺陷的位置、大小与类型[[S63,S41]]。

对于传统胶片型检测，高能X射线穿透被检金属构件时，不同区域因射线吸收量不同造成胶片感光程度存在差异，完成曝光的胶片经暗室冲洗后，可得到黑度分布不同的影像，据此识别内部缺陷[[S63,S3,S8]]。

X射线实时成像及数字化探伤技术无需胶片，依靠图像增强器将穿透铸件后的不可见X射线信号转换为可见光图像，再通过高清相机采集转换为数字图像输入计算机，经处理后在显示设备中直接输出缺陷的性质、尺寸与位置信息，支持大批量铸件在线质检[[S63]]。

![压铸件X射线探伤基础原理示意图，展示X光射线源、光栏、铸件、缺陷、软片、底片等核心部件，以及射线穿过铸件内部缺陷后在感光底片上成像的完整过程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/780f6499-0086-405b-9b25-9b89ecceb45c/resource)

**图1** 压铸件X射线探伤基础原理示意图，展示射线穿过铸件内部缺陷后在感光底片上成像的完整过程[[S30]]。

## 设备组成

X射线探伤系统的典型设备组成包括X射线管、高压发生器、控制台、图像采集系统及防护设施[[S57,S60]]。

### X射线管

X射线管为真空二极管结构，核心包含钨灯丝阴极、高原子序数钨靶阳极。工作时阴极加热释放热电子，在两极高压作用下高速轰击阳极靶辐射出X射线，可单独调控X射线的强度和硬度，是工业压铸无损探伤的核心射线源部件[[S57]]。

![X光探伤装置内部结构原理图，展示钨灯丝、金属靶、铍窗口、聚焦罩等核心部件及其连接关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2206dc4e-0566-4d6c-be49-92e88ab3f7f9/resource)

**图2** X射线发生装置结构示意图，展示钨灯丝、金属靶、铍窗口、冷却水回路等核心部件[[S12]]。

### 高压发生器与控制器

高压发生器由变压器、电容器、整流器、稳流器等部件组成，作用是为X射线管的两极提供加速所需的高压电场，驱动阴极发射的热电子高速轰击阳极靶产生X射线[[S57]]。

控制台集成参数调控、联锁保护功能，可实时设置管电压、管电流、曝光时长等工艺参数，设备通电时触发外部报警指示，配备钥匙开关和检测室安全联锁接口，保障操作安全[[S60]]。

### 图像采集系统

X射线探伤图像采集系统包含三类主流方案[[S48,S29,S59]]：

| 类型 | 技术特点 | 压铸场景适用性 |
|------|----------|---------------|
| 胶片法 | 采用双面涂覆专用乳剂层的工业X射线胶片，配合前后金属增感屏提升感光效率；银盐粒度可分级适配不同缺陷检测精度需求 | 高可靠性要求的航空航天类关键压铸件的存档级检测 |
| CR（计算机射线照相） | 使用存储荧光成像板替代传统胶片完成射线信号采集，后续通过数字扫描转换为可视化图像 | 复杂异形压铸件的批量离线数字化检测 |
| DR（数字实时成像） | 采用平板探测器直接将穿透工件的X射线信号转换为数字化图像，无需暗室胶片冲洗流程 | 压铸自动化产线的高速在线全检场景 |

## 工艺参数

压铸X射线探伤的核心工艺参数取值如下[[S52,S2,S22]]：

| 参数 | 典型取值范围 | 说明 |
|------|-------------|------|
| 管电压 | 铝合金：80~160 kV；通用铸件：80~250 kV | 根据材质与厚度选择 |
| 管电流 | mA级工作档位 | 调节X射线强度 |
| 曝光时间 | 数秒至数分钟 | 根据工件厚度灵活调整 |
| 焦距（FFD） | 300~1000 mm（典型800 mm） | 影响几何不清晰度 |
| 焦点尺寸 | 0.015 mm（微焦点）至5 mm（常规焦点） | 适配不同检测精度要求 |
| 像质计（IQI）灵敏度 | ASTM标准2-2T penetrameter级别 | 底片H&D黑度控制在2.0~2.25 |

## 标准操作流程

压铸X射线探伤标准操作全流程依次为[[S8,S4,S22]]：

1. **工件准备**：对压铸件表面进行清砂、打磨，完全去除表面溅物、油污、锈蚀、飞边等异物，防止表面伪缺陷与内部真实缺陷混淆，按工艺要求标注唯一识别标记。
2. **几何布置**：校准射线源、待检测压铸件、探测器三者的相对位置，确认像质计按标准要求放置于射线源侧工件表面对应位置。
3. **曝光**：根据工件材质、厚度选定预设的管电压、管电流、曝光时间参数完成曝光作业。
4. **图像获取与处理**：胶片法完成暗室显影定影操作，CR/DR法通过软件完成图像去噪、对比度增强等后处理，输出高清晰度缺陷影像。
5. **缺陷评定**：将获取的探伤影像与对应厚度的ASTM/ISO标准参考射线底片进行比对，按指定的severity等级要求评定铸件内部缺陷的合格性。

## 缺陷图像特征

压铸件各类内部缺陷在X射线图像上的典型特征如下：

| 缺陷类型 | 图像特征 |
|----------|----------|
| 气孔 | 圆形或近圆形暗色影像，边界清晰，为卷气或溶解气体析出形成的孔洞[[S61,S42]] |
| 缩孔 | 形状不规则的暗斑，多集中在铸件厚壁、最后凝固区域，局部聚集呈不规则孔洞形态[[S53,S20]] |
| 缩松 | 弥散分布的麻点状、海绵状暗区，无明显边界，为凝固过程中微小补缩不足形成的分散孔洞[[S53,S63]] |
| 裂纹 | 走向杂乱或沿应力分布的曲折细条状暗色线纹，延伸形态不符合卷气或凝固孔洞分布规律[[S33,S56]] |
| 非金属夹杂 | 密度高于基体的氧化物、熔渣类夹杂，底片上呈现亮于周围基体的白亮色影像[[S37,S61]] |

## 评定方法与验收标准

### 核心标准体系

| 标准号 | 适用范围 | 说明 |
|--------|----------|------|
| ASTM E155 | 铝、镁铸件检验用标准参考射线底片 | 将13类常见缺陷按严重程度分为8个等级，配备不同厚度标准参考底片，最新版为2015版[[S45,S6,S14]] |
| ASTM E505 | 铝、镁压铸件参考射线底片（特定厚度范围） | 与ASTM E155配套，针对特定厚度区间给出缺陷分级参考图样[[S66]] |
| ASTM E272 | 高强度铜基和镍铜合金铸件参考射线底片 | 覆盖缩松、气孔等典型缺陷的不同严重程度分级影像参考[[S20,S45]] |
| ISO 10049:1992 | 铝合金铸件针孔度目测评定法 | 专为铝合金铸件针孔类缺陷X射线影像评级制定[[S51]] |
| GB/T 5677-2007 | 铸钢件射线照相及底片等级分类方法 | 等同采用ISO 4993:1987，缺陷分5大类每类6个等级[[S32,S50,S64]] |
| ASTM E94 | 射线检测导则 | 射线检测基本方法指导[[S23,S45]] |
| ASTM E1030 | 金属铸件射线检测试验方法 | 各类材质铸件射线检测方法[[S23,S45]] |

### 评定原则

多缺陷共存时采用“取最低等级”原则进行综合评级[[S32,S50]]。具体而言，在评定视野内同时存在两类以上缺陷时，应按缺陷种类分别进行等级评定，以最低等级定为综合评定等级；同时存在两类以上相同等级缺陷时，其缺陷数、长度和面积都超过该级规定的中间值时，综合评定等级应降低一级[[S50]]。

## 不同压铸合金的适用性

| 合金类型 | 检测适配性 | 透照参数要求 |
|----------|-----------|-------------|
| 铝合金 | 密度较低，相同厚度下所需X射线功率仅为钢件的1/3；缺陷在底片上呈暗于基体的影像[[S37,S24]] | 优先选用较低管电压以提升底片对比度 |
| 镁合金 | 密度在三类合金中最低，适配软X射线透照即可实现高对比度缺陷成像[[S18,S26]] | 透照相同厚度下管电压低于铝合金 |
| 锌合金 | 密度显著高于铝、镁合金[[S36]] | 需选用比铝合金、镁合金更高的管电压，才能保证射线穿透性 |

## 与γ射线探伤、超声探伤的区别

### 与γ射线探伤的核心差异

| 对比维度 | X射线探伤 | γ射线探伤 |
|----------|----------|-----------|
| 射线来源 | X射线机在高压电场作用下加速电子撞击金属靶产生 | 放射性元素的原子核蜕变产生 |
| 适用穿透厚度 | 钢件≤120 mm，铝/镁合金≤200 mm | 钢件可达300 mm |
| 成像清晰度 | 灵敏度高于γ射线，成像质量更优 | 成像清晰度相对较低 |
| 使用场景 | 需外接电源，适合固定场所检测 | 无需外接电源，适合野外、大体积构件现场检测 |

[[S47,S65]]

### 与超声探伤的核心差异

| 对比维度 | X射线探伤 | 超声探伤 |
|----------|----------|----------|
| 检测原理 | 依靠射线穿透衰减差异成像 | 依靠超声波在异质界面的反射信号识别缺陷 |
| 适用对象 | 适配形状复杂、壁厚不均的压铸件，可直接获得缺陷可视化二维投影图像，可明确判定缺陷类型 | 不适用于形状复杂、表面粗糙的薄壁压铸件，厚度低于20 mm时存在检测盲区，难以直观判定缺陷具体类型 |
| 探测深度 | 150 kV设备≤30 mm，250 kV设备可达50~60 mm | 可达20~6000 mm |
| 缺陷种类判别 | 最优（◎） | 较弱（△） |
| 检测速度 | 慢（×） | 快（◎） |
| 设备便携性 | 差（×） | 好（◎） |
| 检测费用 | 高（×） | 低（◎） |

[[S3,S8,S47,S65,S1,S15]]

## 优缺点与局限性

### 优点

- **完全非破坏性**：不会对被检测压铸件的后续使用性能、结构完整性造成任何损伤[[S8]]。
- **直观显示**：可直观显示压铸件内部体积型缺陷的位置、大小、形貌，可识别缩孔、缩松、气孔、夹渣、内部裂纹等多种典型缺陷[[S8,S63,S41]]。
- **可存档**：传统胶片式底片可永久存档，数字式电子图像可长期存储追溯，方便后续质量回溯与工艺优化分析[[S62,S63]]。
- **适合批量检测**：数字式X射线探伤可适配压铸批量化质检场景，提升检测效率[[S63,S13]]。

### 局限性与限制

- **对方向敏感**：针对平面型面缺陷（如微裂纹）存在明显的方向选择性，仅当缺陷平面与X射线入射方向接近平行时才能有效检出；若缺陷平面与射线入射方向垂直则几乎无法识别，易造成漏检[[S54,S62]]。
- **穿透能力有限**：普通机型对铝、镁合金压铸件的最大有效透照厚度在150 mm以内，高能X射线机型理论最大透照厚度可达300 mm级别，但应用普及率低，超厚截面压铸件无法完成有效检测[[S40,S22]]。
- **成本较高**：整套设备购置成本较高，传统胶片检测模式下胶片、显影定影耗材的长期运维成本也处于较高水平[[S63,S62]]。
- **无法区分密度相近的相**：常规X射线探伤无法区分密度相近的不同相组织，如压铸铝镁合金中密度接近的初生α-Al相和共晶Al相无法被有效识别[[S31,S62]]。

## 安全防护与人员资质

### 辐射防护三原则

X射线探伤辐射防护需遵循电离辐射防护三大原则：辐射实践正当化、辐射防护最优化、个人剂量限值制度[[S60]]。

### 防护措施

综合采用三类防护措施[[S60,S16,S35]]：

1. **时间防护**：尽可能缩短接触射线的时间，在高辐射场中作业前预先规划操作流程，使操作人员停留时间最短。
2. **距离防护**：射线的剂量率与距离的平方成反比，采用长距离操作机械手增大操作人员与放射源间的距离。
3. **屏蔽防护**：利用各种屏蔽物体吸收射线。

### 检测室与现场作业要求

| 场景 | 安全要求 |
|------|----------|
| 固定式专用检测室 | 屏蔽墙外300 cm处空气比释动能率不大于2.5 μGy/h；配套安装门-机联锁安全装置、照射信号指示器，确保检测门关闭后X射线装置才能启动[[S35]] |
| 移动式/现场检测 | 控制器与X射线管头连接电缆长度不得短于20 m；将被检物体周围空气比释动能率大于15 μGy/h的区域划定为控制区，控制区外大于1.5 μGy/h的区域划定为监督区，设置明显警示标识，夜间加装红色警示灯[[S35,S55]] |

### 人员资质

- 探伤人员必须持有国家主管部门颁发的对应其作业类别和级别的有效资格证书，严禁无证上岗操作[[S55,S40]]。
- 需按GB4792标准要求定期接受个人辐射剂量监测，作业过程中必须随身携带个人剂量笔、剂量报警仪等检测设备，严格控制自身受照剂量不超过国家规定限值[[S55,S35,S38]]。

## 技术分类

按成像探测器类型分类，工业X射线探伤在无损检测标准体系下明确分为四类主流技术[[S5,S25]]：

| 技术类型 | 探测介质 | 空间分辨率 | 检测效率 | 压铸场景适用性 |
|----------|----------|-----------|----------|---------------|
| 胶片射线照相 | 银盐胶片 | 最高 | 低，需暗室处理 | 航空航天类关键压铸件的存档级检测 |
| 实时成像（RTR） | 荧光屏/影像增强器 | 低于胶片 | 高，可实时在线观察 | 大批量普通压铸件产线在线快速筛选 |
| 计算机射线照相（CR） | 存储荧光板 | 中等 | 中等，需扫描步骤 | 复杂异形压铸件的批量离线数字化检测 |
| 数字射线照相（DR） | 平板探测器 | 高于RTR、低于胶片 | 最高，直接输出数字实时图像 | 压铸自动化产线的高速在线全检 |

[[S58,S5,S8]]

## 与其他无损检测方法的关系

压铸行业常用的四种无损检测方法的边界与互补关系如下表[[S1,S11,S46,S8,S15]]：

| 评价维度 | X射线探伤（RT） | 超声探伤（UT） | 渗透探伤（PT） | 磁粉探伤（MT） |
|----------|----------------|---------------|---------------|---------------|
| 检测原理 | 波的吸收 | 波的反射 | 毛细作用 | 磁力作用 |
| 检出缺陷方向 | 与射线平行方向缺陷 | 与波束垂直方向缺陷 | 表面开口缺陷 | 表层缺陷 |
| 适用材质 | 不限 | 不限 | 不限 | 仅铁磁性材料 |
| 铸件适用性 | 很合适（◎） | 合适（○） | 合适（○） | 很合适（◎） |
| 气孔检出 | 很合适（◎） | 合适（○） | 不适合（×） | 需附加条件（△） |
| 裂纹检出 | 需附加条件（△） | 需附加条件（△） | 很合适（◎） | 很合适（◎） |
| 缺陷种类判别 | 最优（◎） | 较弱（△） | 好（○） | 好（○） |
| 检测速度 | 慢（×） | 最快（◎） | 较慢（△） | 好（○） |
| 检验费用 | 高（×） | 低（◎） | 中等（○） | 中等（○） |

> 注：◎表示很合适/常用，○表示合适，△表示满足附加条件时合适，×表示不合适[[S15]]。

## 典型应用场景

X射线探伤在压铸领域的典型应用包括[[S43,S13,S44]]：

- 铝合金、镁合金等压铸件的批量内部质量抽检与全检；
- 汽车轻量化结构件（端盖、减速器基座、发动机支架、轴承座等）的出厂质检；
- 航空航天精密压铸件、电力电子类压铸件的内部缺陷评定；
- 压铸工艺优化阶段的缺陷分布验证。

压铸X射线探伤可稳定检出压铸件的各类体积型及部分面型内部缺陷，包括气孔、缩孔、缩松、疏松、内部裂纹、非金属夹渣/夹杂，可准确判定缺陷的平面投影位置、尺寸分布与缺陷类型[[S8,S3,S43,S20]]。

## Sources
- S21: [18884425_X射线探伤](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4c8f6cb7-c7ae-4aec-9c16-be589750cf44/resource) (`4c8f6cb7-c7ae-4aec-9c16-be589750cf44`)
- S41: [18884425_X射线探伤](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/950e59ad-a19d-448a-af6e-b23bf704fdbc/resource) (`950e59ad-a19d-448a-af6e-b23bf704fdbc`)
- S34: [8800907_X射线探伤机](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8180a403-4346-408b-9f1f-818dd558b31f/resource) (`8180a403-4346-408b-9f1f-818dd558b31f`)
- S8: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19ff374d-680f-4e32-8fa3-fea57f912f62/resource) (`19ff374d-680f-4e32-8fa3-fea57f912f62`)
- S43: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/972094cb-2ac5-46e0-9523-cbadbbaca479/resource) (`972094cb-2ac5-46e0-9523-cbadbbaca479`)
- S63: [汽车壳体类铸件的压铸工艺优化及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f57810a5-ccef-4ddc-b6f1-db407bd5f8d6/resource) (`f57810a5-ccef-4ddc-b6f1-db407bd5f8d6`)
- S3: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10897c57-25bf-448d-9697-f19474abfdb6/resource) (`10897c57-25bf-448d-9697-f19474abfdb6`)
- S30: [X光检验原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/780f6499-0086-405b-9b25-9b89ecceb45c/resource) (`780f6499-0086-405b-9b25-9b89ecceb45c`)
- S57: [熔模精密铸造 下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d340463c-89ce-4949-bf40-f6cbf9bded66/resource) (`d340463c-89ce-4949-bf40-f6cbf9bded66`)
- S60: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e18207c4-1619-4359-ac8e-56c8d75c6829/resource) (`e18207c4-1619-4359-ac8e-56c8d75c6829`)
- S12: [X光探伤原理图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2206dc4e-0566-4d6c-be49-92e88ab3f7f9/resource) (`2206dc4e-0566-4d6c-be49-92e88ab3f7f9`)
- S48: [18884425_X射线探伤](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a89aa2a3-386a-4bab-8215-8da75c9285c7/resource) (`a89aa2a3-386a-4bab-8215-8da75c9285c7`)
- S29: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/756a0f62-8577-445e-979e-9f78c70af401/resource) (`756a0f62-8577-445e-979e-9f78c70af401`)
- S59: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6aafc15-d5ee-4e7a-a370-81bd4cfa6c58/resource) (`d6aafc15-d5ee-4e7a-a370-81bd4cfa6c58`)
- S52: [1600335_X射线探伤仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bdb3791f-3a93-4096-a239-712a9c698337/resource) (`bdb3791f-3a93-4096-a239-712a9c698337`)
- S2: [表5-5 射线检测条件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/027fd830-c7bf-4ea7-a9e6-56adf4533b2f/resource) (`027fd830-c7bf-4ea7-a9e6-56adf4533b2f`)
- S22: [1991 annual book of astm standards section 1 iron and steel products vol__e3a5133ba7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/519c69bd-29fa-49a6-ad0b-df99956fa917/resource) (`519c69bd-29fa-49a6-ad0b-df99956fa917`)
- S4: [钛合金离心泵壳机加工石墨型铸造及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/131f117c-aed2-4461-8824-2319cb6d0c9f/resource) (`131f117c-aed2-4461-8824-2319cb6d0c9f`)
- S61: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8ffc81a-4da0-446b-b6d5-dfca4099b5b2/resource) (`e8ffc81a-4da0-446b-b6d5-dfca4099b5b2`)
- S42: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/955713a6-115a-4ce9-8885-cc04a2d6b6b8/resource) (`955713a6-115a-4ce9-8885-cc04a2d6b6b8`)
- S53: [A356铝合金空气压缩机支架流变压铸模拟仿真及成形工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf618543-7f30-42bc-9ae6-a211377091c9/resource) (`bf618543-7f30-42bc-9ae6-a211377091c9`)
- S20: [casting copper base alloys__d5182d5c2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/495ff91f-05f3-4c9a-b421-b2a80a1d5bc7/resource) (`495ff91f-05f3-4c9a-b421-b2a80a1d5bc7`)
- S33: [半固态压铸件X射线探伤局部图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8018c7c7-8363-4724-a323-d00abc2c6caf/resource) (`8018c7c7-8363-4724-a323-d00abc2c6caf`)
- S56: [用г探伤法研究铸件中缺陷的资料总结](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c9f3c7d9-0b70-4abc-82b2-1848e789e2f3/resource) (`c9f3c7d9-0b70-4abc-82b2-1848e789e2f3`)
- S37: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8dc026ff-3073-48b8-ab05-f4980c7b7673/resource) (`8dc026ff-3073-48b8-ab05-f4980c7b7673`)
- S45: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0066f78-962a-4a94-b885-d173f9607d78/resource) (`a0066f78-962a-4a94-b885-d173f9607d78`)
- S6: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/16c52e27-18b5-49ca-ac17-2d2bc16a4704/resource) (`16c52e27-18b5-49ca-ac17-2d2bc16a4704`)
- S14: [1991 annual book of astm standards section 2 nonferrous metal products volume 0202 die cast metals aluminum and magne...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/269dbcdb-8068-4d0f-b0d6-c00b695d6d4c/resource) (`269dbcdb-8068-4d0f-b0d6-c00b695d6d4c`)
- S66: [铝合金铸件国内外射线检测标准对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fdb4c95c-e8d5-47c9-bd65-47e5bd1b54d0/resource) (`fdb4c95c-e8d5-47c9-bd65-47e5bd1b54d0`)
- S51: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bbdfd10d-500b-41dd-bd20-5ac0efd8c501/resource) (`bbdfd10d-500b-41dd-bd20-5ac0efd8c501`)
- S32: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f0141e2-b76f-4dd9-a163-cbad98381f06/resource) (`7f0141e2-b76f-4dd9-a163-cbad98381f06`)
- S50: [最新铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b65365b4-f46c-47a4-b1b1-fef3bc128d07/resource) (`b65365b4-f46c-47a4-b1b1-fef3bc128d07`)
- S64: [最新铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f82f3205-d575-499a-944c-e0310348183b/resource) (`f82f3205-d575-499a-944c-e0310348183b`)
- S23: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58981e05-ccb0-4455-9a5c-b127f8162831/resource) (`58981e05-ccb0-4455-9a5c-b127f8162831`)
- S24: [铝合金铸件国内外射线检测标准对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a4721d9-23f1-48fb-94a6-ec7529106962/resource) (`5a4721d9-23f1-48fb-94a6-ec7529106962`)
- S18: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37dec74f-4c62-40e2-9af3-8582db6d27c3/resource) (`37dec74f-4c62-40e2-9af3-8582db6d27c3`)
- S26: [新编铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6cc9507f-4f4f-4c87-a863-bdeb0da20ce9/resource) (`6cc9507f-4f4f-4c87-a863-bdeb0da20ce9`)
- S36: [锌合金3（Zinc Alloy 3）金属数据表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87cdf214-834c-483f-be69-bbcd5d34e4db/resource) (`87cdf214-834c-483f-be69-bbcd5d34e4db`)
- S47: [工程材料及金属热加工基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a69ffd40-e725-4f96-82e5-c267bcb38229/resource) (`a69ffd40-e725-4f96-82e5-c267bcb38229`)
- S65: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb897efc-a6e1-4b49-8bdb-f54197e3db95/resource) (`fb897efc-a6e1-4b49-8bdb-f54197e3db95`)
- S1: [几种无损检验方法的综合比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00a84924-87a9-4fc6-99c0-7ec51cdd73d5/resource) (`00a84924-87a9-4fc6-99c0-7ec51cdd73d5`)
- S15: [TextNode1463](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/29996ce1-ea12-4378-b2eb-5a5cf515dc3d/resource) (`29996ce1-ea12-4378-b2eb-5a5cf515dc3d`)
- S62: [铝合金的搅拌摩擦焊接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed6e3359-6a11-4e3c-9799-c34e0a163cd8/resource) (`ed6e3359-6a11-4e3c-9799-c34e0a163cd8`)
- S13: [铝合金压铸件X射线图像内部缺陷智能检测与分割方法研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22162bc4-e3e9-4739-9e76-fc3abebba753/resource) (`22162bc4-e3e9-4739-9e76-fc3abebba753`)
- S54: [金属材料塑性成形实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c0842b5e-b3df-445b-bde5-d0c8307c6952/resource) (`c0842b5e-b3df-445b-bde5-d0c8307c6952`)
- S40: [最新铸造标准实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9340d68c-6db0-4637-a084-150fc981a1eb/resource) (`9340d68c-6db0-4637-a084-150fc981a1eb`)
- S31: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8f34c5-e0a7-4690-86b6-0a9a7180f2f4/resource) (`7b8f34c5-e0a7-4690-86b6-0a9a7180f2f4`)
- S16: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e310421-ffdf-423a-9132-84de3588a8b1/resource) (`2e310421-ffdf-423a-9132-84de3588a8b1`)
- S35: [新编铸造技术数据手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/83c1f56b-f632-45fe-8d38-1bed85991002/resource) (`83c1f56b-f632-45fe-8d38-1bed85991002`)
- S55: [中国机械工业标准汇编 铸造卷 下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c28e3df2-ae21-4bc4-8da6-f56ea1a1a07f/resource) (`c28e3df2-ae21-4bc4-8da6-f56ea1a1a07f`)
- S38: [金属工艺学 第4分册 铸造、锻压和焊接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8fec4e71-dd84-45fc-b313-c2ccf5e4edbe/resource) (`8fec4e71-dd84-45fc-b313-c2ccf5e4edbe`)
- S5: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1455f1b1-abbc-4298-9426-6a477bc4bb85/resource) (`1455f1b1-abbc-4298-9426-6a477bc4bb85`)
- S25: [0052_e144b7ece1ca5425_无损检测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b559146-a95a-488b-81a4-2a1e92bfb965/resource) (`5b559146-a95a-488b-81a4-2a1e92bfb965`)
- S58: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d62b8e25-4f37-4180-ab02-8bc1fd188577/resource) (`d62b8e25-4f37-4180-ab02-8bc1fd188577`)
- S11: [实用铸件缺陷分析及对策实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/200de5f7-b3de-4ce8-9a9d-9b262942fc81/resource) (`200de5f7-b3de-4ce8-9a9d-9b262942fc81`)
- S46: [木塑复合材料的表面处理与胶接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a390b7dd-e202-4ba1-9c14-d8539527c091/resource) (`a390b7dd-e202-4ba1-9c14-d8539527c091`)
- S44: [1991 annual book of astm standards section 2 nonferrous metal products volume 0202 die cast metals aluminum and magne...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99364ce8-7f61-4820-b169-af52609cef64/resource) (`99364ce8-7f61-4820-b169-af52609cef64`)