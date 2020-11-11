import math
a=int(input("Enter the number that you need sqare root for: "))
f=[]
for i in range(1,math.floor(a/2)+1):
    if(a%i==0):
        f.append(i)
print(f)
for i in range(0, len(f)):
    b=f[i]
    if(b**2==a):
        print("The root of the number {} is {}".format(a,b))
