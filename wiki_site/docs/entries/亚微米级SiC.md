---
version: "v1"
generated_at: "2026-06-18T18:38:18+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 43
  source_quality_score: 0.86
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 定义与分类
亚微米级碳化硅（submicron SiC）是指平均粒径落在 **0.1 μm ~ 1.0 μm** 区间内的 SiC 粉末，行业内要求该粒度区间的粉末粒度分布窄，不得含有 1 μm 以上的大颗粒 [[S33,S2]]。它与纳米级 SiC（粒径 < 100 nm）和常规微米级 SiC（粒径 > 1 μm）存在明确的粒径界限 [[S2]]。在金属基复合材料领域，亚微米级 SiC 主要作为增强颗粒添加至铝基体中，属于“颗粒增强铝基复合材料”的细粒径分支 [[S14]]。

## 基本物理属性
亚微米级 SiC 的主要物理性质汇总如下（部分数据为典型商用粉末的实测值）：

- **晶体结构与形态**：原料多为 β‑SiC 或 α‑SiC，面向金属基复合材料的亚微米级 SiC 粉末典型形貌为不规则多边形，该形貌有助于提高与金属基体的界面结合力，降低复合材料的各向异性风险 [[S35]]。
- **硬度与热稳定性**：莫氏硬度 **9.2 ~ 9.5**，显微硬度约 3340 HV，熔点约 **2700 °C**，热膨胀系数 **3.40 × 10⁻⁶ K⁻¹** [[S15,S20,S22]]。
- **密度**：**3.21 ~ 3.22 g/cm³**（增材制造用亚微米 SiC 粉末实测约 3.2 g/cm³） [[S15,S20,S50]]。
- **比表面积**：常压烧结用亚微米 β‑SiC 粉末要求比表面积**>15 m²/g**，氧质量分数 < 0.2 %，以利于无压烧结致密化 [[S3]]；通用商用亚微米 SiC 粉末的比表面积通常要求不低于 10 m²/g [[S28]]。
- **纯度**：面向选区激光熔化的亚微米级 SiC 粉末实测纯度 **>99.9%**，其激光吸收率可达 **85%** [[S50]]。

下表对比了亚微米 SiC 与金属基体及其他增强相粉末的典型物理性能 [[S50]]：

| 材料 | 密度/g·cm⁻³ | 纯度 | 平均粒径 | 激光吸收率 |
|------|------------|------|---------|------------|
| AlSi10Mg（基体） | 2.68 | >99.9% | 26.4 μm | 9% |
| **亚微米级 SiC** | **3.2** | **>99.9%** | **0.5 μm** | **85%** |
| 纳米级 Al₂O₃ | 3.98 | >99.9% | 50 nm | 78% |
| 微米级 Al₂O₃ | 3.98 | >99.9% | 6 μm | 78% |

## 制备与预处理工艺
### 预分散工艺
为克服亚微米 SiC 颗粒间强范德华力导致的团聚倾向，常采用真空球磨‑冷压‑烧结的预分散流程 [[S49]]：
1. 将亚微米 SiC 与微米级 Al 粉（或镁合金粉）按比例混合，在球料比 **10:1**、转速 **300 rpm** 条件下球磨 **5 h**，使 SiC 颗粒均匀粘附在金属粉末表面；
2. 将混合粉末冷压成坯（典型压力 100 kN，保压 5 min）；
3. 真空烧结（例如 700 °C、2 h）制备成中间合金，随后分批加入熔体中，利用逐步溶解实现 SiC 的均匀分散 [[S49]]。

### 表面涂覆处理
化学镀镍是提高亚微米 SiC 与铝熔体润湿性的常用表面预处理方法：在 SiC 颗粒表面均匀镀覆金属镍层，可显著改善润湿性，抑制界面脆性相 Al₄C₃ 的生成，同时降低长时间压铸过程中熔体粘度的上升幅度 [[S23,S47,S9]]。

## 在铝基体中的工艺行为
### 搅拌铸造与半固态压铸工艺参数
半固态搅拌铸造是制备亚微米 SiC 增强铝基复合材料的典型工艺，其关键在于利用半固态浆料的适当粘度减轻颗粒的上浮偏聚 [[S19,S46]]。典型参数窗口为 [[S19]]：
- 合金半固态阶段固相分数保持约 **40%**；
- 搅拌转速约 **1200 r/min**；
- 全部颗粒添加完成后继续搅拌 **15 ~ 30 min**，在保证 SiC 均匀分布的同时避免卷气。

### 熔体流动与充型行为
添加亚微米 SiC 后，熔体粘度显著高于纯铝熔体，且随 SiC 添加量增加粘度持续升高 [[S27,S40]]。这使得充型流动更为平稳、涡流效应减弱，有利于定向凝固，但熔体流动性随颗粒含量上升而下降，充填复杂薄壁型腔时需要匹配更高的充型压力和充型速度 [[S40]]。

### 界面反应与控制
SiC 与铝液在高温下遵循**溶解‑扩散**机制 [[S41,S42]]：
- SiC 在铝液中溶解，C、Si 元素进入熔体；
- 由于 C 在铝液中溶解度极低且扩散系数高，当界面 C 浓度饱和后，Al₄C₃ 相以细杆状或块状从界面向铝液中生长；
- Si 的扩散速率较慢，一部分 Si 在 SiC/Al 界面处形成厚度**小于 3 nm**的纳米 Si 过渡层，该过渡层可改善界面润湿性、提高界面结合强度 [[S41]]。

**润湿性与有害反应控制**：SiC 与纯铝液的本征润湿角高达 **155°**，属于典型的非润湿体系，直接复合十分困难 [[S41]]。若铝液温度超过 **710 °C** 且合金中 Si 含量较低时，会大量生成 Al₄C₃ 脆性相，导致复合材料耐腐蚀性和力学性能急剧劣化，甚至使熔体无法正常浇注 [[S5]]。向铝合金基体中添加适量 Si 元素，可优先促进 Si‑C 结合，有效抑制 Al₄C₃ 的生成 [[S21,S38]]。

> **关于 Al₄C₃ 的实践共识**：高温下短暂停留生成的纳米级细小 Al₄C₃ 弥散分布于基体中，可能对性能产生有利作用；若在 640 °C 长时间热暴露（如 10 h），Al₄C₃ 将长大为块状脆性相，且 Al₄C₃ 为水溶性相，会使复合材料在高湿环境中发生腐蚀，降低构件服役可靠性 [[S41,S1]]。

## 常见缺陷与分散问题
亚微米 SiC 的比表面积大，颗粒间范德华力远强于微米级颗粒，若工艺控制不当，极易形成尺寸可达 **100 ~ 200 μm** 的团簇 [[S34,S32]]。团簇内部的缝隙无法被铝熔体完全填充，由此诱发多种缺陷 [[S43,S4,S26,S30,S48]]：
- **气孔**：颗粒表面吸附的气体及搅拌卷气未能逸出；
- **间隙孔隙**：团聚颗粒间隙未被熔体充分浸润；
- **微裂纹**：颗粒富集区因应力集中而萌生；
- **偏聚缺陷**：颗粒在铸件特定区域聚集，导致性能不均匀。

这些缺陷显著削弱复合材料的有效承载面积，并在孔洞与团聚区域引发严重应力集中，当亚微米 SiC 添加量超过最优阈值后，复合材料强度、延伸率等综合性能会迅速下降 [[S48]]。

## 对铝基复合材料性能的贡献
### 力学性能提升
- **铸造铝合金‑亚微米 SiC 体系**：在 ZL101（ZAlSi7Mg）铝合金中加入 **16 ~ 20 wt%** 的亚微米 SiC，经 T6 热处理后，室温屈服强度相比未增强合金提升 **66%**，333 °C 高温下屈服强度提升 **200%** 以上，整体耐磨性可提高约 **2.5 倍** [[S17]]。
- **粒径效应**：当 SiC 体积分数相同时，颗粒尺寸越小，复合材料强度越高，但延性随之降低；随 SiC 体积分数升高，抗拉强度、屈服强度和弹性模量同步上升，线膨胀系数同步下降 [[S18]]。
- **增材制造示例**：在选区激光熔化优化的工艺参数下，亚微米 SiC 增强 AlSi10Mg 复合材料可达到最大抗拉强度 **435 MPa**、显微硬度 **190.17 Hv**，相比未增强 AlSi10Mg 合金抗拉强度提升 **18.9%**，强化来源于亚微米 SiC 与原位生成的 Al₄SiC₄ 相的协同作用 [[S24]]。

### 典型应用场景
- **航空航天**：DWA 公司的 25 vol% SiCp/6061Al 复合材料仪表支架已用于 Lockheed 飞机承载电子设备；该类薄板已应用于 F‑16 战机燃油访问舱门、腹鳍、风扇出口导叶，以及 Eurocopter 直升机桨毂套筒；俄罗斯将其用于卫星惯导平台和支承构件 [[S13,S44]]。
- **微电子封装**：含 60 %~ 75 vol% SiC 的 SiC/Al 复合材料性能价格比最优，其热导率与 Cu‑W 相当，密度不到 Cu‑W 的 1/5，弹性模量是 Cu 的两倍。法国 Egide‑Xeram 公司已量产最大外形尺寸 **220 mm × 220 mm** 的该复合材料气密封装外壳，用于军用机载相控阵雷达的微波多芯片组件，标准电子模块（SEM‑E）共振频率可达 600 Hz，比 Cu‑W 高一倍 [[S39,S25]]。
- **汽车与耐磨构件**：亚微米 SiC 增强铝基复合材料用于轻量化发动机活塞、轮毂等耐磨件，可提升部件服役寿命，降低传统合金钢件的自重 [[S45]]。

## 技术局限与挑战
1. **润湿性差**：SiC 与纯铝液的本征润湿角高达 **155°**，直接复合难度极高，且高温下不加控制的反应会生成大量有害脆性相 [[S41,S5]]。
2. **分散均匀性**：亚微米 SiC 的强团聚倾向仅靠常规机械搅拌难以克服，团聚区域成为缺陷源，大幅削弱材料的强韧性匹配水平 [[S31,S14]]。
3. **成本与后续加工**：规模化量产的普通 SiC/Al 复合材料制造成本可控制在 **5 美元/kg** 以下，但亚微米级 SiC 原料价格高于普通微米级 SiC；此外，高硬度增强相的加入使复合材料的切削、焊接等后续加工难度远大于常规铝合金，限制了其大规模民用推广 [[S7,S13]]。

## 与相近概念的关系
- **颗粒增强铝基复合材料**：亚微米级 SiC 是颗粒增强铝基复合材料的细粒径增强体分支，其应用对搅拌分散过程的剪切力和均匀性提出了更高要求 [[S14,S46]]。
- **搅拌铸造**：作为颗粒增强铝基复合材料的主要低成本制备工艺，搅拌铸造通过机械/电磁搅拌等方式将亚微米 SiC 卷入并分散于铝熔体中 [[S34,S46]]。
- **半固态压铸**：半固态压铸工艺高度适配亚微米 SiC 增强铝基复合材料的成形，可降低 SiC 的上浮偏聚倾向，减少气孔和团聚缺陷，提升最终铸件的综合力学性能 [[S14,S46]]。

## 典型微观形貌
下图展示了选区激光熔化工艺制备的（Al₂O₃ + 亚微米 SiC）混杂增强铝基复合材料的 TEM 明场像，图中可见 Al 基体呈胞状分布，亚微米 SiC 颗粒均匀弥散于基体中，表明经过优化的粉末预处理和成形工艺可实现亚微米 SiC 的良好分散 [[S12]]。

![700 mm/s 扫描速度下选区激光熔化制备亚微米 SiC 增强 AlSi10Mg 复合材料 TEM 明场像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/412f5aba-bf59-4603-bab2-650e956527b7/resource)

预分散超声辅助半固态搅拌铸造的完整流程（从粉末预处理到获得复合材料铸件）如下图所示，该工艺路线为克服亚微米 SiC 的团聚问题提供了系统的实现路径 [[S37]]。

![预分散超声辅助半固态搅拌铸造工艺流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bcafd420-40c3-4837-9d82-164ed6c29302/resource)

## Sources
- S33: [工程陶瓷材料的加工技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b35246ce-31cb-4c97-bc94-07878f96afb9/resource) (`b35246ce-31cb-4c97-bc94-07878f96afb9`)
- S2: [b0490 introduction to powder metallurgy__a36c9d0447](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1e9a7de4-b39c-47aa-8655-f150f8e6f094/resource) (`1e9a7de4-b39c-47aa-8655-f150f8e6f094`)
- S14: [基于铝-煅烧高岭土体系的纳米Al2O3p_A356复合材料制备及其挤压铸造研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57625963-572a-42c4-a394-7bec61d8c313/resource) (`57625963-572a-42c4-a394-7bec61d8c313`)
- S35: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4bc67ec-6527-4925-9d23-0ff4b9876704/resource) (`b4bc67ec-6527-4925-9d23-0ff4b9876704`)
- S15: [表面处理技术概论](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65e94e75-b233-4767-ba81-4dd40e992931/resource) (`65e94e75-b233-4767-ba81-4dd40e992931`)
- S20: [低压铸造SiC_Al复合材料铸件的组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/825343c5-f3aa-4370-b6dc-8031b63b0137/resource) (`825343c5-f3aa-4370-b6dc-8031b63b0137`)
- S22: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/861dc85a-f902-4388-8f2d-cd1576db3855/resource) (`861dc85a-f902-4388-8f2d-cd1576db3855`)
- S50: [Tab.2-2 Physical properties of the original powder](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7ff8c3d-dfa6-42f4-a18c-f4cfbd1cdf2d/resource) (`f7ff8c3d-dfa6-42f4-a18c-f4cfbd1cdf2d`)
- S3: [工程陶瓷材料的加工技术及其应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/211ea1a1-ba85-4e1f-94a9-3dd05a358fea/resource) (`211ea1a1-ba85-4e1f-94a9-3dd05a358fea`)
- S28: [2019 asme boiler and pressure vessel code code cases boilers and pressure vessels__656b4c05d7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c28a70b-7b78-4e0a-93e8-eab355d97013/resource) (`9c28a70b-7b78-4e0a-93e8-eab355d97013`)
- S49: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f51e3b42-f9a4-4dec-a608-8cce577ca727/resource) (`f51e3b42-f9a4-4dec-a608-8cce577ca727`)
- S23: [analysis of mold flow and microstructures of die casting in al alloy sic__ef19863685](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e84b56b-4e78-454e-a403-ed330ba374e0/resource) (`8e84b56b-4e78-454e-a403-ed330ba374e0`)
- S47: [analysis of mold flow and microstructures of die casting in al alloy sic__ef19863685](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/edf990b2-c044-427d-9701-ddfbd740a0f4/resource) (`edf990b2-c044-427d-9701-ddfbd740a0f4`)
- S9: [analysis of mold flow and microstructures of die casting in al alloy sic__ef19863685](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/372bea45-45c2-4a87-b27b-fb9970876871/resource) (`372bea45-45c2-4a87-b27b-fb9970876871`)
- S19: [半固态金属成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7cc17d1c-8818-4a40-9617-31fd037bfc2c/resource) (`7cc17d1c-8818-4a40-9617-31fd037bfc2c`)
- S46: [低压铸造SiC_Al复合材料铸件的组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5c75495-7775-4722-a204-12bc846561a7/resource) (`e5c75495-7775-4722-a204-12bc846561a7`)
- S27: [lw2004铝型材技术国际论坛文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95540937-a725-4583-aece-4d3b128f6919/resource) (`95540937-a725-4583-aece-4d3b128f6919`)
- S40: [第三届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c531c991-f8b0-4f51-ac25-5cdad7a1de70/resource) (`c531c991-f8b0-4f51-ac25-5cdad7a1de70`)
- S41: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c755028c-d635-4653-8473-a29724cbebc9/resource) (`c755028c-d635-4653-8473-a29724cbebc9`)
- S42: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d21bffd6-3486-45b0-8c78-399b395bffe7/resource) (`d21bffd6-3486-45b0-8c78-399b395bffe7`)
- S5: [corrosion of aluminium based metal matrix composites__a3a7f960ae](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e74b232-a8cd-4217-8040-4556eef825d8/resource) (`2e74b232-a8cd-4217-8040-4556eef825d8`)
- S21: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8529bcc8-e645-4e05-8fd6-cef9dccfd61a/resource) (`8529bcc8-e645-4e05-8fd6-cef9dccfd61a`)
- S38: [冷却速率及Si含量对连续Cf_Al复合材料组织及性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bedb97c3-ef88-4f5c-98cb-3be5147d69b2/resource) (`bedb97c3-ef88-4f5c-98cb-3be5147d69b2`)
- S1: [aluminum alloys contemporary research and applications__1b42b3bd02](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/099c829a-0243-4fe5-b05c-5430198c48cb/resource) (`099c829a-0243-4fe5-b05c-5430198c48cb`)
- S34: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b36b5fc6-ae74-4c78-9840-c17a61d01a68/resource) (`b36b5fc6-ae74-4c78-9840-c17a61d01a68`)
- S32: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a888280b-73b2-4236-9d8f-461ce00488c8/resource) (`a888280b-73b2-4236-9d8f-461ce00488c8`)
- S43: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/da1abc4f-ca7c-4e05-a3b7-2d0a92bf6023/resource) (`da1abc4f-ca7c-4e05-a3b7-2d0a92bf6023`)
- S4: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2764701b-cdc4-444f-ad12-eaa9c42511a5/resource) (`2764701b-cdc4-444f-ad12-eaa9c42511a5`)
- S26: [轻金属基复合材料](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/94a78a75-90fd-46c1-b748-6752f36468fc/resource) (`94a78a75-90fd-46c1-b748-6752f36468fc`)
- S30: [analysis of mold flow and microstructures of die casting in al alloy sic__ef19863685](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9dd82928-448f-4a71-ba11-ebc2958b0c00/resource) (`9dd82928-448f-4a71-ba11-ebc2958b0c00`)
- S48: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3077460-6881-4484-b4c3-229adb9f49a0/resource) (`f3077460-6881-4484-b4c3-229adb9f49a0`)
- S17: [实用铝铜及其合金金相热处理和失效分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6eed09b6-599f-4ea6-bd0c-929cd1165df2/resource) (`6eed09b6-599f-4ea6-bd0c-929cd1165df2`)
- S18: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c0c3a85-4f51-4f08-8dfd-0c2f6b3641ed/resource) (`7c0c3a85-4f51-4f08-8dfd-0c2f6b3641ed`)
- S24: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/901f4416-2f24-4e85-b8d3-e9cded9122f8/resource) (`901f4416-2f24-4e85-b8d3-e9cded9122f8`)
- S13: [铝合金及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51084c8e-14c2-4e29-bd4e-3ba53601e7ea/resource) (`51084c8e-14c2-4e29-bd4e-3ba53601e7ea`)
- S44: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e08b09b4-1506-4b8e-87d0-22a4a1eebd17/resource) (`e08b09b4-1506-4b8e-87d0-22a4a1eebd17`)
- S39: [工程材料应用技术丛书轻合金及其工程应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c1d70704-7177-41e9-99d8-55de3f9dd18e/resource) (`c1d70704-7177-41e9-99d8-55de3f9dd18e`)
- S25: [工程材料应用技术丛书轻合金及其工程应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9356ee97-a25d-4682-862e-53fd985b79e3/resource) (`9356ee97-a25d-4682-862e-53fd985b79e3`)
- S45: [advanced materials in engineering applications__0b40dace28](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e16280e2-4391-4504-a000-9bf86eeb2b33/resource) (`e16280e2-4391-4504-a000-9bf86eeb2b33`)
- S31: [SiC_ZK60镁基复合材料制备加工工艺与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0a118bb-a3b2-4a0e-85b8-c728f6c0e245/resource) (`a0a118bb-a3b2-4a0e-85b8-c728f6c0e245`)
- S7: [低压铸造SiC_Al复合材料铸件的组织与性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/34bb2b59-9e48-4692-a1e6-9b019a218f6c/resource) (`34bb2b59-9e48-4692-a1e6-9b019a218f6c`)
- S12: [扫描速度700 mm/s下（Al₂O₃+SiC）颗粒混杂增强铝基复合材料打印态样品的TEM明场像](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/412f5aba-bf59-4603-bab2-650e956527b7/resource) (`412f5aba-bf59-4603-bab2-650e956527b7`)
- S37: [图2-2 搅拌铸造工艺：(b) 预分散超声辅助半固态搅拌铸造](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bcafd420-40c3-4837-9d82-164ed6c29302/resource) (`bcafd420-40c3-4837-9d82-164ed6c29302`)