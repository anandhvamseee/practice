s=input()
c=1
l1=[]
l=[i for i in s]
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        #print(i)
        l1.append((c,int(l[i])))
        c=1
    else:
        #print(i)
        c=c+1  
    if i==len(l)-2:
        #print("jft")
        l1.append((c,int(l[i])))
print(*l1)