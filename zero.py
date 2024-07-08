str=[]
no=int(input("enter the total number of inputs"))
for i in range(no):
    num=int(input("enter the number"))
    str.append(num)
print(str)
for i in range(len(str)):
    for j in range(len(str)):
        if(str[i]==0):
            str.append(str[i])
            str.pop(i)
print(str)