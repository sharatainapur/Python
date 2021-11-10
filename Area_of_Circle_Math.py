#Program to print the Area of Circle given the radius using PI value from math library
import math
radius = float(input("Enter the radius of the circle\n"))
print("The Area of the circle using math.pi having radius ",radius,"is ",math.pi*radius*radius)
print("The Area of the circle using pi=3.14 having radius ",radius,"is ",3.14*radius*radius)
print("The difference in the area of circle using the two methods is", math.pi*radius*radius - 3.14*radius*radius)