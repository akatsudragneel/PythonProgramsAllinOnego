b=input("Enter the sentence: ")
first=last= 0
for i in  range(0,len(b)):
    if(b[i]==" "):
        if(first==0):
            first=i
        else:
            last=i
    if(first!=0 and last!=0):
        break
for i in range(first+1, last):
    print(b[i].upper(), end="")
