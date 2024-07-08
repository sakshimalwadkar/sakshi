class student:
    def getdata(self,roll,name):
        self.roll=roll
        self.name=name
    def putdata(self):
        print(f"roll:{self.roll} name:{self.name}")
        
print("main code block")
s1=student()
s2=student()
s1.getdata(101,"abc")
s2.getdata(102,'xyz')
s1.putdata()
s2.putdata()