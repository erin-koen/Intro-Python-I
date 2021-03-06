"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
def read_and_print(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            print(line)

read_and_print('./src/foo.txt')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

newfile = open('./src/bar.txt', 'w')
newfile.write('Line 1\n')
newfile.write('Line2\n')
newfile.write('Line3\n')
newfile.close()