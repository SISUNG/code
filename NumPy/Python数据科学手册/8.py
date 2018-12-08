import numpy as np

x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))

x.sort()
print(x)

x = np.array([2, 1, 4, 3, 5])
i = np.argsort(x)
print(i)
print(x[i])

rand = np.random.RandomState(42)
X = rand.randint(0, 10, (4, 6))
print(X)

print(np.sort(X, axis=0))
print(np.sort(X, axis=1))

x = np.array([7, 2, 3, 1, 6, 5, 4])
print(np.partition(x, 3))


