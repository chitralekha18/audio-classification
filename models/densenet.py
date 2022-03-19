import torch
import torch.nn as nn
import torchvision.models as models
import pdb

class DenseNet(nn.Module):
    def __init__(self, dataset, pretrained=True,nodes=[1,2]):
        super(DenseNet, self).__init__()
        self.layeroutput = []
#        num_classes = 50 if dataset=="ESC" else 2
        self.model = models.densenet201(pretrained=pretrained)
        if len(nodes)==2:
            self.model.classifier = nn.Sequential(nn.Linear(1920,nodes[0]),nn.Linear(nodes[0],nodes[1]))
        else:
            self.model.classifier = nn.Linear(1920, nodes[0])
#        self.model.classifier[0].register_forward_hook(hook)
#        self.model.classifier = nn.Linear(1920, num_classes)
        
    def forward(self, x):
        output = self.model(x)
        return output

    def hook(self,module,input,output): 
        self.layeroutput.append(output)
