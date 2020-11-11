a=input("Enter the string: ")
b=a.lower()
c=[]
i=0
while i<=len(b)-1:
    count=1
    while(i<len(b)-1 and b[i]==b[i+1]):
        count+=1
        i+=1
    c.append(a[i])
    c.append(count)
    i+=1
for j in range (0, len(c)):
    print(c[j], end="")
