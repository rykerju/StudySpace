#魔术方法
#https://www.cnblogs.com/zhangboblogs/p/7860929.html
#__init__:初始化魔术方法
#出发实际：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
import sys


class Person:
    a = 3
    def __init__(self,name):
        print("------>init")
        self.name = name

    #其实就是一个外部包装，在创建对象之前会做的事情
    '''
    def __new__(self):
        print(id(Person))
        print("------>new")
        #返回一个地址后创建对象的过程才会开始
        return object.__new__(self)
        #super(Person, self)__new__(*args, *args)
    '''
    #当类被当作函数（加括号）时默认调用
    def __call__(self):
        print("------->call")

    #删除地址的引用
    #垃圾回收机制
    def __del__(self):
        print("------->del")

    #将对象作为字符串返回回来
    def __str__(self):
        return self.name
'''
p = Person()
print("被引用了{}次".format(sys.getrefcount(p)))#
p1 = p
p2 = p
#此处引用了两次
print("被引用了{}次".format(sys.getrefcount(p)))#
del p1
del p2
print('删除p1p2后打印:{}'.format(p))

print("被引用了{}次".format(sys.getrefcount(p)))#
print(p.a)
p()

'''
p1 = Person('jerry')
print(p1)