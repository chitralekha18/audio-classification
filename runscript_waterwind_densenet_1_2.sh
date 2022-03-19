#!/bin/bash
#SBATCH --job-name=densenet12
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1

#python preprocessing/preprocessing_trainValidation.py --csv_file /home/chitra/workspace/code/Audio-Classification/PrepCSV/waterwind.csv --data_dir /data07/chitra/workspace/data/WaterWind2/audio --store_dir WaterWind_densenet/store_spectrograms/ --sampling_rate 16000 > prepro2.log
python train.py --config_path /home/chitra/workspace/code/Audio-Classification/config/waterwind_densenet_1_2.json > train_1_2.log
