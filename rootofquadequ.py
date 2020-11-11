import math

a= float(input("Enter the coefficient of x^2:"))
b= float(input("Enter the coefficient of x:"))
c= float(input("Enter the constant:"))

print("The equation is : ({})x^2+({})x+({})".format(int(a),int(b),int(c)))

f= -b
real= f/2
s= (b**2 - 4*a*c)
if(s<0):
    s*=-1
    imag= ((math.sqrt(s))/2)
    print("""The roots of the above equations are: r1 = {:.2f}+j{:.2f}
                                      r2 = {:.2f}-j{:.2f}""".format(real,imag,real,imag))
else:
    imag= ((math.sqrt(s))/2)
    print("""The roots of the above equations are: r1 = {:.2f}
                                      r2 = {:.2f}""".format((real+imag), (real-imag)))
