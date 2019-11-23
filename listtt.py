from itertools import combinations
s='hack'
y=int(input())
p=combinations(s,y)
for i in p:
    print(i)