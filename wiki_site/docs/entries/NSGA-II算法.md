---
version: "v1"
generated_at: "2026-06-18T17:15:36+00:00"
confidence_score: 0.88
confidence_level: "very_high"
confidence_basis:
  cited_sources: 27
  source_quality_score: 0.83
  freshness_score: 0.95
  evidence_coverage_score: 1.0
---

## 概述

**带精英策略的快速非支配排序遗传算法**（Elitist Non-dominated Sorting Genetic Algorithm，简称 **NSGA-II**，也常写作 **NSGA2**）是由 Kalyanmoy Deb 于2000年提出的一种多目标进化算法[[S30,S23,S19]]。该算法是对初代 NSGA 的改进版本，通过引入快速非支配排序、拥挤度距离计算和精英保留策略三大核心机制，在求解效率和结果质量上均有显著提升[[S17,S19]]。NSGA-II 是目前应用最广泛的多目标优化基准算法之一，已成为其他多目标优化算法进行性能对比的参照标准[[S23]]。

## 算法类别

NSGA-II 属于：

- **多目标进化算法（MOEA）**：以群体搜索为基础，在一次运行中可获得多个 Pareto 最优解[[S23,S30]]；
- **基于 Pareto 支配的优化方法**：通过个体之间的支配关系定义解的优劣，而非将多目标聚合为单一指标[[S17,S21]]；
- **随机优化算法**下的**进化算法**分支中的**遗传算法**子类[[S21]]。

![优化算法分类](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c14e4092-bcf4-4074-aad8-445fe5ed7e35/resource)

**图1 优化算法的层级分类结构**：随机算法分支下包含进化算法和遗传算法子类，NSGA-II 属于此范畴[[S21]]。

## 核心机制

### 快速非支配排序

将种群中的个体按照 Pareto 支配关系逐层划为非支配层级：第一层为当前最优 Pareto 前沿，第二层为剔除第一层个体后剩余种群的最优前沿，以此类推[[S30,S16]]。该排序方法可有效降低计算复杂度，避免大量无效评估劣质个体[[S16]]。

### 拥挤度距离

针对同一非支配层级下的所有个体，沿每个目标维度排序后，计算个体两侧相邻点间的归一化目标距离之和，等于由相邻解在目标空间坐标作为顶点所构成超立方体的边长总和；边缘个体的拥挤度设为无穷大[[S17,S19,S18]]。拥挤度越高表示个体在目标空间分布越稀疏，可有效维持种群多样性，无需额外设置共享半径参数[[S18]]。

### 精英保留策略

每一代将当前父代种群和经选择、交叉、变异生成的子代种群合并为规模 2N 的混合种群，执行非支配排序和拥挤度筛选，优先选取排名靠前的完整非支配层级个体进入下一代父代种群，最后不足的份额从下一个未完全入选的非支配层级中按拥挤度降序选取补充[[S17,S24,S19]]。该策略确保前代所有精英解都有机会保留到下一代，避免优质解在遗传操作中被破坏[[S17,S24]]。

## 算法流程

NSGA-II 的标准执行步骤如下[[S26,S23,S27]]：

| 步骤 | 操作 |
|------|------|
| Step 1 | 预设进化参数（种群规模 N、交叉概率、变异概率、最大迭代次数），随机生成初始父代种群 Pₜ (t=0) |
| Step 2 | 对 Pₜ 执行二元锦标赛选择、交叉和变异操作，生成子代种群 Qₜ（规模 N） |
| Step 3 | 合并 Pₜ 和 Qₜ 为规模 2N 的混合种群 Rₜ，执行快速非支配排序和拥挤度计算，优先选取非支配层级靠前的个体，不足时从后续层级按拥挤度降序补充，得到新一代父代种群 Pₜ₊₁ |
| Step 4 | 令 t=t+1；若达到最大进化代数则终止并输出最终 Pareto 解集，否则返回 Step 2 |

![NSGA-II 算法完整流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19844181-9054-4514-b621-5addfa8d7962/resource)

**图2 NSGA-II 算法完整逻辑流程**：涵盖初始化种群、生成首代子群、合并父代子代、非支配排序、拥挤度计算、迭代判断与终止等全部步骤[[S9]]。

![NSGA-II 简化流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/568bb8b1-ef61-4a99-bb41-37029ae9fb04/resource)

**图3 NSGA-II 简化流程示意图**：标注了种群规模 N 和迭代计数 t 的演进逻辑，清晰展示父代子代合并构造混合非支配解集的核心操作路径[[S13]]。

## 关键参数

NSGA-II 的典型推荐参数范围及作用如下表所示[[S2,S24,S27,S28,S1]]：

| 参数 | 推荐取值范围 | 典型实测值 | 作用说明 |
|------|-------------|-----------|---------|
| 种群规模 N | 20～200（压铸场景常用 50～200） | 50 或 200 | 增大可提升 Pareto 解集多样性，但加长计算耗时 |
| 选择策略 | 二元锦标赛选择 | - | 基于拥挤度比较算子选择个体 |
| 交叉算子 | 模拟二进制交叉（SBX） | - | 推荐默认算子 |
| 交叉概率 Pc | 0.7～0.9 | 0.9 | 过高易破坏优质解结构，过低则搜索效率不足 |
| 变异算子 | 多项式变异（PM） | - | 推荐默认算子 |
| 变异概率 Pm | 0.1～0.3 | 0.1 | 过小易陷入局部最优，过大则退化为随机搜索 |

在 A356 铝合金缸盖压铸多目标优化工程实践中，NSGA-II 的典型参数配置如下[[S28]]：

| 参数 | 数值 |
|------|------|
| 种群数量 | 12 |
| 迭代次数 | 60 |
| 交叉概率 | 0.9 |

## 与原 NSGA 的对比优势

NSGA-II 相较于初代 NSGA 的核心改进如下[[S19,S16,S7]]：

| 对比维度 | 原 NSGA | NSGA-II |
|----------|---------|---------|
| 排序效率 | 非支配排序计算复杂度高 | 引入**快速非支配排序**，大幅降低计算复杂度 |
| 多样性维持 | 需手动设置共享半径参数 | 采用**拥挤度机制**自动维持分布均匀性，无需额外参数 |
| 解保留策略 | 无精英保留，优质解可能在遗传操作中丢失 | 新增**精英保留策略**，将前代优质解直接合并进入下一代筛选，显著提升收敛速度 |

## 性能评价指标

常用的多目标优化算法性能评价指标如下[[S8,S12]]：

| 指标 | 定义 | 评价含义 |
|------|------|---------|
| 世代距离（GD） | 算法近似 Pareto 解集到真实 Pareto 前沿的平均最小欧氏距离 | 数值越小，收敛性越好 |
| 反向世代距离（IGD） | 真实 Pareto 前沿到算法近似解集的平均最小欧氏距离 | 数值越小，综合覆盖能力越强 |
| 超体积（HV） | 算法近似解集与预设参考点所围成目标空间内超立方体的总体积 | 数值越大，收敛性和分布多样性综合表现越优 |

## 压铸工艺应用案例

### 案例一：一体式大型薄壁前机舱压铸件

针对新能源汽车一体式 Al-Cu 铝合金大型薄壁前机舱压铸件，采用 **Kriging 代理模型 + NSGA-II** 的优化方案[[S25,S2,S15]]：

- **优化变量**：高速压射速度（4～7 m/s）、低速压射速度（0.35～0.6 m/s）、压射位置切换点（20%～24%）、浇注温度（675～700℃）
- **优化目标**：针对减震塔、拉铆安装区域、关键承力区域三个核心性能区开展三目标优化
- **最优参数组合**：低速速度 0.38 m/s、高速速度 5.93 m/s、浇注温度 700℃、切换位置 21.79%
- **优化效果**：三个核心区域综合成型得分分别提升 53%、23%、47%，有效降低缩孔体积、卷气压力、气体含量等缺陷指标

### 案例二：大尺寸铝合金轮毂低压压铸

针对大尺寸铝合金轮毂低压压铸，采用 **响应面法（RSM）+ NSGA-II** 的优化方案[[S29,S6,S20,S10]]：

- **优化变量**：浇注温度（690～710℃）、模具温度（350～450℃）、保压压力（700～1200 mbar）、保压时间（220～260 s）
- **优化目标**：最小化缺陷体积分数和轮辐区域二次枝晶间距（SDAS）
- **最优参数组合**：浇注温度 703℃、模具温度 409℃、保压压力 1086 mbar、保压时间 249 s
- **优化效果**：缺陷体积分数 0.533%（后续冷却工艺校正后进一步降至 0.507%），SDAS 为 53.12 μm；实测铸件抗拉强度相比原工艺提升 9.28%，延伸率提升 45.27%

### 案例三：A356 铝合金缸盖压铸件

针对 A356 铝合金缸盖压铸件，同时优化模具浇注系统结构参数和铸造工艺参数[[S22]]：

- **设计变量**：浇注温度（680～710℃）、模具预热温度（200～300℃）、横浇道断面宽厚比（1.2～1.5）、内浇道断面宽厚比（2～4）、直浇道长径比（1.5～2.5）
- **优化目标**：最小化缩松缩孔体积和凝固时间
- **方法**：采用响应面法建立近似模型，通过 NSGA-II 获取 Pareto 解集，再以 TOPSIS 法筛选最优解

### Pareto 前沿输出示例

![Pareto 最优前沿（归一化）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d477184-8f2d-4d04-9848-f75e09be29e0/resource)

**图4 压铸工艺优化场景下 NSGA-II 得到的归一化 Pareto 前沿散点图**：x 轴为缩孔缩松体积对应指标，y 轴为热裂倾向对应指标，前沿解之间不存在完全支配关系，清晰呈现多目标之间的权衡特征[[S11]]。

## 局限性与改进方向

NSGA-II 的公认局限性及主流改进方向如下[[S8,S3]]：

| 局限性 | 说明 |
|--------|------|
| 高维问题表现下降 | 目标数大于 3 时，种群中非支配个体占比随目标维度快速上升，非支配排序区分度急剧下降，选择压力不足导致收敛放缓 |
| 边缘分布偏差 | 解集多样性依赖拥挤度计算，前沿边缘个体的边界处理容易出现分布偏差 |
| 前沿覆盖均匀性不足 | 原生 NSGA-II 未引入参考点引导，面向大规模复杂多目标优化时前沿覆盖均匀性有限 |

主要改进方向包括：引入参考点机制演变为 **NSGA-III** 算法以应对高维问题；融合分解策略借鉴 MOEA/D 的权重向量引导思路；以及加入自适应算子调整策略提升收敛效率和分布均匀性[[S8,S3]]。

## Sources
- S30: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f79d2090-0503-4092-950e-2022e3f14ec8/resource) (`f79d2090-0503-4092-950e-2022e3f14ec8`)
- S23: [基于3D打印的注塑模随形冷却水路优化设计及应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1b6a382-f64b-4d36-a8e9-391178d1439f/resource) (`d1b6a382-f64b-4d36-a8e9-391178d1439f`)
- S19: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b0e82776-724f-48ae-b187-d4f2eb2ca0fd/resource) (`b0e82776-724f-48ae-b187-d4f2eb2ca0fd`)
- S17: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/760dcd26-eb95-447b-9775-59c9cdd0d3bb/resource) (`760dcd26-eb95-447b-9775-59c9cdd0d3bb`)
- S21: [图4.35 优化算法的分类](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c14e4092-bcf4-4074-aad8-445fe5ed7e35/resource) (`c14e4092-bcf4-4074-aad8-445fe5ed7e35`)
- S16: [汽车发动机底护板复合材料塑件的成型工艺优化及多尺度联合仿真](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fa191ad-97ee-4b63-a938-306f8e2505e2/resource) (`6fa191ad-97ee-4b63-a938-306f8e2505e2`)
- S18: [插排面板注塑成型多目标优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c6e2049-3eed-456e-81e7-f42e17290714/resource) (`9c6e2049-3eed-456e-81e7-f42e17290714`)
- S24: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4dc7580-eb92-49ee-80c7-3ada0a11175a/resource) (`d4dc7580-eb92-49ee-80c7-3ada0a11175a`)
- S26: [基于3D打印的注塑模随形冷却水路优化设计及应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc67551a-803c-4fd1-8a2b-784652f77d1a/resource) (`dc67551a-803c-4fd1-8a2b-784652f77d1a`)
- S27: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/df6bf701-b9b7-480f-ae30-58cef6cd61de/resource) (`df6bf701-b9b7-480f-ae30-58cef6cd61de`)
- S9: [图3.3 NSGA-II算法流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19844181-9054-4514-b621-5addfa8d7962/resource) (`19844181-9054-4514-b621-5addfa8d7962`)
- S13: [图5-1 NSGA-II算法流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/568bb8b1-ef61-4a99-bb41-37029ae9fb04/resource) (`568bb8b1-ef61-4a99-bb41-37029ae9fb04`)
- S2: [TextNode4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/024e32c2-6748-4dee-be75-7c94e9575891/resource) (`024e32c2-6748-4dee-be75-7c94e9575891`)
- S28: [表5.5 NSGA-II算法参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eca1412a-840a-4120-94fb-ddc4966d5292/resource) (`eca1412a-840a-4120-94fb-ddc4966d5292`)
- S1: [NSGA-II 算法设置参数表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/00d33a71-4c5b-4cc3-92c8-f7f0181e1bc5/resource) (`00d33a71-4c5b-4cc3-92c8-f7f0181e1bc5`)
- S7: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e4c0dc9-2277-4c14-97f5-e2c8f50cce7c/resource) (`0e4c0dc9-2277-4c14-97f5-e2c8f50cce7c`)
- S8: [砂型铸造企业全流程低碳生产调度研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/160ae197-2354-40cb-b494-b87f29889849/resource) (`160ae197-2354-40cb-b494-b87f29889849`)
- S12: [NSGA-Ⅲ算法性能对比指标公式](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2e628e5e-cc2a-45b3-8fe0-52c25e030b25/resource) (`2e628e5e-cc2a-45b3-8fe0-52c25e030b25`)
- S25: [TextNode5](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5379d5a-f8f5-466c-aeee-b2092d012b46/resource) (`d5379d5a-f8f5-466c-aeee-b2092d012b46`)
- S15: [TextNode1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60f95e7a-02f6-428f-bfd4-f3a4e3c5a024/resource) (`60f95e7a-02f6-428f-bfd4-f3a4e3c5a024`)
- S29: [TextNode39](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f3b36eb7-4db2-4025-899b-2e3af8cc1246/resource) (`f3b36eb7-4db2-4025-899b-2e3af8cc1246`)
- S6: [大尺寸铝合金轮毂低压铸造凝固模拟及结构强度的仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d0c8dbc-511a-4719-8870-e9787041e3cb/resource) (`0d0c8dbc-511a-4719-8870-e9787041e3cb`)
- S20: [TextNode37](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4bc6553-8c10-4729-b536-07b53eb0d2fd/resource) (`b4bc6553-8c10-4729-b536-07b53eb0d2fd`)
- S10: [TextNode40](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c825c7b-99b6-4ffd-815c-573925a6d6e3/resource) (`1c825c7b-99b6-4ffd-815c-573925a6d6e3`)
- S22: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cfd26ecb-6acf-4e88-9bf0-f7d93516c367/resource) (`cfd26ecb-6acf-4e88-9bf0-f7d93516c367`)
- S11: [pareto最优前沿（归一化）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d477184-8f2d-4d04-9848-f75e09be29e0/resource) (`1d477184-8f2d-4d04-9848-f75e09be29e0`)
- S3: [砂型铸造企业全流程低碳生产调度研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03fd7c0f-af2b-4f31-b3a3-00454b8a37c1/resource) (`03fd7c0f-af2b-4f31-b3a3-00454b8a37c1`)