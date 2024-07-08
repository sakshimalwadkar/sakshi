
a1=[2,6,90,89,7]
a2=[6,6376,848,99]
list=[]
for i in a1:
    if i in a2:
        list.append(i)
print("intersection point",list[0])