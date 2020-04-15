
# 096, 097, 098

# table = ([2, 5, 8], [3, 7, 4], [4, 2, 0])
# print(table)
#
# sel_row = int(input("Select a row: "))
# sel_col = int(input("Select a column: "))
#
# print(table[sel_row][sel_col])
#
# row = int(input("Select a row to display: "))
# print(table[row])
#
# app = int(input("Enter a new value: "))
# table[row].append(app)
#
# print(table[row])

# 099

# table = ([2, 5, 8], [3, 7, 4], [4, 2, 0])
# print(table)
#
# row = int(input("Select a row to display: "))
# print(table[row])
# col = int(input("Select a column in that row to display: "))
# print(table[row][col])
#
# change = input("Do you want to change the value? (y/n): ")
#
# if change == "y":
#     new = int(input("What value do you want to change it to: "))
#     table[row][col] = new
#
# print(table[row])

# 100 Congratulations, that is one hundred challenges!

# geo = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#        "Tom": {"N": 4832, "S": 6784, "E": 4737, "W": 3612},
#        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
# print(geo)

# 101

# geo = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#        "Tom": {"N": 4832, "S": 6784, "E": 4737, "W": 3612},
#        "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#        "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
# print(geo)
#
# name = input("Select a name: ")
# region = input("Select a region: ")
#
# change = int(input("Enter the revised sales figure: "))
# geo[name][region] = change
#
# print(geo[name])

# 102 Tricky.

# lst = {}
# count = 0
#
# while count != 4:
#     name = input("Enter a name: ")
#     age = input("Enter the age of the person named: ")
#     shoe_size = input("Enter his/her shoe size: ")
#     lst[name] = {"Age": age, "Shoe Size": shoe_size}
#     count += 1
#
# sel = input("Enter a name to review: ")
# print(lst[sel])

103, 104

lst = {}
count = 0

while count != 4:
    name = input("Enter a name: ")
    age = input("Enter the age of the person named: ")
    shoe_size = input("Enter his/her shoe size: ")
    lst[name] = {"Age": age, "Shoe Size": shoe_size}
    count += 1

delete = input("Select someone to remove from the list: ")
del lst[delete]

for name in lst:
    print((name), lst[name]["Age"], lst[name]["Shoe Size"])






