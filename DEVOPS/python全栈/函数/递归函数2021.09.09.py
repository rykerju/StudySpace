#冒泡排序
def popsort(data):
    for j in range(0,len(data)):
        for i in range(len(data)-j-1):
            if data[i]>data[i+1]:
                data[i],data[i+1] = data[i+1],data[i]
    return data
print(popsort([2,5,12,2,14,16,18,15,15,61,31]))