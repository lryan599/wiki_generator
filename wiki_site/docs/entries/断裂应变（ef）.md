---
version: "v1"
generated_at: "2026-06-18T18:32:56+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 43
  source_quality_score: 0.85
  freshness_score: 0.85
  evidence_coverage_score: 1.0
---

## 概述

断裂应变是衡量压铸合金在拉伸载荷作用下断裂前所能承受的最大塑性变形程度的核心力学性能指标，常用符号e<sub>f</sub>（工程断裂应变）或ε<sub>f</sub>（真实断裂应变）表示[[S57]]。它直接反映了压铸件的延性、抗断裂能力，是汽车一体压铸结构件碰撞安全仿真的核心输入参数[[S29,S15]]。简言之，压铸件在碰撞、过载或装配变形工况下局部塑性应变须低于材料断裂应变阈值，才能避免贯穿式裂纹和过早断裂[[S29]]。

## 定义与物理含义

### 工程断裂应变（e<sub>f</sub>）

试样断裂时刻标距总伸长与原始标距的比值，计算式为：

e<sub>f</sub> = (L<sub>f</sub> − L<sub>0</sub>) / L<sub>0</sub>

其中L<sub>f</sub>为断裂后对接测得的标距长度，L<sub>0</sub>为试样原始标距，属于工程应变范畴，表征材料整体沿轴向的塑性变形能力[[S11]]。该数值与常用断后伸长率A%的计算逻辑相近，但断裂应变可覆盖加载全周期的瞬时测量结果[[S20,S33,S31]]。

### 真实断裂应变（ε<sub>f</sub>）

以试样断裂瞬间的瞬时横截面积为基准的对数应变，计算公式为：

ε<sub>f</sub> = ln(A<sub>0</sub> / A<sub>f</sub>)

其中A<sub>0</sub>为原始横截面积，A<sub>f</sub>为断裂后缩颈处最小横截面积。可结合体积不变假设由断面收缩率Z推导得到：ε<sub>f</sub> = ln(1/(1−Z))[[S11,S20]]。真实断裂应变反映局部缩颈区域断裂瞬间的真实变形程度。

### 符号使用规范

工程领域常用e<sub>f</sub>作为工程断裂应变的缩写符号，连续介质力学和塑性成形仿真领域通常用ε<sub>f</sub>（希腊字母ε下标f）作为断裂应变的通用标识[[S57]]。

### 与相关概念的区别

- **与断后伸长率A%**：断后伸长率A%仅表征标距段内平均轴向残余塑性变形，数值与原始标距长度强相关，不同标距测得的A%不可直接对比。断裂应变可覆盖断裂瞬间包含弹性变形的总应变，在塑性成形仿真中应用更广泛[[S20,S33,S31]]。
- **与断面收缩率Z%**：断面收缩率以横截面积缩减比例为度量，不受标距影响，可直接反映局部缩颈区域变形程度；而工程断裂应变依赖标距设置，二者物理维度完全不同，不可直接等效[[S20,S33,S41]]。
- **与断裂总伸长率A<sub>t</sub>**：GB/T 228.1中A<sub>t</sub>为断裂时刻总伸长（含弹性与塑性伸长）与原始标距的比值，扣除卸载后弹性恢复量得到的残余伸长率可换算为工程断裂应变e<sub>f</sub>[[S26]]。

![应力-应变曲线示意图，展示弹性区与塑性变形区直至断裂的不同区域](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afc8bf82-54ce-4640-8fad-b18219dd1a2e/resource)
*图1：标准应力-应变曲线示意图，横轴为应变、纵轴为应力，划分弹性区与塑性变形区直至断裂的不同区域，直观展示从弹性变形到断裂的全流程应变变化规律[[S38]]*

## 测量方法与标准

断裂应变的测定依据室温拉伸试验，主要执行以下标准：

### GB/T 228.1（中国标准）

试样原始标距L<sub>0</sub>与平行段原始横截面积S<sub>0</sub>满足比例试样关系L<sub>0</sub> = k√S̅<sub>0</sub>，常用k值为5.65（对应L<sub>0</sub>=5d的圆棒试样）[[S24,S40]]。标距测量分辨率需优于0.1mm，结果精度要求±0.25mm[[S40]]。

断裂有效性判定规则为：常规情况下仅当断裂位置距离最近的标距标记不小于原始标距L<sub>0</sub>的1/3时测试结果有效；若测得的断裂应变数值满足相关标准规定的最低要求，无论断裂位置如何结果均判定为有效。断裂位置不符合要求时可使用移位法计算得到等效断后标距，避免试样报废[[S40,S3]]。

### ASTM E8/E8M（美国标准）

小尺寸拉伸试样的原始标距G推荐取值为25.0mm；米制版本E8M的圆棒试样要求原始标距为5倍试样直径，英制版本E8对应4倍试样直径[[S35,S25]]。通过记录载荷-位移曲线换算得到应力-应变曲线，最终得到试样的断裂延伸率即工程断裂应变[[S25]]。

### ISO 6892-1（国际标准）

室温测试区间为10~35℃，高精度测试要求温度控制在23±5℃。采用引伸计监测试样标距段的全程变形，最终通过断裂时刻的延伸量除以引伸计标距得到断裂应变测试结果[[S27,S45]]。针对压铸Al-10Si-0.3Mg合金的测试案例显示，该标准下测得的同批次材料断裂应变数值存在一定离散性，分布范围为11.3%~16.6%[[S45,S34]]。

![高压铸造Al-10Si-0.3Mg合金六次重复测试的工程应力应变曲线，失效应变在11.34%至16.58%间存在较大离散度](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f005a557-051c-4ae8-911f-8d2fe2e3cd96/resource)
*图2：高压铸造Al-10Si-0.3Mg合金的实测工程应力应变曲线，6次重复测试的失效应变在11.34%至16.58%区间，直观展示压铸铝合金断裂应变的离散性特征[[S55]]*

## 在压铸中的工程意义

断裂应变是压铸行业评价压铸件延性、抗断裂能力的核心指标[[S29]]，其工程意义体现在：

**碰撞安全设计**：压铸件碰撞过程中局部塑性应变必须低于材料断裂应变阈值才能避免贯穿式裂纹。某一体压铸车型的仿真结果显示，30km/h正面中速碰撞工况下压铸件最大塑性应变为3.2%，低于设定的6%断裂应变阈值要求，验证了以断裂应变作为设计边界的安全开发方法有效性[[S48,S19]]。不同车速碰撞场景下的变形策略设计需以材料断裂应变阈值作为边界条件：中低速碰撞下压铸件不产生非线性塑性变形损伤，高速碰撞下仅局部塑性变形不发生整体断裂[[S29,S19]]。

**装配变形可靠性**：高断裂应变的压铸合金可满足自冲铆接等大变形装配工艺需求，避免装配过程中压铸件出现微裂纹甚至断裂[[S36,S47]]。AlSi10MnMg减震塔经T7处理后断裂延伸率≥10%，非常适合自冲铆接（SPR）连接[[S36]]。

## 常见压铸合金的典型断裂应变

下表汇集权威来源中的典型压铸合金工程断裂应变数据：

| 合金牌号 | 典型工程断裂应变 | 备注 | 来源 |
|---------|---------------|------|------|
| **铝合金** | | | |
| ADC12 | 2%~3% (经Sr变质可达3.2%) | JIS标准常规压铸 | [[S39,S14]] |
| A380 (ADC10) | 3% | 压铸模具工程师手册 | [[S6]] |
| AlSi10MnMg (T7) | ≥10% | 免热处理优化版本铸态可达8%~16% | [[S36,S17,S49]] |
| **镁合金** | | | |
| AZ91D | 0.5%~3% | 真空压铸后伸长率可提升40.63% | [[S6,S10]] |
| AM60 | 4%~8% | 真空压铸后可达16%以上 | [[S6,S10]] |
| **锌合金** | | | |
| Zamak 3 (铸态) | 6.3% (时效态16%) | 热室压铸锌合金标准牌号 | [[S56,S23]] |

## 影响因素

### 铸造缺陷（气孔、缩松）

高压铸造铝合金试样的断口缺陷面积占比从0增加至约23%时，真断裂伸长率从约2.1%陡降至0.3%，缺陷占比对塑性延伸性能的影响远高于其对弹性模量、屈服强度的影响[[S30]]。

针对Al-10Si-0.3Mg高压铸造薄壁件的研究表明：试样标距段内局部最大孔隙率小于0.55%时，断裂应变分布的上下边界差值随局部最大孔隙率升高而增大；当局部最大孔隙率高于0.55%时，该差值随局部最大孔隙率升高而减小。体积大于0.015mm³且靠近试样侧表面的孔隙会引发边缘应变局部化，促进早期裂纹萌生，大幅降低断裂应变[[S8]]。

### 真空压铸与高速压铸

型腔绝对压力降至10kPa的ADC12铝合金真空压铸试样，相比普通压铸试样延伸率提升36%，对应断口中韧窝深度明显加深，从偏向脆性的准解理断裂向高延性的韧性断裂转变[[S53]]。AZ91镁合金真空压铸件相比普通压铸件孔隙率显著降低，断裂应变相关的伸长率指标提升40.63%[[S10]]。

### 化学成分与微观组织

- **共晶硅相**：针状、高长径比的共晶硅相在加载过程中引发局部应力集中，降低断裂应变；T6热处理可将板状共晶硅相球化转变为粒状，减少应力集中，在保证强度提升的同时保留可观的断裂韧性[[S28]]。挤压铸造A356铝合金经T4热处理后共晶Si相充分球化，液态挤压试样延伸率提升76%至12.2%，半固态挤压试样延伸率最高可达15.3%[[S42]]。
- **富铁相**：压铸AlSi10-0.16Fe0.6Mn合金（初生相为α-Al）在高应变下富Fe金属间化合物仅产生难以扩展的小尺寸微裂纹；而初生相为α-Fe的同成分合金在低应变下即发生金属间化合物断裂、微裂纹连通加速断裂，显著降低断裂应变[[S18]]。
- **枝晶尺寸**：枝晶尺寸较大时断裂以穿晶断裂为主，枝晶尺寸细化后断裂向沿晶断裂转变；随冷却速度提升，压铸铝合金的一次、二次枝晶臂间距同步减小，对应材料韧性提升、断裂应变升高[[S7,S37]]。

### 热处理状态

流变挤压铸造7075合金铸态的断裂应变显著高于T6热处理态：T6态通过析出强化将抗拉强度大幅提升至520MPa，但塑性下降明显，拉伸断口出现大量浅小韧窝，平均伸长率降至9.05%[[S16,S46]]。

## 与增材制造工艺的区分

研究提示中涉及的“扫描速度1300mm/s时断裂应变26.3%”并非压铸工艺数据，而是**激光粉末床熔融（LPBF/SLM）增材制造**工艺的实验结果。在P=230W、扫描间距70μm的工艺条件下，(Al₂O₃+SiC)混杂增强AlSi10Mg基复合材料当激光扫描速度为1300mm/s时，**压缩断裂应变**可达26.3%，但同参数下其拉伸伸长率仅为0.317%[[S4,S52]]。

SLM成形该材料的力学性能随扫描速度提升整体呈先升高后降低的规律：扫描速度700mm/s时拉伸性能最优，极限抗拉强度达413MPa，对应伸长率5.43%；扫描速度900mm/s时压缩屈服强度达到峰值408MPa；扫描速度1300mm/s时压缩断裂应变达到峰值26.3%[[S52]]。上述数据明确属于增材制造领域，与压铸类工艺需完全区分[[S4]]。

## 关联概念

- **延伸率A%**：断后标距残余伸长与原始标距的百分比，与工程断裂应变计算逻辑相近但仅反映卸载后残余变形[[S20,S31]]
- **断面收缩率Z%**：断后缩颈处横截面积缩减比例，不受标距影响，能更可靠地反映局部塑性[[S20,S33]]
- **弹性模量E**：弹性范围内应力与应变的比值，表征材料刚度[[S11,S33]]
- **屈服强度R<sub>e</sub>**：材料开始产生宏观塑性变形时的应力阈值[[S31]]
- **应力-应变曲线**：完整描绘材料从弹性变形到塑性变形直至断裂的全过程，断裂应变为曲线终点的应变值[[S38]]

## Sources
- S57: [铝合金结构](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f8a8d108-3629-4f1f-815d-e89ada4f899a/resource) (`f8a8d108-3629-4f1f-815d-e89ada4f899a`)
- S29: [大型压铸车身结构安全开发技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/754519c5-2cac-4708-8b28-884b4e4b0f89/resource) (`754519c5-2cac-4708-8b28-884b4e4b0f89`)
- S15: [大型压铸车身结构安全开发技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2fb068cc-0b58-4449-ae8a-9e541757f789/resource) (`2fb068cc-0b58-4449-ae8a-9e541757f789`)
- S11: [金属板料成形及其模具设计实例](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/24b0d505-5db7-4bd1-a438-a758dc6ea994/resource) (`24b0d505-5db7-4bd1-a438-a758dc6ea994`)
- S20: [机械工程材料与热加工工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/401e8d10-2332-40ac-8b8c-982a4b234a5d/resource) (`401e8d10-2332-40ac-8b8c-982a4b234a5d`)
- S33: [模具材料及材料成形工艺](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/98087d5b-627b-4e61-90af-a49d09844488/resource) (`98087d5b-627b-4e61-90af-a49d09844488`)
- S31: [工程材料与金属热加工](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/82fd4031-d533-4902-9b34-ca5a33ca209c/resource) (`82fd4031-d533-4902-9b34-ca5a33ca209c`)
- S41: [简明铝合金加工手册](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c4c7e58d-ecc6-450d-ac86-e0591c36a78d/resource) (`c4c7e58d-ecc6-450d-ac86-e0591c36a78d`)
- S26: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/690e6b10-2d2a-40bc-9c25-e1bb9550d73e/resource) (`690e6b10-2d2a-40bc-9c25-e1bb9550d73e`)
- S38: [应力-应变曲线示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/afc8bf82-54ce-4640-8fad-b18219dd1a2e/resource) (`afc8bf82-54ce-4640-8fad-b18219dd1a2e`)
- S24: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5f8d3368-dabf-4323-a768-8be1f198c2d8/resource) (`5f8d3368-dabf-4323-a768-8be1f198c2d8`)
- S40: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c35f980a-24a8-4130-94ad-67f36071e36f/resource) (`c35f980a-24a8-4130-94ad-67f36071e36f`)
- S3: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0ae3471c-e96e-4a35-bc2a-7579a64613ee/resource) (`0ae3471c-e96e-4a35-bc2a-7579a64613ee`)
- S35: [1991 annual book of astm standards section 1 lron and steel products vol__d9cf5303c8](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9fdce008-15d0-4cbf-b4e2-1974535a3214/resource) (`9fdce008-15d0-4cbf-b4e2-1974535a3214`)
- S25: [alloys and composites corrosion and mechanical properties__573c8b2ba2](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/66f05b23-caf4-490d-b3ad-3f578d21459e/resource) (`66f05b23-caf4-490d-b3ad-3f578d21459e`)
- S27: [变形铝合金材料标准汇编下](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6c3e2ca0-d974-4354-a675-f12db1ec7230/resource) (`6c3e2ca0-d974-4354-a675-f12db1ec7230`)
- S45: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d63bd42e-e21e-4b86-82a2-36fa798abaae/resource) (`d63bd42e-e21e-4b86-82a2-36fa798abaae`)
- S34: [金属注射成形精密零件生产与应用](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9b8c6d9c-a3bd-4ffe-86b7-a8574e9be514/resource) (`9b8c6d9c-a3bd-4ffe-86b7-a8574e9be514`)
- S55: [图5.1 实验测得的高压铸造Al-10Si-0.3Mg合金的工程应力应变曲线结果](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f005a557-051c-4ae8-911f-8d2fe2e3cd96/resource) (`f005a557-051c-4ae8-911f-8d2fe2e3cd96`)
- S48: [表3 仿真结果汇总](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ddec6491-6481-416d-8a03-f92cc3bb8cd5/resource) (`ddec6491-6481-416d-8a03-f92cc3bb8cd5`)
- S19: [一体化压铸车型被动安全性能开发研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3e2f104b-bce0-4362-bb2f-ac570e20a6a9/resource) (`3e2f104b-bce0-4362-bb2f-ac570e20a6a9`)
- S36: [车身真空高压压铸技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a999c2cc-9d4a-4227-a72c-d2ef1ab916c6/resource) (`a999c2cc-9d4a-4227-a72c-d2ef1ab916c6`)
- S47: [车身真空高压压铸技术研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/dd9cf053-008b-4413-93e7-5875dc5224c7/resource) (`dd9cf053-008b-4413-93e7-5875dc5224c7`)
- S39: [表 3-36 压力铸造用铝合金的力学性能 (JIS 标准)](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b6ad0d53-b78f-4958-bf09-93d87e8d9420/resource) (`b6ad0d53-b78f-4958-bf09-93d87e8d9420`)
- S14: [免固溶处理Al-Si-Zn-Mg-Cu铝合金及其凝固行为研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2c66b553-fe19-43d2-88c4-b3e42bb2a58b/resource) (`2c66b553-fe19-43d2-88c4-b3e42bb2a58b`)
- S6: [国外常用压铸镁合金的力学性能（含与压铸铝合金A380的对比）](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1454dd4e-7e78-4e2e-b87b-33711977cab0/resource) (`1454dd4e-7e78-4e2e-b87b-33711977cab0`)
- S17: [轻合金大型一体化结构部件压铸成形技术研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/39d012df-15d6-44a2-b46f-a0fdb58209d1/resource) (`39d012df-15d6-44a2-b46f-a0fdb58209d1`)
- S49: [免热处理压铸Al-9Si合金成分与工艺优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e332d0be-4b58-45fb-97d7-9a4318d58706/resource) (`e332d0be-4b58-45fb-97d7-9a4318d58706`)
- S10: [真空压铸铝合金发动机缸体缺陷与热处理研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/22a1e020-4a29-49ff-b13f-7bde6c9d7f7c/resource) (`22a1e020-4a29-49ff-b13f-7bde6c9d7f7c`)
- S56: [0023_1723c0e84400287c_Zamak](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f5b6764e-2a6c-4500-88e9-8d33e727fcb7/resource) (`f5b6764e-2a6c-4500-88e9-8d33e727fcb7`)
- S23: [0023_1723c0e84400287c_Zamak](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/5ba33081-5841-4639-997e-8952e2c7c508/resource) (`5ba33081-5841-4639-997e-8952e2c7c508`)
- S30: [encyclopedia of aluminum and its alloys two volume set__9820af6cf3](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7bf6d407-d595-48ea-a0ea-b9802b47f813/resource) (`7bf6d407-d595-48ea-a0ea-b9802b47f813`)
- S8: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18a90615-971a-47d0-9e14-7d041a8033bd/resource) (`18a90615-971a-47d0-9e14-7d041a8033bd`)
- S53: [ADC12铝合金真空压铸充型过程及铸件性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ec51670b-eb4d-44ae-aff2-3bf36f8d8ee7/resource) (`ec51670b-eb4d-44ae-aff2-3bf36f8d8ee7`)
- S28: [基于多尺度力学方法的Al-10Si-0.3Mg合金高压铸造薄壁件的延性预测](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6e812a70-80be-422d-986c-298438d85825/resource) (`6e812a70-80be-422d-986c-298438d85825`)
- S42: [不同成形方式及热处理对A356铝合金组织与性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c96d7ae5-9875-4f74-953e-640680bc1d2c/resource) (`c96d7ae5-9875-4f74-953e-640680bc1d2c`)
- S18: [压铸铝_镁合金微观组织特征与分布的三维断层扫描研究进展](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3db1ea2b-98b1-48a8-848d-2c565eba5a34/resource) (`3db1ea2b-98b1-48a8-848d-2c565eba5a34`)
- S7: [亚共晶铝硅合金AlSi10Mg的压铸工艺研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/18910c2d-3807-4df8-a76e-4e00a81ca8d9/resource) (`18910c2d-3807-4df8-a76e-4e00a81ca8d9`)
- S37: [压力铸造对Al-Si-Cu合金组织的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ad68ada4-686f-41ef-96fc-36febafc8f9e/resource) (`ad68ada4-686f-41ef-96fc-36febafc8f9e`)
- S16: [铝合金流变挤压铸造成形技术基础研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/387d1045-0f28-4e66-bf13-80b31dcec003/resource) (`387d1045-0f28-4e66-bf13-80b31dcec003`)
- S46: [图4.21 流变挤压7075合金制件铸态和T6态的应力应变曲线](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d94b3116-2f17-4775-bca5-f148234a20dd/resource) (`d94b3116-2f17-4775-bca5-f148234a20dd`)
- S4: [选区激光熔化成形（Al2O3+SiC）颗粒混杂增强铝基复合材料的数值模拟与组织性能研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0aefcb7f-88dd-4aac-8d1a-cbda498dc667/resource) (`0aefcb7f-88dd-4aac-8d1a-cbda498dc667`)
- S52: [表5-2 不同激光扫描速率下SLM成形(Al₂O₃+SiC)颗粒混杂增强AMCs铝基复合材料力学性能数值](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/eb40b855-0d37-4e8a-9f2e-c0f488795d61/resource) (`eb40b855-0d37-4e8a-9f2e-c0f488795d61`)