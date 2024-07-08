class a:
    def add(self):
        self.a=int(input("enter the value of a"))
        self.b=int(input("enter the value of b"))
class b(a):
    def add1(self):
        print("arithmatic operations")
        print("addition",self.a+self.b)
        print("substraction",self.a-self.b)
        print("multiplication",self.a*self.b)
        print("division",self.a/self.b)
        
obj=b()
obj.add()
obj.add1()