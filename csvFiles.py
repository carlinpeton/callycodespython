import csv
import random
import operator

# CHALLENGES

# 111

# file = open("Books.csv", "w")
# inserts = "Too Kill A Mockingbird, Harper Lee, 1960\n" \
#           "A Brief History of Time, Stephen Hawking, 1988\n" \
#           "The Great Gatsby, F.Scott Fitzgerald, 1922\n" \
#           "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n" \
#           "Pride and Prejudice, Jane Austen, 1813\n"
# file.write(str(inserts))
# file.close()
#
# 112
#
# file = open("Books.csv", "a")
# book = input("Enter a new book: ")
# author = input("Enter a new author: ")
# published = input("Enter the publishing year: ")
# new_rec = book + ", " + author + ", " + published + "\n"
# file.write(str(new_rec))
# file.close()
#
# file = open("Books.csv", "r")
# for row in file:
#     print(row)

# 113 I'm proud of this one.

# num = int(input("Specify the amount of books you want to add to the database: "))
# loop = 0
#
# while loop < num:
#     file = open("Books.csv", "a")
#     book = input("Enter a new book: ")
#     author = input("Enter a new author: ")
#     published = input("Enter the publishing year: ")
#     new_rec = book + ", " + author + ", " + published + "\n"
#     file.write(str(new_rec))
#     file.close()
#     loop += 1
#
# author_check = input("Enter an author for search: ")
# author_check.capitalize()
# file = open("Books.csv", "r")
# reader = csv.reader(file)
# nb_count = 0
#
# for row in file:
#     if author_check in str(row):
#         print(row)
#     else:
#         nb_count += 1
#
# if nb_count == len("Books.csv"):
#     print("There are no books by this author in this database.")

# 114 Produces an error for n/a years.

# year_open = int(input("Enter a starting year: "))
# year_close = int(input("Enter a closing year: "))
# file = list(csv.reader(open("Books.csv", "r")))
# tmp = []
# for row in file:
#     tmp.append(row)
#
# r = 0
# for row in tmp:
#     if year_open <= int(tmp[r][2]) <= year_close:
#         print(tmp[r])
#     r += 1

# 115

# file = open("Books.csv", "r")
# x = 0
# for row in file:
#     display = "Row " + str(x) + " - " + row
#     print(display)
#     x = x + 1

# 116 Definitely the toughest thing so far.

# file = list(csv.reader(open("Books.csv", newline='')))
# Book_list = []
# for row in file:
#     Book_list.append(row)
#
# x = 0
# for row in Book_list:
#     display = x, Book_list[x]
#     print(display)
#     x = x + 1
# get_rid = int(input("Enter a row number to delete: "))
# del Book_list[get_rid]
#
# x = 0
# for row in Book_list:
#     display = x, Book_list[x]
#     print(display)
#     x = x + 1
#
# alter = int(input("Enter a row number to alter: "))
#
# x = 0
# for row in Book_list[alter]:
#     display = x, Book_list[alter][x]
#     print(display)
#     x = x + 1
#
# part = int(input("Enter the column that you want to change: "))
# newdata = input("Enter new data: ")
# Book_list[alter][part] = newdata
# print(Book_list[alter])
#
# file = open("Books.csv", "w")
# x = 0
#
# for row in Book_list:
#     newrec = Book_list[x][0] + ", " + Book_list[x][1] + ", " + Book_list[x][2] + "\n"
#     file.write(newrec)
#     x = x + 1
# file.close()

# 117 I had to go to Google for this one. I learnt about the format, keys and get functions.

name = input("Enter your name: ")

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

count = 0
score = 0

while count < 4:
    num1 = random.randint(0, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1, num2)
    user_ans = float(input('{} {} {} = '.format(num1, op, num2)))
    if user_ans == answer:
        score += 1
        count += 1
    else:
        count += 1

print('You scored {}/4!'.format(score))
marks = (score, "/4")


file = open("MyFirstMathsQuiz.csv", "a")
record = (name.capitalize(), marks)
file.write(str(record))
file.close()
