# -*- coding: utf-8 -*-
#取绝对值
x = int(input('请输入一个数,取绝对值'))
print(abs(x))
y = int(input('比较两数大小,请输入其中一个数'))
z = int(input('请输入另外一个数'))
print('较大的数为 : %d'%max(y,z))

def toHex(count):
	return hex(count)
m = int(input('输入一个数字,求其十六进制表示'))
print(toHex(m))

def check(x):
	if not isinstance(x,(int,float)):
		raise TypeError('不是个数字')
	else:
		print(x)
i = input('判断输入的是否是整数或者小数')
check(i)