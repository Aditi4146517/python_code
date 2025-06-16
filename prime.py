n=int(input("enter a number"))
c=0
for i in range(1,n+1,1):
    if(n%1==0):
        c=c+1
if(c>2):
    print("number is composite")
else:
    print("number is prime")        