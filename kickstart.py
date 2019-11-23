from itertools import permutations
n=int(input())
d=dict()
o=[]

def conv(d):
    n=len(d)
    s=''
    l1=list(d.items())
    for j in range(0,n):
        t1=l1[j]
        for i in range(0,t1[1]):
            s=s+str(t1[0])
    #s=int(s)
    d.clear()
    return s


def perc(no):
     if len(set(list(no)))==1 and len(no)!=1:
         o.append('YES')
     else:
         c=0
         g=''
         perm=list(permutations(no))
         for i in perm:
             for k in i:
                 g=g+k
             if int(g)%11==0:
                 c=1
                 o.append('YES')
                 break
             g=''
         if c!=1:
             o.append('NO')
         c=0
         
         perm=[]


for i in range(0,n):
    l=list(map(int,input().split()))
   # print(l[6:10])
    x=len(l)
   # print(x)
    for j in range(0,x):
        if l[j]!=0:
            d[j+1]=l[j]
    no=conv(d)
    perc(no)
for u in range(1,n+1):
    print('Case #',u,':',o[u-1] )
    