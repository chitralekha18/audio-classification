import matplotlib.pylab as plt
import numpy as np

filename = 'predicted_densenet_waterwind_1_2.csv'
num_interim_nodes = 2
ind1 = 0
ind2 = 1
ind3 = 2
ind4 = 3


lines = open(filename,'r').readlines()

label = []
xaxis = []
yaxis = []
zaxis = []
qaxis = []
class0 = []
class1 = []
plt.figure()
for line in lines:
    line_split = line.replace('\n','').split(',')
    line_split = [float(x) for x in line_split]
    if np.argmax(line_split[-2:]) == 0:
        label.append(0)
    else:
        label.append(1)
    xaxis.append(line_split[ind1])
    # yaxis.append(line_split[ind2])
    # zaxis.append(line_split[ind3])
    # qaxis.append(line_split[ind4])
    class0.append(line_split[-2])
    class1.append(line_split[-1])

    if label[-1] == 0:
        # plt.plot(xaxis[-1],yaxis[-1],'bo')
        plt.plot(xaxis[-1], class0[-1], 'bo')
        # ax3.plot(zaxis[-1], qaxis[-1], 'bo')
        # plt.plot(class0[-1], class1[-1], 'bo')
    else:
        # plt.plot(xaxis[-1], yaxis[-1], 'r*')
        plt.plot(xaxis[-1], class0[-1], 'r*')
        # ax3.plot(zaxis[-1], qaxis[-1], 'r*')
        # plt.plot(class0[-1], class1[-1], 'r*')
plt.show()
print(len(label),len(xaxis),len(yaxis))
plt.scatter(xaxis,yaxis,c=label,alpha=0.5)
plt.xlabel("Dim "+str(ind1))
plt.ylabel("Dim "+str(ind2))
plt.show()

plt.scatter(class0,xaxis,c=label,alpha=0.5)
plt.xlabel("Dim "+"class 0")
plt.ylabel("Dim "+str(ind1))
plt.show()

plt.scatter(class1,xaxis,c=label,alpha=0.5)
plt.xlabel("Dim "+"class 1")
plt.ylabel("Dim "+str(ind1))
plt.show()

plt.figure()
plt.title("Histogram of the 4 embedding dimensions")
plt.subplot(2,2,1)
plt.hist(xaxis)
plt.subplot(2,2,2)
plt.hist(yaxis)
plt.subplot(2,2,3)
plt.hist(zaxis)
plt.subplot(2,2,4)
plt.hist(qaxis)
plt.show()

plt.scatter(class0,class1,c=label,alpha=0.5)
plt.xlabel("final dimension 0")
plt.ylabel("final dimension 1")
plt.show()

plt.scatter(yaxis,zaxis,c=label,alpha=0.5)
plt.xlabel("dim 1")
plt.ylabel("dim 3")
plt.show()