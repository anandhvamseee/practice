s=input()
l=[]
c=[]
for i in s:
    l.append(i)
se=set(l)
for i in se:
    c.append(l.count(i))
#print(c)
#print(se)
se=list(se)
for i in range(len(se)):
    print(c[i],se[i],end='')
    