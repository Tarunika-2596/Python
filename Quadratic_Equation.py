#b.)Quadratic equation
import math
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
d=(b*b)-(4*a*c)

if(d>0):
    r=math.sqrt(d)
    r1=-b+r/2*a
    r2=-b-r/2*a
    print(r1,r2)    
elif(d==0):
    r1=-b/2*a
    print(r1)
else:
    print("No real roots exists")