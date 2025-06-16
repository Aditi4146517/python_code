d=float(input("enter coefficient of x:"))**2-4*float(input("enter coefficient of x^2:"))*float(input("enter constant"))
if(d>0):
    print("real and distinct root")
elif(d==0):
    print("real and equal roots")   
else:
    print("complex roots")     