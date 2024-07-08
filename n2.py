n=int(input("enter the number"))
no=n
rem=0
r=0
rem=no%10
print("last number",rem)
while(n>10):
    r=no/10 
    no=no/10
    print("reverse number",int(r))
    