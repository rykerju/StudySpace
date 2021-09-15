'''
高阶函数，函数可以接受另外一个函数名当作参数（如果函数的一个变量是一个函数名，则该函数
为高阶函数）
系统高阶函数：max  min  sorted
'''
list1 = [('jerry',25),('tom',17),('tony',20),('lily',18)]
m = max(list1,key = lambda x: x[1])#min和max类似
print(m)

#filter的匿名函数要求返回的必须是bool类型的值
f = filter(lambda x:x[1]>17,list1)
print(list(f)) #filter返回ide
#匿名函数和高阶函数配合可以简化代码×××××××××××××××
ma = map(lambda x:x[1]+1,list1)
print(list(ma))

from functools import reduce
r = reduce(lambda x,y:x+y,[1,2,3])
print(r)