# hpc3-setup

`setup_jupyter.sh`参数说明 `srun -p cpu-share -n1 bash setup_jupyter.sh ~/project/ws00 23333 23334`

1. 可选参数1 `~/project/ws00` 指定jupyter的启动目录，默认为`slurm`运行命令的当前目录
2. 可选参数2 jupyter的运行端口（位于计算节点），默认`23333`
3. 可选参数3 ssh的转发端口（位于登录节点），默认`23334`，可以与jupyter的运行端口相同

`setup_jupyter.sh`命令讲解

1. `srun -p cpu-share -n1 bash` 申请一个CPU计算资源，并执行bash进程，此时命令行会进入到`bash`交互式环境，等待输入但无`bash`提示符
2. `. "/home/$USER/miniconda3/etc/profile.d/conda.sh"` 激活计算节点的conda环境
3. `conda activate cuda113` 激活`cuda113`环境
4. `nohup jupyter lab --port=23333 > ~/jupyter_lab.log 2>&1 &` 执行
   * 也许你需要添加`--no-browser`参数
   * `nohup`将该行命令在后台执行
   * 指定jupyter server运行在`23333`端口
5. `ssh -NT -R 127.0.0.1:23333:127.0.0.1:23333 login-node`
   * 从计算节点ssh登录至登录节点，同时`-R`将计算节点的`23333`端口转发至登录节点的`23333`端口
   * [ubuntu doc - OpenSSH Server](https://help.ubuntu.com/lts/serverguide/openssh-server.html)
   * [阮一峰 - SSH原理与运用一](http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html)
   * [阮一峰 - SSH原理与运用二](http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html)
