#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''
"""
x = "apple"

def find(x):
 a_file = open("task01.txt", "r")
 list = [(line.strip()).split() for line in a_file]
 a_file.close()
 return list.index(x)

z = find(x)
print (z)
"""
"""
def find(x):
 return fitask01.txt.read()
def find(needle):
    pass


if __name__ == "__main__":
    assert find('apple') == 0
    assert find('fish') == 5
"""

list [1,2,3,4,5]

print (list.index(1))


