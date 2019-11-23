n=int(input())
s=str(n)
l=[]
sum=0
f=0
for i in s:
    l.append(int(i))
    g=len(l)
while True:
    le=len(l)
    for i in range(le,le-g,-1):
        sum=sum+l[i-1]
    l.append(sum)
    print(sum)
    if sum==n:
        print("Yes")
        f=1
    sum=0
if f!=1:
    print("no")
