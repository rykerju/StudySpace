#定义类和属性（模子）
class Student:
    #类属性
    name = 'xiaowei'
    age = 2
    #类的方法
    def paobu(self):
        '''
        普通方法格式：
        def 方法名（self，参数部分）
        '''
        print('开始跑步')
        print('self',self)
#使用类
xiaowei = Student()
print(xiaowei.name)
xiaowei.paobu()
print(xiaowei)
