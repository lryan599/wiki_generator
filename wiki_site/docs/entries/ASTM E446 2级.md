---
version: "v1"
generated_at: "2026-06-18T19:30:28+00:00"
confidence_score: 0.89
confidence_level: "very_high"
confidence_basis:
  cited_sources: 9
  source_quality_score: 0.9
  freshness_score: 0.81
  evidence_coverage_score: 1.0
---

## 概述

ASTM E446 2级是在钢铸件射线检测中广泛使用的缺陷严重程度验收等级。该等级出自ASTM E446/E446M标准《Standard Reference Radiographs for Steel Castings up to 2 in. (51 mm) in Thickness》，现行最新版本为ASTM E446/E446M-20，标准首次发布于1962年，历经多次修订[[S7]]。

该标准提供一套从轻微到严重的系列参考射线照片，作为铸件内部缺陷评级的基准图谱[[S9,S11]]。Severity Level 2（II级）在标准定义的五个严重程度等级中属于中等偏严格的级别，允许的缺陷总量远低于3、4、5级，仅略高于最严格的1级[[S9]]。

## 标准适用范围

ASTM E446仅适用于**钢铸件**，不适用于铝合金、镁合金、铜合金等有色金属铸件[[S13]]。有色金属铸件须使用相应的专属ASTM标准，如ASTM E505适用于铝/镁压铸件射线检测[[S10]]。

标准明确规定的适用壁厚范围为**厚度≤2英寸（51 mm）**的薄截面钢铸件[[S9,S13]]。该标准与另外两个标准共同构成覆盖不同壁厚的完整体系[[S7]]：

| 标准编号 | 适用壁厚范围 |
|----------|--------------|
| ASTM E446 | ≤2 in (51 mm) |
| ASTM E186 | 2~4½ in (51~114 mm) |
| ASTM E280 | 4½~12 in (114~305 mm) |

## 缺陷类型、等级体系与判断依据

### 缺陷类型

ASTM E446标准覆盖以下缺陷类型[[S9]]：

- **Category A（气体气孔）**：圆形或椭圆形、边缘光滑的暗斑，可单个离散分布或小范围聚集[[S6]]，分级Severity Level 1~5
- **Category B（砂渣夹杂）**：分级Severity Level 1~5
- **Category C（缩孔）**：细分为CA、CB、CC、CD四个子类型，各子类型分别分级Severity Level 1~5
- 裂纹、热裂：标准各提供一个未分级示例，不再纳入常规分级体系

### 严重程度等级体系

ASTM E446的缺陷严重程度划分为**Severity Level 1至Severity Level 5**五个等级[[S9]]，1级最严格（允许缺陷最少），5级最宽松（允许缺陷最多）。II级即Severity Level 2，在中高压承压铸钢件验收中为常用等级[[S9]]。

### 基于缺陷类型的差异化验收

**描述提示中“气孔缺陷需达到该标准的II级，其余缺陷需达到III级”的说法需结合具体应用规范来理解。** ASTM E446标准自身并不为所有缺陷类型统一规定一个等级，而是在第4.2节中明确指出，应针对每一类不连续缺陷分别指定严重程度等级，并给出典型例证：收缩缺陷可指定Severity Level 2，而气孔缺陷可指定Severity Level 3，因为后者对拉伸力学性能的损害通常较小[[S4]]。

在承压设备领域，ASME锅炉及压力容器规范第VIII卷引用ASTM E446时，对缺陷接受等级作出了明确划分[[S13]]：

| 缺陷类别 | 最大允许严重程度等级 |
|----------|---------------------|
| 裂纹、热裂 | 0（不可接受） |
| 气孔 | 2 |
| 夹杂物 | 2 |
| 缩孔 | 2 |

行业普遍存在将不同缺陷类型设定差异化验收等级的实践，该应用模式在钢铸件射线检测标准体系中已有明确规定[[S13]]。

## 射线影像评定方法

ASTM E446标准规定了评定程序[[S4]]：

1. 将生产铸件的射线底片与相同能量等级的标准参考射线照片进行比对；
2. 若生产底片中的缺陷严重程度等于或优于参考图谱指定等级，则该部位可被接收；
3. 若生产底片中的缺陷严重程度超过参考图谱，则该部位应判定为不合格。

标准提供了三套不同能量等级的参考底片（250 kV X射线、1 MV X射线/Ir-192、2~4 MV X射线/Co-60），评定时应选用与实际透照能量相当的图谱[[S9]]。

## 配套参考图谱

ASTM E446官方配套的参考射线照片包含10张编号为1至10的梯度参考放射照片，展示从极轻微到严重的不同类型铸件内部缺陷形态，用于不同严重等级的实际比对判定[[S11]]。该系列图谱涵盖了气孔、夹渣、缩孔等各类缺陷在五个严重程度等级下的典型影像表现。

如图所示，ASTM E446参考图谱系列展示了从轻微到严重的缺陷形态梯度分布，为II级评定提供可视化依据[[S11]]：

![ASTM E446配套参考射线照片图谱”（编号1至10），呈现从轻微到严重的缺陷形态梯度分布，用于不同严重等级的实际比对判定](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2abbdc8-4760-4bfb-9712-c9f12db99a31/resource)

## 与其他标准的关联

在ASTM体系中，E446与E186、E280构成不同壁厚的钢铸件射线检测标准组[[S7]]。在有色金属压铸领域，铝合金和镁合金压铸件使用ASTM E505（原E155体系）标准进行射线检测分级，其所定义的缺陷外观特征描述与E446中的Category A（气孔）定义相似（圆形或椭圆形、边缘光滑的暗斑，可单个或聚集分布）[[S6]]。

在国际标准体系中，与铸件射线检测相关的ISO标准包括ISO 4993《钢铁铸件射线检测》、ISO 5579《金属材料射线检测基本规则》等，构成与ASTM体系并行的技术路径[[S5]]。

## 在样件评定中的应用要点

涉及钢铸件样件的射线检测时，适用ASTM E446 II级验收应遵循以下流程[[S4]]：

- 在正式规范、图纸或订单中明确指定适用的缺陷类别及各缺陷类别的严重程度等级；
- 指定射线检测覆盖范围、透照工艺（按ASTM E94和E142）以及所需像质水平；
- 评定底片密度宜与参考射线照片密度接近，以获得最佳比对结果（建议底片密度控制在2.00~2.25，实际评定可参照1.5~3.5的可接受范围）[[S9]]。

ASME第VIII卷中收录的“钢铸件缺陷检验等级要求表”为样件评定提供了直接的可操作依据，评定者可将受测底片中的各类线性缺陷与体积型缺陷与ASTM E446标准参考图谱逐一对照，确定其是否满足II级验收要求[[S2]]。

## Sources
- S7: [ASTM E 186/E 280/E 446 钢铸件射线照相参考图谱](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7f014dcf-ac42-45c2-8b57-dd8ca84555a3/resource) (`7f014dcf-ac42-45c2-8b57-dd8ca84555a3`)
- S9: [1991 annual book of astm standards section 1 lron and steel products vol__d9cf5303c8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a9b4358d-e068-4046-90d7-a2dc5fe46e37/resource) (`a9b4358d-e068-4046-90d7-a2dc5fe46e37`)
- S11: [Reference Radiographs E 446](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2abbdc8-4760-4bfb-9712-c9f12db99a31/resource) (`e2abbdc8-4760-4bfb-9712-c9f12db99a31`)
- S13: [钢铸件射线检测缺陷最大允许严重程度等级](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9c36b0d-99dc-4f61-90bd-3552cf12273d/resource) (`f9c36b0d-99dc-4f61-90bd-3552cf12273d`)
- S10: [铝合金压铸件实物（模流分析验证对象）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c931f293-10c7-458b-b510-f32bde5cfc50/resource) (`c931f293-10c7-458b-b510-f32bde5cfc50`)
- S6: [1991 annual book of astm standards section 2 nonferrous metal products volume 0202 die cast metals aluminum and magne...](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6bdca45b-8ca3-4705-acc6-beada0fac4f7/resource) (`6bdca45b-8ca3-4705-acc6-beada0fac4f7`)
- S4: [1991 annual book of astm standards section 1 iron and steel products vol__e3a5133ba7](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/519c69bd-29fa-49a6-ad0b-df99956fa917/resource) (`519c69bd-29fa-49a6-ad0b-df99956fa917`)
- S5: [0211_f3e3a822f8666b66_Industrial_radiography](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/58981e05-ccb0-4455-9a5c-b127f8162831/resource) (`58981e05-ccb0-4455-9a5c-b127f8162831`)
- S2: [钢铸件缺陷检验等级要求](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/27ac456b-bc3b-42f4-8229-3d7b38dea4ba/resource) (`27ac456b-bc3b-42f4-8229-3d7b38dea4ba`)