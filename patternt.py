z=4
for i in range(1,4):
    for j in range(1,8):
        if j < z:
            print(" ",end=" ")
        elif j > z:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("\n")
    z=z-1