sum=lambda x,y:x+y
square=lambda x:x*x
z=sum(10,20)
print(z)
lst=[10,9,80,70,60,40,56]
lt=[1,9,8,7,6,4,56]
print(list(map(sum,lst,lt)))
print(list(map(square,lst)))
print(list(map(square,lt)))