---
version: "v1"
generated_at: "2026-06-18T13:40:35+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 16
  source_quality_score: 0.84
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

## 概述

Pandat 是美国 CompuTherm 推出的面向金属合金领域的商用 CALPHAD 热力学计算软件套件，产品体系包含 Pandat 主程序、PanEngine 二次开发引擎和配套专属热力学数据库。其核心优势在于操作界面友好，进行热力学计算时无需用户预先设置计算初值，软件可自动搜索多元相体系的稳定相 [[S10]]。Pandat 支持相图计算、热力学属性预测、凝固模拟、液相投影面生成、相图优化以及基于 C++ 环境的动力学二次开发等核心功能 [[S10]]。配套的 Pan 系列热力学数据库在有色金属领域优势突出，尤其镁（如 PanMg7）、铝相关数据库的计算精度处于国际领先水平 [[S10,S13]]。

## 核心计算功能

Pandat 提供从单点平衡求解到复杂多元相图生成的完整计算体系，可按照变量控制方式划分为点计算、线计算和截面计算三大类。

### 点计算

点计算功能可针对指定固定成分的合金，完成单点热力学平衡求解，输出该固定点下的平衡相转变温度、相组成、平衡相分数等参数 [[S3,S2]]。典型应用包括：

- 计算 AM50-Y 镁合金共晶转变点的残余液相含量 [[S3]]
- 求解过共晶 Al-Si-Cu-Mg 合金中 Mg₂Si 相的生成平衡点 [[S2]]

### 线计算

线计算功能支持沿温度单向变化路径或单一组分单向变化路径，输出连续的相平衡演化结果 [[S3,S5]]。典型应用为：

- 生成合金凝固过程中固相分数随温度连续变化的凝固曲线 [[S3]]
- 计算多元合金的变温截面相图，如 Al-8Mg-xSi 合金、Al-xMg-3Si 三元合金的变温截面 [[S5]]

### 截面计算

截面计算功能可固定指定参数（如温度）后求解剩余维度下的等温相截面，直观展示不同成分区间的相组成分布。典型应用包括：

- 生成 Al-Cu-Mn 体系的 530 ℃ 等温截面 [[S18]]
- 生成 Al-8.2Si-0.8Fe-0.5Mn-Cu-Mg 合金的 100 ℃ 等温截面 [[S16]]

## 配套数据库

Pandat 的配套 Pan 系列数据库在有色金属领域具备行业领先优势，其中镁系、铝系的热力学数据精度处于全球顶尖水平 [[S10]]。数据库体系覆盖的主要合金系统如下：

| 数据库类型 | 适用材料体系 | 说明 |
|---|---|---|
| 铝基数据库（PanAl 系列） | Al 基合金 | PANAl2016 为 2016 版铝基合金数据库；另有 PandatAl2018_TH 用于 2018.1 版软件记载 [[S12]] |
| 镁基数据库（PanMg 系列） | Mg 基合金 | PanMg7 为典型代表，广泛用于镁合金杂质容限计算 [[S13]] |
| 钛基数据库 | Ti 基合金 | CompuTherm 自主开发 [[S10]] |
| 铁基数据库 | Fe 基合金 | CompuTherm 自主开发 [[S10]] |
| 镍基数据库 | Ni 基合金 | CompuTherm 自主开发 [[S10]] |
| 锆基数据库 | Zr 基合金 | CompuTherm 自主开发 [[S10]] |
| 铜合金数据库 | Cu 基合金 | 日本开发，CompuTherm 获授权集成 [[S10]] |
| 焊料数据库（Solder） | 钎焊料合金 | 日本开发，CompuTherm 获授权集成 [[S10]] |

此外，Pandat 可导入标准 .tdb 格式的开放热力学数据库文件。部分二元及多元合金 .tdb 数据库可从 NIMS 计算相图数据库站点（CPDDB）以及 Matcalc 站点获取后直接使用 [[S15]]。

## 计算原理：CALPHAD 方法

Pandat 完全基于 CALPHAD（CALculation of PHAse Diagrams，相图计算）方法实现热力学计算 [[S8]]。该方法的核心逻辑是通过最小化合金体系的总吉布斯自由能来获得相平衡状态 [[S8,S4]]。

在 CALPHAD 框架下，合金体系中每一相的吉布斯自由能 \(G^\Phi\) 通常由三部分组成 [[S8,S9,S4]]：

1. **参考项（\(G^0\)）**：纯组元机械混合所对应的吉布斯自由能；
2. **理想混合熵项（\(G^{ideal}\)）**：理想溶液的混合熵贡献；
3. **超额自由能项（\(G^{excess}\)）**：描述非理想行为的冗余项，通常以 Redlich-Kister 多项式展开。

CALPHAD 方法采取自下而上（bottom-up）的处理方案：从一元系、二元系、三元系逐步经实验数据校准后，外推至高元合金体系进行预测 [[S4]]。

## 在压铸领域的应用

Pandat 在压铸铝合金和镁合金的合金设计、工艺优化和缺陷分析中得到了广泛的应用。

### 铝合金压铸

**成分区间优化** 在 Al-Mg-Si-Mn-Cu-Zr 压铸铝合金开发中，研究者利用 Pandat 计算了 300 ℃ 的 Al-Mg-Si 三元合金等温截面相图以及 Al-8Mg-xSi、Al-xMg-3Si 的变温截面相图。计算明确了不同 Mg、Si 含量区间对应的第二相组成，为避免过宽凝固区间导致的缩松、热裂倾向以及过量 Al₃Mg₂ 相割裂初生 α-Al 基体提供了热力学依据，最终将 Mg 含量控制在 6%~10%、Si 含量控制在 1%~3% 的范围内 [[S5]]。

**凝固路径对比** 针对美铝 C611 和德国 Castasil 37 两种代表性 AlSi 系免热处理压铸合金，Pandat 软件根据实测成分计算了两种合金的凝固曲线，发现 Castasil 37 更早进入共晶凝固阶段、凝固温度范围更小。该计算结果与 DSC 实测的固液相线、凝固放热峰结果高度吻合，可用于解释不同合金的流动性、冷隔缺陷倾向性差异 [[S14,S17]]。

**凝固相图与相组成临界值** 针对过共晶 Al-17Si-4Cu-xMg 半固态压铸合金，Pandat 计算得到的平衡凝固相图表明：Mg 含量 2.2% 为临界值，低于该值组织中不会生成 Mg₂Si 相，高于该值时凝固组织中出现 Mg₂Si 相。此外，540 ℃ 等温截面计算得出了 Cu、Mg 元素含量满足 Mg₂Si 相析出的线性临界关系式 \(w\%(Cu) = -0.24 + 1.82\cdot w\%(Mg)\)，为过共晶半固态压铸合金的元素配比设计提供了直接的理论指导 [[S2]]。

![图7.1 Al-17Si-4Cu-xMg合金的平衡凝固相图，由Pandat软件计算，横轴为Mg质量分数，纵轴为温度，标注2.2%Mg为相组成临界边界](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c31b2a5-df38-4f65-ad32-c30d25dba82c/resource)

### 热裂倾向评估

利用 Pandat 热力学数据库可计算裂纹敏感性指数 CSI（\(CSI = \max \lvert dT/d(f_s^{1/2}) \rvert\)，\(f_s \leq 0.99\)），用于评估合金的热裂倾向 [[S11]]。在低热裂高强韧半固态压铸 Al-Zn-Mg-Cu 合金开发中，Pandat 批量计算了 27 种不同 Zn、Mg、Cu 含量合金的 CSI 值，其中 Al10Zn6Mg4Cu 合金的 CSI 值最低（1272），仅为 7075 合金 CSI 值（3980）的约 1/3，为快速筛选低热裂倾向的合金成分区间提供了高效工具 [[S11]]。

![图3 19#~27# Al-Zn-Mg-Cu合金热裂倾向CSI值柱状图，直观呈现不同合金热裂倾向差异](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/48da3ef9-2390-4f81-a148-e6382db5086f/resource)

### 镁合金压铸

针对 AM50 压铸镁合金添加微量 Y 元素的改性研究，Pandat 计算得到的合金凝固曲线可区分 \(L \rightarrow \alpha\)-Mg 和 \(L \rightarrow \alpha\)-Mg + Mg₁₇Al₁₂ 两段相转变过程，准确预测脆性温度区间内的固相含量变化以及共晶转变点残余液相含量。计算得到的 \(\alpha\)-Mg 和 Mg₁₇Al₁₂ 相转变温度与 DSC 实测结果几乎一致，可直接用于分析 Y 元素对合金热裂补缩能力的影响规律 [[S3]]。

## 与同类软件的对比

Pandat 是热力学计算软件领域的后起产品，主要竞争对手为 Thermo-Calc 和 FactSage。三者在发展背景、数据库特色和操作体验方面各有侧重 [[S10,S7]]。

| 对比维度 | Pandat | Thermo-Calc | FactSage |
|---|---|---|---|
| 开发单位 | 美国 CompuTherm | 瑞典皇家工学院（1981 年首发） | 加拿大蒙特利尔工学院 FACT 系统 |
| 核心优势 | 界面友好，无需设置计算初值；Al、Mg 数据库全球领先 | 历史悠久、功能完善、用户群大；自主开发大量 Fe 基、Ni 基数据库；扩展性强 | 从熔盐/氧化物/无机物起家，适配冶金和化工行业 |
| 适用领域 | 金属合金 | 冶金、金属合金、陶瓷、硬质合金、核材料等 | 冶金、化工、金属相图 |
| 数据库特色 | 有色金属（Al、Mg、Ti）为核心，Fe、Ni、Zr、Cu、Solder 均有覆盖 | 大量自主研发 Fe、Ni 基数据库；Al、Mg、Ti 数据库采购自 ThermoTech；覆盖无机物、陶瓷、硬质合金、核材料 | 金属溶液、氧化物液相/固相、熔盐、水溶液、炉渣数据库；提供钢铁、轻金属、超纯硅数据库 |
| 动力学功能 | C++ 环境二次开发 | DICTRA 模块（扩散模拟等） | - |
| 主要短板 | 对低含量特殊相预测存在缺口 | 界面友好度低、上手难；需要预设计算初值 | - |

## 版本与许可信息

Pandat 为商用软件，公开学术文献中存在 Pandat 2018.1 版本的正式使用记录，配套数据库包括 PandatAl2018_TH [[S12]]。PANAl2016 为 CompuTherm 铝基合金热力学数据库的 2016 版本，面向铝基合金体系热力学计算场景 [[S12]]。软件的全套产品线包含 Pandat 主程序、PanEngine 计算引擎以及配套专属数据库，可根据用户需求进行产品组合授权 [[S10]]。

## 局限性

目前已知的局限性主要体现在以下方面：

- **低含量特殊相的数据覆盖缺口**：当合金中低占比添加相（如低 Y 含量镁合金中的 Al₂Y 相）含量较低时，Pandat 计算得到的理论凝固曲线中不会呈现对应的特征相转变点，与 DSC 实测的相变特征对应性不足，表明存在低含量特殊相的热力学数据覆盖缺口 [[S3]]。
- **数据库覆盖范围有限**：以 PanMg7 数据库为例，其包含 Fe 和 Cu 的数据，但缺少 Ni 和 Co 的数据，也未包含 Pr 和 La 等稀土元素的相关数据，限制了在某些特定合金体系中的应用 [[S13]]。

## Sources
- S10: [TextNode352](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6996a834-5ade-4d09-97be-a649e80e325e/resource) (`6996a834-5ade-4d09-97be-a649e80e325e`)
- S13: [corrosion of magnesium alloys__f9b5b9b229](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4a58d01-91a7-4aa6-808a-6cda39b5f1d8/resource) (`a4a58d01-91a7-4aa6-808a-6cda39b5f1d8`)
- S3: [微量Y添加对AM50镁合金热裂行为的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27408155-4f3d-4767-ab6b-0071516cc2f1/resource) (`27408155-4f3d-4767-ab6b-0071516cc2f1`)
- S2: [半固态挤压铸造过共晶Al-Si-Cu-Mg合金热处理强化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/265ee619-c30b-4120-a4a7-d261f1517a76/resource) (`265ee619-c30b-4120-a4a7-d261f1517a76`)
- S5: [Mg、Si质量比与热处理对压铸Al-Mg-Si-Mn-Cu-Zr合金组织性能影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4156b3bf-fd85-4b1b-a681-cb4b642bcd90/resource) (`4156b3bf-fd85-4b1b-a681-cb4b642bcd90`)
- S18: [图1-3 Pandat软件计算的Al-Cu-Mn三元相图（b）Al-Cu-Mn体系530℃等温截面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db8a4bb2-e1f7-4263-8377-372fa18c1db8/resource) (`db8a4bb2-e1f7-4263-8377-372fa18c1db8`)
- S16: [图1-12 用Pandat软件计算Al-8.2Si-0.8Fe-0.5Mn-Cu-Mg合金在100°C的等温剖面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4a6fb7d-7bac-41b0-a551-f01f574f1afa/resource) (`c4a6fb7d-7bac-41b0-a551-f01f574f1afa`)
- S12: [age hardening of high pressure die casting almg alloys with zn and combi__2edc18344c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d67bf37-d7bd-4fec-80c7-08dc3a81f0e8/resource) (`8d67bf37-d7bd-4fec-80c7-08dc3a81f0e8`)
- S15: [0165_9c7e190c566950f1_Scheil_equation](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0d16001-6bf2-44c6-9a48-885b3ded943e/resource) (`b0d16001-6bf2-44c6-9a48-885b3ded943e`)
- S8: [complex concentrated alloys ccas__861b70e9c9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5d3ec237-78e1-44cb-9b24-73efd0fecdbb/resource) (`5d3ec237-78e1-44cb-9b24-73efd0fecdbb`)
- S4: [alloys and intermetallic compounds from modeling to engineering__edf223cde2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/38a4a310-637c-4191-8b60-7e445470cbb7/resource) (`38a4a310-637c-4191-8b60-7e445470cbb7`)
- S9: [alloy physics a comprehensive reference__0572c6adf4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5fc067e7-1f1a-4e09-beab-cd43fc72cc13/resource) (`5fc067e7-1f1a-4e09-beab-cd43fc72cc13`)
- S14: [两种常用免热处理压铸铝合金的对比研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b051c966-84af-47a9-87fa-b7678414e076/resource) (`b051c966-84af-47a9-87fa-b7678414e076`)
- S17: [两种常用免热处理压铸铝合金的对比研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cc09f6ef-ddff-4d18-9c30-46956a4b3dc2/resource) (`cc09f6ef-ddff-4d18-9c30-46956a4b3dc2`)
- S11: [低热裂、高强韧半固态压铸Al-Zn-Mg-Cu合金开发](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/809a19b3-29cb-4aad-bfe9-895d291da4c1/resource) (`809a19b3-29cb-4aad-bfe9-895d291da4c1`)
- S7: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b146c32-845c-420d-8374-5d67c175a863/resource) (`4b146c32-845c-420d-8374-5d67c175a863`)