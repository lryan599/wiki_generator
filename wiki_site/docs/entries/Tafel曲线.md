---
version: "v1"
generated_at: "2026-06-21T05:58:04+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 29
  source_quality_score: 0.88
  freshness_score: 0.76
  evidence_coverage_score: 1.0
---

## 概述

Tafel曲线，又称极化曲线，是表征金属材料耐腐蚀性能的核心电化学工具。它以半对数坐标绘制：纵坐标为电极电位，横坐标为对数电流密度[[S5,S13]]。通过分析Tafel曲线，可以直接获得材料的腐蚀电位（$E_{\text{corr}}$）和腐蚀电流密度（$i_{\text{corr}}$）等基础腐蚀参数，进而评估材料的瞬时腐蚀速率[[S13,S3]]。在压铸领域，该曲线广泛应用于评价压铸镁合金、铝合金等非铁合金的耐腐蚀性能，尤其是对比不同铸造工艺（如普通压铸、真空压铸、半固态压铸）对合金腐蚀行为的影响[[S24,S33,S16]]。

## 电化学基础

### Tafel方程

Tafel曲线的核心理论基础是Tafel方程，该方程描述了在强极化条件下，电极电位与外加电流密度之间的半对数线性关系。对阳极极化过程，其形式为：

$$E_{\text{appl}} = E_{\text{corr}} + \beta_a \log\left(i / i_{\text{corr}}\right)$$

对阴极极化过程，其形式为：

$$E_{\text{appl}} = E_{\text{corr}} - \beta_c \log\left(i / i_{\text{corr}}\right)$$

其中，$\beta_a$ 为阳极Tafel斜率，$\beta_c$ 为阴极Tafel斜率，二者均为正值常数，经验取值通常在 0.03 V 至 0.30 V 范围内[[S13,S6,S18]]。

### 极化曲线区域划分

典型的活性溶解类Tafel极化曲线可分为三个特征区域[[S11,S34,S5]]：

1.  **线性极化区（微极化区）**：位于腐蚀电位附近，极化过电位绝对值通常小于或等于 10 mV。在此区间，电位与电流密度呈严格线性关系，曲线斜率即为极化电阻（$R_p$）。该区域属于非破坏性测试区域，可对同一试样重复测量[[S8,S21,S35]]。

2.  **弱极化区**：介于线性极化区和强极化区之间。

3.  **强极化区（Tafel区）**：位于腐蚀电位两侧极化过电位绝对值大于 100 mV 的区间。在此区域，电位与电流密度的对数呈严格线性关系，该直线段称为 Tafel 直线[[S11,S34]]。钝化型金属体系的极化曲线还会额外包含过渡钝化区、稳定钝化区和过钝化区[[S5,S18]]。

### Tafel外推法

Tafel外推法是利用强极化区的Tafel直线来测定腐蚀电流密度和腐蚀电位的方法[[S2]]。其理论基础是混合电位理论：在自腐蚀电位下，金属阳极溶解反应电流与阴极还原反应电流数值相等、方向相反，净外测电流为零[[S6,S36]]。操作方法主要有两种[[S11,S22]]：

1.  将阳极Tafel直线和阴极Tafel直线的延长线相交，交点对应的横坐标值（反对数）即为腐蚀电流密度，交点对应的电位值即为腐蚀电位。
2.  分别将阳极或阴极的单条Tafel直线外推至与腐蚀电位 $E_{\text{corr}}$ 的水平直线相交，交点对应的电流即为腐蚀电流密度。

对于存在负差数效应的镁合金等特殊体系，通常仅采用阴极支Tafel直线进行外推，外推电位区间选择比腐蚀电位负 120 ~ 250 mV 的强阴极极化线性区[[S22,S38]]。

## 关键参数与耐蚀性解读

通过分析Tafel曲线可获得以下关键参数，它们共同反映了合金的耐腐蚀性能。

| 参数 | 符号 | 意义与解读 |
| :--- | :--- | :--- |
| 腐蚀电位 | $E_{\text{corr}}$ | 材料在特定环境中达到稳定腐蚀状态时的电极电位。对于活性溶解材料（如镁合金、铝合金），当腐蚀电流密度相当时，腐蚀电位越高，合金的热力学腐蚀倾向越小，耐蚀性越好[[S3]]。 |
| 腐蚀电流密度 | $i_{\text{corr}}$ | 对应于腐蚀电位的瞬时溶解电流密度。对于活性溶解材料，$i_{\text{corr}}$ 是评价耐蚀性的**首要参数**，其值越小，代表材料的均匀腐蚀速率越低[[S3,S13]]。该值可通过法拉第定律换算为均匀腐蚀速率[[S13,S30]]。 |
| 阳极/阴极Tafel斜率 | $\beta_a$, $\beta_c$ | 反映了阳极溶解和阴极还原过程的动力学特征，其数值大小与电极反应机理有关[[S13]]。 |
| 极化电阻 | $R_p$ | 在线性极化区测得的电位-电流曲线斜率，与腐蚀电流密度成反比关系，满足Stern-Geary公式：$i_{\text{corr}} = \frac{b_a b_c}{2.303(b_a + b_c) R_p}$。$R_p$ 值越大，耐蚀性越好[[S8,S21,S35]]。 |

## 测试条件、标准与规范

进行Tafel曲线测试通常采用三电极体系，由研究电极（工作电极）、辅助电极（通常为铂片）和参比电极（如饱和甘汞电极）组成[[S10,S17,S32]]。国际通用的相关标准主要包括：

*   **ASTM G59《动电位极化电阻测量标准规范》**：此标准规定了极化电阻测试的实验流程和设备校准方法。其核心要求包括：试样需用600目SiC水磨砂纸湿抛，并在抛光后1小时内启动试验；标准测试溶液为 1.0N H₂SO₄，测试温度控制在 $30 \\pm 1\\^\\circ\\text{C}$；扫描速率固定为 0.6 V/h ($\\pm 5\\%$)，从腐蚀电位负 30 mV 处开始阳极方向扫描，终止于腐蚀电位正 30 mV 处。该标准提供了Type 430铁素体不锈钢的标准参考曲线，合格的测试得到的极化电阻 $R_p$ 应在 6.11 ~ 12.27 Ω·cm² 的95%置信区间内[[S20,S32,S37]]。

*   **ASTM G102《电化学测量计算腐蚀速率及相关信息标准规范》**：此标准详细规定了如何将测得的腐蚀电流密度通过法拉第定律换算为质量损失速率和平均穿透深度腐蚀速率，并给出了极化电阻值换算为腐蚀速率的配套计算指南[[S35,S31]]。

对于不同合金体系，测试参数会有所调整。例如，316不锈钢在 0.1 mol/L NaCl 溶液中测试扫描速率推荐为 0.5 ~ 1 mV/s[[S17]]。对于镁合金，极化曲线测试的扫描速率建议控制在 0.2 ~ 1 mV/s[[S17]]。在室温（约 20°C）的 3.5 wt% NaCl 电解质中测试时，标准配置为铂片辅助电极、饱和甘汞参比电极、密封工作电极（暴露面积 1 cm²）[[S10]]。

## 在压铸领域的应用与案例分析

Tafel曲线是评价压铸合金耐腐蚀性能及其与微观组织关联性的有效手段。大量研究聚焦于不同压铸工艺对镁合金、铝合金腐蚀行为的影响。

### 压铸镁合金AZ91D的案例

AZ91D是应用最广泛的压铸镁合金之一，其耐蚀性研究是电化学表征的重点。

*   **工艺对比（普通压铸 vs. 真空压铸）**：一项针对真空压铸与普通压铸AZ91D镁合金轮毂的研究[[S24]]表明，在25°C、1.0 wt% NaOH溶液中，两种工艺成形的合金均呈现活性溶解状态。真空压铸试样的Tafel曲线位置相对左移，表明极化阻抗增大。

    **表1 不同成形方式AZ91D镁合金在1.0% NaOH溶液中的极化Tafel参数对比**
    （数据来源：[[S4,S24]]）
    | 成形方式 | 阳极Tafel斜率 $b_a$ / mV | 阴极Tafel斜率 $b_c$ / mV | 自腐蚀电位 $E_{\text{corr}}$ / mV | 自腐蚀电流密度 $i_{\text{corr}}$ / (μA·cm⁻²) |
    | :--- | :--- | :--- | :--- | :--- |
    | 真空压铸 | 491 | 288 | -664 | 63.1 |
    | 普通压铸 | 125 | 83 | -719 | 158.5 |

    关键结论：真空压铸试样的自腐蚀电位为 -664 mV，比普通压铸试样的 -719 mV **降低约 55 mV**；同时其自腐蚀电流密度为 63.1 μA·cm⁻²，远小于普通压铸的 158.5 μA·cm⁻²，表明真空压铸AZ91D的耐蚀性能显著提升[[S24,S4]]。

    ![不同压铸工艺下AZ91D镁合金在1.0%NaOH溶液中的Tafel极化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a89269a3-4146-4275-9935-9450c997a790/resource)
    *图：不同压铸工艺下AZ91D镁合金在1.0%NaOH溶液中的Tafel极化曲线[[S24]]。*

*   **微观组织影响机制**：耐蚀性的差异源于微观组织。普通压铸AZ91D中 Mg₁₇Al₁₂ (β相) 含量较高，作为电偶阴极加速了析氢腐蚀过程，导致其阴极极化度较低。相反，真空压铸工艺可降低铸件孔隙率、提升致密度、细化晶粒并减少第二相杂质含量，从而有效降低腐蚀电流密度并改变Tafel斜率，最终提升耐蚀性[[S24]]。

*   **其他铸造工艺对比**：半固态铸造AZ91D的耐蚀性也优于高压压铸AZ91D。在ASTM D1384饱和Mg(OH)₂ (pH 10.6) 溶液中，半固态铸造AZ91D的腐蚀电位更正、腐蚀电流密度更低。这是因为半固态工艺下，α相与β相的面积比以及两相的铝含量差异更小，削弱了电偶腐蚀效应[[S33,S29]]。高纯度压铸AZ91D在盐雾环境下的腐蚀速率甚至低于压铸铝合金A380，其极化测试结果表现为自腐蚀电位更负，但腐蚀电流密度更小[[S16]]。

### 其他压铸合金案例

*   **AM系列镁合金**：与高铝含量的AZ91D不同，AM50、AM60等低铝压铸镁合金在四硼酸钠缓冲溶液 (pH 9.7) 中可形成相对稳定的氧化/氢氧化物保护膜，其极化行为存在显著差异[[S1]]。
*   **压铸镁合金AZ91-DC**：在0.01 M NaCl (pH 9) 除氧环境下的极化测试显示，压铸态AZ91-DC的腐蚀电流密度可低至 $0.008 \\text{ A/m}^2$，优于常规铸造态合金[[S15]]。

## 局限性与注意事项

尽管Tafel外推法是测定瞬时腐蚀速率的经典方法，但其应用存在明确的局限性[[S38,S22,S2]]：

1.  **适用体系限制**：该方法严格要求极化曲线的阳极或阴极分支中至少有一支**完全受活化电荷转移控制**，且必须存在线性度良好的Tafel直线段。对于受浓差极化控制的体系，或在极化过程中触发新电极反应的体系，Tafel外推结果将严重失真[[S38,S2]]。

2.  **腐蚀形态假设**：Tafel外推法假设电极表面仅发生**均匀腐蚀**。若材料存在局部腐蚀（如点蚀、缝隙腐蚀），该方法失效[[S38]]。

3.  **无法反映长期腐蚀行为**：该法测得的 $i_{\text{corr}}$ 仅代表测试时刻的瞬时腐蚀速率，不能直接表征材料的长期腐蚀动力学[[S22,S12]]。

4.  **镁合金的特殊性**：镁合金存在负差数效应，导致其阳极极化行为不完全遵循Tafel规律，通常只能通过对阴极支进行外推来获取腐蚀速率[[S22,S38]]。

5.  **测试精度**：电极表面状态的变化会显著影响测试结果的精度[[S22]]。

因此，Tafel曲线的测量结果通常需要结合其他测试方法进行交叉验证，例如：利用电化学阻抗谱（EIS）获取极化电阻 $R_p$ 并通过Stern-Geary公式反算腐蚀电流密度，以及进行长时间静态浸泡失重试验对标校准[[S12]]。

## Sources
- S5: [Tafel 极化曲线图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14acbeab-34d6-4f48-aeab-7d4ce8943a9d/resource) (`14acbeab-34d6-4f48-aeab-7d4ce8943a9d`)
- S13: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/33a3f547-ef10-41aa-bffd-cb060f3cf0c8/resource) (`33a3f547-ef10-41aa-bffd-cb060f3cf0c8`)
- S3: [典型航空铝合金塑性成形与蠕变时效成形的工艺基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c2b2c57-626c-47d0-b6ff-dd999647999d/resource) (`0c2b2c57-626c-47d0-b6ff-dd999647999d`)
- S24: [TextNode7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a89269a3-4146-4275-9935-9450c997a790/resource) (`a89269a3-4146-4275-9935-9450c997a790`)
- S33: [塑性变形镁合金的腐蚀与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f29b1698-fab0-4aac-a0f3-bd05bb057f94/resource) (`f29b1698-fab0-4aac-a0f3-bd05bb057f94`)
- S16: [现代压力铸造技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59f7833a-cde4-4a1a-80e1-f56d2ece8ef0/resource) (`59f7833a-cde4-4a1a-80e1-f56d2ece8ef0`)
- S6: [corrosion resistance of metals and alloys__a7601d2bf6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1fb0872e-d072-4582-a6f0-2f66d8e8baf4/resource) (`1fb0872e-d072-4582-a6f0-2f66d8e8baf4`)
- S18: [熔盐电解镁锂合金](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6916190f-d891-4287-aa8f-0f00b0099e80/resource) (`6916190f-d891-4287-aa8f-0f00b0099e80`)
- S11: [塑性变形镁合金的腐蚀与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d17b7e3-3832-46be-95fe-22091fba1390/resource) (`2d17b7e3-3832-46be-95fe-22091fba1390`)
- S34: [塑性变形镁合金的腐蚀与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f50687e8-4a7f-4ade-828d-e3092b3aff85/resource) (`f50687e8-4a7f-4ade-828d-e3092b3aff85`)
- S8: [电镀测试分析技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24a58c85-8d94-4821-b90b-9ec478be19d2/resource) (`24a58c85-8d94-4821-b90b-9ec478be19d2`)
- S21: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/803f4771-bde5-4fca-a530-4db9c32262ea/resource) (`803f4771-bde5-4fca-a530-4db9c32262ea`)
- S35: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f512d38e-3cdc-44d4-bc72-fdf8bf22d102/resource) (`f512d38e-3cdc-44d4-bc72-fdf8bf22d102`)
- S2: [铝合金舰艇腐蚀控制技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08dc2ba7-7961-4830-811b-f4a731b790a9/resource) (`08dc2ba7-7961-4830-811b-f4a731b790a9`)
- S36: [塑性变形镁合金的腐蚀与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f7d27db9-063c-4f21-95a3-841846393f25/resource) (`f7d27db9-063c-4f21-95a3-841846393f25`)
- S22: [塑性变形镁合金的腐蚀与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87a3e7e4-d126-4678-9b48-31f010d1689b/resource) (`87a3e7e4-d126-4678-9b48-31f010d1689b`)
- S38: [ap65镁合金的电化学行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fca4ad42-313d-4c1c-a34d-1fd3a773cc32/resource) (`fca4ad42-313d-4c1c-a34d-1fd3a773cc32`)
- S30: [7466815_腐蚀率](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d6fc4a3b-ab2b-46b2-b67b-edcb991400fa/resource) (`d6fc4a3b-ab2b-46b2-b67b-edcb991400fa`)
- S10: [制冷管铝材中典型夹杂物形成机制及其腐蚀行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cad6eca-1715-45a9-8ada-a91b30cca931/resource) (`2cad6eca-1715-45a9-8ada-a91b30cca931`)
- S17: [塑性变形镁合金的腐蚀与防护](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60d3128e-258a-469a-900f-42410a8643f3/resource) (`60d3128e-258a-469a-900f-42410a8643f3`)
- S32: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eaf77241-f202-4688-b553-897e990a3884/resource) (`eaf77241-f202-4688-b553-897e990a3884`)
- S20: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75598c63-9148-4f78-bfad-9dbdc9a7146e/resource) (`75598c63-9148-4f78-bfad-9dbdc9a7146e`)
- S37: [1988 annual book of astm standards section 3 metals test methods and ana__0c5053198e](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f99197c8-6263-4a00-ae64-3b15088af6b3/resource) (`f99197c8-6263-4a00-ae64-3b15088af6b3`)
- S31: [1991 annual book of astm standards section 3 metals test methods and analytical procedures volume 0302 wear and erosi...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d97c95f8-e44f-4b26-8db1-43aada795173/resource) (`d97c95f8-e44f-4b26-8db1-43aada795173`)
- S4: [表 4 不同成型方式 AZ91D 镁合金试样的极化 Tafel 参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e74e96e-5914-448b-bcb8-d89225b4b18f/resource) (`0e74e96e-5914-448b-bcb8-d89225b4b18f`)
- S29: [不同镁及AZ91D合金在ASTM D1384溶液中的腐蚀参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2be2ce2-e180-4913-9124-34dd100efb60/resource) (`d2be2ce2-e180-4913-9124-34dd100efb60`)
- S1: [corrosion behaviuor of stressed magnesium alloys__0479093b8f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0411eb01-5020-480a-a7bb-afa5ed6a642d/resource) (`0411eb01-5020-480a-a7bb-afa5ed6a642d`)
- S15: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4c38926f-05ea-4f38-9801-83d98d6e3394/resource) (`4c38926f-05ea-4f38-9801-83d98d6e3394`)
- S12: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30ba113f-9a66-429e-8bed-90edb16f14dc/resource) (`30ba113f-9a66-429e-8bed-90edb16f14dc`)