# username = input("Enter your username: ")
# password = input("Enter your password: ")

# plength= len(password)
# password_block= plength*'*'

# print(f'{username}, your password {password_block}, is {plength} charecters long')

school = {'Bobby','Tammy','Jammy','Sally','Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

for name in school:
    if name not in attendance_list:
        print(name)