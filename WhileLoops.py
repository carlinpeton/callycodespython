# 045

# total = 0
#
# while total <= 50:
#     num = int(input("Enter a number: "))
#     total = total + num
#     print("The total is", total)

# 046
#
# num = int(input("Enter a number: "))
#
# while num <= 5:
#     num = int(input("Enter a number: "))
#
# print("The last number you entered was", num)

# 047
#
# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter another number: "))
#
# num3 = num1 + num2
# ans = input("Do you want to add another number? (y/n): ")
#
# while ans == "y":
#     loop_add = float(input("Enter another number: "))
#     num3 = loop_add + num3
#     ans = input("Do you want to add another number? (y/n): ")
#
# print("The total is", num3)

# 048

# count = 0
# invite = input("Enter who you want to invite to the party: ")
# print(invite.capitalize(), "has now been invited.")
# count += 1
# more = input("If you want to invite somebody else say so. (y/n): ")
#
# while more == "y":
#     invite = input("Enter who you want to invite to the party: ")
#     print(invite.capitalize(), "has now been invited.")
#     count += 1
#     more = input("If you want to invite somebody else say so. (y/n): ")
#
# print("You are inviting", count, "people to the party.")

# 049

# count = 1
# compnum = 50
# num = int(input("Guess the number: "))
#
# while num != 50:
#     if num < 50:
#         count += 1
#         print(num, "is too low.")
#         num = int(input("Try again: "))
#     else:
#         count += 1
#         print(num, "is too high.")
#         num = int(input("Try again: "))
#
# print("Well done, you took", count, "attempt(s)!")

# 050

# num1 = int(input("Enter a number between 10 and 20: "))
#
# while num1 < 10 or num1 > 20:
#     if num1 < 10:
#         print("Too low.")
#         num1 = int(input("Try again: "))
#     else:
#         print("Too high.")
#         num1 = int(input("Try again: "))
#
# print("Thank you!")

# 051 A bit more advanced and mentally stimulating.

num = 10

while num != 0:
    print("There are", num, "green bottles hanging on the wall", num,
          "green bottles hanging on the wall, "
          "and if 1 green bottle should accidentally fall")
    num -= 1
    left = int(input("How many green bottles will be hanging on the wall? : "))

    while left != num:
        left = int(input("No, please try again: "))

    print("There will be no more green bottles hanging on the wall.")

