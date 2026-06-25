---
version: "v1"
generated_at: "2026-06-21T06:04:07+00:00"
confidence_score: 0.85
confidence_level: "very_high"
confidence_basis:
  cited_sources: 32
  source_quality_score: 0.87
  freshness_score: 0.74
  evidence_coverage_score: 1.0
---

## 定义

**Prandtl数**（普朗特数，别称普朗特常数，符号 *Pr*）是一个描述流体动量扩散能力与热扩散能力相对比值的无量纲物性参数[[S44,S19]]。其定义为：

\[
Pr = \frac{\nu}{\alpha} = \frac{\mu \cdot c_p}{k}
\]

式中：
- *ν* 为流体运动黏度（动量扩散率，m²/s）
- *α* 为流体热扩散率（m²/s）
- *μ* 为流体动力黏度（Pa·s）
- *c*<sub>p</sub> 为流体定压比热容（J/(kg·K)）
- *k* 为流体热导率（W/(m·K)）[[S44,S19,S22,S16,S29]]

*Pr* 数仅由流体自身的热物理性质决定，与流动状态和几何参数无关[[S44,S39,S45,S19]]。

## 物理意义

*Pr* 数是速度边界层厚度 *δ* 与热边界层厚度 *δ*<sub>T</sub> 相对比值的核心控制参数，满足 *δ*/ *δ*<sub>T</sub> ≈ *Pr*<sup>1/3</sup>[[S19,S29]]：

- **Pr = 1**：速度边界层与热边界层厚度相等，此时层流边界层中的无量纲温度场和速度场完全重合[[S19,S15]]。
- **Pr > 1**：动量扩散能力强于热扩散能力，速度边界层厚度大于热边界层厚度。
- **Pr < 1**：热扩散能力强于动量扩散能力，热边界层厚度大于速度边界层厚度[[S19,S29,S28]]。

在确定雷诺数的前提下，介质的 *Pr* 数越大，则温度梯度越大，传热性能越好[[S39,S14]]。

![平板层流边界层内不同Pr数对应的无量纲温度分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c06afac-f206-46d6-b40e-b08b69f34336/resource)

**图：不同普朗特数下平板层流边界层内的无量纲温度分布**。图中覆盖 *Pr* = 0.6 至 1000 的典型数值区间，直观展示了流体物性对温度场分布的影响[[S8,S43]]。

## 典型介质的普朗特数范围

不同类型流体的 *Pr* 数分布具有明确的区间特征[[S19,S10]]：

| 流体类别 | *Pr* 范围 | 典型特征 |
|---------|----------|----------|
| 气体 | 0.6 ~ 1.0 | *Pr* ≈ 1，几乎不随温度变化 |
| 一般液体（水、导热油等） | > 1 | 油类可达几十至上百，随温度升高而显著降低 |
| 液态金属 / 压铸熔融金属 | 0.001 ~ 0.1 | 铝熔体实测算例为 0.0128 |

常压下气体的 *Pr* 数接近 1，几乎不随温度发生明显变化；常规液体的 *Pr* 数随温度升高呈现显著降低趋势；金属熔体的 *Pr* 数受温度影响很小，整体维持在极低区间[[S19,S7,S9]]。在工程常规压力范围内，几乎所有介质的 *Pr* 数均不随压力变化发生可测量的明显偏移，普通压铸生产工况下可认为压力对此无影响[[S37,S36]]。

压铸生产常用冷却介质（水、水基冷却液、导热油）在 50 °C ~ 250 °C 工作温度区间内，*Pr* 数随温度升高逐步下降，对应物性表中可直接查询各温度点的准确 *Pr* 值[[S11,S18]]。

## 与相关无量纲数的关联

### 对流换热通用准则函数

对流换热的通用准则函数形式为[[S15,S2,S33]]：

\[
Nu = f(Pr, Gr, Re)
\]

各无量纲数定义：

- **Nu（努塞尔数）**：*Nu* = *h*<sub>c</sub>*L* / *λ*，表征流体贴壁处温度梯度大小[[S15,S2]]。
- **Re（雷诺数）**：*Re* = *vL* / *ν*，表征惯性力与黏滞力的相对大小，是强制对流中判断层流/紊流态的核心标志[[S15]]。
- **Gr（格拉晓夫数）**：*Gr* = *gβL*³(<i>T</i><sub>w</sub> − <i>T</i><sub>f</sub>) / *ν*²，是自然对流中判断流态的核心标志[[S15,S2]]。
- **Pr（普朗特数）**：表征动量扩散与热扩散的相对大小，当 *Pr* = 1 时层流边界层中的无量纲温度场与速度场完全重合[[S15]]。

### 强制对流

当强制对流流速足够大、自然对流影响可忽略时，Gr 数可省略，准则方程简化为[[S15,S26,S34]]：

\[
Nu = c \cdot Re^{\,n} \cdot Pr^{\,m}
\]

工程上通过实验数据拟合常数 *c* 及指数 *n*、*m*。

### 自然对流

无限空间自然对流时 Gr 数起主导作用，Re 数可忽略[[S26,S21,S34,S33]]：

\[
Nu = c \cdot (Gr \cdot Pr)^{\,n}
\]

其中 *Gr*·*Pr* 的乘积即为瑞利数 *Ra*，是自然对流换热的核心控制无量纲数。

### 组合参数统一关联式

可通过引入组合无量纲参数 *N*<sub>Cf</sub> 实现强制对流与自然对流换热的统一关联[[S20]]：

\[
\frac{Nu}{Pr^{0.33}} = 0.50 + 0.49 \cdot N_{Cf}^{\;0.52}
\]

其中水平流动工况下 *N*<sub>Cf</sub> = (*Re*² + *Gr*)<sup>0.5</sup>，可同时适配纯强制对流、纯自然对流及混合对流工况[[S20]]。

![纯强制对流、纯自然对流及混合对流的Nu-Pr-Re/Gr关联曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c1da505-ba4d-4838-971e-f7b62e635cf5/resource)

**图：不同对流工况下含普朗特数项的努塞尔数关联曲线**。图中展示了自然对流、强制对流和一般对流三种工况下 *Nu*/*Pr*<sup>1/3</sup> 随 Re 数或 Gr 数平方根的变化规律，直观体现了 *Pr* 数在不同对流换热场景关联式中的核心作用[[S17]]。

### 常用经验关联式及其 *Pr* 适用范围

| 关联式类型 | 适用范围 (*Pr*) | 公式要点 |
|-----------|----------------|---------|
| 柯尔本比拟 | 0.5 < *Pr* < 50 | *j*<sub>H</sub> = *St* · *Pr*<sup>2/3</sup> = *c*<sub>f</sub>/2[[S9,S12]] |
| 普朗特-冯卡门比拟 | 0.5 < *Pr* < 30 | 含过渡层修正的比拟解[[S9,S12]] |
| Dittus-Boelter 公式 | 0.7 < *Pr* < 120 | *Nu* = 0.023<i>Re</i><sup>0.8</sup><i>Pr</i><sup>m</sup>，*Re* > 10⁴、*L*/*D* ≥ 60[[S9,S31]] |
| Sieder-Tate 公式 | 0.6 < *Pr* < 100 | *Nu* = 0.026<i>Re</i><sup>0.8</sup><i>Pr</i><sub>f</sub><sup>1/3</sup>(<i>η</i><sub>f</sub>/*η*<sub>s</sub>)<sup>0.14</sup>，*Re* 10⁴~10⁵、*L*/*D* > 10[[S31,S9]] |

## 温度修正角标 *f* 与 *w*

下标 *f* 对应的 *Pr*<sub>f</sub> 是以冷却介质进出口平均温度（流体主体平均温度）为定性温度计算得到的普朗特数，下标 *w* 对应的 *Pr*<sub>w</sub> 是以冷却管道内壁壁面温度为定性温度计算得到的普朗特数[[S9,S39,S42]]。

在圆环形冷却通道（*d*<sub>2</sub>/*d*<sub>1</sub> 在 1.2 ~ 1.4 区间）的湍流换热公式中，普朗特数的温度修正项采用 (*Pr*/*Pr*<sub>w</sub>)<sup>0.25</sup> 的形式，用于补偿大温差下管壁处流体黏度变化带来的换热计算误差[[S39]]。

当压铸冷却管道内壁面与冷却水之间温差较大（水温温差超过 30 °C）、流体黏度变化显著时，采用 Sieder-Tate 公式计算 *Nu* 数，形式为[[S31,S9]]：

\[
Nu = 0.026 \cdot Re^{0.8} \cdot Pr_f^{\,1/3} \cdot \left(\frac{\eta_f}{\eta_s}\right)^{0.14}
\]

式中 *η*<sub>f</sub> 为流体主体平均温度下的动力黏度，*η*<sub>s</sub> 为壁温下的动力黏度。此公式计算误差小于 20%，适配压铸模冷却系统大温度梯度的实际工况[[S31]]。

## 在模具冷却系统中的应用

### 冷却系统换热计算

*Pr* 数是压铸模具冷却管道内强制对流换热计算的三个核心无量纲参数（*Nu*、*Re*、*Pr*）之一，对流换热系数 *h* 的计算遵循[[S14,S16]]：

\[
h = \frac{\lambda}{d} \cdot f(Re, Pr)
\]

换热系数数值直接由 *Re* 数和 *Pr* 数共同决定，是冷却系统热平衡计算、温度场仿真的必备输入参数[[S14,S16,S4]]。

### 工程设计常规取值

水作为冷却介质时，*Pr* 数通常处于 0.7 ~ 2500 区间[[S38]]。压铸冷却系统工程设计为保证湍流换热效率，要求冷却介质雷诺数 *Re* ≥ 10⁴，需结合对应工况下的 *Pr* 数进行对流换热系数核算[[S38,S14]]。

### 管内强制对流换热关联式

**管内充分发展层流强制对流换热**（Sieder-Tate 型关联式）[[S40]]：

\[
Nu = 1.86 \cdot Re^{1/3} \cdot Pr^{1/3} \cdot \left(\frac{D}{L}\right)^{1/3} \cdot \left(\frac{\eta_b}{\eta_w}\right)^{0.14}
\]

式中 *η*<sub>b</sub> 为冷却介质主体平均黏性系数，*η*<sub>w</sub> 为管壁温度下介质的黏性系数，*L* 为管道受热长度，*D* 为管道直径。

**湍流工况的常用经验公式**[[S45]]：当 *Re* 大于 10 000 时，*Nu* = 0.023<i>Re</i><sup>0.8</sup><i>Pr</i><sup>1/3</sup>。

**圆环形截面冷却通道换热**[[S39]]：当 *d*<sub>2</sub>/*d*<sub>1</sub> 在 1.2 ~ 1.4 之间时，*Nu* = 0.017<i>Re</i><sup>0.8</sup><i>Pr</i><sup>0.4</sup>(<i>Pr</i>/<i>Pr</i><sub>w</sub>)<sup>0.25</sup>(*d*<sub>2</sub>/*d*<sub>1</sub>)<sup>0.18</sup>。

## 层流边界层与平板对流

平板层流对流换热局部 *Nu* 数计算式（*Pr* ≥ 0.6）[[S43]]：

\[
Nu_x = 0.332 \, Re_x^{\,1/2} \, Pr^{\,1/3}
\]

平板层流平均对流换热系数 *h* 可通过该式积分求得[[S43]]。

## Sources
- S44: [铝及铝合金铸轧成形与裂纹扩展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6a5a111-3c1e-4ec8-b41a-0fc86ac1c72d/resource) (`f6a5a111-3c1e-4ec8-b41a-0fc86ac1c72d`)
- S19: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/646bd1c4-912c-454c-bce8-7c4495a5ca02/resource) (`646bd1c4-912c-454c-bce8-7c4495a5ca02`)
- S22: [an introduction to materials engineering and science for chemical and ma__3b6a81c7b9](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c26ed1a-9366-4339-a907-14e1528c9ad0/resource) (`7c26ed1a-9366-4339-a907-14e1528c9ad0`)
- S16: [注塑成型模拟及模具优化设计理论与方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58f11666-4ee1-4130-b9e1-7aa398fe8975/resource) (`58f11666-4ee1-4130-b9e1-7aa398fe8975`)
- S29: [铝合金车轮低压铸造模具冷却系统界面换热机理分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8c0a2c74-a53f-4dda-87d9-410c895f9f08/resource) (`8c0a2c74-a53f-4dda-87d9-410c895f9f08`)
- S39: [现代模具技术注塑成型原理与注塑模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ece434bd-edb7-448d-8fa2-c7bdab5df7c6/resource) (`ece434bd-edb7-448d-8fa2-c7bdab5df7c6`)
- S45: [注塑成型原理与注塑模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fd1e7724-c795-4108-9764-bc698daf777f/resource) (`fd1e7724-c795-4108-9764-bc698daf777f`)
- S15: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/57a4d6c8-0772-4281-91b8-0c2fdb5e0ce3/resource) (`57a4d6c8-0772-4281-91b8-0c2fdb5e0ce3`)
- S28: [铝及铝合金与其他金属的焊接](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8b344147-e0e7-46e6-9ac8-b87b35883293/resource) (`8b344147-e0e7-46e6-9ac8-b87b35883293`)
- S14: [注塑成型模拟及模具优化设计理论与方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/55b0e46d-b069-44ad-ba76-a3c8ec1d2db8/resource) (`55b0e46d-b069-44ad-ba76-a3c8ec1d2db8`)
- S8: [图9-8 各种Pr下的平板上层流边界层内的无量纲温度分布](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c06afac-f206-46d6-b40e-b08b69f34336/resource) (`3c06afac-f206-46d6-b40e-b08b69f34336`)
- S43: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f682eeb6-153d-4448-af20-c372f2c89dc9/resource) (`f682eeb6-153d-4448-af20-c372f2c89dc9`)
- S10: [表 13-3 不同流体层流边界层 Pr 和 Sc 值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42edf522-b047-4548-b1e6-48be1e8cd9e0/resource) (`42edf522-b047-4548-b1e6-48be1e8cd9e0`)
- S7: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/384f7337-ba49-4a5e-b110-dd9b357c596e/resource) (`384f7337-ba49-4a5e-b110-dd9b357c596e`)
- S9: [TextNode282](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fc3585e-b95a-4287-b816-92b9d9114eaf/resource) (`3fc3585e-b95a-4287-b816-92b9d9114eaf`)
- S37: [塑料注射成型与模具设计指南](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ced3a877-38da-477b-846d-857d35e8e1d4/resource) (`ced3a877-38da-477b-846d-857d35e8e1d4`)
- S36: [橡塑挤出模具设计与工程模拟原著](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ce07281d-6111-4b8d-b4ce-961e31e891ef/resource) (`ce07281d-6111-4b8d-b4ce-961e31e891ef`)
- S11: [不同温度下冷却剂的热物性参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4cfe28fb-33fe-4cd5-b3c0-2a2ad8ab8a00/resource) (`4cfe28fb-33fe-4cd5-b3c0-2a2ad8ab8a00`)
- S18: [水的物理性质表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/641ed81a-d480-4ed4-95d1-8ac69ab9e899/resource) (`641ed81a-d480-4ed4-95d1-8ac69ab9e899`)
- S2: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/150891b5-ad3d-4a8c-a33d-657196b30d37/resource) (`150891b5-ad3d-4a8c-a33d-657196b30d37`)
- S33: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc6cfd27-127e-49e6-ac11-901379d3304c/resource) (`bc6cfd27-127e-49e6-ac11-901379d3304c`)
- S26: [材料加工过程的建模与数值分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a2f3e09-fcdc-45cb-a019-547daeb153e1/resource) (`8a2f3e09-fcdc-45cb-a019-547daeb153e1`)
- S34: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bc84729d-7f8f-4faa-9087-e437622889a4/resource) (`bc84729d-7f8f-4faa-9087-e437622889a4`)
- S21: [5083铝合金温热成形界面换热系数求解及影响因素研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7117d122-bc1f-43b5-a933-8ef008bc6064/resource) (`7117d122-bc1f-43b5-a933-8ef008bc6064`)
- S20: [chemical vapor deposition of refractory metals alloys and compounds__a1bd0d0e89](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/665a96bd-592f-43bc-ba2b-3a6a51de31e1/resource) (`665a96bd-592f-43bc-ba2b-3a6a51de31e1`)
- S17: [自然、强制及一般对流的努塞尔数关联式对比曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5c1da505-ba4d-4838-971e-f7b62e635cf5/resource) (`5c1da505-ba4d-4838-971e-f7b62e635cf5`)
- S12: [金属热态成形传输原理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4da992ab-5b41-4c41-8671-2710d29c8fda/resource) (`4da992ab-5b41-4c41-8671-2710d29c8fda`)
- S31: [TextNode283](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9925a576-6213-472d-bc73-d3ad8b955060/resource) (`9925a576-6213-472d-bc73-d3ad8b955060`)
- S42: [铝合金车轮低压铸造模具冷却系统界面换热机理分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f65d0342-6bd2-47ab-8e1a-0c93172b42aa/resource) (`f65d0342-6bd2-47ab-8e1a-0c93172b42aa`)
- S4: [低压铸造筒形件组织性能及铸造缺陷消除机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2a3ea4b1-06c7-48c2-8992-8998a544fcda/resource) (`2a3ea4b1-06c7-48c2-8992-8998a544fcda`)
- S38: [压铸成型工艺与模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e89fd404-b99b-4b02-9880-3395126e8732/resource) (`e89fd404-b99b-4b02-9880-3395126e8732`)
- S40: [现代模具技术注塑成型原理与注塑模设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1500470-15db-4100-a0a4-a12a61f40256/resource) (`f1500470-15db-4100-a0a4-a12a61f40256`)