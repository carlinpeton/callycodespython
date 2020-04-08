import random

# CHALLENGES

# 052

# num = random.randint(1, 100)
# print(num)

# 053

# fruit = random.choice(["apple", "pear", "orange", "grapes", "watermelon"])
# print(fruit)

# 054

# coin = random.choice(["heads", "tails"])
# guess = input("Heads or tails (heads/tails) : ")
#
# if guess == coin:
#     print("You win!")
# else:
#     print("Bad luck")
#
# print("It was a", coin, "!")

# 055 This one required initiative in deciding that for loops could be used.

# num = random.randint(1, 5)
# guess = int(input("Pick a number between 1 and 5: "))
#
#
# for i in range(0, 1):
#     if num != guess:
#         if guess < num:
#             print("Too low.")
#             guess = int(input("Pick a number between 1 and 5: "))
#         else:
#             print("Too high.")
#             guess = int(input("Pick a number between 1 and 5: "))
#
# if num != guess:
#     print("You lose!")
# else:
#     print("Correct!")

# 056

# whole = random.randint(1, 10)
# guess = int(input("I'm thinking of a number between 1 and 10. Enter this number: "))
#
# while whole != guess:
#     guess = int(input("Try again: "))
#
# print("Well done my G!")

# 057 This is a fun game.

# whole = random.randint(1, 10)
# guess = int(input("I'm thinking of a number between 1 and 10. Enter this number: "))
#
# while whole != guess:
#     if guess < whole:
#         print("Too low!")
#     else:
#         print("Too high!")
#     guess = int(input("Try again: "))
#
# print("Well done my G!")

# 058 dope

# question_number = 1
# score = 0
#
# for i in range(0, 5):
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     question_ans = num1 + num2
#     print("Question", question_number, ":", num1, "+", num2, "= ?")
#     ans = int(input("Ans: "))
#     question_number += 1
#     if ans == question_ans:
#         score += 1
#
# print("You scored", score, "out of 5!")

# 059

colour = ["blue", "purple", "green", "orange", "red"]
rand_col = random.choice(colour)
choice = input("Guess the colour I am thinking of: ")

while rand_col != choice:
    if rand_col == "blue":
        print("You are probably feeling quite blue right now.")
        choice = input("Guess the colour I am thinking of again: ")
    elif rand_col == "purple":
        print("A purple heart is better than a black heart.")
        choice = input("Guess the colour I am thinking of again: ")
    elif rand_col == "green":
        print("If you want grass, just water your own.")
        choice = input("Guess the colour I am thinking of again: ")
    elif rand_col == "orange":
        print("Only plumbs think they can rhyme orange.")
        choice = input("Guess the colour I am thinking of again: ")
    else:
        print("I don't know what you've RED, but it's not what it looks like.")
        choice = input("Guess the colour I am thinking of again: ")

print("Well done champ.")
