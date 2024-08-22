'''  DATA STRUCTURE 
The way in which data is stored in computer.
Mutable or Immutable - (changeable / not changeable)
Duplication or No duplication
Ordered or Not Ordered

# list - (Mutable, Duplication, Ordered)
        if data is not supposed to be changes data is fixed length no more data can be added.
        name = []
        
# tuple - (Immutable, Duplication, Ordered)
        name = ()
        
# set - (Mutable, No duplication, Unordered)
        name = set()
        
# dictionary - (Mutable, No duplication, Ordered) - MOSTLY USED
        name = {}
        
DEEP COPY - separate copy if one changes other does not
SHALLOW COPY - same list 2 different names

'''

# fruits = ['apple', 'banana', 'cherry']
# newlist = fruits # here 2 names for same list
# newlist = fruits.copy()
# sorted = fruits.copy()
# # sorted.sort()
# sorted.sort(reverse=True)

# print(fruits)
# print(sorted)

# #  pop removes values from index
# # remove removes value after finding it
# fruits = ['apple', 'banana', 'cherry']

# if (len(fruits) - 1 >= 3):
#     fruits.pop(3)
    
# if ('banana' in fruits):
#     fruits.remove('banana')

# fruits.sort()
# fruits.sort(reverse = True)

# popped = fruits.pop(1)
# print(popped)
# print(fruits)



# list1 = ['a', 'b', 'c']
# x = list1.copy()

# # huge difference b/w both

# list1 = ['a', 'b', 'c']
# x = list1
# list1.remove('b')

# fruits = ['apple', 'banana', 'cherry']
# cars = ['bmw', 'audi']

# fruits.extend(cars)
# cars.extend(fruits)
# print(fruits)
# print(cars)

# courses = ['PF', 'Python', 'OOP']
# print(courses)
# print(courses[0:4])
# print(type(courses))

# print(len(courses))

# # append will by default place the value at the endof the list
# courses.append("value1") 
# # for insterting at a specific index without affecting the previous value
# courses.insert(1, "value2") 

# courses.clear()
# print(courses)

# value = int(input("Enter number of values: "))
# students = []

# # for x in range(value):
# #     students[x] = input("Enter student's name: ")
    
# for x in range(value):
#     name =  input("Enter student's name: ")
#     students.append(name)




# value = int(input("Enter number of subjects: "))
# marks_list = []

# for x in range(value):
#     subject =  int(input(f'Enter marks for subject{x + 1}:'))
#     marks_list.append(subject)
    
# print(marks_list)

# sum = 0
# i = 0
# total = value * 100

# while (i < len(marks_list)):
#     sum = sum + marks_list[i]
#     i += 1
# print('Sum of marks: ',sum)

# percentage = (sum / total) * 100
# print('Percentage: ',percentage, '%')

# average = (sum / value)
# print('Average: ', average)



# sum = 0
# value = int(input("Enter number of subjects: "))
# marks_list = []

# for x in range(value):
#     subject = (int(input(f'Enter marks for subject{x+1} :')))
#     marks_list.append(subject)

#     sum += subject
    
# # greater = marks_list[0]
# # smaller = marks_list[0]

# # for x in range(value):
# #     if marks_list[x] > greater:
# #         greater = marks_list[x]
# #     if marks_list[x] < smaller:
# #         smaller = marks_list[x]

# greater = max(marks_list)
# smaller = min(marks_list)

# print('Greater value: ',greater)
# print('Smaller value: ',smaller)
        
# # total = sum(marks_list)   # build in function for sum
# percentage = (sum / (value * 100)) * 100
# average = (sum / value)
# print('Sum of marks: ',sum)
# print('Percentage: ',percentage, '%')
# print('Average: ', average)


        
        
        
        
# one list input
# 2 lists even odd


# num_of_values = int(input("Enter number of subjects: "))
# numbers, even, odd = [],[],[]

# for x in range(num_of_values):
#     subject =  int(input(f'Enter value:'))
#     numbers.append(subject)
# print('List: ',numbers)

# for x in range(num_of_values):
#     if numbers[x] % 2 == 0:
#         if numbers[x] not in even:      # not in returns true if the value is not in the list
#             even.append(numbers[x])     # in returns true if the value is in the list
#     else:
#         if numbers[x] not in odd:
#             odd.append(numbers[x])
        
# print('Even List:', even)
# print('Odd List:', odd)



#-----------------------------------------------------------------------------------------

cars = ['honda', 'toyota', 'suzuki']
cars[2] = 'bmw'
cars.append('suzuki')
cars.append(['volvo', 'ford'])
print(cars[4][0])
cars.insert(1, ['mitsubishi', 'mercedes'])
print(cars)
print(cars[1][1])
cars[1].remove('mercedes')
print(cars)

# str_car = ''
# for car in cars:
#     print(car)
#     str_car += car
# print(str_car)