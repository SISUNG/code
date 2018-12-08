import matplotlib.pyplot as plt
import seaborn; seaborn.set()

import numpy as np
L = np.random.random(100)
print(sum(L))
print(np.sum(L))

M = np.random.random((3, 4))
print(M)
print(M.sum())
print(M.min(axis=0))
print(M.max(axis=1))

heights = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183,
                    193, 178, 173, 174, 183, 183, 168, 170, 178, 182, 180, 183, 178, 182, 188,
                    175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185])
#print(len(list(heights)))
print('Mean height: ', heights.mean())
print('Standard deviation: ', heights.std())
print('Minimum height: ', heights.min())
print('Maximum height: ', heights.max())

print('25th percentile: ', np.percentile(heights, 25))
print('Median: ', np.median(heights))
print('75th percentile: ', np.percentile(heights, 75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height(cm)')
plt.ylabel('number')
plt.show()