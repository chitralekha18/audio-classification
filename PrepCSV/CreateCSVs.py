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
parser.add_argument("--numFolds", type=int, help="number of folds for training (tho only one is used, it determines the size of the test set)")

args = parser.parse_args()

baseNames = list(set([re.search('(.+?)--*',s).group(1) for s in listdir(args.datafolder) ]) )
numTargets=len(baseNames)

#baseNames.sort()
#baseNames.reverse()
print(f'There are {numTargets} targets and their base file names in the directory are {baseNames}')



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


indices=[] # indicies of sounds in a fold
folds=args.numFolds   # number of folds
foldLength=[]         # length of a fold for each sound

for n in range(numTargets):
	indices.append([i for i, x in enumerate(target) if x == str(n)])
	print(f"length of indices[{n}] is {len(indices[0])}")
	foldLength.append(int(len(indices[n])/folds))
	print(f"Number of folds for target {n} is {foldLength[n]}")



for fold in range(folds):
	for n in range(numTargets):
		for index in indices[n][fold*foldLength[n]:fold*foldLength[n]+foldLength[n]]:
			print('class0',index)
			print(len(target),len(filenamelist),len(param))
			fout.write(filenamelist[index]+','+str(fold)+','+target[index]+','+param[index]+'\n')
fout.close()

