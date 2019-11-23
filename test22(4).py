n=int(input())
o=[]
ls=''
for i in range(n):
    s=input()
    v=input()
    l=[]
    for i in v:
        l.append(s.index(i))
    l.sort()
    print(l)
    for i in range(len(l)):
        ls=ls+s[l[i]]
    o.append(ls)
    ls=''
print(o)
    