import numpy as np

rand = np.random.RandomState(42)
x = rand.randint(100, size=10)
print(x)

print([x[3],x[7], x[2]])
print(type([x[3],x[7], x[2]]))
#<class 'list'>

ind = [3, 7, 4]
print(x[ind])
print(type(x[ind]))
#<class 'numpy.ndarray'>

ind = np.array([[3, 7],
                [4, 5]])
print(x[ind])

x = np.arange(12).reshape((3, 4))
print(x)

row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print(x[row, col])

print(x[row[:, np.newaxis], col])

print(row[:, np.newaxis] * col)

x = np.arange(12).reshape((3, 4))
print(x[2, [2, 0, 1]])
print(x[1:, [2, 0, 1]])

mask = np.array([1, 0, 1, 0], dtype= bool)
print(x[row[:, np.newaxis], mask])

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
x = rand.multivariate_normal(mean, cov, 100)
print(x.shape)
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
plt.scatter(x[:, 0], x[:, 1])
#plt.show()

indices = np.random.choice(x.shape[0], 20, replace=False)
print(indices)

selection = x[indices]
print(selection.shape)
plt.scatter(x[:, 0], x[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
            facecolor='none', edgecolor='b', s = 200)
#plt.show()
x = np.arange(10)
i = np.array([2, 1, 8, 4])
x[i] = 99
print(x)
x[i] -= 10
print(x)

x = np.zeros(10)
x[[0, 0]] = [4, 6]
print(x)

i = [2, 3, 3, 4, 4, 4]
x[i] += 1
print(x)

x = np.zeros(10)
np.add.at(x, i, 1)
print(x)

np.random.seed(42)
x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
i = np.searchsorted(bins, x)
np.add.at(counts, i, 1)
plt.plot(bins, counts, linestyle='steps')
plt.show()

plt.hist(x, bins, histtype='step')
plt.show()


