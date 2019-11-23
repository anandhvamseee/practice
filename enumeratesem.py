from itertools import permutations
o=[]
no='336'
def perc(no):
     if len(set(list(no)))==1 and len(no)!=1:
         o.append('YES')
     else:
         c=0
         g=''
         perm=list(permutations(no))
         for i in perm:
             print(i)
             for k in i:
                 g=g+k
             print(g)
             if int(g)%11==0:
                 print(type(g))
                 print(g)
                 c=1
                 o.append('Yes')
             g=''
             if c!=1:
                 o.append('NO')
         c=0
         perm=[]
perc(no)
print(o)