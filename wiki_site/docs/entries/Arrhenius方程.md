---
version: "v1"
generated_at: "2026-06-18T18:16:04+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 15
  source_quality_score: 0.88
  freshness_score: 0.74
  evidence_coverage_score: 1.0
---

## 概述

Arrhenius方程是一个描述化学反应速率常数或扩散系数与温度之间指数依赖关系的半经验公式。该方程于1889年由S. Arrhenius提出，其核心物理思想是：反应物分子必须获得超过某一能量阈值（即活化能）才能发生有效反应[[S7,S16]]。在压铸技术领域，该方程广泛用于描述模具钢高温氧化速率、熔体与模具间元素互扩散、涂层热降解等与温度强烈相关的动力学过程[[S8,S6,S12]]。

## 定义与数学形式

### 标准表达式

Arrhenius方程描述化学反应速率常数的标准形式为[[S16,S7,S3]]：

$$
k = A \exp\left(-\frac{E_a}{RT}\right)
$$

其中：
- \(k\) — 反应速率常数；
- \(A\) — 指前因子（也称频率因子）；
- \(E_a\) — 反应活化能（J/mol 或 kJ/mol）；
- \(R\) — 摩尔气体常数，取值 8.314 J/(mol·K) [[S16,S3]]；
- \(T\) — 绝对热力学温度（K）。

当用于描述扩散系数时，方程表达为[[S19,S13]]：

$$
D = D_0 \exp\left(-\frac{Q}{RT}\right)
$$

其中：
- \(D\) — 扩散系数；
- \(D_0\) — 扩散指前因子；
- \(Q\) — 扩散激活能。

### 微分与积分形式

Arrhenius方程的微分形式为[[S16,S3]]：

$$
\frac{\mathrm{d}\ln k}{\mathrm{d}T} = \frac{E_a}{RT^2}
$$

其不定积分形式为 \(\ln k = -\dfrac{E_a}{RT} + B\)（\(B\)为积分常数）。当已知两个不同温度 \(T_1\) 和 \(T_2\) 下的速率常数 \(k_1\) 和 \(k_2\) 时，可利用定积分形式直接求解活化能[[S16]]：

$$
\ln\frac{k_2}{k_1} = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)
$$

### 别名

英文文献中该方程存在三种常用称谓：**Arrhenius equation**（通用学术场合）、**Arrhenius formula**（工程计算场合）、**Arrhenius law**（定性描述经验规律场合）。中文文献中对应称谓为：**阿伦尼乌斯方程**、**阿伦尼乌斯公式**、**阿伦尼乌斯定律**，亦存在异体译法“阿累尼乌斯”[[S16,S7]]。

## 在压铸领域的应用

### 模具钢高温氧化

压铸模具钢在使用过程中承受反复的高温浇注循环，其表面氧化是典型的温度激活过程。线性氧化和抛物线氧化两类高温氧化动力学对应的速率常数 \(k_L\) 和 \(k_P\) 均满足Arrhenius型的温度依赖关系[[S8]]：

$$
k_L = A_L \exp\left(-\frac{Q_L}{RT}\right),\quad k_P = A_P \exp\left(-\frac{Q_P}{RT}\right)
$$

温度升高时，模具钢的高温氧化速率呈指数上升。

### 熔体-模具元素互扩散

铝合金熔体与压铸模具之间存在元素互扩散导致的侵蚀现象。扩散系数与温度的关系同样遵循Arrhenius形式[[S6,S5]]：

$$
D = D_0 \exp\left(-\frac{Q}{RT}\right)
$$

温度升高时，固/液两相体系中元素的扩散系数同样呈指数规律增大。

### 涂层降解动力学

压铸模具表面的热防护涂层在服役中的降解过程可分解为涂层氧化反应和内部元素互扩散两个子过程，两者均可分别采用独立的Arrhenius方程进行拟合[[S12]]。涂层总降解速率同时受氧化活化能与内部扩散活化能共同控制，不同温度区间下主导降解的控速机制可能发生切换。

## 典型参数参考值

以下汇总了与压铸相关材料的Arrhenius参数实测值。

| 材料/体系 | 过程类型 | 温度区间 | 活化能 \(Q\) | 指前因子 \(A\) 或 \(D_0\) | 拟合度 | 来源 |
|---|---|---|---|---|---|---|
| 20Cr类热作模具钢 | 高温氧化 | 600–1000 ℃ | 163.501 kJ/mol | \(A = 5.914\times10^7\) | \(R^2 = 0.97\) | [[S20]] |
| 液态铝中Fe元素 | 扩散 | 700–900 ℃ | 16.7 kJ/mol | \(D_0 = 3.7\times10^{-3}\) cm²/s | — | [[S14]] |
| 钴基铝化物涂层 | 氧化（生成α-Al₂O₃） | >1000 ℃ | 82.0876 kJ/mol （约82.09 kJ/mol） | — | — | [[S12]] |

对于液态铝中Fe扩散活化能（16.7 kJ/mol），来源文献指出该数值与纯铝粘滞流动的活化能（13 kJ/mol）非常接近[[S14]]。

钴基铝化物涂层在1323 K和1373 K两个温度下的实测氧化速率常数分别为 \(3.28\times10^{-4}\) mg²/(cm⁴·h) 和 \(4.97\times10^{-3}\) mg²/(cm⁴·h)[[S12]]。

## Arrhenius图的绘制与应用

标准Arrhenius图以 \(\ln k\) 或 \(\ln D\) 为纵坐标，以 \(1/T\) 为横坐标。满足Arrhenius关系的数据在图中呈现为一条直线，其斜率为 \(-E_a/R\)（或 \(-Q/R\)），由此可直接计算活化能[[S16,S3]]。

下图展示了一个扩散系数Arrhenius图的实例。该图给出了Ni在316L侧的扩散系数 \(\ln D\) 随温度倒数 \(1/T\) 变化的线性拟合结果，拟合方程为 \(y = -17.40 - 2.089x\)，直观验证了扩散系数与温度倒数的线性依存关系[[S17]]。

![Ni在316L侧扩散系数的Arrhenius线性拟合图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd83e249-4347-48b3-80b6-db1504094203/resource)

## 方程局限性

### 通用局限性

Arrhenius方程不适用于以下情形[[S16]]：
- 无法表述为统一速率常数的复杂反应体系；
- 反应速率随温度升高反而下降的特殊反应（如某些酶催化反应或吸附控制的异相反应）；
- 温度跨度极大时，活化能 \(E_a\) 不再保持定值，标准Arrhenius图将出现非线性偏移[[S19]]。

此外，在无定形聚合物的玻璃化转变温度 \(T_g\) 附近，该方程对黏度-温度关系的预测精度显著低于WLF方程[[S4]]。

### 压铸工况下的特殊局限性

压铸生产中存在周期性温度交变和多物理机制耦合的特点。不同温度区间内的主导控速机制可能发生切换（例如低温区间为界面化学反应控速，高温区间为固态扩散控速）[[S19]]。若仅依据某一窄温度区间拟合得到的单一活化能值外推至其他温度区间，将产生显著的预测误差。

## 与Eyring方程的关系

Eyring方程（绝对反应速率理论）表达式为[[S2,S9]]：

$$
k = \frac{RT}{Nh}\exp\left(\frac{\Delta S^*}{R}\right)\exp\left(-\frac{\Delta H^*}{RT}\right)
$$

其中：
- \(N\) — 阿伏伽德罗常数；
- \(h\) — 普朗克常数；
- \(\Delta H^*\) — 活化焓，与Arrhenius方程中的活化能 \(E_a\) 在物理意义上完全对应；
- \(\Delta S^*\) — 活化熵。

Arrhenius方程的指前因子 \(A\) 可与 Eyring 方程中的项 \(\dfrac{RT}{Nh}\exp\left(\dfrac{\Delta S^*}{R}\right)\) 对应，其中 \(\exp(\Delta S^*/R)\) 的作用与碰撞理论中的空间位阻因子 \(P\) 相当[[S2,S9]]。对于简单分子反应，\(\Delta S^*\) 很小，\(\exp(\Delta S^*/R) \approx 1\)；对于复杂分子反应，熵减较大，该因子将远小于1。

## 适用条件

Arrhenius方程被广泛应用于[[S16,S7,S4]]：
- 所有反应速率随温度升高的基元反应；
- 大多数均相气相反应、溶液反应和异相冶金反应；
- 金属材料中由空位机制、间隙机制主导的热激活扩散过程；
- 半结晶热塑性聚合物温度依赖的黏流特性表征（适用范围与无定形聚合物的WLF方程互补）。

在扩散机制层面，当扩散仅由单一原子缺陷机制（如单空位机制）主导时，Arrhenius参数 \(D_0\) 和 \(Q\) 可进一步按微观原子尺度参数进行拆分解释[[S13]]。

## Sources
- S7: [an introduction chemical metallurgy__450cfa22a6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7981bc7a-24f8-4810-9a31-941b440adfbd/resource) (`7981bc7a-24f8-4810-9a31-941b440adfbd`)
- S16: [物理化学机械热加工及金属材料专业用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0dad5b7-f3e8-4a22-8721-1b39a96e2126/resource) (`d0dad5b7-f3e8-4a22-8721-1b39a96e2126`)
- S8: [engineering materials 1 an introduction to their properties and applicat__1f116ed029](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7abebcd2-7bdc-419d-9424-469c1c96351e/resource) (`7abebcd2-7bdc-419d-9424-469c1c96351e`)
- S6: [铝合金熔炼理论与工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/75f2c256-4bf1-4b48-82ab-275cd86edff3/resource) (`75f2c256-4bf1-4b48-82ab-275cd86edff3`)
- S12: [钴基合金铝化物涂层的高温氧化行为](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a2cf6839-40d4-453c-a56a-652faf9ebfa0/resource) (`a2cf6839-40d4-453c-a56a-652faf9ebfa0`)
- S3: [chemical metallurgy__e85294305f](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/53dcc801-f9ce-4a1e-883d-21e190862784/resource) (`53dcc801-f9ce-4a1e-883d-21e190862784`)
- S19: [defects in solids special topics in inorganic chemistry__f0d8aa076d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f01a5d20-3fbe-412d-a962-ec94b551814e/resource) (`f01a5d20-3fbe-412d-a962-ec94b551814e`)
- S13: [diffusion in solid metals and alloys__edf6ecfd85](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b2669b6a-4376-462e-943f-6126a105ff36/resource) (`b2669b6a-4376-462e-943f-6126a105ff36`)
- S5: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d51ab46-df02-4621-a2fd-8960dc5b5d82/resource) (`6d51ab46-df02-4621-a2fd-8960dc5b5d82`)
- S20: [步进加热炉方坯加热特性与性能演变研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f60d1cc2-3979-4bcc-873d-fc01ceb1ca44/resource) (`f60d1cc2-3979-4bcc-873d-fc01ceb1ca44`)
- S14: [铝及铝合金与其他金属的焊接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c48cf6fb-f857-4a9b-b702-3ece61395110/resource) (`c48cf6fb-f857-4a9b-b702-3ece61395110`)
- S17: [图 (a) Ni 在 316L 侧的扩散系数与温度的关系图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd83e249-4347-48b3-80b6-db1504094203/resource) (`dd83e249-4347-48b3-80b6-db1504094203`)
- S4: [橡塑挤出模具设计与工程模拟原著](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65f1961e-2cf8-43af-b1c8-05d8cf086d43/resource) (`65f1961e-2cf8-43af-b1c8-05d8cf086d43`)
- S2: [an introduction chemical metallurgy__450cfa22a6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/32de30f7-3d17-40bf-bdad-8840f1630523/resource) (`32de30f7-3d17-40bf-bdad-8840f1630523`)
- S9: [an introduction to chemical metallurgy__a3796fd351](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8667e2c0-24b8-4fcc-90d7-66f0fa46472c/resource) (`8667e2c0-24b8-4fcc-90d7-66f0fa46472c`)