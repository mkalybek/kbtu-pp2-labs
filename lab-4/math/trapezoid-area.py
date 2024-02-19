def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

a = float(input("Enter the length of A: "))
b = float(input("Enter the length of B: "))
height = float(input("Enter the height of the trapezoid: "))

area = trapezoid_area(a, b, height)
print(f"The area of the trapezoid is: {area}")
