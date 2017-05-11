# -*- coding: utf-8 -*-
#python中,一边循环一边计算的机制叫做生成器
list1 = [ x for x in range(10)]
print(list1)

#生成器的实现方法一::::::
generator = (x for x in range(10))
print(generator)
for x in generator:
	print(x)
print('---------------------------------------------------')

#生成器的实现方法二:::::函数实现
#斐波拉契数列1, 1, 2, 3, 5, 8, 13, 21, 34
def fib(x):
	n,a,b = 0,0,1
	while n < x:
		yield b
		n = n+1
		a,b = b,a+b
	return 'haha'
f = fib(6)
print('斐波拉契数列')
for x in f:
	print(x)

print('-------------------------------------------------')
print('杨辉三角形 : ')
def yanghui():
	l = [1]
	while 1:
		yield l
		l = [1] + [l[x]+l[x+1] for x in range(len(l)-1)]+[1]
n = 0
for t in yanghui():
	print(t)
	n = n+1
	if n>10:
		break

