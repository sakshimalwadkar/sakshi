str1=input("enter the string 1")
str2=input("enter the string 2")
def anagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        print("the enterd string is anagram")
    else:
        print("the enterd string is not anagram")
anagram(str1,str2)    
        