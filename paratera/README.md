# 超算云paratera

1. link
   * [website](https://cloud.paratera.com/)
2. 独占节点形式，不满核按满核收费

```bash
export http_proxy=http://172.16.54.201:8888
export https_proxy=http://172.16.54.201:8888
export ftp_proxy=http://172.16.54.201:8888
```

## Example00: srun hello world

```bash
# partition all amd_256
srun -p amd_256 -n1 pwd
# /public3/home/sc72969
srun -p amd_256 -n1 hostname
# w1309.para.bscc
srun -p amd_256 -n1 echo "hello world"
srun -p amd_256 -n1 lscpu
srun -p amd_256 -n2 -N2 printenv | grep SLURM
```

```text
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                64
On-line CPU(s) list:   0-63
Thread(s) per core:    1
Core(s) per socket:    32
Socket(s):             2
NUMA node(s):          2
Vendor ID:             AuthenticAMD
CPU family:            23
Model:                 49
Model name:            AMD EPYC 7452 32-Core Processor
Stepping:              0
CPU MHz:               2345.757
BogoMIPS:              4691.51
Virtualization:        AMD-V
L1d cache:             32K
L1i cache:             32K
L2 cache:              512K
L3 cache:              16384K
NUMA node0 CPU(s):     0-31
NUMA node1 CPU(s):     32-63
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc art rep_good nopl nonstop_tsc extd_apicid aperfmperf eagerfpu pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_l2 cpb cat_l3 cdp_l3 hw_pstate sme ssbd rsb_ctxsw ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip overflow_recov succor smca
```

```text
SLURM_CONF=/var/spool/slurm/d/conf-cache/slurm.conf
SLURM_MPI_TYPE=pmi2
SLURM_PRIO_PROCESS=0
SLURM_UMASK=0002
SLURM_CLUSTER_NAME=bscc-a2
SLURM_SUBMIT_DIR=/public3/home/sc72969/ws00
SLURM_SUBMIT_HOST=ln32.para.bscc
SLURM_JOB_NAME=printenv
SLURM_JOB_CPUS_PER_NODE=64
SLURM_NTASKS=1
SLURM_NPROCS=1
SLURM_JOB_ID=1823346
SLURM_JOBID=1823346
SLURM_STEP_ID=0
SLURM_STEPID=0
SLURM_NNODES=1
SLURM_JOB_NUM_NODES=1
SLURM_NODELIST=w2115
SLURM_JOB_PARTITION=amd_256
SLURM_TASKS_PER_NODE=1
SLURM_SRUN_COMM_PORT=43458
SLURM_JOB_UID=3998
SLURM_JOB_USER=sc72969
SLURM_JOB_ACCOUNT=bscc-a2
SLURM_JOB_QOS=normal
SLURM_WORKING_CLUSTER=bscc-a2:172.16.52.101:6817:9472:102
SLURM_JOB_NODELIST=w2115
SLURM_STEP_NODELIST=w2115
SLURM_STEP_NUM_NODES=1
SLURM_STEP_NUM_TASKS=1
SLURM_STEP_TASKS_PER_NODE=1
SLURM_STEP_LAUNCHER_PORT=43458
SLURM_SRUN_COMM_HOST=172.16.54.202
SLURM_TOPOLOGY_ADDR=bscc-a2_zone1.w2115
SLURM_TOPOLOGY_ADDR_PATTERN=switch.node
SLURM_CPUS_ON_NODE=64
SLURM_CPU_BIND=quiet,mask_cpu:0xFFFFFFFFFFFFFFFF
SLURM_CPU_BIND_LIST=0xFFFFFFFFFFFFFFFF
SLURM_CPU_BIND_TYPE=mask_cpu:
SLURM_CPU_BIND_VERBOSE=quiet
SLURM_TASK_PID=58921
SLURM_NODEID=0
SLURM_PROCID=0
SLURM_LOCALID=0
SLURM_LAUNCH_NODE_IPADDR=172.16.54.202
SLURM_GTIDS=0
SLURM_JOB_GID=3998
SLURMD_NODENAME=w2115
```

## Example01: sbatch hello world

`my.script`

```bash
#!/bin/sh
#SBATCH -J sbatch-hello-world
#SBATCH -p amd_256
#SBATCH -N 2
#SBATCH --ntasks-per-node=3
/bin/hostname
srun -l /bin/hostname
srun -l /bin/pwd
```

PS: `-l` prepend task number to lines of stdout/err

登录节点提交作业

```bash
sbatch -o my.stdout my.script
```

`my.stdout` 不同用户的输出会略有不同

```text
ea0315.para.bscc
3: ea0405.para.bscc
1: ea0315.para.bscc
0: ea0315.para.bscc
4: ea0405.para.bscc
5: ea0405.para.bscc
2: ea0315.para.bscc
5: /public3/home/sc72969/ws00
0: /public3/home/sc72969/ws00
4: /public3/home/sc72969/ws00
1: /public3/home/sc72969/ws00
2: /public3/home/sc72969/ws00
3: /public3/home/sc72969/ws00
```

## Example02: conda python environment

`.mambarc`

```text
always_yes: false
channels:
  - conda-forge
show_channel_urls: true
default_channels:
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/main
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/r
  - https://mirrors.bfsu.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.bfsu.edu.cn/anaconda/cloud
  msys2: https://mirrors.bfsu.edu.cn/anaconda/cloud
  bioconda: https://mirrors.bfsu.edu.cn/anaconda/cloud
  menpo: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch: https://mirrors.bfsu.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.bfsu.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.bfsu.edu.cn/anaconda/cloud
```

```bash
micromamba create -n nocuda
micromamba install -y -n nocuda pytorch cython ipython pytest matplotlib h5py pandas pillow protobuf scipy requests tqdm lxml opt_einsum cvxpy
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
#SBATCH -p amd_256
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
1: python path: /public3/home/sc72969/micromamba/envs/nocuda/bin/python
1: python version: 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0]
1: pytorch version: 2.0.0
0: python path: /public3/home/sc72969/micromamba/envs/nocuda/bin/python
0: python version: 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0]
0: pytorch version: 2.0.0
```

基于今天的使用体验来评价Sugon曙光、paratera超算云、hzw鸿之微

1. 使用体验降序：Sugon > paratera > hzw
2. paratera超算需要代理方可访问外网，香港访问hzw需要网络代理
3. hzw不提供GPU，其余二者提供GPU/DCU
4. UDA/UDP代码均可运行，但未对比运行时间
