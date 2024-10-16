#!/bin/sh

#SBATCH --partition=medium-lg
#SBATCH --account=medium-lg
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=100G
#SBATCH --gpus=1

#SBATCH --mail-user=ashwinb@isi.edu
#SBATCH --mail-type=BEGIN,END,FAIL,REQUEUE,ALL

python "/nas/home/ashwinb/robotic_manipulation/MORALS/examples/get_MG_RoA.py" --config trifinger.txt --name_out trifinger --RoA --sub 16 