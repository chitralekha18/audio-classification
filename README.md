# Rethinking CNN Models for Audio Classification

This repository is forked from the repository that contains the PyTorch code for the paper [Rethinking CNN Models for Audio Classification](https://arxiv.org/abs/2007.11154). 

It involves four steps:
1. prepare csv
2. preprocessing
3. training
4. testing

### PrepCSV
Refer to PrepCSV/CreateCSV*.py to prepare the csv file that has a list of all the training, validation, and test files. The only difference between train-validation set and test set csvs is that train/validation has 5 folds, while test has only 1 fold.
### Preprocessing
The preprocessing is done separately to save time during the training of the models.
 
```console
python preprocessing/preprocessing_trainValidation.py --csv_file ./PrepCSV/<file>.csv --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/ --sampling_rate 16000
```

### Training the Models

The configurations for training the models are provided in the config folder. The sample_config.json explains the details of all the variables in the configurations. The command for training is: 
```console
python train.py --config_path /config/your_config.json
```

### Testing the model
```console
python test.py --config_path /config/your_config.json
```
