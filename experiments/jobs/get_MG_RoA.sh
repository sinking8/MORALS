#!/bin/sh

#SBATCH --partition=medium
#SBATCH --account=medium
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=100G
#SBATCH --gpus=1

#SBATCH --mail-user=ashwinb@isi.edu
#SBATCH --mail-type=BEGIN,END,FAIL,REQUEUE,ALL

python "/nas/home/ashwinb/robotic_manipulation/MORALS/experiments/get_MG_RoA.py" --config_dir "/nas/home/ashwinb/robotic_manipulation/MORALS/experiments/config/" --config /pendulum/pendulum_lqr_2.txt  --RoA --sub 16 