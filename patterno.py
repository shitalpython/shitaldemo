k = 8
for i in range(1, 10):
    for j in range(1, 10):
        if j <= k:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print("\n")
    k=k-1