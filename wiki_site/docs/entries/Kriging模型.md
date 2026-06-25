---
version: "v1"
generated_at: "2026-06-21T05:42:08+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 37
  source_quality_score: 0.84
  freshness_score: 0.89
  evidence_coverage_score: 1.0
---

Kriging模型是一种基于高斯过程的空间插值代理模型，在压铸（铸造）工艺优化中用于建立工艺参数与质量响应之间的非线性映射，替代高成本的数值仿真与物理试验。该模型起源于地质矿藏预测，1989年由Sax El引入工程近似实验领域，后广泛应用于压铸工艺参数优化场景，属于统计插值模型、高斯过程模型和代理模型范畴 [[S12,S15]]。

## 数学模型与核心原理

Kriging模型将未知函数表述为全局趋势项与局部随机偏差项的组合，其标准形式为：

\[
y(x) = f(x) + z(x)
\]

其中 \( f(x) \) 为确定性回归函数（常取常数、一次多项式等），\( z(x) \) 为均值为零、方差为 \( \sigma^2 \) 的高斯随机过程，用于刻画样本点之间的空间相关性 [[S12,S14,S30]]。

为表达这种空间相关性，通常采用高斯型自相关函数：

\[
R_l(x_i^l, x_j^l) = \exp\left[-\theta_l (x_i^l - x_j^l)^2\right]
\]

其中 \( \theta_l \) 为第 \( l \) 维的超参数，可通过最大化样本似然函数估计得到 [[S4,S14,S41]]。

模型训练完成后，可同时输出待测点的预测均值（最优无偏估计）和预测方差（不确定度）。这一特性使其能够直接用于自适应加点策略，通过在高不确定度区域补充样本迭代提升模型精度 [[S34,S16,S12]]。

![Kriging模型对典型非线性振荡函数的拟合效果示例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7024cb52-dfe4-4445-a497-2ca7aa10b167/resource)

**图1** Kriging模型对函数 \( Y = X + 0.5\sin(5X) \) 的拟合结果，蓝色方块为原始采样点，黑色虚线为拟合曲线，展示其对非线性函数的插值能力 [[S23]]。

## 常见变体

| 变体名称 | 主要特征 | 适用场景 |
|---------|---------|---------|
| 普通Kriging | 以常数作为全局回归项的基础形式 | 全域趋势较弱、局部变异主导的铸造/压铸工艺响应拟合 [[S19]] |
| 各向异性Kriging | 允许各维度自相关核函数设独立超参数 | 不同工艺参数对响应影响程度差异显著的场景 [[S22]] |
| 自适应Kriging | 基于预测方差自动筛选高不确定度区域并补充样本，少量初始样本即能快速收敛 | 仿真成本高、样本获取难的压铸工艺优化 [[S50,S13]] |

## 压铸工艺优化全链路角色

Kriging模型在压铸领域中的典型应用流程为：

1. **试验设计（DOE）**：在工艺参数空间内通过正交试验、均匀试验或拉丁超立方采样等方法抽取初始样本集 [[S17,S26]]；
2. **响应获取**：通过数值仿真（如ProCAST、Moldflow）或现场试验获得每个样本对应的质量响应值 [[S41,S43]]；
3. **初始建模与校验**：构建Kriging模型，采用决定系数 \( R^2 \)、均方根误差RMSE等指标评估精度；常见收敛阈值如 \( R^2 \geq 0.8 \) 或更高 [[S43,S49]]；
4. **自适应加点**：若精度不满足要求，通过最大期望改进准则（EI）等加点策略迭代新增样本点、更新样本库并重塑模型，直至精度收敛 [[S43,S36]]；
5. **全局寻优**：基于收敛的Kriging模型，利用遗传算法（NSGA‑II）、量子粒子群算法等求解最优工艺参数组合 [[S18,S41,S26]]。

### 与正交试验、均匀试验的结合方式

压铸场景中常将正交试验数据作为Kriging的主要训练来源。例如，在AL365铝合金咖啡机顶盖压铸优化中，采用四因素四水平正交试验生成训练集，输入为浇注温度、模具温度、充填速度和压射比压，输出为模具热疲劳应力 [[S20,S41]]。

为进一步提高样本均匀性与全局性，可在正交试验基础上增补少量均匀试验样本。以不锈钢Y型三通管熔模铸造为例，将25组三因素五水平正交试验样本与5组 \( U_5(5^3) \) 均匀试验样本组合训练Kriging模型，训练集完全插值得到 \( R^2=1 \)，独立拉丁超立方测试样本校验得RMSE仅为0.07099 [[S10,S33]]。需指出，训练集 \( R^2=1 \) 是因Kriging模型为严格的插值模型；其泛化能力仍需通过独立测试集确认，该案例的低RMSE说明模型在该工况下具有良好的预测能力 [[S10,S2]]。

![优化迭代历史](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19d6945d-2bc1-47ec-808d-4e8cfdcd78a9/resource)

**图2** Kriging模型与Moldflow仿真在连续迭代中的变形量（warpage）对比，显示自适应加点策略下模型预测值逐步逼近仿真真值的过程 [[S3]]。

## 典型工艺参数与响应映射

### 常用输入参数与输出响应

| 常见输入工艺参数 | 典型输出质量响应 |
|----------------|----------------|
| 浇注温度、模具预热温度 | 缩孔/缩松体积、缩孔率 [[S2,S41]] |
| 低速/高速压射速度、切换位置 | 孔隙率、充填温度 [[S2,S28]] |
| 压射比压、充型时间 | 气体含量、卷气压力 [[S2,S49]] |
| 浇注温度、型壳焙烧温度、浇注速度 | 模具热疲劳应力、铸件力学性能（抗拉强度、延伸率）[[S10,S41]] |

### 经验工艺窗口示例

| 铸造场景 | 参数范围 | 来源 |
|---------|---------|------|
| 一体式大型薄壁铝合金前机舱压铸 | 高速速度4 ~ 7 m/s，低速速度0.35 ~ 0.6 m/s，切换位置20% ~ 24%，浇铸温度675 ~ 700 ℃ | [[S2]] |
| ZL114A铝合金低压铸造舱体 | 浇注温度700 ~ 780 ℃，模具预热温度250 ~ 300 ℃，充型时间8 ~ 12 s | [[S49]] |
| 压射机构工艺优化 | 浇注温度701 ℃附近，压室预热温度338 ℃附近，压射速度56 mm/s附近 | [[S28]] |

## 模型性能评价与验证策略

### 关键评价指标

- **决定系数 \( R^2 \)**：取值范围 \([0,1]\)，越接近1表示模型对因变量方差的解释能力越强 [[S37,S45,S32]]。
- **均方根误差RMSE**：与原始响应同量纲，越接近0表示预测值与真实值的整体偏差越小 [[S37,S45]]。
- **相对最大绝对误差RMAE**：反映局部区域的最大预测偏差，用于评估模型在极端位置的可靠性 [[S7,S27]]。

### 压铸领域典型精度水平

| 案例 | 模型类型 | \( R^2 \) | RMSE | 备注 |
|------|---------|-----------|------|------|
| 二次枝晶间距预测 | Kriging（低压铸造） | 0.9898（校正后0.9556） | — | 工程可用模型 [[S31]] |
| Y型三通管缩孔率预测 | 正交+均匀试验训练的Kriging | 训练集1.0 | 独立测试集0.07099 | 经独立测试集校验，泛化能力良好 [[S10]] |
| 低压铸造缩松缩孔体积预测 | 自适应Kriging（21组样本） | 0.9035 | — | 通过EI加点准则收敛，优化后相对误差1.64% [[S43]] |
| QPSO优化的Kriging（模具热疲劳应力） | 标准Kriging vs. QPSO‑Kriging | 相较标准版提升9.47% | 降低82.32% | 超参数优化显著提高精度 [[S7,S20]] |

### 验证方法

工程中普遍采用训练集与独立测试集拆分的方式进行交叉验证：用部分样本拟合模型，其余未参与训练的样本用于评估泛化性能，避免单纯依赖训练集拟合指标判定模型有效性 [[S10,S36]]。此外，还可采用测试点评价法，即在模型构建完成后于设计空间内重新抽样验证 [[S17]]。

### 过拟合风险判别

由于Kriging模型是严格插值模型，对训练样本可实现 \( R^2=1 \) 的完全拟合，但这仅反映模型对训练点的记忆能力。当独立测试集的 \( R^2 \) 远低于训练集、泛化误差显著增大时，即判为过拟合，此类模型无法支撑后续压铸工艺全局优化 [[S10,S2,S8]]。

## 主要局限

- **计算复杂度**：模型训练需对 \( n \) 阶相关矩阵求逆，计算复杂度为 \( O(n^3) \)，训练样本量过大时建模耗时显著增加 [[S19]]。
- **高维问题精度衰减**：相关矩阵维度随设计变量维度同步升高，超过10维后矩阵易奇异，空间相关性估计难度增大，泛化精度明显下降 [[S14,S19,S15]]。
- **外推不可靠**：Kriging为无偏内插模型，仅在训练样本覆盖的设计空间内部可输出稳定预测；超出边界的外推区域无空间相关性支撑，预测可信度极低，禁止用作决策依据 [[S12,S15]]。
- **离散/分类变量支持有限**：原生仅支持连续型输入，对于模具材质编号、合金牌号等离散分类变量，需通过独热编码等预处理转换为连续数值，过程复杂度高于支持向量回归、人工神经网络等算法 [[S32]]。
- **样本点排布要求**：若采样点间距过近或位于同一平面内，可能导致相关矩阵奇异，无法完成参数求解 [[S19]]。

## 与其他代理模型的对比

| 特性 | Kriging（GP） | 多项式响应面（RSM） | 人工神经网络（ANN） | 支持向量回归（SVR） |
|------|---------------|---------------------|---------------------|---------------------|
| 非线性拟合能力 | 强，适合高非线性问题 [[S15,S36]] | 较弱，主要适用于低维、弱非线性问题 [[S15,S21]] | 极强，可逼近任意非线性函数 [[S40,S25]] | 较强，核技巧可处理非线性 [[S15]] |
| 小样本适应性 | 优秀，小样本下仍可得到较高精度 [[S2,S50]]；完全插值所有训练点 | 一般，需要一定样本量保证回归系数估计 | 差，小样本下易过拟合 [[S8]] | 较好，仅由支持向量决定模型 |
| 高维性能 | 随维度升高精度下降，相关矩阵易奇异 [[S14,S19]] | 拟合效果较差 [[S15]] | 可处理高维但需大量样本 | 优秀，计算复杂度与维度无关，可避免维度灾难 [[S15]] |
| 预测不确定性 | 可同时输出预测均值与方差，直接指导自适应加点 [[S16,S34]] | 不具备 | 通常不具备 | 通常不具备 |
| 计算成本 | 较高（\( O(n^3) \)），样本量大时远高于RSM、SVR [[S19]] | 低 | 中等 | 中等 |
| 鲁棒性与精度稳定性 | 在相同铸造场景、不同样本量下的平均RMSE及标准差均为最低，鲁棒性最优 [[S42]] | 中等或大样本时表现较差 | 大样本时表现较好 | 整体表现仅次于GP [[S42]] |

## 典型应用效果

- **低压铸造舱体缩松缩孔优化**：以浇注温度、模具预热温度、充型时间为输入，通过自适应Kriging代理模型（初始15组LHS样本，EI加点至21组）迭代收敛后 \( R^2=0.9035 \)，优化工艺使缩松缩孔体积下降24.58%，Kriging预测最优值与有限元仿真验证的相对误差仅1.64% [[S43,S47]]。
- **大型薄壁前机舱压铸多目标优化**：针对三个关键区域的综合成型得分构建三个Kriging响应曲面，所有抽样点均落在预测曲面上，拟合误差极小，后续采用NSGA‑II算法实现多目标工艺参数寻优 [[S2,S30]]。
- **超参数优化提升效果**：在模具热疲劳应力预测中，采用量子粒子群算法（QPSO）优化Kriging模型的变差函数超参数后，\( R^2 \) 提升9.47%，RMSE降低82.32%，RMAE降低84.91%，预测残差区间由 \([-2, 10]\) 收窄至 \([-2, 1]\) [[S7,S20]]。

Kriging模型作为压铸工艺智能优化体系中的核心代理建模工具，凭借其插值特性、不确定性量化能力以及小样本适应性，在铸造缺陷预测、工艺窗口寻优和模具寿命评估等场景中发挥了关键作用 [[S2,S41,S18]]。实际应用中须注意样本质量、维度控制与过拟合检验，以保证模型在工程决策中的可靠性。

## Sources
- S12: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/44606976-b9d1-4ea8-9f78-904eec2c6fe0/resource) (`44606976-b9d1-4ea8-9f78-904eec2c6fe0`)
- S15: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/49333412-3c39-4135-b66a-754d4f42bec1/resource) (`49333412-3c39-4135-b66a-754d4f42bec1`)
- S14: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/47b74638-cf13-44ec-b133-b434b60cc3f2/resource) (`47b74638-cf13-44ec-b133-b434b60cc3f2`)
- S30: [TextNode3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/919cd7cd-0ff8-4d59-b4f3-63cd3312e53a/resource) (`919cd7cd-0ff8-4d59-b4f3-63cd3312e53a`)
- S4: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1aa5aac9-f71c-4682-ae57-88749390dd95/resource) (`1aa5aac9-f71c-4682-ae57-88749390dd95`)
- S41: [压力铸造成型工艺参数优化数学模型研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bef5e7f7-97be-41d7-889b-3e50c95dd3ad/resource) (`bef5e7f7-97be-41d7-889b-3e50c95dd3ad`)
- S34: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/99c29e95-23b9-4922-aa3f-01c2c941c048/resource) (`99c29e95-23b9-4922-aa3f-01c2c941c048`)
- S16: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56def17b-e199-4183-97d9-92b60673e870/resource) (`56def17b-e199-4183-97d9-92b60673e870`)
- S23: [Kriging 模型在 X 从 1 到 9 范围内的拟合效果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7024cb52-dfe4-4445-a497-2ca7aa10b167/resource) (`7024cb52-dfe4-4445-a497-2ca7aa10b167`)
- S19: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/622a54b3-21a7-4ed8-8ec2-e2fee4b7cf50/resource) (`622a54b3-21a7-4ed8-8ec2-e2fee4b7cf50`)
- S22: [Anisotropic Kriging](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c072a44-c21c-42c2-b6db-bf6b1c639348/resource) (`6c072a44-c21c-42c2-b6db-bf6b1c639348`)
- S50: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ffccf282-d4cd-468a-8a6c-ea2efe24ad05/resource) (`ffccf282-d4cd-468a-8a6c-ea2efe24ad05`)
- S13: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/45749263-d0c2-4b4d-8c7d-34603e6975dd/resource) (`45749263-d0c2-4b4d-8c7d-34603e6975dd`)
- S17: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/586c81f6-6d99-4e5c-8615-f515516e131d/resource) (`586c81f6-6d99-4e5c-8615-f515516e131d`)
- S26: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7eb202d0-f74e-4f31-979b-02f9fe838a76/resource) (`7eb202d0-f74e-4f31-979b-02f9fe838a76`)
- S43: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dbddfea0-fbcc-4a41-8eb7-920cfdbb3c28/resource) (`dbddfea0-fbcc-4a41-8eb7-920cfdbb3c28`)
- S49: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f80d0bb6-e087-4a98-b1b6-3615cad4708d/resource) (`f80d0bb6-e087-4a98-b1b6-3615cad4708d`)
- S36: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1806597-dd23-44d8-95cd-f3d8bf8be517/resource) (`a1806597-dd23-44d8-95cd-f3d8bf8be517`)
- S18: [基于智能算法的一体式大型薄壁前机舱压铸成型工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60f95e7a-02f6-428f-bfd4-f3a4e3c5a024/resource) (`60f95e7a-02f6-428f-bfd4-f3a4e3c5a024`)
- S20: [压力铸造成型工艺参数优化数学模型研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68adbd40-9f10-46f2-8f88-6b924a7dd869/resource) (`68adbd40-9f10-46f2-8f88-6b924a7dd869`)
- S10: [不锈钢Y型三通管熔模铸造浇注方案设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39aa64a7-ce1a-482a-8d52-5bb6d40c41f8/resource) (`39aa64a7-ce1a-482a-8d52-5bb6d40c41f8`)
- S33: [不锈钢Y型三通管熔模铸造浇注方案设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/999eb5b2-dcbd-4f81-93c2-d632d6c41553/resource) (`999eb5b2-dcbd-4f81-93c2-d632d6c41553`)
- S2: [TextNode4](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/024e32c2-6748-4dee-be75-7c94e9575891/resource) (`024e32c2-6748-4dee-be75-7c94e9575891`)
- S3: [图3 优化迭代历史](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/19d6945d-2bc1-47ec-808d-4e8cfdcd78a9/resource) (`19d6945d-2bc1-47ec-808d-4e8cfdcd78a9`)
- S28: [5355586_压射机构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8f1a2977-ab07-40ac-9164-8857d5b073cd/resource) (`8f1a2977-ab07-40ac-9164-8857d5b073cd`)
- S37: [铝合金压铸工艺参数不确定性对铸件静强度性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a1c59ed2-1005-4b7c-8336-621b0f1dbd85/resource) (`a1c59ed2-1005-4b7c-8336-621b0f1dbd85`)
- S45: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e4ca1b6d-1239-415c-8c8c-d7a3d4fca6f2/resource) (`e4ca1b6d-1239-415c-8c8c-d7a3d4fca6f2`)
- S32: [融合岩性信息的CNN-LSTM-GAT深度网络孔隙压力预测方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60/resource) (`95d34ab1-8cb2-4349-9f4c-52b1d4f1ac60`)
- S7: [压力铸造成型工艺参数优化数学模型研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/294efda0-d5e7-4b4a-a055-6a3103c104f1/resource) (`294efda0-d5e7-4b4a-a055-6a3103c104f1`)
- S27: [artificial intelligence aided materials design ai algorithms and case st__7887fa7595](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8d8076ce-1394-4f6d-bf23-31e938c348cf/resource) (`8d8076ce-1394-4f6d-bf23-31e938c348cf`)
- S31: [Table 4.7 Summary of secondary dendrite spacing model fitting](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93dcda06-de4b-4612-87f6-200e20a30cc2/resource) (`93dcda06-de4b-4612-87f6-200e20a30cc2`)
- S8: [材料加工过程实验建模方法](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3306d6f9-7d4b-4e0b-941d-ad6ac53ff9aa/resource) (`3306d6f9-7d4b-4e0b-941d-ad6ac53ff9aa`)
- S21: [aip conference proceedings aip international conference on modeling opti__9dbb7b9ee0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6967b44c-57c8-4b2c-8958-41da01f91c35/resource) (`6967b44c-57c8-4b2c-8958-41da01f91c35`)
- S40: [基于CAE与遗传神经网络的变速箱壳体压铸工艺优化及质量预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b4e91d3a-69f4-48bb-9e12-3e72f8397365/resource) (`b4e91d3a-69f4-48bb-9e12-3e72f8397365`)
- S25: [a neural network system for the prediction of process parameters in pres__ec0b04f9b1](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7c35e8bd-c47c-4067-8308-e6b005327b02/resource) (`7c35e8bd-c47c-4067-8308-e6b005327b02`)
- S42: [第一届高聚物成型加工与材料物性预测国际学术研讨会论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d40e34d2-7071-4ae1-983e-dc9dc5ef5d7b/resource) (`d40e34d2-7071-4ae1-983e-dc9dc5ef5d7b`)
- S47: [航天构件低压铸造与热成形工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e91e2e9f-1172-486a-a33f-20579a826a18/resource) (`e91e2e9f-1172-486a-a33f-20579a826a18`)