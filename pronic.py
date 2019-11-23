n=int(input())
l=[]
p=0
#f=0
for i in range(1,int(n/2)+1):
    if n%i==0:
        l.append(i)
for i in range(len(l)):
    if i+1==len(l):
        break
    if l[i]-l[i+1]==-1 :
        p=l[i]*l[i+1]
    if p==n:
        print("pronic")
        #f=1
        break
    