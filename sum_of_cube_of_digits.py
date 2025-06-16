n=int(input("enter a number"))
s=0
while(n!=0):
    d=n%10
    s=s+d**3
    n=n//10  
print(f"sum of cube of digits={s}")    