#Get the input sentence or string
a=input("Enter the required string with consecutive occurances:")
#As Python is case sensitive, make all the letters to lower case
b=a.lower()
#Initialize a new string hodling variable so that this will be printed as output
c=""
#Initialize a variable count to 0
i=0
#Check if the value is within range 0 to n-1 where n is the length of the string 
while(i<=len(b)-1):
    #Check if the index is only upto n-2
    #Because, we donot want to check the condition of not being equal after n-2 index
    if(i<len(b)-2 and b[i]!=b[i+1]):
        c+=a[i] #add the letters one by one to the empty array
    #Else if the previous conditions fail, check for indices
    #Now, we need to check if consecutive indiced values are equal 
    elif(i<len(b)-1 and b[i]==b[i+1]):
        while( i<len(b)-1 and b[i]==b[i+1]):
            i+=1
        c+=a[i]
    #This is for the final index to be tended to, when a[n-2]=a[n-1]
    else:
        c+=a[i]
    i+=1
#Reverse the string and print it as the output
print(c[::-1])
        
