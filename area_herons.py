import math;
a,b,c=float(input("a:")),float(input("b:")),float(input("c:"))
s=(a+b+c)/2
print(f"area={math.sqrt(s*(s-a)*(s-b)*(s-c)):.2f}")