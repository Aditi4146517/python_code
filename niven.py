n=int(input("enter a number"))
n1=n 
s=0 
while(n!=0):
    d=n%10
    s=s+d
    n=n//10
if(n1%s==0):
    print("no. is neven") 
else:
    print("no. is not neven")    
