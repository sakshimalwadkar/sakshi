
class parent:
    def fun1(self):
        print("hello world")
class  parent1:
    def fun2(self):
        print("hii")
class child(parent,parent1):
    def fun3(self):
        print("hello world")
obj=child()
obj.fun1()
obj.fun2()
obj.fun3()
