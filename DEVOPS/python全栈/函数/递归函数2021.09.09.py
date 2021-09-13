#冒泡排序
def popsort(data):
    for j in range(0,len(data)):
        for i in range(len(data)-j-1):
            if data[i]>data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
    return data
print(popsort([2,5,14,16,18,15,15,61,31]))
'''
函数在内部不调用其他函数，而是调用自身
'''
print(12)

import  re
text = '/dev/dadaasashks/all'
res = re.sub(r'/dev','+',text)
print(res)
        


