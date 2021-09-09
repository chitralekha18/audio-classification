import glob
import os

#filename,fold,target,category,esc10,src_file,take
#1-100032-A-0.wav,1,0,dog,True,100032,A
#p_normednote_0.000_inst_0.865_iclass_2_.wav.wav
csvfile = 'RNN.csv'
fout = open(csvfile,'w')
fout.write('filename,fold,target,inst,pitch\n')
folder = 'RNNData.2p3i'
filenamelist = []
target = []
pitch = []
inst = []
for file in glob.glob(folder+'/*.wav'):
	#print(file)
	filename = file.split(os.sep)[-1]
	filenamelist.append(filename)
	target.append(filename.split('_')[-2])
	pitch.append(filename.split('_')[2])
	inst.append(filename.split('_')[4])
	
indices0 = [i for i, x in enumerate(target) if x == "0"]
indices1 = [i for i, x in enumerate(target) if x == "1"]
indices2 = [i for i, x in enumerate(target) if x == "2"]
print(len(indices0),len(indices1),len(indices2))

folds=5
i = 0
indices0foldnum = int(len(indices0)/folds)
indices1foldnum = int(len(indices1)/folds)
indices2foldnum = int(len(indices2)/folds)
for fold in range(folds):
	for index in indices0[fold*indices0foldnum:fold*indices0foldnum+indices0foldnum]:
		print('class0',index)
		print(len(target),len(filenamelist),len(inst),len(pitch))
		fout.write(filenamelist[index]+','+str(fold)+','+target[index]+','+inst[index]+','+pitch[index]+'\n')
			
		i = i+1
	for index in indices1[fold*indices1foldnum:fold*indices1foldnum+indices1foldnum]:
		print('class1',index)
		fout.write(filenamelist[index]+','+str(fold)+','+target[index]+','+inst[index]+','+pitch[index]+'\n')
		i = i+1
	for index in indices2[fold*indices2foldnum:fold*indices2foldnum+indices2foldnum]:
		print('class2',index)
		fout.write(filenamelist[index]+','+str(fold)+','+target[index]+','+inst[index]+','+pitch[index]+'\n')
		i = i+1
	

fout.close()

