---
version: "v1"
generated_at: "2026-06-18T19:38:28+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 32
  source_quality_score: 0.87
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 定义与分类

JIS AC4B 是日本工业标准（JIS）中规定的一种 Al-Si-Cu 系铸造铝合金，其牌号前缀“AC”代表铝基铸造合金（Aluminum Casting）[[S6,S9]]。该合金正式收录于 JIS H5302-1976《压铸铝合金》标准，同时也出现在 JIS H5202（重力铸造用铝合金）标准体系中，面向铸造及压铸场景管控成分[[S30,S9,S6]]。

AC4B 属于在 Al-Si 系合金中添加 Cu 元素以改善切削性与力学性能的合金类型[[S6,S18]]。典型成分为 Al-8.2Si-2.6Cu[[S21]]。

## 化学成分

JIS H5302-1976 标准规定的 AC4B 铝合金化学成分（质量分数，%）如下表所示[[S30]]。

| 元素 | Si | Fe | Cu | Mn | Mg | Zn | Ni | Ti | Pb | Sn | Cr | Al |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 含量 (wt%) | 7.0~10.0 | ≤1.0 | 2.0~4.0 | ≤0.50 | ≤0.50 | ≤1.0 | ≤0.35 | ≤0.20 | ≤0.20 | ≤0.10 | ≤0.20 | 余量 |

工程实测案例中常规 AC4B 合金的典型成分为 Si 8.1%、Cu 1.3%、Mg 0.4%、Mn 0.42%，其余主要为 Al[[S15]]。另一来源给出的典型成分为 Al-8.2Si-2.6Cu[[S21]]。

## 物理性能

下表列出 JIS 标准中 AC4B 合金的物理性能参数[[S14]]。

| 性能项目 | 数值 | 单位 |
|----------|------|------|
| 密度 (20°C) | 2.77 | g/cm³ |
| 液相线温度 | 590 | °C |
| 固相线温度 | 520 | °C |
| 线膨胀系数 (20~100°C) | 21.0×10⁻⁶ | /°C |
| 线膨胀系数 (20~200°C) | 22.0×10⁻⁶ | /°C |
| 线膨胀系数 (30~300°C) | 23.0×10⁻⁶ | /°C |
| 热传导系数 (25°C) | 96 | W/(m·°C) |
| 纵向弹性模量 | 76.0 | GPa |
| 横向弹性模量 | 25.0 | GPa |

**关于熔化温度区间的说明**：JIS 标准给出的固/液相线温度为 520°C/590°C[[S14]]，此数值落在 522~596°C 的常见描述区间附近，为日本官方标准优先采用值。另有基于 JMatPro 软件计算得到的结果为固相线 521°C、液相线 606°C[[S19]]，以及国内铸造工艺实测得到的凝固温度区间 508~588°C[[S35]]。多源数据存在一定差异，当需要标准合规判定时宜优先采纳 JIS 标准值。

AC4B 合金在不同温度下的固相率变化规律表明：500°C 前固相率为 1.0，500~600°C 区间快速降至 0，显示出宽阔的固液两相区[[S26]]。密度在 500~600°C 固液转变区间出现显著下降[[S10]]。导热系数在 0~500°C 区间保持较高水平，500~600°C 随固液转变骤降，完全液化后回升[[S31]]。

![图3.1 AC4B合金的导热系数、热焓值、密度、固相率随温度变化曲线，横轴覆盖0~800°C，呈现固相率在500~600°C由1.0快速降至0的典型糊状凝固特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa50703d-678d-4141-ab02-ae97180534a8/resource)

## 相组成与微观组织

AC4B 压铸铝合金的铸态典型相组成已通过金相显微镜（OM）和扫描电镜（SEM）得到实测验证，明确包含以下相[[S28,S17,S11]]：

- **α-Al 基体**：合金的连续基体相。
- **共晶 Si**：呈浅灰色针状/板条状分布在 α-Al 基体上，为组织中数量最多的第二相。
- **Al₆(Fe,Mn)Si 相**：亦呈针状/板条状、浅灰色形貌，与共晶 Si 共存于基体中。
- **Al₂Cu 相**：呈块状化合物形态，在凝固过程中为最先形成的初生相之一。
- **Al₅Cu₂Ni 相**：亦呈块状化合物形态，与 Al₂Cu 相伴生[[S11,S29]]。

SEM/EDX 定量分析确认，Al₂Cu 相和 Al(Fe,Mn)Si 相是凝固过程中最先形成的两个初生相[[S11,S29]]。添加微量 Sr 元素时，Sr 优先偏聚在 Al(Fe,Mn)Si 相和共晶 Si 相的 <111> 晶面上，干扰相的生长孪晶面形成，实现对硅相的变质细化效果[[S11]]。

![AC4B铝合金标准金相显微组织图，出自《实用铝铜及其合金金相热处理和失效分析》，展示α-Al基体上针状/板条状共晶Si和块状化合物的分布特征](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d88c7e4-4ef4-4e8f-9149-aed04cf8b5c4/resource)

当合金经历固溶加热温度过高（过烧）时，会出现共晶硅集聚长大、共晶体复熔物呈团絮状和椭圆形等特征，且无常规过烧球现象[[S15]]。

## 铸造工艺特性

### 凝固特性

AC4B 合金具有宽阔的结晶温度范围（JIS 标准值 520~590°C），呈现典型的**糊状凝固**特性，区别于 ADC12 的近共晶层状凝固特性[[S21,S14]]。

### 工艺性能评价

下表总结 AC4B 合金的综合铸造工艺特性（1 为优，5 为劣）[[S7,S6]]：

| 工艺特性 | 评价 |
|----------|------|
| 熔液流动性 | 良好 |
| 耐压性 | 优良 |
| 热裂倾向 | 低 |
| 铸造裂纹倾向 | 低 |
| 缩孔倾向 | 低 |
| 焊接性 | 良好 |
| 耐蚀性 | 相对较差 |
| 热处理响应 | 可经 T5/T6 热处理强化 |

### 推荐工艺参数

- **浇注温度**：推荐区间 610~730°C，树脂砂低压铸造场景下常用浇注温度为 720°C[[S5,S8,S27]]。
- **模具预热/工作温度**：190~270°C[[S8]]。
- **参考压射参数**（基于同系 AlSi9Cu 类合金）：一级压射速度 0.02~0.34 m/s，二级压射速度 1.2~3.8 m/s，增压压力 120~280 bar[[S5]]。
- **变质处理**：Sr、Ti 复合变质可细化微观组织，优化铸件力学性能[[S34]]。

## 力学性能

AC4B 合金的力学性能与其状态（铸态、热处理态）及铸造工艺方法密切相关。该合金采用 T5、T6 热处理工艺进行强化，铸态与热处理态性能符合日本 JIS H5202 标准对应要求[[S7,S18]]。

JIS H5302 标准体系下力学性能拉伸试样采用指定尺寸的金属型铸型制备，标准试样的铸型图纸标注有全周边 R3、R5 的圆角尺寸，用于标准性能测试[[S23,S33]]。

在压铸工艺中，较高的冷却速率会促进针状有害 β-Al₅FeSi 相向低危害的粒状 α-(FeMn)₃Si₂Al₁₅ 富铁相转变；当合金中 Mn 含量高于 Fe 含量时，富铁相的粒化程度进一步提升，可有效降低其对基体的脆化作用[[S16,S36]]。

## 对比与应用

### 与其他合金的对比

| 对比项 | AC4B | ADC12 | AC4C | A380 | A356 |
|--------|------|-------|------|------|------|
| 合金系 | Al-Si-Cu | Al-Si-Cu | Al-Si-Mg | Al-Si-Cu | Al-Si-Mg |
| 典型 Si (%) | 7.0~10.0[[S30]] | 9.6~12[[S12]] | 6.5~7.5[[S30]] | 8.5~12[[S3]] | ~7[[S32]] |
| 典型 Cu (%) | 2.0~4.0[[S30]] | 1.5~3.5[[S12]] | ≤0.25[[S30]] | ~3.5[[S3]] | 无 |
| Mg (%) | ≤0.50[[S30]] | ≤0.3[[S12]] | 0.25~0.45[[S30]] | ≤0.10[[S3]] | ~0.3[[S32]] |
| 凝固特征 | 宽结晶区间，糊状凝固[[S21]] | 近共晶，层状凝固[[S21]] | 中等区间 | — | — |
| 耐蚀性 | 较差[[S6]] | 较差 | 优异[[S6]] | 较差 | 优异[[S22]] |
| 切削性 | 良好[[S6]] | 良好 | 尚可 | 良好 | 较差 |
| 热处理强化 | 可 T5/T6[[S18]] | 受限 | 可 T4/T6[[S22]] | 受限 | 可 T6[[S22]] |
| 典型适用场景 | 耐压壳体、发动机缸体/缸盖[[S19,S18]] | 薄壁复杂压铸件[[S21,S12]] | 要求耐蚀/导电的结构件[[S6]] | 大型压铸件[[S3,S24]] | 要求韧性的结构件[[S22]] |

**与 ADC12 的差异**：AC4B 的 Si 含量更低、结晶温度区间更宽，凝固为糊状凝固，ADC12 为近共晶层状凝固。ADC12 压铸件热脆性更低，更适合薄壁复杂压铸件；AC4B 更适合需要后续热处理提升性能的中厚壁耐压零件[[S21,S12]]。

**与 AC4C 的差异**：AC4B 添加了约 2.6% 的 Cu 元素以提升切削性和热处理强化效果，而 AC4C 为 Al-Si-Mg 系不含 Cu。AC4C 的耐蚀性和导电性更优异，可通过 T4/T6 热处理获得更高的综合力学性能[[S6,S13]]。

### 典型应用领域

AC4B 合金广泛用于各类耐压机械零件的铸造生产，是制造发动机缸盖、缸体的常用铝合金牌号之一[[S19,S18]]。主要应用包括[[S6,S19,S1,S18]]：

- 发动机缸盖、缸体
- 泵体及耐压壳体类铸件
- 结构复杂的机械零件
- 适配金属模铸造、低压铸造工艺的中厚壁耐压部件

## Sources
- S6: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2ddb21d9-ad51-4139-a83f-02b121d79e6e/resource) (`2ddb21d9-ad51-4139-a83f-02b121d79e6e`)
- S9: [TextNode36](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/394db064-901d-4687-8f0d-5fd71b983ee6/resource) (`394db064-901d-4687-8f0d-5fd71b983ee6`)
- S30: [表 2-28 压铸铝合金化学成分 (JIS5302-1976)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb4d069d-6f35-46a9-9d58-5c82e406ba50/resource) (`cb4d069d-6f35-46a9-9d58-5c82e406ba50`)
- S18: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7b8aa5ba-8fbf-42f0-a36f-1d784dc2b3d4/resource) (`7b8aa5ba-8fbf-42f0-a36f-1d784dc2b3d4`)
- S21: [局部加压Al-Si-Cu系合金的Cu偏析及流动机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/844e4b15-1f42-44ff-99ce-2a9ca66330da/resource) (`844e4b15-1f42-44ff-99ce-2a9ca66330da`)
- S15: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/76321aea-45e2-4d46-bc42-ca19915ce534/resource) (`76321aea-45e2-4d46-bc42-ca19915ce534`)
- S14: [表 3-7 重力铸造用铝合金的物理性能 (JIS 标准)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a357633-efee-48b7-af95-785431ea5b50/resource) (`6a357633-efee-48b7-af95-785431ea5b50`)
- S19: [铝合金缸盖金属型倾转铸造工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bae125d-3bb9-4a74-bc7c-c2548e392901/resource) (`7bae125d-3bb9-4a74-bc7c-c2548e392901`)
- S35: [AC4B合金凝固率随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f4b96e81-0e60-4bdd-b7b1-ca24682bf49d/resource) (`f4b96e81-0e60-4bdd-b7b1-ca24682bf49d`)
- S26: [图3.1 AC4B合金的导热系数、热焓值、密度、固相率随温度变化图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa50703d-678d-4141-ab02-ae97180534a8/resource) (`aa50703d-678d-4141-ab02-ae97180534a8`)
- S10: [AC4B合金密度随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4229e09a-1611-46eb-9f03-143fd59173fe/resource) (`4229e09a-1611-46eb-9f03-143fd59173fe`)
- S31: [AC4B合金导热系数随温度变化曲线图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cce58a63-ace7-40b0-9e1c-bd0fca0dc615/resource) (`cce58a63-ace7-40b0-9e1c-bd0fca0dc615`)
- S28: [Zn-Al钎料钎焊Al-Si-Cu压铸铝合金组织及性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba6e4862-b28a-48be-a3fa-1a091d13c0fb/resource) (`ba6e4862-b28a-48be-a3fa-1a091d13c0fb`)
- S17: [Zn-Al钎料钎焊Al-Si-Cu压铸铝合金组织及性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/797a0bfd-9495-4174-be77-5c58662c160d/resource) (`797a0bfd-9495-4174-be77-5c58662c160d`)
- S11: [effects of combination of 002 wt sr and ti on the characteristics of ac4__29b5b91aee](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e14fe0a-7ed9-417f-81cf-b907969e17ac/resource) (`4e14fe0a-7ed9-417f-81cf-b907969e17ac`)
- S29: [AC4B合金各相的成分、颜色及可能相组成表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c2a58558-5f22-43a3-9f69-d405699b5806/resource) (`c2a58558-5f22-43a3-9f69-d405699b5806`)
- S7: [重力铸造用铝合金的铸造性与物理性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/324f35c0-f423-4bdd-8887-680e798f020e/resource) (`324f35c0-f423-4bdd-8887-680e798f020e`)
- S5: [die casting process optimization using taguchi methods__eca7652172](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/29f38cea-127b-4999-9a88-7ec6134087d4/resource) (`29f38cea-127b-4999-9a88-7ec6134087d4`)
- S8: [a study of porosity formation in pressure die casting using the taguchi__4ac320727f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/373145fd-0ac2-4c63-bf89-5bc7ecb66dbd/resource) (`373145fd-0ac2-4c63-bf89-5bc7ecb66dbd`)
- S27: [表4.4 工艺参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6ef46ba-6337-41e5-94c6-794a6bb786c5/resource) (`b6ef46ba-6337-41e5-94c6-794a6bb786c5`)
- S34: [AC4B合金的扫描电镜微观结构（含Sr与Ti添加）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/defb382a-1e6f-4f2a-9a41-4703ca9b981e/resource) (`defb382a-1e6f-4f2a-9a41-4703ca9b981e`)
- S23: [金属型试样的铸型示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8eacc982-6a25-4050-b8de-04ca5b935c02/resource) (`8eacc982-6a25-4050-b8de-04ca5b935c02`)
- S33: [适用于7种和9种合金的金属型试样铸型图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db342aa4-439a-4524-a734-94c2f08faa58/resource) (`db342aa4-439a-4524-a734-94c2f08faa58`)
- S16: [correlation between segregation behavior and wall thickness in a rheolog__a4234ae113](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/784e7151-a917-4b74-b71f-310ec6361f51/resource) (`784e7151-a917-4b74-b71f-310ec6361f51`)
- S36: [correlation between segregation behavior and wall thickness in a rheolog__a4234ae113](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7f48e2a-7d2c-4da7-9243-badf3e032f24/resource) (`f7f48e2a-7d2c-4da7-9243-badf3e032f24`)
- S12: [346011_ADC12](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5360db8a-9d57-4216-a66f-54ad6f211a0b/resource) (`5360db8a-9d57-4216-a66f-54ad6f211a0b`)
- S3: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11d4bc0b-e810-41fc-855e-69a767839057/resource) (`11d4bc0b-e810-41fc-855e-69a767839057`)
- S32: [Table 2 Chemical composition of A356 and A357](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d74eb2aa-dd5c-4fe1-8176-c9d8ca7d1ab0/resource) (`d74eb2aa-dd5c-4fe1-8176-c9d8ca7d1ab0`)
- S22: [特种铸造 国外现代铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86d3a765-2c3d-4e98-bf23-2db2e4f25391/resource) (`86d3a765-2c3d-4e98-bf23-2db2e4f25391`)
- S24: [铝及铝合金材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c1ad7af-032b-4ea5-ad57-96c963416703/resource) (`9c1ad7af-032b-4ea5-ad57-96c963416703`)
- S13: [铝与铝合金材料生产技术500问](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/554fa922-5344-4271-bfbb-c0822929ce29/resource) (`554fa922-5344-4271-bfbb-c0822929ce29`)
- S1: [铝合金材料的应用与技术开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09b9ff0e-20f2-49ce-997f-c6d6eec0ab3d/resource) (`09b9ff0e-20f2-49ce-997f-c6d6eec0ab3d`)