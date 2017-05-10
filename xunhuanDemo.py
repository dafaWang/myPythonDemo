# -*- coding: utf-8 -*-
count = 0
x = input('请输入一个数字,计算从0到此数之和')
for x in range(int(x)):
	count = count + x
print('count = %d'%count)
count1 = 0
index = 0
while index < int(x):
	index = index + 1
	count1 = count1 + index
print('count1 = %d'%count1)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print('hello ,%s'%x)
print('----------------------------------------------------')
n = 1
while n < 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END') 
print('------------------------------------------------------')
m = 0
while m < 10:
	m = m + 1
	if m % 2 == 0:
		continue
	print(m)
print('------------------------------------------------------')
# o = 0
# while True:
# 	o = o + 1
# 	print(o)	#这是一个死循环

