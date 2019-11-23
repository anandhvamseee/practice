l1=list(input().split())
l2=list(input().split())
l3=list(input().split())
s=''
o=[]
for i in l1:
    for j in l2:
        for k in l3:
            s=s+i+" "+j+" "+k
            o.append(s)
            s=''
print(o)