import math

a=int(input("Enter the number to be checked: "))
c=a
sum=0
while c>0:
    b=c%10
    c=math.floor(c/10)
    sum+=math.factorial(b)
if sum==a:
    print("The number {} is a Strong number:".format(a))
else:
    print("The number {} is not a Strong number:".format(a))
