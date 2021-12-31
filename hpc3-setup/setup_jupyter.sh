notebook_dir=${1:-${PWD}}
compute_node_port=${2:-23333}
login_node_port=${3:-23334}

uid=$(date '+%Y%m%d%H%M%S')_$$
logdir=~/hpc3-setup/${uid}
mkdir -p ${logdir}

. "/home/$USER/miniconda3/etc/profile.d/conda.sh"
conda activate cuda113
cd ${notebook_dir}
nohup jupyter lab --port=${compute_node_port} --ServerApp.open_browser=False --ExtensionApp.open_browser=False > ${logdir}/jupyter_lab.log 2>&1 &
# --notebook-dir=${notebook_dir}
nohup ssh -NT -v -R 127.0.0.1:${login_node_port}:127.0.0.1:${compute_node_port} login-node > ${logdir}/ssh.log 2>&1 &
echo "[setup_jupyter.sh] jupyter and ssh-R is running"
sleep 7d
kill %1
kill %2
sleep 1 #wait for one second
echo "[setup_jupyter.sh] goodbye"
