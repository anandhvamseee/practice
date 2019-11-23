n=int(input())
t=int(input())
l1=[]
p=0
for i in range(n):
    l=list(map(int,input().split()))
    for j in range(len(l)-1):
        p=p+l[-1]*l[i]
    l1.append(p)
    p=0
print(l1)