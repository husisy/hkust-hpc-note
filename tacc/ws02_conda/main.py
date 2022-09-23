import os
import subprocess


def list_conda_env():
    proc = subprocess.run(['conda', 'env', 'list'], stdout=subprocess.PIPE)
    ret = set([x.split()[0] for x in proc.stdout.decode('utf-8').split('\n')[3:] if x])
    return ret

def is_env_exist(name):
    env_list = list_conda_env()
    ret = name in env_list
    return ret

def delete_conda_env(name):
    env_list = list_conda_env()
    if name in env_list:
        os.system(f'conda env remove -n {name}')

# delete_conda_env('cuda113a')

assert not is_env_exist('cuda113')
os.system('conda create -y -n cuda113')
os.system('conda install -y -n cuda113 -c pytorch pytorch torchvision torchaudio cudatoolkit=11.3')
os.system('conda install -y -n cuda113 -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum cupy nccl')

# conda create -y -n cuda113
# conda install -y -n cuda113 -c conda-forge cudatoolkit=11.3
# conda install -y -n cuda113 -c pytorch pytorch torchvision torchaudio
# conda install -y -n cuda113 -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum cupy nccl
