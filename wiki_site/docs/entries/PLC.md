---
version: "v1"
generated_at: "2026-06-18T07:35:17+00:00"
confidence_score: 0.86
confidence_level: "very_high"
confidence_basis:
  cited_sources: 42
  source_quality_score: 0.88
  freshness_score: 0.77
  evidence_coverage_score: 1.0
---

## 概述

在压铸与真空低压铸造领域，可编程序控制器（PLC）是冷室压铸机、低压铸造机的核心控制部件，整机动作执行、工艺参数调整、生产数据计算全部由其实现。相比传统继电器顺序控制系统，采用PLC的控制系统线路大幅简化，运行稳定可靠、故障率低，占用空间小，安装维护便捷[[S43,S9]]。

## 定义

依据1987年国际电工委员会（IEC）颁布的国际标准，PLC是一种专为工业恶劣环境设计的数字运算操作电子系统，采用可编程存储器存储逻辑运算、顺序控制、定时、计数、算术运算等指令，通过数字量、模拟量输入输出接口直接控制压铸类机械设备和铸造全生产流程[[S6,S37]]。

在压铸行业语境下，“PLC”与“PLC控制器”为通用称谓，当前行业公开资料中未检索到压铸行业完全专属的定制化专用PLC产品，压铸与真空低压铸造场景的控制需求均通过通用工业PLC产品结合压铸设备厂商定制的专属控制程序实现匹配[[S29]]。

## 基本工作循环

PLC在压铸场景下的工作循环分为三个核心阶段[[S11,S45]]：

1. **输入扫描阶段**：顺序读取压铸机所有位置传感器、操作按钮、安全门行程开关的状态，存入输入映像寄存器。
2. **程序执行阶段**：从上到下、从左到右扫描对应压铸动作逻辑的梯形图，对输入状态完成逻辑运算，实现锁模、射料、保压等动作的时序判断。
3. **输出刷新阶段**：将运算完成的控制信号输出到接口电路，驱动压铸机对应执行元件动作。

CPU采用循环扫描的工作方式，从第一条用户程序开始到程序结束完成一次扫描，每扫描1次用户程序就执行1次[[S45]]。

## 在压铸系统中的过程角色

### 压铸机时序控制与安全联锁

PLC已在现代压铸机中大范围替代继电器和顺序控制器作为核心控制单元，可支持10个以上甚至近20个压射速度设定点、10个以上压力设定点的任意压射模式自定义[[S36]]。射料触发必须满足前/后安全门关闭、模具锁紧、射嘴扣合等前置条件；程序采用多工步调度运行架构，对输入信号做锁存/解锁处理避免误触发，检测到工序异常时立即中断运行跳转错误处理流程，记录错误代码，仅当维护人员完成故障核验后才可清除错误标志恢复生产[[S49,S20,S25]]。

### 压射过程闭环控制

压射过程的闭环纠偏最快可在1个生产循环内完成，压射速度控制精度可达2%，活塞储能器压力波动可控制在±1%以内[[S36]]。PLC可永久存储不同模具的专属工艺参数，支持HMI显示慢压射速度、快压射速度、压射延迟时间等实时参数，并对接上位机完成压射全周期的压力、位移、速度数据记录，为压射性能优化、铸件质量预测模型搭建提供基础数据支撑[[S49,S36]]。

### 真空低压铸造压力闭环控制

现代低压铸造机普遍采用压力传感器+PLC实现充型全过程闭环控制，可对升液、充型、增压、保压、卸压全工序的气压参数完成无极调节，实现低紊流平稳充型[[S39]]。典型控制系统采用模糊PID算法，基于给定压力随时间变化的设定值和铸造罐内实际压力反馈，动态调节电磁阀与数字组合阀的通断状态，实现充型过程金属液面上升速度的精准控制，获得层流充型效果[[S47,S28]]。

铝合金发动机缸盖低压铸造智能PLC控制系统还集成温度闭环控制、安全联锁检测功能，未满足工艺条件时自动触发报警，保障生产安全[[S42,S50]]。

### 辅机协调调度

PLC将压铸主机与给汤机、喷涂机器人、取出机等周边辅机纳入统一时序调度架构，通过工步完成信号的交互实现全流程联动，支持手动单步操作、单循环半自动运行、全自动连续生产三种运行模式的无缝切换[[S20,S41]]。

## 常用型号与配置实例

### 欧姆龙CQM1系列

早期卧式冷室压铸机自动化改造普遍采用欧姆龙CQM1系列PLC作为控制核心。以力劲DCC280卧式冷室压铸机为例，典型配置为：电源模块1块、CPU模块1块、输入模块4块、晶体管输出模块2块、继电器输出模块1块，可覆盖锁开型、顶出、抽芯、射料全流程的信号采集与动作控制需求[[S5]]。该系列PLC可在接入编程器后切换为编程、监视、运行三种操作模式，分别用于程序修改、在线调试、正常生产控制[[S45]]。

### 西门子S7-200 SMART

西门子S7-200 SMART PLC是真空低压铸造场景的主流适配型号，可扩展模拟量输入模块EM AE04、EM AR02、数字量扩展模块EM QT16，支持PPI自由通信协议，可外接ADAM2520通信模块通过RS232接口与上位机实现数据交互，满足模糊PID压力闭环控制的运算需求。其模拟量转换的数值范围为-27648~27648，适配压力、温度类工业传感器的信号处理[[S47,S22]]。

### 西门子S7-1200系列

西门子S7-1200系列1214C DC/DC/DC型号PLC适配压铸类设备控制需求，支持TCP/IP、PROFINET、Modbus TCP、RS485/RS232等主流工业通信协议，可灵活扩展数字量与模拟量I/O端口，支持IEC 61131-3标准下的梯形图、功能块图、结构化文本等多种编程语言[[S15]]。

### 西门子Simatic S5系列

西门子Simatic S5系列PLC曾被广泛用于汽车行业自动化压铸单元的整体控制，可配合上位机PC模块实现压射过程12项关键参数的每秒千次采样，完成压射速度、增压时间、充型时长等数据的实时监控与超差报警，适配高精密压铸的质量追溯需求[[S24]]。

### 国产D20型PLC

国产工业PLC型号D20可用于压铸周边设备的控制，其主要技术参数如下表所示[[S12]]：

| 参数项 | 数值/说明 |
|---|---|
| I/O总点数 | 20点（直流输入12点，继电器输出8点） |
| 扫描周期 | ≤20ms/千开关符 |
| 工作温度 | -5℃~+40℃ |
| 抗振动等级 | 10~55Hz，振幅0.075mm |
| 冲击耐受 | 15g，持续11ms |
| 污染等级 | 3 |
| 防护等级 | IP2X |
| 输入隔离方式 | 光电耦合 |
| 输出隔离方式 | 继电器隔离 |
| 输出容量 | AC220V/2A，DC24V/2A（阻性负载） |

## 关键参数与检测要求

根据GB/T 37365-2019《压铸单元-性能检测方法》，压铸单元配套PLC的性能检测必检项目包含以下六个维度[[S8]]：

| 检测项目 | 说明 |
|---|---|
| 扫描速度 | 反映CPU执行用户程序的速度 |
| 用户程序存储容量 | 决定可存储的控制程序规模 |
| 数字I/O实际点数与可扩展点数 | 决定可接入的数字量信号规模 |
| 模拟量I/O实际点数与可扩展点数 | 决定可接入的模拟量信号规模 |
| 通讯功能 | 有无通讯模块、通讯接口类型、是否能扩展 |
| 特殊功能模块 | 有无、数量、是否能扩展 |

## 结构组成与信号交互

PLC的硬件结构主要由中央处理器单元（CPU）、存储器（RAM和ROM）、输入输出接口电路、总线单元和电源单元等组成[[S45,S6]]。

### 与执行器/传感器的信号交互架构

PLC与压铸专属传感、执行部件的信号交互架构如下[[S18,S47]]：

- **模拟量输入**：通过模拟量输入模块连接压力传感器、位移传感器，将4~20mA检测信号转换为可处理的数字量。在典型西门子S7-200 SMART架构下，2个绝压传感器可直接采集上下铸罐压力，1个表压传感器可采集储气罐压力，实现全气路状态实时感知。
- **数字量输出**：通过数字量输出接口直接驱动电磁阀，继电器输出型PLC可直接驱动压铸系统电磁阀、报警装置，单点点位可承载2A电阻性负载。
- **模拟量输出**：向电液比例阀/比例伺服阀输出控制信号，实现合模、压射、增压等各工序的压力、流量连续可调。

PLC还可通过PPI自由通信协议搭配ADAM2520通信模块，直接对接HMI、SCADA上位机，每秒向上位机同步运行与采样数据，同时主动监测通信链路状态，通信超时自动跳转异常处理流程避免事故；还可对接伺服驱动器、过程监测系统，接入红外测温等外部监测信号，触发自动喷淋调节等响应动作[[S20,S40]]。

### 抗干扰与接口防护

针对铸造车间多粉尘、电磁干扰强的恶劣工况，压铸配套PLC的输入输出接口普遍采用光电耦合器设计，抗干扰能力强，可直接适配压铸机各类限位开关、接近开关、比例阀、压力传感器等现场器件[[S45]]。

压铸工况下PLC基础抗干扰供电方案如下表所示[[S9,S7,S3]]：

| 供电项目 | 配置要求 |
|---|---|
| 供电系统 | 三相五线制AC380V 50Hz，N为零线，PE为保护接地 |
| 控制电源（推荐方案） | 功率400~500VA隔离变压器降压至AC220V |
| 直流稳压器 | 输入AC220V，输出DC24V，功率≥320W |
| 接地保护 | 所有电压>50V的电气箱体接独立接地导线，接地电阻≤0.1Ω |

压铸机配套PLC的供电统一采用DC24V，由主控制柜内AC220V输入的稳压电源统一供给[[S43]]。PLC配套控制柜的防护等级需符合GB 4208（等效IEC 529）的IP代码规范，铸造车间常规选型为IP55等级，可阻挡铸造粉尘堆积、抵御低压喷水，适配压铸现场高粉尘、可能存在冷却液喷溅的工况环境[[S34,S48]]。

## 标准与规范

### 编程语言标准

压铸配套PLC的国际标准体系遵循IEC 61131系列规范，其中IEC 61131-3规定了5类标准化编程语言：梯形图（LD）、功能块图（FBD）、指令表（IL）、结构化文本（ST）、顺序功能图（SFC），广泛应用于压铸控制系统的程序开发[[S37,S30]]。

### 产品与安全标准

国内压铸领域PLC相关合规要求明确[[S8,S16,S27]]：

| 标准编号 | 适用范围 |
|---|---|
| GB/T 15969.1-2007、GB/T 15969.2-2008 | PLC产品本体性能（对应IEC 61131系列国内转化标准） |
| GB/T 20906-2007 | 压铸单元安全技术要求 |
| GB/T 24391-2009 | 低压铸造机安全要求 |
| GB 5226.1-2002 | 机械电气设备通用技术条件（对应IEC 60204-1） |
| GB/T 37365-2019 | 压铸单元性能检测方法 |

### 压铸专属安全规范

根据GB 20906《压铸单元安全技术要求》，当PLC控制系统出现损害安全功能的故障且不会引发意外起动时，系统必须具备故障自识别能力，自动触发联锁机制阻断危险运动。同时压铸机电气系统强制要求通过1500V/1min耐压试验，绝缘电阻不大于1MΩ，连续接地电阻不大于0.1Ω[[S33,S3]]。

## 局限性与注意事项

### 扫描周期限制

PLC CPU采用循环扫描的工作方式。普通PLC在压铸高速高压工况下扫描周期超过20ms时，无法匹配10m/s级超高压射19ms的加速响应要求，将导致压射速度/压力切换点偏移，引发铸件气孔、充型不足缺陷[[S9,S45]]。

### 电磁干扰防护

开关量输入输出接口必须内置光电耦合器，实现强电信号与PLC内部弱电控制回路的电气隔离，大幅提升高振动、强电磁干扰压铸车间环境下的信号可靠性[[S45,S21]]。针对压铸车间强电磁干扰环境，采用厚度≥1.0mm的锌合金压铸壳体封装PLC控制单元，即可实现40~57dB以上的电磁屏蔽效率[[S14,S31]]。

### 程序与安全联锁可靠性

对压铸安全联锁、高压射控制等安全等级要求极高的场景，需采用FSC级多重冗余PLC系统，人为提升组态修改的操作门槛，必须停止全系统并同步所有冗余模块的版本后方可修改控制逻辑，避免非授权误改控制程序引发安全事故[[S32,S19]]。

### 典型故障模式

压铸场景下PLC典型故障可通过面板指示灯直接判断[[S1,S35]]：

- **BAT亮红灯**：电池完全失效，内部RAM中存储的压铸工艺程序存在丢失风险。
- **BAT亮黄灯**：电池电量不足，需及时更换。
- **RUN绿灯熄灭**：CPU工作异常。
- 当压铸机出现无总压故障且液压回路无异常时，需优先检查PLC起压信号的输出状态，排查PLC无输出类故障。

## 图示

### 压铸实验台PLC压射参数采集记录系统

该图展示ADC12铝合金真空压铸实验的压射参数记录系统，左侧为力劲集团DCC630M卧式冷室压铸机配套的PLC控制柜，右侧屏幕展示由该PLC系统采集存储的压铸充型全流程工艺参数表格，直观呈现PLC作为压射实验台控制核心完成数据采集存储功能的实际应用场景[[S46]]。

![真空压铸实验台的PLC压射参数采集记录系统](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f21ab859-713a-4dbf-b7b5-948dd6309ccd/resource)

### 压铸机PLC控制中心典型操作界面

该图展示压铸试验配套的PLC控制中心操作界面，包含模具控温、工艺温度监控、工艺流程监控三个功能入口，还设置了等级切换与密码输入区、重要参数设定、系统参数设定操作按钮，直观呈现压铸场景下PLC配套HMI系统的典型操作逻辑[[S23]]。

![压铸机PLC控制中心典型操作界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71b2c46f-6c93-4a6b-98d3-da7895f92202/resource)

## Sources
- S43: [压铸生产培训教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d4b76c90-5139-47e8-a096-d9984dd5b36c/resource) (`d4b76c90-5139-47e8-a096-d9984dd5b36c`)
- S9: [TextNode28](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2480ec2b-006b-4f02-b2a0-e526fe309085/resource) (`2480ec2b-006b-4f02-b2a0-e526fe309085`)
- S6: [国防科工委十五规划教材材料加工工艺过程的检测与控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10daad05-bb86-4076-b3b7-1ceac85ec157/resource) (`10daad05-bb86-4076-b3b7-1ceac85ec157`)
- S37: [84414_可编程逻辑控制器](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/a23220b1-7410-4fa6-b73f-72cbff4090ec/resource) (`a23220b1-7410-4fa6-b73f-72cbff4090ec`)
- S29: [压铸模设计手册 软件版](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8e48eb00-a819-4869-a38e-010241021c60/resource) (`8e48eb00-a819-4869-a38e-010241021c60`)
- S11: [国防科工委十五规划教材材料加工工艺过程的检测与控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/2dc0d66b-bdbe-4569-b2e7-026cd9dadf03/resource) (`2dc0d66b-bdbe-4569-b2e7-026cd9dadf03`)
- S45: [TextNode29](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/e8598a6f-bf66-49df-8667-15b4ff16e145/resource) (`e8598a6f-bf66-49df-8667-15b4ff16e145`)
- S36: [压铸技术与生产](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9f429109-75c2-4ed8-b92f-c4bdf609dbf6/resource) (`9f429109-75c2-4ed8-b92f-c4bdf609dbf6`)
- S49: [TextNode185](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/fc3db1c3-2077-4937-889b-6225903fdf9b/resource) (`fc3db1c3-2077-4937-889b-6225903fdf9b`)
- S20: [TextNode186](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6a1d7387-fa3d-4dc4-b565-c275dd2cfd14/resource) (`6a1d7387-fa3d-4dc4-b565-c275dd2cfd14`)
- S25: [TextNode184](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/7dbeb513-2786-4ae3-9c0c-4ed13333686a/resource) (`7dbeb513-2786-4ae3-9c0c-4ed13333686a`)
- S39: [casting copper base alloys__d5182d5c2c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/bf975e8f-f4f6-4fb5-8f26-afdf131c11c0/resource) (`bf975e8f-f4f6-4fb5-8f26-afdf131c11c0`)
- S47: [机械振动对真空低压铸造ZL114A微观组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f386c23d-c8ca-4f63-b178-9b80fd88f532/resource) (`f386c23d-c8ca-4f63-b178-9b80fd88f532`)
- S28: [机械振动对真空低压铸造ZL114A微观组织及力学性能的影响](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/8ccb320d-52eb-40a7-9d7e-3580882d809c/resource) (`8ccb320d-52eb-40a7-9d7e-3580882d809c`)
- S42: [轻合金半固态成形技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/d0ca2b92-f505-4200-a632-53b7406fa1ee/resource) (`d0ca2b92-f505-4200-a632-53b7406fa1ee`)
- S50: [基于PLC发动机缸盖低压铸造成型的智能控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/ffcc26d0-cefc-46d0-ad3e-069a612bbb58/resource) (`ffcc26d0-cefc-46d0-ad3e-069a612bbb58`)
- S41: [development of the cold chamber pressure die casting machine__da0bfa0647](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/cf3556d3-574e-4e59-b366-095d37a0a290/resource) (`cf3556d3-574e-4e59-b366-095d37a0a290`)
- S5: [卧式冷室压铸机技术教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/10d83d31-9e08-4533-97de-ae47bb392053/resource) (`10d83d31-9e08-4533-97de-ae47bb392053`)
- S22: [铝合金管材半连续铸造工艺稳定性控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6f99eaca-872d-404c-a953-0bfcf7d8fd8e/resource) (`6f99eaca-872d-404c-a953-0bfcf7d8fd8e`)
- S15: [工业级砂型打印机墨滴喷射仿真与供墨系统优化研究](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/3fc70157-c591-4d75-82ca-4d9ae95dee51/resource) (`3fc70157-c591-4d75-82ca-4d9ae95dee51`)
- S24: [cim and control of pressure die casting in the automotive industry__4d2d9d451d](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/771caf84-eff7-4e04-ae70-65af376388c6/resource) (`771caf84-eff7-4e04-ae70-65af376388c6`)
- S12: [机械产品目录 1996 第5册 金属切削机床、机床附件、机床电器、锻压机械、铸造机械、木工机械](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/358bcf79-e86a-48df-b3d4-24e4adb2da42/resource) (`358bcf79-e86a-48df-b3d4-24e4adb2da42`)
- S8: [GBT+37365（压铸单元-性能检测方法）-2019.pdf-6deb6160-73d6-4c2e-8d16-cbe072540d5b](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/1c6246fe-5a31-42ba-8c3b-763ac13069ab/resource) (`1c6246fe-5a31-42ba-8c3b-763ac13069ab`)
- S18: [特种铸造工学基础](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/61026198-5a23-4651-aced-323d19c582de/resource) (`61026198-5a23-4651-aced-323d19c582de`)
- S40: [大型压铸模是实现一体化压铸的关键技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/c5c9e282-d626-481d-a616-c5332dd4250b/resource) (`c5c9e282-d626-481d-a616-c5332dd4250b`)
- S7: [TextNode27](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/173947da-8f4c-48c5-ae1d-e7bf0e9cf960/resource) (`173947da-8f4c-48c5-ae1d-e7bf0e9cf960`)
- S3: [压铸实用技术](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/07802100-e1ac-4638-9729-73958f198c34/resource) (`07802100-e1ac-4638-9729-73958f198c34`)
- S34: [箱式变电站标准工程图纸集粹设计加工安装材料造价](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9bc8540b-929a-4f57-82cf-8f7b115fd8b8/resource) (`9bc8540b-929a-4f57-82cf-8f7b115fd8b8`)
- S48: [箱式变电站标准工程图纸集粹设计加工安装材料造价](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f9c833a4-adc7-4df6-952b-259627e6b117/resource) (`f9c833a4-adc7-4df6-952b-259627e6b117`)
- S30: [abstract state machines alloy b vdm and z third international conference__3efe2aa57c](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/928d8363-50fe-485f-b824-628f14b4c99f/resource) (`928d8363-50fe-485f-b824-628f14b4c99f`)
- S16: [GB+20906（压铸单元安全技术要求）-2007.pdf-42830308-040b-4641-b26a-8aabe6de1e87](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/56e3df01-060b-44d3-a080-6983b8858c5d/resource) (`56e3df01-060b-44d3-a080-6983b8858c5d`)
- S27: [GB+24391（低压铸造机-安全要求）-2009.pdf-e6b67b23-6077-467d-b3e0-d7937ccdb816](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/89aaa1e4-b4a1-48e1-9dce-12a3140d8030/resource) (`89aaa1e4-b4a1-48e1-9dce-12a3140d8030`)
- S33: [GB+20906（压铸单元安全技术要求）-2007.pdf-42830308-040b-4641-b26a-8aabe6de1e87](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/97e1c3f6-e157-4c51-bb85-319bfe83a630/resource) (`97e1c3f6-e157-4c51-bb85-319bfe83a630`)
- S21: [国防科工委十五规划教材材料加工工艺过程的检测与控制](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/6d99d980-19f9-48bd-9dda-5f0f6b9654b6/resource) (`6d99d980-19f9-48bd-9dda-5f0f6b9654b6`)
- S14: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/393d0709-0ce2-4975-9b85-4ff09c52aa8a/resource) (`393d0709-0ce2-4975-9b85-4ff09c52aa8a`)
- S31: [第二届中国国际压铸会议论文集](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/93c239c7-2e85-40e5-a6d5-253a6de04abf/resource) (`93c239c7-2e85-40e5-a6d5-253a6de04abf`)
- S32: [大话自动化从蒸汽机到人工智能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/95cbc060-80b4-439f-ab68-337a390dc9d9/resource) (`95cbc060-80b4-439f-ab68-337a390dc9d9`)
- S19: [大话自动化从蒸汽机到人工智能](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/63029dbb-1733-4543-ad47-36f33f356684/resource) (`63029dbb-1733-4543-ad47-36f33f356684`)
- S1: [卧式冷室压铸机技术教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/0130de31-9828-4914-a6ee-c40a6b0ae37a/resource) (`0130de31-9828-4914-a6ee-c40a6b0ae37a`)
- S35: [卧式冷室压铸机技术教程](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/9ddd7a3c-dc26-4da8-9cd4-486728cb7758/resource) (`9ddd7a3c-dc26-4da8-9cd4-486728cb7758`)
- S46: [图2.4 压射过程参数记录系统](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/f21ab859-713a-4dbf-b7b5-948dd6309ccd/resource) (`f21ab859-713a-4dbf-b7b5-948dd6309ccd`)
- S23: [图2.6 控制中心界面](http://192.168.150.150:8000/api/v1/workspaces/die_casting_wiki_v2/document-elements/71b2c46f-6c93-4a6b-98d3-da7895f92202/resource) (`71b2c46f-6c93-4a6b-98d3-da7895f92202`)