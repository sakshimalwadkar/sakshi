n=int(input("enter number from 1 to n:"))
a=[]
print("enter the number from 1 to",n,":-")
for i in range(n):
    no=int(input("enter the number:"))
    a.append(no)
    a.sort()
print(a)
missing=1
for i in range(len(a)-1):
    if(a[i]!=missing):
        print("missing number is:",missing)
        missing+=1
    missing+=1  