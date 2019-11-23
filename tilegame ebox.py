import math
ta=0
si=int(input())
n=int(input())
for i in range(n,-1,-1):
    if int(math.sqrt(i)+0.5)**2==i:
        ta=i
        break
