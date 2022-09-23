# ws04 torch distributed

submit the job

```bash
tcloud submit
```

see the output

```bash
tcloud cat slurm_log/ws04_torch_distributed.log
```

`ws04_torch_distributed.log`

```txt
# demo_send_recv[rank=1]
[rank=1] recv "tensor([ 0.6517, -0.2573,  0.9071])"
# demo_send_recv[rank=0]
[rank=0] send "tensor([ 0.6517, -0.2573,  0.9071])"
# demo_send_recv[rank=0]
[rank=0] send "tensor([-0.4900, -0.2297,  1.0807])"
# demo_send_recv[rank=1]
[rank=1] recv "tensor([-0.4900, -0.2297,  1.0807])"
# demo_non_blocking_send_recv[rank=0]
[rank=0] isend "tensor([-1.0977,  0.4893,  0.2584])"
[rank=0] torch0=tensor([-1.0977,  0.4893,  0.2584])
# demo_non_blocking_send_recv[rank=1]
[rank=1] irecv "tensor([-2.5870e-11,  4.5566e-41,  5.4376e-14])"
[rank=1] torch0=tensor([-1.0977,  0.4893,  0.2584])
# demo_tensor_sync_gradient[rank=1]
[rank=1] recv "tensor([ 0.2887, -1.0888, -0.9806], requires_grad=True)"
[rank=1] torch0.grad= "None"
[rank=1] totally not work at all
# demo_tensor_sync_gradient[rank=0]
[rank=0] send "tensor([ 0.2887, -1.0888, -0.9806], requires_grad=True)"
[rank=0] torch0.grad= "tensor([ 0.5038, -2.2189,  0.9740])"
[rank=0] totally not work at all
```
