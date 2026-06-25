---
version: "v1"
generated_at: "2026-06-18T12:24:23+00:00"
confidence_score: 0.85
confidence_level: "high"
confidence_basis:
  cited_sources: 33
  source_quality_score: 0.84
  freshness_score: 0.8
  evidence_coverage_score: 1.0
---

## 概述

Coffin-Manson方程是低周疲劳（Low Cycle Fatigue, LCF）领域最基本的唯象寿命预测模型，描述了材料在塑性应变主导的疲劳工况下，塑性应变幅与疲劳失效寿命之间的定量关系。该方程由L. F. Coffin Jr.于1954年[[S16,S23,S28]]和S. S. Manson于1953—1954年[[S1,S28]]分别独立提出，后被广泛命名为Coffin-Manson关系式或Manson-Coffin关系式。方程适用于失效循环数N<sub>f</sub>处于10²~10⁴区间的低周疲劳范畴[[S4,S3,S12,S21]]，在压铸模具热疲劳寿命预测中具有核心地位。

## 标准数学表达式

### 经典Coffin-Manson形式

经典模型将塑性应变幅与疲劳失效循环反向次数以幂律形式关联[[S28]]：

$$\frac{\Delta\varepsilon_p}{2} = \varepsilon_f'(2N_f)^c$$

式中，Δε<sub>p</sub>/2为塑性应变幅，ε<sub>f</sub>'为疲劳延性系数，c为疲劳延性指数，2N<sub>f</sub>为失效时的总载荷反向次数（1个完整拉压循环对应2次载荷反向，因此2N<sub>f</sub> = 2N<sub>f</sub>）[[S12,S28,S18]]。

### 全应变-寿命形式（Basquin-Coffin-Manson方程）

将Coffin-Manson塑性应变项与Basquin弹性应变项叠加，得到覆盖低周至高周疲劳区间的总应变幅-寿命方程[[S28,S12,S24,S30]]：

$$\frac{\Delta\varepsilon_t}{2} = \frac{\Delta\varepsilon_e}{2} + \frac{\Delta\varepsilon_p}{2} = \frac{\sigma_f'}{E}(2N_f)^b + \varepsilon_f'(2N_f)^c$$

式中σ<sub>f</sub>'为疲劳强度系数，E为弹性模量，b为疲劳强度指数。弹性项主导长寿命（高周疲劳）区间，塑性项主导短寿命（低周疲劳）区间[[S12,S18]]。

### 对数线性形式

对核心幂律式取双对数后得到线性关系，是试验数据拟合参数的标准方法[[S12,S18,S19]]：

$$\lg(\Delta\varepsilon_p/2) = \lg(\varepsilon_f') + c \cdot \lg(2N_f)$$

在双对数坐标系中，斜率c即为疲劳延性指数，截距lg(ε<sub>f</sub>')即为疲劳延性系数的对数值[[S12]]。

## 关键参数解读

| 参数符号 | 名称 | 物理意义 | 典型取值范围 | 获取方法 |
|:---:|:---:|:---|:---:|:---|
| Δε<sub>p</sub>/2 | 塑性应变幅 | 单次循环中塑性应变范围的二分之一，反映循环塑性变形程度 | 0.0002–0.04（压铸模具钢）[[S34,S9,S10,S15]] | 从稳定迟滞回线提取[[S25,S17]] |
| ε<sub>f</sub>' | 疲劳延性系数 | 无量纲，近似等于材料单轴拉伸真断裂延性ε<sub>f</sub> | 0.35–0.69（压铸模具钢）[[S34,S15,S10,S1]] | 应变控制低周疲劳试验双对数拟合截距[[S25]] |
| c | 疲劳延性指数 | 无量纲，表征塑性应变幅随寿命增加而下降的速率 | −0.5~−0.7（通用工程约定）[[S1,S4,S17]]；−0.5~−1.0（部分文献）[[S12]] | 应变控制低周疲劳试验双对数拟合斜率[[S12,S18]] |
| 2N<sub>f</sub> | 载荷反向次数 | 疲劳失效前经历的载荷反向总次数，等于失效循环次数N<sub>f</sub>的2倍 | — | 试验实测失效判据对应的循环反向数[[S28,S12]] |

### 参数获取的标准试验方法

Coffin-Manson参数的获取遵循ASTM E606[[S25]]等应变控制低周疲劳试验规范：采用轴向加载，应变比R=−1，加载波形为三角形波，试验频率控制在0.1~1 Hz，以试样完全断裂或最大应力下降25%作为失效判据。采集不同总应变幅下的半寿命周期稳定迟滞回线，分离得到塑性应变幅Δε<sub>p</sub>/2，通过双对数坐标线性拟合得到ε<sub>f</sub>'和c[[S25,S17]]。

## 在压铸模具钢热疲劳中的应用

### 热疲劳机理与低周疲劳适配性

压铸模具服役过程中，每经历一次充型-冷却循环，型腔表面材料在高温热胀受约束时产生压塑性应变，激冷收缩时受拉，循环往复导致表面塑性应变不断累积，最终触发热疲劳裂纹。该类失效循环次数通常为数百至数万次，属于典型的低周疲劳范畴[[S4,S11]]。在锌合金压铸中，由于模具工作温度较低，定性为低温高周疲劳；铝合金和铜合金压铸则应定性为高温低周疲劳[[S34]]。各类合金对应模具的失效形式[[S33]]如下：

| 压铸合金 | 主要失效形式 |
|:---:|:---|
| 锌合金 | 热浸蚀、热磨损 |
| 铝合金 | 热疲劳、开裂断裂 |
| 铜合金 | 热疲劳、变形 |

### 工程推导式

针对压铸场景，可由Coffin-Manson基础形式推导出直接使用工艺参数的寿命计算公式[[S2,S32,S34]]：

$$N_F = \left[ \frac{C \cdot \varepsilon_f}{\alpha(T_2 - T_1) - \frac{(1-\mu_1)}{E_1}\sigma_1 - \frac{(1-\mu_2)}{E_2}\sigma_2} \right]^{1/n}$$

式中，α为模具材料热膨胀系数，T₁、T₂分别为模具表层最低、最高工作温度，μ₁、μ₂与E₁、E₂为对应温度下的泊松比和弹性模量，σ₁、σ₂为对应温度下的屈服强度，C和n为材料常数（一般n=0.5，C取值范围−0.5~−0.7）[[S2,S4,S17]]。

### 平均应力修正（Morrow修正）

当压铸循环存在非对称应力时，可采用Morrow修正公式引入平均应力σ<sub>m</sub>的影响[[S13,S35,S26,S18]]：

$$\frac{\Delta\varepsilon_t}{2} = \frac{\sigma_f' - \sigma_m}{E}(2N_f)^b + \varepsilon_f'(2N_f)^c$$

该修正可有效提升非对称应力循环工况下的寿命预测精度[[S35]]。

### 高温蠕变-疲劳交互作用

压铸模具在长时间高温服役时，蠕变损伤不可忽视。工程上采用线性叠加模型，分别计算疲劳损伤累积项与蠕变损伤累积项，求和得到总损伤[[S35,S11]]：

$$\sum_{i=1}^{n_1}\frac{N_{经i}}{N_i} + \sum_{j=1}^{n_2}\frac{t_{经j}}{t_j} = \frac{H}{L}$$

## 名称使用习惯

北美地区主流工程文献普遍使用“Coffin-Manson”命名，欧洲大陆及部分高温蠕变研究文献倾向于使用“Manson-Coffin”的表述顺序[[S30]]。二者含义完全等同，均为描述塑性应变幅与低周疲劳寿命关系的同一经典理论，检索时不应刻意区分。

## 应变-寿命曲线及其含义

![图1 应变-寿命（ε-N）曲线示意图，横坐标为载荷反向次数的对数lg2Nf，纵坐标为应变幅的对数。弹性应变线（Basquin，斜率b）与塑性应变线（Coffin-Manson，斜率c）叠加形成总应变线，交点对应转变寿命2Nt。](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/385e99d5-746b-4668-b0a0-2b8e75cd1b02/resource)

在双对数坐标系中，Coffin-Manson塑性应变线为一条直线，其斜率为疲劳延性指数c（典型范围−0.5~−1.0），纵轴截距为lg(ε<sub>f</sub>')[[S12,S29,S6]]。弹性应变线（Basquin）斜率b典型值范围为−0.05~−0.15，截距为σ<sub>f</sub>'/E[[S12]]。两条直线的交点对应转变疲劳寿命2N<sub>t</sub>[[S12,S28]]：寿命低于此值时，疲劳抗力由材料延性主导（塑性应变占优，适用Coffin-Manson项）；寿命高于此值时，由材料强度主导（弹性应变占优，适用Basquin项）[[S12]]。

## 压铸模具钢Coffin-Manson参数数据

### H13钢及其改性钢

| 材料 | 温度区间（℃） | Δε<sub>p</sub>/2 | ε<sub>f</sub>' | c | 数据来源 |
|:---|:---:|:---:|:---:|:---:|:---:|
| H13（标准） | 室温~600 | 0.00022~0.03 | 0.69 | −0.5 | S34 |
| H13Nb2（含铌微合金化） | 室温~700 | 0.01~0.04 | 0.45 | −0.5~−0.6 | S9 |
| 4Cr5MoSiV1（国产H13对应） | 200~600 | 0.0005~0.03 | 0.5~0.65 | −0.5~−0.65 | S10 |

### Cr-Mo-V系热作模具钢

| 材料 | 温度区间（℃） | Δε<sub>p</sub>/2 | ε<sub>f</sub>' | c | 数据来源 |
|:---|:---:|:---:|:---:|:---:|:---:|
| Cr-Mo-V热作模具钢（ASSAB 8407S等） | 360~650 | 0.001~0.025 | 0.35~0.6 | −0.6~−0.7 | S15 |

### TMF工况下H13钢的BCM模型标定数据

在热机械疲劳（TMF）条件下，基于H13钢数据的Basquin-Coffin-Manson模型拟合结果为[[S24]]：

- **IP-TMF（同相）**：σ<sub>f</sub>' = 31680.818 MPa，b = −0.6042，ε<sub>f</sub>' = 0.05605，c = −0.4164
- **OP-TMF（反相）**：σ<sub>f</sub>' = 1412.108 MPa，b = −0.15461，ε<sub>f</sub>' = 2.08415，c = −0.98669

以上结果表明，相同材料在不同相位加载条件下的Coffin-Manson参数存在显著差异，对压铸热循环寿命预测时需针对性选用[[S24]]。

- 含铌微合金化H13Nb2钢的热疲劳损伤因子增长最慢，普通H13钢损伤增长最快，反映其疲劳寿命存在明显梯度差异[[S8]]。不同奥氏体化温度下的冲击韧性测试同样表明H13Nb2的最优塑性表现[[S14]]，为疲劳延性系数的取值提供了材质依据。

## 工程应用案例

### 案例一：铝合金导轮压铸模

采用经典Coffin-Manson（CM）模型预测铝合金导轮压铸模具寿命为184747模次，而该模具实际在41808模次时出现热疲劳裂纹需要修补，表明经典CM模型对压铸热疲劳寿命的预测偏于安全且存在较大偏差，需结合温度修正[[S13,S20]]。

### 案例二：四点关联法寿命估算

利用四点关联法获取材料疲劳参数，结合Coffin-Manson方程对铝合金压铸模进行寿命预测，得到理论寿命约100000模次[[S36]]。四点关联法各经验公式如下[[S36]]：

$$b = -0.083 - 0.166 \cdot \lg(\sigma_f/\sigma_b)$$
$$\sigma_f' = \frac{9}{8}\sigma_b(\sigma_f/\sigma_b)^{0.9}$$
$$c = -0.52 - \frac{1}{4}\lg\varepsilon_f + \frac{1}{3}\lg\left[1 - 82\left(\frac{\sigma_b}{E}\right)\left(\frac{\sigma_f}{\sigma_b}\right)^{0.179}\right]$$
$$\varepsilon_f' = 0.827 \cdot \varepsilon_f \left[1 - 82\left(\frac{\sigma_b}{E}\right)\left(\frac{\sigma_f}{\sigma_b}\right)^{0.179}\right]^{-1/3}$$

### 案例三：ProCAST-Abaqus-FE-safe联合仿真

采用ProCAST模拟压铸热平衡阶段温度场，将温度结果导入Abaqus计算热应力场，再将应力结果导入FE-safe软件代入Coffin-Manson模型计算寿命，所得低寿命危险区与实际生产中模具热疲劳裂纹萌生位置完全吻合，验证了该联合仿真流程的有效性[[S38]]。

### 案例四：激光熔覆涂层压铸模

对不同激光熔覆涂层的铝合金压铸模，代入相应的材料性能参数，采用修正Coffin-Manson模型计算得到[[S27]]：单一Ni60涂层模具热疲劳寿命为840000次，Ni60+TiC复合涂层为1400000次，Ni60+Al₂O₃复合涂层为1600000次，与覆层模具实际服役寿命提升规律完全匹配。

## 适用条件与局限性

1. **低周疲劳范围**：方程适用于N<sub>f</sub> ≈ 10²~10⁴次的低周疲劳区间，此时塑性应变在总应变中占比显著[[S4,S1,S3]]。超越此范围进入高周疲劳区间时，弹性应变项（Basquin）占主导地位，应使用全应变-寿命形式。

2. **高温蠕变-疲劳交互作用**：经典Coffin-Manson方程本身为单轴等温疲劳模型，不直接覆盖蠕变损伤。高温服役（如铝/铜合金压铸）须采用线性叠加模型或蠕变-疲劳交互修正[[S35,S11]]。

3. **温度依赖性**：Coffin-Manson参数（ε<sub>f</sub>'、c）与试验温度和循环频率密切相关，而压铸热疲劳工况下温度时刻波动，选取合适的等效温度参数是一大难点[[S1]]。

4. **材料延性依赖**：疲劳延性系数ε<sub>f</sub>'近似等于单轴拉伸真断裂延性ε<sub>f</sub>[[S1]]，因此材料塑性越好则低周疲劳抗力越优。弹性-塑性转变寿命以下由延性主导[[S12]]。

5. **平均应力影响**：基础Coffin-Manson方程基于对称循环（R=−1）假设。存在非零平均应力的工况需采用Morrow修正或其他应力修正模型[[S13,S35,S18]]。

## Sources
- S16: [achievement of high fatigue resistance in metals and alloys stp 467__5d030dc5bf](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92acbb5e-6840-41ea-bbb7-d809e089b67c/resource) (`92acbb5e-6840-41ea-bbb7-d809e089b67c`)
- S23: [achievement of high fatigue resistance in metals and alloys__d0ca5ee873](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a7c9d1b3-a9dd-4b2b-8c7d-cf77dbf503e4/resource) (`a7c9d1b3-a9dd-4b2b-8c7d-cf77dbf503e4`)
- S28: [aluminium alloys theory and applications__f2d28f5a78](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c25e9b6c-721b-462c-8804-d96f1868389f/resource) (`c25e9b6c-721b-462c-8804-d96f1868389f`)
- S1: [energy based approach to thermal fatigue life of tool steels for die cas__16af947521](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/06c301fa-2e7f-4865-8bdb-d85ba6af9eb8/resource) (`06c301fa-2e7f-4865-8bdb-d85ba6af9eb8`)
- S4: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1974bddf-49ba-4eef-a93a-22038d25d277/resource) (`1974bddf-49ba-4eef-a93a-22038d25d277`)
- S3: [8689283_低周疲劳](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12e965b8-2a67-4eca-98ec-16f202ec78b0/resource) (`12e965b8-2a67-4eca-98ec-16f202ec78b0`)
- S12: [advances in welding metal alloys dissimilar metals and additively manufa__99cf3beb76](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79e28236-582e-44f6-8044-77b2ad42bc7c/resource) (`79e28236-582e-44f6-8044-77b2ad42bc7c`)
- S21: [基于数值模拟的复杂壳体压铸模具优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a347df4b-5786-4560-9495-a4885558b3f4/resource) (`a347df4b-5786-4560-9495-a4885558b3f4`)
- S18: [基于ProCAST铝合金压铸模热疲劳缓解机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/979769f4-599d-4b3c-8a85-8b28eb2706f3/resource) (`979769f4-599d-4b3c-8a85-8b28eb2706f3`)
- S24: [压铸模具钢热机械疲劳行为及损伤机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0a84575-af2b-4d7e-85c6-084bd64a8a1b/resource) (`b0a84575-af2b-4d7e-85c6-084bd64a8a1b`)
- S30: [creep and high temperature deformation of metals and alloys__3b591a6325](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d008bcf2-3e5d-447d-b512-68bf61c3b5ea/resource) (`d008bcf2-3e5d-447d-b512-68bf61c3b5ea`)
- S19: [图3.2交变次数2Nf与应变幅εa之间的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9adc3921-6451-499a-99f2-92535e89b173/resource) (`9adc3921-6451-499a-99f2-92535e89b173`)
- S34: [压铸模数学模型及测温试验研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dee19188-494c-4bda-8b2e-ef4d44f619ea/resource) (`dee19188-494c-4bda-8b2e-ef4d44f619ea`)
- S9: [表 4.2 三种 H13 钢在室温与 700°C 下的弹性模量及断裂应变](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/471b9780-2eeb-45b6-b57a-71d896cb8bf5/resource) (`471b9780-2eeb-45b6-b57a-71d896cb8bf5`)
- S10: [压铸模具钢热机械疲劳行为及损伤机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58183cde-9a94-4c74-8ff6-1dc641eb4776/resource) (`58183cde-9a94-4c74-8ff6-1dc641eb4776`)
- S15: [energy based approach to thermal fatigue life of tool steels for die cas__16af947521](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/925ac59f-f6b6-4e07-9908-d6a1d915fdce/resource) (`925ac59f-f6b6-4e07-9908-d6a1d915fdce`)
- S25: [压铸模具钢热机械疲劳行为及损伤机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0b294e1-0e64-4e3e-8c74-0c7307a3fb6b/resource) (`b0b294e1-0e64-4e3e-8c74-0c7307a3fb6b`)
- S17: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9628507c-037b-405b-b9e9-d2aa1242e938/resource) (`9628507c-037b-405b-b9e9-d2aa1242e938`)
- S11: [a new approach to monitoring thermal fatigue cracks in die casting mould__67351de365](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6de348c8-c249-45a2-8cdf-da4d2dc73770/resource) (`6de348c8-c249-45a2-8cdf-da4d2dc73770`)
- S33: [表1.4 各种合金压铸模的失效形式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd575fa4-28be-4e2d-be7c-4785efbc4da7/resource) (`dd575fa4-28be-4e2d-be7c-4785efbc4da7`)
- S2: [压铸模数学模型及测温试验研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0eeba9ef-5924-4e2f-95ae-6c1cf11a3f89/resource) (`0eeba9ef-5924-4e2f-95ae-6c1cf11a3f89`)
- S32: [压铸模具成型温度场实时监测及控制技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/db00290a-768f-44c6-b829-beaccc614de8/resource) (`db00290a-768f-44c6-b829-beaccc614de8`)
- S13: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e652c33-261e-4b1d-a9e8-12cc0efd6f9a/resource) (`7e652c33-261e-4b1d-a9e8-12cc0efd6f9a`)
- S35: [发动机叶片工程应用分析优化加书签](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e12a6c1d-9b49-4994-beeb-96a89e5afb55/resource) (`e12a6c1d-9b49-4994-beeb-96a89e5afb55`)
- S26: [defects fracture and fatigue proceedings of the second international sym__b82eae5125](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bb181485-a8b4-47c1-8880-15b153736051/resource) (`bb181485-a8b4-47c1-8880-15b153736051`)
- S29: [FIG. 2—Schematic strain-life curve.](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cd36815f-d6bc-436c-850c-8ab1893d9fc2/resource) (`cd36815f-d6bc-436c-850c-8ab1893d9fc2`)
- S6: [Schematic strain-life curve](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/385e99d5-746b-4668-b0a0-2b8e75cd1b02/resource) (`385e99d5-746b-4668-b0a0-2b8e75cd1b02`)
- S8: [图3.10 A2热处理条件下热疲劳损伤因子与循环次数的关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/442c813b-05e1-4ad3-b050-d225aff62dae/resource) (`442c813b-05e1-4ad3-b050-d225aff62dae`)
- S14: [图2.17 奥氏体化温度对淬火后硬度的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/84fd0c99-e908-42b5-b89c-715bb7636407/resource) (`84fd0c99-e908-42b5-b89c-715bb7636407`)
- S20: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f8dc69a-2bb2-40aa-9993-9aa9b9cca1dc/resource) (`9f8dc69a-2bb2-40aa-9993-9aa9b9cca1dc`)
- S36: [执手多型腔压铸工艺及模具优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e6aa47a6-66d5-447a-87a5-6d3aeb6c9901/resource) (`e6aa47a6-66d5-447a-87a5-6d3aeb6c9901`)
- S38: [压铸模具钢热疲劳试验与有限元仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fbf751ab-5751-4e48-947b-fd4f81490ac4/resource) (`fbf751ab-5751-4e48-947b-fd4f81490ac4`)
- S27: [基于ProCAST铝合金压铸模热疲劳缓解机理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c1599d52-9e33-486f-9725-cca513b1e0e5/resource) (`c1599d52-9e33-486f-9725-cca513b1e0e5`)