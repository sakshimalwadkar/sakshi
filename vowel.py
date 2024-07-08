str=input("enter the string")
def vowel():
 c=0
for i in range(len(str)):    
       if(str[i]=='a' or str[i]=='A' or str[i]=='e' or str[i]=='E'or str[i]=='i' or str[i]=='I' or str[i]=='o' or str[i]=='O' or str[i]=='u' or str[i]=='U' ):
          c=+1
print("a count",str.count('a')+str.count('A'))
print("e count",str.count('e')+str.count('E'))
print("i count",str.count('i')+str.count('I'))
print("o count",str.count('o')+str.count('O'))
print("u count",str.count('u')+str.count('U'))
print("total count",c)
vowel()
 