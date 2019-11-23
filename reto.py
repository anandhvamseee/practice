s=input()
l=list(s)
k=len(l)
li=[]
lv=[]
lc=[]
c=1
for i in range(0,len(l)):
    print(i)
    if i==k-1:
        break
    for j in range(i+1,len(l)):
        print(j,end='')
        if l[i]==l[j]:
            c=c+1
    if c>1:
        li.append(i)
        v=l[i]
        lv.append(v)
        lc.append(c)
        c=0

print(li)
print(lv)
print(lc)
#for i in range(len(lc)):
    #for j in range(1,
            
        
        
         
    
    
    
    
    
    