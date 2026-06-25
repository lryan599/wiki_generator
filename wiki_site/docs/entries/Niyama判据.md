---
version: "v1"
generated_at: "2026-06-18T11:40:39+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 21
  source_quality_score: 0.83
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

## 概述

**Niyama判据**（又称Niyama准则、Niyama缩松判据、新山判据）是由日本学者新山英辅（Eiji Niyama）等人于1982年首次提出的一种预测铸件凝固过程中产生缩松缺陷的经验判据。该判据最早发表在文献《A method of shrinkage prediction and its application to steel casting practice》中，通过对比3种尺寸、5种材质铸钢件的缩松缩孔分布数据完成验证[[S1,S9,S12,S13]]。国内权威铸造专业典籍《中国材料工程大典 第19卷 材料铸造成形工程（下）》将其正式定名为**新山英辅（Niyama）缩松判据**，是目前铸造行业通用的正式命名[[S15,S16]]。

Niyama判据是目前铸造缺陷预测领域应用最广泛的判据之一，是主流铸造CAE软件（如ProCAST、MAGMA、AnyCasting、FTSolver等）缩松预测模块的核心开发基础[[S9,S13]]。

## 定义与公式

### 经典表达式

Niyama判据的标准数学表达式为[[S13,S21]]：

\[
N_y = \frac{G}{\sqrt{R}}
\]

式中：
- \( N_y \) — Niyama判据值；
- \( G \) — 计算区域的局部温度梯度，定义为三维温度梯度矢量的模，通过该单元与周围26个相邻单元的温度梯度最大值求解[[S15,S21]]；
- \( R \) — 冷却速度（凝固速率），由液相线温度与固相线温度的差值除以对应时间间隔计算[[S15,S21]]。

### 常用单位

Niyama判据的常用单位组合为：G取°C/cm、R取°C/min，对应判据单位为 \( \mathrm{°C^{1/2} \cdot min^{1/2} \cdot cm^{-1}} \) [[S4,S26]]。

### 判定准则

当判据值小于某一临界值 \( C_{\text{Niyama}} \) 时，对应区域易产生缩松缺陷，即[[S4,S5,S16]]：

\[
\frac{G}{\sqrt{R}} < C_{\text{Niyama}}
\]

### 评估温度

Niyama判据的数值在凝固接近结束时进行评估，对应计算温度为 \( T_{Ny} = T_{sol} + 0.1 \times (T_{liq} - T_{sol}) \)，即比100%固相温度高出凝固总区间10%的温度节点，主流铸造模拟软件默认计算对应的固相分率为0.9[[S4,S7]]。

## 物理本质与作用机理

Niyama判据的物理意义源于对凝固过程中枝晶间补缩难易程度的评估。其原始推导假设液态金属沿枝晶网格的流动符合Darcy渗流定律[[S19]]。随着凝固进程推进，枝晶骨架占比不断提升，糊状区渗透率持续下降。当\( N_y \)值低于对应材料的临界值时，枝晶间补缩通道近乎被完全阻塞，剩余液态金属无法及时补充凝固收缩，进而诱发显微缩松[[S3,S15]]。

## 临界值与合金依存性

### 经典临界值

一般铸钢件的Niyama判据临界值范围为 \( 0.8 \sim 1.1 \; \mathrm{(°C \cdot min)^{1/2} / cm} \)，其中小型铸钢件临界值约0.8，大型铸钢件临界值约1.1[[S4,S15,S26]]。对于铸钢件，当 \( N_y < 1.1 \; \mathrm{°C^{1/2} \cdot min^{1/2} \cdot cm^{-1}} \) 时，铸件将出现缩松缩孔缺陷[[S13]]。

### 不同合金的临界值

| 合金类型 | 临界值 | 单位 | 备注 | 来源 |
|----------|--------|------|------|------|
| 铸钢（通用） | 0.8 ~ 1.1 | \( \mathrm{(°C \cdot min)^{1/2} / cm} \) | 小件取0.8，大件取1.1 | [[S4,S15]] |
| 铸钢（经典） | < 1.1 | \( \mathrm{°C^{1/2} \cdot min^{1/2} \cdot cm^{-1}} \) | 低于此值产生缺陷 | [[S13]] |
| M30C、M35-1奥氏体不锈钢 | 1.0 | \( \mathrm{(°C \cdot s)^{1/2} / mm} \) | — | [[S4]] |
| 通用铝合金 | 1.0 | \( \mathrm{(°C \cdot min)^{1/2} / cm} \) | 西安工业大学团队验证 | [[S4]] |
| ZL205A铝合金（砂型低压铸造） | 2 | \( \mathrm{(K \cdot s)^{1/2} / cm} \) | Ny < 2存在缩松倾向 | [[S25]] |
| Ti-Al合金 | 2.0 | \( \mathrm{(°C \cdot min)^{1/2} / cm} \) | 低于2易出现宏观缩孔，高于4无缩松 | [[S4]] |

## 在铸造缺陷预测体系中的定位

Niyama判据属于针对**枝晶间显微缩松**的专用预测判据，与等温曲线法、温度梯度法、POROS判据等同属凝固缺陷预测类判据[[S9,S16]]。它与宏观缩孔判据存在明确差异：

- **Niyama判据**：核心功能是预测枝晶间显微缩松的倾向性，仅判定低于临界值的区域易产生分散型细小显微缩松，不适用于判定集中型宏观缩孔的位置和尺寸[[S6]]；
- **宏观缩孔判据**（如POROS判据、残余熔体模数法）：针对孤立大体积金属液补充不足的场景，可预测体积较大的集中型宏观缩孔[[S6]]。

![图4-22 铸件缺陷预测情况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89c59049-71a7-497b-bf4a-734b6f2f15dc/resource)

图4-22展示了304不锈钢阀体铸件中POROS宏观缩孔判据（左）与Niyama显微缩松判据（右）的对比预测结果，二者结合可区分不同尺度的缩缺陷分布[[S17]]。

## 修正与扩展形式

经典Niyama判据属于经验公式，无明确的物理量纲意义，未将合金成分、枝晶形貌、流动阻力等参数纳入计算体系[[S5,S13,S15]]。后续学者提出了多种修正形式以提升预测精度和适用范围。

### 无量纲Niyama判据（Carlson & Beckermann）

Carlson与Beckermann于2010年提出的无量纲Niyama判据是目前工业领域应用最广泛的修正形式，其表达式为[[S13]]：

\[
N_y^* = \frac{G \lambda_2 \sqrt{\Delta P_{cr}}}{\sqrt{\mu_1 \beta \Delta T_f R}}
\]

式中引入二次枝晶间距 \( \lambda_2 \)、微孔形核临界压降 \( \Delta P_{cr} \)、液态金属黏度 \( \mu_1 \)、合金总凝固收缩率 \( \beta \)、结晶温度区间 \( \Delta T_f \) 等材料属性参数。该判据对WCB铸钢、普通铝合金、AZ91D镁合金均具备良好适配性，可精准预测薄壁铸件的显微缩松程度，已被ProCAST等主流铸造仿真软件集成支持[[S13,S23]]。

### 其他修正形式

| 修正形式 | 表达式 | 特点 | 来源 |
|----------|--------|------|------|
| 贾宝仟枝晶形态修正判据 | \( G/\sqrt{R} < A\sqrt{\Delta T}/\sqrt{D_L} \) | 引入枝晶形态修正系数A、液固温差ΔT、溶质扩散系数\( D_L \) | [[S15]] |
| 宽凝固区间铝合金修正判据（易杰） | \( Niyama = G \cdot t_f^{2/3} / v_s \) | 引入总凝固时间\( t_f \)、固液界面移动速度\( v_s \)，优于原始判据 | [[S3]] |
| 铸件几何形态修正判据 | \( G \cdot R^{-1/4} \cdot U^{-1/2} \) | 引入Darcy定律补缩流速U，区分棒/板状截面差异 | [[S3]] |

## 适用范围与局限性

### 适用场景

- **砂型铸造**：铸钢、常规铝合金可直接采用经典临界值0.8~1.1、1.0[[S24]]；
- **熔模精密铸造**：不锈钢、高温合金适配经典临界值1.0~1.1[[S24]]；
- **金属型铸造**：铝/镁合金凝固速度更快，临界值需适当高于同合金砂型铸造阈值[[S24]]。

### 局限性

1. **仅评估枝晶间补缩难度**：无法预测孤立液相区生成的宏观缩孔、充裹气诱发的气孔等非补缩不足导致的孔隙缺陷[[S19,S23]]；
2. **对强韧材料预测最佳**：对热强性较好的铸钢在冷型中凝固的场景预测精度最高；对热型壳中的铸钢、冷型中具有显著固相塑性塌陷补缩的轻质合金场景预测结果偏高[[S19,S23]]；
3. **未考虑熔体处理影响**：无法反映熔体氧化物含量等重要因素的影响[[S23]]；
4. **高压压铸（HPDC）不通用**：高压压铸存在极端高冷却速率（可达1000°C/s）、高压强制补缩作用，以及大量由卷气而非补缩不足诱发的孔隙缺陷，经典Niyama判据未引入压力场变量，临界值难以标定，预测精度不足。行业共识推荐采用考虑Darcy定律和高压影响的改进判据来适配高压压铸的缩松预测需求[[S2,S11,S24]]。

## 可视化示例

ProCAST软件输出的铝合金涡轮蜗壳Niyama判据分布模拟结果，使用单位为 \( \mathrm{(K \cdot s)^{0.5} / cm} \)，蓝色区域标识Niyama低值区即缩松高风险区域[[S29]]。

![图4.11 Niyama判据模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe9f6efa-42a9-426c-8776-7eedaa1f017f/resource)

## Sources
- S1: [0004_724a991557565b32_Metal_casting_simulation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/086031e2-612e-45cc-a951-4358bef6c283/resource) (`086031e2-612e-45cc-a951-4358bef6c283`)
- S9: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e6b25e5-2ec8-44bb-8de0-ac2f3c8d1897/resource) (`3e6b25e5-2ec8-44bb-8de0-ac2f3c8d1897`)
- S12: [电磁补缩冷芯锭凝固过程研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ad3e12a-c529-451c-928e-efe1adfb1fe0/resource) (`4ad3e12a-c529-451c-928e-efe1adfb1fe0`)
- S13: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5df1ce83-b1f8-4b76-973f-8bf35956e5c3/resource) (`5df1ce83-b1f8-4b76-973f-8bf35956e5c3`)
- S15: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/85ffad9d-31ed-4438-8d39-d3a5b2585a4d/resource) (`85ffad9d-31ed-4438-8d39-d3a5b2585a4d`)
- S16: [基于选区激光烧结的阀体快速铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8921bf99-5e16-4a75-92ff-369738f9746b/resource) (`8921bf99-5e16-4a75-92ff-369738f9746b`)
- S21: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b02daf63-fe34-4548-b485-52a32700df8a/resource) (`b02daf63-fe34-4548-b485-52a32700df8a`)
- S4: [K4648镍基高温合金异型结构件铸造过程数值模拟及实验研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27ab5300-69c1-435a-87c2-caca8ea8d2d3/resource) (`27ab5300-69c1-435a-87c2-caca8ea8d2d3`)
- S26: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5d2af19-8dda-4d66-a5d4-4dd2fa8ee8e8/resource) (`d5d2af19-8dda-4d66-a5d4-4dd2fa8ee8e8`)
- S5: [基于数值模拟的转子盘熔模铸造工艺的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2942f2b3-80f7-4219-895e-1243ef1d6444/resource) (`2942f2b3-80f7-4219-895e-1243ef1d6444`)
- S7: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39ff805a-ae97-4482-9719-8ad91144fe1e/resource) (`39ff805a-ae97-4482-9719-8ad91144fe1e`)
- S19: [castings principles the new metallurgy of cast metals__9ac1d4f9a8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a5244ff7-8021-4f23-a2c3-caed6dbe3c00/resource) (`a5244ff7-8021-4f23-a2c3-caed6dbe3c00`)
- S3: [A356铝合金重力铸造微观缺陷研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20a7c2b8-7745-4ffc-a270-6744b459274b/resource) (`20a7c2b8-7745-4ffc-a270-6744b459274b`)
- S25: [板形铸件完全凝固时的Niyama数值分布，含底注式（a-e）与低压铸造式（f-j）工艺，对应壁厚10-40mm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4034f5b-5e71-440b-bca8-8eda1c6104bd/resource) (`d4034f5b-5e71-440b-bca8-8eda1c6104bd`)
- S6: [低压铸铝件缩孔缺陷数值模拟与工艺改进](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3765979d-d84d-4c44-9162-2d82be5f2628/resource) (`3765979d-d84d-4c44-9162-2d82be5f2628`)
- S17: [图4-22 铸件缺陷预测情况](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89c59049-71a7-497b-bf4a-734b6f2f15dc/resource) (`89c59049-71a7-497b-bf4a-734b6f2f15dc`)
- S23: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb169579-ae86-47e8-9f5e-bc405747ca88/resource) (`bb169579-ae86-47e8-9f5e-bc405747ca88`)
- S24: [复杂薄壁不锈钢轴承座熔模铸造仿真优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc718c93-15da-476e-9f79-14025f396aca/resource) (`bc718c93-15da-476e-9f79-14025f396aca`)
- S2: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0afe2103-07d3-4fe3-ba9b-ae86ad8e95c1/resource) (`0afe2103-07d3-4fe3-ba9b-ae86ad8e95c1`)
- S11: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4687709f-d0e8-42b2-a15c-5298da553602/resource) (`4687709f-d0e8-42b2-a15c-5298da553602`)
- S29: [图4.11 Niyama判据模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe9f6efa-42a9-426c-8776-7eedaa1f017f/resource) (`fe9f6efa-42a9-426c-8776-7eedaa1f017f`)