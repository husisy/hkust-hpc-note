# ws01 info

submit the job

```bash
tcloud submit
```

see the output

```bash
tcloud cat slurm_log/ws01_info.log
```

`nvidia-smi`

```txt
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 465.19.01    Driver Version: 465.19.01    CUDA Version: 11.3     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  On   | 00000000:3D:00.0 Off |                  N/A |
| 33%   30C    P8    24W / 300W |      1MiB / 24268MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce ...  On   | 00000000:3F:00.0 Off |                  N/A |
| 33%   30C    P8    23W / 300W |      1MiB / 24268MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   2  NVIDIA GeForce ...  On   | 00000000:40:00.0 Off |                  N/A |
| 33%   30C    P8    23W / 300W |      1MiB / 24268MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   3  NVIDIA GeForce ...  On   | 00000000:41:00.0 Off |                  N/A |
| 33%   31C    P8    19W / 300W |      1MiB / 24268MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

`lscpu`

```txt
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              80
On-line CPU(s) list: 0-79
Thread(s) per core:  2
Core(s) per socket:  20
Socket(s):           2
NUMA node(s):        2
Vendor ID:           GenuineIntel
CPU family:          6
Model:               85
Model name:          Intel(R) Xeon(R) Gold 5218R CPU @ 2.10GHz
Stepping:            7
CPU MHz:             818.259
CPU max MHz:         4000.0000
CPU min MHz:         800.0000
BogoMIPS:            4200.00
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            1024K
L3 cache:            28160K
NUMA node0 CPU(s):   0-19,40-59
NUMA node1 CPU(s):   20-39,60-79
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb cat_l3 cdp_l3 invpcid_single intel_ppin ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm mpx rdt_a avx512f avx512dq rdseed adx smap clflushopt clwb intel_pt avx512cd avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat pln pts pku ospke avx512_vnni md_clear flush_l1d arch_capabilities
```

`free -h`

```txt
              total        used        free      shared  buff/cache   available
Mem:           251G         29G        147G        828M         74G        219G
Swap:          8.0G        6.1G        1.9G
```

`df -h`

```txt
Filesystem                        Size  Used Avail Use% Mounted on
overlay                           916G   96G  774G  11% /
tmpfs                              64M     0   64M   0% /dev
tmpfs                             126G     0  126G   0% /sys/fs/cgroup
shm                                64G  834M   64G   2% /dev/shm
10.0.201.1:gluster-trs-data.rdma  7.3T  4.3T  2.7T  62% /mnt/data
10.0.201.1:gluster-trs-home.rdma  7.3T  5.2T  1.8T  75% /mnt/home
/dev/sda2                         916G   96G  774G  11% /etc/hosts
tmpfs                             126G   12K  126G   1% /proc/driver/nvidia
tmpfs                              26G  9.5M   26G   1% /run/nvidia-persistenced/socket
udev                              126G     0  126G   0% /dev/nvidia4
tmpfs                             126G     0  126G   0% /proc/asound
tmpfs                             126G     0  126G   0% /proc/acpi
tmpfs                             126G     0  126G   0% /proc/scsi
tmpfs                             126G     0  126G   0% /sys/firmware
```

`getenv`

```txt
CONDA_SHLVL=1
CONDA_EXE=/mnt/home/xxx/.Miniconda3/bin/conda
SRUN_DEBUG=3
SLURM_STEP_ID=0
SLURM_NODEID=0
SLURM_TASK_PID=44783
SSH_CONNECTION=103.49.160.65 37540 192.168.1.213 22
SLURM_PRIO_PROCESS=0
LANG=C.UTF-8
SLURM_SUBMIT_DIR=/mnt/home/xxx/WORKDIR/ws01_info
HOSTNAME=10-0-3-12
OLDPWD=/mnt/home/xxx
SLURM_CPUS_PER_TASK=1
SLURM_STEPID=0
SLURM_SRUN_COMM_HOST=10.0.3.12
SLURM_DISTRIBUTION=cyclic
ENVIRONMENT=BATCH
SLURM_CHECKPOINT_IMAGE_DIR=/var/slurm/checkpoint
CONDA_PREFIX=/mnt/home/xxx/.Miniconda3/envs/hello
SLURM_PROCID=0
SLURM_JOB_GID=20168
SLURMD_NODENAME=10-0-3-12
SLURM_TASKS_PER_NODE=1
_CE_M=
XDG_SESSION_ID=14830535
USER=xxx
SLURM_NNODES=1
SLURM_LAUNCH_NODE_IPADDR=10.0.3.12
SLURM_STEP_TASKS_PER_NODE=1
PWD=/mnt/home/xxx/WORKDIR/ws01_info
SLURM_JOB_NODELIST=10-0-3-12
HOME=/mnt/home/xxx
SLURM_CLUSTER_NAME=tacc
CONDA_PYTHON_EXE=/mnt/home/xxx/.Miniconda3/bin/python
SLURM_NODELIST=10-0-3-12
SSH_CLIENT=103.49.160.65 37540 22
SLURM_NTASKS=1
SLURM_UMASK=0002
SLURM_JOB_CPUS_PER_NODE=20
TACC_USERDIR=/mnt/home/xxx/USERDIR
SLURM_TOPOLOGY_ADDR=10-0-3-12
_CE_CONDA=
SLURM_WORKING_CLUSTER=tacc:cpu03:6817:8192
SLURM_STEP_NODELIST=10-0-3-12
SLURM_JOB_NAME=run.slurm
SLURM_SRUN_COMM_PORT=43663
TMPDIR=/tmp
SLURM_JOBID=8652
SLURM_JOB_QOS=taccqos
SLURM_TOPOLOGY_ADDR_PATTERN=node
CONDA_PROMPT_MODIFIER=(hello)
SSH_TTY=/dev/pts/9
MAIL=/var/mail/xxx
SLURM_CPUS_ON_NODE=20
SLURM_JOB_NUM_NODES=1
TERM=xterm
SHELL=/bin/bash
SLURM_JOB_UID=20167
SLURM_JOB_PARTITION=tacc
SLURM_JOB_USER=xxx
SLURM_NPROCS=1
SHLVL=3
TACC_WORKDIR=/mnt/home/xxx/WORKDIR/ws01_info
SLURM_SUBMIT_HOST=10-0-3-12
SLURM_JOB_ACCOUNT=tacc
SLURM_STEP_LAUNCHER_PORT=43663
SLURM_GTIDS=0
LOGNAME=xxx
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/20167/bus
XDG_RUNTIME_DIR=/run/user/20167
PATH=/mnt/home/xxx/.Miniconda3/envs/hello/bin:/mnt/home/xxx/.Miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
SLURM_JOB_ID=8652
SLURM_STEP_NUM_TASKS=1
CONDA_DEFAULT_ENV=hello
SLURM_STEP_NUM_NODES=1
SLURM_LOCALID=0
_=/mnt/home/xxx/.Miniconda3/envs/hello/bin/python
```
