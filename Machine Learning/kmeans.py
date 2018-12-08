import numpy as np
from sklearn.datasets import make_blobs
import sklearn.datasets as sd
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors

import pandas as pd

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

"""
data, target = make_blobs(n_samples=100, n_features=2, centers=3)
plt.scatter(data[: , 0], data[: , 1], c = target)
plt.show()
"""

N = 1500
centers = 4
data1, y1 = sd.make_blobs(N, n_features=2, centers=centers, random_state=28)

data2,y2 = sd.make_blobs(N,n_features=2,centers=centers,random_state=28)

data3 = np.vstack((data1[y1==0][:200],data1[y1==1][:100],data1[y1==2][:10],data1[y1==3][:50]))
y3 = np.array([0]*200+[1]*100+[2]*10+[3]*50)

km = KMeans(n_clusters=centers, random_state=28)
km.fit(data1, y1)
y_hat = km.predict(data1)

print("所有样本点距离聚簇中心点的总样本和", km.inertia_)
print("每个样本点距离聚簇中心点的平均距离", km.inertia_/N)
print("聚簇中心点的坐标", km.cluster_centers_)

def expand_border(a, b):
    d = (b - a)* 0.1
    return a - d, b + d

cm = mpl.colors.ListedColormap(list('rgbmyc'))
plt.figure(figsize=(15, 9), facecolor='w')
plt.subplot(241)
plt.scatter(data1[:, 0], data1[:, 1],c = y1, s = 20, cmap=cm, edgecolors=None)

x1_min,x2_min = np.min(data1,axis=0)
x1_max,x2_max = np.max(data1,axis=0)
x1_min,x1_max = expand_border(x1_min,x1_max)
x2_min,x2_max = expand_border(x2_min,x2_max)
plt.xlim((x1_min,x1_max))
plt.ylim((x2_min,x2_max))
plt.title("原始数据")
plt.grid(True)

plt.subplot(242)
plt.scatter(data1[:, 0], data1[:, 1], c=y_hat, s=30, cmap=cm, edgecolors='none')
plt.xlim((x1_min, x1_max))
plt.ylim((x2_min, x2_max))
plt.title(u'K-Means算法聚类结果')
plt.grid(True)

plt.show()







