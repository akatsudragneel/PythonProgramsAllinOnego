a= int(input("Enter the number: "))
for i in range (1,a+1):
    for j in range(i,a):
        print(" ", end="")
    for k in range(0,i):
        print("* ", end="")
    print("\n")
