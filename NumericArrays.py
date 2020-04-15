from array import *
import random

# 088

# nums = array('i', [])
#
# for x in range(0, 5):
#     newVal = int(input("Enter a number: "))
#     nums.append(newVal)
#
# nums = sorted(nums)
# print(nums)

# 089

# nums = array('i', [])
#
# for x in range(0, 5):
#     newVal = random.randint(1, 100)
#     nums.append(newVal)
#
# for x in nums:
#     print(x)

# 090

# nums = array('i', [])
# count = 0
#
# while count != 5:
#     addition = int(input("Enter a value between 10 and 20: "))
#     while addition < 10 or addition > 20:
#         addition = int(input("That value was outside the range, try again: "))
#     else:
#         count += 1
#         nums.append(addition)
#
# nums = sorted(nums)
# print(nums)
# print("Thank you")

# 091

# nums = array('i', [3, 3, 5, 7, 4])
# print(nums)
#
# select = int(input("Enter one of the numbers: "))
# print("The number you selected appeared", nums.count(select), "time(s).")

# 092

# user_a = array('i', [])
# comp_rand = array('i', [])
#
# for x in range(0, 3):
#     add = int(input("Enter in a value: "))
#     user_a.append(add)
#     print(user_a)
#
# for x in range(0, 5):
#     add_rand = random.randint(1, 100)
#     comp_rand.append(add_rand)
#
# print(comp_rand)
# print(user_a)
#
# comp_rand.extend(user_a)
#
# print(comp_rand)
#
# comp_rand = sorted(comp_rand)
#
# for x in comp_rand:
#     print(x)

# 093
#
# nums = array('i', [])
# removed = array('i', [])
# for x in range(0, 5):
#     new = int(input("Enter a number: "))
#     nums.append(new)
#
# nums = sorted(nums)
# print(nums)
#
# rem = int(input("Pick a number that you want to remove: "))
# nums.remove(rem)
# removed.append(rem)
#
# print(nums)
# print(removed)

# 094

# nums = array('i', [2, 44, 5, 23, 88])
# print(nums)
# sel = int(input("Select one of these numbers: "))
#
# while sel not in nums:
#     sel = int(input("That number isn't in the array. Select one of these numbers: "))
#
# print("Position:", nums.index(sel))

# 095 Tripped on this one. It was the nums[i] bit.

# nums = array('f', [50, 100, 40, 20, 10])
# user = int(input("Enter a whole number between 2 and 5: "))
#
# while 2 > user or user > 5:
#     user = int(input("That integer was not in between 2 and 5 try again: "))
#
# for i in range(0, 5):
#     sol = nums[i] / user
#     print(round(sol, 2))





