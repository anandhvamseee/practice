n=int(input())
l=list(map(int,input().split()))
p=[i+1 for i in range(n)]
for i in range(1,n+1):
    #print(i)
    for j in range(1,n+1):
        #print(j)
        if j%i==0:
            if l[j-1]==0:
                l[j-1]=1
            else:
                l[j-1]=0
print(l)
