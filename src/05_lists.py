# Lecture
# l = []

# create a list with numbers
# num_list = [1, 2, 3, 4]

# add element to empty list
# l.append(77)

# print all values in num_list
# for element in num_list:
#     print(element) 

# get index and the value - the position of each cell in num_list
# if you want the index of the element, use enumerate to access
# for (i, elem) in enumerate(num_list):
# 	print(f'Element {i} is {elem}')

# n -1 entity
# for x in range(10):
# 	print(x)

# End of Lecture 


# Project

# For the exercise, look up the methods and functions that are available for use
# with Python lists

# x = [1, 2, 3]
# y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
# x.append(4)
# print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
# x.extend(y)
# print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
# x.remove(8)
# print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
# x.insert(5, 99)
# print(x)

# Print the length of list x
# YOUR CODE HERE
# print("Number of items in the list is ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# x = map(lambda x: x*1000, x)
# print(list(x))
