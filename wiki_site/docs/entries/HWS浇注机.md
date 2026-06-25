---
version: "v1"
generated_at: "2026-06-18T19:01:55+00:00"
confidence_score: 0.87
confidence_level: "very_high"
confidence_basis:
  cited_sources: 15
  source_quality_score: 0.9
  freshness_score: 0.74
  evidence_coverage_score: 1.0
---

## 概述

HWS浇注机是指由德国Heinrich Wagner Sinto（海因里希·瓦格纳·新东）公司提供的配套静压造型线使用的高端自动浇注设备，通常与HWS公司设计制造的多功能静压造型线集成部署于砂型铸造车间[[S13,S20]]。根据GB/T 25370-2020《铸造机械 术语》的分类体系，该设备属于“自动浇注机（automatic pouring machine；automatic pouring device）”范畴，即“按照设定工艺，自动完成浇注过程的浇注机”，并进一步归属于配套静压砂型造型线使用的专用集成型自动浇注装置，整合了高精度随动定量与稳定温控功能[[S23,S16]]。

HWS全称为Heinrich Wagner Sino，系德国老牌造型设备厂商与日本新东（Sinto）共同成立的合资企业，面向全球铸造行业供应与静压造型线配套的高端自动浇注系统[[S13]]。目前公开铸造专业文献中尚未收录该设备在中文行业内的通用别名或本土化俗称[[S13]]。

## 工艺定位与适用场景

HWS自动浇注机核心适配的工艺场景为**砂型铸造**，可兼容铸铁件和铸铝件的连续自动化浇注生产。其显著特点之一是能够部署于支持两种不同高度砂箱的复合型静压造型线上，实现不同材质铸件的并行柔性生产[[S13,S25]]。

在HWS多功能静压造型线中，浇注机的典型部署位置与工艺衔接关系如下：造型主机造好的砂型经翻转机翻转、铣浇口机铣出浇口杯后进入合箱机合型；生产铸铁件时，合型后的砂型在铸工带A段由铸铁件浇注机完成浇注，随后经过渡小车运送到铸铁专用冷却段进行冷却；生产铸铝件时，合型后的砂型仅通过铸工带A段不浇注，由过渡小车运送到铸铝件专用浇注冷却段进行浇注和冷却[[S25]]。两种材质的铸件通过不同落砂通道落砂，旧砂分别返回各自独立的型砂制备中心[[S25]]。

## 设备结构与组成

根据GB/T 25370-2020的术语定义，自动浇注机的核心构成涵盖以下关键子系统[[S23]]：

| 子系统/部件 | 功能说明 |
|-------------|----------|
| 浇注机本体 | 按照工艺要求将金属液定量注入铸型的机器或装置 |
| 称重机构 | 用于称量浇包内金属液重量的机构 |
| 塞杆及塞杆启闭机构 | 用于堵住浇注口、控制金属液流动的耐火材质杆状部件及其升降控制装置 |
| 浇包自动更换系统 | 将盛有金属液的浇包送入浇注机换包位置，并将空包退回的整套装置 |
| 同步浇注装置 | 与造型线同步移动，在运动中完成浇注并于浇注完成后自动返回原位的成套装置 |

HWS浇注机配套的HSP系列静压造型机整体平面布局包含电机、传动机构及砂箱等核心部件[[S8]]。

![HWS HSP型静压造型机整体平面结构布局图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3db57b7e-d2ae-4096-a8c5-658d740f0991/resource)

历史文献中亦保留有与HWS类设备一致的高压造型线自动浇注装置实物示意图[[S20]]。

![HWS类自动浇注装置配套高压砂型造型线部署示意图](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90032a26-6b93-42e1-9d8d-b8d25680a4e3/resource)

## 控制逻辑与操作流程

基于PLC控制的自动浇注类设备通用操作流程分为**手动模式调试**与**自动模式连续运行**两大阶段，该控制逻辑与HWS自动浇注机兼容[[S6]]：

- **手动模式**：切换操作开关后分别单独测试手臂移动、注料、取料等独立动作，确认各执行机构无异常。
- **自动模式**：完成初始取料后，循环执行舀取金属液→滴料定重→移动对准浇口→注料→返回待机的全自动工序。

## 故障分类与维护体系

铸造自动浇注类设备故障按来源可分为三大类[[S2]]：

| 故障类别 | 细分项 |
|----------|--------|
| 控制系统故障 | 控制器本体故障、外围控制元件故障 |
| 机械本体故障 | 机构磨损、结构失效等 |
| 工艺相关故障 | 浇注参数偏差、金属液状态异常等 |

对应维护点检周期可划分为四个层级[[S19,S21]]：

| 维护周期 | 典型检查项目 |
|----------|-------------|
| 日检 | 压力表、安全门等运行状态检查 |
| 月检 | 缓冲机构、传动部件磨损检查 |
| 半年检 | 核心易损件更换、液压气动系统校验 |
| 年检 | 整机性能全面标定 |

> **说明**：上述故障分类与维护体系为铸造自动浇注类设备的通用框架，可适配HWS浇注机的维护管理。HWS品牌专属的原厂故障处理细则目前尚无法从公开权威来源确认[[S14]]。

## 安全与合规要求

HWS浇注机作为铸造车间内的自动浇注设备，需遵循相关中国国家标准中规定的安全要求。GB 24391-2009《低压铸造机 安全要求》给出了铸造浇注类设备的共性安全强制规范：液压系统安全应符合GB/T 3766，气动系统安全应符合GB/T 7932；浇注动作必须与合型及插芯机构联锁，只有当铸型完全合型及插芯到位时方可进行浇注；设备空运转等效连续声压级不得大于85 dB(A)[[S22,S1]]。GB 20906-2007《压铸单元安全技术要求》（修改采用EN 869:1998）引用了ISO 14120机械安全防护装置标准及ISO 13849系列安全控制系统标准，可作为自动浇注设备安全合规的补充参考[[S9]]。

在安全控制系统设计层面，自动浇注系统的安全功能需符合IEC 61508、IEC 61511定义的安全完整性等级（SIL）规范，通过设置独立的安全传感器、逻辑解算器、最终执行元件三层安全冗余结构，实现异常工况下自动进入安全停机状态的功能[[S18]]。

## Sources
- S13: [砂型铸造设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/65f2a18b-7e12-4d82-a5c7-b4ce86c80b98/resource) (`65f2a18b-7e12-4d82-a5c7-b4ce86c80b98`)
- S20: [铸铁高压造型线自动浇注装置](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/90032a26-6b93-42e1-9d8d-b8d25680a4e3/resource) (`90032a26-6b93-42e1-9d8d-b8d25680a4e3`)
- S23: [GBT+25370（铸造机械-术语）-2020.pdf-ceefffc7-3e72-4acd-b812-3277e391ef89](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/b59f3abc-8b82-486f-bc91-f7d5749aa728/resource) (`b59f3abc-8b82-486f-bc91-f7d5749aa728`)
- S16: [GBT+25370（铸造机械-术语）-2020.pdf-ceefffc7-3e72-4acd-b812-3277e391ef89](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/79aa69ea-6ff7-4680-8198-425880b34abe/resource) (`79aa69ea-6ff7-4680-8198-425880b34abe`)
- S25: [砂型铸造设备](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ef806618-12a4-4369-86eb-5916458b7ae4/resource) (`ef806618-12a4-4369-86eb-5916458b7ae4`)
- S8: [HWS公司静压造型机平面布置图（a）HSP造型机](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3db57b7e-d2ae-4096-a8c5-658d740f0991/resource) (`3db57b7e-d2ae-4096-a8c5-658d740f0991`)
- S6: [压铸生产培训教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/294a010a-c364-4b9f-9680-faf371494cb2/resource) (`294a010a-c364-4b9f-9680-faf371494cb2`)
- S2: [Equipment Fault Classification by Source](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/04f1f62f-babd-4702-9b1f-dc981edb02de/resource) (`04f1f62f-babd-4702-9b1f-dc981edb02de`)
- S19: [自动喷雾机保养内容及检修周期表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/87fa256d-a204-437f-b46a-07a93c999b58/resource) (`87fa256d-a204-437f-b46a-07a93c999b58`)
- S21: [附表B-1 DK7725型数控线切割机维护点检项目时间记录表](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a0e4833c-fe74-490d-aab7-8ce4515ce10b/resource) (`a0e4833c-fe74-490d-aab7-8ce4515ce10b`)
- S14: [engineering equipment for foundries proceedings of the seminar on engine__879d587d16](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6b606f0c-d8db-4848-8568-d317bc5bab3a/resource) (`6b606f0c-d8db-4848-8568-d317bc5bab3a`)
- S22: [GB+24391（低压铸造机-安全要求）-2009.pdf-e6b67b23-6077-467d-b3e0-d7937ccdb816](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ab465327-3866-413a-b44c-470a9f11b07a/resource) (`ab465327-3866-413a-b44c-470a9f11b07a`)
- S1: [GB+24391（低压铸造机-安全要求）-2009.pdf-e6b67b23-6077-467d-b3e0-d7937ccdb816](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/019097cd-cf5d-45c8-8584-3e76fdf6954d/resource) (`019097cd-cf5d-45c8-8584-3e76fdf6954d`)
- S9: [GB+20906（压铸单元安全技术要求）-2007.pdf-42830308-040b-4641-b26a-8aabe6de1e87](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56e3df01-060b-44d3-a080-6983b8858c5d/resource) (`56e3df01-060b-44d3-a080-6983b8858c5d`)
- S18: [control valve handbook__31ece27f09](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/86be92fa-773e-4dba-8be6-4ed240aa75fd/resource) (`86be92fa-773e-4dba-8be6-4ed240aa75fd`)