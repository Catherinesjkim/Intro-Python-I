"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# syntactic sugar for loops - shortcut 
# create a new list containing the squares of all values in 'numbers'
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# long way
# squares = []
# for num in numbers:
# 	squares.append(num*num)

# list comprehension - short way
# squares = [num*num for num in numbers]

# create a new list containing only even values of 'numbers'
# long way
# evens = []
# for num in numbers:
# 	if num % 2 == 0:
# 		evens.append(num)

# short way
# evens = [num for num in numbers if num % 2 == 0] 
# print(evens)


# create a new list containing only the names that start with "s" so that they are properly capitalized (regardless of how the name originally appears)
# names = ["Sarah", "Jorge", "sam", "bobby", "steph"]
# s_names = [name.capitalize() for name in names if name[0].lower() == 's']
# print(s_names)

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

# y = []

# print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# y = []

# print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

# a = ["foo", "bar", "baz"]

# y = []

# print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

# x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
# y = []

# print(y)