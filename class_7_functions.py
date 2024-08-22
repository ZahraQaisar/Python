'''
    FUNCTIONAL PROGRAMMING
    
        1 - Reusability
        2 - Structured Program
        3 - Easy Debugging
    
    Function definition
    Function calling
    Function arguments/parameters
    return value
    default value
    arguments - args
    
    ARGUMENTS TYPES
        1. arbitrary argu, *args - if the values of the parameters are not known
        2. keyword arguments - in key = value syntax 
                             - unordered
                             - condition is that the names of parameters should be same in both
        3. arbitrary keyword, **args
        
        using / means allowing positional args but not allwoing keyword args
        fun_name(*, arg) - this means if pos arg is sent it will not be accepted but keyword willbe accepted
        (a, b , /, c, d) - in this a and are positional 
                         - and c and d are keyword args
    
    input in function is tuple if * in start
'''

# # -----ARBITRARY-----
# def print_name(*name):
#     print(name)
#     # for n in name:
#     #     print(n)
# # print_name("atlas", 'lia', 'joe')
# print_name('joe')

# # -----KEYWORD-----
# def print_name(name, rollnum, marks):
#     print("Rollnum: ", rollnum)
# print_name(name = "atlas", rollnum = 123, marks = 95)

# # -----ARBITRARY KEYWORD-----
# def print_name(**student):
#     for n in student:
#         print(n)
#         print(student[n])
#         print(student)
# print_name(name = "atlas", rollnum = 123, marks = 95)

# def hello_world():
#     print("Hello world")

# # value of is default but if a value if passed then that value will be considered
# def sum(a,b = 5):
#     s = a + b
#     return s
    
# def sub(a,b):
#     sb = a - b
#     print('Subtraction:',sb)
    
# def product(a,b):
#     p = a * b
#     print('Product:', p)
    
# def divide(a,b):
#     d = a / b
#     print('Division:',d)
    
# def exponent(a,b):
#     e = a ** b
#     print('Exponent:',e)

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# print(sum(num1, num2))
# # sum(num1)
# # sub(num1, num2)
# # product(num1, num2)
# # divide(num1, num2)
# # exponent(num1, num2)


# def square(val):
#     sqr = val ** 2
#     return sqr

# num = int(input("Enter value:"))
# print('Square:',square(num))



# def sum(num):
#     s = 0
#     for n in num:
#         s += n
    
#     return s

# numbers = []
# len_list = int(input("Length of list:"))
# for i in range(len_list):
#     num = int(input("Number:"))
#     numbers.append(num)

# # print(numbers)
# add = sum(numbers)

# print("Sum:",add)

# def max_find(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         print(n1,'is maximum.')
#     elif n2 > n1 and n2 > n3:
#         print(n2,'is maximum.')
#     elif n3 > n1 and n3 > n2:
#         print(n3, 'is maximum')


# num1 = int(input("Number1: "))
# num2 = int(input("Number2: "))
# num3 = int(input("Number3: "))

# max_find(num1, num2, num3)

# ------------------------------------------------------------

def days_in_month(month, year):
    d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(m >= 1 and m <= 12):
        if(m == 2):
            if(is_leap_year(y)):
                d[1] = 29
        return d[m - 1]   
    else:
        print("Invalid month")
        return -1
# is_leap_year = lambda year: year % 4 == 0
def is_leap_year(year):
    if(year % 4 == 0):
        return True
    else:
        return False

m = int(input("Enter no. of month (1-12):"))
y = int(input("Enter year (4-digit no.):"))

days = days_in_month(m, y)
if(days != -1):
    print(f'No. of days in {m}, {y}:', days)
    
# -----------------------------LAMBDA-------------------------------
    
# lambda - pupose: instead of writing sigle line code 
    
sq = lambda a : a * a # will have only one paarmeter
prdt = lambda a, b: a * b

print(sq(4))
print(prdt(4, 2))