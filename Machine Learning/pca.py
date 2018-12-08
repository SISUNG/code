import numpy as np
import matplotlib.pyplot as plt

x = np.array([2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1])
y = np.array([2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9])

x_mean = np.mean(x)
y_mean = np.mean(y)

x_scaled = x - x_mean
y_scaled = y - y_mean

#plt.plot(x_scaled, y_scaled, 'o')
#plt.show()

data = np.matrix([[x_scaled[idx], y_scaled[idx]]] for idx in range(len(x_scaled)))

cov = np.cov(x_scaled, y_scaled)

eig_val, eig_vec = np.linalg.eig(cov)

plt.plot(x_scaled, y_scaled, 'o',)
xmin ,xmax = x_scaled.min(), x_scaled.max()
ymin, ymax = y_scaled.min(), y_scaled.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2
plt.xlim(xmin - dx, xmax + dx)#x轴刻度
plt.ylim(ymin - dy, ymax + dy)#y轴刻度

plt.plot([eig_vec[:,0][0],0],[eig_vec[:,0][1],0], color = 'red')
plt.plot([eig_vec[:,1][0],0],[eig_vec[:,1][1],0], color = 'red')
plt.show()





