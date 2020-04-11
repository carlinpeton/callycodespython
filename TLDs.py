
# TUPLES, LISTS AND DICTIONARIES

# CHALLENGES

# 069

# countries = ("france", "belgium", "congo", "cameroun", "canada")
#
# print(countries)
#
# choice = input("Name your favourite country: ")
#
# if choice in countries:
#     print("\nThat country is in index position", countries.index(choice), "!")
# else:
#     print("That country is not an option!")

# 070

# countries = ("france", "belgium", "congo", "cameroun", "canada")
#
# print(countries)
#
# choice = input("Name your favourite country: ")
#
# if choice in countries:
#     print("\nThat country is in index position", countries.index(choice), "!")
# else:
#     print("That country is not an option!")
#
# position = int(input("Enter the number position of your second favourite country: "))
#
# print("The country you have chosen is", countries[position], "!")

# 071

# sports = ["Football", "Basketball"]
# print(sports)
#
# user = input("Enter you favourite sport other than these two named: ")
# user = user.capitalize()
# sports.append(user)
# sports.sort()
# print("The updated list is: ", sports)

# 072

# subjects = ["Maths", "Physics", "Economics", "History", "English", "RE"]
#
# print("Look at this list of subjects: ", subjects)
#
# yuck = input("Name the subject that you do not like: ")
#
# subjects.remove(yuck)
#
# print("The new list of subjects is: ", subjects)

# 073

# fav_dishes = {}
#
# for i in range(0, 4):
#     foods = input("Name a favourite dish: ")
#     fav_dishes[i] = foods
#
# print("\nYour favourite dishes are as follows: ", fav_dishes)
#
# bye_bye = int(input("\nIf you had to remove one, which one would you remove (type index pos.) : "))
# del fav_dishes[bye_bye]
# print("\nYour favourite dishes are as follows: ")
#
# print(sorted(fav_dishes.values()))

# ANSWERS :)
# Fufu and Spinach
# Jollof (w/JERK chicken)
# Pizza
# Turkish (any with lamb)

# 074 kept it simple (it's 3:30 AM right now, i'm tired)
#
# colours = ["blue", "purple", "orange", "black", "brown", "green", "red", "yellow", "pink", "white"]
#
# start = int(input("Enter a number between 0 and 4: "))
# end = int(input("Enter a number between 5 and 9: "))
#
# print(colours[start:end])

# 075

# three_digit = [333, 666, 777]
#
# for i in three_digit:
#     print(i)
#
# user_input = int(input("Enter a 3-digit number that is on the list: "))
#
# if user_input in three_digit:
#     print(three_digit.index(user_input))
# else:
#     print("Not on the list mate.")

# 076 This one was fun.

# invite_list = []
# for i in range(0, 3):
#     invite = input("Enter the name of someone that you want to invite: ")
#     invite_list.append(invite)
#
# more = input("Do you want to invite more? (y/n): ")
#
# while more == "y":
#     invite = input("Enter the name of someone that you want to invite: ")
#     invite_list.append(invite)
#     more = input("Do you want to invite more? (y/n): ")
#
# print("You have invited", len(invite_list), "people to your party.")

# 077

# invite_list = []
# for i in range(0, 3):
#     invite = input("Enter the name of someone that you want to invite: ")
#     invite_list.append(invite.capitalize())
#
# more = input("Do you want to invite more? (y/n): ")
#
# while more == "y":
#     invite = input("Enter the name of someone that you want to invite: ")
#     invite_list.append(invite.capitalize())
#     more = input("Do you want to invite more? (y/n): ")
#
# print("You have invited", len(invite_list), "people to your party.")
# print("The people you have invited are as follows: ")
# print(invite_list)
#
# scrub = input("Enter the name of one of your invitees: ")
# scrub = scrub.capitalize()
# print(scrub.capitalize(), "is in position", invite_list.index(scrub), "of your list.")
# review = input("Do you still want to invite this person? (y/n): ")
#
# if review == "n":
#     invite_list.remove(scrub)
#     print("The updated list of invitees is as follows: ")
#     print(invite_list)

# 078 Python is very intuitive. Very simple.

# tv = ["GOT", "MH", "SUITS", "THE FLASH"]
#
# for i in tv:
#     print(i)
#
# add_tv = input("Enter another TV programme: ")
# add_tv = add_tv.upper()
# add_tv_pos = int(input("Enter the number of the position you want to enter this into: "))
#
# tv.insert(add_tv_pos, add_tv)
#
# print("The new list is as follows: ")
# print(tv)

# 079

nums = []

for i in range(0, 3):
    num_add = int(input("Enter a number: "))
    nums.append(num_add)

reduction = input("Do you still want the last number that you entered saved? (y/n): ")

if reduction == "n":
    nums.remove(num_add)

print("Your list is", nums)











