# Summing Fibonacci numbers
import numpy as np
phi = (1 + np.sqrt(5)) / 2
print("Phi", phi)

n = np.log(4 * 10 ** 6 * np.sqrt(5) + 0.5)/np.log(phi)
print(n)

n = np.arange(1, n)
print(n)

fib = (phi**n - (-1/phi)**n)/np.sqrt(5)
print("First 9 Fibonacci Numbers", fib[:9])

fib = fib.astype(int)
print("Integers", fib)

eventerms = fib[fib % 2 == 0]
print(eventerms)