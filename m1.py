class grandfather:
    def fun1(self):
        print("hii")
class father(grandfather):
    def fun2(self):
        print("hello")
class son(father):
    def fun3(self):
        print("son")
obj=father()
obj1=son()
obj.fun2()
obj.fun1()
obj1.fun3()