'''
通过列表生成式，我们可以创建一个列表
但是，受内存资源限制，列表容量肯定是有限的
不必创建完整的list，大量节省空间，一边循环一边计算的机制称之为生成器：
generator
'''
#制作一个生成器的方式一（）
generator1 = (name*3 for name in range(10))
for i in range(5):
    print(generator1.__next__())
    #每次调用一个next就会产生一个元素
    #方式一：generator.__next__()
    #方式二：next(generator)
    #当生成器产生的元素全部结束，就会报错


#定义生成器的方式二：借助函数完成
'''
具体方法：
1、定义一个函数，函数中使用yield
2、调用函数，接受调用的结果
3、借助next()，__next__()
'''
#例：
def func():
    n = 1
    while True:
        n = n+1
        #print(n)
        yield  n#此时就变成了生成器
print(func().__next__())
#斐波纳契数列
def fibonach(len):
    a,b = 0,1
    n=0
    while n<len:
        yield b
        a,b = b,a+b
        n = n+1
g = fibonach(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))



#生成器里面有一个send方法，用到的时候再好好看
#temp = yield 3 #这句话的执行顺序是，return 3 然后暂停 然后传值
#g.send()传值必须先传g.send(None)
def task1():
    for i in range(10):
        yield '我在搬第{}块砖'.format(i)
def task2():
    for i in range(10):
        yield '我在听第{}首歌'.format(i)
g1 = task1()
g2 = task2()
while True:
    print(g1.__next__())
    print(g2.__next__())
