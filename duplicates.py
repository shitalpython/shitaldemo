num=[1,2,3,4,4,5,6,6]
p=set()
for x in num:
    if num.count(x)>1:
        p.add(x)
print(list(p))