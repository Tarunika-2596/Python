#4. Find the area of a triangle given its sides
import math
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area of the triangle:", area)