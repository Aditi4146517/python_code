n=int(input("enter a number:"))
s=9
while(n!=0):
    d=n%10
    if(s>d):
        s=d  
    n=n//10
print(f"smallest digit={s}")        