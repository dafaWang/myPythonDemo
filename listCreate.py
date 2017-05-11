# -*- coding: utf-8 -*-
print('生成[1x1, 2x2, 3x3, ..., 10x10]这样的list')
list1 = [x*x for x in range(1,11)]
print(list1)
print('-----------------------------------------')
print('对上面的list筛选出偶数平方的list')
list2 = [x*x for x in list1 if x %2 == 0]
print(list2)
print('------------------------------------------')
print('把[a,b,c],和[1,2,3]两个列表随机组合生成一个新列表')
a = ['a','b','c']
b = ['1','2','3']
c = [n+m for n in a for m in b]
print(c)
print('---------------------------------------------')
print('打印所有两位数,排除含有数字7的数')
lista = list(range(0,10))
listb = list(range(0,10))
listc = [10*x+y for x in lista if x != 7 for y in listb if y!=7]
print(listc)
#print(str([10 * x + y for x in list(range(0,10)) if x != 7 for y in list(range(0,10)) if y != 7]))