# print("hello owrld")
# x = 5

# def greet(name):
#     print("hello", name)
    
# person1 ={
#     'name ' : 'Zahra',
#     'age' : 20
# }

import os 
os.chdir('test')
d = os.listdir()

for x in d:
    path = os.path.join(os.getcwd(), x)
    # os.remove(path)
    print(path)