import math

# CHALLENGES

# 027

# num = float(input("Enter a number with decimal places: "))
# print(num*2)

# 028

# num = float(input("Enter a number with decimal places: "))
# print(round(num*2, 2))

# 029

# fhunna = float(input("Enter an integer over 500: "))
#
# while fhunna < 500:
#     print("The integer you entered was not over 500, please try again.")
#     fhunna = float(input("Enter an integer over 500: "))
# else:
#     print(math.sqrt(fhunna))

# 030

# print(round(math.pi, 5))

# 031

# rad = float(input("Enter the radius of a circle: "))
# Area = math.pi * rad**2
# print(Area)

# 032

# rad = float(input("Enter the radius of a cylinder: "))
# dep = float(input("Enter the depth of a the cylinder: "))
#
# Volume = dep * rad**2 * math.pi
# print("The volume of the cylinder is", Volume)

# 033

# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter another number: "))
# whole_div = num1 // num2
# rem = num1 % num2
#
# print(num1, "divided by", num2, "is equal to", whole_div,"remainder", rem)

# 034
# Best code i've made yet.

print("1) Square \n2) Triangle\n")
num = float(input("Enter the number one or two: "))

while num != 1 and num != 2:
    print("You have not entered the number one or two.")
    num = float(input("Enter number one or two: "))
else:
    if num == 1:
        side = float(input("Enter the length of the sides of the square: "))
        Area = side ** 2
        print("The area of the square is", Area)
    else:
        height = float(input("Enter the height of the triangle: "))
        base = float(input("Enter the length of the base of the triangle: "))
        Area = height * base * 0.5
        print("The area of the triangle is", Area)