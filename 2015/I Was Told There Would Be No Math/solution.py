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
    area = 0
    ribbon = 0
    for line in content:
        output = [eval(i) for i in line.split("x")]
        output.sort()
        num_small = output[0]
        num_medium = output[1]
        num_large = output[2]
        area = area + 3*num_small*num_medium + 2*num_small*num_large + 2*num_large*num_medium
        ribbon = ribbon + 2*num_small + 2*num_medium + num_small*num_medium*num_large
    print(area)
    print(ribbon)