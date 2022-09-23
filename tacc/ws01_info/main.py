import os

def test_command(cmd):
    print(f'#{cmd}') #TODO the print out is out of sync
    os.system(cmd)
    print() #newline

for key,value in os.environ.items():
    print(f'{key}={value}')
WORKDIR = os.environ.get('TACC_WORKDIR') #/mnt/home/xxx/WORKDIR/ws01_info
USERDIR = os.environ.get('TACC_USERDIR') #/mnt/home/xxx/USERDIR
SLURM_USERLOG = os.environ.get('TACC_SLURM_USERLOG') #None
print(f'{WORKDIR=}')
print(f'{USERDIR=}')
print(f'{SLURM_USERLOG=}')

test_command('nvidia-smi')

test_command('nvidia-smi -q')

test_command('lscpu')

test_command('free -h')

test_command('df -h')

test_command('which conda') #/mnt/home/xxx/.Miniconda3/condabin/conda

# tcloud cat /slurm_log/hello.log
