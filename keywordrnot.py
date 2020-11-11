import sys
import math
import string

count=0
keywords=['break', 'case', 'default', 'defer', 'else', 'for', 'func', 'goto', 'if', 'map', 'range', 'return', 'struct', 'type', 'var']
a=input("Enter the word to check if it is a keyword or not: ")
for b in keywords:
    if(a==b):
        count+=1
if(count==1):
    print(a+" is a keyword")
else:
    print(a+" is not a keyword")

