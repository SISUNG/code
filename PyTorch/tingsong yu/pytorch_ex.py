import scipy
import os
#print(dir(scipy))
print(help(scipy))

#print(os.path.split(os.path.abspath(__file__))[-1])

print(os.path.abspath(__file__))
dir = os.path.split(os.path.abspath(__file__))[:-1]#此处得到的是元组，需要提取其第一个元素

print(dir[0])
#print(str(dir))
print(os.listdir(dir[0]))#列出当前文件夹下的所有文件

