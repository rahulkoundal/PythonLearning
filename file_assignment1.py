"""
Write a program that prompts for a file name, then opens that file and reads through the file,
 and print the contents of the file in upper case. Use the file words.txt to produce the output below.

You can download the sample data at http://www.py4e.com/code3/words.txt
"""

file_name = input("Enter file name: ")

try:
    file_handle = open(file_name)
except Exception as e:
    print(e)
    quit()

for line in file_handle:
    print(line.rstrip().upper())
print(file_handle)

print(type(file_handle))

print(dir(file_handle))

