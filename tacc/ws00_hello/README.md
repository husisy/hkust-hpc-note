# ws00 hello

submit the job

```bash
tcloud submit
```

see the output

```bash
tcloud cat slurm_log/ws00_hello.log
# hello from tacc
```

what's happening under the hood?

1. craate a conda environment `hello` if it doesn't exists (the following example will depend on this environment)
   * sit down and be relax, it might be several minutes
2. upload the files in current folder (be care, do not put large file in current folder)
3. TODO
