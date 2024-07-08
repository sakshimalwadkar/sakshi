q=int(input("enter the quantity"))
r=int(input("enter the rate"))
d=int(input("enter the discount%"))
total=q*r
print("total=",q*r)
print("dis value=",total/d)
demo=(d/100)*1000
basic=total-demo
print("basic_total=",total-demo)
g=int(input("enter the gst"))
gst=(g/100)*1000
print("net_salary",gst+basic)