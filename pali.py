n=int(input())
l=[]
for i in str(n):
    l.append(i)
l1=l
def pal(n,l,l1):
    if l.reverse()==l1:
        return True
    else:
        return False
while True:
    if pal(n,l,l1)==True:
        print(n)
        break
    else:
        n=n+1

