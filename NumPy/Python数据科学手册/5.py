import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a + b)
print(a + 5)

M = np.ones((3, 3))
print(M + a)

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
print(a)
print(b)
print(a + b)

M = np.ones((2, 3))
a = np.arange(3)
print(M + a)

a = np.arange(3).reshape((3, 1))
b = np.arange(3)

M = np.ones((3, 2))
a = np.arange(3)
print(a[: , np.newaxis].shape)
print(M + a[:, np.newaxis])
print(np.logaddexp(M, a[:, np.newaxis]))

X = np.random.random((10, 3))
Xmean = X.mean(0)
print(Xmean)
X_centered = X - Xmean
print(X_centered.mean(0))

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

import matplotlib.pyplot as plt
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')
plt.colorbar()
plt.show()#显示坐标图