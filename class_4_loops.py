# ============================ LOOPS ============================
# WHILE LOOP (CONDITIONAL)
#       loop control variable  e.g. i
# FOR LOOP (COUNTER)
# 2 kinds of infinite loops


# i = 1
# while(i <= 10):
#     # print("hello world")
#     print(i)
#     i += 1      # i = i + 1

# i = 1
# while(i > 0):
#     if (i == 10):
#         break
#     print(i)
#     i += 1  

# i = 10
# while(i >= 1):
#     print(i)
#     i -= 1  

# i = 0
# num = int(input("Enter number:"))
# while(i <= num):
#     print(i)
#     i += 1

# num = int(input("Enter number:"))
# i = 0       # for even
# # i = 1     # for odd
# while(i <= num):
#     print(i)
#     i += 2
    
# num1 = int(input("Enter number:"))
# num2 = int(input("Enter number:"))
# if (num1 >= 0 and num2 >= 0):
#     if(num1 < num2):
#         while(num1 <= num2):
#             if(num1 %2 != 0):
#                 num1 += 1
#                 print(num1)
#             num1 += 1
#     elif(num1 > num2):
#         while(num1 >= num2):
#             if(num1 % 2 != 0):
#                 num1 -= 1
#                 print(num1)
#             num1 -= 1
#     elif(num1 == num2):
#         if(num1 % 2 == 0):
#             print(num1)
#             print('Both numbers are even and equal.')
#         else:
#             print('Both numbers are odd and equal.')
# else:
#     print("Invalid! The numbers",num1 ,num2, "are negative.")
    
    
    
# num1 = int(input("Enter number:"))
# num2 = int(input("Enter number:"))
# if (num1 >= 0 and num2 >= 0):
#     if(num1 < num2):
#         while(num1 <= num2):
#             if(num1 %2 != 0):
#                 num1 += 1
#                 print(num1)
#             num1 += 1
#     else:
#         print("Invalid! ",num1 , "is greater than", num2)
# else:
#     print("Invalid! The numbers",num1 ,num2, "are negative.")

# 2^0 - 2^10
# 1, 2, 4, 8


# i = 0
# while(i <= 10):
#     num = 2**i 
#     print(num)
#     i += 1
    
# num1 = int(input("Enter number:"))
# num2 = int(input("Enter number:"))
# if(num1 < 0 or num2 < 0):
#     print("Power should be positive.")
# else:
#     while(num1 <= num2):
#         num = 2**num1
#         print(num)
#         num1 += 1

# # for i in range(start, stop, step)
# # by default stop if one argument in range
# for i in range(1): 
#     print(i)
    
# num = int(input("enter a number: "))
# for i in range(1, num +1 , 2):
#     print(i)
# for i in range(num, 0, -2):
#     print(i)

# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))

# if(num1 < 0 or num2 < 0):
#     print("Invalid! Enter both positive number.")
# elif(num1 >= 0 and num2 >= 0):
#     if(num1 == num2):
#         if(num1 % 2 == 0):
#             print(num1, "Both are even and same numbers.")
#         else:
#             print("Both are equal and odd numbers.")
#     elif(num1 < num2):
#         if(num1 % 2 != 0):
#             num1 += 1
#         for x in range(num1, num2 + 1, 2):
#             print(x)
#     elif(num1 > num2):
#         if(num1 % 2 != 0):
#             num1 -= 1
#         for x in range(num1, num2 - 1, -2):
#             print(x)

# msg = input("Enter a string: ")
# for x in range(len(msg)):
#     # print(msg)
#     print(msg[x])
    
# i = 0
# while(i < len(msg)):
#     print(msg[i])
#     i += 1

# word = 'hello'
# guess = input("Enter your guess: ")
# # value = True
# while(True):
#     if(len(word) != len(guess)):
#         print("Try Again!")
#         choice = input("Quit(Y/N)?")
#         if(choice == "Y" or 'y'):
#             break
        
word = 'hello'
guess = input("Enter your guess: ")
value = True
while(value):
    if(len(word) != len(guess)):
        print("Try Again!")
    elif(len(word) == len(guess)):
        i = 0
        output = ""
        for x in word:
            if(x == guess[i]):
                output += x
            elif(word.find(guess[i]) != -1):
                output += '#'
            else:
                output += '~'
            i += 1
        print(output)
    choice = input("Quit? Y/N: ")
    if (choice == 'Y' or 'y'):
        value = False 
        


# word = 'hello'
# guess = input("Enter your guess: ")

# if(len(word) != len(guess)):
#     print("Try Again!")
# elif(len(word) == len(guess)):
#     i = 0
#     output = ""
#     for x in word:
#         if(x == guess[i]):
#             output += x
#         elif(word.find(guess[i]) != -1):
#             output += '#'
#         else:
#             output += '~'
#         i += 1
#     print(output)

# 1 + 2 + 3 + 4 + 5
# 3 + 3 
# 6
# 1 + 3
# 4


