"""a=[10,20,30,40,50]
b=[]
for i in range(1,len(a)+1):
   print(a[-i])
    b.append(a[-i]"""

rev=[]
a=[10,20,30,40,50]
for i in a:
    rev.insert(0,i)
    print(rev)