# ============================ VARIABLES ============================

# variable types -- string literal, int, bool, float

a, b, c = 10, 5, 3
a = b = c = 10

print(a, b, c)

a = 10
b = 'abcd'
c = 3.1
d = True
print('type: ',type(a))
print('type: ',type(b))
print('type: ',type(c))
print('type: ',type(d))

message1 = 'python\'s world'
message2 = "python's world"
message3 = '''    python

's

    world'''

print(message3)

message4 = 'hello' + 'world' + '!'
print(message4)

message5 = 'hello!' * 5
print(message5)



# ============================ FUNCTIONS ============================

# return type
# name
# parameters/ arguments

# len 
# help

# --- string functions
# upper() 
# lower() 
# count() 
# find() 
# replace() 
# split 
# stip 
# string[]

# ===================================================================

message = 'Hello World!'
print('length: ',len(message))
print(message[0])
print('last char: ', message[len(message) - 1])
print(message[6:9]) #   6 start and end at 8 printing 8 and excluding 9
print(message[0:5])
print(message[:5])
# print(message[5:])

# new_message = message.lower()
# new_message2 = message.upper()
# print(new_message)
# print(new_message2)
# print(message.lower())
# print(message.count())

# print(help(len))

MSG = "You are learning pyThon! PYTHON'S AWESOM"

new_message = MSG.lower()

check = 'pyTHon'         
check2 = check.lower()

print(new_message.count(check2))

print(MSG.lower().count('PytHoN'.lower()))

print(message.find('Wor'))
print(message[3:].find('l')) #  this will print 0 becase its now starting from 0

# new_msg = message.replace(x, y)
mesg = 'Hello World! Hello'
new_msg = mesg.replace('hello', 'python')
new_msg2 = mesg.lower().replace('heHlo'.lower(), 'python')
print(new_msg)
print(new_msg2)

name = '        Zahra   Qaisar    '

print(name.strip())

print(message.split(' '))



# message = 'world'

# new = len(message)
# last = new - 1
# mid = new // 2
# print(new)

# # f = message[:1]
# f = message[0]
# m = message[mid]
# l = message[last]

# print(f+m+l)

message = 'wonderland'

new = len(message)
mid = new // 2
print(message[mid])
fst = message[mid-1]
md = message[mid]
lst = message[mid + 1]
print(fst+md+lst)

print(message[mid-1:mid+2])


s1 = 'hello'
s2 = 'world'

mid = len(s1) // 2
# print(s1[mid])

new = s1[:mid+1] + s2 + s1[mid+1:]
print(new)

s1 = 'hello'
s2 = 'world'

length = len(s1)
last = length - 1
mid = length // 2
f = s1[0]
m = s1[mid]
l = s1[last]

length2 = len(s2)
last = length2 - 1
mid = length2 // 2
f2 = s2[0]
m2 = s2[mid]
l2 = s2[last]

print(f, m, l)
print(f2, m2, l2)

print(f + f2 + m + m2 + l + l2)

# s1="hello"
# s2="world"
# begin_s1=s1[0]
# begin_s2=s2[0]
# mid_s1=len(s1)//2
# mid_s2=len(s2)//2
# end_s1=len(s1)-1
# end_s2=len(s2)-1

# print(begin_s1+begin_s2+mid_s1+mid_s2+end_s1+end_s2)

# ============================ ENCRYPTION ============================

# encryption
# hashing - encypted but cannotbe decrypted
# salting - adding random char 

# ============================ FORMAT, F STRING ============================

name = 'Product'
price = 3000
quantity = 5

# s = '{} {}$'.format(name, price)
s = f'{name} {price}$'
s = f'{name.lower()} {price * quantity}$'

# ============================ TYPE CASTING ============================

x = int(5) # type casting the variable in int
s = int('50')
y = s+1
print(y)
z = int(float("50.5"))
print(z)

i = 5.75
print(round(i))
print(round(i, 1))


