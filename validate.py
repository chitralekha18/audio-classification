import torch
import numpy as np
import pdb
from torchsummary import summary
def evaluate(model, device, test_loader,test=0):
	correct = 0
	total = 0
	conf_mat = np.zeros((2,2))

	if test:
		fout = open('predicted_.csv','w')
	
	model.eval()
	with torch.no_grad():
		for batch_idx, data in enumerate(test_loader):
			inputs = data[0].to(device)
			target = data[1].squeeze(1).to(device)
			model.model.classifier[0].register_forward_hook(model.hook)

			outputs = model(inputs)
			if test:
				for i in range(min(len(model.layeroutput),len(outputs.data))):
					fout.write(','.join(model.layeroutput[i].numpy().astype('str'))+',')
					fout.write(','.join(outputs.data[i].numpy().astype('str'))+'\n')


			_, predicted = torch.max(outputs.data, 1)
			total += target.size(0)
			correct += (predicted == target).sum().item()
			for i in range(len(target)):
				conf_mat[target[i].item(),predicted[i].item()] += 1
				

	#fout.close()
	return (100*correct/total),conf_mat
