---
version: "v1"
generated_at: "2026-06-18T14:52:05+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 62
  source_quality_score: 0.84
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

CAFE法是一种将元胞自动机（Cellular Automaton, CA）与有限元（Finite Element, FE）耦合的跨尺度数值模拟方法，全称为元胞自动机‑有限元法（Cellular Automaton‑Finite Element method）[[S26,S75,S45]]，简称为CAFE法或CA‑FE法[[S41]]。该方法由Rappaz和Gandin于1994年首次提出，通过宏观有限元求解温度场、流场等传输物理量，再由微观元胞自动机计算晶粒的形核、生长与取向演化，并通过两者之间的数据传递实现双向耦合，专门用于铸造与压铸件凝固过程中的晶粒组织预测[[S75,S26,S41]]。

在商业软件生态中，ProCAST软件内部带有一个名为“显微组织分析模块”的可选附加模块，业界常以带重音符号的CAFÉ指代该模块[[S24]]。该模块基于通用CAFE学术方法，集成了等轴晶、包晶和共晶转变模型，可实现三维凝固组织仿真[[S24,S70]]。因此，通用CAFE模型是学术界公开的数值方法体系，而CAFÉ则是ProCAST软件中封装后的专有商业功能命名，两者不可完全等同[[S42,S70]]。截至2026年，国内现行铸造术语标准（如GB/T 5611《铸造术语》）尚未将CAFE法收录为正式术语条目，该方法属于新兴的微观组织模拟领域[[S48,S71]]。

## 跨尺度耦合原理

CAFE法的核心是宏观‑微观跨尺度网格体系：宏观有限元采用较大尺寸的网格，用于求解温度场、流场、溶质场等传输控制方程；在有限元网格内部进一步划分出微米级的CA元胞，用于计算晶粒形核、生长、择优取向及竞争淘汰等微观演化行为[[S62]]。两者之间的数据传递通过插值机制完成——由FE节点温度向CA元胞温度插值映射，CA元胞形核与生长过程中释放的凝固潜热则反馈更新FE节点温度，形成双向耦合循环[[S38,S62]]。

关于耦合强度，CAFE法存在两种实现方式：
- **弱耦合**：采用有限差分法的大网格（如控制体积CV网格）预计算温度场，将CV节点的温度直接赋值给对应控制体积内部的所有CA元胞，无需额外插值。该方法计算效率较高，但对非规则、非线性的复杂凝固界面适应性较差，精度有限[[S41,S38]]。
- **强耦合**：基于有限元变分原理，采用双线性插值（二维）或三角形面积权重插值，由宏观FE节点的温度分步插值得到任意CA元胞位置的精准温度；CA元胞状态变化后，立即更新FE节点温度。该方法对非均匀温度场适应性强，且对宏观网格质量要求更低，计算精度更高[[S38,S52]]。

一个典型的CAFE耦合算法循环可描述为：先由FE节点温度通过插值获得CA元胞温度→在元胞内计算局部过冷度→进行形核判断与枝晶尖端生长计算→释放凝固潜热并更新固相率→将潜热反馈至FE节点→更新宏观温度场，进入下一个时间步长，直至凝固完成[[S62,S38]]。

![CAFE法有限元‑元胞自动机跨尺度耦合原理示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92d7fdfb-ef61-4deb-b202-bda1ca34c3e7/resource)

**图1**：CAFE模型耦合原理示意图，清晰展示有限元节点i、j、k的位置、温度插值传递路径、微观CA元胞网格分布以及凝固潜热反向释放的完整耦合流程[[S46]]。

## 核心模型组成

### 元胞自动机部分

CAFE法的元胞自动机部分包含两个核心物理子模型。

**（1）连续形核高斯分布模型**

CAFE法默认采用Rappaz和Gandin提出的基于高斯分布的连续形核模型，将铸件内部及铸型壁面上的异质形核基底按尺寸和润湿性差异离散为连续分布的形核激活点，从而更真实地反映工业凝固过程中形核位置随过冷度逐渐激活的特征[[S17,S20,S69]]。其数学表达由两部分组成：

在某一过冷度ΔT下，形核密度变化率服从高斯分布：

\[
\frac{dn}{d(\Delta T)} = \frac{n_{max}}{\sqrt{2\pi}\, \Delta T_{\sigma}} \exp\!\left[-\frac{(\Delta T - \Delta T_N)^2}{2\Delta T_{\sigma}^2}\right]
\]

对应的任意过冷度ΔT下的累计形核密度通过积分求得：

\[
n(\Delta T) = \int_{0}^{\Delta T} \frac{dn}{d(\Delta T)} \, d(\Delta T)
\]

其中：\(n_{max}\)为该类形核位置的最大形核密度；\(\Delta T_N\)为平均形核过冷度（高斯分布中心值）；\(\Delta T_{\sigma}\)为过冷度的标准方差（高斯分布的标准差），代表形核过冷度的离散程度[[S8,S14,S57]]。

工程应用中通常区分两组独立的高斯分布参数：**面形核参数**（下标s）对应铸型壁面和铸件表面的异质形核行为，形核密度单位为\(\text{m}^{-2}\)；**体形核参数**（下标v）对应铸件内部金属液中的异质形核行为，形核密度单位为\(\text{m}^{-3}\)[[S17,S29,S35]]。

![CAFE法面形核与体形核参数的高斯分布示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e8ec3e9-90b1-4328-9e61-b2d3708e78ab/resource)

**图2**：体形核参数与面形核参数的高斯分布示意图，标注对应过冷度与形核密度等关键参数[[S23]]。

**（2）KGT枝晶尖端生长动力学模型**

枝晶生长动力学采用Kurz‑Giovanola‑Trivedi（KGT）模型。该模型将枝晶尖端总过冷度ΔT解构为四个物理分量：

\[
\Delta T = \Delta T_c + \Delta T_t + \Delta T_k + \Delta T_r
\]

分别为成分过冷度\(\Delta T_c\)、热过冷度\(\Delta T_t\)、动力学过冷度\(\Delta T_k\)与曲率过冷度\(\Delta T_r\)。在常规铸造条件下，后三个分量远小于成分过冷度，工程仿真中可忽略，以成分过冷\(\Delta T_c\)近似代替总过冷度[[S34,S39,S54]]。

KGT完整模型体系包含溶质过饱和度\(\Omega = Iv(Pe)\)、枝晶尖端半径R、溶质Peclet数\(Pe = Rv/(2D)\)以及Ivantsov积分函数\(Iv(Pe)\)等多个关联方程[[S34,S50,S39]]。为适应高速凝固或多元合金场景，存在两种经典修正形式：引入非平衡分配系数k与非平衡液相线斜率m的修正[[S34,S51]]；通过当量法将二元KGT模型拓展至多元合金体系[[S34,S62]]。

在CAFE工程仿真中，为提高计算效率，通常将KGT模型简化为过冷度的多段多项式拟合形式：

\[
v(\Delta T) = a_2 \Delta T^2 + a_3 \Delta T^3
\]

式中\(a_2\)和\(a_3\)为仅与目标合金成分相关的生长动力学标定常数，省去了迭代求解Ivantsov积分的开销[[S34,S25,S53]]。

### 有限元部分

CAFE法的宏观有限元侧通过数值离散求解三大核心传输控制方程[[S41,S47,S68]]：

- **热传导方程**：\(\rho C_p \frac{\partial T}{\partial t} = \nabla \cdot (\lambda \nabla T) + \rho L \frac{\partial f_s}{\partial t}\)，其中ρ为密度，\(C_p\)为定压比热容，λ为导热系数，L为凝固潜热，\(f_s\)为宏观固相率。
- **溶质扩散方程**：\(\frac{\partial C_i}{\partial t} = \nabla \cdot (D_i \nabla C_i) + (C_l - C_s)\frac{\partial f_s}{\partial t}\)。
- **动量与质量守恒方程**（Navier‑Stokes方程及连续性方程），用于描述流场与压力场。

宏观FE节点上的温度、溶质浓度及流速等物理量通过插值映射传递至每一个微观CA元胞，为晶粒形核与生长计算提供局部物理条件[[S62,S38]]。

## 关键参数与操作条件

CAFE模拟精度高度依赖预先标定的合金形核参数与生长动力学系数[[S7,S28,S74]]。主要参数及其典型取值与影响规律总结如下。

| 参数 | 物理含义 | 典型范围/示例 | 影响规律 |
|------|---------|--------------|---------|
| **ΔTₙ** | 平均形核过冷度（高斯分布中心值） | 1~10 K；如S30432钢体形核取8 K，16Cr20Ni14Si2合金体形核取8 K[[S15,S74,S28]] | ΔTₙ偏小→形核触发提前，晶粒细、等轴晶占比高；ΔTₙ偏大→形核延迟，晶粒粗大，柱状晶区域扩大[[S15,S28]] |
| **n_max** | 最大形核密度 | 体形核：10⁷~10¹³ m⁻³；面形核：10⁵~10⁷ m⁻²；如S30432钢体形核8×10⁸ m⁻³，Mg‑9Al‑2Si‑0.5Ca‑0.2Ce‑0.2Mn合金体形核3.7×10¹² m⁻³[[S15,S66,S28]] | n_max偏小→形核核心不足，晶粒粗大；n_max偏大→晶粒细化，等轴晶占比显著提升[[S74]] |
| **ΔT_σ** | 形核过冷度标准方差 | 0.1~1 K；如16Cr20Ni14Si2合金面/体形核均取0.1 K，S30432钢取0.5 K[[S15,S74,S28]] | ΔT_σ偏小→形核过程集中在窄过冷度区间，晶粒尺寸分布均匀；ΔT_σ偏大→形核分散于宽过冷区间，晶粒尺寸离散度增大[[S15,S28]] |
| **a₂, a₃** | KGT生长动力学系数 | 与合金成分强绑定；16Cr20Ni14Si2合金：a₂=6.631854×10⁻⁸ m/s·K², a₃=1.181568×10⁻⁶ m/s·K³[[S28]] | a₂/a₃取值偏小→枝晶生长速率低估；偏大→生长速率高估，模拟晶粒尺寸偏差增大[[S16,S28,S30]] |
| **CA网格尺寸** | 微观元胞空间离散尺度 | 1~10 μm[[S62,S33]] | 网格尺寸远大于枝晶尖端特征尺度→元胞捕获规则失真，枝晶形貌细节丢失[[S33]] |
| **时间步长** | 全局离散时间步长 | 10⁻⁴~10⁻² s[[S33]] | 时间步长过大→无法准确捕捉形核与生长瞬态过程，引发数值误差[[S33]] |

## 工艺作用与功能

CAFE法在压铸件及一般铸造件的凝固模拟中承担以下核心功能[[S18,S62,S21,S11]]：

1. **柱状晶向等轴晶转变（CET）预测**：CAFE结合宏观温度场与柱状晶前沿、液相区游离等轴晶的竞争生长机制，可基于Hunt CET判据定量输出CET转变发生的空间位置及临界温度梯度与凝固速度参数。
2. **晶粒尺寸与组织分布统计**：完成凝固模拟后，对所有CA元胞的晶粒属性进行后处理统计，可输出晶粒尺寸分布直方图、平均晶粒半径分布云图以及等轴晶/柱状晶占比统计，经校准的模拟结果与实测金相的平均误差可低至0.07%[[S73,S74]]。
3. **枝晶形貌动态可视化**：CA规则为不同晶粒随机分配固定结晶取向（通常用不同颜色区分），通过相邻液态元胞的分步捕获机制，可动态呈现从形核初期到凝固结束全流程的枝晶生长、侧枝发展及晶粒间碰撞竞争过程[[S62,S21,S12]]。
4. **微观偏析与缩松缺陷关联分析**：CAFE预测的晶粒分布结果可进一步关联缺陷评估。等轴晶越细小、占比越高，溶质在晶粒间分布越均匀，微观偏析程度越低，但分散性微小缩松的形成概率较高；柱状晶越发达，柱状晶前沿溶质富集效应越显著，容易形成集中通道偏析，且糊状区补缩不充分时更易形成集中缩松缺陷[[S11,S12,S64]]。

## 应用领域

CAFE法已在多种合金与铸造工艺中得到验证和应用：

- **铸钢件**：E级铸钢ZG25MnCrNiMo机车车钩的CAFE组织模拟结果显示，钩头薄壁区域柱状晶占比偏高，钩头与钩舌相交浇口部位等轴晶较发达，该结果可用于解释裂纹与缩孔多发的组织诱因[[S9,S36]]。此外，S30432耐热不锈钢、Q355钢、42CrMo钢等钢种的连铸坯和钢锭凝固组织也已采用CAFE法进行模拟研究[[S15,S25,S16]]。
- **铝合金铸造与压铸件**：Al6082合金农用机械框架/壳体熔模铸造[[S6]]；铝合金水泵座压铸件薄壁/厚壁部位晶粒度预测，模拟结果全部达到4级晶粒度要求[[S36]]；大尺寸铝合金轮毂低压铸造SDAS及局部CAFE组织模拟[[S58]]；ZL201铝合金副车架凝固组织模拟[[S10]]。
- **镁合金铸造与压铸件**：Mg‑Al‑Si系合金（如Mg‑9Al‑2Si‑0.5Ca‑0.2Ce‑0.2Mn）在不同工艺下的晶粒尺寸模拟，结果与实测误差小于10%[[S66]]；AZ31B镁合金铸轧微观组织模拟[[S59]]；AZ91D镁合金轮毂低压铸造工艺组织优化[[S32,S59]]。
- **高温合金精密铸造**：16Cr20Ni14Si2高温合金复杂薄壁发动机连接壳体熔模铸造，CAFE模拟得到的晶粒平均半径为11.91 μm，与实测金相平均值12.8 μm的误差仅约0.07%[[S7,S73]]。Ni基高温合金定向凝固涡轮叶片的枝晶竞争生长与晶粒形貌亦可通过CAFE方法预测[[S40,S13]]。
- **钛合金及其他合金**：Ti‑6Al‑4V合金离心铸造凝固组织模拟[[S35]]；Ag‑28Cu‑1Ni合金连铸微观组织模拟[[S38]]等亦有报道。

## 与其他微观组织模拟方法的关系

当前金属凝固微观组织模拟领域主要有四类数值方法，CAFE法在适用范围和计算效率上体现了一定的综合优势。

**表：四种微观组织模拟方法特性对比**[[S43,S44,S45]]

| 对比维度 | CAFE法 | 纯CA法 | 相场法（PF） | 蒙特卡洛法（MC） |
|---------|--------|--------|-------------|----------------|
| **适用尺度** | 厘米级至米级工程铸件 | 毫米级小区域 | 微米级少量枝晶 | 厘米级（无精确物理尺度标定） |
| **物理基础** | 基于形核与生长动力学 + 宏观多物理场 | 基于形核与生长动力学 | 基于热力学与动力学耦合 | 基于概率统计与自由能最小化 |
| **预测精度** | 全局晶粒尺寸误差<5%（经校准可达0.07%） | 对均匀温度场下晶粒形貌预测较好 | 最高，可解析亚枝晶与微观偏析细节 | 最低，仅能定性匹配晶粒形貌 |
| **计算效率** | 中等（蒙特卡洛>CA>CAFE>PF） | 较高 | 最低（计算资源消耗极大） | 最高 |
| **实现复杂度** | 较高 | 中等 | 最高 | 最低 |
| **核心优势** | 适应非均匀温度场下的大尺寸铸件全流程微观组织模拟 | 物理机制清晰，速度快 | 无需追踪界面，可模拟复杂枝晶形貌与偏析 | 算法简单，易于实现 |
| **核心限制** | 多尺度耦合误差，参数标定要求高 | 仅能处理均匀/等温温度场 | 计算域极小，难以用于实际工程铸件 | 缺乏物理基础，无法定量预测 |

此外，与单独的有限元（FE）方法相比，单独FE仅能完成宏观温度场、流场和应力场的求解，不具备晶粒结构预测能力；与单独的CA方法相比，单独CA仅在均匀温度场的假设下完成小区域组织模拟，CAFE法则通过宏观FE耦合拓展至非均匀冷却条件下的实际工程件全尺寸组织预测[[S26,S31,S45]]。

## 软件集成与标准现状

- **ProCAST**：ProCAST v2004及后续版本已集成CAFE方法为核心的显微组织分析模块（即前述CAFÉ模块），支持直接调用高斯分布形核模型和KGT枝晶尖端生长动力学模型，可实现三维铸件凝固微观组织的高精度仿真[[S37,S75]]。
- **MAGMAsoft**：具备微观组织分析功能，可预测球墨铸铁组织中石墨球数及珠光体含量，但公开技术资料中未明确标注原生集成标准CAFE方法框架[[S2,S61]]。
- **AnyCasting**：内置基本凝固微观组织形成分析能力，公开技术文档中未明确标注原生集成CAFE方法模块[[S67,S72]]。
- **标准**：截至2026年，国内现行铸造行业基础标准如GB/T 5611《铸造术语》中未收录CAFE法条目，该方法暂未完成行业标准化定义[[S48,S71]]。

## 局限性

1. **计算效率瓶颈**：枝晶尖端尺寸与固液界面厚度相差3~4个数量级，宏观FE大网格与微米级CA细网格的耦合涉及大量双向插值迭代，三维大尺寸工程铸件全尺度串行模拟耗时往往超出常规工程允许范围[[S41]]。
2. **多尺度耦合误差**：双线性插值近似与宏微观时间步长不匹配均可引入系统误差，未在精密校准条件下，模拟结果与实测金相的晶粒尺寸偏差可超过15%[[S38]]。
3. **物理参数高敏感性**：CAFE模拟精度高度依赖预先标定的形核参数与KGT生长系数。以16Cr20Ni14Si2合金为例，经参数校准的模拟结果可达0.07%的误差，但未校准参数场景下偏差将显著增大[[S7]]。
4. **多元多相合金适用性受限**：现有公开可获取的CAFE适应热力学参数库多针对二元和简单三元合金开发。多元多相复杂合金需要手工重新拟合生长动力学系数并补充相图耦合计算，算法适配周期长，通用性不足[[S62]]。

## Sources
- S26: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/517e67e6-a5fe-4c5b-96c1-1b85392824bf/resource) (`517e67e6-a5fe-4c5b-96c1-1b85392824bf`)
- S75: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5dd046a-6d09-4419-9377-bee1308b3a85/resource) (`f5dd046a-6d09-4419-9377-bee1308b3a85`)
- S45: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92a4eeba-faae-477e-9596-e5adbbf25424/resource) (`92a4eeba-faae-477e-9596-e5adbbf25424`)
- S41: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8859f46b-9063-4c4d-8c97-03ef1f5a9218/resource) (`8859f46b-9063-4c4d-8c97-03ef1f5a9218`)
- S24: [铝合金机匣铸造工艺及数值模拟分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/509e8ac7-23f0-4f15-bca1-6b210d3cfb94/resource) (`509e8ac7-23f0-4f15-bca1-6b210d3cfb94`)
- S70: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S42: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a14f6fc-8302-4aa0-8268-75ac725cf37f/resource) (`8a14f6fc-8302-4aa0-8268-75ac725cf37f`)
- S48: [最新铸造标准应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/962a8dfd-1c9b-486d-ace1-9c3be4c63949/resource) (`962a8dfd-1c9b-486d-ace1-9c3be4c63949`)
- S71: [GB_T41972—2022《铸铁件铸造缺陷分类及命名》国家标准解读](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ecc26ba5-246b-4281-aebf-c06256a33f89/resource) (`ecc26ba5-246b-4281-aebf-c06256a33f89`)
- S62: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d7e1b035-beae-4459-be95-eaa845104008/resource) (`d7e1b035-beae-4459-be95-eaa845104008`)
- S38: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7cec895e-b453-469b-9612-d5895ec09fcf/resource) (`7cec895e-b453-469b-9612-d5895ec09fcf`)
- S52: [镁稀土合金激光选区熔化宏_微观组织跨尺度调控研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a6891e4f-fc6d-42d3-b5ae-1a9ad5b200ed/resource) (`a6891e4f-fc6d-42d3-b5ae-1a9ad5b200ed`)
- S46: [图1.1 CAFE模型，i、j、k为有限元节点](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/92d7fdfb-ef61-4deb-b202-bda1ca34c3e7/resource) (`92d7fdfb-ef61-4deb-b202-bda1ca34c3e7`)
- S17: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/36a68bc1-f9fe-4fc3-b529-c2790ff3fcab/resource) (`36a68bc1-f9fe-4fc3-b529-c2790ff3fcab`)
- S20: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44f5c4d2-4c18-4999-861c-da5e3ae51c82/resource) (`44f5c4d2-4c18-4999-861c-da5e3ae51c82`)
- S69: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ebb14ee0-82bc-4232-bb74-e93c89824d2c/resource) (`ebb14ee0-82bc-4232-bb74-e93c89824d2c`)
- S8: [S30432耐热不锈钢连铸方坯凝固组织及热裂倾向性数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19901788-f0e6-4c22-99c6-94b9f0d2ce7d/resource) (`19901788-f0e6-4c22-99c6-94b9f0d2ce7d`)
- S14: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2cfd5e8b-4f13-4589-98b0-23f452b07932/resource) (`2cfd5e8b-4f13-4589-98b0-23f452b07932`)
- S57: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c7cb25b8-d253-4227-92d1-127bc3ae0faa/resource) (`c7cb25b8-d253-4227-92d1-127bc3ae0faa`)
- S29: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5d1f42d2-faab-44d5-88bb-970fdbcc8b52/resource) (`5d1f42d2-faab-44d5-88bb-970fdbcc8b52`)
- S35: [钛合金TC4真空自耗熔炼铸锭质量控制基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/74a43b7a-3d7c-4982-9570-fddd42168bfa/resource) (`74a43b7a-3d7c-4982-9570-fddd42168bfa`)
- S23: [图2.3 体形核参数和面形核参数高斯分布示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4e8ec3e9-90b1-4328-9e61-b2d3708e78ab/resource) (`4e8ec3e9-90b1-4328-9e61-b2d3708e78ab`)
- S34: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/73f65a2e-0a39-4fa1-85b9-c3e5bf4aa246/resource) (`73f65a2e-0a39-4fa1-85b9-c3e5bf4aa246`)
- S39: [S30432耐热不锈钢连铸方坯凝固组织及热裂倾向性数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e7cb4b5-dc64-48f2-9534-00800738d89b/resource) (`7e7cb4b5-dc64-48f2-9534-00800738d89b`)
- S54: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b28143ed-7d3b-4917-bc3c-6e6658b93be8/resource) (`b28143ed-7d3b-4917-bc3c-6e6658b93be8`)
- S50: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99e1d1b4-6428-4cd7-a0ad-ac1a7f449c6d/resource) (`99e1d1b4-6428-4cd7-a0ad-ac1a7f449c6d`)
- S51: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c26a758-7ad0-4ce2-9cd7-5e3efcd009ac/resource) (`9c26a758-7ad0-4ce2-9cd7-5e3efcd009ac`)
- S25: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/513ec0da-6c73-49f1-a92c-01eac0b3010b/resource) (`513ec0da-6c73-49f1-a92c-01eac0b3010b`)
- S53: [钛合金TC4真空自耗熔炼铸锭质量控制基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa98b97d-b5ad-4307-be4d-eaf616476bca/resource) (`aa98b97d-b5ad-4307-be4d-eaf616476bca`)
- S47: [基于ProCAST砂型铸造高锰钢斗齿的工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93d9dba8-c607-455d-b4c0-2a53e06f97d4/resource) (`93d9dba8-c607-455d-b4c0-2a53e06f97d4`)
- S68: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e7fcaa63-7589-4f51-acf0-cf4c8a901265/resource) (`e7fcaa63-7589-4f51-acf0-cf4c8a901265`)
- S7: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18b28cee-92ba-47e2-905d-07beb59e57a1/resource) (`18b28cee-92ba-47e2-905d-07beb59e57a1`)
- S28: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5501fef9-db84-4b0a-939f-6f329f5401e9/resource) (`5501fef9-db84-4b0a-939f-6f329f5401e9`)
- S74: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3d9d46e-a897-4b8e-ab04-7aa22a125207/resource) (`f3d9d46e-a897-4b8e-ab04-7aa22a125207`)
- S15: [S30432耐热不锈钢连铸方坯凝固组织及热裂倾向性数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2d23ecff-97c7-4aaa-b1d3-edcf5279e16b/resource) (`2d23ecff-97c7-4aaa-b1d3-edcf5279e16b`)
- S66: [Mg-Al-Si系合金凝固与时效组织演化及力学性能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e3573307-851d-41ad-bf42-ad4831199de0/resource) (`e3573307-851d-41ad-bf42-ad4831199de0`)
- S16: [基于深度学习的42CrMo八角锭铸造参数预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/31357d3a-5280-488a-9708-9c7a9bd9331e/resource) (`31357d3a-5280-488a-9708-9c7a9bd9331e`)
- S30: [不同铸造工艺条件下工型异形件凝固组织数值模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6065e589-9db5-4051-ba53-4c4e0099c005/resource) (`6065e589-9db5-4051-ba53-4c4e0099c005`)
- S33: [中国材料工程大典 第19卷 材料铸造成形工程（下）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71a182ef-2cfc-45f6-ab1f-99aaeaae5eba/resource) (`71a182ef-2cfc-45f6-ab1f-99aaeaae5eba`)
- S18: [Q355钢连铸特厚板坯凝固结构模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4139c7c8-056b-4ca8-b86d-6423707d0fe3/resource) (`4139c7c8-056b-4ca8-b86d-6423707d0fe3`)
- S21: [金属液态成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4630ada2-31e0-4c8a-958d-22c0f2ff8bd0/resource) (`4630ada2-31e0-4c8a-958d-22c0f2ff8bd0`)
- S11: [低合金钢板坯与轧材均质化控制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/25924147-6f8d-4c5b-a28f-05599abd3717/resource) (`25924147-6f8d-4c5b-a28f-05599abd3717`)
- S73: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0d7c9d5-c5a6-4090-a641-5e0c9e283965/resource) (`f0d7c9d5-c5a6-4090-a641-5e0c9e283965`)
- S12: [铝合金离心铸造凝固过程数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/26041cf4-e2e1-4025-975e-5ccfb763ad39/resource) (`26041cf4-e2e1-4025-975e-5ccfb763ad39`)
- S64: [大型铸锻件缺陷分析图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd516e85-9ac9-44f5-90ea-41e86bceb5e9/resource) (`dd516e85-9ac9-44f5-90ea-41e86bceb5e9`)
- S9: [铸钢机车车钩精密铸造工艺及其凝固组织研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1ab61bc0-6a64-4145-b34f-75faf41470cd/resource) (`1ab61bc0-6a64-4145-b34f-75faf41470cd`)
- S36: [铝合金水泵座压铸模镶块冷却水道结构改进与压铸工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7a4738b0-9aed-443a-9c52-9cbb334a702e/resource) (`7a4738b0-9aed-443a-9c52-9cbb334a702e`)
- S6: [农用Al6082合金熔模铸造组织有限元模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/14c577b8-ceda-4bc0-9482-cc37ec05e91f/resource) (`14c577b8-ceda-4bc0-9482-cc37ec05e91f`)
- S58: [图5.22 SDAS及局部CAFE模拟对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8022ac1-4f3e-4495-bbb7-6b4358f0cf0c/resource) (`c8022ac1-4f3e-4495-bbb7-6b4358f0cf0c`)
- S10: [Al-Ti二元系温度-成分相图及CAFE模拟、实物图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24634c81-4fcf-4207-9652-487a6c408c0e/resource) (`24634c81-4fcf-4207-9652-487a6c408c0e`)
- S59: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c8b6f546-e4a4-4da2-9f72-63b58f40a5ef/resource) (`c8b6f546-e4a4-4da2-9f72-63b58f40a5ef`)
- S32: [corrosion resistance of aluminum and magnesium alloys understanding performance and testing__520a2300d4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f0ad2a2-cb30-4c6a-898f-f6b3a9c1bd61/resource) (`6f0ad2a2-cb30-4c6a-898f-f6b3a9c1bd61`)
- S40: [铸造数值模拟软件技术及应用进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/83c6fb94-abde-408c-9989-2652fd7a7006/resource) (`83c6fb94-abde-408c-9989-2652fd7a7006`)
- S13: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c4c6421-0ff1-4ab7-9692-ac5967d677a8/resource) (`2c4c6421-0ff1-4ab7-9692-ac5967d677a8`)
- S43: [双辊铸轧高性能Al-Mg-Si系合金凝固行为及组织调控](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8da005e9-4fc8-4417-a168-94fbdd7cdf1e/resource) (`8da005e9-4fc8-4417-a168-94fbdd7cdf1e`)
- S44: [铝及铝合金铸轧成形与裂纹扩展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91cb450f-151d-4489-95b0-1a4bd4608757/resource) (`91cb450f-151d-4489-95b0-1a4bd4608757`)
- S31: [基于CAFE法对16Cr20Ni14Si2熔模铸造凝固组织的模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f09739e-fbe5-496d-9057-fa42a5b6b8e2/resource) (`6f09739e-fbe5-496d-9057-fa42a5b6b8e2`)
- S37: [显示ProCAST与DataCAST版本信息的命令行窗口](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bd4ee2c-ec8e-4846-a216-284da02d99fe/resource) (`7bd4ee2c-ec8e-4846-a216-284da02d99fe`)
- S2: [材料加工工程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/078124b8-4f7e-4a47-a3ec-338bab4a0f15/resource) (`078124b8-4f7e-4a47-a3ec-338bab4a0f15`)
- S61: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf063c89-7f01-49f0-bec3-84d9babc20a4/resource) (`cf063c89-7f01-49f0-bec3-84d9babc20a4`)
- S67: [铝合金磁电机盖压铸成型数值模拟及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e562be0d-a62e-438a-ab41-56d9bd1c800a/resource) (`e562be0d-a62e-438a-ab41-56d9bd1c800a`)
- S72: [基于传热原理的热节快速分析模型及应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed3205c1-6263-447d-81d5-a9507e87a7a4/resource) (`ed3205c1-6263-447d-81d5-a9507e87a7a4`)