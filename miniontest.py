def minion_game(string):
    v=['a','e','i','o','u','A','E','I','O','U']
    count=0
    ke=0
    st=0
    for m in string:
        if m in v:
            count=count+1
    le=len(string)
    temp=le
    for i in range(0,le):
        if string[i] in v:
            while temp!=i:
                for j in range(i,temp):
                    print("",end='')
                
                ke=ke+1
                temp=temp-1
            #print("")
            #kevin=kevin+1
            temp=le
    else:
        while temp!=i:
            for o in range(i,temp):
                print("",end='')
            st=st+1
            temp=temp-1
            #stuart=stuart+1
            #print("")
        temp=le
    print(st)
    print(ke)
    if st>ke:
        print("Stuart",st)
    else:
        print("Kevin",ke)


if __name__ == '__main__':
    s = input()
    minion_game(s)