import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x < 3)
print(x > 3)
print(x <= 3)
print(x >= 3)
print(x != 3)
print(x == 3)

print((2 * x) == (x ** 2))

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print(x)

print(np.count_nonzero(x < 6))
print(np.sum(x < 6))

print(np.sum(x < 6, axis = 1))
print(np.any(x > 8))
print(np.any(x < 0))
print(np.all(x < 10))
print(np.all(x == 6))
print(np.all(x <8, axis=1))

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
print(x)

print(x < 5)
print(x[x < 5])

A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
print(A | B)

