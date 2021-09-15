names = [1,2.1,2,1,2145,12,132,54,548,6565,454,5,88,84]
result = [name for name in names if name>56]
print(result)
#能倍5整除的组成一个列表
result1 = [name for name in names if name%5==0]
print(result1)


#练习
#[(偶数，奇数),(),()]
result2 = [(x,y) for x in range(5) if x%2==0 for y in range(10) if y%2!=0]
print(result2)

#列表1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]------>[3,6,9,5]
listtest = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
result5 = [x[2] for x in listtest]
print(result5)

keylist = ['name','age','job']
valuelist = ['jerry','power']#,'enjoylife']
dict = zip(keylist,valuelist)
print(dict)
for i in dict:
    print(i)
'''
字典生成式
'''
{item:price for item,price in zip(list1,list2)}