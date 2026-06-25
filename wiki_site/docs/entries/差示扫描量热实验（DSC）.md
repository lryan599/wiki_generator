---
version: "v1"
generated_at: "2026-06-18T14:58:58+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 53
  source_quality_score: 0.84
  freshness_score: 0.83
  evidence_coverage_score: 1.0
---

## 概述

差示扫描量热法（DSC）是在程序控温条件下，测量输入到试样和参比物的功率差与温度关系的热分析技术，可定量得到相变及热反应的热焓数据[[S35,S5]]。该技术通过“功率补偿”或“热流差分”硬件设计，直接输出与热流相关的定量信号，消除了传统差热分析（DTA）中固有的基线漂移问题。DSC 是压铸铝合金及准晶材料领域最常用的热分析表征手段之一，覆盖凝固特性分析、特征相热效应识别、凝固路径推演、缺陷溯源等多个方向[[S44,S43,S62]]。

## 分类与工作原理

当前工业应用的主流 DSC 仪器分为**热流型（HF-DSC）** 和**功率补偿型（PC-DSC）** 两大类[[S16,S5]]。

### 热流型 DSC

热流型 DSC 将试样和参比单元对称布置在高导热性的共底导热盘上，通过测量二者的温度差换算得到差分热流，具有时间常数小、响应速度快的特点，分为圆柱型和圆盘型两种结构[[S16,S8]]。其核心热传导关系为：

\[
\Delta T(t) = T_{sc} - T_{rc} = R_e \cdot C_{rc}\frac{dT_{rc}}{dt} - R_e \cdot C_{sc}\frac{dT_{sc}}{dt} - R_e \cdot \dot{\lambda}
\]

热阻 \(r\) 极小，等效热阻 \(R_e\) 相应极小，保证了仪器的快速响应[[S16]]。

![圆盘型热流DSC热传导原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86032ab3-7cb2-4b48-b4dd-27fe3253f7a8/resource)

*图1：热流型差示扫描量热仪（HF-DSC）结构与热流路径示意图，标注样品、参比单元的热流传输路径和各节点温度参数[[S31]]。*

### 功率补偿型 DSC

功率补偿型 DSC 将试样和参比物分别放置在两组独立控制的低质量微小型加热炉内，系统始终维持试样与参比物处于热零位状态，直接测量供给二者的功率差得到热流值，无需额外的热流换算方程[[S13,S8]]。其热量平衡方程为：

\[
z_s \cdot \Gamma_s \cdot \frac{dq_s}{dt} + \left(1 + \Gamma_s \cdot \frac{dz_s}{dt}\right)q_s = m_s \cdot \frac{dT_p}{dt} \cdot \Gamma_s
\]

![功率补偿DSC单元结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcd20f39-9a54-44c4-b282-22a9b56939bf/resource)

*图2：功率补偿差示扫描量热仪（PC-DSC）结构示意图，展示参比池、铂热敏电阻温度传感元件、独立控温加热电阻及热流路径[[S54]]。*

## 与差热分析（DTA）的关系

### DTA 定义

差热分析（DTA）是在程序控温条件下，测量试样与惰性参比物之间的温度差随温度/时间变化的热分析技术。试样发生的任何物理化学变化产生的吸/放热效应，都会导致其与参比物之间产生温差信号 \(\Delta T = T_s - T_r\)[[S56,S5]]。商用 DTA 的温度上限可达 1500°C，远高于常规商用 DSC 的温度范围[[S5,S27]]。

### 核心区别

| 对比维度 | DSC | DTA |
|---------|-----|-----|
| 直接测量量 | 进出试样的热流/供给功率差 | 试样与参比物的温差 ΔT |
| 输出数据类型 | 可直接输出定量热焓数据 | 经校正后获得半定量热数据 |
| 基线稳定性 | 更优，基线漂移小 | 存在基线漂移问题 |
| 商用测温上限 | 一般不显著高于铝的熔点（约660°C） | 可达1500°C |
| 样品位置 | 热电偶置于坩埚外侧 | 热电偶直接浸没于试样中 |

> 来源：[[S27,S5,S35,S11]]

### 技术关联

DSC 与 DTA 同属于经典热分析技术，均可通过 Borchardt-Daniels 动力学模型近似计算相变转化率。二者商用化产品均在 20 世纪 50 年代末推出，现代系统均通过集成计算机大幅提升了数据重现性与基线稳定性[[S5,S11]]。

## 设备组成与样品制备

### 典型设备结构

DSC 设备通常包括以下核心单元[[S27,S35]]：
- 程序温度控制单元
- 高灵敏度低噪声差分热信号放大单元
- 数字数据采集/记录单元
- 专用气氛供给与控制单元
- 制冷模块（机械制冷/液氮制冷）

DSC 传感器的测温热电偶布置在试样坩埚外侧而非浸没入试样中，另设独立热电偶采集试样温度驱动温度轴。这种设计使得热流信号与试样温度信号可以独立、准确地获取[[S27]]。

### 样品制备要求

对于金属合金试样，DSC 标准样品制备的推荐措施如下[[S12,S17,S3]]：

- **取样质量**：常规推荐 5–15 mg（铝合金测试），部分高灵敏度热流型 DSC 可采用约 90 mg 的样品质量；
- **表面处理**：取样后需打磨去除表面氧化层并通过超声波清洗干燥；
- **热历史消除**：测试前推荐预先以规定速率升温至目标温度以上保温，随后冷却，消除加工或存储过程中的热历史影响；
- **坩埚加盖**：所有坩埚均需加盖；必要时在坩埚盖上开微孔，避免测试过程中气体膨胀顶起坩埚破坏热接触。

### 坩埚与气氛条件

**坩埚材质**：常规中低温测试（<600°C）广泛使用标准铝制坩埚；1000°C 以上的高温测试采用氧化铝陶瓷坩埚[[S3,S12]]。

**常用气氛条件**：

| 气氛类型 | 推荐流量 | 适用场景 |
|---------|---------|---------|
| 高纯氮气（N₂） | 10–50 mL/min | 常规测试 |
| 高纯氩气（Ar） | 10–50 mL/min | 高温金属测试，防止样品氧化 |
| 高纯氦气（He） | — | 深低温段测试，优化控温效果 |

> 来源：[[S17,S20,S3,S7,S23]]

## 关键实验参数

### 温度范围

| 设备类型 | 温度范围 |
|---------|---------|
| 常规商用 DSC | −50°C 至 350°C / 室温至 550°C |
| 高温型 DSC | 20°C 至 700°C 以上 |
| 液氮制冷型 DSC | 下限低至 −190°C |
| DTA 类设备 | 上限可达 1500°C |

普通商用 DSC 的上限温度通常不显著高于纯铝的熔化温度[[S35,S6,S18,S15,S14]]。

### 升温/降温速率

| 场景 | 推荐范围 |
|------|---------|
| 常规工业与科研 | 5–25 K/min |
| 高精度 Calvet 型热流 DSC | 低至 0.1 K/s |
| 专用 DSC 设备动态范围 | 0.0004 K/s 至 >1000 K/s |

> 来源：[[S2,S7,S12,S23,S34]]

### 样品质量

| 测试类型 | 推荐质量 |
|---------|---------|
| 常规铝合金测试 | 2–15 mg |
| 部分高灵敏度热流型 DSC | 约 90 mg |
| 芯片式快速扫描 DSC（DFSC） | 百微米级、厚度约 10 μm，质量远低于常规 DSC |

> 来源：[[S7,S23,S12,S3]]

### 参数对结果的影响

**升温速率**：升温速率增大时，受反应动力学控制的相变对应的 DSC 特征温度向高温方向偏移（右移），峰值高度增大、峰形变宽[[S7,S47,S48,S4,S9]]。

**降温速率**：较快降温速率下合金结晶时间缩短，原子/分子链段无法充分排列形成完整晶体，对应结晶熔融峰向低温方向偏移、峰形显著加宽[[S7,S47]]。超过设备可控降温范围时，DSC 对样品温度的控制能力逐步丧失，特定温度节点后的热流曲线出现明显人为伪差，该部分数据不可纳入后续评价[[S3,S55]]。

**样品质量**：质量过大时内部温度梯度加大，出现峰形展宽、特征温度偏移、重叠相变无法区分；质量过小时信噪比过低，测量重复性显著变差[[S11,S55]]。

## DSC 曲线的解读

### 基本要素与特征温度

DSC 曲线的典型要素包括吸热峰（谷）、放热峰、基线区域[[S22]]。特征温度确定规范如下[[S9,S47]]：

| 特征温度 | 含义 |
|---------|------|
| 外推起始温度 | 曲线偏离基线的起始点与相变峰前沿切线交点对应的温度 |
| 峰值温度 | 峰最高点对应的温度，代表反应速率达到最大值的温度 |
| 终止温度 | 相变过程结束，曲线回到基线位置对应的温度 |

### 吸热峰与放热峰的物理意义

**吸热峰**对应样品从外界吸收热量的过程，典型包括：材料熔化、第二相/析出相溶解、玻璃化转变、晶型转变等。在压铸铝合金的升温曲线中，吸热峰通常对应共晶相熔融、α-Al 基体相熔融、亚稳相溶解等过程[[S27,S51,S39,S49]]。

**放热峰**对应样品向外界释放热量的过程，典型包括：凝固冷却结晶、固态相变、相析出、晶化、时效析出相形成等。在压铸铝合金的降温曲线中，放热峰通常对应 α(Al) 相凝固、共晶相凝固、GP 区/亚稳相析出等过程[[S27,S51,S60,S39]]。

### 基线校正

DSC 基线校正的标准方法包括[[S38,S42,S59]]：

1. **空白基线法**：使用空置的样品和参比坩埚在完全相同温度程序下测试获得空白基线并扣除；
2. **无反应区间外推**：在无热效应反应区间外推基线；
3. **零级曲率多项式拟合**：对残余零级曲率进行三阶多项式拟合校正；
4. **多次重复扫描/过时效参比扫描**：进一步提升校正精度。

## 铸态 Al-Cu-Fe 准晶 DSC 案例

> 本案例以成分为 Al₆₃Cu₂₅Fe₁₂ 的 1# 铁模铸态准晶试样为研究对象，数据来源均来自权威实验文献[[S65,S10]]。

### 20°C/min 升温——四个吸热峰

在 20°C/min 升温速率条件下，DSC 曲线呈现 4 个可明确区分的吸热峰：

| 峰序 | 峰值温度 | 对应相 | 相变类型 |
|------|---------|--------|---------|
| 第1峰 | 636.2°C | τ 相（富铜相） | 熔化 |
| 第2峰 | 878.0°C | I 相（二十面体准晶） | 熔化 |
| 第3峰 | 976.3°C | β 相（富铜相） | 熔化 |
| 第4峰 | 1025.4°C | λ 相（富铁相） | 熔化 |
| 熔点 | 1066.9°C | 试样整体 | 开始熔化 |

由 Al-Cu-Fe 相图可知，各相的熔点按 λ→β→I→τ 顺序依次降低，DSC 实验数据与此完全吻合[[S65,S10]]。

![铸态Al₆₃Cu₂₅Fe₁₂准晶20℃/min升温DSC曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9717538-3e50-4ce4-a84b-784315efead8/resource)

*图3：1#铁模铸态Al₆₃Cu₂₅Fe₁₂准晶试样以20°C/min升温的DSC热分析曲线，清晰展示4个吸热峰及试样完全熔化温度1066.9°C[[S61]]。*

### 不同冷却速率下的降温析出行为

从 1200°C 降温时，DSC 的析出相序列受冷却速率显著影响[[S65]]：

| 降温速率 | 放热峰数量 | 相析出顺序 |
|---------|-----------|-----------|
| 20°C/min | 3 个 | 998.0°C 先析出 λ 相 → 961.7°C 析出 β 相 → 834.7°C 发生包晶反应 L+λ→I 生成准晶 I 相，反应完成后无 τ 相 |
| 50°C/min | 2 个 | λ 相被抑制，仅准晶 I 相和 β 相依次析出 |

> **结论**：提高冷速可有效减少 Al-Cu-Fe 准晶材料中的相组成，提升准晶 I 相的占比[[S65]]。

### 快速凝固（甩带）准晶

当冷速达到 10⁵–10⁶ K/s 的快速凝固甩带试样，DSC 升温曲线仅出现 2 个吸热峰：872.2°C 对应准晶 I 相熔化峰，988.2°C 对应 β 相熔化峰，试样中已不含 τ 相和 λ 相。该结果与 XRD 表征的两相组成完全匹配[[S63]]。

## 在压铸领域的应用场景

### 合金凝固特性分析

DSC 可直接用于免热处理大型一体化压铸铝合金的凝固特性测定。以 Castasil 37、C611 等 Al-Si 系免热处理压铸合金为例，在 10 K/min 升/降温速率下，DSC 可准确测定共晶相熔化吸热峰、α-Al 相熔化吸热峰及对应的凝固放热峰，得到的固相线、液相线温度与 Pandat 热力学模拟结果完全吻合。测得的凝固温度区间可直接指导压铸浇注温度设定，避免冷隔、热裂等工艺缺陷[[S51]]。

### 特征相识别

DSC 可用于压铸铝合金中常见特征相的热效应判定，包括准晶 I 相、τ 相、β 相、λ 相、Mg₂Si 相、θ-Al₂Cu 相、GP 区、亚稳析出相等。通过特征吸热/放热峰的位置和面积，可对不同相的溶解/析出过程进行定性和半定量分析，是压铸铝合金相识别的低成本高效方法[[S25,S28,S40]]。

### 凝固路径推演

DSC 测试可用于半固态挤压铸造 Al-Si-Cu-Mg 系压铸合金的完整凝固路径推演。通过不同特征温度处的放热峰识别，可直接验证从初晶 Si→α-Al→共晶 Si→Q-Al₅Cu₂Mg₈Si₆→θ-Al₂Cu 相的全序列析出过程，并能准确表征 Mg 含量变化对合金凝固温度的影响规律[[S64]]。

### 缺陷热效应分析

DSC 可用于压铸铝合金缺陷的热效应溯源。以 6063 挤压铝合金的“黑斑”缺陷为例，通过对比无缺陷区域和黑斑区域试样的 DSC 曲线特征差异，可判定缺陷由局部快速冷却后再次升温导致的 β' 相（Mg₂Si）局域大量异常析出引发，是铝合金生产质量管控的重要手段[[S45]]。

### 纳米析出物表征

DSC 可用于纳米级析出物的热效应分析。半固态挤压铸造 Al-Si-Cu-Mg 合金的 DSC 曲线中，不同位置的放热峰可分别对应 GP 区、θ'' 相、Q' 相、θ' 相等纳米析出相的形成过程。半固态压铸工艺对应的析出峰温度显著低于重力铸造、峰面积更大，直接证明半固态工艺可显著促进纳米相析出、提升时效强化效果[[S21]]。

## 常见标准

| 标准编号 | 主要内容 | 适用范围 |
|---------|---------|---------|
| ASTM E967 | 差示扫描量热仪与热分析仪温度校准标准 | DSC/DTA 温度校准[[S33,S1]] |
| ASTM E1269 | 差示扫描量热法测定比热容 | 金属材料等（如 H13 模具钢）[[S32]] |
| ISO 11357-4 | 差示扫描量热法测定比热容 | 与 ASTM E1269 对等[[S33]] |
| GB/T 19466 系列 | 等同转化 ISO 11357 塑料材料 DSC 性能测定 | 玻璃化转变温度、熔融焓、结晶焓、比热容[[S41,S53]] |

## 方法的局限性

DSC 技术存在以下核心局限[[S9,S28,S60]]：

- **无法直接判定物相组成**：DSC 仅能获取不同温度下的热流差和相变焓变信息，仅依靠热效应的位置和大小无法直接判定该热效应对应的物相组成；
- **重叠热效应难以区分**：无法明确区分重叠热效应分别对应的具体相变类型；
- **必须结合其他表征手段**：为准确完成全部相变过程的物相归属判定，必须结合 XRD 物相表征、硬度/电导率测试、电子显微分析等其他技术手段进行综合解读。

---

**别名说明**：用户常将“DSC”与“差热分析”混称，但二者是不同的热分析技术。DSC（差示扫描量热法）直接测量热流/功率差并输出定量热焓数据，DTA（差热分析）直接测量温差信号并需校正后才能获得半定量结果[[S27,S5,S56]]。

## Sources
- S35: [10451127_差式扫描量热仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f5b0222-a588-4c20-9c09-c61ecb0293b5/resource) (`8f5b0222-a588-4c20-9c09-c61ecb0293b5`)
- S5: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ef79a61-549d-45ae-b5a5-8966783697c8/resource) (`0ef79a61-549d-45ae-b5a5-8966783697c8`)
- S44: [两种常用免热处理压铸铝合金的对比研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b051c966-84af-47a9-87fa-b7678414e076/resource) (`b051c966-84af-47a9-87fa-b7678414e076`)
- S43: [冷却速率对6005A、7N01和7A99铝合金组织及性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae2e3977-b935-463b-ae7e-dcefcaf3b1c9/resource) (`ae2e3977-b935-463b-ae7e-dcefcaf3b1c9`)
- S62: [一体压铸用免热处理铝合金自主研发及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb6be324-5b4d-4719-b2d0-33ec2e532fcc/resource) (`fb6be324-5b4d-4719-b2d0-33ec2e532fcc`)
- S16: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/41c73b2f-2252-4b65-9394-d876ecc300fe/resource) (`41c73b2f-2252-4b65-9394-d876ecc300fe`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/15c59022-8e49-4616-9ab1-d0c77726e32c/resource) (`15c59022-8e49-4616-9ab1-d0c77726e32c`)
- S31: [热流型差示扫描量热仪（HF-DSC）热流示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86032ab3-7cb2-4b48-b4dd-27fe3253f7a8/resource) (`86032ab3-7cb2-4b48-b4dd-27fe3253f7a8`)
- S13: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37de08f4-c48c-4249-864f-ee8b83a46bc8/resource) (`37de08f4-c48c-4249-864f-ee8b83a46bc8`)
- S54: [功率补偿差示扫描量热仪（PC-DSC）结构示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dcd20f39-9a54-44c4-b282-22a9b56939bf/resource) (`dcd20f39-9a54-44c4-b282-22a9b56939bf`)
- S56: [16991063_差示热分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e0816f3b-3fdc-40d5-9162-0a772c189e9c/resource) (`e0816f3b-3fdc-40d5-9162-0a772c189e9c`)
- S27: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bb76973-e525-4988-9e33-c212c97d10d7/resource) (`6bb76973-e525-4988-9e33-c212c97d10d7`)
- S11: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a89c5a4-33b9-47b2-8bc5-a26696e1fb34/resource) (`2a89c5a4-33b9-47b2-8bc5-a26696e1fb34`)
- S12: [铸型材质对锆基块体非晶合金性能的影响及铸造成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3799a1be-756c-4ff8-a275-de3c3e2a5ac0/resource) (`3799a1be-756c-4ff8-a275-de3c3e2a5ac0`)
- S17: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/456834b8-9094-4217-981a-619653fd6f10/resource) (`456834b8-9094-4217-981a-619653fd6f10`)
- S3: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0afcee01-a84c-4d9b-834e-973ec0ddc959/resource) (`0afcee01-a84c-4d9b-834e-973ec0ddc959`)
- S20: [A356低压铸造铝合金车轮工艺优化及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5823ce37-8a17-42ab-ab96-1ca67ee7d382/resource) (`5823ce37-8a17-42ab-ab96-1ca67ee7d382`)
- S7: [纤维增强聚苯硫醚复合材料的制备及多尺度性能分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12dda3a3-8fa7-4858-aba4-2de5b1a67ce9/resource) (`12dda3a3-8fa7-4858-aba4-2de5b1a67ce9`)
- S23: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c4c77fd-83cb-4c5e-9628-3cce43a94170/resource) (`5c4c77fd-83cb-4c5e-9628-3cce43a94170`)
- S6: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0f8a07f2-f259-4126-bafc-43c7a3941e6e/resource) (`0f8a07f2-f259-4126-bafc-43c7a3941e6e`)
- S18: [adhesive bonding of aluminum alloys__3de44d7277](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53e23cc9-7544-45b2-822d-4e6993638b6d/resource) (`53e23cc9-7544-45b2-822d-4e6993638b6d`)
- S15: [图2-7 DSC 404 F3 Pegasus高温型差示扫描量热仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/398c34eb-14a9-4d95-9b9c-3326cd0ef160/resource) (`398c34eb-14a9-4d95-9b9c-3326cd0ef160`)
- S14: [差式扫描量热仪（DSC）基本信息表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3940765c-c280-44bb-b145-2f38c358cde5/resource) (`3940765c-c280-44bb-b145-2f38c358cde5`)
- S2: [甘油含量对加热卷烟热转化行为与气溶胶传热特性影响的实验及模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/045a1147-9a29-4953-bbc1-ecb1a0848d45/resource) (`045a1147-9a29-4953-bbc1-ecb1a0848d45`)
- S34: [不同DSC设备的测量原理、冷却速率范围及样品尺寸对比表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e5e09f6-9a1c-4c53-9d52-7931cee18621/resource) (`8e5e09f6-9a1c-4c53-9d52-7931cee18621`)
- S47: [铸型材质对锆基块体非晶合金性能的影响及铸造成形研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7ae8114-f3ab-4273-a701-1eb6777d00e8/resource) (`b7ae8114-f3ab-4273-a701-1eb6777d00e8`)
- S48: [图3.2 铝-煅烧高岭土混合粉末在不同加热速率（15、20、25、30℃/min）下的DSC曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c3017012-180e-49ea-859f-b4e811c5136e/resource) (`c3017012-180e-49ea-859f-b4e811c5136e`)
- S4: [图3.25 E51/DDM树脂体系DSC曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e029aa0-bd96-4dbc-8c1f-f2a67857a5a8/resource) (`0e029aa0-bd96-4dbc-8c1f-f2a67857a5a8`)
- S9: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1614f23a-20a7-4d82-bf97-a3056cf45261/resource) (`1614f23a-20a7-4d82-bf97-a3056cf45261`)
- S55: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de961f05-9099-4753-89ce-687a13820a62/resource) (`de961f05-9099-4753-89ce-687a13820a62`)
- S22: [图11 典型的DSC热分析色谱图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5a4d62e7-3fbb-4673-9db6-2aac5b6d1499/resource) (`5a4d62e7-3fbb-4673-9db6-2aac5b6d1499`)
- S51: [两种常用免热处理压铸铝合金的对比研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc09f6ef-ddff-4d18-9c30-46956a4b3dc2/resource) (`cc09f6ef-ddff-4d18-9c30-46956a4b3dc2`)
- S39: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99d23920-cf3f-4bb5-ab30-2c1168aefe60/resource) (`99d23920-cf3f-4bb5-ab30-2c1168aefe60`)
- S49: [Zn对金属型铸造Al-Mg-Si-Cu合金组织和力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c487e7ed-e47c-4194-aac4-6f42bec66cd1/resource) (`c487e7ed-e47c-4194-aac4-6f42bec66cd1`)
- S60: [钛铝基金属间化合物](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6b08933-208a-4af1-b1f0-878aa0ed1d4b/resource) (`f6b08933-208a-4af1-b1f0-878aa0ed1d4b`)
- S38: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94c9887f-a6c5-4042-9dce-64fba4664aee/resource) (`94c9887f-a6c5-4042-9dce-64fba4664aee`)
- S42: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad3ddbe3-6834-433f-a4dd-ecd3fe5d679f/resource) (`ad3ddbe3-6834-433f-a4dd-ecd3fe5d679f`)
- S59: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3d01b5e-7a4f-4d05-bffc-580e378fdcc8/resource) (`f3d01b5e-7a4f-4d05-bffc-580e378fdcc8`)
- S65: [Al-Cu-Fe三元准晶的制备及其热物理性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff82e8e6-bba0-453f-908a-cf5a1b3ae092/resource) (`ff82e8e6-bba0-453f-908a-cf5a1b3ae092`)
- S10: [Al-Cu-Fe三元准晶的制备及其热物理性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25973a42-6c5e-4a32-9f13-51b0b550b07e/resource) (`25973a42-6c5e-4a32-9f13-51b0b550b07e`)
- S61: [图3.5 铸态试样的DSC热分析曲线（升温）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9717538-3e50-4ce4-a84b-784315efead8/resource) (`f9717538-3e50-4ce4-a84b-784315efead8`)
- S63: [Al-Cu-Fe三元准晶的制备及其热物理性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd62bd73-d686-43dd-9459-cc4460088a53/resource) (`fd62bd73-d686-43dd-9459-cc4460088a53`)
- S25: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/639994be-f45c-4b53-919a-5b89382cac5d/resource) (`639994be-f45c-4b53-919a-5b89382cac5d`)
- S28: [Al-Mg-Si 和 Al-Si-Mg 合金 DSC 曲线峰值与析出/溶解反应对应关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71c85972-b233-4369-b18f-886d94f71598/resource) (`71c85972-b233-4369-b18f-886d94f71598`)
- S40: [汽车零部件用高强半固态铝合金的成分设计及工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9aaa5c83-378b-4c91-8a20-d58e2a027c6a/resource) (`9aaa5c83-378b-4c91-8a20-d58e2a027c6a`)
- S64: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fee44ca5-bb66-4ed1-b406-3972ad30f148/resource) (`fee44ca5-bb66-4ed1-b406-3972ad30f148`)
- S45: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b067ebd3-1726-4dd1-9cac-d14e269b3ca0/resource) (`b067ebd3-1726-4dd1-9cac-d14e269b3ca0`)
- S21: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/596cd4c3-043d-4449-8a7f-3fa39b5dc9a6/resource) (`596cd4c3-043d-4449-8a7f-3fa39b5dc9a6`)
- S33: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89e014b0-8c7b-49c1-9cd9-1c45ec0ab23a/resource) (`89e014b0-8c7b-49c1-9cd9-1c45ec0ab23a`)
- S1: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/003604b0-5ba5-4973-ad30-a5bc98049281/resource) (`003604b0-5ba5-4973-ad30-a5bc98049281`)
- S32: [图2-13 DSC 404C型差示扫描量热仪](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8666cf8c-c1f0-4900-8734-9668f9c00be1/resource) (`8666cf8c-c1f0-4900-8734-9668f9c00be1`)
- S41: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d10f5a2-fd21-4132-8ac5-5709d8211d9c/resource) (`9d10f5a2-fd21-4132-8ac5-5709d8211d9c`)
- S53: [熔模铸造手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d460ecfc-2ce3-4193-91c0-ef576259c999/resource) (`d460ecfc-2ce3-4193-91c0-ef576259c999`)