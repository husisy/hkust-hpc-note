# 鸿之微hzw

1. link
   * [website](https://cloud.hzwtech.com/)
2. 绑定邮箱、下载软件获得试用机时

## Example00: srun hello world

```bash
# partition: normal
srun -p normal -n1 pwd
# /data/home/df103693/df103693
srun -p normal -n1 hostname
# c16
srun -p normal -n1 echo "hello world"
srun -p normal -n1 lscpu
srun -p normal -n2 -N2 printenv | grep SLURM
```

```text
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                28
On-line CPU(s) list:   0-27
Thread(s) per core:    1
Core(s) per socket:    14
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 79
Model name:            Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz
Stepping:              1
CPU MHz:               2400.000
CPU max MHz:           2400.0000
CPU min MHz:           1200.0000
BogoMIPS:              4788.87
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              35840K
NUMA node0 CPU(s):     0-13
NUMA node1 CPU(s):     14-27
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch epb cat_l3 cdp_l3 invpcid_single intel_ppin intel_pt ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm rdt_a rdseed adx smap xsaveopt cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm arat pln pts md_clear spec_ctrl intel_stibpflush_l1d
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
c103
0: c103
1: c103
2: c103
3: c104
4: c104
5: c104
0: /data/home/df103693/df103693/ws00
1: /data/home/df103693/df103693/ws00
2: /data/home/df103693/df103693/ws00
4: /data/home/df103693/df103693/ws00
3: /data/home/df103693/df103693/ws00
5: /data/home/df103693/df103693/ws00
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
#SBATCH -p normal
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
0: python path: /data/home/df103693/df103693/micromamba/envs/nocuda/bin/python
0: python version: 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0]
0: pytorch version: 2.0.0
1: python path: /data/home/df103693/df103693/micromamba/envs/nocuda/bin/python
1: python version: 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0]
1: pytorch version: 2.0.0
```
