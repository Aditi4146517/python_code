n=int(input("enter a number"))
rev=0
n1=n
while(n!=0):
    d=n%10
    rev=rev*10+d 
    n=n//10 

if(rev==n1):
    print("number is palindrome")
else:
    print("number is not palindrome")        