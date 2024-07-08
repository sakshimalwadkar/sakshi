a=[]
n=int(input("enter the total number of element in an array"))
for i in range(n):
    no=int(input("enter the number"))
    a.append(no)
max_proc=0
for i in range(len(a)):
    inc=i+1
    for inc in range(len(a)-1):
        mul=a[i]*a[inc]
        if (mul>max_proc):
            max_proc=mul
print("maximum product of an array",max_proc)            