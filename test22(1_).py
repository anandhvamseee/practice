s=input()
l=[i for i in s]
#l2=[]
d={}
se=set(l)
os=''
for i in se:
    d[i]=str(l.count(i))
print(l)
o=list(d.items())
o.sort()
o.reverse()
for i in o:
    for j in i:
        os=os+j
print(os)
