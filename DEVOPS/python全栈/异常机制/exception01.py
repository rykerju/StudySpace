#语法错误和异常
#异常处理
'''
try:
    可能出现异常的代码
except IndexError:
    报错误一，则执行的代码
except ZeroDivisionError:
    错误二，则执行的代码
except Exception as err:
    print('出错啦',err)
    除了以上错误之外，剩下的错误全部走这里
finally:
    无论是否存在异常都会被执行的代码
    如果try内有return，则会执行完finally然后再return
'''
#抛出异常
def register():
    username = input('请输入用户名：')
    if len(username)>6:
        raise Exception('你输入的用户名太长')

register()