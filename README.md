# Rethinking CNN Models for Audio Classification

This repository is forked from the repository that contains the PyTorch code for the paper [Rethinking CNN Models for Audio Classification](https://arxiv.org/abs/2007.11154). 

## Installation
Install the packages to create the conda 'audioclassification2' environment:
```
conda env create -f requirements.yml
conda activate audioclassification2
```

## Audio Classification Train and Test
It involves four steps:
1. prepare csv
2. preprocessing
3. training
4. testing


### PrepCSV
Run PrepCSV/CreateCSVs.py to prepare the csv files that have a list of all the (a) training and validation, and (b) test files. The only difference between train-validation set and test set csvs is that train/validation has 5 folds, while test has only 1 fold.

```console
python PrepCSV/CreateCSVs.py --datafolder path/to/audio --trainfolds=5 --csvfile=path/to/out_TRAIN.csv

python PrepCSV/CreateCSVs.py --datafolder path/to/audio --trainfolds=1 --csvfile=path/to/out_TEST.csv
```

### Preprocessing
The preprocessing is done ahead of time to save time during the training of the models. 

```console
python preprocessing/preprocessing_trainValidation.py --csv_file path/to/out_TRAIN.csv --data_dir /path/to/audio_data/ --store_dir path/to/store_spectrograms/ --sampling_rate 16000

python preprocessing/preprocessing_test.py --csv_file path/to/out_TEST.csv --data_dir path/to/audio_data/ --store_dir path/to/store_spectrograms/ --sampling_rate 16000

```

### Training the Models

The configurations for training the models are provided in the config folder. The sample_config.json explains the details of all the variables in the configurations. The command for training is: 
```console
python train.py --config_path config/your_config.json
```

### Testing the model
```console
python test.py --config_path config/your_config.json
```
The output is going to be in your current directory in "predicted_x_y.csv", where x is the number of penultimate nodes, and y is the number of classes. The number of columns in this file is equal to x+y. For example, if the penultimate layer has 3 nodes and the final layer has 2 nodes, there will be 5 columns in the predicted CSV file.


### Merge classifier output with GAN json file
Additionally, to merge the predicted softlabels and outputs of the classifier with the GAN json file, follow the following steps:

5. copy the *predicted_\*.csv* file to a folder, for example, softLabelsForGAN/
6. copy the original GAN json file from your GAN data directory  into this folder softLabelsForGAN/
7. copy the testfilelist csv generated from 1. into softLabelsForGAN/
8. Run the following command to add the classifier outputs to the given GAN json file:
```console
python addsoftlabels.py <predicted_*.csv> <testfilelist CSV> <original_GANjson> <output_json_withsoftlabels>
```
The new json file will contain *"softlabel_x_y_z"* added to each file entry where *x* is the number of nodes in penultimate layer, *y* is number of nodes in the output layer, and *z* is the current node ID. So for example, if you use "predicted_*_3_2.csv", the *x* and *y* values will always be *3* and *2* respectively, and *z* value will range from 0 to 4, where 0, 1 and 2 represent the three penultimate layer nodes, and 3 and 4 represent the two final layer nodes.
