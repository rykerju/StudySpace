import os
import multiprocess
def ping(host):
    result = multiprocess.run(
        'ping %s &> /dev/null'%host,shell=True
    )
    return result
def main():
    for i in range(0,256):
        host = '180.101.49.%s'%i
        ret_val = ping(host)
        if ret_val:
            print(host,'DONE')
        else:
            print(host,'fail')
main()
