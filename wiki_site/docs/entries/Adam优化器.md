---
version: "v1"
generated_at: "2026-06-18T17:36:18+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 17
  source_quality_score: 0.85
  freshness_score: 0.88
  evidence_coverage_score: 1.0
---

在压铸技术wiki中，Adam优化器指向自适应矩估计（Adaptive Moment Estimation）算法，属于一种通用的神经网络训练随机梯度下降优化器。全量中英文压铸领域公开资源检索结果表明，以“Adam”直接命名的压铸合金牌号、压铸设备型号、压铸模具标准件、压铸工艺规范类术语不存在。检索结果中出现的“Adam”字样仅包括科研人员姓名与机器学习领域的Adam优化器算法[[S3,S12,S18,S20]]。因此，本条目阐述Adam优化器作为压铸智能化应用的通用优化工具的核心原理、参数配置及在铸造/压铸场景中的前沿应用案例。

## 定义与原理

Adam优化器全称为自适应矩估计（Adaptive Moment Estimation），属于一类用于更新神经网络权重的自适应随机梯度下降优化器，融合了AdaGrad与RMSProp两类算法的核心特性[[S23]]。该算法通过分别计算梯度的一阶矩和二阶矩的滑动指数估计，为不同网络参数动态分配独立的自适应学习率[[S1,S23]]。

Adam的数学核心包含以下四个环节[[S1]]：

**1. 一阶矩与二阶矩滑动估计**  
对梯度 \( g_t \) 及梯度平方 \( g_t^2 \) 进行指数滑动平均，得到一阶矩估计 \( m_t \) 和二阶矩估计 \( v_t \)：

\[
m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t
\]

\[
v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2
\]

其中，\( \beta_1 \) 和 \( \beta_2 \) 分别为一阶矩和二阶矩的指数衰减率[[S1]]。

**2. 偏差校正**  
因 \( m_0 \) 和 \( v_0 \) 初始化为0，迭代初期矩估计存在偏向零的偏差。算法通过以下方式进行校正，且随着迭代步数 \( t \) 增大，校正作用自动减弱[[S1]]：

\[
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}
\]

\[
\hat{v}_t = \frac{v_t}{1 - \beta_2^t}
\]

**3. 参数更新规则**  
完成校正后，按以下公式更新模型参数 \( \theta_t \) [[S1]]：

\[
\theta_t = \theta_{t-1} - \alpha \cdot \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}
\]

其中，\( \alpha \) 为全局学习率，\( \varepsilon \) 为避免分母为0的极小数值常数[[S1]]。

**4. 学习率衰减变体**  
工程实践中可引入学习率衰减机制，每轮迭代或一定迭代次数后将当前学习率乘以衰减因子，或按 \( \alpha = \alpha \cdot \sqrt{t} \) 规则更新，在训练后期逐步缩小更新步长，提升收敛稳定性[[S1]]。

## 核心超参数

Adam算法的官方推荐默认超参数取值如下表所示[[S1,S14]]：

| 参数符号 | 参数含义 | 默认推荐值 |
|:---:|:---|:---:|
| \( \alpha \) | 全局学习率 | 0.001 |
| \( \beta_1 \) | 一阶矩指数衰减率 | 0.9 |
| \( \beta_2 \) | 二阶矩指数衰减率 | 0.999 |
| \( \varepsilon \) | 数值稳定常数 | \( 10^{-8} \) |

## 与AdaGrad、RMSProp及SGD的关系

Adam被公认为AdaGrad与RMSProp两类算法的结合体[[S23]]：

- **AdaGrad**：为各参数独立维护累计梯度平方的全局统计量，天然适配稀疏梯度场景，但累计量随迭代无限累积，导致训练后期有效学习率趋近于零。Adam继承了AdaGrad逐参数自适应学习率的设计思想[[S23]]。
- **RMSProp**：对梯度平方进行滑动平均统计，仅保留近期梯度信息，适配非稳态和在线学习场景。Adam继承了RMSProp的二阶矩滑动平均特性，并额外加入一阶动量累积与偏差校正机制[[S23]]。
- **SGD**：普通随机梯度下降的性能高度依赖人工指定的全局固定学习率，微小调参不当即可导致不收敛。Adam不需要大量人工调参，可自动为每个参数生成动态自适应学习率，收敛速度远快于普通SGD，工程落地门槛更低[[S1,S4,S9]]。

## 在压铸及制造场景中的应用

目前，NADCA出版的《Die Casting Process Control》等传统行业标准与工艺教材中尚未收录Adam优化器相关工业案例[[S10,S17]]，但压铸及相关铸造领域的智能化前沿研究已产生多个基于Adam的高水平应用案例：

### 1. 压铸成品质量预测

Adam E. Kopper等利用采用Adam优化的深度学习监督学习模型，对超过95万条压铸生产周期的全流程数据进行分析，成功实现对压铸成品合格件/报废件的高效预测。该研究发表于《International Journal of Metalcasting》[[S6,S13]]。

### 2. 低压铸造工艺智能设计

在铝合金舱体结构件低压铸造工艺智能设计研究中，基于Keras搭建的多模态多输入深度神经网络采用带学习率衰减的Adam优化器进行训练，以平均绝对百分比误差为损失函数，建立“铸件结构—成分—浇注系统参数—铸造工艺参数—屈服强度”的映射关系。最终合金抗拉强度的预测误差可控制在±5%以内，大幅缩短传统铝合金新材料开发与低压铸造工艺设计的周期和成本[[S7,S23]]。

### 3. 铸件DR图像缺陷语义分割

针对精密铸件DR图像的U-Net语义分割缺陷检测任务，研究采用AdamW（带权重衰减的Adam变体）优化器对模型进行训练，可有效加速模型收敛；搭配PReLU激活函数替代ReLU后，模型泛化性能得到进一步提升[[S24]]。

### 4. 压铸件气孔压力预测典型配置

面向压铸件孔隙压力预测等AI辅助工艺分析任务，典型工程化训练配置为：学习率0.001，批大小32，总训练轮次100，搭配L2正则化与均方误差（MSE）损失函数[[S21]]。

## 改进变体：AdamW

AdamW是在原始Adam基础上优化权重衰减实现方式的改进变体，在深度学习语义分割等计算机视觉任务中可进一步提升模型泛化能力并加速收敛，相比原始Adam取得更优的训练效果[[S24]]。在精密铸件DR图像缺陷检测任务中已得到实际验证[[S24]]。

## 行业标准收录现状

目前，北美压铸协会（NADCA）公开出版的《Die Casting Process Control》等传统压铸工艺控制类教材和标准资料中，尚未收录Adam优化器相关的工业落地案例与规范条文。Adam优化器在压铸场景的应用仍属于该领域智能化前沿研究方向，尚未全面进入行业通用标准体系[[S10,S17]]。

## 配图说明

以下示意图展示铸造领域数据驱动工艺优化通用的神经网络结构：输入层包含合金化学成分、各维度铸造工艺参数等信息，隐藏层完成特征映射，输出层对应铸件缺陷指数、力学性能等目标指标。此类神经网络模型常采用Adam优化器进行高效训练，以建立“参数→目标”的非线性映射关系[[S19]]。

![铸造领域数据驱动工艺优化的通用人工神经网络结构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4661cdd-cb15-4cd4-93fc-3307298830b2/resource)

## Sources
- S3: [压铸手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/08c0bdc3-48cc-466b-b13b-8730859a9bef/resource) (`08c0bdc3-48cc-466b-b13b-8730859a9bef`)
- S12: [最新铸造标准应用手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4a8bfdbd-4b73-4cd8-8233-f1880c827cbd/resource) (`4a8bfdbd-4b73-4cd8-8233-f1880c827cbd`)
- S18: [analytical characterization of aluminum steel and superalloys__29f2247322](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9cfdd06a-4eb8-4011-a38a-4969dd1d14aa/resource) (`9cfdd06a-4eb8-4011-a38a-4969dd1d14aa`)
- S20: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4b74529-4b07-4d76-8708-83d0b16e86b0/resource) (`d4b74529-4b07-4d76-8708-83d0b16e86b0`)
- S23: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f88199be-e880-428f-9e24-29e58c617e6d/resource) (`f88199be-e880-428f-9e24-29e58c617e6d`)
- S1: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04c7d629-7bbd-45e4-863c-bbe3cd5befcf/resource) (`04c7d629-7bbd-45e4-863c-bbe3cd5befcf`)
- S14: [锻造时压力机应变场与模具温度场的数字重构研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6980c7f2-43a9-40a4-9de1-b479edda6b43/resource) (`6980c7f2-43a9-40a4-9de1-b479edda6b43`)
- S4: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0b193b97-7e63-4348-8d76-3c1022ef3810/resource) (`0b193b97-7e63-4348-8d76-3c1022ef3810`)
- S9: [aiot系统开发基于机器学习和python深度学习融合人工智能和物联网两大热点技术将人工智能的优越方法应用到物联网的构建中形成更加智能的物联网系统物联网核心技术丛书](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/42e1a58b-4dd3-4f26-8f77-554a11205343/resource) (`42e1a58b-4dd3-4f26-8f77-554a11205343`)
- S10: [die casting process control__e0210f9156](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/437649b7-2395-457a-be8e-edac76c0bfae/resource) (`437649b7-2395-457a-be8e-edac76c0bfae`)
- S17: [die casting process control__e0210f9156](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/91d4f31e-9e12-47dc-a1e6-3a62420be3d2/resource) (`91d4f31e-9e12-47dc-a1e6-3a62420be3d2`)
- S6: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/11690005-1902-4b9d-a3f9-2cc468698556/resource) (`11690005-1902-4b9d-a3f9-2cc468698556`)
- S13: [数据驱动调压铸造工艺智能设计及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/68348d13-fe47-41e1-a85b-3a13df94ae0f/resource) (`68348d13-fe47-41e1-a85b-3a13df94ae0f`)
- S7: [数据驱动铝合金舱体结构件材料及工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a496fdb-c431-44ec-839b-2d40b0f5eab3/resource) (`1a496fdb-c431-44ec-839b-2d40b0f5eab3`)
- S24: [铝合金压铸工艺参数不确定性对铸件静强度性能影响研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fef28f15-5d6f-412f-b3c9-39807f08565a/resource) (`fef28f15-5d6f-412f-b3c9-39807f08565a`)
- S21: [表 3 训练参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ed0b4bf7-aaa6-4710-b903-25f7de72be40/resource) (`ed0b4bf7-aaa6-4710-b903-25f7de72be40`)
- S19: [人工神经网络模型](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4661cdd-cb15-4cd4-93fc-3307298830b2/resource) (`c4661cdd-cb15-4cd4-93fc-3307298830b2`)