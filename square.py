def square(array):   
    sq=[]
    for i in range(len(array)):
      s=array[i]*array[i]
      sq.append(s)
    return sq
array=[1,2,3,4,5]
print("squared list of array",square(array))    