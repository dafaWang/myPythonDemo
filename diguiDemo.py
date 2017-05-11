# -*- coding: utf-8 -*-
def fun1(n):
	if n == 1:
		return 1
	return n * fun1(n-1)
#上面这个是递归函数,不过因为  return 中含有*表达式,所以不属于尾递归-->会造成调用栈溢出
#尾递归:尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fun2(n):
	return fun3(n,1)
def fun3(num,result):
	if num == 1:
		return result
	return fun3(num-1,num*result)
#这样修改之后就编程了尾递归,在fun3中没有任何表达式,只是单纯的调用自己(自嗨)
x = input('选择1-->使用尾递归;选择2-->使用非尾递归  : 计算1000内的递归乘法')
if int(x)==1:
	print(fun2(4))
else:
	print(fun1(100))