n=int(input("enter a number")
n1=n  
while(n!=0):
    d=n%10
    if(d==0):
        print("number is duck")
        break 
    else:
        n=n//10
if(d!=0):       
    print("number is not duck")