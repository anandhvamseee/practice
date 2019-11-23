from itertools import combinations
x,y=input().split()
y=int(y)
x=sorted(x)
l=len(x)
for i in range(1,l+1):
    p=combinations(x,i)
    for j in p:
        for k in j:
            print(k,end='')
        print("")
