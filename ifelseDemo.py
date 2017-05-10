# -*- coding: utf-8 -*-
height = input('请输入您的身高(单位m)')
weight = input('请输入您的体重(单位kg)')
bmi = float(weight)/float(height)/float(height)
if bmi<18.5:
	print('过轻')
elif 18.5<=bmi<25:
	print('正常')
elif 25<=bmi<28:
	print('过重')
elif 28<=bmi<32:
	print('肥胖')
elif bmi>=32:
	print('严重肥胖')