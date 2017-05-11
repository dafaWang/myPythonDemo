# -*- coding: utf-8 -*-
from collections import Iterable
#也就是遍历......
#list遍历
list1 = ['a','b','c','d','e']
for x in list1:
	print('list1--> ',x)
print('----------------------------------------')
#tuple遍历
tuple1 = ('1','2','3','4','5')
for x in tuple1:
	print('tuple1--> ',x)
print('----------------------------------------')
#字典遍历-->默认遍历的是key
dict1 = {'name':'dafa','age':13,'sex':'nan'}
for k in dict1:
	print('dict1-key-> ',k)
print('----------------------------------------')
#遍历value
for v in dict1.values():
	print('dict1-value-> ',v)
print('----------------------------------------')
#遍历key+value:
for k,v in dict1.items():
	print('key--value : ',k,'--',v)

print('-----------------------------------------')
#判断对象是否为可迭代对象
print('int 是否为可迭代对象? %s' %str(isinstance(3,Iterable)))
print('str 是否为可迭代对象? %s' %str(isinstance('tu',Iterable)))