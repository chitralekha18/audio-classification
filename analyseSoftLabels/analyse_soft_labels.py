import matplotlib.pylab as plt
import numpy as np
from mpl_toolkits import mplot3d

filename = 'predicted_densenet_waterwind_3_2.csv'
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
node0class0 = []
node0class1 = []
node1class0 = []
node1class1 = []
# plt.figure()
for line in lines:
    line_split = line.replace('\n','').split(',')
    line_split = [float(x) for x in line_split]
    if np.argmax(line_split[-2:]) == 0:
        label.append('tab:blue')
    else:
        label.append('tab:red')
    xaxis.append(line_split[ind1])
    yaxis.append(line_split[ind2])
    zaxis.append(line_split[ind3])
    # qaxis.append(line_split[ind4])
    class0.append(line_split[-2])
    class1.append(line_split[-1])

    if label[-1] == 'tab:blue':
        # plt.plot(xaxis[-1],yaxis[-1],'bo')
        # plt.plot(xaxis[-1], class0[-1], 'bo')
        # ax3.plot(zaxis[-1], qaxis[-1], 'bo')
        # plt.plot(class0[-1], class1[-1], 'bo')
        node0class0.append(class0[-1])
        node1class0.append(class1[-1])
    else:
        # plt.plot(xaxis[-1], yaxis[-1], 'r*')
        # plt.plot(xaxis[-1], class0[-1], 'r*')
        # ax3.plot(zaxis[-1], qaxis[-1], 'r*')
        # plt.plot(class0[-1], class1[-1], 'r*')
        node0class1.append(class0[-1])
        node1class1.append(class1[-1])
# plt.show()
print(len(label),len(xaxis),len(yaxis))
plt.scatter(xaxis,yaxis,c=label,alpha=0.5)
plt.xlabel("Dim "+str(ind1))
plt.ylabel("Dim "+str(ind2))
plt.show()

fig, ax = plt.subplots()
x_axis = [1/(1+np.exp(-x)) for x in xaxis]
y_axis = [1/(1+np.exp(-x)) for x in yaxis]
ax.scatter(x_axis,y_axis,c=label,alpha=0.5,label=label)
plt.xlabel("Dim "+str(ind1)+" sigmoid normed")
plt.ylabel("Dim "+str(ind2)+" sigmoid normed")
ax.legend()
plt.show()

# plt.figure()
z_axis = [1/(1+np.exp(-x)) for x in zaxis]
# q_axis = [1/(1+np.exp(-x)) for x in qaxis]
# plt.scatter(z_axis,q_axis,c=label,alpha=0.5)
# plt.xlabel("Dim "+str(ind1)+" sigmoid normed")
# plt.ylabel("Dim "+str(ind2)+" sigmoid normed")
# plt.show()

# plt.scatter(zaxis,qaxis,c=label,alpha=0.5)
# plt.xlabel("Dim "+str(ind1))
# plt.ylabel("Dim "+str(ind2))
# plt.show()

## 3 -d plots
plt.figure()
ax = plt.axes(projection='3d')
scatter = ax.scatter3D(xaxis, yaxis, zaxis,c=label, alpha=0.5)
plt.xlabel('dim 0')
plt.ylabel('dim 1')
ax.set_zlabel('dim 2')
plt.title('Penultimate layer outputs of (3_2) before sigmoid squashing')

plt.figure()
ax = plt.axes(projection='3d')
scatter = ax.scatter3D(x_axis, y_axis, z_axis,c=label, alpha=0.5)
plt.xlabel('dim 1')
plt.ylabel('dim 2')
ax.set_zlabel('dim 3')
plt.title('Penultimate layer outputs of (3_2) after sigmoid squashing')

ax = plt.axes(projection='3d')
scatter = ax.scatter3D(x_axis, q_axis, z_axis,c=label, alpha=0.5)
plt.xlabel('dim 0')
plt.ylabel('dim 3')
ax.set_zlabel('dim 2')
plt.title('Penultimate layer outputs of (4_2) after sigmoid squashing')


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

plt.figure()
# plt.title("Histogram of the 4 embedding dimensions")
plt.subplot(2,2,1)
plt.hist(node0class0)
plt.title('final node 0, class 0')
plt.xlim(-5,5)
plt.subplot(2,2,2)
plt.hist(node0class1)
plt.title('final node 0, class 1')
plt.xlim(-5,5)
plt.subplot(2,2,3)
plt.hist(node1class0)
plt.title('final node 1, class 0')
plt.xlim(-5,5)
plt.subplot(2,2,4)
plt.hist(node1class1)
plt.title('final node 1, class 1')
plt.xlim(-5,5)
plt.show()
plt.scatter(class0,class1,c=label,alpha=0.5)
plt.xlabel("final dimension 0")
plt.ylabel("final dimension 1")
plt.show()

plt.scatter(yaxis,zaxis,c=label,alpha=0.5)
plt.xlabel("dim 1")
plt.ylabel("dim 3")
plt.show()