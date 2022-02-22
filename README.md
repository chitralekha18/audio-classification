# Rethinking CNN Models for Audio Classification

This repository is forked from the repository that contains the PyTorch code for the paper [Rethinking CNN Models for Audio Classification](https://arxiv.org/abs/2007.11154). 

It involves three steps:
1. preprocessing
2. training
3. testing

The preprocessing is done separately to save time during the training of the models.

For ESC-50: 
```console
python preprocessing/preprocessingESC.py --csv_file /path/to/file.csv --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/ --sampling_rate 44100
```

For UrbanSound8K:
```console
python preprocessing/preprocessingUSC.py --csv_file /path/to/csv_file/ --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/
```

For GTZAN:
```console
python preprocessing/preprocessingGTZAN.py --data_dir /path/to/audio_data/ --store_dir /path/to/store_spectrograms/ --sampling_rate 22050
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
