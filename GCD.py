a,b=int(input("enter first number:")),int(input("enter second number"))
if(a<b):
    n=a 
else:
    n=b 
i,f=1,1     
while(i<=n):
    if(a%i==0 and b%i==0):
        f=i 
        i=i+1  
print("gcd=",f)