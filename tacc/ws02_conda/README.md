# ws02 manage conda environment

BE VERY CAREFULL!!! use this folder only when you know every line exactly.

**请谨慎**使用当前文件夹的代码，当且仅当你非常清楚这里的每一行代码再去使用之

当前文件夹的代码在做如下操作

1. 基于`hello`环境执行`main.py`代码
2. 检测是否存在`cuda113`环境，如果存在则删去这一环境
3. 创建`cuda113`环境
4. 依次执行如下命令来安装这些包

```bash
conda create -y -n cuda113
conda install -y -n cuda113 -c pytorch pytorch torchvision torchaudio cudatoolkit=11.3
# conda install -y -n cuda113 -c conda-forge cudatoolkit=11.3
# conda install -y -n cuda113 -c pytorch pytorch torchvision torchaudio
conda install -y -n cuda113 -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum cupy nccl
# TODO start from ws10_official_way
```
