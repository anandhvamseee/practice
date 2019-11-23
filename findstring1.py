s=input()
t=input()
v=len(t)
c=0
l=[]
l2=[]
for i in t:
    l.append(i)
for i in range(0,len(s)):
    if i+(v-1)==len(s):
        break
    else:
        for j in range(i,i+v):
            l2.append(s[j])
    if l2==l:
        c=c+1
    else:
        l2.clear()
print(c)
