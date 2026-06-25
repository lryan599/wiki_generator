---
version: "v1"
generated_at: "2026-06-18T12:03:29+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 35
  source_quality_score: 0.86
  freshness_score: 0.84
  evidence_coverage_score: 1.0
---

## 定义与基本解释

二次枝晶臂间距（Secondary Dendrite Arm Spacing, SDAS）定义为合金凝固形成的一次枝晶臂上，相邻垂直方向分布的二次枝晶臂之间的平均垂直距离，是铸造合金最重要的微观结构长度参数之一，测量时取金相视野下至少20次测量结果的统计平均值[[S31,S11,S29]]。对于亚共晶铝合金等枝晶型组织，SDAS是表征其枝晶组织细化程度的核心微观参数，直接决定铸件力学性能和内部缺陷倾向性[[S11]]。

一次枝晶臂间距（d₁）与二次枝晶臂间距（d₂）在概念和形成规律上存在本质区别：

- **一次枝晶臂间距 d₁**：主干之间的间距，经验公式指数 n₁≈1/2[[S10,S29]]；
- **二次枝晶臂间距 d₂（SDAS）**：二次分枝之间的间距，经验公式指数 n₂≈1/3[[S10,S29]]；

二次枝晶臂间距的大小直接影响成分偏析、第二相及显微孔洞的分布，从而对铸件性能产生影响[[S10]]。

![ZL114A合金二次枝晶臂示意图，标注SDAS测量方向](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81120436-9b7f-4d99-98c0-916a29719364/resource)


## 形成机制与粗化理论

枝晶在凝固早期于尖端附近以极小间距生长；随着凝固进行，系统试图降低枝晶体系的表面能，细小的二次枝晶臂优先溶解，粗大枝晶持续生长，导致SDAS逐步增大。该过程受液相中溶质扩散速率的限制[[S4,S10,S25]]。

经典枝晶粗化机制包含四种物理模型[[S10]]：

| 模型 | 名称 | 特征描述 |
|---|---|---|
| 模型Ⅰ | 径向熔化模型 | 细臂整体径向熔化消失 |
| 模型Ⅱ | 缩颈熔断模型 | 枝晶根部形成缩颈后逐渐熔化及游离 |
| 模型Ⅲ | 轴向熔化模型 | 细枝晶逐渐轴向萎缩而消失 |
| 模型Ⅳ | 枝晶合并模型 | 相邻枝晶臂合并为一体 |

浇注温度高、冷却强度小，将促进枝晶的粗化过程[[S2]]。


## SDAS与冷却速率/局部凝固时间的关系

SDAS主要受铸件局部的冷却速度 v 控制，通用经验关系式如下[[S10,S2,S29]]：

- **以局部凝固时间为变量**：SDAS = a · (局部凝固时间)^m
- **以冷却速率为变量**：SDAS = b · (冷却速率)^(-n)

其中指数 n 因枝晶层级不同而有所区别：

| 枝晶间距类型 | 指数 | 公式形式 |
|---|---|---|
| 一次枝晶臂间距 d₁ | n₁≈1/2 | d₁ = a(1/(G_L·R))^(n₁) |
| 二次枝晶臂间距 d₂（SDAS） | n₂≈1/3 | d₂ = b(ΔT_S/(G_L·R))^(n₂) |

式中 G_L 为凝固界面液相一侧的温度梯度，R 为界面生长速度，ΔT_S 为非平衡结晶温度范围[[S10,S29]]。

### 压铸常用合金的经验参数

不同合金类型的SDAS经验公式系数存在显著差异，但指数n均接近1/3[[S39]]：

| 合金类型 | 系数 b 取值范围 | 指数 n 取值范围 |
|---|---|---|
| 铸铁 | 2.0 | 0.33~0.35 |
| 铝合金 | 1.7~3.0 | 0.33~0.35 |
| 镁合金 | 2.3~4.5 | 0.33~0.35 |

### 特种铝合金的实测关系式

- **A356铝合金**：晶粒粗化系数 a = 680 μm·s^(-1/3)，指数 m = 1/3，利用 Furer-Wunderlin 二次枝晶臂侧熔模型计算[[S31,S13]]。
- **低压铸造铝合金**：SDAS = μ₁·(CR)^(-0.34±0.02)，其中μ₁为材料特定常数[[S13]]。


## 不同工艺条件下的SDAS典型范围

### 高压压铸

高压压铸场景下存在两种不同起源的枝晶，其SDAS呈现双峰分布[[S18,S11]]：

| 枝晶来源 | SDAS典型范围 |
|---|---|
| 压室预结晶枝晶（ESCs/PSDs） | 15~25 μm |
| 型腔内快速凝固形成的枝晶 | 2~5 μm |

对于高压压铸AlSi9Cu3(Fe)合金，部分薄壁件快速冷却条件下SDAS可低至6 μm（6×10⁻³ mm）[[S5,S3]]。

压铸A380合金压室自然凝固组织的二次臂间距约15~25 μm，对应局部凝固时间约34~158 s，平均冷却速度约2.3~0.95 ℃/s[[S17]]。

### 低压铸造

低压铸造条件下SDAS受涂料厚度显著影响[[S15]]：

| 涂料厚度 | 铸件边部SDAS | 铸件心部SDAS |
|---|---|---|
| 0 μm | 14.5 μm | 17.4 μm |
| 100±50 μm | 15.6 μm | 20.1 μm |
| 200±50 μm | 18.8 μm | 24.3 μm |
| 300±50 μm | 21.2 μm | 28.9 μm |

SDAS分布规律表现为铸件边部小于心部，且随涂料厚度的增加呈递增趋势[[S15]]。

### 重力铸造与挤压铸造对比

5083铝合金重力铸造铸件SDAS范围为10~35.89 μm，且同工艺下铸件不同位置的SDAS数值差异显著；采用压力辅助挤压铸造工艺后，该合金SDAS可均匀控制在3.19~10 μm区间，不同位置SDAS偏差显著降低[[S36,S38]]。

### 不同壁厚位置分布规律

以铝合金压铸车轮为例，不同工艺下车轮五个典型取样位置的SDAS由大到小依次为：轮心 > 轮辐 > 轮辋 > 外轮缘 > 内轮缘，即从轮心厚大区域向轮辋薄壁区域延伸，SDAS呈梯度递减趋势[[S11,S8]]。


## 对力学性能的影响

### 基本规律

SDAS减小可显著提升压铸合金的抗拉强度、屈服强度、延伸率与硬度。同时，更小的SDAS使枝晶间显微缩松与非金属夹杂物的尺寸和分布危害性降低，且均质化热处理所需时间更短或效率更高，最终提升铸件气密性与耐压性能[[S29,S25,S4,S19]]。

### ZL114A低压铸造合金的定量数据

ZL114A（Al-Si-Mg系）合金实验实测结果[[S33]]：

| SDAS状态 | 抗拉强度 (MPa) | 延伸率 (%) | 显微硬度 (HV) |
|---|---|---|---|
| SDAS最小时 | 336.27 | 5.60 | 129.00 |
| SDAS最大时 | 305.72 | 3.05 | 119.60 |

该结果表明SDAS的减小与力学性能提升之间存在显著的正相关关系[[S33]]。

### SDAS与共晶硅的交互作用

在相同冷却条件下，SDAS细化时可同步促进共晶硅颗粒尺寸减小、分布均匀。变质处理（添加Sr、Na等元素）与快速冷却的共同作用，可实现SDAS与共晶硅的双重细化，进一步提升合金的强韧性匹配效果[[S27,S6]]。


## SDAS与缺陷的关联

### 与显微缩松的关系

SDAS与铝合金压铸件显微缩松呈显著正相关。SDAS增大时，枝晶搭接后形成的封闭孤立液相区域体积更大，补缩通道更难打通，缩松倾向显著提升。针对ZL114A合金的实验数据[[S14]]：

| 试样壁厚 | SDAS (μm) | 缩松体积分数 (%) |
|---|---|---|
| 3 mm | 24.6 | 0.35 |
| 6 mm | 39.1 | 0.74 |

壁厚的增大会降低冷却速率，进而降低过冷度，SDAS随之增大，枝晶越发达，枝晶间的缩松缺陷也随之增加[[S14]]。

### 与可检测宏观孔隙的关系

铝合金铸件中SDAS与X射线可检测孔隙的定量关系[[S12]]：

- **SDAS < 28 μm**：常规30倍放大X射线探伤无法识别出可见孔隙；
- **SDAS从28 μm升至48 μm**：可见孔隙最大长度从0.1 mm同步上升至0.7 mm。

### 与热裂敏感性的关系

SDAS增大将提升铸件热裂敏感性。SDAS较大时，枝晶间液膜厚度更大，凝固后期晶间残余液相难以补缩晶界微裂纹，当收缩应力超过剩余液膜的临界抗拉强度时，热裂缺陷萌生概率显著提升[[S23]]。


## 压铸/低压铸造中降低SDAS的工艺措施

降低SDAS的核心思路是缩短局部凝固时间、提升冷却速率。工程实践中有效的优化措施包括[[S28,S20,S13,S22]]：

1. **提升模具与铸件界面的换热系数**——通过增设随形冷却水道、布置局部冷铁强制提升冷却速率；
2. **适当降低浇注温度**——在保证充型流畅性的前提下；
3. **适当提升增压补缩压力**——缩短固液两相区停留时间；
4. **添加晶粒细化剂**——促进异质形核、抑制二次枝晶粗化。

### 压铸A356铝合金的SDAS影响因素权重

针对压铸A356铝合金的正交试验分析表明，SDAS影响因素权重排序为[[S9]]：

> **模具温度 > 浇注温度 > 压射速度 > 保压压力**

低模具温度、低浇注温度的工艺组合可获得最小SDAS[[S9]]。

对于低压铸造铝合金，浇注温度对厚大部位SDAS的影响最大，模具预热温度的影响次之；浇注温度由680°C升高至740°C时，SDAS由33.69 μm增大至35.67 μm（增幅约5.9%）[[S20]]。


## 测量与表征方法

### 金相试样制备

通用流程[[S1]]：依次采用400#、800#、1200#、2000#及以上目数水砂纸进行粗磨和精磨，再先后使用粒度1.5 μm和0.5 μm的金刚石抛光剂完成镜面抛光。针对铝合金试样，采用Keller试剂等指定腐蚀剂处理约30 s以获得清晰的枝晶组织轮廓[[S1]]。

### 手动测量统计法

测量规则：沿垂直于一次枝晶臂方向画直线，记录直线与枝晶臂的交点距离及个数，每个金相视场至少完成20次独立测量，统计不少于10个以上有效枝晶区域，取所有测量值的算术平均值作为最终结果[[S11,S24,S1]]。

![AlSi7Mg合金5×放大倍率下实测SDAS为29 μm的金相显微照片，附带100 μm标尺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fb564b98-ef78-4df8-8d78-d064053fdbd0/resource)

### 图像自动测量注意事项

基于机器学习的自动SDAS测量系统需注意以下要点[[S3]]：

- 训练数据集需覆盖含一定比例缺陷（含气孔、划痕、模糊成像、外来外生晶等）的样本；
- 自动识别前需完成不同放大倍率下的像素-长度标定；
- 避免将枝晶间隙、铸造缺陷误判为有效二次枝晶臂间距。

### 相关标准

目前尚无专门针对枝晶间距的独立国际标准，但以下标准的测量框架可直接适配SDAS测量流程[[S26,S34]]：

| 标准号 | 适用范围 | 可迁移应用 |
|---|---|---|
| ASTM E112 | 金属晶粒度测定 | 截线统计方法、样本量要求与SDAS测量规则一致 |
| ASTM E562 | 定量金相 | 面积分数统计规则可用于SDAS分布均匀度的区域统计 |
| ISO 643 | 钢中晶粒度测定 | 通用显微表征框架可直接适配SDAS测量流程 |


## 数值模拟中的SDAS预测

### 主流软件的SDAS预测功能

MAGMASOFT软件内置微观组织分析模块，可通过全铸件凝固速率场映射计算对应合金的SDAS分布，自动生成全铸件SDAS云图，并直接关联后续力学性能与缺陷的预测[[S37,S30]]。ProCAST软件的微结构模块同样提供SDAS模拟分析功能[[S30]]。

### 仿真-力学分析集成应用

将ProCAST计算得到的全铸件SDAS数据通过形函数插值算法直接映射到Abaqus力学仿真模型中，取代传统均匀材料属性设置，可显著提升压铸件疲劳寿命预测精度，仿真结果与实测结果吻合度更高[[S32]]。

### AZ91D镁合金低压铸造工艺优化案例

以浇注温度（680~720°C）和充型压力（4.3~8.0 kPa）为设计变量，以缩松体积和SDAS为优化目标，通过集成计算平台实现多目标自动优化。优化前缩松体积为4.1%、SDAS为88.5 μm；在浇注温度689°C、充型压力6.5 kPa条件下，优化后缩松体积降至2.1%，SDAS降至81.2 μm[[S22]]。

## Sources
- S31: [基于田口法的铝合金空心控制臂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d2933bd3-4d66-4b0e-9318-68c5652dd034/resource) (`d2933bd3-4d66-4b0e-9318-68c5652dd034`)
- S11: [压铸铝车轮非均组织性能分析与热处理工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43f15ce3-aa38-4386-b18e-61d9052f3d05/resource) (`43f15ce3-aa38-4386-b18e-61d9052f3d05`)
- S29: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be8dfb47-9fc7-4518-a3d0-f1bb1279b7de/resource) (`be8dfb47-9fc7-4518-a3d0-f1bb1279b7de`)
- S10: [中国材料工程大典 第18卷 材料铸造形成工程 （上册）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/316f0c34-35a7-4134-8280-9ee690fa9569/resource) (`316f0c34-35a7-4134-8280-9ee690fa9569`)
- S4: [castings principles the new metallurgy of cast metals__9ac1d4f9a8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1a912fa1-f89a-40c4-bcde-e9fe6bf33945/resource) (`1a912fa1-f89a-40c4-bcde-e9fe6bf33945`)
- S25: [complete casting handbook__a339dffea0](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/af45e090-e54b-4cfe-a9ec-ce40b3363093/resource) (`af45e090-e54b-4cfe-a9ec-ce40b3363093`)
- S2: [有色金属熔炼与铸锭](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/09f4cc75-2e13-434a-9f36-7a36bb0230cf/resource) (`09f4cc75-2e13-434a-9f36-7a36bb0230cf`)
- S39: [表 4-4 式 (4-26) 中的系数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9140053-f55e-4c7d-ab5b-e336a05c7f25/resource) (`f9140053-f55e-4c7d-ab5b-e336a05c7f25`)
- S13: [development of an innovative low pressure die casting process for alumin__7a4bafd851](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b1ef995-f609-43c1-8407-14d79f8f1a2d/resource) (`5b1ef995-f609-43c1-8407-14d79f8f1a2d`)
- S18: [压铸条件下合金流动停止机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/899c8814-12f6-4b63-bc9d-a43dbd5ce395/resource) (`899c8814-12f6-4b63-bc9d-a43dbd5ce395`)
- S5: [advances in processing and mechanical behavior in lightweight metals and alloys__ec5cc90182](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1f6f4d20-ea6b-4fbf-b243-9eec70c8587b/resource) (`1f6f4d20-ea6b-4fbf-b243-9eec70c8587b`)
- S3: [advances in processing and mechanical behavior in lightweight metals and alloys__ec5cc90182](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0e40c6b1-497e-4bd7-a4f1-e62accde7645/resource) (`0e40c6b1-497e-4bd7-a4f1-e62accde7645`)
- S17: [压铸条件下合金流动停止机理](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8323a67d-0cad-48ca-83e4-e3e2b0ffc02d/resource) (`8323a67d-0cad-48ca-83e4-e3e2b0ffc02d`)
- S15: [表4.1 不同涂料厚度下铸件边部与心部的二次枝晶臂间距平均值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6201de43-3ed0-49d5-8e9f-b81f981afe9f/resource) (`6201de43-3ed0-49d5-8e9f-b81f981afe9f`)
- S36: [effect of the gap distance on the cooling behavior and the microstructur__6e37cbb0fa](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eaa07300-374e-4743-9bbf-bd23f66f3554/resource) (`eaa07300-374e-4743-9bbf-bd23f66f3554`)
- S38: [effect of die geometry on the microstructure of indirect squeeze cast an__aec613b571](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f20ec3a4-a6aa-4f98-ae78-2a0239cc6eb3/resource) (`f20ec3a4-a6aa-4f98-ae78-2a0239cc6eb3`)
- S8: [表3-4 各工艺不同位置SDAS数据统计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3072d696-97c2-449d-b43d-34b19f496e55/resource) (`3072d696-97c2-449d-b43d-34b19f496e55`)
- S19: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/903bf1d0-6bbf-4a00-bdfd-3fa2ff25fa6c/resource) (`903bf1d0-6bbf-4a00-bdfd-3fa2ff25fa6c`)
- S33: [机械振动对真空低压铸造ZL114A微观组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e2669b75-842d-4e60-a86f-c592790f4f60/resource) (`e2669b75-842d-4e60-a86f-c592790f4f60`)
- S27: [comparative study on the microstructures and hardness of the alsi106cumg__b188063cb6](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b8b8a642-c30f-4aed-a4e9-8553413d99c3/resource) (`b8b8a642-c30f-4aed-a4e9-8553413d99c3`)
- S6: [Al-12wt%Si合金的力学性能及共晶Si、SDAS尺寸参数](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22043f78-3c80-4734-b15a-5f48ef040ecf/resource) (`22043f78-3c80-4734-b15a-5f48ef040ecf`)
- S14: [ZL114A合金薄壁件充型能力及缩松缺陷倾向的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5b4097be-1d8b-431e-ad12-a0baf809a32b/resource) (`5b4097be-1d8b-431e-ad12-a0baf809a32b`)
- S12: [automotive alloys 1999__dbd41f2733](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4ebaad3e-e066-440e-84aa-7451095d6036/resource) (`4ebaad3e-e066-440e-84aa-7451095d6036`)
- S23: [第三届国际熔模精密铸造会议文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/aaf74412-8396-46df-8a9b-1eadc0c4205f/resource) (`aaf74412-8396-46df-8a9b-1eadc0c4205f`)
- S28: [铝合金三通阀体金属型重力铸造数值模拟与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b90eb5ae-3e8a-4a12-bfeb-f0737cc67d47/resource) (`b90eb5ae-3e8a-4a12-bfeb-f0737cc67d47`)
- S20: [风机叶轮的低压铸造工艺模拟研究和模具设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9aefe056-70c3-49aa-902f-0bdd94374c52/resource) (`9aefe056-70c3-49aa-902f-0bdd94374c52`)
- S22: [AZ91D镁合金集成计算平台构建及轮毂低压铸造工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f742a45-27dd-4fc8-9ed3-33d69ee64444/resource) (`9f742a45-27dd-4fc8-9ed3-33d69ee64444`)
- S9: [基于正交试验与信噪比分析的铝合金钳体支架压铸工艺参数优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30c333f2-c4a3-4897-a64a-c20f0cf8967d/resource) (`30c333f2-c4a3-4897-a64a-c20f0cf8967d`)
- S1: [自行车铝合金结构件液态模锻及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/03ceb72d-76ab-4b95-b5f7-9a26ad13ee9c/resource) (`03ceb72d-76ab-4b95-b5f7-9a26ad13ee9c`)
- S24: [铝合金发动机缸盖低压铸造工艺创新与性能优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab343de8-bac1-43ab-bf63-8156fd1498a3/resource) (`ab343de8-bac1-43ab-bf63-8156fd1498a3`)
- S26: [ASTM E112 标准中关于金属显微组织检验的说明文本](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afc74f33-084d-4fe8-8b45-d7a76b087b60/resource) (`afc74f33-084d-4fe8-8b45-d7a76b087b60`)
- S34: [ASTM 测试方法对应表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e773253f-c3c4-43e3-9ad5-84c62f547293/resource) (`e773253f-c3c4-43e3-9ad5-84c62f547293`)
- S37: [压铸模具典型结构图册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec8e7be0-2540-4195-9d05-37c70bb76d0f/resource) (`ec8e7be0-2540-4195-9d05-37c70bb76d0f`)
- S30: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf063c89-7f01-49f0-bec3-84d9babc20a4/resource) (`cf063c89-7f01-49f0-bec3-84d9babc20a4`)
- S32: [大尺寸铝合金轮毂低压铸造凝固模拟及结构强度的仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d62984fc-4de0-4472-b080-ad3cddb9a232/resource) (`d62984fc-4de0-4472-b080-ad3cddb9a232`)