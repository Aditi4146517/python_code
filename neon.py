n=int(input("enter a number"))
s=n*n 
sum=0
while(s!=0):
    d=s%10
    sum=sum+d  
    s=s//10

if(n==sum):
    print("number is neon")
else:
    print("number is not neon")