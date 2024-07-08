name=[]
roll=[]
marks=[]
def addstud():
    r=input("enter the roll no=")
    roll.append(r)
    n=input("enter the name=")
    name.append(n)
    m=input("enter the marks")
    marks.append(m)
def view():
    print("ROLL NO \tNAME \tMARKS")
    for i in range(len(roll)):
      print(roll[i],"\t",name[i],"\t",marks[i])
def update():
    froll=input("enter the find roll")
    for i in range(len(roll)):
        if(roll[i]==froll):
          uroll=input("enter the roll no=")
          uname=input("enter the name=")
          umarks=input("enter the marks")
          roll[i]=uroll
          name[i]=uname
          marks[i]=umarks
def delete():
    droll=input("enter the roll no of delete")
    for i in range(len(roll)):
        if(roll[i]==droll):
            roll.remove(roll[i])
            name.remove(name[i])
            marks.remove(marks[i])
            break
count=3
while(count!=0):
    uname=input("Enter the username=")
    upass=input("Enter the password=")
    if(uname=="admin" and upass=="1234"):
        print("login successfully")
        print("**************STUDENT MANAGEMENT SYSTEM******************")
        cnt=1
        while(cnt!=0):
            print("add student")
            print("view student")
            print("update ")
            print("delete ")
            print("exit")
            ch=int(input("enter the choice"))
            if(ch==1):
                print("adds student") 
                addstud() 
            if(ch==2):
                print("view student")
                view()
            if(ch==3):
                print("update ")
                update()
            if(ch==4):
                print("delete ")
                delete()
            if(ch==5):
                cnt=0
                print("you are logged out")
        count=1
    elif(uname!="admin" and upass!="1234"):
        print("login unsuccessfully both incorrect")
    elif(uname!="admin"):
        print("user name incorrect")
    elif(upass!="1234"):
        print("user password incorrect")
    count-=1
    if(count!=0):
        print("remaining attempt=",count)
        print("you can try again.....")

        