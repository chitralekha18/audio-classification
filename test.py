import torch
import torchvision
import torch.nn as nn
import numpy as np
import json
import utils
import validate
import argparse
import models.densenet
import models.resnet
import models.inception
import time
import dataloaders.datasetaug
import dataloaders.datasetnormal
import pdb
from tqdm import tqdm
from tensorboardX import SummaryWriter

parser = argparse.ArgumentParser()
parser.add_argument("--config_path", type=str)



def evaluate(model, device, val_loader, params, split):

    acc,conf_mat = validate.evaluate(model, device, val_loader)
    print(conf_mat)
    return acc


if __name__ == "__main__":
    args = parser.parse_args()
    params = utils.Params(args.config_path)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    for i in range(0, params.num_folds):
        if params.dataaug:
            val_loader = dataloaders.datasetaug.fetch_dataloader("{}testing128mel{}.pkl".format(params.data_dir, i), params.dataset_name, params.batch_size, params.num_workers, 'testing')
        else:
            val_loader = dataloaders.datasetnormal.fetch_dataloader("{}testing128mel{}.pkl".format(params.data_dir, i), params.dataset_name, params.batch_size, params.num_workers)

        writer = SummaryWriter(comment=params.dataset_name)
        if params.model=="densenet":
            model = models.densenet.DenseNet(params.dataset_name, params.pretrained).to(device)
            chkpt,model = utils.load_checkpoint('RNN/rnn_checkpoint_dir/model_best_4.pth.tar',model)
#            model = utils.load_checkpoint('RNN/rnn_checkpoint_dir/last2.pth.tar',model)
        elif params.model=="resnet":
            model = models.resnet.ResNet(params.dataset_name, params.pretrained).to(device)
            chkpt,model = utils.load_checkpoint('RNN/rnn_checkpoint_dir_resnet/model_best_1.pth.tar',model)
#        elif params.model=="inception":
#            model = models.inception.Inception(params.dataset_name, params.pretrained).to(device) 


        print(evaluate(model, device, val_loader, params, i))


