# README TACC

1. link
   * [github/turingaicloud/quickstart](https://github.com/turingaicloud/quickstart)
   * [official-site](https://tacc.ust.hk/)
2. 配置本地环境（非windows）
   * 邮件联系官方表示希望申请账号`tacc-contact@lists.ust.hk`：需要准备公钥私钥、填写google-form、用户名等
   * 下载tcloud SDK [github-link](https://github.com/turingaicloud/quickstart/releases)
   * 解压，执行`setup.sh`，将`tcloud`添加至全局变量`PATH`
   * `tcloud config --username XXX`
   * `tcloud config --file /absolute/path/to/private/id-rsa`
   * `tcloud init`
3. 常用命令
   * `tcloud ls ..`
   * `tcloud ls slurm_log`
   * `tcloud ls slurm_log/xxx.log`
   * `tcloud submit`

如下文件夹分别是

1. `ws00_hello`: how to print hello world on cluster
2. `ws01_info`: basic info about the cluster, like CPU/GPU/memory/disk
3. `ws02_conda`: setup conda environment
4. `ws03_torch_basic`: demo basic torch/cupy function on GPU
5. `ws04_torch_distributed`: demo torch basic MPI operation, like send/recv
6. `ws05_torch_ddp`: demo torch DDP training
7. `ws10_official way`: the recommended way to setup conda environment in the official documentation
