# -*- coding: utf-8 -*-
#切片
#创建一个含有50个数字的list
mylist = list(range(50))
print(mylist)
print('---------------------------------------------')
#要取其中前15个
fro15 = mylist[:15]
print('前15个数为 : %s'%str(fro15))
#要取出后15个
beh15 = mylist[-15:]
print('后15个数为 : %s'%str(beh15))
#取出从20-30
cen10 = mylist[20:30]
print('第20-30个分别为 : %s'%str(cen10))
#前20个数,每两个取一个
jum2 = mylist[:20:2]
print('前20个数,每两个数取一个数 分别为 : %s'%str(jum2))
#第10-40个数,每4个取一个
jum4 = mylist[10:40:4]
print('第10-第40,每4个取一个数,为 %s'%str(jum4))
#复制上一个list
copyJum4 = jum4[:]
print("切片方法复制上一个list 为 %s"%str(copyJum4))

mytuple = tuple(range(10))
print(mytuple)
#取出从1-8-->每两个数中取一个
print(mytuple[1:8:2])
