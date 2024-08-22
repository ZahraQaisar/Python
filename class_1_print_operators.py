# 03208472627
# sir hafiz furqan

# # IDLE (integrated development and learning environment)
# # IDE (integrated developement environment)
# # python --- case sensitive
## constant variable in capslock
## variable in small letters

# # imetation game 

# # weak AI 
# # strong AI 
# # super AI

# print function
print("hello world")
print(5)
print(5+3)

print("Zahra Qaisar")
print("Advance Python Programming")

print("#####  #####  #   #  #####  #####")
print("   #   #   #  #   #  #   #  #   #")
print("  #    #####  #####  #####  #####")
print(" #     #   #  #   #  # #    #   #")
print("#####  #   #  #   #  #   #  #   #")


# # assignment operator(=)
# # arthematic operator(=, -, *, /)

a = 5
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  #integral division just print the value before the decimal
print(a % b)


a = 10
b = 6

c = a
a = b
b = c

print("a =", a)
print("b = ", b)


# code to reverse numbers

# # num = 59
# # 5 * 10 + 9
# # 50 + 9
# # 59
# # 9 * 10 + 5
# # 90 + 5
# # 95

num = 23
first = num // 10
last = num % 10

print(first)
print(last)

f = last * 10
l = first
num2 = f + l
print(num2)

# power of any number 
num3 = 2

print(num3 ** 2)
print(num3 ** 3)
print(num3 ** 10)

# code to find area of circle

PI = 3.14
radius = 8.4

area_circle = PI * (radius ** 2)

print(area_circle)
 
 

# ============================ ASSIGNMENT 1 ============================



# 1. write a program that will reverse 3 digit number
# 2. write a program that have 3 variables a, b and c 
#   having any integer values. Program will find discriminant(b ** 2 - 4ach)
# 3. write a program that will have a variable called num. 
#   Program will change the sign of number.


# CODE FOR REVERSING 3 DIGIT NUMBER
num = 789
print(num)
# (3 * 100) + 20 + 1
# 300 + 20 + 1 
# 321
# 123
first = num // 100
second = num % 100
second2 = second // 10
last = second % 10


print(" ",first)
print(" ",second)
print(" ",second2)
print(" ",last)

reverse = (last * 100) + (second2 * 10) + first
print(reverse)

# CODE FOR DISCRIMINANT 
a = 2
b = 4
c = 8

dis = (b ** 2) - (4 * a * c) 
print(dis)

# CODE FOR CHANGING THE SIGN OF THE NUMBER
num = -10
print(-1 * num)


a = 275
string = str(a)
print(string[::-1])