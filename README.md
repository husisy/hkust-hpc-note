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

## 配置conda环境

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

配置jupyter lab password

1. see [link](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)
2. 执行命令`jupyter notebook --generate-config`
3. 执行命令`jupyter notebook password`，然后创建新密码即可

## 配置ssh-R

修改`.ssh/config`文件，添加内容见下方代码块

1. 其中`HostName`中的ip可以通过在登录节点执行命令`ip a`获取
2. 配置成功后在登录节点执行`ssh login-node`可以实现「登录节点登录登录节点」，以此验证文件配置正确

`.ssh/config`

```txt
Host login-node
  HostName 192.168.2.254
  IdentityFile ~/.ssh/id_rsa
```

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

使用计算节点的bash

```bash
srun -p gpu-share -n1 --pty bash
```

module相关

```bash
module avail
module load xxx #replace xxx with what you want
```

gpu node

1. indirect login: ssh to `hpc3.ust.hk`, then use `ssh login-1`
2. direct login: ssh to `xgpu.ust.hk`, `xgpu` and `login-1` is the same node and it is for user to test some GPU program

### MWE01 sbatch

`my.script`

```bash
#!/bin/sh
#SBATCH --time=1
/bin/hostname
srun -l /bin/hostname
srun -l /bin/pwd
```

登录节点提交作业

```bash
sbatch -p cpu-share -n4 -o my.stdout my.script
```

### MWE02 访问计算节点的jupyter

恶意占用计算资源**绝对不是**超算中心提倡的行为，**请勿**恶意占用计算资源，**务必**遵守超算中心的使用条款

**警告**：如果你不清楚以下的每一条命令具体在做什么，请**不要**尝试slurm同时提交多个任务（即`--nodes=2 --ntasks=4`参数），存在端口冲突、文件冲突等问题，**甚至可能**会把你的用户文件、conda环境等弄坏，由此导致的后果概不负责

**务必**先完成上方「配置conda环境」和「配置ssh-R」，文件结构见下

```bash
~/hpc3-setup
├── UID/
│   ├── jupyter_lab.log
│   ├── ssh.log
│   └── ...
├── setup_jupyter.sh
├── stop_task.sh
└── ...
```

你需要进行如下操作

1. 创建`~/hpc3-setup`文件夹
2. 将当仓库的`setup_jupyter.sh`文件复制到登录节点`~/hpc3-setup/setup_jupyter.sh`
3. 将当仓库的`stop_task.sh`文件复制到登录节点`~/hpc3-setup/stop_task.sh`
4. 说明
   * `~/hpc3-setup/UID`是每次运行`setup_jupyter.sh`产生的日志文件，其中UID由时间以及进程ID组成，保证每次运行不冲突
   * `~/hpc3-setup/UID/jupyter_lab.log`是jupyter lab的运行日志，可用于调试
   * `~/hpc3-setup/UID/ssh.log`是ssh的运行日志，可用于调试
5. terminal-1 在登录节点的`~/hpc3-setup/`目录执行命令`srun -p cpu-share -n1 bash setup_jupyter.sh`
   * 说明：如果上述命令运行成功，jupyter lab已经在计算节点的`23333`端口运行，同时转发至登录节点的`23334`端口
   * 说明：执行该命令会使得当前terminal处于运行状态，所以下一步骤需要另一个terminal
   * 关于该命令的详细说明见该仓库`hpc3-setup/README.md`
   * 至此，你的vscode-remote已经可以访问登录节点的`23334`端口来访问jupyter
6. terminal-2 在你的电脑（本机）上执行 `ssh -L 127.0.0.1:23335:127.0.0.1:23334 USERNAME@hpc3.ust.hk`
   * 将上述的`USERNAME`替换为你的用户名
   * 说明：如果上述命令运行成功，登录节点的`23334`端口已转发至你电脑的`23335`端口
   * 至此，你可以在浏览器进入`127.0.0.1:23335`来访问jupyter
7. 结束任务
   * 方法1: 在terminal-1多次输入`ctrl-C`来强制中止
   * 方法2: `scancel xxx`, `xxx`为slurm的task ID
   * 方法3: 在jupyter的terminal中，切换至`~/hpc3-setup`目录，执行`bash stop_tash.sh`，执行之前**务必**保存所有jupyter内容，输出内容类似于下方代码块

```bash
$ srun -p gpu-share -n1 bash setup_jupyter.sh
[setup_jupyter.sh] jupyter and ssh-R is running
setup_jupyter.sh: line 16: 24198 Terminated              sleep 7d
[setup_jupyter.sh] goodbye
$
```

### MWE03 常用python库

配置conda环境见上文

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
