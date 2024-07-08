str=input("enter the string to be reversed")
def string(str):
    a=[]
    b=[]
    for i in range(len(str)):
        a.append(str[i])
    b=a.copy()
    print(a)
    b.reverse()    
    print("the reversed string",b)
string(str)