n=int(input())
t=int(input())
fo=[0,0,0]
l1=[]
il=[]
o=[]
io=[]
v=0
for i in range(n):
    l=list(map(int,input().split()))
    for i in range(0,len(l)-1,2):
        v=(l[i]*l[-1])+(l[i+1]*l[-1])
        il.append(v)
    l1.append(il)
    il=[]
#print(l1)
m=zip(l1[0],l1[1],l1[2])
m=list(m)
for i in range(len(m)):
    if list(m[i]).index(max(list(m[i])))==0:
        fo[0]=fo[0]+1
    if list(m[i]).index(max(list(m[i])))==1:
        fo[1]=fo[1]+1
    if list(m[i]).index(max(list(m[i])))==2:
        fo[2]=fo[2]+1
print(fo.index(max(fo))+1)

        