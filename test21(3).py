d={}
al='abcdefghijklmnopqrstuvwxyz'
j=0
o=[]
val=0
for i in al:
    d[i]=j
    j=j+1
s=input()
print(d)
if s.isupper():
    s.lower()
for i in range(0,len(s),2):
    o.append(s[i])
    val=int(d[s[i]])+int(s[i+1])
    print(val)
    for k,j in d.items():
        if j==val:
            o.append(k)
    val=0
for i in o:
    print(i,end='') 