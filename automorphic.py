n=int(input("enter a number"))
n1=n 
a=n*n  
while(n!=0):
    d=n%10
    e=a%10
    if(d!=e):
        break  
    else:
        n=n/10
        a=a/10
if(d==e):
    print("automorphic")
else:
    print(" not automorphic")                       
