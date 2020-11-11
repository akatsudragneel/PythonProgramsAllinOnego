import math
f=[]
a=int(input("Enter the N to get the Nth number of the fibonacci serires: "))
f.append(0)
f.append(1)
for i in range(2,a):
    b=f[i-1]+f[i-2]
    f.append(b)
print(f[a-1])
print("The reverse of the fibonacci series till the Nth number specified: ")
for j in range(0, len(f)):
    print(f[a-j-1],end=" ")
    
