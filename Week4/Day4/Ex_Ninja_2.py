# # Ex 1 
# # Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# # middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# # For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee. 
# # But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

# def get_full_name(first_name, last_name, middle_name=""):
#     if len(middle_name)>0:
#         middle_name = f' {middle_name}'

#     print(f'{first_name}{middle_name} {last_name}')

# get_full_name(first_name="bruce", last_name="lee")
# get_full_name(first_name="john", middle_name="hooker", last_name="lee")


# # Ex 2 

# dict = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-', ' ':'/'}

# def encrypt(text):
#     letters = []
#     for i in text:
#         try:
#             morse = f'{dict[i.upper()]} ' 
#             letters.append(morse)
#         except:
#             morse = f'{dict[i]}'
#             letters.append(morse) 
#     return "".join(letters)

# def decrypt(text):
#     letters = []
#     text = text.split(" ")
#     for i in text:
#         for key, val in dict.items():
#             if val == i:
#                 letters.append(key.lower())
#     return "".join(letters) 


# # print(encrypt('hello world'))
    
# # print(decrypt(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. "))

# print(encrypt(input()))

# print(decrypt(input()))