s=input()
l=s.split()
m=l.count('mat')+l.count('Mat')
j=l.count('jet')+l.count('Jet')
if m==j:
    print("True")
else:
    print("false")