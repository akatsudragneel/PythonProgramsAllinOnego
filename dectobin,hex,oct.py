a=int(input("Enter the number to be converted into other forms:"))
print("The binary value of {} is {}".format(a,bin(a).replace("0b","")))
print("The hexadecimal value of {} is {}".format(a,hex(a).replace("0x","").upper()))
print("The octal value of {} is {}".format(a,oct(a).replace("0o","")))
b=input("Enter the binary sequence to be converted into decimal:")
dec=0
for i in range(0, len(b)):
    if(b[i]=="0" or b[i]=="1"):
        dec+=(2**(len(b)-i-1))*int(b[i])
    else:
        print("This is not a binary sequence")
        exit()
print("The octal value of {} is {}".format(b,oct(dec).replace("0o","")))
