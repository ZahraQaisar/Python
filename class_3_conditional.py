# the statements which can't be reasoned whether true or false.
# are PARADOX

# ============================ CONDITIONAL OPERATORS ============================
# answers always on bool
# <, >, <=, >=, ==, !=
# ============================ CONDITIONAL STATEMETS ============================
# if else
# ============================ LOGICAL OPERATORS ============================
# and, or, not(reverses T to F and F to T)

# a = int(input("enter a num: "))
# b = int(input("enter a num: "))
# print(a-b)

# age = int(input("enter age: "))

# if(age < 18):
#     print("not eligible")
    
# if(age >= 18):
#     print("eligible")

# num1 = int(input("enter num1: "))
# num2 = int(input('enter num2: '))

# if (num1 > num2):
#     print(num1, "is greater than ", num2)
# if (num2 > num1):
#     print(num2, "is greater than", num1)
# if (num1 == num2):
#     print(num1, num2, "both are equal.")
    
# num = int(input("enter num1: "))

# if (num < 0):
#     print(num, "a negative number.")
# if (num > 0):
#     print(num, "a positive number.")
# if (num == 0):
#     print(num, "is zero.")
    
# dis = int(input("enter distance: "))

# if(dis < 0):
#     print("Inavlid input!")   
# if(dis == 0):
#     print("distance is 0 fare is 0.")
# if(dis >= 1):
#     if(dis <= 5):
#         print("fare is 200 RS/- for the distance", dis)
# if(dis > 5):
#     if(dis <= 15):
#         print("fare is 500 RS/- for the distance", dis)
# if(dis > 15):
#     # 20
#     extra = dis - 15
#     #5
#     dis3 = extra * 50
#     newfare = dis3 + 500
#     print("Fare for the distance", dis, "is", newfare)
    
# if(dis <= 0):
#     print("distance cannot be zero or -ve.")
# if(dis > 0):
#     if(dis <= 5):
#         fare = 200
#     if(dis > 5):
#         if(dis <= 15):
#             fare = 500
#         if(dis > 15):
#             # 20
#             extra = dis - 15
#             #5
#             dis3 = extra * 50
#             fare = dis3 + 500
#             print("Fare for the distance", dis, "is", fare)
#     print("your fare is:", fare)

# a = 10
# b = 5
# c = 3

# if(a > b and a > c):
#     print('true')

# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
# num3 = int(input("num3:"))

# if(num1 > num2 and num1 > num3):
#     print(num1, "is greater")
# if(num2 > num1 and num2 > num3):
#     print(num2, "is greater")
# else:
#     print(num3, "is greater.")


# i1, i2, d1, d2, t, f = -14, 42, 3.5, 20.5, True, False

# print(t and i2/5 == 7 or  21 >= d2)
# # t and False or True
# # True and False or True
# # False or True
# # True

# # presedence 
#     # not 
#     # and 
#     # or

num = int(input("enter"))
if (num % 2 == 0):
    print("even")