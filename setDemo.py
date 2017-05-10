# -*- coding: utf-8 -*-
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合
s1list = [1,1,1,2,2,3,3,3,4]
print('s1list = %s'%str(s1list))
s1 = set(s1list)
print(s1)
s = set([1,2,3])
print(s)
x = input('请为set添加一个元素')
s.add(int(x))
print(s)
y = input('请为set删除一个元素')
s.remove(int(y))
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
set1 = set([1,2,3,4,5,6,7])
set2 = set([5,5,6,7,7,8,8,9,0,0])
print('set1 = %s'%str(set1))
print('set2 = %s'%str(set2))
print('set1 & set2 = %s' %str(set1 & set2))	
print('set1 | set2 = %s' %str(set1 | set2))
