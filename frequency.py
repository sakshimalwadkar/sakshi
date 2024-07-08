str=input("enter the string")
def freq(str):
    for i in str:
     frequency=str.count(i)
     print(i,frequency)
freq(str)
