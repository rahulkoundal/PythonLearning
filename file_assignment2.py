"""
Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:

X-DSPAM-Confidence: 0.8475

Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

fh = open(fname)

sum_value = extract_value = count_line = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        extract_index = line.find('0')
        extract_value = float(line[extract_index:])
        sum_value = sum_value + extract_value
        count_line = count_line + 1

print("Done", sum_value, count_line, sum_value/count_line)
