n=int(input("enter a number"))
s=0
while(n!=0):
    d=n%10
    s=s+d  
    n=n//10
print(f"sum of digits={s}")    