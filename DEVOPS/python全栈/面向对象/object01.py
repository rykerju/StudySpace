#定义类和属性（模子）
class Student:
    #类属性
    name = 'xiaowei'
    age = 2
    #魔术方法之一:前面有两个__后面有两个__称作魔术方法,系统会默认执行
    def __init__(self):
        print('------>init')

    #类的方法
    def paobu(self):
        '''
        普通方法格式：
        def 方法名（self，参数部分）
        '''
        print('开始跑步')
        print('self',self)
    
    #类方法
    '''
    1、定义方式不一样，需要加@classmethod
    2、类方法的参数不是对象而是类
    3、类方法中只可以使用类属性
    4、类中不可以使用普通方法
    作用:
    因为只能访问类属性和类方法。所以可以在创建对象之前，如果需要完成一些动作(功能)，可以使用类方法
    '''
    @classmethod
    def test(cls):
        print(cls)
    #静态方法
    '''
    静态方法
    1、静态方法无需传递参数(cls,self)
    2、也只能访问类的属性和方法，对象是无法访问的
    '''
    @staticmethod
    def static():
        print('haahh')
#使用类
xiaowei = Student()
print(xiaowei.name)
xiaowei.paobu()
print(xiaowei)
