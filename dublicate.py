array=[10,1,2,3,3,5,6]
print("original list of array",array)
result=[]
for i in array:
    if i not in result:
        result.append(i)
print("array after removing dublicate element",result)        