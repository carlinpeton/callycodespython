
# CHALLENGES
# 001, 002, 003

# x = input("Your first name: ")
# y = input("What is your surname?: ")
# print("Hello " + x + " " + y)
#
# print("What do you call a bear with no teeth?\nA gummy bear!")

# 004 (COMMAS)
# x = input("Enter a number: ")
# y = input("Enter another number: ")
# answer = int(x) + int(y)
#
# print("The total answer is", answer)

# 005

# x = input("Enter a number: ")
# y = input("Enter another number: ")
# z = input("And another one: ")
#
# answer = (int(x) + int(y)) * int(z)
# print("The answer is ", answer)

# 006

# whole_pizza = input("Input how many pizza slices you started with: ")
# eaten_slices = input("Input how many slices you have eaten: ")
# remaining_pizza = int(whole_pizza) - int(eaten_slices)
#
# print("You have", remaining_pizza, "slices of pizza remaining!")

# 007

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# next_bday = int(age) + 1
#
# print(name, ", on your next birthday you will be ", next_bday)
#
# I don't know how to get rid of the extra spaces after Carlin and after 22.

# 008
#
# price = input("Input your total bill price: ")
# diners = input("Input the number of diners: ")
#
# each_pay = int(price) / int(diners)
#
# print("Each person must pay: £", each_pay)

# 009 Number of seconds, minutes and hours in a given amount of days.
#
# days = input("Input a number of days: ")
#
# hours = int(days) * 24
# minutes = int(days) * (24 * 60)
# seconds = int(days) * (24 * 60**2)
#
# print(days, "days is equivalent to: \n", hours, "hours \n", minutes, "minutes \n", seconds, "seconds")

# 010
#
# kilos = input("Enter a weight in kilos: ")
#
# kilo_to_pounds = 2204 * int(kilos)
#
# print("This is equivalent to:", kilo_to_pounds, "pounds")

# 011 My proudest bit of code yet. My first use of while loops (to ensure the program doesn't stop running
# until the user is successful).

one_hunna = input("Enter a number over 100: ")

while int(one_hunna) <= 100:
    print("The number you have entered is not above 100. Please try again.")
    one_hunna = input("Enter a number over 100: ")
else:
    ten = input("Enter a number under 10: ")
    while int(ten) >= 10:
        print("The number you have entered is not under 10. Please try again.")
        ten = input("Enter a number under 10: ")
    else:
        sf = int(one_hunna) / int(ten)
        print("\nThe number", one_hunna, "goes into", ten, sf, "times")




