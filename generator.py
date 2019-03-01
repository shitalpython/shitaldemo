#generator function returns itterator object
#when a function have yeild keyword then it becomes generator
#yeild keep state of execution in memory

def square(numbers):
    for i in numbers:
        print("before")
        yield (i*i)
        print("after")


mysquare=square([10,20,30,40,50,60])
print(next(mysquare))
print(next(mysquare))
print(next(mysquare))
print(next(mysquare))