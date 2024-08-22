'''
        CRUD OPERATIONS MUST


    DICTIONARY
    
    (Mutable - changeable, No duplication, Ordered) - MOSTLY USED
    
    key value pair( associative, hah_maps, objects)
    
    reference - of keys are called before any addition of new key all the keys will be printed

'''

'''
EMPTY STRING :-
                False
                None
                ''
                0

but if str = '0' then it is not null

'''

student = {
    'name' : 'ali',
    'age' : 22,
    'courses' : ['python', 'web', 'android'],
    'address' : {
        'city' : 'Lahore',
        'country' : 'Pakistan'
    }
}

address = student['address']

for key, value in address.items():
    print(key, ':',value)

# print(student['address']['country'])

# student.update({'addr' : 'lahore'})
# print(student)
# key = student.values()
# val = student.keys()

# print(key)
# print(val)

# student['phone'] = '555-555-555'
# student['name'] = 'newname' #   value updated
# # update method
# student.update({'name' : 'abcdef', 'age' : '25', 'phone' : '999-999-999'})

# # del student['age']

# if 'addr' in student:
#     del student['addr']
# else:
#     print('not found')

# #   popitem() - deletes the last key
# age = student.pop('age') # pop deletes the value from the dictionary but returns it in another variable
# print(student)
# print(age)
# print(len(student)) # will count the keys
# print(student.keys()) # will return a list of keys only in dictionary
# print(student.values())  # values only


# for key in student:
#     # print(key)
#     # print(student[key])
#     print(key, ':', student[key])
    
# print(student.items())

# for key in student.keys():
#     print(key, ':',key)
    
# for value in student.values():
#     print(key, ':',value)

# for key, value in student.items():
#     print(key, ':',value)
    
    
# print(student.get("name"))
# print(student.get("rollnum")) # will not throw error but return NONE if the key doesn't exits
# print(student.get("rollnum", 'Rollnum not found'))
# print(student['name'])
# print(student[True])
# print(student['courses'][1])

# if 'rollnum' in student:
#     print(student['rollnum'])
# else:
#     print("not found")