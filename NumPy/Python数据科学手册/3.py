import numpy as np
from scipy import special

np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
print(compute_reciprocals(values))

print(np.arange(5) / np.arange(1, 6))

x = np.arange(9).reshape((3, 3))
print(2 ** x)

x = np.arange(4)
print('x =', x)
print('x+5 =', x + 5)
print('x-5 =', x - 5)
print('x * 2 =', x * 2)
print('x / 2 =', x / 2)
print('x // 2 =', x // 2)
print(np.add(x, 2))

x = np.array([-2, -1, 0, 1, 2])
print(abs(x))
print(np.absolute(x))
print(np.abs(x))

x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print(np.abs(x))

theta = np.linspace(0, np.pi, 3)
print('theta = ', theta)
print('sin(theta) = ', np.sin(theta))
print('cos(theta) = ', np.cos(theta))
print('tan(theta) = ', np.tan(theta))

x = [-1, 0, 1]
print('x = ', x)
print('arcsin(x) = ', np.arcsin(x))
print('arccos(x) = ', np.arccos(x))
print('arctan(x) = ', np.arctan(x))

x = [1, 2, 3]
print('x = ', x)
print('e^x = ', np.exp(x))
print('2^x = ', np.exp2(x))
print('3^x = ', np.power(3, x))

x = [1, 2, 4, 10]
print('x = ', x)
print('ln(x) = ', np.log(x))
print('log2(x) = ', np.log2(x))
print('log10(x) = ', np.log10(x))

x = [0, 0.001, 0.01, 0.1]
print('exp(x) - 1 = ', np.expm1(x))
print('log(1+x) = ', np.log1p(x))

#Gamma函数
x = [1, 5, 10]
print('gamma(x) = ', special.gamma(x))
print('ln|gamma(x)| = ', special.gammaln(x))
print('beta(x, 2) = ', special.beta(x, 2))

#误差函数（高斯积分）
#它的实现和它的逆实现
x = np.array([0, 0.3, 0.7, 1.0])
print('erf(x) = ', special.erf(x))
print('erfc(x) = ', special.erfc(x))
print('erfinv(x) = ', special.erfinv(x))

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)

y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)

x = np.arange(1, 6)
print(np.add.reduce(x))
print(np.multiply.reduce(x))
print(np.add.accumulate(x))
print(np.multiply.accumulate(x))

#外积，获得两个不同输入数组所有元素对的函数运算结果
x = np.arange(1, 6)
print(np.multiply.outer(x, x))