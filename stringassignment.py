"""
Write code using find() and string slicing (see section 6.10)
 to extract the number at the end of the line below. Convert
 the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475"

number_starting_index = text.find('0')

print(number_starting_index)

number_value = float(text[number_starting_index:])

print(number_value)

print(type(number_value))

