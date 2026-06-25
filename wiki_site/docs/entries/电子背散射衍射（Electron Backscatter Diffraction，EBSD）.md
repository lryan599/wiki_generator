---
version: "v1"
generated_at: "2026-06-18T14:33:33+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 29
  source_quality_score: 0.86
  freshness_score: 0.82
  evidence_coverage_score: 1.0
---

## 概述

电子背散射衍射（Electron Backscatter Diffraction, EBSD）是一种基于扫描电子显微镜（SEM）的附属表征技术，用于获取块体晶态或多晶材料的微区晶体学特征。EBSD 具备空间分辨率高、角分辨率可接受、适配各类电子束仪器以及可实现自动数据采集与取向制图的特点[[S25,S15,S17]]。该技术早期也被称为广角菊池衍射（wide-angle Kikuchi diffraction）、背散射菊池衍射（Backscatter Kikuchi Diffraction, BKD）或背散射电子菊池衍射（Backscatter Electron Kikuchi Diffraction, BEKD）[[S15,S17]]。在压铸领域，EBSD 被广泛用于铝合金、镁合金等压铸件的晶粒取向、织构、晶界特征分布、相鉴定以及残余应变分析，是连接压铸工艺参数与微观组织演变的核心表征手段。

## 基本原理

### 菊池花样的产生

当电子束轰击金属样品表面时，入射电子在样品表层下发生非弹性散射并向各方向扩散。当散射电子满足布拉格衍射条件时，每一族晶面会产生一对衍射锥，其半顶角接近180°（近似平坦）。这对衍射锥与放置在样品前方的磷光屏相交，形成一对平行的菊池线（Kikuchi lines），两条菊池线的角间距为2倍布拉格角，与对应晶面的晶面间距成反比[[S6]]。

![电子背散射衍射基本工作原理示意图，展示电子束轰击倾斜样品后在磷光屏上形成衍射图案的完整光路](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c60182b3-0777-4cab-8aa4-fb36b15eeced/resource)

### 自动标定算法

EBSD 自动标定的核心流程包括三个步骤[[S35,S2,S37]]：

1. **预先生成晶面夹角库**：测试前向系统输入待分析样品的晶体结构，系统自动生成对应所有晶面的晶面夹角列表。
2. **衍射带指标化**：通过霍夫变换（Hough Transform）提取采集到的菊池衍射带位置，将实测衍射带夹角集合与理论晶面夹角库进行匹配，完成各衍射带的指数标定。
3. **取向计算**：定义参考坐标系，经过三次欧拉角旋转变换，得到晶体坐标系与SEM样品参考坐标系的转换矩阵，最终输出对应微区的晶体取向。

## EBSD系统组成与操作条件

### 硬件组成

EBSD 系统的硬件部分主要包括[[S25,S35]]：
- **闪烁屏（磷光屏）**：涂覆磷光材料的玻璃屏，用于接收背散射电子衍射信号；
- **低光照相机**：可聚焦于磷光屏的CCD或CMOS相机；
- **机械接口**：适配SEM真空腔，保证磷光屏和相机在样品腔内的正确定位；
- **电子束及样品台控制接口**：用于实现无人值守的自动逐点扫描。

在常规立式SEM中，EBSD测试要求样品与水平面夹角为60°~80°，通常采用70°倾斜[[S25,S35]]。

![EBSD系统衍射几何关系示意图，标注入射电子束、样品、衍射花样与相机之间的空间位置关系](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4360014f-c808-406b-b4ab-b601ff659a73/resource)

### 典型测试参数

| 参数 | 典型范围/值 | 备注 |
|------|------------|------|
| 加速电压 | 10~30 kV（最低2.5 kV） | 常规测试常用15~20 kV[[S5,S25,S36]] |
| 入射束流 | ~1 nA | 场发射SEM常用[[S25]] |
| 样品倾斜角 | 60°~80°（常规70°） | 参见ISO 24173-2009[[S35]] |
| 工作距离 | 15~20 mm（压铸镁合金） | 视SEM型号与磷光屏位置调整[[S4]] |
| 菊池花样采集速度 | 最高50~60帧/秒 | 慢扫描CCD典型帧率60~90帧/秒，实用标定上限40~50个点/秒[[S36,S21]] |
| 侧向空间分辨率 | 可达10 nm（场发射SEM） | 取决于SEM类型和样品原子序数[[S17,S25]] |

压铸镁合金EBSD测试的具体参数示例：加速电压20 kV，样品倾斜70°，工作距离15~20 mm，扫描步长0.3 μm，统计采集晶粒总数大于300[[S4]]。压铸铝合金薄壁件测试可采用加速电压15 kV、扫描步长1 μm[[S38]]。

### EBSD探测器类型

目前主流商用EBSD探测器可分为三类[[S21,S11,S5]]：

| 类型 | 特点 |
|------|------|
| CCD相机（含慢扫描CCD） | 慢扫描CCD兼具高速成像与高质量花样采集能力，典型帧率60~90帧/秒，实用标定上限40~50个点/秒 |
| CMOS相机 | 在集成度和采集帧率方面优于CCD |
| 直接电子探测器 | 无需磷光屏转换即可直接捕获电子信号，支持低至3 kV入射电子能量下获得高质量菊池花样 |

## 在压铸中的核心应用

### 晶粒尺寸与形态统计

EBSD可为压铸件提供定量的晶粒尺寸与形态分布数据。针对A360铝合金高压压铸（HPDC）冷却盖板试样的研究表明，经工艺优化后（快压射速度2.5 m/s、浇注温度630℃、模具预热温度220℃），沿流线不同位置的平均晶粒尺寸分别由优化前的13.12 μm/12.58 μm/12.96 μm降至11.90 μm/11.84 μm/12.79 μm，两条工艺下晶粒尺寸从近内浇口到远内浇口均呈现先减小后增大的分布规律，试样中均存在尺寸大于30 μm的压室预结晶（ESCs）组织[[S10]]。

![高压压铸铝合金5mm厚度样品中心区域的EBSD晶粒图，展示HPDC工艺下晶粒的尺寸分布特征，标尺100 μm](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bdc130cb-9f86-4d97-8c5d-d0daffd8f824/resource)

HPDC镁合金中，冷室高压压铸与热室高压压铸AZ91合金试样的平均晶粒尺寸分别较触变射铸同合金试样（约10.5 μm）增大20%和70%[[S18]]。Mg-4Al-5RE系HPDC镁合金沿厚度方向呈现明显的晶粒尺寸梯度：从表层到心部由5.5 μm逐步增大到9.5 μm，该梯度分布由不同位置冷却速率差异和心部聚集的ESCs组织共同导致[[S41]]。

### 晶体取向与织构分析

EBSD反极图（IPF）是压铸件织构分析的常规输出形式。对AZ91压铸镁合金的EBSD测试表明，晶格整体无明显择优取向，织构呈随机分布特征，仅局部存在小范围多晶粒聚集成晶团的取向一致性区域[[S18]]。这种近随机织构是HPDC快速凝固条件下晶体非择优生长的典型特征。

对于有热处理工序的压铸件，EBSD可揭示固溶时效对晶粒取向和织构的影响。针对Al-10Si-0.3Mg高压压铸薄壁件的研究表明，铸态试样沿厚度方向存在显著的晶粒尺寸梯度（表层细晶层、心部粗晶层），经适配的固溶时效热处理后该梯度完全消失，表层与心部晶粒尺寸无显著差异[[S38]]。

### 晶界特征分布与CSL晶界分析

EBSD是开展晶界特征分布（Grain Boundary Character Distribution, GBCD）表征的核心工具。通过对逐点晶体取向数据的采集，提取相邻晶粒的旋转轴-取向差轴角对，结合重合位置点阵（CSL）模型和Brandon判据，可以对Σ≤29的特殊低能晶界进行分类统计，输出形式包括长度分数和数量分数两种[[S33,S14,S42]]。该分析对理解压铸合金沿晶开裂、腐蚀敏感性与特殊晶界占比的关联规律具有重要意义，可支撑压铸合金晶界工程优化。

### 相鉴定与分布

EBSD结合能谱分析（EDS）是压铸合金多相精准鉴定的常规手段[[S33,S2]]。其基本流程为：先通过能谱获取目标相的元素组成，在数据库中匹配候选相晶体结构，再结合EBSD采集的菊池衍射花样完成标定。在压铸铝合金中可区分α-Al基体与共晶Si相，在镁合金中可区分α-Mg基体、共晶Mg₁₇Al₁₂相以及富稀土金属间化合物等不同相，实现初生相、共晶相和金属间化合物的定量化统计。

### 微观应变与残余应力评估

EBSD的局部取向差图（Kernel Average Misorientation, KAM）是压铸试样微区残余应变可视化的有效手段。相邻测试点间的取向差数值直接对应晶格畸变程度，取向差越大则该区域残余应变水平越高。通过预先建立标样的取向差-应变校准关系，可进一步实现微区应变的定量表征[[S33]]。

### 压铸缺陷解析

HPDC镁合金、铝合金热裂缺陷形成于凝固后期高固相率区域。EBSD表征可在热裂裂纹周边位置观测到明显的局部取向聚集畸变特征，其应力集中程度显著高于周边无缺陷区域。同时，热裂沿晶界扩展的路径可通过EBSD晶界取向差数据精准重构，为压铸热裂形成机制研究提供晶体学层面的直接证据[[S13,S26]]。

压铸试样中孔隙、微裂纹、夹杂等缺陷周边区域的EBSD标定率往往显著下降，其核心原因是缺陷附近存在严重的晶格畸变和局部高应力集中，同时缺陷边缘表面不平整导致菊池花样完全失真[[S23]]。

## 试样的制备要求

EBSD的信号采集深度仅为样品表层下10~40 nm范围[[S25,S4]]，对制样引入的表面残余应变层极其敏感，极薄的形变层就会导致菊池花样畸变，大幅降低标定匹配率。因此，压铸合金EBSD试样制备需满足以下要求：

### 压铸镁合金制样流程

以Mg-4Al-5RE系压铸镁合金为例，推荐的EBSD制样流程为[[S4]]：
1. 依次使用300#、1200#、3000#、7000#水磨砂纸打磨；
2. 用1 μm金刚石悬浮液（煤油作为润滑剂）抛光8 min；
3. 用0.05 μm硅乳胶溶液（OPS）抛光12 min；
4. 用4 vol.%硝酸酒精溶液腐蚀1~2 s，去除表面残余应力层。

该流程可有效避免机械制样引入的机械孪晶假象。

### 压铸铝合金制样方法

对于A360等压铸铝合金，推荐在机械抛光后采用氩离子束抛光（如Gatan697型离子抛光机）作为最终精修工序，以进一步去除机械抛光残留的极薄变形层，获取满足高标定率要求的试样表面[[S27]]。

铝合金等软质金属也可采用“机械粗抛+电解抛光”的组合工艺：机械抛光依次采用5 μm、2.5 μm、1 μm金刚石抛光膏完成，随后通过电解抛光完全消除亚表层应变，适配压铸铝合金EBSD测试需求[[S12]]。

## 与其他表征技术的对比与互补

### 与XRD织构分析的对比

XRD测试得到的是毫米级大区域的统计平均织构结果，无法区分晶粒尺度下的取向分布与晶界特征；EBSD可逐点采集微米/纳米级微区取向数据，同时获得晶粒尺寸、晶界类型、应变梯度等多维度信息。二者协同可实现大区域织构统计与微区织构异质性的跨尺度关联分析[[S1,S24]]。

### 与SEM-EDS的协同

EBSD无法直接获得元素分布信息。将EBSD探测器与EDS探测器并排布置在SEM样品腔同侧，可在同一次扫描中同步获取微区取向与元素分布数据，实现第二相粒子取向关系、成分偏析对应织构演变的关联表征[[S28,S11]]。

### 与TEM微区取向分析的对比

| 特征 | EBSD | TEM |
|------|------|-----|
| 空间分辨率 | 可达10 nm量级 | 近原子级 |
| 可扫描区域 | 数百微米级 | 极小区域 |
| 统计代表性 | 强 | 弱 |
| 样品制备 | 相对简便 | 难度高 |
| 典型应用 | 大规模取向制图、织构统计 | 纳米尺度缺陷位向关系 |

二者协同可实现纳米尺度缺陷精细表征与宏观尺度多晶织构统计的跨尺度关联[[S1,S25]]。

## 衍生技术

### 透射菊池衍射（TKD）

透射菊池衍射（Transmission Kikuchi Diffraction, TKD）适用于超细纳米晶材料的取向表征，采用同轴配置可实现快速准确测量。但其最大可检测视场远小于常规EBSD，因此获得的位向差分布、织构等统计数据代表性弱于常规EBSD，适合表征晶粒尺寸小于100 nm的超细晶样品[[S34]]。

### 3D-EBSD

常规EBSD结合聚焦离子束（FIB）逐层铣削技术，可对样品进行逐层扫描采集表面取向数据，最终重构获得样品的三维空间取向数据集，实现三维尺度下的晶界、织构和取向梯度表征[[S24]]。

## 局限性与挑战

1. **对表面状态敏感**：EBSD信号采集深度仅10~40 nm，表面残余应变层会严重降低标定匹配率[[S25,S4]]。
2. **空间分辨率受限于电子束作用区**：商用场发射SEM搭载EBSD系统的最高侧向空间分辨率约10 nm，无法对尺度小于该极限的压铸纳米级析出相进行精准表征[[S17]]。
3. **低对称度相标定困难**：压铸多相合金中低对称度的第二相、亚微米级细晶压铸相，由于菊池带数量少、衬度弱，会出现标定匹配率明显下降的问题，需配套能谱元素分析辅助完成相识别[[S8]]。
4. **缺陷区域无法标定**：孔隙、微裂纹、夹杂等缺陷周边区域因严重晶格畸变和表面不平整，导致菊池花样完全失真，无法获得有效标定[[S23]]。

## 相关标准

现行EBSD相关国际标准为ISO 24173-2009（与ASTM E2627核心规范对齐），该标准明确了EBSD分析系统的组成框架、样品倾斜要求、花样标定流程以及晶粒尺寸与织构等参数输出的规范性要求，是通用EBSD测试的基础执行依据[[S35]]。

## Sources
- S25: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aceec2e0-894e-4ce7-89b9-1e6056d0b39b/resource) (`aceec2e0-894e-4ce7-89b9-1e6056d0b39b`)
- S15: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/655fc5e3-d811-4067-8148-92da22ae63b6/resource) (`655fc5e3-d811-4067-8148-92da22ae63b6`)
- S17: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7098aaa1-9dc3-422a-b3b4-9c33e130954a/resource) (`7098aaa1-9dc3-422a-b3b4-9c33e130954a`)
- S6: [aluminium alloys theory and applications__f2d28f5a78](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2b765a46-3344-4297-b1dd-5632b9cbcf29/resource) (`2b765a46-3344-4297-b1dd-5632b9cbcf29`)
- S35: [铝合金的激光焊接及性能评价](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cfa3bf42-e550-4797-b58c-87ac7b04e37a/resource) (`cfa3bf42-e550-4797-b58c-87ac7b04e37a`)
- S2: [铝合金的激光焊接及性能评价](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12c8f98d-f069-4ad5-8786-50d47e4a84e4/resource) (`12c8f98d-f069-4ad5-8786-50d47e4a84e4`)
- S37: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4b74529-4b07-4d76-8708-83d0b16e86b0/resource) (`d4b74529-4b07-4d76-8708-83d0b16e86b0`)
- S5: [characterisation and control of defects in semiconductors__2322662471](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22da0210-cc0d-4a32-8a52-4fe81225cba4/resource) (`22da0210-cc0d-4a32-8a52-4fe81225cba4`)
- S36: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d35e1b38-cae2-440d-91af-defeb8b03c0e/resource) (`d35e1b38-cae2-440d-91af-defeb8b03c0e`)
- S4: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f5411d6-1a1b-4089-ad91-9895b6f56414/resource) (`1f5411d6-1a1b-4089-ad91-9895b6f56414`)
- S21: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b460fec-aa18-4280-8fe8-e39d04be46b0/resource) (`9b460fec-aa18-4280-8fe8-e39d04be46b0`)
- S38: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/de2aa6b4-2b97-4d9e-b78f-62b5884eb031/resource) (`de2aa6b4-2b97-4d9e-b78f-62b5884eb031`)
- S11: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/51f23f5c-b45f-4ecf-8519-50ff6d4131ec/resource) (`51f23f5c-b45f-4ecf-8519-50ff6d4131ec`)
- S10: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a9d4e80-5ac8-4a38-b0fa-1ba74f51a1c3/resource) (`4a9d4e80-5ac8-4a38-b0fa-1ba74f51a1c3`)
- S18: [镁合金半固态触变射铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/72922439-eb49-4892-b8e9-0591f153a3d6/resource) (`72922439-eb49-4892-b8e9-0591f153a3d6`)
- S41: [Mg-4Al-5RE-xGd（wt.%）压铸镁合金组织性能及强韧化机制研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f1258f06-fe0d-4a3c-9a8c-cac647f09270/resource) (`f1258f06-fe0d-4a3c-9a8c-cac647f09270`)
- S33: [铝合金的激光焊接及性能评价](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c60cd57b-d8d3-4e34-b1ef-ae9917156b1a/resource) (`c60cd57b-d8d3-4e34-b1ef-ae9917156b1a`)
- S14: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/621e4c30-abef-4812-8351-fbd5989a8ea4/resource) (`621e4c30-abef-4812-8351-fbd5989a8ea4`)
- S42: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f6e28510-69c8-4c4f-b181-4922eb6bb442/resource) (`f6e28510-69c8-4c4f-b181-4922eb6bb442`)
- S13: [镁合金一体化压铸缺陷控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/59a31f25-71e7-4a09-9426-f3724f773e6a/resource) (`59a31f25-71e7-4a09-9426-f3724f773e6a`)
- S26: [镁合金一体化压铸缺陷控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ada11852-8491-4716-ae76-ab93c1100ea7/resource) (`ada11852-8491-4716-ae76-ab93c1100ea7`)
- S23: [casting and solidification of light alloys__06e9012dec](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9bd1012-8bf1-497f-8187-130b28cd1461/resource) (`a9bd1012-8bf1-497f-8187-130b28cd1461`)
- S27: [A360铝合金冷却盖板压铸工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ae1fec2d-24c7-4ed8-bdec-c6334de35663/resource) (`ae1fec2d-24c7-4ed8-bdec-c6334de35663`)
- S12: [铝合金精锻成形技术及设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/52a2c985-493f-4196-8557-5d94c61d9514/resource) (`52a2c985-493f-4196-8557-5d94c61d9514`)
- S1: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0145eb27-8393-47ea-804d-ccf579a0ba51/resource) (`0145eb27-8393-47ea-804d-ccf579a0ba51`)
- S24: [铝合金的激光焊接及性能评价](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aa34c824-2b90-4e7d-9f36-4ed219fddd3e/resource) (`aa34c824-2b90-4e7d-9f36-4ed219fddd3e`)
- S28: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aee6e933-0224-45ca-b8db-ada3cf3b6555/resource) (`aee6e933-0224-45ca-b8db-ada3cf3b6555`)
- S34: [design of alloy metals for low mass structures__b942e89304](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cb1d67dd-b8e4-458e-b794-5e5b8802ab29/resource) (`cb1d67dd-b8e4-458e-b794-5e5b8802ab29`)
- S8: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/323f89a3-b776-4fcc-9c46-0adbea35a221/resource) (`323f89a3-b776-4fcc-9c46-0adbea35a221`)