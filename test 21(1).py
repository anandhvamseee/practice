l1=list(input().split())
l2=list(input().split())
l3=[]
l2.reverse()
print(l1)
print(l2)
v=max(len(l1),len(l2))
for i in range(v):
    if 'None' in l1:
        l1[l1.index('None')]=''
    if 'None' in l2:
        l2[l2.index('None')]=''
    l3.append(l1[i]+l2[i])
print(*l3)