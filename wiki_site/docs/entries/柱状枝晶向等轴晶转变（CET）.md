---
version: "v1"
generated_at: "2026-06-18T17:13:01+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 35
  source_quality_score: 0.84
  freshness_score: 0.87
  evidence_coverage_score: 1.0
---

## 概述

柱状晶向等轴晶转变（Columnar-to-Equiaxed Transition, CET）是金属凝固过程中决定微观组织演变的关键相变过程，指定向生长的柱状枝晶前沿区域内形核生长的等轴晶累积到临界体积分数后，阻断柱状晶定向延伸，最终凝固组织由柱状晶主导向等轴晶主导转变[[S13,S42,S47]]。该转变直接决定铸件/铸坯的中心偏析程度、热加工裂纹倾向等核心质量指标，受合金成分、过热度、冷却强度、形核密度多因素共同调控[[S47]]。

在压铸条件下，CET的调控对薄壁件的微观组织均匀性、力学性能和缺陷控制具有重要工程意义。

## 微观机制

目前主流的CET转变机理包含两类理论[[S13,S3]]：

1. **机械阻塞理论**：由Lipton等提出，认为当柱状晶前沿累积足够多的自由形核晶粒后，等轴晶与柱状晶发生竞争生长，最终柱状晶生长被机械阻滞而停止。
2. **溶质阻塞理论**：由Martorano团队证实，等轴晶生长过程中向界面前沿释放的溶质会局部消除成分过冷效应，进而抑制柱状晶的延伸并诱发CET。

## 关键影响参数

CET发生位置和转变比例受以下核心参数影响[[S47,S36]]：

- **温度梯度 \(G\)**：降低凝固前沿温度梯度，可使CET位置向靠近铸型表面区域偏移，提升等轴晶占比。
- **生长速率/界面迁移速率**：凝固前沿生长速率需处于适配区间，影响等轴晶形核与长大的竞争关系。
- **冷却速率**：适当提升冷却速率有助于细化晶粒，但过高的冷却强度会增大温度梯度，反而促进柱状晶生长。
- **合金成分**：合金中溶质元素的含量变化可改变枝晶尖端过冷度和形核驱动力，从而调控CET位置。
- **形核质点密度**：外来形核质点数量充足时，等轴晶形核密度增大，促使CET提前发生。

对Q355钢475mm特厚板坯的研究表明，过热度从11K升至46K时，CET起始位置的温度梯度\(G\)从1179.46 K·m⁻¹降至766.89 K·m⁻¹，冷却速率\(L\)从0.072329 K·s⁻¹降至0.035806 K·s⁻¹，直接量化了过热度对CET临界热参数的影响规律[[S18]]。

合金元素对CET位置亦有显著定量影响：C含量在0.13~0.20 wt.%区间内递增时，CET起始位置距坯壳表面距离从152.3mm递减至110.1mm；Mn含量在1.25~1.60 wt.%区间内递增时，该距离从160.3mm线性递减至126.1mm[[S36]]。

## 经典定量判据

### Hunt模型（1984）

Hunt J.D.于1984年建立了首个二元合金在稳态单向凝固条件下的CET定量判据[[S28,S13,S3]]。该模型基于两项核心假设：溶质元素在液相中呈稳态分布，柱状晶前沿温度梯度遵循线性变化规律。

模型通过等轴晶体积分数划分组织区间：
- 等轴晶体积分数 < 0.66%：全柱状晶组织
- 0.66%~49%：柱状晶与等轴晶共存的过渡组织
- > 49%：完全CET转变，全等轴晶组织

临界温度梯度判据表达式为：

\[
G < 0.617 \cdot N_0^{1/3} \cdot \left[ 1 - \left( \frac{\Delta T_N}{\Delta T_c} \right)^3 \right] \cdot \Delta T_c
\]

式中：\(N_0\)为形核密度（m⁻³），\(\Delta T_N\)为形核过冷度（K），\(\Delta T_c\)为枝晶尖端成分过冷度（K）[[S28]]。

后续Biscuola等针对Al-7wt%Si合金进行修正，发现该合金等轴晶体积分数达到20%时即可满足机械阻塞条件触发CET[[S3]]。

### Gäumann模型

Gäumann模型是在Hunt模型基础上面向多元合金高梯度快速凝固场景提出的简化CET解析模型[[S8,S15]]。其核心假设为：常规凝固条件下热过冷、曲率过冷及动力学过冷的数值远小于成分过冷，柱状晶与等轴晶的前沿过冷度与生长速度满足统一关系\(\Delta T = (a v)^{1/n}\)。

多元合金CET临界条件表达式为：

\[
G_T = \frac{1}{n + 1} \sqrt[3]{\frac{-4\pi}{3\ln(1-\varphi_{\text{CET}})}} N_0^{1/3} \left(1 - \frac{\Delta T_n^{n+1}}{(\alpha v)^{(n+1)/n}}\right) (a v)^{1/n}
\]

针对激光立体成形等高梯度快速凝固场景，形核过冷度可忽略，模型可简化为：

\[
\frac{G_T^n}{v} = a \left[ \sqrt[3]{\frac{-4\pi N_0}{3 \ln(1 - \varphi_{\text{CET}})}} \frac{1}{n+1} \right]^n
\]

该模型适用场景包含激光立体成形、增材制造等非平衡快速凝固场景，相比Hunt模型可预测绝对稳定性现象[[S8,S15]]。

### KGT模型

KGT（Kurz–Giovanola–Trivedi）模型由Kurz W、Giovanola B、Trivedi R于1986年提出，是快速定向凝固场景下的枝晶尖端生长动力学模型[[S40,S20]]。其枝晶尖端成分过冷度可简化为\(\Delta T_c = \Delta T_0 (a_1 \cdot V)^{1/n}\)，常作为Gäumann等高级CET判据中的枝晶尖端生长子模块使用[[S15,S40]]。

### 经验判据（厚板连铸专用）

针对475mm厚度Q355低合金钢特厚板坯连铸场景，基于凝固传热-CAFE耦合模型多工况仿真数据与工业低倍检验结果，通过线性回归推导得到CET开始位置的简化温度条件[[S14,S27]]：

\[
\frac{G^{1.47}}{L} < 482486.07
\]

该判据的决定系数\(R^2 = 0.97363\)，多方案验证偏差率较低，但仅适用于475mm规格Q355钢连铸特厚板坯的CET预测[[S14,S45]]。**现有公开文献中未检索到该判据在压铸场景下的相关应用记录**，不同压铸合金体系均有各自独立的经验CET简化判据[[S27,S48]]。

## CET对铸件性能的影响

### 宏观偏析抑制

CET提升等轴晶占比后可显著降低铸件宏观偏析程度。粗大柱状晶结构会加剧枝晶间隙溶质富集，而CET后形成的等轴晶组织可抑制心部偏析缺陷，减小带状偏析缺陷带宽度，使元素分布更加均匀[[S47,S21]]。当CET滞后、柱状晶过度延伸时，定向生长的柱状晶会推动溶质富集的液相持续向铸件中心迁移，最终在铸件心部形成连通性极强的集中型中心正偏析[[S38]]。

### 热裂倾向降低

CET调控可有效降低压铸件热裂倾向。等轴晶细化后晶界总面积增加，凝固后期残余液相补缩通道更通畅，可减少凝固收缩阶段的应力集中，降低晶界处低熔点富集相诱发热裂纹的概率[[S37,S35]]。对于镁合金压铸场景，在等轴晶占比合理范围内，热裂缺陷率可大幅下降[[S39]]。

当CET发生过晚、柱状晶区域占比过大时，铸件凝固后期晶间残留的低熔点液膜会集中分布在柱状晶交汇面，在收缩拉应力作用下热裂纹萌生概率大幅提升[[S5]]。

### 力学性能提升

CET后形成的细小等轴晶组织可显著提升压铸件力学性能：

| 合金体系 | 细化条件 | 晶粒尺寸变化 | 力学性能提升 | 来源 |
|---------|---------|-------------|-------------|------|
| Al-7Si | 1.00 wt.% Al-1Ti-3B | 220μm（柱状）→ 60μm（等轴） | 抗拉强度 +6.66%，延伸率 +37.50% | [[S34]] |
| LM6铝硅合金 | 0.50 wt.% Al5Ti1B | 粗大柱状 → 细小等轴 | 抗拉强度：76.73 MPa → 106.68 MPa（+39.00%） | [[S34]] |

### 致密性优化

CET完成后形成的均匀等轴晶组织可优化压铸件内部致密性：疏松分布更加均匀，总孔隙率从1.5%降低到0.2%，原本沿粗大晶界分布的大尺寸长条形孔洞转变为弥散分布的细小孤立孔洞[[S2]]。这降低了铸件渗漏风险，提升了密封承压能力。

## 压铸工艺中的CET调控

### 铝合金压铸

铝合金压铸CET调控的成熟工业方案包括[[S19,S33,S23]]：

- **晶粒细化处理**：向熔体中添加Al-Ti-B或Al-Ti-C中间合金作为晶粒细化剂，推荐添加量为0.5~2kg/吨铝熔体，避免TiB₂颗粒过度团聚。
- **温度参数控制**：浇注温度控制在640~700℃区间，模具预热温度控制在180~220℃范围。
- **冷却系统优化**：优化冷却水道布置均衡散热，降低凝固前沿温度梯度，促进CET向近模面位置发生，提升等轴晶占比。

### 镁合金压铸

镁合金压铸CET调控方案包括[[S31,S30,S35]]：

- **晶粒细化**：可采用碳变质处理（添加含碳化合物），或添加Ce元素作为细化剂。AZ31合金中Ce含量为0.8wt.%时，平均晶粒尺寸从约260μm细化到约25μm，显著提升等轴晶占比。
- **工艺参数范围**：浇注温度670~690℃，模具预热温度200~250℃，压射比压40~70MPa，配合适当的留模时间优化凝固过程。

### 锌合金压铸

锌合金压铸可向熔体中添加B或TiB中间合金、Zr、La、Ce元素作为变质细化剂，细化晶粒促进CET转变提升等轴晶占比，进而提高铸件的抗拉强度和伸长率[[S12]]。

## 检测与表征

### 金相组织观察

取样后经逐级打磨抛光，采用适配的侵蚀剂（如铝合金采用体积分数1.5%HF溶液腐蚀10s左右）显露晶粒边界，通过光学显微镜采集全截面组织图像，结合ImageJ等图像分析软件可定量统计CET转变位置、柱状晶区与等轴晶区面积占比等参数[[S32]]。

### EBSD分析

将试样经粗磨、多道次精抛后，采用氩离子抛光去除表面应力层，在配备EBSD模块的场发射扫描电镜下设置样品倾转70°、加速电压15~20kV、1~4μm扫描步长，采集全截面晶粒取向分布数据。通过配套软件统计不同区域晶粒取向各向异性程度，精准区分定向生长的柱状晶区域与取向随机分布的等轴晶区域，实现CET位置的定量标定[[S32]]。

### 凝固热分析

在压铸型腔内不同位置预埋K型校准热电偶，以100Hz及以上的采样频率记录凝固全程温度-时间曲线。通过对曲线做一阶、二阶微分，提取形核温度、再辉温度、枝晶相干点等特征参数，结合试样淬断后对应的金相组织，可反推不同冷却条件下CET发生的临界温度梯度和过冷度阈值[[S26,S10]]。

## CET与其他凝固缺陷的关系

### 羽毛晶

当凝固前沿温度梯度过高、CET被完全抑制时，铝合金、镁合金等压铸合金的大角度择优取向柱状晶易生成羽毛晶组织，引发材料各向异性，降低铸件横向力学性能[[S24]]。

### 中心偏析与缩松

CET滞后时，柱状晶区过度发育产生的搭桥现象及凝固收缩可导致铸件中心区域碳、磷、硫、锰等元素富集，形成中心偏析缺陷，常伴随中心裂纹和疏松[[S38]]。通过电磁搅拌、低过热度浇注等手段促进CET早期发生、增加等轴晶率，是控制中心偏析的关键措施[[S47,S21]]。

## 图示

### CET组织原理示意图

下图展示了铸坯凝固过程中CET的组织演变：左侧为定向生长的柱状晶区，右侧为随机分布的等轴晶区，标注X方向指向凝固推进方向，清晰呈现从柱状晶主导到等轴晶主导的转变特征[[S6]]。

![铸坯凝固过程中柱状晶向等轴晶转变的组织原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26547fb5-a685-4752-8e6f-b8630b5ef5df/resource)

### 稳态CET判据图

下图为经典稳态CET判据图，横轴为温度梯度对数（LOG(G)），纵轴为凝固前沿生长速率对数（LOG(V)），清晰划分出等轴晶区与柱状晶区的边界，两条曲线为两者转变边界，可辅助说明G-V参数组合与组织类型的对应关系[[S22]]。

![稳态CET模型判据图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79365c18-abb0-48c1-a2f9-e6f3e8539f89/resource)

## Sources
- S13: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4139c7c8-056b-4ca8-b86d-6423707d0fe3/resource) (`4139c7c8-056b-4ca8-b86d-6423707d0fe3`)
- S42: [同步辐射成像技术在金属材料凝固研究中的应用进展（特邀）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ece4cc76-99b8-4489-bc57-027cb637096b/resource) (`ece4cc76-99b8-4489-bc57-027cb637096b`)
- S47: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe5ed7ed-7156-4961-a1b7-776f57a9a610/resource) (`fe5ed7ed-7156-4961-a1b7-776f57a9a610`)
- S3: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1885edc4-1f6e-42d0-85e7-a2a5906e7a83/resource) (`1885edc4-1f6e-42d0-85e7-a2a5906e7a83`)
- S36: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b7633973-e2c3-4860-a304-62c058d91600/resource) (`b7633973-e2c3-4860-a304-62c058d91600`)
- S18: [表4-2 不同连铸工艺参数下的CET开始位置处的温度梯度和冷却速率](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63fadbb4-53d0-42d4-abd7-b0d7d95aec3f/resource) (`63fadbb4-53d0-42d4-abd7-b0d7d95aec3f`)
- S28: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/911a4233-a839-4830-957a-3b7334440378/resource) (`911a4233-a839-4830-957a-3b7334440378`)
- S8: [激光立体成形 高性能致密金属零件的快速自由成形](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e57261f-0eb8-452c-996f-592de6599bc4/resource) (`2e57261f-0eb8-452c-996f-592de6599bc4`)
- S15: [激光立体成形 高性能致密金属零件的快速自由成形](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e92056c-a86b-4db1-8bac-f2ba82e3c79c/resource) (`4e92056c-a86b-4db1-8bac-f2ba82e3c79c`)
- S40: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d91ae7bf-4484-418a-bf2b-ca1ffd7a536b/resource) (`d91ae7bf-4484-418a-bf2b-ca1ffd7a536b`)
- S20: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fa4a609-0599-4bd8-879b-fe308ac04f26/resource) (`6fa4a609-0599-4bd8-879b-fe308ac04f26`)
- S14: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ac987ee-f5c9-413f-bc4c-3e2a072005dd/resource) (`4ac987ee-f5c9-413f-bc4c-3e2a072005dd`)
- S27: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90c47766-db4f-4a9a-8879-a6a543954723/resource) (`90c47766-db4f-4a9a-8879-a6a543954723`)
- S45: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f37f5b96-cc7e-4a71-83b4-8c38fe4ef5f3/resource) (`f37f5b96-cc7e-4a71-83b4-8c38fe4ef5f3`)
- S48: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fedb2862-48fe-4d15-a13e-f125a7921181/resource) (`fedb2862-48fe-4d15-a13e-f125a7921181`)
- S21: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/722f15c6-b9aa-40d0-a0bd-e1543663f18a/resource) (`722f15c6-b9aa-40d0-a0bd-e1543663f18a`)
- S38: [3158108_中心偏析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce9d11e5-47cd-4361-b786-6504ad2a8570/resource) (`ce9d11e5-47cd-4361-b786-6504ad2a8570`)
- S37: [aluminium cast house technology xi selected peer reviewed papers from th__bcb2213732](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc4ee2a9-6f86-4d6c-8e86-aa857e51aa89/resource) (`bc4ee2a9-6f86-4d6c-8e86-aa857e51aa89`)
- S35: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b5a0f60b-8add-4017-b2af-cfe0912ff801/resource) (`b5a0f60b-8add-4017-b2af-cfe0912ff801`)
- S39: [镁合金压铸件缺陷分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d590b819-17e2-4330-aac4-639dfa21e6e2/resource) (`d590b819-17e2-4330-aac4-639dfa21e6e2`)
- S5: [ZL205A合金圆筒状包络构件低压铸造线状偏析形成机理及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/204c0b79-95ba-410c-af2d-1d3bc725a744/resource) (`204c0b79-95ba-410c-af2d-1d3bc725a744`)
- S34: [铝合金流变铸造卷入性缺陷及其钝化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af67030b-5900-44e1-902c-62d2b2d95e9c/resource) (`af67030b-5900-44e1-902c-62d2b2d95e9c`)
- S2: [变形铝合金的细化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/060587b4-66b7-42e2-9b59-a58044b59b9c/resource) (`060587b4-66b7-42e2-9b59-a58044b59b9c`)
- S19: [direct chill casting of light alloys science and technology__4b73b9fd82](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64e137f3-d50b-45de-b47b-d70b48d4c438/resource) (`64e137f3-d50b-45de-b47b-d70b48d4c438`)
- S33: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9e46e3e-91d4-4a90-9190-35167bdd9508/resource) (`a9e46e3e-91d4-4a90-9190-35167bdd9508`)
- S23: [免热处理压铸Al-Zn-Si-Cu合金微观组织与性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/80c26883-1a30-4119-a018-30a712415a6d/resource) (`80c26883-1a30-4119-a018-30a712415a6d`)
- S31: [变形镁合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9920ec16-3d7b-400b-b4a8-2607fb2755ba/resource) (`9920ec16-3d7b-400b-b4a8-2607fb2755ba`)
- S30: [镁合金压铸工艺数值模拟及缺陷带形成探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/957856b4-035c-4f6f-bf3a-66dba655678f/resource) (`957856b4-035c-4f6f-bf3a-66dba655678f`)
- S12: [压铸工艺及设备模具实用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/37edb326-5e17-41ff-8bbe-832ce9573211/resource) (`37edb326-5e17-41ff-8bbe-832ce9573211`)
- S32: [超声熔体处理和Al-Ti-B协同作用下Al-Cu合金的显微组织和力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ffcb976-16de-4060-8fdf-a7438ea7fa94/resource) (`9ffcb976-16de-4060-8fdf-a7438ea7fa94`)
- S26: [a new approach to assess the effects of sr and bi interaction in adc12 a__3057b622a1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d2740ea-eab5-41ca-aeb0-d57cc28c4b57/resource) (`8d2740ea-eab5-41ca-aeb0-d57cc28c4b57`)
- S10: [aluminium die casting alloys alloy composition microstructure and proper__bcc2285001](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31635eb9-63bb-4b54-9a94-0e6a710868f4/resource) (`31635eb9-63bb-4b54-9a94-0e6a710868f4`)
- S24: [原铝及其合金的熔铸生产问答](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81faf12d-1a61-457c-a163-a95fff828a04/resource) (`81faf12d-1a61-457c-a163-a95fff828a04`)
- S6: [铸坯凝固过程中柱状晶向等轴晶转变（CET）的组织示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26547fb5-a685-4752-8e6f-b8630b5ef5df/resource) (`26547fb5-a685-4752-8e6f-b8630b5ef5df`)
- S22: [图1-23 稳态CET模型；Fig. 1-23 Steady-state CET model](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79365c18-abb0-48c1-a2f9-e6f3e8539f89/resource) (`79365c18-abb0-48c1-a2f9-e6f3e8539f89`)