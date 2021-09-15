'''
闭包：
1、有嵌套函数
2、内部函数调用了内部函数变量
3、返回值为内部函数
    满足如上的条件的函数就是闭包函数
'''
a = 3
print(id(a))
def func():
    global a
    a = 4
    print(id(a))
func()