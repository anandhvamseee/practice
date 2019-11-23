n=int(input())
d={}
l=list(input().split())
for i in range(1,n*2,2):
    if int(l[i])>200:
        d[l[i-1]]=int(l[i])
print(d)
print(l)