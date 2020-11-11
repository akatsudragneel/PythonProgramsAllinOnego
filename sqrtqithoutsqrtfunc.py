import math

def square(n,i,j):
    mid=(i+j)/2
    mul=mid**2
    if((mul==n)or (abs(mul-n)<0.00001)):
        return mid
    elif(mul<n):
        return square(n,mid,j)
    else: 
        return square(n,i,mid)     
    
n=float(input("Enter the number to find the square root: "))
found=False
i=1
while(found==False):
    if(i*1 == n):
        print(i)
        found==True
    elif(i**2>n):
        res= square(n,i-1,i)
        print("{0:.5f}".format(res))
        found=True
    i+=1
