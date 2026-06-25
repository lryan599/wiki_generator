---
version: "v1"
generated_at: "2026-06-18T17:55:45+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 49
  source_quality_score: 0.83
  freshness_score: 0.9
  evidence_coverage_score: 1.0
---

ProCAST 2018是基于有限元法（FEM）的铸造全过程多物理场仿真软件，由法国ESI集团开发，是ProCAST系列软件在2018年度的主要发行版本[[S54,S17]]。该软件通过数值模拟技术，对液态金属充型、凝固、冷却及应力演变等物理过程进行耦合计算，广泛应用于高压压铸（HPDC）、低压压铸（LPDC）、砂型铸造、熔模精密铸造及离心铸造等多种铸造工艺的工艺设计与优化[[S15,S4,S57]]。其核心价值在于，可在模具制造和实际试模之前，在虚拟环境中预测铸造缺陷、优化工艺参数，从而降低研发成本、缩短产品开发周期[[S54,S59]]。

ProCAST 2018的核心求解器采用有限元法（FEM），与市面上部分采用有限差分法（FDM）的主流铸造仿真软件相比，在描述复杂几何边界和薄壁结构特征方面具备更高的解析精度[[S7,S30]]。软件采用模块化架构，由8个标准功能模块组成，包括：传热分析及前后处理（Base License）、流动分析（Fluid flow）、应力分析（Stress）、热辐射分析（Radiation）、显微组织分析（Micromodel）、电磁感应分析（Electromagnetics）、有限元网格划分（MeshCAST）及反向求解（Inverse）[[S42,S61]]。用户可根据具体工程需求，按需组合启用相应的功能模块。对于常规应用，通常配置包含前后处理、网格划分、传热分析、流动分析及应力分析的模块组合[[S42]]。

ProCAST 2018的前后处理流程高度集成。在网格处理阶段，软件支持导入IGES、STEP、Parasolid等多种格式的CAD模型，并具备网格划分工具，能够生成三角形/四边形面网格及四面体/六面体体网格[[S25,S56]]。研究表明，该版本能够处理边长为3mm的高精度等边三角形型壳面网格，合格铸件与浇注系统组合体的面网格与体网格一体化预处理要求，满足复杂熔模铸造构件仿真的前处理精度需求[[S10,S12,S37]]。待求解的物理模型准备完毕后，在“体管理”（Volume Manager）设置界面中定义各部件的属性，包括部件类型（合金或铸型）、材料牌号、初始温度、充填率及应力计算类型等关键参数[[S45]]。

**表1：ProCAST 2018体管理核心参数设置示例**
| 序号 | 部件名称 | 类型 | 材料 | 充填率 (%) | 初始温度 (℃) | 应力类型 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Part_1_1 | Alloy | SCS13 | 0 | 1570 | Linear-Elastic |
| 2 | Part_1_2 | Mold | Silica Sand | 100 | 800 | Rigid |

*表注：此表基于SCS13合金及硅砂铸型的参数设置案例，展示了该版本前处理环节中体管理的典型参数配置。数据来源 [[S45]]。*

ProCAST 2018的铸造工艺仿真能力广泛，全面支持高压压铸（HPDC）、低压压铸（LPDC）、砂型铸造和熔模精密铸造四大核心工艺，同时兼容离心铸造、连续铸造、倾斜铸造等多种特种铸造工艺[[S15,S4,S57]]。其核心功能模块包含：
*   **充型流动模拟**：该模块采用完全耦合的Navier-Stokes流动方程，实现金属液流场与传热的同步计算。针对高压压铸的高速紊流流动，其内置了k-epsilon紊流模型。此外，模块还包含气体分析子模型，用于处理充型过程中的卷气行为，并带有粒子轨迹追踪功能，可全程记录夹杂物的运动路径与最终位置[[S1,S25,S50]]。模拟结果能够精确还原金属液在对称多分支浇注系统内的流动状态，预测卷气、冲蚀等缺陷风险[[S16]]。
*   **凝固过程模拟**：基于热焓方程计算相变潜热，支持充型-凝固完全耦合的高精度求解或单独快速凝固计算。模块内置Niyama判据和缩孔判据，可直接预测铸件内部缩孔、缩松等体积缺陷，后处理可输出任意时刻的固相分数、温度梯度和局部凝固时间等特征参数[[S1,S15,S31]]。
*   **热应力与变形模拟**：实现全流程的流场-温度场-应力场耦合计算，覆盖铸件、铸型、型芯及冷铁等全部组件。模块提供弹性、塑性、粘塑性等多套本构模型，用户可选用Perzyna模型对液相线以下全温度区间的应力应变进行求解，从而获得残余应力分布、热裂倾向指数及最终变形量等结果[[S1,S25,S38,S31]]。
*   **微观组织预测**：采用元胞自动机-有限元（CA-FE）耦合框架，将铸件任意位置的热历程与晶体的形核、长大过程相关联，可仿真计算晶粒尺寸、分布与形貌，实现铸件力学性能的前置预测[[S25,S1,S50]]。

ProCAST 2018内置的材料数据库是一个开放平台，用户可对其进行更新和扩展[[S17]]。该数据库包含了基本合金系统的热力学数据库，能够根据用户直接输入的化学成分，自动计算并生成诸如液相线温度、固相线温度、潜热、比热容和固相率变化等一系列热物性参数[[S17]]。

关于目标合金ZL205A，其为典型的Al-Cu系高强韧铸造铝合金，标准化学成分范围（wt%）为：Cu 4.6~5.4，Mn 0.3~0.5，Ti 0.15~0.30，Zr 0.05~0.2，B 0.005~0.05，Cd 0.15~0.24，V 0.05~0.25，Al为余量。该合金元素组成与ProCAST内置的Al-Cu合金材料数据库支持的计算元素范畴相匹配[[S28,S39]]。用户可依据文献数据或实测结果对其热物性参数进行修正，以实现高精度仿真。核心操作流程如下[[S22,S49,S26,S40]]：
1.  **成分确定**：采用ICP-OES（电感耦合等离子体发射光谱仪）等分析手段，实测目标合金的各元素质量分数。通常需要剔除含量过低的杂质元素，将合规调整后的元素配比输入软件材料数据库。
2.  **计算模型选择**：选定合适的凝固热力学计算模型。常用模型包括Scheil、Lever、Back Diffusion等。其中，Scheil模型基于非平衡凝固假设，适用于固相中无扩散的场合。若选用Back Diffusion模型，需设定一个不低于0.01 K/s的特征冷却速度，该速度需与实际铸造工况相匹配。
3.  **自动计算生成**：软件根据输入成分和所选模型，自动计算出随温度变化的导热系数、密度、比热容/热焓、固相率等关键热物性函数。
4.  **离散数据修正**：若自动计算结果的精度不足以满足要求，用户可手动录入通过实验（如DSC测试）或文献公开获取的温度-参数离散点数据，对自动计算曲线进行修正和校准。

多项公开发表的ZL205A合金铸造仿真研究均证实了该路径的有效性[[S6,S33,S24]]。研究人员可直接利用ProCAST内置的Al-Cu合金材料计算模块，选用Scheil模型，依据ZL205A标准成分完成全部热物性参数的精准构建，生成的密度、比热容随温度变化的曲线可直接用于后续充型凝固过程仿真与缺陷预测，显著提升模拟精度。

ProCAST 2018内置的逆向求解功能，官方正式名称为Inverse反算求解模块，属于软件的独立功能模块，其最典型的应用场景是利用实测温度数据，反向求解铸件与模具之间的界面传热系数（HTC）等未知边界条件或材料热物性参数[[S20]]。该功能基于逆热传导问题（IHCP）的理论框架，以Beck提出的逆热传导法为底层数学支撑。其核心原理是通过迭代求解温度场计算值与实测值的残差，并利用敏感系数逐次修正HTC的取值，直至满足收敛判据，如公式`|Δh_k / h_k| < ε`（ε通常取0.001或更小），从而得到完整的随时间或温度变化的HTC曲线[[S19,S18]]。

在实际操作中，为保持合理的计算时间，需遵循“简化模型、单次仅求解单个未知量”的原则。通常将原始复杂的三维模型简化为对应的二维或二维轴对称子模型，以加速单次正向求解的耗时[[S19,S11]]。完整操作流程如下[[S11,S5,S44]]：
1.  **测温点定义与数据采集**：在物理实验中，将热电偶布置在距离待求界面两侧约5mm的位置，以确保测量质量。运行几次正向温度场计算，在后处理模块（Visual-Viewer）中确定各实测温点对应的有限元网格节点编号。
2.  **实测数据预处理**：将原始采集的实测温度数据，利用Origin等数据处理软件进行滤波平滑处理，并按照规范的格式（如`Prefixim.dat`或`.xyn`文件）生成软件可识别的温度输入文件，文件内包含时间步信息和对应的节点温度数据。
3.  **反算参数设置**：在PreCAST前处理中，完成材料热物性参数、初始条件及正向边界条件的设定。参考已有研究结果，为待求HTC设定一个随温度或时间变化的初始预估值，并激活Inverse反算选项，选中对应的铸件-模具界面。在Inverse Settings面板中，依次导入与温度文件相对应的测温点网格节点编号，并设置温度单位、TAU、SIGMA、CONV、VARB及最大迭代次数（ITRMAX）等核心控制参数。
4.  **求解与验证**：将所有参数配置文件置于同一工作目录下，运行Inverse Solver启动迭代计算。计算收敛后，即可得到反求的最优HTC结果。最后，需将反算得到的HTC曲线代回正向模拟中进行验证，通过对比模拟温度曲线与实测温度曲线的拟合度，来评估反算结果的准确性和可靠性。

**表2：铸模-铸锭界面换热系数反算初始参数参考值（部分）**
| 界面温度 (℃) | 初始HTC (W·m⁻²·℃⁻¹) |
| :---------- | :------------------ |
| 750 | 650 |
| 1100 | 2000 |
| 1500 | 2500 |

*表注：此表为一次钢铁铸件铸模-铸锭界面HTC反算研究中，为ProCAST反算模块设置的初始HTC值，用于迭代计算的起始估计。实际应用时需根据具体合金和工艺进行调整。数据来源 [[S32]]。*

工程应用案例证明该模块的有效性。在对1550℃和1600℃两种钢液浇注温度下的铸模-铸锭界面HTC反算中，最终得到的HTC在0-100s内维持在2500 W·m⁻²·℃⁻¹以上，随后在100-500s内快速降至约1200-1400 W·m⁻²·℃⁻¹，500s后缓慢下降至约445-703 W·m⁻²·℃⁻¹并趋于稳定。将反算结果代入正向模拟后，测温点的模拟温度与实测温度差值在30℃以内[[S44]]。在A356铝合金低压铸造车轮的冷却水路-模具界面HTC反算中，通过两次迭代即求得最优HTC为5004 W/(m²·K)，对应降温曲线的拟合误差小于5%[[S62]]。在Cu-7Ni-7Al-4Fe铜镍合金通海阀铸件与砂型界面的HTC反算中，将求得的随温度变化的HTC（1060℃，454 W/m²·K；1160℃，480 W/m²·K；1200℃，550 W/m²·K；1220℃，560 W/m²·K）代入正向模拟，实测与模拟温度平均差值仅为5.85℃[[S51]]。这些案例证实了ProCAST的Inverse模块在反算界面换热系数方面的可行性与精度。

尽管功能强大，ProCAST 2018在工程应用中仍存在一些固有局限性与计算考量：
*   **网格处理的复杂性**：在导入IGES等通用CAD格式模型时，极易产生多余图元、重叠面、面间隙等几何缺陷，用户需投入大量精力手动修复模型。同时，网格划分质量对计算收敛性和精度至关重要，若相邻网格单元尺寸差异过大，或存在不连续、单边接触的网格，将直接导致计算不收敛甚至程序崩溃[[S14,S4]]。
*   **多相流计算假设的限制**：软件默认将压铸过程中的金属液视为不可压缩流体[[S14]]。但在高速高压（内浇口流速高于10m/s甚至可达100m/s）的极端工况下，气液两相的交互作用极为复杂，计算精度存在固有误差，无法完全复现高压充填下卷气、氧化夹杂的真实分布状态[[S29,S14]]。
*   **逆向求解功能的局限**：在反算HTC时，软件反算方式通常只能输入单条测温曲线进行拟合，这导致在多点位测温时，未参与反算拟合的测温点正向模拟误差可能较大，最高可达25.5℃。因此，其精度相对于采用自行编写的多曲线耦合反算程序而言略低[[S21]]。
*   **计算效率**：ProCAST支持多机并行计算以提升效率。对于常规中等规模的压铸件（体网格数约1000万级），在主频2.8GHz、内存1GB以上的硬件环境下，单个工艺周期的热平衡及充型凝固模拟总耗时约为10-15分钟[[S2,S41]]。然而，大规模、高精度要求的仿真任务依然需要可观的算力与时间成本。

ProCAST 2018在压铸领域，特别是汽车与通讯零部件制造中，得到了广泛应用。在汽车结构件方面，其成功应用于铝合金减震塔、一体化前舱盖、铝合金车门等典型大型薄壁件的充型、缺陷预测与工艺优化。例如，对某AlSi9Cu铝合金一体化前舱盖的仿真分析表明，整个充型时间约为0.5s，并获得了不同区域的充填速度与缺陷分布，验证了“一体化压铸”在大型薄壁件上的成型可行性[[S59,S47]]。在通讯壳体方面，软件被用于评估和优化铝合金电器配件、薄壁通讯机箱、手机壳体等产品的压铸工艺，其缩孔缩松缺陷的预测结果与实际生产吻合度高，能有效指导实际生产，降低试模成本[[S4,S3]]。

通过ProCAST软件生成的手机壳体缩孔缩松缺陷模拟结果，直观展示了软件在通讯类薄壁压铸件缺陷预测上的应用效果，支撑了仿真精度相关内容的说明[[S3]]。
![手机壳体缩孔缩松模拟结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0857ae7d-4cae-4431-8caf-675e61d91722/resource)

鉴于上述功能、模块与应用场景，ProCAST 2018在不同用户群体与技术场景中有各类别称，可视为其应用维度的延伸：
*   **ProCAST有限元软件平台**与**ProCAST有限元仿真平台**：多用于高校与科研院所，侧重于对异形复杂铸件进行铸造工艺仿真教学和基础工艺研究，强调其作为FEM平台的科研属性[[S48,S53,S7]]。
*   **ProCAST多物理场仿真平台**：多用于工业端，侧重于充型-凝固-应力多场耦合仿真，以解决量产铸造过程中的工艺优化问题，强调其多物理场耦合能力[[S48,S53,S7]]。
*   **ProCAST 2018有限元仿真软件**：特指该2018年版本的专属标注，仅在对应版本的特定工程案例研究中作为研究对象或工具使用[[S48,S53,S7]]。

**表3：ProCAST 2018与部分主流铸造数值模拟软件技术特性对比**
| 软件名称 | 核心求解方法 | 开发主体 | 主要特点及适用场景 |
| :--- | :--- | :--- | :--- |
| **ProCAST** | **有限元法 (FEM)** | **法国 ESI Group** | **多物理场耦合能力强，仿真精度高，尤其适用于几何形状复杂（如熔模铸件）的高保真模拟。** |
| FLOW-3D CAST | 有限差分法 (FDM) | 美国 Flow Science | 采用独有的TruVOF自由表面追踪技术，在充型流动、特别是卷气预测方面有优势。 |
| MAGMASOFT | 有限差分法 (FDM) | 德国 MAGMA GmbH | 综合工艺设计与稳健性评估能力强，数据库积累深厚，在压铸和铸铁领域应用广泛。 |
| 华铸CAE | 有限差分法 (FDM) | 华中科技大学 | 国内商品化程度最高的铸造模拟软件，性价比较高，在国内铸造企业有大量应用。 |
| AnyCasting | 有限差分法 (FDM) | 韩国 AnyCasting Co. | 操作界面友好，专注于铸造工艺仿真，尤其在压铸领域的应用较为成熟。 |

*表注：此表横向对比了ProCAST 2018与其他主流铸造仿真软件在技术路线和应用上的差异。数据来源 [[S30, S9]]。*

## Sources
- S54: [盘类零件压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d3a31ed1-0c0d-4c71-bc3c-6818b40da0ae/resource) (`d3a31ed1-0c0d-4c71-bc3c-6818b40da0ae`)
- S17: [压铸模CADCAECAM](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3ef11554-2e86-4f0f-8f90-4908a7c498b4/resource) (`3ef11554-2e86-4f0f-8f90-4908a7c498b4`)
- S15: [800MW-1000MW级不锈钢转轮铸件铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3c1603cf-1be4-4bca-b6df-6bf644a57b69/resource) (`3c1603cf-1be4-4bca-b6df-6bf644a57b69`)
- S4: [燃汽轮机用SCS13合金锁键铸造工艺数值模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0999261c-ff8b-4cc2-91a7-a495826e0198/resource) (`0999261c-ff8b-4cc2-91a7-a495826e0198`)
- S57: [Cu及Cu-Sn合金凝固过程模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd273b06-cd96-497f-ac47-0861037cc35f/resource) (`dd273b06-cd96-497f-ac47-0861037cc35f`)
- S59: [新型一体化前舱盖的压铸与模态分析](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8ff7d8e-dae0-49a4-aeac-4bb70b4c9f7e/resource) (`f8ff7d8e-dae0-49a4-aeac-4bb70b4c9f7e`)
- S7: [燃汽轮机用SCS13合金锁键铸造工艺数值模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/12ddc946-447d-4491-91e0-c98f1b605429/resource) (`12ddc946-447d-4491-91e0-c98f1b605429`)
- S30: [表2.1 主流铸造数值模拟软件对比](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/62ad51a3-c595-452b-8c7d-bff26d5f2a5f/resource) (`62ad51a3-c595-452b-8c7d-bff26d5f2a5f`)
- S42: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8a14f6fc-8302-4aa0-8268-75ac725cf37f/resource) (`8a14f6fc-8302-4aa0-8268-75ac725cf37f`)
- S61: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fe0c050e-e159-4526-8b45-b84e3a2141d0/resource) (`fe0c050e-e159-4526-8b45-b84e3a2141d0`)
- S25: [基于ProCAST砂型铸造高锰钢斗齿的工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5434f168-c7cc-4b02-af30-893e26f72d94/resource) (`5434f168-c7cc-4b02-af30-893e26f72d94`)
- S56: [基于虚拟现实的特种铸造工艺仿真研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd18bda9-cc1c-466e-87fc-224bca5ba3f4/resource) (`dd18bda9-cc1c-466e-87fc-224bca5ba3f4`)
- S10: [锁键及浇注系统组合体网格划分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/20b17cd1-58b6-4ecc-b70e-8a2fee2deee4/resource) (`20b17cd1-58b6-4ecc-b70e-8a2fee2deee4`)
- S12: [锁键及浇注系统组合体的型壳面网格划分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2389ac05-f0a9-44c0-80b8-0026919b2855/resource) (`2389ac05-f0a9-44c0-80b8-0026919b2855`)
- S37: [图3.7 锁键与浇注系统三维组树模型面网格与体网格划分](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bec93b8-9e84-4bac-8200-6385fc1b1e35/resource) (`7bec93b8-9e84-4bac-8200-6385fc1b1e35`)
- S45: [图3.8 体管理参数设置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9a0ed3fa-a5a7-4790-80c2-9585fab11f60/resource) (`9a0ed3fa-a5a7-4790-80c2-9585fab11f60`)
- S1: [金属液态成形工艺设计](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/01030027-9a05-4921-9760-3e0716e2d640/resource) (`01030027-9a05-4921-9760-3e0716e2d640`)
- S50: [镍基高温合金真空低压铸造工艺基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/be724a61-fb8f-4668-a542-d511aa30272f/resource) (`be724a61-fb8f-4668-a542-d511aa30272f`)
- S16: [TextNode33](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3dd9cbb6-eccc-4c95-b43b-845bbf9bcb56/resource) (`3dd9cbb6-eccc-4c95-b43b-845bbf9bcb56`)
- S31: [城轨车辆铝合金铸造牵引梁材料与成型工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67439f79-5134-4af0-bdd7-6ba5623ec810/resource) (`67439f79-5134-4af0-bdd7-6ba5623ec810`)
- S38: [基于CAE分析的压铸模具表面激光强化技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7d3ef7ec-65e9-4e35-993a-19ad9926f654/resource) (`7d3ef7ec-65e9-4e35-993a-19ad9926f654`)
- S28: [表2-1 ZL205A铝合金化学成分（wt%）[69]](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/60794375-b354-4522-bf6b-d84035cae814/resource) (`60794375-b354-4522-bf6b-d84035cae814`)
- S39: [铝与铝合金速查手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/81eefca1-b17e-4298-bcc1-329a2f5ff0c5/resource) (`81eefca1-b17e-4298-bcc1-329a2f5ff0c5`)
- S22: [Mg-10Gd-2Y-1Zn-0.5Zr镁合金基座件基于有限元模拟的铸造残余应力研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/4b0dedca-d2b7-407f-9165-d1438b3f1789/resource) (`4b0dedca-d2b7-407f-9165-d1438b3f1789`)
- S49: [AZ91D镁合金构件铸造残余应力有限元模拟研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a8f1b3cc-ac6d-40b5-b8d3-c18420f8ea6f/resource) (`a8f1b3cc-ac6d-40b5-b8d3-c18420f8ea6f`)
- S26: [铜镍铝合金通海阀铸造缺陷预测及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5de1d0bc-03b1-49fd-be0c-19aaa80d8ead/resource) (`5de1d0bc-03b1-49fd-be0c-19aaa80d8ead`)
- S40: [燃汽轮机用SCS13合金锁键铸造工艺数值模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/827634ab-cfbf-4cc2-a2bc-bf2e0e58d05b/resource) (`827634ab-cfbf-4cc2-a2bc-bf2e0e58d05b`)
- S6: [ZL205A合金圆筒状包络构件低压铸造线状偏析形成机理及控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1201c591-d552-4b9f-98b8-271d4ebe3b4c/resource) (`1201c591-d552-4b9f-98b8-271d4ebe3b4c`)
- S33: [ZL205A合金密度随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d3aa385-e6ba-4643-a790-5be9e59ac84e/resource) (`6d3aa385-e6ba-4643-a790-5be9e59ac84e`)
- S24: [(c) ZL205A铝铜合金比热容随温度变化曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/515cdd70-9b53-4df3-a37b-6547d016c536/resource) (`515cdd70-9b53-4df3-a37b-6547d016c536`)
- S20: [镍基高温合金真空低压铸造工艺基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/43983e8d-2550-45fd-bd6b-4bc03493d0e8/resource) (`43983e8d-2550-45fd-bd6b-4bc03493d0e8`)
- S19: [铸模-铸锭界面气隙对综合界面换热系数的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/421657c6-405f-4a70-a3bb-71ab8693f782/resource) (`421657c6-405f-4a70-a3bb-71ab8693f782`)
- S18: [气动元件阀体系列铸造工艺设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/40a5f1d3-7229-41f6-8fb1-5e9a2dfee043/resource) (`40a5f1d3-7229-41f6-8fb1-5e9a2dfee043`)
- S11: [铸模-铸锭界面气隙对综合界面换热系数的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22302f98-3314-493a-ac37-8546f97e8988/resource) (`22302f98-3314-493a-ac37-8546f97e8988`)
- S5: [大型铝合金轮毂低压铸造双浇道工艺的模拟及优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0c302c49-014d-42ba-b96d-3ae4dc889a9b/resource) (`0c302c49-014d-42ba-b96d-3ae4dc889a9b`)
- S44: [铸模-铸锭界面气隙对综合界面换热系数的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/933c6899-3b6d-4940-8734-596a7124f06b/resource) (`933c6899-3b6d-4940-8734-596a7124f06b`)
- S32: [表5.3 界面换热系数随温度变化的初始值hₖ⁰](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/67c18984-e17e-456a-9586-1a9b30ea73fe/resource) (`67c18984-e17e-456a-9586-1a9b30ea73fe`)
- S62: [A356低压铸造铝合金车轮工艺优化及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ff43a93d-76b2-432f-ab5f-ec45fa615e2b/resource) (`ff43a93d-76b2-432f-ab5f-ec45fa615e2b`)
- S51: [铜镍铝合金通海阀铸造缺陷预测及工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf868c73-ff0e-4b2b-9f10-89fc5d43b9e7/resource) (`bf868c73-ff0e-4b2b-9f10-89fc5d43b9e7`)
- S14: [低熔点合金再造加工基准的组织性能及成形工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/30a05f52-399e-48c5-aaa8-bc548788c66e/resource) (`30a05f52-399e-48c5-aaa8-bc548788c66e`)
- S29: [压铸过程数值模拟技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/610a031e-bceb-406c-ad4f-62285e10d3fa/resource) (`610a031e-bceb-406c-ad4f-62285e10d3fa`)
- S21: [A356低压铸造铝合金车轮工艺优化及组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/499a64e4-bd7f-49d6-ad60-c40a183ff5ec/resource) (`499a64e4-bd7f-49d6-ad60-c40a183ff5ec`)
- S2: [气缸盖罩盖铸件热平衡分析不同模拟方案计算效率比较](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04a99c87-d293-4601-9ee7-4425a547f5e6/resource) (`04a99c87-d293-4601-9ee7-4425a547f5e6`)
- S41: [挤压铸造成形铝合金飞轮壳构件微观组织与力学性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86f9aa7c-356e-4e30-a1e8-766f1f791f2c/resource) (`86f9aa7c-356e-4e30-a1e8-766f1f791f2c`)
- S47: [基于压铸工艺的铝合金车门结构设计与优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a4b48e1a-5f56-44e0-98c2-921c1a3afe20/resource) (`a4b48e1a-5f56-44e0-98c2-921c1a3afe20`)
- S3: [手机壳体缩孔缩松模拟结果（ProCAST软件）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0857ae7d-4cae-4431-8caf-675e61d91722/resource) (`0857ae7d-4cae-4431-8caf-675e61d91722`)
- S48: [基于ProCAST砂型铸造高锰钢斗齿的工艺优化](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a724de55-42e0-46ef-87d6-dab50d97a214/resource) (`a724de55-42e0-46ef-87d6-dab50d97a214`)
- S53: [基于数值模拟的铝合金涡轮蜗壳铸造工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cbcee639-0ac9-4d7f-8309-92a4c5d40853/resource) (`cbcee639-0ac9-4d7f-8309-92a4c5d40853`)
- S9: [图2.1 数值仿真软件简介](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18e2326b-ae98-4bac-a90f-aaf4d66bff7a/resource) (`18e2326b-ae98-4bac-a90f-aaf4d66bff7a`)