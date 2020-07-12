# A function is packaged together to perform a certain task
# A function can do a specific purpose into a single location
# keep your code DRY
# focus on input and what it returned

# Lecture
#? Passing value by argument v. reference
# 1. I'm changing the object
# 2. 

# define a doubling function that passes args by value
# x = 1
# def mult2(x):
#    return x * 2

# define a doubling function that passes args by reference
# def mult2_list(l):
#     for i in range(len(l)):
#         l[i] *= 2
        # no return statement is needed

# try out our Functions
# y = 12
# mult2(mult2(y))
# print(mult2(y))
# print(f'y= {y}')

# l = [3, 7, 13]
# mult2_list(l)

# for i in l:
#     print(i)

# End of lecture


# recorded video - Artem
# define a doubling function that passes args by value
# pass by value - the value of that number is copied - dupe of a cup and it's a brand new cup
# a second copy of some_num - a temporary variable of the value 12 created somewhere in the memory
def mult2(x):
    return x * 2 # making a copy of the variable

# define a doubling function for a list of variables passed by reference - if it's not a basic variable
# it's a list and it doesn't get copied because a list could get very long and big to make a copy over and over again
# l is a pointer to some list that exist somewhere else, that's why we don't have to return it due to memory
# def mult2_list(l):
#     for i in range(len(l)):  ## memorize!
#         l[i] *= 2
    # return l - no need to return it because it's being passed by reference, not a copy

# some_num = 12 # stores it in memory
# y = mult2(12)
# print(y)

# sort of C looking code
# new_array = malloc(4)

# just a pointer
# some_nums = [1,2,3,4]
# print(some_nums)

# mult2_list(some_nums)
# print(some_nums)

# End of recorded video


# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

