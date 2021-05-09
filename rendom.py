# username = input("Enter your username: ")
# password = input("Enter your password: ")

# plength= len(password)
# password_block= plength*'*'

# print(f'{username}, your password {password_block}, is {plength} charecters long')

# school = {'Bobby','Tammy','Jammy','Sally','Danny'}
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

# for name in school:
#     if name not in attendance_list:
#         print(name)


some_list = ['a','b','c','b','d','m','n','n']

duplicates = list(set([i for i in some_list if some_list.count(i)>1 ]))
print(duplicates)