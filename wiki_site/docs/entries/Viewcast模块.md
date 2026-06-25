---
version: "v1"
generated_at: "2026-06-18T16:13:11+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 21
  source_quality_score: 0.85
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

ViewCAST（别名 Visual-Viewer）是法国 ESI 公司 ProCAST 铸造仿真软件的核心原生后处理模块，负责将数值计算得到的所有物理场结果进行可视化输出。它是 ProCAST 标准工作流的最终环节：CAD 几何建模 → MeshCAST 网格划分 → PreCAST 参数配置 → DataCAST 预处理 → ProCAST 求解运算 → **ViewCAST 结果可视化**[[S17,S22,S24]]。在后处理阶段，用户可通过 ViewCAST 观察和分析温度场、流场、应力场、元素偏析以及微观组织等多种仿真计算结果[[S17,S1,S15]]。

## 命名演变与归属关系

ViewCAST 模块的官方名称随 ProCAST 版本架构变更而经历了一次重要更名：

- **经典版本阶段（2009 年以前）**：后处理模块的正式英文名称为 **ViewCAST**（首字母 V 大写，后续 CAST 全大写）。在此阶段，ViewCAST 是完全独立的可执行程序，通过 ProCAST 主界面菜单栏直接启动[[S17,S15,S18]]。
- **Visual Environment 集成版本阶段（2009 版以后）**：ESI 将独立的模块体系整合到统一的 Visual Environment 界面框架下，原 ViewCAST 正式更名为 **Visual-Viewer**，以集成子窗口的形式内嵌在 ProCAST 统一操作界面内，无需单独启动[[S16,S9]]。工程界常用的简化写法 “Visual Viewer”（无连字符）属于等效表达，而非官方术语[[S10,S2]]。
- 新旧版本中 ViewCAST 与 Visual-Viewer 的命名共存，是该模块在各类文献中出现名称混淆的核心原因[[S16]]。两者在功能上本质一致，均对应 ProCAST 的后处理可视化环境。

> **澄清：与 CASTPost 的关系**  
> CASTPost 是 ESI 旗下另一款早期有限差分铸造仿真软件 PAM-CAST 的配套后处理程序。PAM-CAST 与 ProCAST 分属不同产品线，二者不存在 ProCAST 套件内 ViewCAST 与 CASTPost 作为并列后处理组件的分工关系[[S4]]。

## 核心功能

ViewCAST（Visual-Viewer）将 ProCAST 计算得到的所有结果数据转换为图形化显示，其核心功能涵盖以下方面[[S17,S1,S15,S18]]：

| 功能类别 | 支持内容 |
|---|---|
| 标量场可视化 | 温度场、固相率、缩孔缩松判据、元素偏析等 |
| 矢量场/力场可视化 | 热应力 Effective Stress、总位移 Total Displacement、温度梯度矢量等 |
| 微观组织结果显示 | 晶粒形貌、相组成等微观组织模拟结果[[S17,S8]] |
| 动态过程展示 | 充型过程、凝固次序、缩孔形成过程的 GIF 动画输出[[S20,S6]] |
| 剖切与截面分析 | 支持切割截面模式下的场量观察[[S20,S23]] |

此外，ViewCAST 独特地支持在求解器运行过程中**实时读取并渲染动态生成的计算快照**，用户无需等待全量仿真计算完成即可提前观察部分场量的演化过程[[S17]]。

## 操作流程与入口

### 经典版本操作路径

ProCAST 2008.0 主界面顶部菜单栏明确标注了各模块入口，点击后可直接启动独立的 ViewCAST 可执行程序[[S3]]。

![ProCAST 2008.0主界面菜单栏（含后处理模块VisualCAST入口）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3cbf9da7-726a-4dbb-9c78-30289a09f370/resource)

### 集成版本操作路径

在 Visual Environment 集成界面中，Visual-Viewer 作为内嵌子窗口出现。ProCAST 17.5 版本的 Visual-Viewer 主界面设有 “Open File” 与 “Execute Session” 两大核心入口，最近打开列表以缩略图形式展示历史模拟结果；右侧 “Highlights” 区域列出多尺度结果可视化、截面切割、局部冷却速率计算、2D 直方图等核心后处理功能[[S23]]。

![ProCAST Visual-Viewer (ViewCAST) 17.5版本主界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa27f35b-fe01-4560-b686-91e7fec0c02f/resource)

### 加载温度场与应力场的标准操作

以 ProCAST 2009.0 为例，加载特定物理场的标准菜单路径如下[[S20]]：

| 目标物理量 | 菜单路径 |
|---|---|
| 温度场云图 | Contour → Thermal → Temperature |
| 等效应力云图 | Contour → Stress → Effective Stress |
| 总位移分布 | Contour → Stress → Total Displacement |

### 求解启动与结果文件

上述操作的前提是求解已经完成或正在进行。启动求解时，在 ProCAST 2009.0 主界面弹出的 ProCAST Solver 对话框中点击 “Run” 按钮，求解器将生成 ViewCAST 可读取的结果文件[[S19]]。

## 关键参数与可配置项

ViewCAST 在观察分析过程中提供多项用户可调节参数：

**温度色标范围调节**

软件默认自动遍历所有网格单元的温度极值作为色标上、下限，但当温度跨度很大时（例如从浇注温度至室温），色标对比度较小，凝固细节难以分辨。用户可手动将色标下限调整至略低于合金固相线的区间，从而大幅提升相变关键温度区间的色彩对比度，清晰展示凝固过程的细节差异[[S6]]。

**Niyama 判据标尺设置**

在使用 Niyama 判据预测缩松、缩孔缺陷时，操作路径为 Contour → Thermal → Mapping Factors，将结果标尺设置为 0~1.1：显示值小于 1.1 的区域即为可能出现缩松、缩孔的位置[[S11]]。Niyama 判据的参数设置对话框可通过 Action → R，G，L 菜单调出，支持设置上下限温度、参考温度以及单位制等参数[[S11]]。

**GIF 动画导出**

ViewCAST 支持将连续时间步的仿真结果序列导出为 GIF 动态图片格式，用于直观展示充型进程、凝固过程及应力场演化的完整动态变化，同时支持单独导出指定剖切截面下的场量结果[[S20]]。

## 在压铸/铸造工艺分析中的应用

### 充型过程与浇不足缺陷预判

通过 ViewCAST 观察铸件三维温度场分布，可查看不同时刻的温度变化：在充型过程中识别出低于液相线的低温区域，直接预判浇不足缺陷的发生位置和概率[[S5,S25]]。结合充型过程的动态动画，可分析金属液面是否平稳上升、是否存在喷射或紊流等异常流态[[S25]]。

### 缩松、缩孔缺陷识别

利用 Niyama 判据在 ViewCAST 中可识别缩松、缩孔潜在区域。当 Mapping Factors 标尺设置为 0~1.1 时，显示值小于 1.1 的区域即为缩松、缩孔可能出现的位置，工程师可据此判断冒口补缩效果是否充分[[S11]]。

### 热裂倾向分析

通过温度场分布与热应力场的联动显示，可识别出凝固过程中温度梯度突变、热应力集中的区域，预判热裂缺陷的潜在位置[[S14]]。结合 Effective Stress 和 Total Displacement 结果，可进一步支撑浇口、冷铁和溢流口的布局优化[[S20,S14]]。

### 工艺参数迭代优化

ViewCAST 导出的按时间序列分布的温度场、固相率和凝固过程图像，可用于比对不同铸造工艺参数（浇注温度、充型速度、冷却工艺等）下的模拟结果，通过反复迭代优化实现工艺成本缩减和研发周期的缩短[[S11,S5]]。

## 限制与注意事项

- **版本兼容性**：ProCAST 2016 版本起已确认可正常使用 ViewCAST 集成功能，无功能缺失记录[[S25]]。早期版本（2008~2009）以独立程序形式运行，需注意操作入口和界面布局差异[[S3,S19]]。
- **命名歧义**：查阅文献时，ViewCAST、Visual-Viewer 和 Visual Viewer 均指向同一后处理环境，如需引用 API 或脚本接口则建议确认所使用的具体版本命名[[S16]]。
- **非 ProCAST 套件的混淆项**：CASTPost 属于 PAM-CAST 产品线，不应与 ViewCAST 混淆[[S4]]。部分软件界面截图中的 “VisualCAST” 标记（如 ProCAST 2009.0 菜单栏）与 ViewCAST 为同一模块的不同表述[[S19]]。

## Sources
- S17: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd273b06-cd96-497f-ac47-0861037cc35f/resource) (`dd273b06-cd96-497f-ac47-0861037cc35f`)
- S22: [表3.1 国内外主流铸造模拟软件](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f69680cd-edbb-41aa-a12f-2e53e9ac09ad/resource) (`f69680cd-edbb-41aa-a12f-2e53e9ac09ad`)
- S24: [ProCAST软件模拟流程示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa554781-e160-4593-92a4-dfdf1eeecb8f/resource) (`fa554781-e160-4593-92a4-dfdf1eeecb8f`)
- S1: [大尺寸铝合金轮毂低压铸造凝固模拟及结构强度的仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0d1cb07b-8d9a-4d31-af09-a50f709fbbdc/resource) (`0d1cb07b-8d9a-4d31-af09-a50f709fbbdc`)
- S15: [大尺寸铝合金轮毂低压铸造凝固模拟及结构强度的仿真分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9e761af5-9b99-4e22-997d-f45f69405132/resource) (`9e761af5-9b99-4e22-997d-f45f69405132`)
- S18: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e14a4c12-1c9e-490f-b811-41979e25169d/resource) (`e14a4c12-1c9e-490f-b811-41979e25169d`)
- S16: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd18bda9-cc1c-466e-87fc-224bca5ba3f4/resource) (`dd18bda9-cc1c-466e-87fc-224bca5ba3f4`)
- S9: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a14f6fc-8302-4aa0-8268-75ac725cf37f/resource) (`8a14f6fc-8302-4aa0-8268-75ac725cf37f`)
- S10: [铝合金大壁厚差支架挤压铸造工艺设计及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8bcc0d92-7418-4cd9-ac20-c39002106f99/resource) (`8bcc0d92-7418-4cd9-ac20-c39002106f99`)
- S2: [铝合金大壁厚差支架挤压铸造工艺设计及数值模拟](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3b913285-1e00-49e4-abf8-fe0a6dd717e9/resource) (`3b913285-1e00-49e4-abf8-fe0a6dd717e9`)
- S4: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ef11554-2e86-4f0f-8f90-4908a7c498b4/resource) (`3ef11554-2e86-4f0f-8f90-4908a7c498b4`)
- S8: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8518bd29-2557-4193-ab70-c8db0f2fac43/resource) (`8518bd29-2557-4193-ab70-c8db0f2fac43`)
- S20: [金属材料液态成型实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f0607f4d-1558-46ad-af42-51691340faa0/resource) (`f0607f4d-1558-46ad-af42-51691340faa0`)
- S6: [压铸模具设计师手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67b3f6f8-e19a-4bae-a872-4c8c2aba7202/resource) (`67b3f6f8-e19a-4bae-a872-4c8c2aba7202`)
- S23: [图2.5 Viewer主页面示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fa27f35b-fe01-4560-b686-91e7fec0c02f/resource) (`fa27f35b-fe01-4560-b686-91e7fec0c02f`)
- S3: [图11-3 ProCAST主界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3cbf9da7-726a-4dbb-9c78-30289a09f370/resource) (`3cbf9da7-726a-4dbb-9c78-30289a09f370`)
- S19: [图11-17 运行DataCAST和ProCAST](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e9bdc1e2-fccc-4c49-8039-8475db0ce79b/resource) (`e9bdc1e2-fccc-4c49-8039-8475db0ce79b`)
- S11: [金属材料液态成型实验教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8eae2810-23f0-45b1-8f4b-fa26f1198fe2/resource) (`8eae2810-23f0-45b1-8f4b-fa26f1198fe2`)
- S5: [基于ProCAST的大尺寸非对称薄壁铝合金铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60c3dba0-96a8-4abd-acf8-925a75695605/resource) (`60c3dba0-96a8-4abd-acf8-925a75695605`)
- S25: [大型长导程ZL205A内鼓低压铸造工艺技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc7019c6-979a-467d-a3b9-e6c8d910a786/resource) (`fc7019c6-979a-467d-a3b9-e6c8d910a786`)
- S14: [基于数值模拟的转子盘熔模铸造工艺的研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/950d606b-47ee-429d-843e-f18d49036098/resource) (`950d606b-47ee-429d-843e-f18d49036098`)