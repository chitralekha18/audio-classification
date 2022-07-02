import glob
import os
import argparse
import os
from os import listdir
from os.path import isfile, join
import re

parser = argparse.ArgumentParser()
parser.add_argument("--csvfile", type=str, help="name of output csv file", default='outputcsv')
parser.add_argument("--datafolder", type=str, help="path to foler of aduio data")
parser.add_argument("--trainfolds", type=int, help="number of folds for training (tho only one is used, it determines the size of the test set)")

args = parser.parse_args()

baseNames = list(set([re.search('(.+?)--*',s).group(1) for s in listdir(args.datafolder) ]) )
#baseNames.sort()
#baseNames.reverse()
print(f'Base file names in directory are {baseNames}')



#filename,fold,target,category,esc10,src_file,take
#1-100032-A-0.wav,1,0,dog,True,100032,A
#DSWind--strength-01.00--c-02.wav

csvfile = args.csvfile # 'waterwind_test.csv'


fout = open(csvfile,'w')
fout.write('filename,fold,target,param\n')
folder=args.datafolder #folder = '/data07/chitra/workspace/data/WaterWind2/audio'
filenamelist = []
target = []
param = []
inst = []

nameCounter=0
for baseName in baseNames :
	for file in glob.glob(folder+'/'+baseName+'*.wav'):
		#print(file)
		filename = file.split(os.sep)[-1]
		param.append(str(float(filename.split('--')[1].split('-')[1])))
		filenamelist.append(filename)
		target.append(str(nameCounter)) 
	nameCounter+=1



	
indices0 = [i for i, x in enumerate(target) if x == "0"]
indices1 = [i for i, x in enumerate(target) if x == "1"]
print(len(indices0),len(indices1))

folds=args.trainfolds
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

