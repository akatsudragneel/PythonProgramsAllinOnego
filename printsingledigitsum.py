import math

a=int(input("Enter the number: "))
f=[]
d=[]
sum=0
while(a>0):
    b=a%10
    a=math.floor(a/10)
    f.append(b)
f.reverse()
i=0
for i in range(len(f)):
    sum=sum+f[i]
    d.append(sum)
for i in range(len(d)):
    if d[i]>=10:
        d[i]=0
print(max(d))
