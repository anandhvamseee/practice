 def minion_game(string):
    l=len(string)
    t=l
    kevin=0
    stuart=0
    v=['a','e','i','o','u','A','E','I','O','U']
    for i in range(l):
        if string[i] in v:
            kevin=kevin+(t-i)
        else:
            stuart=stuart+(t-i)
    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin==stuart:
        print("Draw")
    else:
        print("Stuart",stuart)
    
    

if __name__ == '__main__':
    s = input()
    import timeit
    start=timeit.default_timer()
    minion_game(s)
    end=timeit.default_timer()
    print("time taken ",(start-end) )