# LCM of 10,20,300,27,42
#  2 | 10, 20, 300, 27, 42
#     ---------------------
#  2 |  5, 10, 150, 27, 21
#     ---------------------
#  3 |  5,  5,  75, 27, 21
#     ---------------------
#  3 |  5,  5,  25,  9,  7
#     ---------------------
#  3 |  5,  5,  25,  3,  7
#     ---------------------
#  5 |  5,  5,  25,  1,  7
#     ---------------------
#  5 |  1,  1,   5,  1,  7
#     ---------------------
#  7 |  1,  1,   1,  1,  7
#     ---------------------
#    |  1,  1,   1,  1,  1
#     ---------------------
# LCM = 2*2*3*3*3*5*5*7 = 18900
import sys
import math
a=[]
b=[]
lcm=[]

s=True
while(s):
    x=input()
    if(x=="q"):
        s=False
    else:
        x=int(x)
        if(x<0):
            sys.exit("Invalid input")
        a.append(x)
        
c=a[0]
for i in range(1, len(a)):
    d=a[i]
    e= max(c,d)
    while(True):
        if(e%c==0 and e%d==0):
            lcm=e
            break
        e+=1
    c=lcm
print("The LCM is",lcm)

















        