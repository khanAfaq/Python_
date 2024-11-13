# Different operations on the list:
print('\n')

numbers=[1,4,6,7,9]
# add item at end of the list,
numbers.append(8)
print(numbers)

print('\n')

# insert take index position at which you want to add a number:
numbers.insert(6,10)
print(numbers)

print('\n')
numbers.remove(10)
print(numbers)

print('\n')

# remove last item in the list pop():
numbers.pop()
print(numbers)

print('\n')

print(numbers.index(7))

print('\n')

# How to check that the specfic item is in the list
print(50 in numbers)

print('\n')

afaq=[1,2,2,3,8,9]
print(afaq.count(2))

print('\n')

ahmad=[9,5,3,1,2,4]
ahmad.sort()
print(ahmad)

# Sort the number in ascending order:
ahmad.reverse()
print(ahmad)

print('\n')

# How to take copy of a list:
num=[1,8,5,7]
num2=num.copy()
num.append(4)
print(num2)
print(num)

