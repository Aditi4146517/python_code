n=int(input("enter a number"))
suc=0
pr=1
while(n!=0):
    d=n%10
    if(d%2==0):
        suc=d+1
        pr=pr*suc  
    n=n//10  
print(" product of successor=",pr)    