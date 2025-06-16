n=int(input("enter a number"))
soe=0
soo=0
while(n!=0):
    d=n%10
    if(d%2==0):
        soe+=d 
    else:
        soo+=d 
    n=n//10  
print(f"sum of even digits={soe} and sum of odd digits={soo}")           