a=int(input("enter first number"))
b=int(input("enter second number"))
i,f=0,0
while((i<a) and (i<b)):
    i=i+1
    if(a%i==0 and b%i==0):
        f=f+1
if(f>1) :
    print("they are not co-primes")
else:
    print("they are co-primes")           
