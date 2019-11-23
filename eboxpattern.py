if __name__ == '__main__':
    N = int(input())
    o=[]
    for i in range(N):
        l=list(map(int,input().split()))
        if l[0]=='insert':
            o.insert(l[1],l[2])
        elif l[0]=='print':
            print(o)
        elif l[0]=='remove':
            o.remove(l[1])
        elif l[0]=='append':
            o.append(l[1])
        elif l[0]=='sort':
            o.sort()
        elif l[0]=='pop':
            o.pop()
        else:
            o.reverse()
        l=[]
    

    

