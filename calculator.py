def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def div(x,y):
    return x//y

def multi(x,y):
    return x*y        

opt=int(input("enter your choice(1-4)1.addition   2.subtraction  3.division  4.multiplication"))
if(opt==1):
    result=add(int(input("enter first number:")),int(input("enter second number:")))
    print("sum=",result)

elif(opt==2):
    result=sub(int(input("enter first number:")),int(input("enter second number:")))
    print("subtraction=",result)

elif(opt==3):
    result=div(int(input("enter first number:")),int(input("enter second number:")))
    print("division=",result) 

elif(opt==4):
    result=multi(int(input("enter first number:")),int(input("enter second number:")))
    print("multiplication=",result)  

else:
    print("invalid choice")         