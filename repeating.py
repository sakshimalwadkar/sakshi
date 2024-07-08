str=input("enter the string")
def repeat(str):
    for i in range(len(str)):
        cnt=str.count(str[i])
        if(cnt==1):
            re=str[i]
            break
    return re
n=repeat(str)
print("the non-repeating character is",n)    