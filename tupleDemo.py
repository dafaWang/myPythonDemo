# -*- coding: utf-8 -*-
tuple1 = ('a','b',['A','B'])
print(tuple1)
a = input('替换tuple中的A元素')
b = input('替换tuple中的B元素')
tuple1[2][0] = a
tuple1[2][1] = b
print('修改后的tuple 为:%s'%str(tuple1))