import math
#ax^2 + b^x + c=0

#Inputs
a=float(input("Enter the coefficiemt of x^2: "))
b=float(input("Enter the coefficiemt of x: "))
c=float(input("Enter the value of constant: "))

#Calculation
discriminant= b**2-4*a*c
x1=(-b+math.sqrt(math.pow(b,2)-(4*a*c)))/2
x2=(-b-math.sqrt(math.pow(b,2)-(4*a*c)))/2

#Output
print("The roots of the quadratic equationa are: {} and {}.".format(x1, x2))
print(f"Discriminant: {discriminant}")
