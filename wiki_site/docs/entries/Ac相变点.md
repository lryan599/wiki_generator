---
version: "v1"
generated_at: "2026-06-19T04:58:56+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 35
  source_quality_score: 0.88
  freshness_score: 0.73
  evidence_coverage_score: 1.0
---

## 概述

Ac相变点是钢铁材料在非平衡加热条件下发生组织转变的临界温度[[S7,S14,S36]]。该命名由法国冶金学家F. Osmond提出，Ac源自法语“arret chauffage”（加热停滞）的缩写[[S7,S14,S36]]。在实际生产中，钢的加热和冷却并不是极缓慢的平衡过程，因此实际发生相变的温度会偏离Fe-Fe₃C平衡相图中的理论临界点，加热时移向高温，冷却时移向低温，这一现象称为“滞后”[[S14,S17,S20]]。为区别于平衡转变温度，通常将加热时的实际临界温度用Ac₁、Ac₃、Acm表示，冷却时的实际临界温度用Ar₁、Ar₃、Arcm表示[[S14,S17,S22]]。

Ac相变点构成了钢铁热处理工艺的核心温度基准，尤其在压铸模具钢的淬火、回火、焊补预热及失效分析中起着不可替代的作用[[S24,S25,S23]]。

![Fe-Fe₃C相图中平衡临界线与实际加热冷却临界线的位置关系示意图，清晰标注了Ac系列相变点相对于平衡A系列的温度偏移](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10d785c5-9c7a-4db8-941c-3c822835730a/resource) [[S3]]

## 定义与分类

### 基本定义

Ac相变点是钢铁在连续加热过程中，当温度超过平衡临界温度时发生扩散型相变的实际起始或终了温度[[S20,S36]]。与平衡相图的临界点相比，各Ac点的物理含义如下：

- **Ac₁**：加热时珠光体向奥氏体转变的开始温度，高于平衡点A₁（727℃）[[S20,S38,S22]]；
- **Ac₃**：加热时先共析铁素体全部溶入奥氏体的终了温度，高于平衡相图A₃线[[S20,S38]]；
- **Acm**（亦称Accm）：加热时二次渗碳体全部溶入奥氏体的终了温度，高于平衡相图Acm线[[S20,S22]]。

### 按钢种分类

不同碳含量的钢在加热时所涉及的Ac相变点类型不同[[S33,S30,S10]]：

| 钢种 | 碳质量分数 w(C) | 涉及的Ac相变点 | 加热时的组织转变特征 |
|:---|:---|:---|:---|
| 亚共析钢 | < 0.77% | Ac₁、Ac₃ | 加热至Ac₁以上珠光体转变为奥氏体，继续加热至Ac₃时先共析铁素体全部溶入奥氏体，得到单相奥氏体 |
| 共析钢 | ≈ 0.77% | Ac₁ | 加热至Ac₁以上即可完成珠光体向奥氏体的完全转变 |
| 过共析钢 | > 0.77% | Ac₁、Acm | 加热至Ac₁以上珠光体开始转变为奥氏体，继续加热至Acm时二次渗碳体全部溶入奥氏体，得到单相奥氏体 |

![钢铁材料加热与冷却过程的真实温度-时间曲线，左侧加热曲线上清晰标注了Ac₁(730℃)和Ac₃(885℃)的具体位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23a52662-c63e-4aff-87ff-01414fe90941/resource) [[S8]]

## 核心属性

### 化学成分的影响

化学成分对Ac相变点数值有显著影响[[S9,S38]]。合金元素通过改变钢的相变动力学来调整Ac点的位置：
- 稳定奥氏体的元素（如Mn、Ni）会降低Ac₁和Ac₃温度；
- 稳定铁素体或形成碳化物的元素（如Si、Cr、V、Mo、W）会升高Ac₁和Ac₃温度[[S9]]。

Andrews通过大量实验数据的回归分析，提出了定量计算合金元素对Ac₁和Ac₃影响的经典经验公式[[S9,S36]]：

$$
A_{c_3} = 910 - 203\sqrt{w(\mathrm{C})} - 15.2w(\mathrm{Ni}) + 44.7w(\mathrm{Si}) + 104w(\mathrm{V}) + 31.5w(\mathrm{Mo}) + 13.1w(\mathrm{W})
$$

$$
A_{c_1} = 723 - 10.7w(\mathrm{Mn}) - 16.9w(\mathrm{Ni}) + 29.1w(\mathrm{Si}) + 16.9w(\mathrm{Cr}) + 290w(\mathrm{As}) + 6.38w(\mathrm{W})
$$

### 加热速度的影响

加热速度对Ac相变点有决定性影响：加热速度越快，相变所需的过热度越大，Ac相变点整体数值越高[[S16,S17,S36]]。实验研究表明[[S16]]：
- 即使以10⁷℃/s的极高速率加热，Ac₁起始温度（Ac₁s）也仅升高至约840℃；
- 但加热速度对转变终了温度（Ac₁f）影响极为显著：加热速度为10²℃/s时Ac₁f约为950℃，10⁵℃/s时升至1050℃，10⁶℃/s时可升至约1100℃[[S16]]。

这一规律说明在高速感应加热等场合，Ac点的实际数值将大幅偏离平衡临界温度，热处理工艺制定时必须予以充分考虑。

## 工艺作用与规范

### 淬火加热温度的确定

在压铸模具钢热处理中，淬火加热温度的制定必须以对应牌号的实测Ac₃或Ac₁为核心判据[[S24,S1]]。亚共析钢如H13（4Cr5MoSiV1）的淬火加热温度必须高于Ac₃，以保证完全奥氏体化；过共析钢的淬火加热温度通常选择在Ac₁以上、Acm以下，以保留适量未溶碳化物控制晶粒尺寸[[S24,S10]]。

各牌号压铸模具钢的Ac相变点实测数据及推荐淬火温度范围如下：

| 牌号 | Ac₁ (℃) | Ac₃/Acm (℃) | Ms (℃) | 典型应用场合 | 数据来源 |
|:---|:---|:---|:---|:---|:---|
| H13 / 4Cr5MoSiV1 | 850～860 | 910～915 | 335～340 | 铝/镁合金压铸模 | [[S2,S21,S41]] |
| 3Cr2W8V | ≈830 | ≈930 | ≈370 | 铜合金压铸模 | [[S42]] |
| Y4 (4Cr3Mo2MnVNbB) | ≈789 | ≈910 | ≈263 | 铜合金压铸模 | [[S35]] |
| Y10 (4Cr5Mo2MnVSi) | ≈815 | ≈893 | ≈271 | 铝合金压铸模 | [[S35]] |

### 回火温度的限制

压铸模具钢回火温度必须严格控制在实测Ac₁以下，以避免基体组织在回火过程中发生非预期的奥氏体相变[[S24]]。常用热作模具钢如H13的回火温度区间为550～650℃，远低于其Ac₁（约860℃），确保回火过程中仅发生马氏体的分解和碳化物的析出而不重新奥氏体化[[S1]]。

## 相关关系与体系

### 与Ar冷却相变点的关系

Ac加热相变点与Ar冷却相变点共同构成钢的非平衡相变温度体系[[S20,S22,S28]]。两者的基本位置关系为[[S7,S14,S40]]：

- Ac₁ > 平衡A₁ > Ar₁
- Ac₃ > 平衡A₃ > Ar₃
- Acm > 平衡Acm > Arcm

这一滞后现象的根本原因在于珠光体⇌奥氏体相变属于扩散型相变，需要一定的过热度或过冷度提供相变驱动力[[S9,S36]]。

### 与Ms、Mf点的关系

完整的钢加热-冷却相变临界温度体系从高温到低温依次排列为：Ac₄（δ→γ）→ Ac₃ → Acm → Ac₁ → Ar₁ → Ar₃ → Arcm → Ms（马氏体开始转变点）→ Mf（马氏体转变完成点）[[S7,S28]]。Ac系列各点温度均显著高于Ms点，以H13钢为例：Ac₁=840～860℃、Acm/Accm=940℃、Ms=320～340℃[[S4,S15,S2]]。

### 加热-冷却相变体系总览

![钢的Fe-Fe₃C相图局部，完整标注了三条平衡临界线A₁、A₃、Acm及加热临界线Ac₁、Ac₃、Acm、冷却临界线Ar₁、Ar₃、Arcm，直观显示Ac线均位于平衡线上方](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50c51961-aeab-4936-beb4-d0556aa2adbe/resource) [[S13]]

## 缺陷机制

若淬火加热温度未正确参考Ac相变点，将导致一系列组织缺陷：

**加热不足（欠热）**：淬火加热温度低于Ac₃且保温时间不足时，珠光体未充分溶解、奥氏体成分不均匀。亚共析钢组织中将残存铁素体，淬火后出现软点、硬度分布不均；过共析钢基体碳浓度不够，淬火后硬度不足、淬透层深度不足[[S27,S11,S5]]。

**过热与过烧**：加热温度远超Ac₃上限时，奥氏体晶粒将快速粗化[[S27,S26]]。严重时出现晶界氧化或局部熔化（过烧），淬火开裂倾向显著增大，模具冲击韧性大幅下降，过烧为不可逆的致命缺陷[[S27]]。

## 应用场景

**模具焊补预热温度确定**：压铸模具焊补前的预热温度必须严格控制在实测Ac₁以下，以避免焊补热输入导致局部区域发生组织相变，产生额外组织应力引发焊补裂纹[[S6]]。

**量产热处理工艺文件制定**：所有压铸模具量产热处理工艺文件的温度区间设置必须以对应牌号的实测Ac₁、Ac₃数值为基准，杜绝工艺参数随意设定引发的批量模具报废风险[[S25]]。

**模具失效分析中的工艺合规性判定**：解剖失效模具试样检测金相组织，对比标准Ac点对应的相变组织特征，可精准反推热处理实际加热温度是否偏离合理控制区间，判定前期热处理工艺执行是否合规[[S23]]。

## 局限性

Ac相变点的定义基础是Fe-C二元体系中铁的同素异构转变（体心立方⇌面心立方）以及珠光体向奥氏体的扩散型相变过程[[S14,S20]]。因此，Ac相变点**仅适用于钢铁材料体系**，不适用于铝、锌、镁等非铁压铸合金[[S37,S39]]。非铁合金不存在此类固态相变机制，没有对应定义的Ac相变点，其热处理状态采用完全不同的相变体系（如固溶、时效等）进行描述。

## Sources
- S7: [a hundred years of metallurgy__4ffafa7bed](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/217c72ee-d869-4d8d-87fd-765918f20766/resource) (`217c72ee-d869-4d8d-87fd-765918f20766`)
- S14: [工程材料与加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51828d90-0cbc-4bd6-9a3c-f8a0294104f6/resource) (`51828d90-0cbc-4bd6-9a3c-f8a0294104f6`)
- S36: [材料加工工程科技英语](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5d8a8a1-c8ab-45db-8952-3736ec79283f/resource) (`e5d8a8a1-c8ab-45db-8952-3736ec79283f`)
- S17: [金属材料及其成形加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/579d0186-b7ca-44af-a989-f7ea9547502e/resource) (`579d0186-b7ca-44af-a989-f7ea9547502e`)
- S20: [材料加工原理及工艺学无机非金属材料和金属材料分册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/77842660-e418-4b39-a115-b683873a7812/resource) (`77842660-e418-4b39-a115-b683873a7812`)
- S22: [工程材料与热加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d088d0c-ba22-477d-ae72-a61f139c9865/resource) (`8d088d0c-ba22-477d-ae72-a61f139c9865`)
- S24: [基于ProCAST铝合金压铸模热疲劳缓解机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/922ea530-6da6-4485-ad52-9629d964b98a/resource) (`922ea530-6da6-4485-ad52-9629d964b98a`)
- S25: [压铸技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9661e3a6-1b11-4f96-aa62-63d28dbfa720/resource) (`9661e3a6-1b11-4f96-aa62-63d28dbfa720`)
- S23: [压铸模失效方式探讨](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/906cddae-ddd8-4972-bc2c-05f16e144256/resource) (`906cddae-ddd8-4972-bc2c-05f16e144256`)
- S3: [Fe-Fe₃C相图共析反应部分，标注钢的平衡与实际临界温度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10d785c5-9c7a-4db8-941c-3c822835730a/resource) (`10d785c5-9c7a-4db8-941c-3c822835730a`)
- S38: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/efa219d0-ceae-47d8-a399-2a7598db650d/resource) (`efa219d0-ceae-47d8-a399-2a7598db650d`)
- S33: [金属材料及其成形性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd92d411-f156-42ae-9df4-4136f2923ff2/resource) (`cd92d411-f156-42ae-9df4-4136f2923ff2`)
- S30: [模具制造基础知识](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a15d815c-8f76-44d2-9dab-d23d13888039/resource) (`a15d815c-8f76-44d2-9dab-d23d13888039`)
- S10: [实用模具材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c977fce-3467-423c-8c66-b6a95fa460da/resource) (`2c977fce-3467-423c-8c66-b6a95fa460da`)
- S8: [钢铁加热与冷却相变温度图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/23a52662-c63e-4aff-87ff-01414fe90941/resource) (`23a52662-c63e-4aff-87ff-01414fe90941`)
- S9: [材料加工工程科技英语](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25bc91b3-8444-4336-9958-acaf28e65269/resource) (`25bc91b3-8444-4336-9958-acaf28e65269`)
- S16: [表面改性热处理技术与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5723b8fd-9666-401a-98e1-350501cdd845/resource) (`5723b8fd-9666-401a-98e1-350501cdd845`)
- S1: [工模具材料强化处理应用技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00bd9d52-1b18-4c85-979f-fd60036a6980/resource) (`00bd9d52-1b18-4c85-979f-fd60036a6980`)
- S2: [模具材料及表面强化处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0992cc81-ed39-44dd-adca-898444e4808f/resource) (`0992cc81-ed39-44dd-adca-898444e4808f`)
- S21: [4Cr5MoSiV1钢的临界点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7dc9d85e-1371-4f76-bc5d-ada7e14101a8/resource) (`7dc9d85e-1371-4f76-bc5d-ada7e14101a8`)
- S41: [工模具材料强化处理应用技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fca92532-96cf-4c31-bbc4-085b198dfb1d/resource) (`fca92532-96cf-4c31-bbc4-085b198dfb1d`)
- S42: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff41bf26-faa5-46ca-b32d-06e031dd0e78/resource) (`ff41bf26-faa5-46ca-b32d-06e031dd0e78`)
- S35: [实用模具材料应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e5d1fccc-0dbd-43a5-8370-7f1f63612e35/resource) (`e5d1fccc-0dbd-43a5-8370-7f1f63612e35`)
- S28: [模具材料及其热处理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9d8c1f54-be2b-4502-90b3-e62e912eeb7d/resource) (`9d8c1f54-be2b-4502-90b3-e62e912eeb7d`)
- S40: [图4-2 实际加热（冷却）时，Fe-Fe3C相图上各相变点的位置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb7d8349-6169-4b06-ad46-dd61d18564a6/resource) (`fb7d8349-6169-4b06-ad46-dd61d18564a6`)
- S4: [图2-2 H13钢的CCT曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11acaaf8-dba9-4a17-872a-74423a72db6c/resource) (`11acaaf8-dba9-4a17-872a-74423a72db6c`)
- S15: [图2-3 H13钢的TTT曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5623e4a5-65a0-4fff-a567-be74086f1804/resource) (`5623e4a5-65a0-4fff-a567-be74086f1804`)
- S13: [钢在加热和冷却时临界点的位置示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/50c51961-aeab-4936-beb4-d0556aa2adbe/resource) (`50c51961-aeab-4936-beb4-d0556aa2adbe`)
- S27: [机械工程材料与加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ad227d0-717a-4fc7-8e44-7d9e29812e80/resource) (`9ad227d0-717a-4fc7-8e44-7d9e29812e80`)
- S11: [材料热处理与表面工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/434919b8-cdc1-4b8a-b17b-b5891ed937f4/resource) (`434919b8-cdc1-4b8a-b17b-b5891ed937f4`)
- S5: [表面改性热处理技术与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11ead60c-c362-457e-9868-6e86640394f3/resource) (`11ead60c-c362-457e-9868-6e86640394f3`)
- S26: [工程材料与加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99f775a1-764f-4ddb-bda0-119512fd88c3/resource) (`99f775a1-764f-4ddb-bda0-119512fd88c3`)
- S6: [压铸冶金学](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/187562c0-a215-4bad-bf2e-2ef0e796b369/resource) (`187562c0-a215-4bad-bf2e-2ef0e796b369`)
- S37: [实用模具材料手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8394212-0a4e-4dd0-9dbf-1832e4f25407/resource) (`e8394212-0a4e-4dd0-9dbf-1832e4f25407`)
- S39: [中外有色金属及合金铸件标准](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f494169a-6e51-41f4-ad12-398dad24d2f8/resource) (`f494169a-6e51-41f4-ad12-398dad24d2f8`)