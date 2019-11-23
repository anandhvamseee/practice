from itertools import combinations_with_replacement
x,y=input().split()
y=int(y)
x=sorted(x)
p=combinations_with_replacement(x,y)
for i in p:
    for j in i:
        print(j,end='')
    print("")
