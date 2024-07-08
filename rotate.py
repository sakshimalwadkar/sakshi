str=[]
no=int(input("enter the total number of inputs"))
n=int(input("enter the number of rotation"))
for i in range(no):
    num=int(input("enter the number"))
    str.append(num)
print(str)
for i in range(n):
    if (i<n):
        str.append(str[0])
        str.pop(0)
        i=0
        if(i>n):
            break
print(str)            