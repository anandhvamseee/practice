s=input()
o=''
l=[i for i in s]
#l.reverse()
l1=[]
for i in range(len(l)):
    l1.append(s)
    l.remove(l[0])
    #l.reverse()
    s="".join(l)
    #l.reverse()
l1.reverse()
print(l1)

