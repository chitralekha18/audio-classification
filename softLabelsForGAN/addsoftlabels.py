import json
import numpy as np
import sys

##
# python addsoftlabels.py <predicted_*.csv> <testfilelist CSV> <original_GANjson> <output_json_withsoftlabels>
# example: 
# python addsoftlabels.py predicted_densenet_waterwind_3_2.csv waterwind_test.csv nsjson_modified.json nsjson_modified_softclasslabels.json
##
def sigmoid(val):
    return 1/(1+np.exp(-val))

if __name__ == "__main__":
    predictedsoftlabelsCSV = sys.argv[1]
    filelistCSV = sys.argv[2]
    original_json = sys.argv[3]
    output_json = sys.argv[4]

    # Opening JSON file
    f = open(original_json)
    data = json.load(f)

    filelist = open(filelistCSV,'r').readlines()[1:]

    softlabel_files = [predictedsoftlabelsCSV]
    for softlabelfile in softlabel_files:
        lines = open(softlabelfile,'r').readlines()
        numparams = int(softlabelfile.replace('.csv','').split('_')[-2]) + int(softlabelfile.replace('.csv','').split('_')[-1])
        base_key = 'softlabel_'+softlabelfile.replace('.csv','').split('_')[-2]+'_'+softlabelfile.replace('.csv','').split('_')[-1]+'_'

        

        if len(lines)!= len(filelist):
            print("Error!")
            break

        for lineno in range(len(lines)):
            filename = filelist[lineno].split(',')[0].replace('.wav','')
            softvals = list(map(float, lines[lineno].replace('\n','').split(',')))

            for param_id in range(numparams):

                key = base_key+str(param_id)

                data[filename][key] = round(sigmoid(softvals[param_id]),3)

    with open(output_json, "w") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)

