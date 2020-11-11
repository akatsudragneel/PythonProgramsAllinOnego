import sys

names=[]
heights=[]
complete=[]
complete1=[]
print("Enter the names of the players: ")
allow= True
while(allow==True):
    a=input()
    if(a== "end"):
        allow=False
    elif(a==""):
        e=input("""Was it a mistake, or do you want to end the input(
                press M for mistake and press E to end): """)
        if(e=="M"):
            allow=True
        else:
            allow=False
    else:
        names.append(a)
print(names)

print("Enter the heights of the players according to the names entered(in feet): ")
for i in range(0, len(names)):
    h=float(input())
    if(h=="" or h==0):
        print("Enter a valid height(in feet):\n")
    else:
        heights.append(h)
print(heights)

for k in range(0, len(heights)):
    print(k)
    dict={"name":names[k], "height":heights[k]}
    complete.append(dict)
print(complete)

complete1.append(sorted(complete, key = lambda j: j['height'],reverse=True))
for item in complete1:
    print(item['name'])
