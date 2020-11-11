#Given the string as input.

#Change the vowels of the first strinf to $
#Change the consonant of he second string to #
#Convert the entire thirst string to upper case
#Finally concat all the results

a=input("First String:") #get the first string
b=input("Second String:")#get the second string
c=input("Third String:") #get the third string

a=list(a) #make the string into a list so that we can easily assign values

#use for loop to browse through each and find out which is a vowel and relace it by $
for i in range (0, len(a)):
    if(a[i]=="a" or a[i]=="A" or a[i]=="e" or a[i]=="E" or a[i]=="i" or a[i]=="I" or a[i]=="o" or a[i]=="O" or a[i]=="u" or a[i]=="U"):
        a[i]="$"
a="".join(a)

b=list(b) #make the string into a list so that we can easily assign values

#use the loop to browse through each abd find out which is a consonant and replace by #
for i in range (0, len(b)):
    if(b[i]!="a" and b[i]!="A" and b[i]!="e" and b[i]!="E" and b[i]!="i" and b[i]!="I" and b[i]!="o" and b[i]!="O" and b[i]!="u" and b[i]!="U"):
        b[i]="#"
b="".join(b)

c=c.upper() #To capitalize all the letters in a string

print(a+b+c)#print all of the results as a single output concatenated
