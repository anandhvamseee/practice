n=int(input())
c=0
l=[100,50,10,5,2,1]
for i in l:
    if n%i==0:
        c=c+int(n/i)
        break
    else:
        c=c+int(n/i)
        n=n%i
print(c)