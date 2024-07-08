def palindrome(str):
 r="".join(reversed(str))
 print("reversed string",r) 
 if(r==str):
    print("the string is palindrome")
 else:
    print("the string is not palindrome")       
 return r
str=input("enter the string")
print(palindrome(str))