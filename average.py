array=[1,2,4,5]
print(array)
def average(array):
    a=0
    for i in array:
        a+=i
    print("the average of array is",a/len(array))
average(array)