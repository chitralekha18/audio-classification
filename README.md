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
The output is going to be in your current directory in "predicted_.csv". The number of columns in this file is equal to the number of nodes in penultimate layer plus the number of output nodes. For example, if the penultimate layer has 3 nodes and the final layer has 2 nodes, there will be 5 columns in the predicted CSV file.

### Merge classifier output with GAN json file
Additionally, to merge the predicted softlabels and outputs of the classifier with the GAN json file, follow the following steps:

5. copy the *predicted_\*.csv* file to the folder IncludeSoftLabelsToGANjson, and rename it to represent the number of penultimate and final nodes. For example, if the penultimate layer has 3 nodes and the final layer has 2 nodes, rename this file to *predicted_3_2.csv*.
6. Also copy the json file from the data directory for GAN into this folder (IncludeSoftLabelsToGANjson)
7. And copy the test csv generated from 1. into this folder (IncludeSoftLabelsToGANjson)
8. Run the following command to add the classifier outputs to the given GAN json file:
```console
python addsoftlabels.py <predicted_*.csv> <testfilelist CSV> <original_GANjson> <output_json_withsoftlabels>
```
For example: (the example set of files is already provided) 
```console
python addsoftlabels.py predicted_densenet_waterwind_3_2.csv waterwind_test.csv nsjson_modified.json nsjson_modified_softclasslabels.json
```
The new json file will contain *"softlabel_x_y_z"* added to each file entry where *x* is the number of nodes in penultimate layer, *y* is number of nodes in the output layer, and *z* is the current node ID. So for example, when you use "predicted_densenet_waterwind_3_2.csv", the *x* and *y* values will always be *3* and *2* respectively, and *z* value will range from 0 to 4, where 0, 1 and 2 represent the three penultimate layer nodes, and 3 and 4 represent the two final layer nodes.
