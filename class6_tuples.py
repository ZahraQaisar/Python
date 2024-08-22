'''
    TUPLE
    
    list in tuple cannot be modified as it is in tuple
    
    tuple changed into list then changes in list are made and them list is changed into tuple
    
    del can be used directly
'''

cars = ('honda', 'toyota', 'suzuki')
print(cars[0])

# for simgle item tuple , at the end

car1 = ('honda') # considered as string
car2 = ('honda',) # considered as tuple
print(type(car1))
print(type(car2))

cars = ('honda', ['toyota', 'suzuki'])
cars2 = ('honda', ['toyota', 'suzuki'], 'bmw', 'Ford')
print(cars[1][0])
print(cars[-1])
print(cars[1:])

if 'toyota' in cars[1]:
    print("true")
else:
    print("false")
    
if 'toyota' in cars:
    print("true")
else:
    print("false")
    
# when * is used the rest of the values are stored as list in that variable

fruits = ("a", 'b', 'c', 's','raspberyy')
(green, blue, *red, purple) = fruits
print(green)
print(blue)
print(red)
print(purple)

# adding 2 tuples
t1 = ()
t2 = ()
t3 = t1 + t2

# multiplying tuples will copy the values in the tuples

t4 = t1 * 2

'''

    SETS
    
    list is not possible in set only str, int, float, bool

'''

set1 =set(('apple', 'banana', 'cherry', 'apple', 'apple'))
print(type(set1))
print(set1)

set1.add('orange')

if 'apple' in set1:
    print("yes")

for fruit in set1:
    print(fruit)
    
# update is basically add
# remove and discard

# removes throws error if the value is not in the set
# discards does not 

# pop deletes random value


set1 = set(('apple', 'banana', 'cherry'))
set2 = set(('apple','kiwi', 'grapes'))

set3 = set1.union(set2)
set3 = set1.union(set1)
set3 = set1 | set2 # unionn # this operator can be only used with set | set not other data struct
set3 = set1.intersection(set2)
set3 = set1.difference(set2)
set3 = set1.difference(set1)
set3 = set1.symmetric_difference(set2) # common values not included

print(set3)
