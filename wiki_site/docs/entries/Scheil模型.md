---
version: "v1"
generated_at: "2026-06-18T17:20:58+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 20
  source_quality_score: 0.81
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

## 概述

Scheil模型（Scheil model，又称Scheil-Gulliver模型、谢尔模型、非平衡杠杆模型）是描述合金非平衡凝固过程中溶质再分配规律的经典微观偏析预测模型[[S11,S13,S10]]。该模型由G.H. Gulliver于1913年和E. Scheil于1942年独立提出，用于在非平衡条件下计算凝固路径、获取热物性参数及预测析出相，是铸造过程数值模拟的基础模型之一[[S11,S13]]。在压铸工艺数值仿真中，Scheil模型是ProCAST、Thermo-Calc、Pandat、MAGMASOFT等主流软件内置的标准凝固路径计算模块[[S9,S19,S22,S15,S17]]。

## 基本假设

Scheil模型建立在四个核心假设之上[[S11]]：

1. **固相无扩散**：凝固完成后已生成的固相内部溶质完全不发生迁移，凝固过程中不同时刻析出的固相成分被完全保留，最终沿枝晶径向形成梯度分布的溶质浓度带[[S13,S11,S7]]。

2. **液相完全混合**：液相区域溶质依靠高扩散系数、热对流、Marangoni对流实现无限快的均匀化，任意时刻剩余液相整体浓度完全一致[[S11,S13]]。

3. **固/液界面局部平衡**：凝固推进过程中固/液两相界面位置始终满足相图给出的热力学平衡条件，界面两侧溶质浓度比严格等于平衡分配系数k[[S11,S7]]。

4. **固相线与液相线为直线段**：早期经典模型额外假设固相线与液相线为直线。在使用CALPHAD等数值热力学软件计算时，该条件可放宽，但这些计算依赖相图计算获得的平衡相图，可能出现逆行溶解度等奇点，影响Scheil计算结果[[S11,S2]]。

## 数学表达

基于溶质守恒推导得到的Scheil-Gulliver方程，其推导核心是利用固/液界面处排出的溶质量与液相中溶质增量之间的质量平衡关系[[S2]]。

**液相溶质浓度表达式**[[S2,S13,S10]]：

$$
C_L = C_0 \cdot f_L^{\;(k-1)}
$$

**固相溶质浓度表达式**[[S2,S8]]：

$$
C_S = k C_0 (1 - f_S)^{(k-1)}
$$

其中：
- \( k \) — 固/液界面溶质平衡分配系数（由相图确定，\( k = C_S / C_L \)）
- \( C_0 \) — 合金初始名义成分
- \( f_S \) — 固相质量分数
- \( f_L = 1 - f_S \) — 剩余液相质量分数

当 \( f_S = 0 \) 时，边界条件为 \( C_L = C_0 \)；对该微分质量平衡式积分即得上述标准形式[[S2]]。该方程亦被称为“非平衡凝固时的杠杆定律”[[S10]]。

## 物理意义

### 微观偏析形成机制

Scheil模型的预测结果表明，相比平衡凝固过程，非平衡条件下剩余液相中溶质富集程度更高。由于固相无扩散，已凝固固相内部成分不均匀，其平均成分 \( \overline{C}_S \) 始终低于界面处平衡成分 \( C_S^\* \)，导致剩余液相数量必然大于平衡结晶时的相应数量[[S10]]。

### 共晶形成倾向

凝固温度降至平衡固相线时仍残留大量富溶质液相，最终在更低的共晶温度下完成全部凝固，生成占比更高的共晶组织[[S10]]。Scheil方程只适用于 \( C_S^\* \) 达到最大固溶度 \( C_{SM} \) 之前；此后体系发生共晶转变，该方程不再适用[[S10]]。

### 枝晶成分分布

枝晶臂区域的溶质浓度沿生长方向呈梯度分布，形成典型的枝晶微观偏析：枝晶心部溶质含量低（先凝固），枝晶间区域溶质含量高（后凝固）[[S7,S8,S20]]。

![基于Scheil方程的微观偏析形成原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44292d73-e244-4345-8f58-1c5a43233f93/resource)

此图完整展示Scheil模型描述的微观偏析形成过程：子图(a)为一次柱状晶臂横截面的等浓度线分布，子图(b)为相图中标注的凝固路径，子图(c)为沿枝晶径向测量的浓度曲线，直观呈现了溶质从枝晶心部到枝晶间区域的梯度富集特征[[S7]]。

## 与平衡凝固（杠杆定律）的对比

平衡凝固杠杆定律假设固相和液相中溶质均完全扩散，凝固完成后得到成分完全均匀的单相固溶体；Scheil模型则得到存在显著成分梯度的非均匀组织[[S6,S3,S23]]。

| 对比维度 | Scheil模型 | 平衡杠杆定律（Lever rule） |
|---------|-----------|------------------------|
| 固相扩散假设 | 无扩散 (\( D_S = 0 \)) | 完全扩散 (\( D_S = \infty \)) |
| 液相扩散假设 | 完全混合 (\( D_L = \infty \)) | 完全混合 (\( D_L = \infty \)) |
| 最终组织 | 成分梯度分布的非均匀组织 | 成分完全均匀的单相固溶体 |
| 非平衡固相线温度 | 显著低于平衡固相线，接近共晶温度 | 位于平衡固相线 |
| 共晶相生成量 | 显著偏高 | 与相图一致 |
| 适用场景 | 高合金快速非平衡凝固 | 低合金常规平衡凝固 |

Scheil预测的非平衡固相线温度显著低于平衡固相线，完全凝固点接近共晶温度。低合金常规平衡场景优先采用杠杆定律计算，高合金快速非平衡凝固场景优先采用Scheil模型计算[[S6,S3,S23]]。

![Al-17Si-4Cu-2.5Mg合金的平衡与非平衡凝固路径对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd07453e-66dc-4ee1-987f-7e4b57c732fc/resource)

该图对比了Al-17Si-4Cu-2.5Mg过共晶压铸铝合金在平衡杠杆定律（Lever rule）与Scheil模型下的凝固路径，横轴为固相分数、纵轴为温度，标注了四个凝固阶段及各阶段析出相的体积分数，直观呈现了非平衡凝固条件下固相线温度向下偏移和共晶相生成比例明显提升的特性[[S20]]。

## 在压铸工艺中的应用

### 适用性分析

Scheil模型适用于压铸工艺下冷却速率较快的非平衡凝固场景。工业压铸条件下局部凝固时间短，固相溶质扩散可近似忽略，这一基本前提使得Scheil模型能够准确预测Al-Si系、Al-Cu系等常见压铸铝合金的微观偏析溶质富集规律、共晶相生成比例及固/液相线温度区间，计算结果相比平衡杠杆规则更贴合实际压铸快速凝固的实测数据[[S4,S8,S6]]。

### 主流软件集成应用

Scheil模型已被集成到以下主流热力学计算与铸造仿真软件中：

**Thermo-Calc**：内置专门的Scheil-Gulliver计算模块，官方公开提供了332.1铸造铝合金的Scheil凝固模拟教程，支持输出完整的非平衡凝固路径、相析出顺序及共晶相生成量等计算结果[[S22,S8]]。

**Pandat**：原生支持Scheil模型计算，官方公开了Cu70Zn30合金及多组元铝合金的Scheil凝固路径计算示例，可直接输出不同固相分数下的溶质浓度和相分数数据，配合开放的TDB热力学数据库可快速完成压铸铝合金非平衡凝固仿真[[S11,S15,S22]]。

**ProCAST**：内置4种凝固路径计算模型，其中Scheil模型定位为快速非平衡凝固专用计算模块，推荐用于高合金成分体系的热物性参数计算，已在SCS13等合金的工程仿真中得到应用。ProCAST还提供Lever规则（完全扩散平衡）、Back Diffusion（有限反扩散模型）及Multiple Solidification（多相凝固路径模拟）三种补充模型[[S9,S19]]。

**MAGMASOFT**：内置基于Scheil模型的热物性参数生成模块，可将非平衡凝固计算得到的热焓及固相分数随温度变化的数据集直接耦合到充型、凝固全流程仿真中，提升压铸铝合金铸件缺陷预测精度[[S17,S14]]。

### Al-Si系合金压铸模拟实例

对于典型的Al-17Si-4Cu-2.5Mg过共晶压铸铝合金，Scheil模型可精确模拟α-Al初晶析出→初晶Si析出→多元共晶反应→终凝共晶的完整凝固路径，并给出各阶段析出相的体积分数，为压铸工艺参数优化提供关键的热物性依据[[S20]]。

## 局限性

Scheil模型存在以下核心局限：

1. **凝固末期溶质浓度发散**：当固相分数 \( f_S \) 趋近于1时，液相溶质浓度计算结果会趋于无穷大，无法准确表征凝固末期的溶质分布[[S13,S16]]。

2. **高估偏析程度**：模型完全忽略固相中的逆向扩散，得到的微观偏析程度显著高于工业常规凝固过程的实测结果[[S21,S7]]。

3. **高温扩散元素预测偏差**：针对碳等固相扩散系数高、高温区间固相传质不可忽略的合金元素，该模型预测误差明显偏大[[S6,S21]]。例如，在Cu-7Ni-7Al-4Fe-2Mn合金的热物性参数计算中，Scheil模型计算的固相线温度与DSC实测值存在偏差，原因之一即为模型忽略了非平衡凝固条件下溶质在固相中的相互作用[[S16]]。

4. **未考虑枝晶粗化**：Scheil模型未纳入凝固过程中的枝晶臂粗化效应，该效应会促进固相溶质均匀化、降低实际偏析程度[[S21,S6]]。

## 改进与变体模型

为克服Scheil模型的上述局限性，研究者陆续提出了一系列改进模型[[S6,S21]]：

### Brody-Flemings模型（1966年）

Brody与Flemings于1966年提出首个在Scheil模型基础上引入固相有限反扩散的改进微观偏析模型。该模型保留液相完全扩散假设，引入固相扩散边界层概念，并通过局部凝固时间与二次枝晶臂间距耦合定义溶质反扩散参数β，首次定量考虑了凝固过程中固相溶质的反向迁移效应[[S13,S6,S21]]。

### Clyne-Kurz模型（1981年）

Clyne与Kurz对Brody-Flemings模型进行了进一步修正，重新定义了无量纲溶质傅里叶数（反扩散参数），消除了原模型在高扩散系数场景下的数值发散问题，预测精度更高，在中间冷却速率的工业凝固场景下适用性更强[[S6,S21,S24]]。

### 后续发展

后续模型包括Kobayashi（1988年）提出的改进解析解、Yeum-Laxmanan-Poirier（1989年）的有限元方法、考虑枝晶臂粗化效应的Kirkwood（1984年）模型、Mortensen（1989年）解析模型，以及同时考虑固相和液相有限扩散的Tong-Beckermann模型等[[S21,S24]]。Voller-Beckermann模型创新性地将枝晶粗化效应与反向扩散耦合，成为现代非平衡凝固研究中应用最广泛的模型之一[[S6]]。

### 常用微观偏析模型分类汇总

| 模型名称 | 液相扩散假设 | 固相扩散假设 | 主要特点 |
|---------|------------|------------|---------|
| Lever rule（杠杆定律） | 完全扩散 | 完全扩散 | 平衡凝固理想模型 |
| Scheil模型 | 完全混合/无限扩散 | 无扩散 | 非平衡凝固经典模型 |
| Brody-Flemings模型 | 完全扩散 | 有限反扩散 | 引入固相扩散边界层与反扩散参数β |
| Clyne-Kurz模型 | 完全扩散 | 有限反扩散 | 修正反扩散参数，消除数值发散 |
| Voller-Beckermann模型 | 有限扩散 | 有限扩散 | 耦合枝晶粗化效应与反向扩散 |

以上分类基于《中国材料工程大典》第19卷"材料铸造成形工程（下）"的系统归纳[[S23]]，并补充了后续模型发展信息[[S6,S21]]。

## 小结

Scheil模型作为非平衡凝固微观偏析分析的经典理论框架，以其简洁的数学形式揭示了快速凝固条件下溶质再分配的本质规律。尽管该模型因忽略固相扩散而高估偏析程度，但其预测结果定义了非平衡凝固的偏析上界，在压铸铝合金工艺设计与铸造数值模拟中具有不可替代的基础地位。在实际应用中，通常根据合金体系特性和冷却条件选择Scheil模型、Clyne-Kurz模型或更复杂的Voller-Beckermann模型，以获得与实测数据最佳吻合的凝固路径预测结果[[S6,S21,S24]]。

## Sources
- S11: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6906ac87-0c71-4b40-8179-0e29632891e1/resource) (`6906ac87-0c71-4b40-8179-0e29632891e1`)
- S13: [钛合金TC4真空自耗熔炼铸锭质量控制基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a3c1725d-b2e4-432e-b57a-e0ef89280e85/resource) (`a3c1725d-b2e4-432e-b57a-e0ef89280e85`)
- S10: [金属液态成型原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/600ccf15-ecd7-4f9d-9964-498a1e48bee4/resource) (`600ccf15-ecd7-4f9d-9964-498a1e48bee4`)
- S9: [铜镍铝合金通海阀铸造缺陷预测及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5de1d0bc-03b1-49fd-be0c-19aaa80d8ead/resource) (`5de1d0bc-03b1-49fd-be0c-19aaa80d8ead`)
- S19: [燃汽轮机用SCS13合金锁键铸造工艺数值模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8d4b8f4-6998-49e9-91ed-bb5fa1acad44/resource) (`c8d4b8f4-6998-49e9-91ed-bb5fa1acad44`)
- S22: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d37c0b26-2565-4299-913c-4e030936fd92/resource) (`d37c0b26-2565-4299-913c-4e030936fd92`)
- S15: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0d16001-6bf2-44c6-9a48-885b3ded943e/resource) (`b0d16001-6bf2-44c6-9a48-885b3ded943e`)
- S17: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b791779c-501a-40f6-ac79-ec32772621ab/resource) (`b791779c-501a-40f6-ac79-ec32772621ab`)
- S7: [advanced physical chemistry for process metallurgy__40b302dbe5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44292d73-e244-4345-8f58-1c5a43233f93/resource) (`44292d73-e244-4345-8f58-1c5a43233f93`)
- S2: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06200254-b26c-49ab-b093-a488bf28fb91/resource) (`06200254-b26c-49ab-b093-a488bf28fb91`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4af313e5-3c4a-48db-880b-55f930a87492/resource) (`4af313e5-3c4a-48db-880b-55f930a87492`)
- S20: [图7.3 Al-17Si-4Cu-2.5Mg合金的平衡与非平衡凝固路径](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd07453e-66dc-4ee1-987f-7e4b57c732fc/resource) (`cd07453e-66dc-4ee1-987f-7e4b57c732fc`)
- S6: [低合金钢板坯与轧材均质化控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/327595db-9092-4ebc-8e62-8954f580828a/resource) (`327595db-9092-4ebc-8e62-8954f580828a`)
- S3: [铸态高强韧性板簧座铸造工艺设计及残余应力的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14223897-d64a-4236-b4dd-c2db211c4d16/resource) (`14223897-d64a-4236-b4dd-c2db211c4d16`)
- S23: [表6.5-1 常用的微观偏析计算模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d9a4df4b-4b75-4d0a-ac38-b8862b8c4d47/resource) (`d9a4df4b-4b75-4d0a-ac38-b8862b8c4d47`)
- S4: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1bf28692-e6a9-4038-b09f-ead5e04adf78/resource) (`1bf28692-e6a9-4038-b09f-ead5e04adf78`)
- S14: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6c0ddc9-3495-490b-bb55-129392d012fc/resource) (`a6c0ddc9-3495-490b-bb55-129392d012fc`)
- S16: [铜镍铝合金通海阀铸造缺陷预测及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b13ae393-8f91-400b-97e1-2e84ca03c077/resource) (`b13ae393-8f91-400b-97e1-2e84ca03c077`)
- S21: [advanced physical chemistry for process metallurgy__40b302dbe5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2acd6d8-6f62-4597-94ca-f5b814c20afa/resource) (`d2acd6d8-6f62-4597-94ca-f5b814c20afa`)
- S24: [design of alloy metals for low mass structures__b942e89304](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ea30b9b1-355d-47f7-ba61-2d42451fce31/resource) (`ea30b9b1-355d-47f7-ba61-2d42451fce31`)