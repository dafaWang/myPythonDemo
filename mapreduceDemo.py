# -*- coding: utf-8 -*-
from functools import reduce
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def add(a):
	return a+3
l = [1,2,3,4,5,6,7,8]
print(list(map(add,l)))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add2(a,b):
	return a + b
print(reduce(add2,l))

def addstr(a,b):
	return str(a+b)
l2 = ['h','e','l','l','o']
print(reduce(addstr,l2))
print('---------------------------------------------------------')

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('-------------------------------------------------------------')
#编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
	return reduce(qiuji,L)
def qiuji(a,b):
	return a*b

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))