a=int(input("enter the first number"))
b=int(input("enter the first number"))
c=int(input("enter the first number"))
if (a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
     print("b is greter")
elif(a==b and b==c ):
    print("all are equal")
elif(a==b and b<c):
    print(" a and b are same and c is smaller")
elif(b==c and b<a):
    print(" b and c are same and a is smaller")
elif(a==c and b<a):
    print("a and c are equal and b is smaller")
else:
    print("c is greater")
   