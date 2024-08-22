# Variable : The name of a memory location to store the value.

var = 'Hello World'
print(var)

# Operator: Used to performs operations like add, subtract, product, divisio,
#           integral division, exponent
n1 = 4
n2 = 5
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2)
print(n1 ** n2)


# Tuple: 1. collection of values that cannot be changed 
#        2. neither deleted nor added
#        3. Values store in () round brackets
#        4. values can be of different data types

new_tuple = (1, 2, 3, '4', True)
print(type(new_tuple))

# List: 1. Collection of values 
#       2. can be modified i.e add, change, delete
#       3. values can be of diff data types
#       4. values store in []

new_list = [1, 2, 3, '4', True]
print(type(new_list))


# Dictionary: 1. Key : Value pair
#             2. value cannot be repeated
#             3. values and keys can be of different data types
#             4. keys and values store in {} brackets

new_dic = {
    'name' : 'ali',
    'age' : 20,
    30 : 'no',
    True : 'yes'
}
print(type(new_dic))


#  Loop: involes iteration of specific number of times

# for x in range(start, stop, step):
# the following for loop print even numbers in range(0-11) excluding 11
for x in range(0, 11, 2):
    print(x)
    
# Comprehension Loop: Nested loop
#                     invloves a loop in a loop

#  in the following example every value of x is printed 2 times
for x in range(10):
    for i in range(2):
        print(x)
    
# Function: Block of code that can be called and used multiple times when required
#           created with the key word 'def'
#           () is must after the defining the name of the function
#           involves arguments
#           arguments have further types
#               arbitary auguments
#               keyword arguments
#               arbitary keyword auguments

def new_func():
    print("hello world")
def main():
    new_func()  
main()

# arbitary arguments - when the number of inputs is not knon
#                      * before the argv in of function
def new_fun(*num):
    print(num)
def main():
    new_fun('hello', 'world')
main()

# keyword arguments - same name of function argv and function call argv
def new_fun2(num1, num2):
    print(num1 + num2)
def main():
    num1 = 10
    num2 = 11
    new_fun2(num1, num2)
main()

#  arbitary keyword auguments - involving both arbitary arguments and keyword arguments
def new_fun3(n1, n2, n3 = 2, n4 = 5):
    n = n1+n2+n3+n4
    print(n)
    
def main():
    n1, n2 = 3, 4
    new_fun(n1, n2)
    
main()
    
