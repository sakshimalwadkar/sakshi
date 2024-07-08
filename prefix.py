list=["flower","flow",]
temp=len(list[0])
for i in range(len(list)):
    if(len(list[i])<temp):
        temp=len(list[i])
    while temp>0 and list[0][0:temp ]!=list[i][0:temp]:
        temp=temp-1
print("prefix",list[0][0:temp])