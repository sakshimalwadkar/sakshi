import pandas as pd
s=pd.Series([1,2,3,5,4])
print(s)
data={'a':[1,2,3],'b':[4,5,6]}
df=pd.DataFrame(data)
print(df)
#pandas series
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)
#pandas series-labels
my=pd.Series(a)
print(my[0])
#pandas series-create tables
m=pd.Series(a,index=["x","y","z"])
print(m)
