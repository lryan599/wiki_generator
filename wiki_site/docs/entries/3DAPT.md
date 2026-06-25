---
version: "v1"
generated_at: "2026-06-18T16:51:26+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 29
  source_quality_score: 0.87
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述与定义

**三维原子探针层析技术**（3D Atom Probe Tomography，简称3DAPT），亦称三维原子探针（3DAP）、原子探针层析技术（APT），是一种基于场离子显微镜（FIM）与飞行时间质谱原理结合发展而来的、具备近原子级三维元素分布重构能力的微观化学分析技术[[S5,S11]]。该技术历史上亦被称为位置敏感原子探针（PoSAP）和层析原子探针（TAP）[[S1,S11]]。其作为场离子显微技术的衍生方法，严格要求待测样品为尖端锋利、高长径比的针状几何构型，这是实现单原子级高精度三维元素分布表征的基础前提[[S5,S29]]。

在材料科学领域，3DAPT是目前唯一能够在三维空间中同时实现近原子分辨率、逐原子级灵敏度以及全元素定性定量分析的表征手段[[S15,S23]]。

## 工作原理

3DAPT的核心工作机制包含场蒸发、离子飞行时间质谱与位置敏感探测三个关键技术环节，以实现原子在三维空间内的精准定位与鉴别：

1.  **场蒸发（Field Evaporation）**  
    通过向曲率半径约 50 nm 的针状样品尖端表面施加强度达几至几十 V/nm 的极强电场（高压脉冲或超快激光脉冲辅助），使得处于尖端表层原子被逐层电离并以离子形态脱离样品表面[[S7,S33]]。由此，样品的原子从表层开始分层剥离，实现了对材料沿深度方向精确剖析的可能。

2.  **飞行时间质谱（Time-of-Flight Mass Spectrometry）**  
    电离生成的离子在电场驱动下沿高真空飞行管进行无碰撞飞行。系统记录单个离子从样品端到达探测器的精确飞行时间，配合已知飞行距离，根据其质荷比（m/q）判定该离子的元素种类[[S7,S33]]。

3.  **位置敏感探测（Position-Sensitive Detection）**  
    离子到达探测器时，其横向撞击坐标 x、y 由位置敏感探测器（PSD）记录，结合离子被探测的先后顺序分配其深度方向的 z 坐标。由此，通过收集百万乃至上亿个原子的四维数据（x, y, z, 质荷比），最终重构出被测区域内近原子分辨率的三维全元素空间分布图谱[[S1,S7,S20]]。

传统的飞行时间原子探针（1DAP）仅记录原子的 z 轴深度信息，其分析结果仅为一维成分浓度曲线。三维原子探针在此基础上引入了横向位置探测能力，在深度剖析之余重建了完整的空间元素分布[[S9,S20]]。下方工作示意图清晰展示了1DAP与3DAPT的核心结构差异，以及3DAPT中离子横向坐标探测的关键原理。

![图 常规飞行时间原子探针（1DAP）与三维原子探针（3DAP）工作原理对比示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3149e43d-867c-47bf-a5fb-f4d3cb679d54/resource)

![图 位置敏感探测器记录离子横向坐标的原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b5216b5-3204-46a1-afeb-7732ce86ec26/resource)

## 设备组成

现代APT仪器的关键部件组成如下[[S5,S4]]：

*   **样品座与低温系统**：用于固定针尖试样，并通常配备低温恒温器将样品冷却至约 20 K 以抑制原子热运动，保障超高真空环境。
*   **局域提取微电极**：微米级孔径，放置于针尖前方几微米处。该电极通过减小电场施加距离，显著减小了诱发场蒸发所需的脉冲电压幅值（常规不超过 5 kV），从而支持更高的脉冲重复频率（可达 100 kHz 以上）。
*   **高压脉冲/超快激光脉冲发生模块**：向样品表面提供场蒸发所需的瞬态能量脉冲。对于导电性差的半导体、氧化物等材料，则采用脉宽为 300 fs 至几十 ps 的飞秒级脉冲激光激发场蒸发。
*   **高真空飞行管**：为离子提供无碰撞的飞行路径，保证飞行时间测量的准确性。
*   **带微通道板的位置灵敏探测器**：记录离子撞击的 x、y 位置和时间信号。

## 关键性能参数

现代3DAPT设备的关键性能指标如下表所示：

| 参数类别 | 典型参数/性能 | 备注与意义 |
| :--- | :--- | :--- |
| 空间分辨率 | 横向：≤ 0.2–0.3 nm；深度方向：~0.1 nm | 可分辨材料内部原子尺度的结构排布[[S11,S15]] |
| 质量分辨率（m/Δm） | > 300 | 配备反射式能量补偿器，可无歧义区分复杂商用铝合金中的绝大多数合金元素[[S1,S8,S11]] |
| 探测灵敏度 | 单原子级 | 质谱仪可识别单个原子的质荷比，成分统计精度约 0.1 at.%[[S5,S15]] |
| 典型分析体积 | 50×50×200 nm³ | 一次性分析可记录约 10⁷~10⁸ 个原子的事件[[S15,S33]] |
| 分析速率 | > 10,000 原子/秒 | 局域电极技术的引入将分析效率提升了1–2个数量级[[S4]] |

## 试样制备

3DAPT分析对试样有严格的几何要求，需为尖端曲率半径极小的针状。

### 传统电解抛光法

针对可加工的金属丝材，传统试样制备流程为二步电解抛光[[S10,S18]]：
1.  **初次减薄**：将细金属丝在 70%磷酸-30%去离子水溶液中，以 4–7 V 直流电压进行减薄。
2.  **尖端精细抛光**：使用含乙酸和铬酸钠的抛光液（比例约 1 g 四水合铬酸钠溶于 10 ml 乙酸），在 8–11 V 直流电压下完成针尖成型。若针尖发生断裂或钝化，可采用 2%高氯酸的丁氧基乙醇溶液通过铂丝小液滴回路进行二次锐化。

### 聚焦离子束（FIB）制样法

对于位置精度要求极高的压铸件或复杂三维微纳结构样品，目前主要采用FIB技术定点制备针尖，其标准流程包含以下步骤[[S14,S25,S22]]：
1.  **沉积保护层**：在目标待分析区域表面，先后利用低电压（如 5 kV）电子枪和 30 kV Ga³⁺ 离子枪沉积 Pt 保护层，避免后续高能离子束铣削损坏待分析区域。
2.  **原位剥离薄片**：使用 30 kV 镓离子束在目标区域两侧及底部铣削出沟槽，将包含目标分析区域的薄片从块体样品中完整剥离。
3.  **转移与固定**：通过显微操作微探针将薄片提取并转移、焊接至支撑针座上。
4.  **尖端成型与修整**：逐步降低 Ga 离子束电流参数，对薄片进行逐层同心圆减薄，最终获得顶端厚度低于 100 nm 的楔形尖端结构。

最终的针尖顶端曲率半径需精细控制在 10–50 nm 区间，并保持尖端沿长度方向拥有稳定的锥形角，以规避测试过程中的断裂风险[[S13,S29]]。此外，最终减薄步骤需采用低于 1 kV 的低能离子束进行清洁处理，以最大限度消除 Ga 离子注入造成的表面弹道混合伪影[[S13]]。

### 压铸件取样注意事项

由于压铸件内部存在复杂的非平衡快凝组织和铸造缺陷，取样时需给予额外关注[[S6,S36]]：
*   **选取目标区域**：应避开压铸过程产生的表面夹渣、近表层孔洞及粗大共晶相团聚区域，优先在已确定的目标微区（如预期含有纳米析出相或目标晶界的位置）取样。
*   **优化减薄工艺**：需逐步调整离子束参数，防止铝合金等材料中硬度差异显著的多相组织因铣削速率不均导致尖端非均匀变形，降低制备过程中的提前断裂概率[[S13]]。

## 在压铸领域的应用价值

压铸合金属于快速凝固体系，其微观组织普遍存在纳米尺度溶质偏聚、亚稳态析出相及晶界处复杂的成分分布。3DAPT是目前突破常规技术局限，在原子尺度直接解析该类组织特征的最适宜手段之一[[S23,S34]]。

1.  **纳米析出相成分的独立、精准定量**
    传统透射电镜（TEM/STEM）搭载的能谱分析（EDS）受限于电子束与样品交互体积效应，所获得的纳米相成分信号不可避免地混合了大量基体相信息[[S8]]。3DAPT的空间分辨率可达原子层级，分析人员可以直接框选一个小于析出相尺寸的选定体积，对其内部原子进行独立计数，从而获得不受基体相信号干扰的纳米析出相本征化学组成[[S8,S30]]。例如，相关科研团队利用 APT 技术直接测定了 Al-Mg-Si 系合金中最关键的时效强化相 β'' 相的精确化学计量比为 Mg₅Si₄Al₂[[S27]]。

2.  **揭示合金元素的分配与溶质偏聚规律**
    *   **元素分配定量**：在 Al-1.15Mg-1.14Si-0.268Cu-0.0141Fe (at.%) 峰时效合金的 APT 研究中，成功测定了约 20% 的 Cu 原子参与时效析出过程，而约 80% 的 Cu 原子仍保留在基体中发挥固溶强化作用。这一结果为精确计算合金的固溶强化贡献值提供了直接的实验依据[[S27]]。
    *   **晶界偏聚与力学性能关联**：APT能够直接、定量地揭示压铸镁合金、铝合金中溶质原子沿晶界的富集浓度，并可结合宏观力学性能测试，建立晶界偏聚程度与铸件抗拉强度、延伸率之间的定量关联[[S12,S28]]。

3.  **研究时效过程中的析出序列**
    对于Al-Mg-Si-Cu系合金，3DAPT不仅可以识别β″、β′、Q′等关键时效强化相，还能追踪其复杂的前驱过渡相（如S、L、C、QP、QC相等），使得完整复现压铸合金在后续人工时效热处理中的全周期析出序列成为可能[[S21]]。

## 技术对比：优势与局限

### 与其他微区成分分析技术的对比

3DAPT与扫描电镜（SEM）、电子探针（EPMA）以及透射电镜（TEM/STEM）在空间分辨率和成分分析能力上存在显著代差。以下从样品要求、分析尺度及核心能力等方面进行详细比较。

| 特征维度 | 3DAPT | SEM-EDS/WDS | TEM/STEM-EDX | EPMA (WDS) |
| :--- | :--- | :--- | :--- | :--- |
| **样品要求** | 尖端曲率半径~50 nm的针状试样[[S33]] | 兼容最大~10×10 cm的块状样品[[S31]] | 厚度 < 100 nm 的薄箔，制备难度大、耗时长[[S31]] | 抛光块状样品，通常需导电镀层[[S31]] |
| **空间分辨率** | 横向 0.2–0.3 nm，深度 0.1 nm[[S11,S15]] | 微米级（受电子束交互体积限制）[[S31]] | 亚纳米级（探针），但成分信号空间分辨受样品厚度限制[[S8,S31]] | 微米级（受电子束交互体积限制）[[S31]] |
| **分析维度** | 三维全元素重构图[[S1]] | 一维（点分析）/二维（面扫描）[[S31]] | 一维/二维，或三维重构（耗时） | 一维/二维 |
| **成分表征能力** | 单原子灵敏度，~0.1 at.% 统计精度，无基体干扰[[S5,S8]] | 半定量至定量，对轻元素灵敏度较低 | 定量，但纳米析出相成分信号受基体混叠干扰严重[[S8,S30]] | 定量，波长分辨率高，但空间分辨能力弱[[S31]] |
| **核心局限** | 样品破坏性、分析体积极小[[S4,S33]] | 空间分辨率较低（微米级）[[S31]] | 分析体积小，制样繁复、存在电子束散射导致的基体信号混合问题[[S8,S31]] | 仅能获取微米级的成分信息[[S31]] |

### 3DAPT的局限性

尽管3DAPT具有原子层级的解析能力，其在应用中的局限同样突出[[S4,S5,S33]]：
*   **破坏性表征与试样要求苛刻**：测试过程通过在脉冲电场下逐层场蒸发离子，通过消耗整个针尖样品完成分析，样品无法回收。同时，样品必须被制备为尖端曲率半径约 50 nm 的高长径比针状，对制样设备与人员经验要求极高[[S33,S13]]。
*   **分析体积小，统计代表性受限**：单次典型分析体积仅约 10⁵ nm³，涉及原子总量~10⁶ 至 10⁸个。受限于统计规律，其常规成分测量精度约为 0.1 at.%。对于微米尺度的第二相或缺陷，其在此类极小体积内被捕获的概率极低，无法对大体积材料进行统计学意义上的第二相体积分数统计[[S5,S4]]。
*   **成分假象风险**：测试及制样过程可能引入三类主要假象：(1) 不同相的场蒸发阈值差异导致“局部放大效应”，造成元素空间分布失真；(2) 部分元素多电荷态质谱峰的重叠引发定量误差；(3) FIB制样时的 Ga 离子注入和弹道混合效应会引入非本征成分[[S13,S19]]。
*   **数据处理高度复杂**：三维坐标重构依赖于理想点投影假设（back-projection），实际测试中数据易出现图像畸变，通常需要结合透射电镜等关联显微表征技术进行校准。海量原子数据集必须使用专用算法进行处理，数据解析门槛高、周期长[[S8,S19]]。

## 标准与规范

截至2026年6月，国际标准化组织（ISO）和美国材料与试验协会（ASTM）体系中暂未发布原子探针层析分析的独立专项标准。该领域在全球范围内的通用权威操作指南为由Elsevier出版的学术专著 **《Atom Probe Tomography: Put Theory into Practice》**，该书由该领域核心专家编写，系统论述了3DAPT从样品制备、测试操作到数据解析的全流程规范。此外，世界范围内主流的商业化APT仪器供应商 CAMECA/AMETEK 发布的 LEAP 系列设备官方操作手册，为行业提供了基础性的实操规范[[S33,S15]]。

## 典型分析示例

作为通用能力展示，公开资料中收录了3DAPT应用在 Inconel X-760 镍基高温合金中的标准分析数据，展示了该技术的核心输出类型：从分析体积内（如：7×7×40 nm³）直接构建三维 Al 和 Ti 原子分布图，并通过选定区域进行原子计数统计，获得合金元素沿深度方向的一维浓度分布曲线（concentration depth profile）[[S30]]。尽管当前直接针对压铸铝合金、镁合金特定牌号（如ADC12、AZ91D）的3DAPT公开研究案例数量尚不多见，其技术方法和工作流程对于表征压铸合金中的纳米尺度组织已展现出极高的适配性[[S1,S24]]。

## Sources
- S5: [TextNode832](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e6f7124-e977-4b0f-a24a-c31a3adf92eb/resource) (`1e6f7124-e977-4b0f-a24a-c31a3adf92eb`)
- S11: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/372ee86c-9277-4bd3-baa6-795687311bff/resource) (`372ee86c-9277-4bd3-baa6-795687311bff`)
- S1: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01ce9ab1-e749-453c-b9e7-2b2cc6ab2747/resource) (`01ce9ab1-e749-453c-b9e7-2b2cc6ab2747`)
- S29: [TextNode844](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c871eed2-f83d-4058-9598-3951c1fae03e/resource) (`c871eed2-f83d-4058-9598-3951c1fae03e`)
- S15: [TextNode434](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/526cc315-1433-46f1-a03c-7e4e4751b945/resource) (`526cc315-1433-46f1-a03c-7e4e4751b945`)
- S23: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8040381a-ec73-4b0c-a379-5902c8bbf9cf/resource) (`8040381a-ec73-4b0c-a379-5902c8bbf9cf`)
- S7: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/256615c6-03f0-4595-bd39-4dd5b03a3118/resource) (`256615c6-03f0-4595-bd39-4dd5b03a3118`)
- S33: [TextNode435](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb982dac-c033-44f5-a948-be36fcfe06da/resource) (`eb982dac-c033-44f5-a948-be36fcfe06da`)
- S20: [图15.1 (a) 传统飞行时间原子探针原理示意图；(b) 三维原子探针原理示意图。](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65bf22e6-1505-48da-a77b-18fc31715166/resource) (`65bf22e6-1505-48da-a77b-18fc31715166`)
- S9: [图15.1 常规飞行时间原子探针（1DAP）与三维原子探针（3DAP）的原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3149e43d-867c-47bf-a5fb-f4d3cb679d54/resource) (`3149e43d-867c-47bf-a5fb-f4d3cb679d54`)
- S4: [alloy physics a comprehensive reference__0572c6adf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/187ef9c4-a072-4b64-90aa-1e56e5e2d4a3/resource) (`187ef9c4-a072-4b64-90aa-1e56e5e2d4a3`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cf45de3-99c0-4466-9f08-84357f9959bf/resource) (`2cf45de3-99c0-4466-9f08-84357f9959bf`)
- S10: [decomposition of alloysthe early stages__3e07cf9fbe](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/35e19cce-59d6-4c18-9596-e3d57dbbde7c/resource) (`35e19cce-59d6-4c18-9596-e3d57dbbde7c`)
- S18: [decomposition of alloys the early stages proceedings of the 2nd acta scr__62779ff670](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60c197fd-3265-4413-8b5a-3732c745e20a/resource) (`60c197fd-3265-4413-8b5a-3732c745e20a`)
- S14: [carbon alloys novel concepts__44fdd170cc](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b6f9ff8-905d-470a-a288-d6befd73f9d7/resource) (`4b6f9ff8-905d-470a-a288-d6befd73f9d7`)
- S25: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89a8a185-135c-41fa-90ad-700a06417717/resource) (`89a8a185-135c-41fa-90ad-700a06417717`)
- S22: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72cc6b73-d884-4c41-9469-6789eefdaf5c/resource) (`72cc6b73-d884-4c41-9469-6789eefdaf5c`)
- S13: [TextNode845](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/459afca3-ceda-4546-b973-71e8aabc14f3/resource) (`459afca3-ceda-4546-b973-71e8aabc14f3`)
- S6: [压铸铝合金研究现状与未来发展趋势](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/229dea7d-d879-4251-a364-024bedca3c6c/resource) (`229dea7d-d879-4251-a364-024bedca3c6c`)
- S36: [压铸成型工艺及模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f521c2e9-7dbf-44c2-a82f-5210aab43a51/resource) (`f521c2e9-7dbf-44c2-a82f-5210aab43a51`)
- S34: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef7cf1b8-b70f-4fa3-be8a-c264645f5189/resource) (`ef7cf1b8-b70f-4fa3-be8a-c264645f5189`)
- S30: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d23c2791-48b2-47ca-9dd4-393693f6652c/resource) (`d23c2791-48b2-47ca-9dd4-393693f6652c`)
- S27: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b3912501-633c-4de9-a6e7-dfa524c66718/resource) (`b3912501-633c-4de9-a6e7-dfa524c66718`)
- S12: [铁铝金属间化合物合金化与成分设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4380effc-956c-4f8a-bf24-5825b316aadd/resource) (`4380effc-956c-4f8a-bf24-5825b316aadd`)
- S28: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bd9814f6-5e98-4821-8609-114ec92ba8d9/resource) (`bd9814f6-5e98-4821-8609-114ec92ba8d9`)
- S21: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a6aa65c-3916-4048-ba58-31ada5802366/resource) (`6a6aa65c-3916-4048-ba58-31ada5802366`)
- S31: [characterization of minerals metals and materials 2013 proceedings of a__b4b8d0d97d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc/resource) (`d38e6ca7-d9cd-4b9b-8e85-5a8c3582dbfc`)
- S19: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61cda757-33ec-46d5-8959-5b63ed3453d6/resource) (`61cda757-33ec-46d5-8959-5b63ed3453d6`)
- S24: [die casting effect on surface characteristics of thin walled az91d magne__f28f4e7437](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/825b66f5-724f-4d31-99c4-81cbc03149e7/resource) (`825b66f5-724f-4d31-99c4-81cbc03149e7`)