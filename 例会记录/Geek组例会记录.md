# Geek组例会记录（2021.11.7）



## 星座的话题

* 对人类求交集
* 心理学效应

## ROS系统核心



### 1. 机器人开发的问题节点

控制驱动

节点通讯

测试仿真

......

### 2. 什么是ROS？

* 集成的机器人开发系统
* 开源项目
* 简化了中间的过程（封装）
* 线上仿真，
* The Robot Operating System (ROS) is **a set of software libraries and tools that help you build robot applications**.
* From drivers to state-of-the-art algorithms, and with powerful developer tools, ROS has what you need for your next robotics project. And **it's all open source.**
* 

[detail](https://www.ros.org/)     [wiki](http://wiki.ros.org/cn)

### 3. 特点

* 分布式系统实现的多编程语言编程
* 中间环节封装，简化开发过程
* 

### 4. 机器人开发的分层式结构

* 单机器人
  * Application
  * Middleware
  * OS
  * ROS1
  * ROS2
* 多机器人
  * OS
    * process system(ubuntu)
  * Driving
  * Hardware
  * Control center(Linux)
    * server
    * WiFi connection
* 分层
  * 社区层（知识分享）
  * 计算图层（处理数据的网络）
  * 文件系统层（存储区上的源代码）
  * 命名层（名字节点）
* 计算图层
  * 概念
    * 松耦合
      * 松耦合系统通常是基于消息的系统，此时客户端和远程服务并不知道对方是如何实现的。 客户端和服务之间的通讯由消息的架构支配。 **只要消息符合协商的架构，则客户端或服务的实现就可以根据需要进行更改，而不必担心会破坏对方。**
    * （另：）紧耦合
      * 紧耦合就是**模块或者系统之间关系太紧密，存在相互调用**。 紧耦合系统的缺点在于==更新一个模块的结果导致其它模块的结果变化，难以重用特定的关联模块。==
    * 进程
      * 进程（Process）是计算机中的程序关于某数据集合上的一次运行活动，是**系统进行资源分配和调度的基本单位，是操作系统结构的基础。**
      * 线程
        * **线程**（英语：thread）是[操作系统](https://zh.wikipedia.org/wiki/操作系统)能够进行运算[调度](https://zh.wikipedia.org/wiki/调度)的最小单位。
    * 分布式系统

### 5. ROS消息通信机制

#### 概念

* 节点
  * master
    * Master节点是集群的控制节点，负责整个集群的管理和控制。
    * 针对集群执行的控制命令都是发送给Master节点的。 
    * 因为Master节点如此重要，所以Master节点默认是不执行工作负载的。
  * node
    * 在ROS内理解为进程
* 消息
  * ROS内为数据结构（堆/栈/队列/......）

#### 话题通信

* 异步
  * 接收者可以进行其他动作
* 单向
  * 单向的消息传递
* 连续

#### 服务通信

* 客户端与服务器之间的==同步双向==服务消息通讯

#### 动作通信

* 异步
* 双向<!--相互的信息传递-->

#### 通信过程

* 概念
  * RPC（远程过程调用）
    * RPC是一种服务器-客户端（Client/Server）模式
    * 经典实现是一个通过**发送请求-接受回应**进行信息交互的系统。
    * RPC是一种[进程间通信](https://zh.wikipedia.org/wiki/进程间通信)的模式，程序分布在不同的[地址空间](https://zh.wikipedia.org/wiki/地址空间)里。
    * 如果在同一主机里，RPC可以通过不同的虚拟地址空间（即便使用相同的物理地址）进行通讯，而在不同的主机间，则通过不同的物理地址进行交互。
    * 许多技术（通常是不兼容）都是基于这种概念而实现的。
  * IP
    * **网际协议**（英语：Internet Protocol，缩写：**IP**），又称**互联网协议**，是用于[分组交换](https://zh.wikipedia.org/wiki/封包交換)数据网络的协议。
    * IP是在[TCP/IP协议族](https://zh.wikipedia.org/wiki/TCP/IP协议族)中[网络层](https://zh.wikipedia.org/wiki/网络层)的主要协议，任务仅仅是根据源主机和目的主机的地址来传送数据。为此目的，IP定义了寻址方法和数据报的封装结构。第一个架构的主要版本为[IPv4](https://zh.wikipedia.org/wiki/IPv4)，目前仍然是广泛使用的互联网协议，尽管世界各地正在积极部署[IPv6](https://zh.wikipedia.org/wiki/IPv6)。
  * TCP
    * 传输控制协议（TCP，Transmission Control Protocol）是一种面向连接的、可靠的、基于字节流的传输层通信协议
  * XML
    * 可扩展性标记语言
  * XML-RPC
    * 远程过程调用协议
    * 通过XML编码
* 建立连接

