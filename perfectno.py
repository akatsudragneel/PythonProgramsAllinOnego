import sys

f=[]
add=0
a=int(input("Enter the number to check if it is a perfect number:"))
for i in range(1, int(a/2)+1):
    if(a%i==0):
        factor=i
        f.append(factor)
for j in range(0, len(f)):
    add+=f[j]
if(a==add):
    print("Factors of the number {} are:".format(a))
    print(f, end="")
    print("\n{} is a perfect number".format(a))
else:
    print("Factors of the number {} are:".format(a))
    print(f, end="")
    print("\n{} is not a perfect number".format(a))
