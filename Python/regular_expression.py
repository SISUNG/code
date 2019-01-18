import os
import os.path
import re#正则表达式地

#print(os.getcwd())#返回当前目录
#a = os.getcwd()
#print(os.listdir(a))#返回当前目录下的文件名和子目录列表

#b = os.listdir(a)
#print(os.stat(b[2]))#返回当前目录下的第二个文件的信息

#print(os.path.join(os.getcwd(), b[2]))#返回当前目录下的第二个文件的绝对路径
#c = os.path.join(os.getcwd(), b[2])#返回当前目录下的第二个文件的绝对路径
#print(os.path.split(c))#将路径分割成符合当前操作系统的组成名称，返回一个元组

"""
path = 'D:\\研究'
for root, dirs, files in os.walk(path):
    #print(root)#保存目录路径的字符串
    #print(dirs)#返回root目录下的子目录列表
    #print(files)#返回每个非目录文件的一个列表
    for file in files:
        path = os.path.join(root, file)
        path = os.path.normcase(path)
        if re.search(r'.*\.pdf', path):
            print(path)
"""

"""
s = ('xxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxya')
a = filter((lambda s: re.match(r"xxx", s)), s)  # match 完全匹配
print(*a)  # xxx

a = filter((lambda s: re.search(r"xxx", s)), s)  # search 搜索
print(*a)  # xxx abcxxxabc axxxxa

a = filter((lambda s: re.search(r"x.x", s)), s)  # search 搜索,'.'匹配任意字符
print(*a)  # xxx abcxxxabc xyx x.x axxxxa

a = filter((lambda s: re.search(r"x\.x", s)), s)  # search 搜索,'\.'就是.了
print(*a)  # x.x

a = filter((lambda s: re.search(r"x.*x", s)), s)  # search 搜索,*匹配任意次数
print(*a)  # xxx abcxxxabc xyx x.x axxxxa axxya

a = filter((lambda s: re.search(r"x.+x", s)), s)  # search 搜索,+至少出现一次
print(*a)  # xxx abcxxxabc xyx x.x axxxxa

a = filter((lambda s: re.search(r"c+", s)), s)  # search 搜索,至少有一个c
print(*a)  # abcxxxabc abc

# 用[]表示要匹配的特殊字符集，用^表示非
# 要用^和$在开头和结尾表示从头到尾不包含c字符
a = filter((lambda s: re.search(r"^[^c]*$", s)), s)  # search 搜索,至少有一个c
print(*a)  # xxx xyx x.x axa axxxxa axxya
"""

import re
m = re.match('foo', 'seafood')#从字符串开始的位置匹配，成功返回匹配的对象，失败返回None
if m is not None:
    print('match-' + m.group())
m = re.search('foo', 'seafood')#match()函数从起始位开始匹配
if m is not None:
    print('search-' + m.group())

bt = 'bat|bet|bit'#匹配多个值，使用择一表达式
m = re.match(bt, 'bat')
if m is not None:
    print('1能匹配-'+ m.group())#用加号把两个字符串相加
m = re.match(bt, 'blt')
if m is not None:
    print('2能匹配-' + m.group())
m = re.match(bt, 'he bit me')
if m is not None:
    print('3能匹配-' + m.group())
m = re.search(bt, 'he bit me')
if m is not None:
    print('4能匹配-' + m.group())

#匹配任何单个字符，点号'.'除了换行符\n和非字符，都能匹配
import re
bt = '.end'
m = re.match(bt, 'bend')
if m is not None:
    print('bend能匹配-'+ m.group())
m = re.match(bt, 'end')
if m is not None:
    print('end能匹配-' + m.group())
m = re.match(bt, 'end')
if m is not None:
    print("end能匹配-" + m.group())
m = re.match(bt, '\nend')
if m is not None:
    print("\nend能匹配-" + m.group())
m = re.search(bt, 'the end.')
if m is not None:
    print("the end.能匹配-" + m.group())

#匹配小数点
bt = '3.14'
pi_bt = '3\.14'#匹配字面量的点号
m = re.match(bt, '3.14')
if m is not None:
    print('3.14能匹配-' + m.group())
m = re.match(pi_bt, '3.14')
if m is not None:
    print('精确匹配-' + m.group())
m = re.match(pi_bt, '3014')
if m is not None:
    print('3014能匹配-' + m.group())

import re
bt = "[cr][23][dp][o2]"
m = re.match(bt, 'c2po')
if m is not None:
    print('c3po能匹配-' + m.group())

bt = '\w+@\w+\.com'
mails = ['nobody@xxxcom', 'nnn@xxxs.com', 'sdhfdhfdfhj.com']
for i in range(len(mails)):
    m = re.match(bt, mails[i])
    if m is not None:
        print(m.group())

import re
m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{4})',r'\3/\1/\2','2/20/1991')
print(m)

m = re.split(':', 'sr1:str2:str3:str4')
print(m)
print('str1:str2'.split(':'))

DATA = ('Mountation View, CA 94040', 'sunnyvale, CA', 'Los Altos, 94023', 'Palo Alto CA','Cupertino 95014')
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ',datum))

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edo', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize) / 3000000000
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    #print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))

import re
reg = '(?<=95|98|NT|2000)Windows'
#(?=...)如果...跟在字符串后面才做匹配，非获取匹配；称为正向前视断言
#m = re.search(reg, '2000Windows')


import re
m = re.split(':', "str1:str2:str3")
if m is not None:
    print('匹配成功-' + m.group())


