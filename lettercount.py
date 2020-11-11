#THE LETTER THAT HAS THE HIGHEST COUNT

letter=[]
answer=[]
a= input ("Enter the sentence: ")
a=b=a.lower().replace(" ", "")
i=j=0
k=len(a)
b=list(dict.fromkeys(b))
print(a)
print(b)
for i in range(0, len(b)):
    count=0
    for j in range(0, len(a)):
        if(a[j]==b[i]):
            count+=1
    letter.append(b[i])
    letter.append(count)
print(letter)
m=3
z=letter[1]
while(m<len(letter)):
    z=max(z,letter[m])
    m+=2
print(z)
for i in range(0, len(letter)):
    if(letter[i]==z):
        print("Maximum occuring character is '{}' = {} times". format(letter[i-1].upper(), z))
