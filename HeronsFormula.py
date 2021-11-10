#Program - Heron's Formula to find the area of the triangle using the length of the sides.
a,b,c=input("Enter the Length of the sides of Triangle\n").split()
a,b,c=float(a),float(b),float(c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of Triangle using Heron's Formula based on sides is:",area)
