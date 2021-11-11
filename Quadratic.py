#Python Program to find the roots of the Quadratic Equation.
#EQUATION IS OF THE FORM - ax2+bx+c=0
import sys

a,b,c=input("Enter the coefficients a,b and c\n").split()
a,b,c=float(a),float(b),float(c)
discriminant = (b*b)-(4*a*c)
if a==0:
    print("The value of a cannot be 0 for Quadratic Equation")
    sys.exit()
if discriminant==0:
    print("The roots are Equal")
    root1=root2=(-b/2*a)
elif discriminant<0:
    print("No Roots Exists")
    sys.exit()
else:
    root1=(-b+discriminant**0.5)/(2*a)
    root2=(-b-discriminant**0.5)/(2*a)
print("The roots are ",root1," and",root2)