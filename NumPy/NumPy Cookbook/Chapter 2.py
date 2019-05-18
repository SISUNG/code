# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:17:20 2019

@author: 23842
"""


"""
# Creating views and copies
import scipy.misc
import matplotlib.pyplot as plt
lena = scipy.misc.ascent()
acopy = lena.copy() # 深复制，变化不会影响原数据
aview = lena.view() # 浅复制，变化会影响原数据，相当于[:]
plt.subplot(221)
plt.imshow(lena)

plt.subplot(222)
plt.imshow(acopy)

plt.subplot(223)
plt.imshow(aview)

aview.flat = 0
plt.subplot(224)
plt.imshow(aview)

plt.show()
"""


"""
# Flipping Lena
import scipy.misc
import matplotlib.pyplot as plt

lena = scipy.misc.ascent()

plt.subplot(221)
plt.title('Original')
plt.axis('off')
plt.imshow(lena)

plt.subplot(222)
plt.title('Flipped')
plt.axis('off')
plt.imshow(lena[:,::-1])

plt.subplot(223)
plt.title('Sliced')
plt.axis('off')
plt.imshow(lena[:lena.shape[0]//2, :lena.shape[1]//2])

mask = lena % 2 == 0
masked_lena = lena.copy()
masked_lena[mask] = 0
plt.subplot(224)
plt.title('Masked')
plt.axis('off')
plt.imshow(masked_lena)
plt.show()

import numpy as np
a = np.array([[True, False],
     [False, True]])
b = np.array([[1,2],
     [3,4]])
b[a] = 0
print(b)
"""


"""
# Fancy indexing
import scipy.misc
import matplotlib.pyplot as plt
lena = scipy.misc.ascent()
xmax = lena.shape[0]
ymax = lena.shape[1]
lena[range(xmax), range(ymax)] = 0
lena[range(xmax-1, -1, -1), range(ymax)] = 0
plt.imshow(lena)
plt.show()
"""


"""
# Indexing with a list of locations
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
lena = scipy.misc.ascent()
xmax = lena.shape[0]
ymax = lena.shape[1]

def shuffle_indices(size):
    arr = np.arange(size)
    np.random.shuffle(arr)
    
    return arr

xindices = shuffle_indices(xmax)
yindices = shuffle_indices(ymax)
plt.imshow(lena[np.ix_(xindices, yindices)])    
"""


"""
# Indexing with Booleans
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

lena = scipy.misc.ascent()

def get_indices(size):
    arr = np.arange(size)
    return arr % 4 == 0

lena1 = lena.copy()
xindices = get_indices(lena.shape[0])
yindices = get_indices(lena.shape[1])
lena1[xindices, yindices] = 0
plt.subplot(211)
plt.imshow(lena1)

lena2 = lena.copy()
lena2[(lena > lena.max() / 4) & (lena < 3 * lena.max() / 4)] = 0
plt.subplot(212)
plt.imshow(lena2)
plt.show()
"""


# Broadcasting arrays
import scipy.io.wavfile
import matplotlib.pyplot as plt
from urllib import request
import numpy as np

response = request.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
print(response.info())

WAV_FILE = 'smashingbaby.wav'
filehandle = open(WAV_FILE, 'wb')
filehandle.write(response.read())
filehandle.close()

sample_rate, data = scipy.io.wavfile.read(WAV_FILE)
print("Data type", data.dtype, "Shape", data.shape)

plt.subplot(211)
plt.title("Original")
plt.plot(data)

newdata = data * 0.2
newdata = newdata.astype(np.uint8)
print("Data type", newdata.dtype, "Shape", newdata.shape)
scipy.io.wavfile.write("quiet.wav", sample_rate, newdata)
plt.subplot(212)
plt.title("Quiet")
plt.plot(newdata)
plt.show()
