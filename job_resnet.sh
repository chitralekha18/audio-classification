#!/bin/bash
#SBATCH --job-name=audclas
#SBATCH --partition=gpu
#SBATCH --output=train_audclass_resnet.txt
#SBATCH --gres=gpu:1

python train.py --config_path config/rnn_resnet.json
