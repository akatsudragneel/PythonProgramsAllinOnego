import sys

ans=[]
t=int(input())
for i in range(0,t):
    n=c1=c2=mn=mx=0
    c=""
    n=int(input())
    c=input()
    c=c.replace(" ","")
    if(len(c)>n  or len(c)<n):
        sys.exit()
    c=list(c)
    c=[int(i) for i in c]
    c= sorted(c,reverse=True)
    c1=c[0]
    c2=c[1]
    total=0
    j=1
    while j<len(c):
        mx=max(c1, c2)
        mn=min(c1,c2)
        total+=mn
        c1=mx-mn
        j+=1
        if(j==len(c)): break
        c2=c[j]
        if(c1==0 and c2!=0):
            total+=c2
    ans.append(total)
for i in range(0, len(ans)):
    print(ans[i])

