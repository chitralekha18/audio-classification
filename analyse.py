import matplotlib.pylab as plt

filename = "predicted_densenet_waterwind.csv"
lines = open(filename,'r').readlines()
plt.figure()
plt.subplot(2,2,1)
for line in lines:
	line_split = line.split(',')
	float_line_split = [float(i) for i in line_split]
	
