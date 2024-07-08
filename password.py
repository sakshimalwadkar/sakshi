
print("password must be 8 character,upper case,lower case,number,special character")
str=input("enter the password")
lcnt=0
ucnt=0
ncnt=0
scnt=0
for i in range(len(str)):
    if(str[i]>='a' and str[i]<='z'):
        lcnt+=1
    elif(str[i]>='A' and str[i]<='Z'):
        ucnt+=1
    elif(str[i]>='0' and str[i]<='9'):
        ncnt+=1
    else:
         scnt+=1
         
if(lcnt!=0 and ucnt!=0 and ncnt!=0 and scnt!=0 and len(str)>=8):
     print("valid password")
else:
    print("in-valid password")