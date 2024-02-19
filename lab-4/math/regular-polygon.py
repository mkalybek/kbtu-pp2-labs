import math

def regular_polygon_area(n, s):
    return (1/4) * n * s**2 / math.tan(math.pi / n)

n = int(input("Enter the number of sides of the regular polygon: "))
s = float(input("Enter the length of each side of the regular polygon: "))

area = regular_polygon_area(n, s)
print(f"The area of the regular polygon is: {area}")
