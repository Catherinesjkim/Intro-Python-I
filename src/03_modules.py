"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# "do-it-yourself" with sys.argv
# The sys module implements the command line arguments in a simple list structure named sys.argv

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# print(sys.argv)
# for arg in sys.argv:
#     print(arg)
# argv will give us an array of arguments in the command line (add a bunch of words or numbers) and pass into the program. 
# It's a list obtained via the library sys: ['03_modules.py', 'argument1', 'argument2', 'argument12']

# Print out the OS platform you're using:
# YOUR CODE HERE
# print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
# print(sys.version)
# 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
# C compiler & version under the hood: [Clang 6.0 (clang-600.0.57)]

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# can write a script opening and closing processes - i.e. opening Spotify

# Print the current process ID
# YOUR CODE HERE
# print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
# print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
# print(os.getlogin())

# low level libraries like commands: math, date time, etc. 