email_dict = dict()
try:
    file_name = input("Please enter the file name:")
    file_handle = open(file_name)
except Exception as e:
    print(e)
    quit()

for line in file_handle:
    if line.startswith('From '):
        hours = line.split()[5][:2]
        email_dict[hours] = email_dict.get(hours, 0) + 1

a = sorted([(k, v) for k, v in email_dict.items()])

for i, k in a:
    print(i, k)

print(email_dict)
