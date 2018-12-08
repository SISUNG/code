import numpy as np
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print('x3 ndim: ', x3.ndim)
print('x3 shape: ', x3.shape)
print('x3 size: ', x3.size)

print('dtype: ', x3.dtype)#不同计算机得到的结果可能不同

print('itemsize: ', x3.itemsize, 'bytes')#不同计算机得到的结果可能不同
print('nbytes: ', x3.nbytes, 'bytes')

print(x1)
print(x1[0])
print(x1[4])
print(x1[-1])
print(x1[-2])

print(x2)
print(x2[0, 0])
print(x2[2, 0])
print(x2[2, -1])

x2[0, 0] = 12
print(x2)
x1[0] = 3.14159
print(x1)

x = np.arange(10)
print(x)
print(x[:5])
print(x[5:])
print(x[4:7])
print(x[::2])
print(x[1::2])

print(x[::-1])
print(x[5::-2])

print(x2)
print(x2[:2, :3])
print(x2[:3, ::2])
print(x2[::-1, ::-1])

print(x2[:, 0])
print(x2[0, :])
print(x2[0])

#非副本视图的子数组
print(x2)
x2_sub = x2[:2, :2]
print(x2_sub)
x2_sub[0, 0] = 99
print(x2_sub)
print(x2)

#创建数组的副本
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)
x2_sub_copy[0, 0] = 42
print(x2_sub_copy)
print(x2)

grid = np.arange(1, 10).reshape((3,3))
print(grid)

x = np.array([1, 2, 3])
print(x.reshape((1, 3)))
print(x[np.newaxis, :])
print(x.reshape((3,1)))
print(x[:, np.newaxis])

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))
z = [99, 99, 99]
print(np.concatenate([x, y, z]))

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(np.concatenate([grid, grid]))#沿着第一个轴拼接

print(np.concatenate([grid, grid], axis=1))#沿着第二个轴拼接

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])
print(np.vstack([x, grid]))

y = np.array([[99],
              [99]])
print(np.hstack([grid, y]))

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

grid = np.arange(16).reshape((4, 4))

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

left, right = np.hsplit(grid, [2])
print(left)
print(right)
