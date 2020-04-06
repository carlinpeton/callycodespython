
# Challenges

# 035
#
# user_name = input("Enter your name: ")
#
# for i in range(0, 3):
#     print(user_name)

# 036
#
# user_name = input("Enter your name: ")
# num = int(input("Enter a number: "))
#
# for i in range(0, num):
#     print(user_name)

# 037
#
# user_name = input("Enter your name: ")
#
# for i in user_name:
#     print(i)

# 038 This is when I realised that you could put for loops in for loops.

# user_name = input("Enter your name: ")
# num = int(input("Enter a number: "))
#
# for r in range(0, num):
#     for i in user_name:
#         print(i)

# 039
#
# num = int(input("Enter a number between 1 and 12: "))
# print("The", num, "times table up to 12 is as follows. ")
# times = 0
#
# for i in range(0, 13):
#     print(times)
#     times = times + num

# 040

# fifty = int(input("Enter a number below 50: "))
# rang = fifty - 1
# fif = 50
#
# for i in range(rang, 50):
#     print(fif)
#     fif = fif - 1

# EBI; using the steps function in the range = simpler code

# num = int(input("Enter a number below 50: "))
#
# for i in range(50, num-1, -1):
#     print(i)

# 041
#
# name = input("Enter your name: ")
# num = int(input("Enter a number: "))
#
# if num < 10:
#     for i in range(0, num):
#         print(name.capitalize())
# else:
#     for i in range(0, 3):
#         print("Too high")

# 042
#
# total = 0
#
# num1 = int(input("Enter any number: "))
# Con = input("Do you want this number included?:  ")
# Con = Con.capitalize()
#
# if Con == "Yes":
#     total = total + num1
#
# num2 = int(input("Enter any number: "))
# Con = input("Do you want this number included?:  ")
# Con = Con.capitalize()
#
# if Con == "Yes":
#     total = total + num2
#
# num3 = int(input("Enter any number: "))
# Con = input("Do you want this number included?:  ")
# Con = Con.capitalize()
#
# if Con == "Yes":
#     total = total + num3
#
# num4 = int(input("Enter any number: "))
# Con = input("Do you want this number included?:  ")
# Con = Con.capitalize()
#
# if Con == "Yes":
#     total = total + num4
#
# num5 = int(input("Enter any number: "))
# Con = input("Do you want this number included?:  ")
# Con = Con.capitalize()
#
# if Con == "Yes":
#     total = total + num5
#
# print("The total is", total)

# You're an idiot, you didn't even use for loops...

# total = 0
# for i in range(0, 5):
#     num = int(input("Enter any number: "))
#     ans = input("Do you want to include this in your total?: ")
#     if ans == "yes":
#         total = total + num
# print("The total is", total)

# 043

# direction = input("What direction do you want to count? (u/d): ")
#
# if direction == "u":
#     top = int(input("Enter the number you want to count to: "))
#     for i in range(1, top+1):
#         print(i)
# elif direction == "d":
#     down = int(input("Enter a number below 20 that you want to count from: "))
#     for i in range(20, down-1, -1):
#         print(i)
# else:
#     print("I don't understand.")

# 044

ppl = int(input("How many people do you want to invite to your party?: "))

if ppl < 10:
    for i in range(0, ppl):
        invite = input("Name a person that you want to invite: ")
        print(invite, "has been invited.")
else:
    print("My G, that is too many people!")
