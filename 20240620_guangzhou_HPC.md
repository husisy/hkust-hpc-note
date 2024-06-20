# 20240620 GuangZhou HPC

中山大学 100 anniversary

国家超算广州中心 天河星逸

Chen Zhiguang

Yin Zhong

1. 天河二号 top500 六连冠
2. 天河星逸
   * 超算网络香港专线
3. “星光”超算应用平台 [link](https://starlight.nscc-gz.cn)
4. 应用社区
   * 高精度大气海洋数值预报应用社区：多过程跨模式跨网格耦合模式
   * 高端装备制造设计应用社区：流体计算仿真，汽车整体设计
   * 新材料设计社区：DFT，Matgen, CrystalNet [doi-link](https://dl.acm.org/doi/10.1145/3132747.3132759)
   * 大规模生物医药应用社区: drugVQA [doi-link](https://www.nature.com/articles/s42256-020-0152-y)
   * 超算教育实践平台建设
5. 典型应用
   * 地球科学
   * 海洋科学
   * 宇宙科学：Juno宇宙粒子探测
   * 生命科学
   * 航空航天：C919全机气动优化
6. 超算参数
   * p2p bandwidth: 400Gbps
   * p2p latency: 1.5us
   * double flops: 20PFlops
   * intel CPU node
   * intel GPU node: A800x8, 1TB memory (CPU)
   * FT CPU node信创
   * 三维蝶形网络拓扑
   * 上网代理
   * 在线可视化：paraview, ncview, FlowNL [doi-link](https://doi.org/10.1109/tvcg.2022.3209453)
   * 已购买部分商业软件：如Ansys
   * 任务提交：容器、slurm
   * vscode server
   * UDT客户端传输

国家超算广州中心南沙分中心简介

1. 网络专线
2. CPU: `64cores * 2000`
3. GPU: `A800 * 500`
4. 报价

## Case Study

Junxian He, CSE HKUST, Compression Represents Intelligence Linearly

1. [arxiv-link](https://arxiv.org/abs/2404.09937) Compression Represents Intelligence Linearly
2. compression leads to intelligence
3. how to encode text corpus with fewer bits in a lossless manner

## Get Started

1. 登录“星光”超算应用平台 [link](https://starlight.nscc-gz.cn)
2. 申请“星光”超算应用平台 [link](https://starlight.nscc-gz.cn)
3. 申请HPC账号并绑定
   * 在网页首页「可用集群」绑定
4. 使用指南：在网页首页「指南」查看指南
5. 登录节点：在网页首页「可用集群」点击“绑定的节点”

查询partition状态

```bash
yhinfo
```

查询作业状态

```bash
yhqueue
yhqueue --user=USERNAME #replace USERNAME with YOUR username
```

打印`hello world`

1. 单节点单进程 `yhrun -p ai -n1 echo "hello world"`
2. 单节点多进程 `yhrun -p ai --ntasks=4 --label echo "hello world"`
3. 多节点多进程 `yhrun -p ai --nodes=2 --ntasks=4 --label echo "hello world"`
4. 多节点多进程打印host `yhrun -p ai --nodes=2 --ntasks=4 --label /bin/hostname`

查询nvidia-smi

```bash
yhrun -p ai -n1 nvidia-smi
```

```text
Thu Jun 20 16:18:40 2024
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.12             Driver Version: 535.104.12   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A800 80GB PCIe          On  | 00000000:4F:00.0 Off |                    0 |
| N/A   31C    P0              43W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA A800 80GB PCIe          On  | 00000000:50:00.0 Off |                    0 |
| N/A   33C    P0              45W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   2  NVIDIA A800 80GB PCIe          On  | 00000000:53:00.0 Off |                    0 |
| N/A   33C    P0              46W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   3  NVIDIA A800 80GB PCIe          On  | 00000000:57:00.0 Off |                    0 |
| N/A   35C    P0              48W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   4  NVIDIA A800 80GB PCIe          On  | 00000000:9C:00.0 Off |                    0 |
| N/A   33C    P0              47W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   5  NVIDIA A800 80GB PCIe          On  | 00000000:9D:00.0 Off |                    0 |
| N/A   33C    P0              45W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   6  NVIDIA A800 80GB PCIe          On  | 00000000:A0:00.0 Off |                    0 |
| N/A   34C    P0              47W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
|   7  NVIDIA A800 80GB PCIe          On  | 00000000:A4:00.0 Off |                    0 |
| N/A   32C    P0              47W / 300W |      2MiB / 81920MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```
