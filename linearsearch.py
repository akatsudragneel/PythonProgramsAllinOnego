import sys

a=[]
c=[]
n= int(input("Enter the number of elements you wish to enter: "))
print("Enter the numbers: ")
for i in range (n):
    b=int(input())
    a.append(b)
n1= int(input("Enter the number yould want to search for: "))
for j in range (len(a)):
    if(a[j]==n1):
        c.append(j+1)
        if(len(c)>1):
            print("and")
        print("The position in which the number is found is {}".format(j+1))
if(len(c)==0):
    print("The search is invalid!!, there is no match")
