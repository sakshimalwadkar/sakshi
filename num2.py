import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
#shape of the array
print(arr1.shape)
print(arr2.shape)
#number of dimensions
print(arr1.ndim)
print(arr2.ndim)
#number of elements in the array
print(arr1.size)
print(arr2.size)
#datatype of the element
print(arr1.dtype)
print(arr2.dtype)
#array of zeros
zeros=np.zeros((3,3))
print(zeros)
#array of ones
ones=np.ones((2,4))
print(ones)
#identity matrix
identity=np.eye(3)
print(identity)
#array with random values
random=np.random.random((2,2))
print(random)
#array with range values
range_arr=np.arange(1,10)
print("\n range array",range)
#array with linearly spaced values
linspace=np.linspace(0,1,5)
print("linearly spaced array",linspace)
#array manipulation
reshaped=range_arr.reshape((3,3))
print("\n reshaped array",reshaped)
flattened=reshaped.flatten()
print("\n falttened array",flattened)
transposed=reshaped.transpose()
print("\n transposing array",transposed)
#Arithamtic operations
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print("\n element wise addition",a1+a2)
print("\n elemet wise multiplication",a1*a2)
print("\n element wise power",a1**a2)
print("\n element wise substraction",a1-a2)
#statistical and mathematical methos
print("sum=",a1.sum())
print("mean=",a1.mean())
print("standard deviations",a1.std())
print("varience",a1.var())
print("minimum",a1.min())
print("maximum",a1.max())
print("cumulative sum",a1.cumsum())
print("cumulative product",a1.cumprod())
#logical operations
b=np.array([True,False,True])
print("\n all elements true",b.all())
print("any element true",b.any())
print("indices of non-zero element",np.nonzero(arr1))
#sorting,searching,counting
unsorted=np.array([1,2,3])
sorted=np.sort(unsorted)
print("\n sorted array",sorted)
print("Indices that would sort the array",np.argsort(unsorted))
print("index of max value",np.argmax(unsorted))
print("index of min value",np.argmin(unsorted))
print("count of non-zero elements",np.count_nonzero(unsorted))
#copy and view
copy=a1.copy()
view=a1.view()
print("\n copied array",copy)
print("\n viewed array",view)
#other useful methods
#clipping values
clip=a1.clip(2,4)
print("\n clipped array",clip)
#repeating elements
repeat=a1.repeat(2)
print("repeated array",repeat)
#taking element
taken=a1.take([0,2])
print("taken elements",taken)
#putting values into specified indices
put=a1.copy()
put.put([0,2],[10,4])
print("array after putting values",put)
#getting the diagonal of array
diagonal=reshaped.diagonal()
print("diagonal of reshaped array",diagonal)