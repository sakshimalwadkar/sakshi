def add(x,y):
    return x+y
a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
d=int(input("enter the d value")) 
e=add(a,b)
f=add(c,d)    
print("add a+b",e)
print("add c+d",f)
print("add a+b+c+d",add(e,f))