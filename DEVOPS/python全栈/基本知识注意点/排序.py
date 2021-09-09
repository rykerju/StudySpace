# 冒泡排序
import random
'''
def popsort(data:list):
    for j in range(0,len(data)):
        for i in range(0,len(data)-j-1):
            if data[i]>data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
    return data
data = popsort([10,2,1,5,4,96,45,12,54,87,36])
print(data)
'''
'''
思路可以从先确定某一个方案运行的次数开始，本题先确定了次数
'''
def popsort(data,reverse=True):
    if reverse:
        for j in range(0,len(data)):
            for i in range(0,len(data)-j-1):
                if data[i]<data[i+1]:
                    data[i],data[i+1] = data[i+1],data[i]
        return data
    for j in range(0,len(data)):
        for i in range(len(data)-j-1):
            if data[i]>data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
    return data
data = [10,2,1,5,4,96,45,12,54,87,36]
popsort(data,reverse=False)
                

