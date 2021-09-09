import torch
import numpy as np
def evaluate(model, device, test_loader):
	correct = 0
	total = 0
	conf_mat = np.zeros((3,3))
	
	model.eval()
	with torch.no_grad():
		for batch_idx, data in enumerate(test_loader):
			inputs = data[0].to(device)
			target = data[1].squeeze(1).to(device)

			outputs = model(inputs)

			_, predicted = torch.max(outputs.data, 1)
			total += target.size(0)
			correct += (predicted == target).sum().item()
			for i in range(len(target)):
				conf_mat[target[i].item(),predicted[i].item()] += 1
				

	return (100*correct/total),conf_mat
