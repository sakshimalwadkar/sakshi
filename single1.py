class parent:
    def fun1(self):
        print("parent fun")
class child(parent):
    def fun2(self):
        print("child fun")
obj=child()
obj.fun1()
obj.fun2()