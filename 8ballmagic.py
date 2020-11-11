import random
import sys

a= ["IT IS CERTAIN","YOU MAY RELY ON IT","AS I SEE IT, YES","OUTLOOK LOOKS GOOD","MOST LIKELY","IT IS DECIDELY SO","WITHOUT A DOUBT","YES, DEFINETLY"]
while(1):
    quest=input("Enter a question? (press ENTER to exit)")
    i= random.randint(0,7)
    if(quest):
        if(i):
            print(a[i])
    else:
        sys.exit()
