# Sugon曙光智算

1. link
   * [official-site](https://ac.sugon.com/)
2. 注册：略
3. 使用：下载客户端，使用其中的命令行
4. 概念
   * partition: 可访问队列，在官网首页可查看，例如 `xahctest`，可通过 `sinfo` 查看
   * job-id: 作业id，例如 `4217048`，可通过 `squeue` 查看
   * job-name: 作业名称
   * module: 模块名称，例如 `compiler/intel/2017.5.239`, `Pytorch/1.10.0-hpcx-gcc-7.3.1`，可通过 `module avail` 查看
5. `job_example/`目录下包含

```bash
## replace the following <xxx> with the real value
module avail
module load <module>
module unload <module>
module list #list loaded module
module show <module>
module purge #unload all loaded modules
```

```bash
sinfo #list available partition
squeue #list running jobs
scontrol show job <job-id> #show job details
scancel <job-id> #cancel job
scontrol show partition <partition-name>

sbatch xxx.sh
salloc
sacct #show job history
```

```bash
#!/bin/bash
## replace the following <xxx> with the real value
##     <job-name>
##     <partition-name> : 可访问队列，可选 xahctest
#SBATCH -J <job-name>
#SBATCH -p <partition-name>
#SBATCH -N <number-of-node>
#SBATCH --ntasks-per-node=32

module purge
module load compiler/intel/2017.5.239 mpi/hpcx/2.4.1/intel-2017.5.239
module load apps/abinit/8.10.3/hpcx-2.4.1-intel2017
srun --mpi=pmix_v3 abinit < example.in
```

## Example00: srun hello world

```bash
srun -p xahctest -n1 pwd
# /work/home/acfu6a24vx
srun -p xahctest -n1 hostname
# c01r2n16
srun -p xahctest -n1 echo "hello world"
```

## Example01: sbatch hello world

`my.script`

```bash
#!/bin/sh
#SBATCH -J sbatch-hello-world
#SBATCH -p xahctest
#SBATCH -N 2
#SBATCH --ntasks-per-node=4
/bin/hostname
srun -l /bin/hostname
srun -l /bin/pwd
srun -l printenv | grep SLURM
```

PS: `-l` prepend task number to lines of stdout/err

登录节点提交作业

```bash
sbatch -o my.stdout my.script
```

`my.stdout` 不同用户的输出会略有不同

```text
c01r2n01
1: c01r2n01
0: c01r2n01
2: c01r2n01
3: c01r2n01
4: c01r2n02
6: c01r2n02
5: c01r2n02
7: c01r2n02
1: /work/home/acfu6a24vx
4: /work/home/acfu6a24vx
0: /work/home/acfu6a24vx
6: /work/home/acfu6a24vx
2: /work/home/acfu6a24vx
7: /work/home/acfu6a24vx
5: /work/home/acfu6a24vx
3: /work/home/acfu6a24vx
```

## Example01: conda python environment

在登录节点创建`conda/mamba`环境，关于`conda/mamba`使用见 [github/husisy/learning/python/conda](https://github.com/husisy/learning/tree/master/python/conda)

```bash
micromamba create -n nocuda
micromamba install -y -n nocuda pytorch cython ipython pytest matplotlib h5py pandas pillow protobuf scipy requests tqdm lxml opt_einsum

micromamba shell init --shell=bash --prefix=~/micromamba
```

准备如下文件

```text
sbatch.script
run.sh
draft00.py
```

`sbatch.script`

```bash
#!/bin/sh
#SBATCH -J python-hello-world
#SBATCH -p xahctest
#SBATCH -N 1
#SBATCH --ntasks-per-node=2
srun -l bash run.sh
```

`run.sh`

```bash
source ~/.bashrc
micromamba activate nocuda
python -u draft00.py
# -u to disable output buffering
```

`draft00.py`

```Python
import sys
import torch
print(f'python path: {sys.executable}')
print(f'python version: {sys.version}')
print(f'pytorch version: {torch.__version__}')
```

登录节点提交作业

```bash
sbatch -o sbatch.stdout sbatch.script
```

`sbatch.stdout`

```text
0: python path: /work/home/acfu6a24vx/micromamba/envs/nocuda/bin/python
0: python version: 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0]
0: pytorch version: 2.0.0
1: python path: /work/home/acfu6a24vx/micromamba/envs/nocuda/bin/python
1: python version: 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0]
1: pytorch version: 2.0.0
```
