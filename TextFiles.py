
# CHALLENGES

# 105
#
# numbers_file = open("Numbers.txt", "w")
# numbers_file.write("1, 2, 3, 4, 5")
# numbers_file.close()

# 106

# names = open("Names.txt", "w")
# names.write("Cally\n")
# names.write("AJ\n")
# names.write("Dami\n")
# names.write("Jonno\nBenaz\n")
# names.close()

# 107

# file = open("Names.txt")
# print(file.read())

# 108

# file = open("Names.txt", "a")
# new_name = input("Enter a new name: ")
# file.write(new_name)
# file.close()

# 109 nice task

# print("1) Create a new file\n2) Display the file\n3) Add a new item to the file\nMake a selection 1, 2 or 3: ")
#
# inp = int(input("Enter 1, 2 or 3: "))
#
# if inp == 1:
#     sbj = input("Enter a new subject: ")
#     sbj_file = open("Subject.txt", "w")
#     sbj_file.write(sbj + "\n")
#     sbj_file.close()
# elif inp == 2:
#     sbj_file = open("Subject.txt", "r")
#     print(sbj_file.read())
# elif inp == 3:
#     sbj = input("Enter a new subject: ")
#     sbj_file = open("Subject.txt", "a")
#     sbj_file.write(sbj + "\n")
#     sbj_file = open("Subject.txt", "r")
#     print(sbj_file.read())
#     sbj_file.close()
# else:
#     print("The number you have entered is incorrect.")

# 110 tricky concept

# names = open("Names.txt", "r")
# print(names.read())
# names.close()
#
# names = open("Names.txt", "r")
# a_name = input("Type one of the names that you see: ")
# a_name = a_name + "\n"
#
#
# for that_name in names:
#     if that_name != a_name:
#         names = open("Names3.txt", "a")
#         names.write(that_name)
#         names.close()
#
# names.close()









