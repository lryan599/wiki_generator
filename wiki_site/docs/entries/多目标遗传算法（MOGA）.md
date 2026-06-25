---
version: "v1"
generated_at: "2026-06-18T19:21:51+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 30
  source_quality_score: 0.83
  freshness_score: 0.93
  evidence_coverage_score: 1.0
---

## 概述

多目标遗传算法（Multi-Objective Genetic Algorithm, MOGA）是一类将遗传算法扩展至多目标优化问题的进化计算方法，其核心机制是在一次运行中搜索到一组互不支配的Pareto最优解，而非单一的全局最优解。该词条在实际研究与工程文献中，最常以非支配排序遗传算法（Non-dominated Sorting Genetic Algorithm, NSGA）系列为代表，其中NSGA-II（第二代非支配排序遗传算法）是压铸工艺多目标优化领域应用最广泛的基准算法之一 [[S17,S35]]。

初代NSGA由Srinivas和Deb于1993年提出，核心思路是在选择操作前对种群个体进行多级排序以分配虚拟适应度，通过适应度共享维持种群多样性 [[S6]]。NSGA-II由Kalyanmoy Deb于2000年首次提出、2002年在《IEEE进化计算汇刊》正式发表，引入了三项关键改进：快速非支配排序降低计算复杂度、拥挤度算子替代共享半径、精英保留策略将优秀前代个体直接保留到下一代 [[S35,S8,S17]]。NSGA-III则进一步引入参考点引导机制，适配三个以上目标的高维多目标优化场景 [[S7]]。

> **术语说明**：NSGA-II 是 MOGA 家族中最具代表性的具体算法，但在技术交流中，"多目标遗传算法"常被默指为 NSGA-II 或基于非支配排序的遗传算法变体，二者并非完全等同但高度关联。

## 定义与核心概念

### 多目标优化问题形式

多目标优化问题可表述为在一组约束条件下，同时对多个相互冲突的目标函数进行优化 [[S30,S31]]：

$$\min f(X) = \{f_1(X), f_2(X), \ldots, f_m(X)\}$$

$$s.t. \quad X_L \leq X \leq X_U$$

式中，$X$ 为 $n$ 维决策变量向量，$f_i(X)$ 为第 $i$ 个目标函数，$X_L$ 与 $X_U$ 分别为变量边界。

### Pareto 最优与支配关系

Pareto 支配关系是 MOGA 算法的理论基石。以最小化优化为例，解 $x_1$ 支配解 $x_2$ 的条件为 [[S35,S21]]：

1. 在所有目标函数上，$x_1$ 的取值均不大于 $x_2$ 的取值：$f_i(x_1) \leq f_i(x_2)$，$\forall i = 1, 2, \ldots, m$；
2. 至少存在一个目标函数，$x_1$ 的取值严格小于 $x_2$：$\exists j$，$f_j(x_1) < f_j(x_2)$。

**Pareto最优解**定义为：对于可行解域中的某个解 $X^*$，不存在任何其他可行解在所有目标上都优于 $X^*$。即对任意Pareto最优解而言，一个目标性能的改善必然导致至少另一目标性能的劣化 [[S31,S11]]。

**Pareto前沿**指所有Pareto最优解在目标空间中的投影集合。位于同一Pareto前沿上的任意两个解之间不存在支配关系，无法直接判定绝对优劣，需要结合实际工程需求进行折中决策 [[S11,S35]]。

## 核心原理与关键机制

### 非支配排序

非支配排序是NSGA-II的核心分级机制。其工作流程为 [[S35,S21]]：

1. 将种群中所有个体按支配关系进行逐层划分；
2. 第一层为当前所有非支配解，构成Pareto前沿（Front 1）；
3. 移除第一层后的剩余个体中，所有非支配解构成第二层（Front 2）；
4. 以此类推，直至全部分级完成，层级序号越低，个体优先级越高。

该机制通过层级晋升方式，确保搜索始终朝着真实Pareto前沿方向收敛。

### 快速非支配排序

快速非支配排序是NSGA-II对初代NSGA排序算法的关键改进，通过在排序过程中利用个体间的支配计数和被支配集合信息，将排序时间复杂度从 $O(MN^3)$ 降至 $O(MN^2)$（其中 $M$ 为目标数，$N$ 为种群规模），显著提升了大种群多目标优化的计算效率 [[S35,S17]]。

### 拥挤度距离

拥挤度距离用于衡量同一非支配层级内个体在目标空间中的分布密度，是NSGA-II维持解集多样性的核心算子。计算方法为 [[S18,S21]]：

1. 在每个目标维度上，将同一层级内的所有个体按目标函数值排序；
2. 边界个体的拥挤度设置为无穷大；
3. 其余每个个体的拥挤度为在所有目标维度上，与该个体相邻两个体距离之和，等价于该个体两侧相邻点构成的超立方体边长总和。

拥挤度越大，代表个体周边区域解分布越稀疏。算法在生成新一代种群时，优先选择拥挤度较大的个体，以保持解集的分布均匀性 [[S18]]。

### 精英保留策略

NSGA-II在每个进化代中，将父代种群与子代种群合并成规模为 $2N$ 的混合种群，对该混合种群做非支配排序与拥挤度计算后，按照非支配层级由低到高、同层级按拥挤度由大到小的顺序，筛选出 $N$ 个最优个体构成新一代父代种群 [[S18,S33]]。此机制确保前代中的优秀解能够直接进入下一代，加速算法的收敛进程 [[S17]]。

## 算法步骤与流程

NSGA-II 算法的标准执行步骤可归纳如下 [[S33,S1,S35]]：

| 步骤 | 操作内容 |
|------|----------|
| 步骤1：初始化 | 设定种群规模 $N$、交叉概率、变异概率、最大进化代数等参数，随机生成规模为 $N$ 的初始父代种群 $P_t$（$t=0$） |
| 步骤2：遗传操作 | 对父代种群执行二元锦标赛选择，采用模拟二进制交叉（SBX）和多项式变异（PM）操作，生成规模为 $N$ 的子代种群 $Q_t$ |
| 步骤3：种群合并 | 将父代 $P_t$ 与子代 $Q_t$ 合并，构造规模为 $2N$ 的混合种群 $R_t$ |
| 步骤4：非支配排序 | 对混合种群 $R_t$ 进行快速非支配排序，获得不同层级的非支配前沿 |
| 步骤5：拥挤度估计 | 对每个非支配层级内的所有个体计算拥挤度距离 |
| 步骤6：新种群构建 | 按非支配优先级由低到高、同层级拥挤度由大到小的顺序，从 $R_t$ 中筛选 $N$ 个个体，构成新一代父代种群 $P_{t+1}$ |
| 步骤7：终止判定 | 若当前进化代数达到预设最大值，则终止算法并输出最终Pareto解集；否则令 $t = t+1$，返回步骤2 |

NSGA-II算法流程图展示了从种群初始化、父子代合并、非支配排序、拥挤度计算到输出Pareto解集的完整逻辑链 [[S13]]。

![NSGA-II算法标准执行流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/568bb8b1-ef61-4a99-bb41-37029ae9fb04/resource)

## 参数与操作条件

### 通用场景推荐参数

基础遗传算法在通用场景下的推荐参数范围为 [[S26]]：

| 参数 | 推荐范围 |
|------|----------|
| 种群规模 | 20 ~ 100 |
| 交叉概率 | 0.4 ~ 0.99 |
| 变异概率 | 0.0001 ~ 0.1 |

### 压铸工艺优化场景典型参数

针对压铸多目标优化问题，由于优化对象通常为由数值仿真或代理模型构建的非解析目标函数，参数设置往往高于通用场景 [[S12,S1,S34]]：

| 参数 | 压铸场景典型取值 | 来源示例 |
|------|------------------|----------|
| 种群规模 | 30 ~ 200 | A356缸盖优化30 [[S34]]；大型薄壁前机舱优化50 [[S1]]；铝合金阀体优化200 [[S12]] |
| 交叉概率 | 0.8 ~ 0.9 | 阀体0.8 [[S12]]；缸盖0.9 [[S34]]；前机舱0.9 [[S1]] |
| 变异概率 | 0.1 | 多案例通用 [[S12,S1]] |
| 最大迭代代数 | 100 ~ 300 | 前机舱100 [[S1]]；缸盖200 [[S34]]；阀体300 [[S12]] |
| 交叉分布指数 | 10 ~ 20 | 缸盖交叉分布指数10，变异分布指数20 [[S34]] |

以A356铝合金缸盖铸造优化研究为例，其NSGA-II参数配置为：种群数量30、迭代次数200、交叉概率0.9、交叉分布指数10、变异分布指数20 [[S34]]。

## 压铸领域的应用

### "数值仿真—代理模型—NSGA-II"优化模式

在压铸工艺多目标优化中，主流的实现路径为代理模型耦合NSGA-II方法，典型流程如下 [[S20,S30]]：

1. **试验设计**：通过Box-Behnken（BBD）或中心复合设计（CCD）完成样本点采样；
2. **数值仿真**：采用ProCAST等铸造仿真软件获取各组样本对应的铸件质量结果（缩松体积、凝固时间、力学性能等）；
3. **代理模型构建**：采用RBF神经网络、Kriging克里金模型或二阶响应面模型，建立工艺参数与优化目标之间的高精度映射关系，训练集误差控制在10%以内；
4. **多目标优化**：将训练完成的代理模型作为目标函数，输入NSGA-II算法迭代寻优，输出Pareto最优解集；
5. **决策与验证**：通过TOPSIS等多目标决策方法从Pareto解集中筛选折中最优解，最终利用数值仿真或实际试生产完成效果验证。

该技术路线图清晰展示了从初始种群生成、代理模型预测、适应度计算到最优结果输出的全过程 [[S15]]。

![遗传算法-神经网络联合优化流程图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b5929fa-277b-4524-9677-7da62a613f25/resource)

### 典型应用案例

**案例一：一体式大型薄壁前机舱高压压铸优化**

以新能源汽车一体式前机舱为对象，采用Kriging代理模型耦合NSGA-II进行三目标工艺优化 [[S32,S1]]。

- **优化变量**：高速速度（4~7 m/s）、低速速度（0.35~0.6 m/s）、压射切换位置（20%~24%）、浇铸温度（675~700°C）
- **优化目标**：最大化减震塔区域综合性能得分（y1）、最大化拉铆螺母安装区域综合性能得分（y2）、最大化铆接连接区域综合性能得分（y3）
- **验证参数**：低速速度0.38 m/s、高速速度5.93 m/s、浇铸温度700°C、切换位置21.79%
- **优化效果**：三个区域综合性能得分相对初始值分别提升53%、23%、47%

Pareto前沿分析表明，三个优化目标之间存在显著的权衡关系，二维投影图进一步揭示了两两目标间的非线性竞争特性 [[S32]]。

**案例二：A356铝合金缸盖铸造工艺优化**

以A356铝合金缸盖为对象，采用响应面法耦合NSGA-II进行双目标优化 [[S2,S30,S4]]：

- **优化变量**：浇铸温度（680~710°C）、模具预热温度（200~300°C）、横浇道断面宽厚比、内浇道断面宽厚比、直浇道长径比
- **优化目标**：最小化缩松缩孔体积、最小化铸件凝固时间
- **优化效果**：通过TOPSIS决策得到最优解（预测缩松体积8.7475 cm³、凝固时间119.71 s），经ProCAST仿真验证后，缩松体积降低9.80%，凝固时间降低7.25%

**案例三：AZ91D镁合金轮毂低压铸造优化**

以AZ91D镁合金轮毂为对象，开展双目标低压铸造工艺优化 [[S23]]：

- **优化变量**：浇注温度（680~720°C）、充型压力（4.3~8.0 KPa）
- **优化目标**：最小化缩松体积、最小化二次枝晶臂间距
- **优化效果**：在浇注温度689°C、充型压力6.5 KPa条件下，缩松占比从4.1%降至2.1%，二次枝晶臂间距从88.5 μm降至81.2 μm

**案例四：球铁凸轮轴铸造缺陷优化**

以球铁凸轮轴为对象，采用RBF神经网络代理模型耦合NSGA-II进行缺陷控制优化 [[S28,S20]]：

- **优化变量**：材料成分（C、Si、Mn、S）、浇注温度、保压时间、模具温度
- **优化目标**：最小化缩孔缩松体积、最小化热裂倾向（HTI值）
- **Pareto解集特征**：共获得20组有效Pareto解，前沿曲线平滑，无完全支配解

该案例揭示了一个典型的工艺权衡矛盾：球铁的石墨化膨胀有利于补偿凝固收缩以减小缩孔缩松，但同时增加了凝固过程中的合金应变量，使热裂倾向增大，需要在多目标决策中进行平衡取舍 [[S28]]。

## Pareto 解集特征与评估

### 压铸优化Pareto前沿的典型特征

在压铸工艺多目标优化中，二维Pareto前沿通常呈现以下特征 [[S22,S10,S25]]：

- 曲线平滑无明显断点，表明算法具备良好的收敛性
- 目标函数之间呈负相关的权衡特性
- 所有解之间不存在完全支配关系
- 可根据不同压铸场景的质量优先级，从中选取适配的折中参数组合

### 多目标优化性能评估指标

| 指标 | 英文全称 | 含义 | 评估重点 |
|------|----------|------|----------|
| IGD | Inverted Generational Distance | 衡量真实Pareto前沿上的点到算法近似解集的平均最小欧式距离，数值越小收敛性越好 | 收敛性 |
| HV | Hypervolume | 计算算法生成的所有近似解与指定参考点围成的超立方体总体积，数值越大覆盖范围越广 | 收敛性+分布性 |
| SP | Spacing Metric | 统计解集内每个解到其最近邻解欧式距离的离散程度，数值越小分布越均匀 | 分布均匀性 |

以上三类指标构成了多目标优化算法性能评估的标准框架 [[S7]]。

## 与其他多目标算法的关系与比较

在多目标进化优化领域，MOGA/NSGA-II与多种算法各有侧重，下表对不同算法的特性进行比较：

| 算法 | 核心框架 | 优势 | 局限 | 适用场景 |
|------|----------|------|------|----------|
| NSGA-II | 基于非支配排序+拥挤度+精英保留 [[S17]] | 收敛速度快，2~3目标场景Pareto解集分布均匀，应用最广泛 | 高维目标（>3）场景性能下降 [[S7]] | 压铸工艺双/三目标优化 |
| NSGA-III | 基于参考点引导选择 [[S7]] | 高维目标（>3）与大候选池场景收敛性及综合性能显著优于NSGA-II | 低维小规模场景无显著优势；多样性依赖参考点分布 | 大规模复杂调度优化 |
| SPEA2 | 基于强度Pareto进化+邻域截断 [[S7]] | 解集多样性丰富，覆盖范围宽 | 计算复杂度更高，迭代耗时更长 | 对解集分布均匀性要求极高的场景 |
| MOEA/D | 基于分解策略，将多目标分解为多个单目标子问题 [[S24]] | 高维多目标场景计算效率高 | 性能高度依赖权重向量设置 | 高维目标函数优化 |
| MOPSO | 基于粒子群智能+外部存档 [[S19]] | 收敛速度快，适合低维小规模场景 | 全局搜索能力弱于NSGA-II，易陷入局部最优 | 低维快速优化 |

综上所述，NSGA-II在2~3个目标的常规压铸工艺优化场景中综合性能均衡，是当前工程实践中最成熟的选择 [[S17,S35]]。SPEA2在解集分布多样性上优于NSGA-II和NSGA-III，但计算成本更高 [[S7]]。

## 实现工具与库

| 工具/平台 | 类型 | 特性 |
|-----------|------|------|
| MATLAB `gamultiobj` | 商用软件内置函数 | 内置NSGA-II实现，调用接口简洁，可直接与MATLAB优化工具箱及后处理模块联动，适合快速原型开发 [[S16,S29]] |
| PlatEMO | 开源MATLAB工具箱 | 2017年发布，集成数十种主流多目标优化算法和标准测试集，开源免费、可自定义扩展，是学术研究的基准工具 [[S16,S29]] |

## 关键术语中英文对照

| 中文术语 | 英文术语 |
|----------|----------|
| 多目标遗传算法 | Multi-Objective Genetic Algorithm (MOGA) |
| 非支配排序遗传算法（第二代） | Non-dominated Sorting Genetic Algorithm II (NSGA-II) |
| Pareto 最优解 | Pareto optimal solution |
| Pareto 最优解集 | Pareto optimal set (Pareto set) |
| Pareto 前沿 | Pareto front |
| 非支配排序 | Non-dominated sorting |
| 快速非支配排序 | Fast non-dominated sorting |
| 拥挤度距离 | Crowding distance |
| 精英保留策略 | Elitism (Elitist preserving strategy) |
| 代际距离 | Generational Distance (GD) |
| 反向世代距离 | Inverted Generational Distance (IGD) |
| 超体积 | Hypervolume (HV) |
| 间距 | Spacing Metric (SP) |
| 模拟二进制交叉 | Simulated Binary Crossover (SBX) |
| 多项式变异 | Polynomial Mutation (PM) |

## Sources
- S17: [汽车发动机底护板复合材料塑件的成型工艺优化及多尺度联合仿真](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6fa191ad-97ee-4b63-a938-306f8e2505e2/resource) (`6fa191ad-97ee-4b63-a938-306f8e2505e2`)
- S35: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f79d2090-0503-4092-950e-2022e3f14ec8/resource) (`f79d2090-0503-4092-950e-2022e3f14ec8`)
- S6: [风机面壳塑件成型质量双目标优化及联合仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e4c0dc9-2277-4c14-97f5-e2c8f50cce7c/resource) (`0e4c0dc9-2277-4c14-97f5-e2c8f50cce7c`)
- S8: [考虑螺旋离心泵水力性能及铸造成型的多目标优化设计研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/197c2b1a-80a7-4e6f-8bec-597c48a245b8/resource) (`197c2b1a-80a7-4e6f-8bec-597c48a245b8`)
- S7: [砂型铸造企业全流程低碳生产调度研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/160ae197-2354-40cb-b494-b87f29889849/resource) (`160ae197-2354-40cb-b494-b87f29889849`)
- S30: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cfd26ecb-6acf-4e88-9bf0-f7d93516c367/resource) (`cfd26ecb-6acf-4e88-9bf0-f7d93516c367`)
- S31: [基于3D打印的注塑模随形冷却水路优化设计及应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d1b6a382-f64b-4d36-a8e9-391178d1439f/resource) (`d1b6a382-f64b-4d36-a8e9-391178d1439f`)
- S21: [插排面板注塑成型多目标优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9c6e2049-3eed-456e-81e7-f42e17290714/resource) (`9c6e2049-3eed-456e-81e7-f42e17290714`)
- S11: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3271ac53-6ce1-477a-a4ae-0f034ddac6d9/resource) (`3271ac53-6ce1-477a-a4ae-0f034ddac6d9`)
- S18: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/760dcd26-eb95-447b-9775-59c9cdd0d3bb/resource) (`760dcd26-eb95-447b-9775-59c9cdd0d3bb`)
- S33: [基于3D打印的注塑模随形冷却水路优化设计及应用研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dc67551a-803c-4fd1-8a2b-784652f77d1a/resource) (`dc67551a-803c-4fd1-8a2b-784652f77d1a`)
- S1: [基于智能算法的一体式大型薄壁前机舱压铸成型工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/024e32c2-6748-4dee-be75-7c94e9575891/resource) (`024e32c2-6748-4dee-be75-7c94e9575891`)
- S13: [图5-1 NSGA-II算法流程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/568bb8b1-ef61-4a99-bb41-37029ae9fb04/resource) (`568bb8b1-ef61-4a99-bb41-37029ae9fb04`)
- S26: [凝固界面换热系数反求及铝合金薄壁件压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ba462557-8b97-41a2-81a7-b5f811bd8597/resource) (`ba462557-8b97-41a2-81a7-b5f811bd8597`)
- S12: [表 8 NSGA-Ⅱ算法参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ffbf94f-b174-497d-8c2e-53ab3cb2d908/resource) (`4ffbf94f-b174-497d-8c2e-53ab3cb2d908`)
- S34: [表5.5 NSGA-II算法参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eca1412a-840a-4120-94fb-ddc4966d5292/resource) (`eca1412a-840a-4120-94fb-ddc4966d5292`)
- S20: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7e15ef14-10ec-466c-b375-de6de618fdac/resource) (`7e15ef14-10ec-466c-b375-de6de618fdac`)
- S15: [注塑成型工艺优化技术路线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60a66810-d013-4ca3-a451-4eaf4eb142f1/resource) (`60a66810-d013-4ca3-a451-4eaf4eb142f1`)
- S32: [基于智能算法的一体式大型薄壁前机舱压铸成型工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d5379d5a-f8f5-466c-aeee-b2092d012b46/resource) (`d5379d5a-f8f5-466c-aeee-b2092d012b46`)
- S2: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0493ceb9-c64e-4dcf-b21a-eff5ff7dfdb1/resource) (`0493ceb9-c64e-4dcf-b21a-eff5ff7dfdb1`)
- S4: [A356铝合金缸盖的数值模拟及浇注系统结构对铸件的质量影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09fd8115-a3c8-4499-9cf6-01271c2432fc/resource) (`09fd8115-a3c8-4499-9cf6-01271c2432fc`)
- S23: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f742a45-27dd-4fc8-9ed3-33d69ee64444/resource) (`9f742a45-27dd-4fc8-9ed3-33d69ee64444`)
- S28: [凸轮轴铸造缺陷成因及其工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c17c336b-df2a-4d56-908f-d6ed81f8b6e0/resource) (`c17c336b-df2a-4d56-908f-d6ed81f8b6e0`)
- S22: [图5.5 pareto最优前沿](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f1eca4e-c91d-4b7e-862b-ab89d607f0af/resource) (`9f1eca4e-c91d-4b7e-862b-ab89d607f0af`)
- S10: [pareto最优前沿（归一化）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1d477184-8f2d-4d04-9848-f75e09be29e0/resource) (`1d477184-8f2d-4d04-9848-f75e09be29e0`)
- S25: [图5.10 Pareto最优解集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b01d4765-7cac-4cb1-a3f3-755f01265289/resource) (`b01d4765-7cac-4cb1-a3f3-755f01265289`)
- S24: [不同规模测试算例算法指标对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aeb0644a-b8c9-44ce-a67b-42597168cc46/resource) (`aeb0644a-b8c9-44ce-a67b-42597168cc46`)
- S19: [基于响应面法和多目标粒子群算法的玻璃纤维增强ABS塑件多目标优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7cf52f97-57d5-4e1b-a7a8-c2e91485a4fe/resource) (`7cf52f97-57d5-4e1b-a7a8-c2e91485a4fe`)
- S16: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/64ef5d43-e7e6-48ee-a995-b7e4daa562af/resource) (`64ef5d43-e7e6-48ee-a995-b7e4daa562af`)
- S29: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf1de26e-839d-456f-bb45-7d09bb621093/resource) (`cf1de26e-839d-456f-bb45-7d09bb621093`)