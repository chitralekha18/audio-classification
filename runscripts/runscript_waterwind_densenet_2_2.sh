#!/bin/bash
#SBATCH --job-name=dense22
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1

#python preprocessing/preprocessingRNN.py --csv_file /home/chitra/workspace/code/Audio-Classification/PrepCSV/waterwind.csv --data_dir /data07/chitra/workspace/data/WaterWind2/audio --store_dir WaterWind_densenet/store_spectrograms/ --sampling_rate 16000 > prepro2.log
python train.py --config_path /home/chitra/workspace/code/Audio-Classification/config/waterwind_densenet_2_2.json > train_2_3.log
