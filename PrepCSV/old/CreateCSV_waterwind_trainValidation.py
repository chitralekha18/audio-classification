import glob
import os

#filename,fold,target,category,esc10,src_file,take
#1-100032-A-0.wav,1,0,dog,True,100032,A
#DSWind--strength-01.00--c-02.wav
csvfile = 'waterwind.csv'
fout = open(csvfile,'w')
fout.write('filename,fold,target,param\n')
folder = '/data07/chitra/workspace/data/WaterWind2/audio'
filenamelist = []
target = []
param = []
inst = []
for file in glob.glob(folder+'/waterfill*.wav'):
	#print(file)
	filename = file.split(os.sep)[-1]
	param.append(str(float(filename.split('--')[1].split('-')[1])))
	filenamelist.append(filename)
	target.append('0') #water
for file in glob.glob(folder+'/DSWind*.wav'):
        #print(file)
	filename = file.split(os.sep)[-1]
	param.append(str(float(filename.split('--')[1].split('-')[1])))
	filenamelist.append(filename)
	target.append('1') #wind


	
indices0 = [i for i, x in enumerate(target) if x == "0"]
indices1 = [i for i, x in enumerate(target) if x == "1"]
print(len(indices0),len(indices1))

folds=5
i = 0
indices0foldnum = int(len(indices0)/folds)
indices1foldnum = int(len(indices1)/folds)
for fold in range(folds):
	for index in indices0[fold*indices0foldnum:fold*indices0foldnum+indices0foldnum]:
		print('class0',index)
		print(len(target),len(filenamelist),len(param))
		fout.write(filenamelist[index]+','+str(fold)+','+target[index]+','+param[index]+'\n')
			
		i = i+1
	for index in indices1[fold*indices1foldnum:fold*indices1foldnum+indices1foldnum]:
		print('class1',index)
		fout.write(filenamelist[index]+','+str(fold)+','+target[index]+','+param[index]+'\n')
		i = i+1

fout.close()

