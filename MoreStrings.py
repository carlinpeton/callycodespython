
# CHALLENGES

# 080

# first_name = input("Enter your first name: ")
# print(len(first_name))
#
# surname = input("Enter your surname: ")
# print(len(surname))
#
# full_name = first_name + " " + surname
# print(full_name)
# print(len(full_name))

# 081

# fav_sub = input("Enter your favourite subject: ")
#
# for letter in fav_sub:
#     print(letter, end="-")

# 082
#
# poem = "If you can dream—and not make dreams your master; " \
#         "If you can think—and not make thoughts your aim;"
# print(poem)
#
# start = int(input("Enter a number to indicate a starting point: "))
# end = int(input("Enter a number to indicate an ending point: "))
#
# print(poem[start:end])

# 083

# phrase = input("Enter a phrase in uppercase letters: ")
# phrase_check = phrase.isupper()
#
# while not phrase_check:
#     print("That weren't it mate.")
#     phrase = input("Enter a phrase in uppercase letters: ")
#     phrase_check = phrase.isupper()
#
# print("Well done mate.")

# 084

# posty = input("Enter the first four digits of your postcode: ")
# posty = posty.upper()
# print(posty)

# 085 A little tricky.

# vowels = ["a", "e", "i", "o", "u"]
# vowel_count = 0
# name = input("Enter your name: ")
# name = name.lower()
# print(vowels)
#
# for letter in name:
#     if letter in vowels:
#         vowel_count += 1
#
# print("There are", vowel_count, "vowels in your name.")

# 086

# password = input("Enter a new password: ")
# again = input("Enter the password again: ")
#
# if password == again:
#     print("Thank you")
# elif password.lower() == again.lower():
#     print("They must be in the same case.")
# else:
#     print("Incorrect my G.")

# 087 This one TRIPPED me.

# word = input("Enter any word in: ")
# length = len(word)
# num = 1
#
# for i in word:
#     pos = length - num
#     letter = word[pos]
#     print(letter)
#     num += 1










