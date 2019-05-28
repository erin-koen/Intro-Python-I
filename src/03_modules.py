"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print ('before')
print (sys.argv)
print('after')
# Print out the OS platform you're using:
# YOUR CODE HERE
osPlatform = sys.platform
print (osPlatform)


# Print out the version of Python you're using:
# YOUR CODE HERE

version = sys.version

print (version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
process_id = os.getpid()
print ('process ID ' + str(process_id))

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print ('cwd ' + cwd)

# Print out your machine's login name
# YOUR CODE HERE
loginName = os.getlogin()
print('login ' + loginName)
