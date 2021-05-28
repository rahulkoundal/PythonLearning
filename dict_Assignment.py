

email_dict = dict()
try:
    file_name = input("Please enter the file name:")
    file_handle = open(file_name)
except Exception as e:
    print(e)
    quit()

for line in file_handle:
    if line.startswith('From '):
        email_list = line.split()
        email = email_list[1]
        email_dict[email] = email_dict.get(email, 0) + 1


big_word = big_count = None

for key, value in email_dict.items():
    if big_count is None or value > big_count:
        big_word = key
        big_count = value

# print(big_word, big_count)

for i in email_dict:
    print(i)

