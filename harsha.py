s=0
c=0
for i in range(1,11):
   s=s+i
   for j in range(1,i+1):
       if s%j==0:
           c=c+1
           print(s,c)
   c=0
    