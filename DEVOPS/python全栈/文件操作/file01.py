#文件操作
'''
文件上传
保存log
系统函数open():
'''
stream = open(r'test.txt', mode='r', encoding='utf-8') #字符前面的r是防止路径字符串转义
container = stream.read(2)
container1 = stream.read(3)
#同一段会接着上次的内容读取
container2 = stream.readline()
container3 = stream.readlines()
#很占内存，不推荐使用


'''
读文件尽量要用循环
'''
'''
如果是图片，则不能使用默认的读取方式，应该使用文件对应的，其实就是指定文件类型
'''
import os
'''
os.path.split(path)将文件绝对路径下此文件和上层目录分割开
os.path.splittext(path)将文件名的扩展名提取出来
os.getsize(path)获取文件大小，单位为字节

os.path.join(os.getcwd(),'file','a1.jpg')拼接路径
os.listdir(path)返回path路径下所有的文件和和文件夹,来浏览文件夹下的文件名
os.mkdir(path)创建文件夹
os.rmdir(path)删除文件夹，只能删除空文件夹
os.removedirs()
os.remove(path)删除文件
os.path.exists(path)判断有没有这个文件夹
os.chdir
'''
print(os.path.dirname('../'))