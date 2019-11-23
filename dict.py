s=""" was established in 200
 ur vision is to impart education, in a conductive ambience, as comprehensive as possibl
 e, with the support of all the modern technologies and produce graduates and post graduates 
 in engineering with the ability and passion to work wisely, creatively, and effectively fo
 r the betterment of our society. t is our endeavor to develop a system of ducation which"""  
 
d={}
a='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i in a:
        d[i]=d.setdefault(i,0)+1
print(d)