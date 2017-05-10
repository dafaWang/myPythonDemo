# -*- coding: utf-8 -*-
def power(a,b=1):#计算b个a相乘,b为位置参数,默认是1
	sum = 1
	while b>0:
		sum = sum * a
		b = b -1
	return sum
#单例
def add_end(L = None):
	if L is None:
		L = []
		L.append('初始化')
	else:
		L.append('end')
	return L

x = int(input('请输入第一个数'))
y = int(input ('请输入第二个数'))
if (not isinstance(x,int)) | (not isinstance(y,int)):
	print('输入错误')
else:
	print(str(y)+'个'+str(x)+'相乘 = %d'%power(x,y))
print('--------------------------------------------------')
print(add_end([1]))
print(add_end())

#可变参数::::::
def add(*nums):#在不确定参数个数的时候前面加*,想用list一样使用这个参数
	sum = 0
	for num in nums:
		sum = sum + int(num)
	return sum
mynums = input('请输入您想加的数字,用逗号隔开')
print(mynums)
numlist = mynums.split(',')
print(str(numlist)+'中的数加起来 = %d'%add(*numlist))

	
#关键字参数-->可以扩展函数功能

#定义一个person的构造方法
def person(name,age,**other):
	print('name = ',name,'age = ',age,'other = ',other)
myname = input('请输入姓名')
myage = input('请输入年龄')
person(myname,myage)
sex = input('请输入性别')
height = input ('请输入身高')
myother = {'sex':sex,'height':height}
person(myname,myage,**myother)
print('------------------------------------------------------')
#命名关键字参数-->就是参数必须有命名
def person1(name,age,*args,city='beijing',job):
#也可以写作person1(name,age,*,city='beijing',job)
	print(name,age,args,city,job)
person1(myname,myage,myother,job='haha')#由于city为默认参数,所以可以不传
#但是'haha'必须要指定job这个名字


#参数组合
#顺序:必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def fun1(a,b,c=1,*args,**argss):
	pass
def fun2(a,b,c=1,*,d,**argss):
	pass

#可变参数接收的是一个tuple,关键字参数接收的是一个dict