import math as m
n=int(input())
v=int(m.sqrt(n))
c=0
for i in range(1,v+1):
    if i==v:
        break
    for j in range(i+1,v+1):
        if i**2+j**2==n:
            #print(i,j)
            c=1
            break
if c!=1:
    print('false')
        
