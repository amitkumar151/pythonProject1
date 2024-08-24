import math

radius = float(input("enter the radius of circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
area2=3.14*(radius**2)
print(f"area of circle {area:,.2f}")
print(f"area of circle {area2:,.2f}")