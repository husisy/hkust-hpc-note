import os
import torch

os.system('nvidia-smi')

for key,value in os.environ.items():
    print(f'{key}={value}')

# os.system('conda install -y -n cuda113a -c conda-forge cython ipython pytest matplotlib h5py pandas pylint jupyterlab pillow protobuf scipy requests tqdm lxml opt_einsum cupy nccl')

print(f'{torch.__file__=}')
print(f'{torch.__version__=}')
print(f'{torch.cuda.is_available()=}')
print(f'{torch.cuda.device_count()=}')
