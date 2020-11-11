import sys

a= int(input("Enter the number of inputs: "))
s=[]
f=[]
for i in range (0,a):
    b=int(input())
    s.append(b)
i=z=o=0
while(i<a):
    if(s[i]==0):
        z+=1
    elif(s[i]==1):
        o+=1
    else:
        sys.exit("Invalid Input")
    i+=1
for i in range(z):
    f.append(0)
for i in range(o):
    f.append(1)
for i in range(a):
    print(f[i],end="")
