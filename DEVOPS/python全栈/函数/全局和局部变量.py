'''
要想修改函数外的全局变量需要使用global定义一下
函数内的函数调用最近一层使用nonlocal（全局变量不包含在其中）
'''
a = 300
def func():
    #a = 100

    def funcinner():
        #a = 200
        nonlocal a
        print(a)
    funcinner()
    print(a)
iner()
func()
    