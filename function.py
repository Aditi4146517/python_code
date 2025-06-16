
import math
def calArea(a,b=0):
    if(b==0):
        area=math.pi*a**2
        return area
        print("area of circle=",area)
    else:
        area=a*b
        return area  
        print("area of rectangle=",area) 

calArea(5,7)   

tarea= calArea(2,3)+calArea(5,6)+calArea(8,9)
print("total area=",tarea)
#return should be last
#write a function to find sum and avg of a number

def avg(*num):
    s=0
    l=len(num)
    for n in num:
        s+=n
    average=s/l 
    print("sum=",s,"average=",average)
    return s,average    

avg(4,5,6,7)
def empDetail(**emp):
    for k,v in emp.items():
        print(f"{k}-{v}")

empDetail(name="abc",salary="5000",department="management")

#local variable and global variable
def myfun():
    lv=10
    lv+=20
    print(lv)
    gv+=20
    lv+=20
print(gv+=10)    






