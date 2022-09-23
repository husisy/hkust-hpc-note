import torch
import numpy as np

class MyModel00(torch.nn.Module):
    def __init__(self):
        super(MyModel00, self).__init__()
        self.fc0 = torch.nn.Linear(5, 13)
        self.fc1 = torch.nn.Linear(13, 1)

    def forward(self, x):
        x = self.fc0(x)
        x = torch.nn.functional.relu(x)
        x = self.fc1(x)[:,0]
        return x


def demo_basic(rank, world_size):
    print(f'# demo_basic[rank={rank}]')
    torch.distributed.init_process_group(backend='nccl',
            init_method='tcp://127.0.0.1:23333', rank=rank, world_size=world_size)
    device = torch.device(f'cuda:{rank}')

    model = MyModel00().to(device)
    ddp_model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[rank])

    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(ddp_model.parameters(), lr=0.001)

    optimizer.zero_grad()
    outputs = ddp_model(torch.randn(23, 5))
    labels = torch.randn(23).to(device)
    loss_fn(outputs, labels).backward()
    optimizer.step()

    torch.distributed.destroy_process_group()


if __name__ == "__main__":
    n_gpus = torch.cuda.device_count()

    # see https://pytorch.org/docs/stable/nn.html#distributeddataparallel
    torch.multiprocessing.set_start_method('spawn')

    if n_gpus>1:
        world_size = n_gpus
        torch.multiprocessing.spawn(demo_basic, args=(world_size,), nprocs=world_size, join=True)
