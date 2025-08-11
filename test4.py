# Determining whther the triangle is euilateral, issoceles or scalene
x = float(input("Enter the first triangle: "))
y = float(input("Enter the second triangle: "))
z = float(input("Enter the third triangle: "))
if x == y == z:
    print("This is an Equilateral trianlge")
elif x == y != z or x != y == z:
    print("This is an Isosceles trianlge")
elif x != y != z:
    print("This is a Scalene trianlge")
