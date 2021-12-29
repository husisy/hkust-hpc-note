# HKUST HPC3

**WARNING** do NOT put sensitive data in this repo, this repo might be public in the future

这是**非官方**的超算使用指南

1. link
   * [homepage](https://itsc.hkust.edu.hk/services/academic-teaching-support/high-performance-computing/hpc3-cluster)
   * [faq](https://itsc.hkust.edu.hk/services/academic-teaching-support/high-performance-computing/hpc3-cluster/hpc3-cluster-faq)
   * [slurm-intro](https://itsc.hkust.edu.hk/services/academic-teaching-support/high-performance-computing/hpc3-cluster/jobs)
   * [slurm-tutorial](https://slurm.schedmd.com/tutorials.html)
2. 申请账号 [link](https://itsc.hkust.edu.hk/services/academic-teaching-support/high-performance-computing/hpc3-cluster/account)
   * 需要填写导师的ITSC账号
   * 提交申请后大约3天会收到邮件告知账后开通
3. ssh登录：命令行下执行`ssh USERNAME@hpc3.ust.hk`
   * 务必将`USERNAME`替换为**你的**用户名（即ITSC account），以下不再赘述
   * linux、mac的命令行自带ssh-client
   * win10需手动安装ssh-client：依次进入`settings`, `Apps`, `Apps & features`, `optional features`, `Add a feature`，然后选中`OpenSSh Client`，点击`install`即完成安装
   * （建议）配置公钥、私钥登录方式，配置`.ssh/config`文件，自行谷歌
   * （可选）vscode连接登录节点

slurm基本概念

1. link
   * [official site](https://www.schedmd.com/index.php)
   * [英文文档](https://slurm.schedmd.com/documentation.html)
   * [gitbook/中文文档](https://docs.slurm.cn/users/)
2. concept: node, partition, job, job step
3. `sinfo` 分区和节点的状态
   * partition：`cpu-share`, `gpu-share`, `himem-share`, 按照state分为多行显示
   * avail: `up`, `down`
   * state: `down*`表示节点无响应
   * nodelist
4. `squeue` 工作或工作步骤的状态
   * jobid
   * partition
   * name
   * user
   * ST: `R=Running`, `PD=Pending`
   * time
   * nodes
   * nodelist(reason)
   * `squeue --user=xxx`, `squeue -u=xxx`
5. `scontrol`
   * `scontrol show partition`
   * `scontrol show node hhnode-ib-146`
   * `scontrol show job`
6. `srun`
   * `srun --partition=xxx --nodes=3 --label /bin/hostname`, `srun -p xxx -N3 -l /bin/hostname`
   * `srun --partition=xxx --ntasks=3 --label /bin/hostname`

`HPC3`超算配置

1. `RTX2080`, `11GB`, `250W`

## minimum working example

### MWE00

查询partition状态

`sinfo`

查询作业状态

```bash
squeue
squeue --user=USERNAME #replace USERNAME with YOUR username
```

`srun`打印`hello world`

1. 单节点单进程 `srun -p cpu-share -n1 echo "hello world"`
2. 单节点多进程 `srun -p cpu-share --ntasks=4 --label echo "hello world"`
3. 多节点多进程 `srun -p cpu-share --nodes=2 --ntasks=4 --label echo "hello world"`
4. 多节点多进程打印host `srun -p cpu-share --nodes=2 --ntasks=4 --label /bin/hostname`

查询nvidia-smi

`srun -p gpu-share -n1 nvidia-smi`

module相关

```bash
module avail
module load xxx #replace xxx with what you want
```

### MWE01 sbatch

`my.script`

```bash
#!/bin/sh
#SBATCH --time=1
/bin/hostname
srun -l /bin/hostname
srun -l /bin/pwd
```

`sbatch -p cpu-share -n4 -o my.stdout my.script`

### MWE02 常用python库

**WARNING**集群配置了module，其中包含anaconda，也许那是更推荐的使用方式，以下仅为个人走通的方式

登录节点安装miniconda

1. 下载`miniconda`
   * 执行命令 `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
2. 安装 `bash Miniconda3-latest-Linux-x86_64.sh` 空格翻页，最后输入`yes`接受使用条款
3. 退出ssh登录再重新登录服务器方可生效
4. 命令行前面会出现`(base)`表示当前处于`base`环境
   * 强烈不建议使用`base`环境，因为`base`环境是conda用于管理自身的环境，一旦出现包兼容问题就只能重装conda，更建议创建新的环境，然后在新的环境中安装自己需要的包
   * （建议）执行`conda config --set auto_activate_base false`
5. 当你不再使用conda时，卸载conda：直接删除miniconda文件夹即可 `rm ~/miniconda3`
6. 其他
   * conda的更多使用说明见 [官方文档](https://docs.conda.io/en/latest/miniconda.html)，例如复制环境，升级包等
   * conda包列表搜索见 [链接](https://anaconda.org/)，在这个网站可以确认某个包是否有win/mac/linux版本等，以及查找某个包的版本等信息

创建`cuda113`环境

```bash
conda create -y -n cuda113
conda install -y -n cuda113 -c conda-forge cudatoolkit=11.3
conda install -y -n cuda113 -c pytorch pytorch torchvision torchaudio
conda install -y -n cuda113 -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum cupy nccl
```

文件结构

```bash
.
├── my.script
└── draft00.py
```

`my.script`

```bash
#!/bin/sh
. "/home/$USER/miniconda3/etc/profile.d/conda.sh"
conda activate cuda113
python draft00.py
```

`draft00.py`

```Python
import cupy as cp
assert cp.cuda.is_available()
cp0 = cp.array([1,2,3])
cp1 = cp.array([1,2,3])
print(cp0 + cp1)
```

1. 提交作业 `sbatch --partition=gpu-share --ntasks=1 -o my.stdout my.script`
2. （大约稍等10秒）查看输出结果 `cat my.stdout`

## The Recipe of How to Running Bash on Clusters
***
Two commends

```sh
 salloc -p gpu-share -N1 -n1 --gres=gpu:1 
```

- This one can help you to access the computing resource.
- After your input it, the system will grant you a jobid. COPY IT!
- It might take a while, if resources in short supply.
- More information about arguments(like # of node, # of gpu, etc) can be find in 'salloc -h' 

Now, you have a jobid, say it is 12345

```sh
srun --jobid=12345 --pty bash
```

After running it, you will find now your bash are in other node, and you can do whatever you want

e.g.
```sh
(base) [someone@hhnode-ib-145 test]$ conda activate some_env 
```

BTW, remember kill the bash by using scancel when you don't need it anymore.

```sh
scancel 12345
```


## TODO

1. [ ] mpi
2. [ ] pytorch-distributed
3. [ ] tensorflow
4. [ ] tensorflow-distributed
5. [ ] English version README

## contribution

欢迎贡献更多使用示例
