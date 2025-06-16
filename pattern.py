"""rows=5
for i in range(1,rows+1):
    print("*"*i)

#3
rows=4
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()            

#1 square hollow pattern
rows=7
cols=5
for i in range(rows):
    for j in range(cols):
        if(i==0 or i==rows-1 or j==0 or j==cols-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()               

#2 number triangular
rows=4
for i in range(1,rows+1):
    for j in range(i):
        print(i,end=" ")
    print() """      