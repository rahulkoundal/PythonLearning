"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list
 of words using the split() method. The program should build a list of words.
 For each word on each line check to see if the word is already in the list
 and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
"""

words_list = list()
try:
    file_name = input("Please enter the file name:")
    file_handle = open(file_name)
except Exception as e:
    print(e)
    quit()

for line in file_handle:
    line = line.strip().split()
    for i in line:
        if i not in words_list:
            words_list.append(i)


words_list.sort()
print(words_list)


