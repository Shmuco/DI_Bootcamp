# # Exercise 1: Birthday Look-Up

# # Instructions

# # 1. Create a variable called birthdays. Its value should be a dictionary.
# # 2. Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be 
#  #   the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# birthdays = {
#     'James':'2000/05/13',
#     'Harry':'1994/11/13',
#     'Herbert': '1986/08/09',
#     'Greg': '1909/03/28',
#     'Zack': '1854/12/12'
# }
# # 3. Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# print('Welcome, you can look up the birthdays of the people in the list')
# #    1. Ask the user to give you a person’s name and store the answer in a variable.
# user_input = input('Please enter the name: ')
# #    2. Get the birthday of the name provided by the user.
# birthday = birthdays[user_input]
# #    3. Print out the birthday with a nicely-formatted message.
# print(f'{user_input}s birthday is: {birthday}')

# # Ex 2
# # 1. Before asking the user to input a person’s name print out all of the names in the dictionary.
# birthdays = {
#     'James':'2000/05/13',
#     'Harry':'1994/11/13',
#     'Herbert': '1986/08/09',
#     'Greg': '1909/03/28',
#     'Zack': '1854/12/12'
# }
# print('Welcome, you can look up the birthdays of the people in the list')
# for i in birthdays:
#     print(i)
# user_input = input('Please enter the name: ')


# # 2. If the person that the user types is not found in the dictionary, print an 
# #    error message (“Sorry, we don’t have the birthday information for <person’s name>”)
# if user_input in birthdays:
#     print(f'{user_input}s birthday is: {birthdays[user_input]}')
# else: print(f'Sorry, we don’t have the birthday information for {user_input}')


# Ex 3

# birthdays = {
#     'James':'2000/05/13',
#     'Harry':'1994/11/13',
#     'Herbert': '1986/08/09',
#     'Greg': '1909/03/28',
#     'Zack': '1854/12/12'
# }

# # 1. Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# new_name = input('Enter a new name: ')
# new_birthday = input(f'Enter {new_name}s birthday YYYY/MM/DD: ')
# birthdays[new_name]=new_birthday
# print('Welcome, you can look up the birthdays of the people in the list')
# for i in birthdays:
#     print(i)
# user_input = input('Please enter the name: ')

# if user_input in birthdays:
#     print(f'{user_input}s birthday is: {birthdays[user_input]}')
# else: print(f'Sorry, we don’t have the birthday information for {user_input}')


# # Ex 4

# items = {"banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3}
# # 1. Print all the items and their prices in a sentence.
# for i in items:
#     print (f'The price of a {i} is ${items[i]}')

# # 2. Change the value of all the keys to dictionaries containing both the price and the amount of items in stock.

# items = {("banana", 4): 2,
#     ("apple", 2): 4,
#     ("orange", 1.5): 2,
#     ("pear", 3): 1}
# # 3.Once you’ve added the stock details write some code to calculate how much it would cost to buy everything in stock.

# total = 0
# for i in items:
#     cost = i[1]*items[i]
#     print(cost)
#     total += cost
# print(total)


# # Ex 5
# # 1. Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# # 2. Convert it into a list using Python (don’t do it by hand!).
# li = string.split(",")

# # 3. Print out a message saying how many manufacturers/companies are in the list.
# print(len(li))

# # 4. Print the list of manufacturers in reverse/descending order (Z-A).
# li.sort(reverse= True)
# print (li)

# # 5. Using loops or list comprehension:
# #    - Find out how many manufacturers’ names have the letter ‘o’ in them.
# counter = 0 
# for i in li:
#     if 'o' in i:
#         counter += 1
# print(counter)

# #   - Find out how many manufacturers’ names do not have the letter ‘i’ in them.
# counter = 0 
# for i in li:
#     if 'i' in i == False:
#         counter +=1
# print(counter)

# # 6. Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# li_2 = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# # - Remove these programmatically. (Hint: you can use sets to help you).
# li_2_set = set(li_2)

# # - Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), 
# #   also print out a message saying how many companies are now in the list.
# # counter = 0
# print(f'There are {len(li_2)} companies in the list of {",".join(li_2_set)}.')

# # 7. Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
# li_2.sort()

# final = []
# for i in li_2:
#     word = i[::-1]
#     word = "".join(word)
#     final.append(word)
# print(final)




