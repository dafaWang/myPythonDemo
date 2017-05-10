# -*- coding: utf-8 -*-
mydict = {'a':40,'b':50,'c':60}
print(mydict)
print(mydict['b'])#根据key-->b来查找value
print('d' in mydict)#查看d是否是mydict中的一个key
print('a' in mydict)#查看a是否是mydict中的一个key

print(mydict.get('a','没找到a'))
print(mydict.get('d','没找到d'))#通过get()方法来查找对应key值的value,没找到就默认输出后面的

if 'd' in mydict:
	#先判断'd'是否在字典mydict中,如果存在就删除key为'd'的value
	mydict.pop('d')
	print(mydict)
elif 'a' in mydict:
#先判断'd'是否在字典mydict中,如果存在就删除key为'd'的value
	mydict.pop('a')
	print(mydict)
