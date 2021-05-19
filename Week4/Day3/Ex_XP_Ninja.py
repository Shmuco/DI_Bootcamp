# # Ex 1
# import random
# li = [] 
# # 1. Instead of asking the user for 10 integers, generate 10 random integers yourself. 
# #    Make sure that these random integers are between -100 and 100.
# # 2. Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
# # 3. Will the code work when the number of random numbers is not equal to 10?
# for i in range(random.randint(50,1000)):
#     li.append(random.randint(-100,100))
# li2 =[]
# li_50 =[]
# li_10 =[]
# li_sq =[]
# li_nodub =[]
# print(li)
# print(sorted(li))
# sum_li = sum(li)
# print(sum_li)

# li2.append(li[0])
# li2.append(li[-1])
# print(li2)

# for i in li:
#     if i > 50:
#         li_50.append(i)
# print(li_50)

# for i in li:
#     if i < 10:
#         li_10.append(i)
# print(li_10)

# for i in li:
#     li_sq.append(i*i)
# print(li_sq)

# li_set = set(li)
# for i in li_set:
#     li_nodub.append(i)
# print(li_nodub)
# print(len(li_nodub))

# average = sum_li/len(li)
# print(f'Average: {average}')

# print(max(li))
# print(min(li))


# # Ex 2

# # Create a dictionary that contains users: each key will represent a username, and each value will represent that user’s password. Initialize this dictionary with 3 users & passwords.
# # Create a loop that does the following:
# # If the user inputs “exit”, break out of the loop.
# # If the user inputs “login”, ask them for their username and password.
# # If the user’s details exist print “you are now logged in”.
# # If the user is successfully logged in, store the username in a variable called logged_in so we can track it later.


# users = {
#     "James":"James123",
#     "Kiyle":"Kiyle123",
#     "John":"John123",
# }

# flag = True
# login = False
# while flag is True:
#     user_input = input('Whats your username? ')
#     if user_input == "exit":
#         flag = False
#     elif user_input in users:
#         password = input("Whats your password? ")
#         if password == users[user_input]:
#             print("log in successfull")
#             login = True
#             flag = False
#         else: print("Password incorrect")
#     else: print("User not found")


# Ex 3 

# Continuation of the Exercise Above - Authentication CLI - login

# If the user does not exist ask if they would like to sign up:
# Ask the user for a username and make sure it doesn’t exist as a key in our dictionary, if the username is not valid continue asking the user to input a username.
# Ask the user for a password. The password is the value.

# users = {
#     "James":"James123",
#     "Kiyle":"Kiyle123",
#     "John":"John123",
# }

# flag = True
# login = False
# while flag is True:
#     user_input = input('Whats your username? ')
#     if user_input == "exit":
#         flag = False
#     elif user_input in users:
#         password = input("Whats your password? ")
#         if password == users[user_input]:
#             print("log in successfull")
#             login = True
#             flag = False
#         else: print("Password incorrect")
#     else: 
#         q = input("User not found. Would you like to sign up? ")
#         if q == "yes":
            
#             new_user = user_input
#             if new_user not in users:
#                 new_password = input("Password: ")
#                 users[new_user] = new_password
#                 print("logged in and user created")
#                 login = True
#                 flag = False
# print(users)

