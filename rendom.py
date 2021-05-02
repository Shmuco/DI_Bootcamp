username = input("Enter your username: ")
password = input("Enter your password: ")

plength= len(password)
password_block= plength*'*'

print(f'{username}, your password {password_block}, is {plength} charecters long')