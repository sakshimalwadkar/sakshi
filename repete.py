def first(str1):
    for i in range(len(str1)):
        cnt=str1.count(str1[i])
        if cnt==1:
            re=str1[i]
            break
    return re
str1=input("enter the string")
ch=first(str1)
print("this character is non repeting",ch)