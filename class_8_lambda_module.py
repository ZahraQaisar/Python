# #  LAMBDA

# #  concise code
# #  function store in a variable 
# #  can be returned and also saved in a var

# # ----------------------------------------

# def sum(a, b):
#     return(a+b)

# x = lambda x, y : x + y

# print(x(2, 5))

# # ----------------------------------------

# def myfunc(n):
#       return lambda a : a * n

# mydoubler = myfunc(2)
# # function = function
# print(mydoubler(11))


#  ------------ MODULE --------------

# from math
# from math import *

#  HUGE DIFF BETWEEN BOTH
#   NAME OF THE MODULE WILL NOT BE NEEDED TO WRITE WHEN A FUNCTION OF A MODULE IS CALLED
# ------------------------------------------
#  python standard library 
# can have build in functions and constant variables
# math
# os
# datetime
# random

# import math 

# # directory
# # print(dir(math))

# print(math.factorial(5))
# print(math.sin(math.radians(90)))
# print(math.pi)

# import random

# courses = ['PF', 'OOP', 'Python', 'WD', 'AD']

# course = random.choice(courses)
# print(course)
# print(dir(random))

# import datetime as dt
# # module name .modulae part. function
# # today = datetime.datetime.now()
# today = dt.datetime.now()

# # d = datetime.datetime(2028, 5, 3)
# # d = datetime.datetime(2028, 5, 3, 12, 10, 5)
# # print(d)
# print(today.strftime('%A'))
# print(today.strftime('%j'))

# print(today)


# import calendar
# print(calendar.isleap(2020))

# from math import sqrt, ceil
# print(sqrt(4))


# import turtle 

# t = turtle.Turtle()

# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# t.clone()