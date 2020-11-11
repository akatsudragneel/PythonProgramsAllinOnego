a=input("Enter the number to check for armstrong: ")
sum=0
for i in range(0, len(a)):
    sum+=int(a[i])**len(a)
if(sum==int(a)):
    print("Yes, the number %s is an Armstrong Number"%a)
else:
    print("No, the number %s is not an Armstrong Number"%a)
