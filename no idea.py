x,y=map(int,input().split())
l=list(map(int,input().strip().split()))[:x]
A=list(map(int,input().strip().split()))[:y]
B=list(map(int,input().strip().split()))[:y]
h=0
def diff(l,A):
    return (list(set(A) - set(l))) 
v=diff(l,A)
#print(v)
g=len(A)-len(v)
h=h+g
def diff(l,B):
    return (list(set(B) - set(l)))
k=diff(l,B)
j=len(B)-len(k)
h=h-j
#print(k)
print(h)
        



