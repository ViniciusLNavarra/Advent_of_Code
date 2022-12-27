#!/usr/bin/env python
import os.path
import sys

# Define a filename.
if sys.platform.startswith('win32'):
    filename = os.getcwd() + "\input.txt"
else:
    filename = os.getcwd() + "/input.txt"

print(filename)

if not os.path.isfile(filename):
    print('File does not exist.')
else:
# Open the file as f.
# The function readlines() reads the file.
    with open(filename) as f:
        content = f.read().splitlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
    for line in content:
        floor = 0
        position = 1
        for i in line:
            if i == '(':
                floor+=1
                position+=1
            else:
                floor-=1
                if floor == -1:
                    print(position)
                position+=1
        print(floor)
