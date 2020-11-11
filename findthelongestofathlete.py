import sys

R=[]
print("""enter the distance covered by the athletes
in Kilometers
(press q to exit):""")
status=True
while(status):
    a=input()
    if(a=="q"):
        status=False
    else:
        status=True
        a=float(a)
        R.append(a)
R.sort()
for i in range(len(R)):
    if(R[i]<=0):
        sys.exit("Invalid Input")
print("[{:.1f},{:.1f},{:.1f}]".format(R[-1], R[-2], R[-3]))
    
