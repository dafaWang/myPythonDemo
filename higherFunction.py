# -*- coding: utf-8 -*-
#高阶函数就是函数作为别的函数的参数
#方法名儿也是变量-->比如python内置的求绝对值方法abs()
f = abs #将f也指向abs方法
print(f(-40))
def fun1(a,b,fun2):#将函数fun2作为参数传入函数fun1
	return fun2(a)+fun2(b)
print('------------------------------------------------------------')
print(fun1(-24,-10,f))