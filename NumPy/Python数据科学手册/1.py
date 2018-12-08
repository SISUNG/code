import numpy as np
import array

print(np.__version__)#1.14.2

L = list(range(10))
print(L)
print(type(L[0]))

L2 = [str(c) for c in L]
print(L2)
print(type(L2[0]))

L3 = [True, "2", 3.0, 4]
print([type(item) for item in L3])

L = list(range(10))
A = array.array('i', L)
print(A)

print(np.array([1, 4, 2, 5, 3]))

print(np.array([3.14, 4, 2, 3]))

print(np.array([1, 2, 3, 4], dtype = 'float32'))

print(np.array([range(i, i+3) for i in [2, 4, 6]]))#嵌套列表构成的多维数组

print(np.zeros(10, dtype=int))

print(np.ones((3, 5), dtype=float))

print(np.full((3, 5), 3.14))

print(np.arange(0, 20, 2))

print(np.linspace(0, 1, 5))

print(np.random.random((3, 3)))

print(np.random.normal(0, 1, (3,3)))

print(np.random.randint(0, 10, (3,3)))

print(np.eye(3))

print(np.empty(3))