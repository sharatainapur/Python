#Program to find the distance between 2 points on the earth's surface 
import math
t1,g1,t2,g2=input("Enter the Latitude and Longitude Coordinates of the 2 points\n").split()
t1,g1,t2,g2=float(t1),float(g1),float(t2),float(g2)

# Let (t1; g1) and (t2; g2) be the latitude and longitude of two points on the Earth's surface.
# The distance between these points in kilometers, following the surface of the earth, is:
# distance = 6371.01 * arccos (sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

#The coordinates are in Degree but the functions take values in radians and hence importing the math library for conversion
#1Deg × π/180 = 0.01745Rad

t1=math.radians(t1)
g1=math.radians(g1)
t2=math.radians(t2)
g2=math.radians(g2)

dist=6371.01*math.cosh(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("The distance between the two points on the Earth's surface is", dist, " kms")