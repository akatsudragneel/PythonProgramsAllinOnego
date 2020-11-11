import sys
import math
import string

a=input("Enter the string: ")
a=ord(a.lower())-97
b=int(input("Enter the number: "))
a=a+b
if(a>=26):
    a=a%26
print("The output is "+chr(a+97).upper())
