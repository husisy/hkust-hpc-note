import torch
import cupy as cp
import numpy as np

def demo_torch_info():
    #TODO conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
    print(f'{torch.__file__=}') #/mnt/home/xxx/.Miniconda3/envs/cuda113/lib/python3.10/site-packages/torch/__init__.py
    print(f'{torch.__version__=}') #1.12.1
    print(f'{torch.cuda.is_available()=}') #True
    print(f'{torch.cuda.device_count()=}') #4


def test_torch_matmul():
    assert torch.cuda.is_available()
    np_rng = np.random.default_rng()
    np0 = np_rng.uniform(size=(3, 3)).astype(np.float64)
    np1 = np_rng.uniform(size=(3, 3)).astype(np.float64)
    device = 'cuda'

    ret_ = np0 @ np1
    torch0 = torch.tensor(np0, dtype=torch.float64, device=device)
    torch1 = torch.tensor(np1, dtype=torch.float64, device=device)
    ret0 = (torch0 @ torch1).cpu().numpy()
    assert np.abs(ret_-ret0).max() < 1e-10


def test_cupy_matmul():
    np_rng = np.random.default_rng()
    np0 = np_rng.uniform(size=(3, 3)).astype(np.float64)
    np1 = np_rng.uniform(size=(3, 3)).astype(np.float64)

    ret_ = np0 @ np1
    cp0 = cp.array(np0, dtype=cp.float64)
    cp1 = cp.array(np1, dtype=cp.float64)
    ret0 = (cp0 @ cp1).get()
    assert np.abs(ret_-ret0).max() < 1e-10



if __name__=='__main__':
    demo_torch_info()

    test_torch_matmul()

    test_cupy_matmul()
