projectid=["101","102","103","104","105"]
name=["sakshi","puja","sanuu","diksha","tanuu"]
des=["repainting_walls","kitchen","outdoor_spaces","analysing_walls","refacing_cabinets"]
start=["12-june-2024","13-july-2024","14-march-2024","15-april-2024","1-jan-2024"]
end=["19-june-2024","15-july-2024","16-march-2024","25-april-2024","7-jan-2024"]
duration=[6,1,1,9,7]
budget=[1000,2000,3000,4000,5000]
status=[1,1,3,3,5]
def add():    
    p=input("enter the project id=") 
    projectid.append(p)
    n=input("enter the name=")
    name.append(n)
    d=input("enter the description")
    des.append(d)
    s=input("enter the start date")
    start.append(s)
    e=input("enter the end date")
    end.append(e)
    d=input("enter the duration")
    end.append(d)
    b=int(input("enter the budget"))
    budget.append(b)
    st=input("enter the status")
    status.append(st)
def view():
    demo=0
    print("PROJECT_ID \tNAME \tDESCRIPTION \tSTART_DATE \tEND_DATE \tBUDGET \tSTATUS")
    for i in range(len(projectid)):
      print(projectid[i],"\t",name[i],"\t",des[i],"\t",start[i],"\t",end[i],"\t",duration[i],"\t",budget[i],"\t",status[i],"\t")
             
    for i in range(len(budget)):
       demo=demo+budget[i]  
    print("total renovation cost of the year",demo)
    
    print("the status can be analysed as follows:-\n 1=new \n 2=inprocessed \n 3.done \n 4.overdue \n 5.reject")
    ch=int(input("enter your choice="))
    for i in range(len(status)):
        if(status[i]==ch):
                     print(projectid[i],"\t",name[i],"\t",des[i],"\t",start[i],"\t",end[i],"\t",duration[i],"\t",budget[i],"\t",status[i],"\t")    
     
def update():
    print("click on 1-6 position which are to be updated")
    print("1.update project_id \n 2.update name \n 3.update start_date \n 4.update end_date \n 5.budget \n 6.status")
    c=int(input("enter the choice"))
    fprojectid=input("enter the project id to be find")
    for i in range(len(projectid)):
        if(projectid[i]==fprojectid):
          if(c==1):
            upid=input("enter the project id to be updated=")
            projectid[i]=upid
          elif(c==2):
            uname=input("enter the name=")
            name[i]=uname
          elif(c==3):
           udes=input("enter the description")
           des[i]=udes
          elif(c==4):
           ustart=input("enter  the start date")
           start[i]=ustart
          elif(c==5):
           uend=input("enter the end date")
           end[i]=uend
          elif(c==6):
           ubudget=input("enter the budget")
           budget[i]=ubudget
          elif(c==7):
           ustatus=input("enter the staus")
           status[i]=ustatus
def delete():
    dpid=input("enter the project id of delete")
    for i in range(len(projectid)):
        if(projectid[i]==dpid):
            projectid.remove(projectid[i])
            name.remove(name[i])
            des.remove(des[i])
            start.remove(start[i])
            end.remove(end[i])
            budget.remove(budget[i])
            status.remove(status[i])
            break
count=3
while(count!=0):
    uname=input("Enter the username=")
    upass=input("Enter the password=")
    if(uname=="admin" and upass=="1234"):
        print("login successfully")
        print("**************Home Renovation Tracker******************")
        cnt=1
        while(cnt!=0):
            print("1.add project details ")
            print("2.view project details")
            print("3.update project details ")
            print("4.delete project details")
            print("exit")
            ch=int(input("enter the choice"))
            if(ch==1):
                print("adds ") 
                add() 
            if(ch==2):
                print("view ")
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

        