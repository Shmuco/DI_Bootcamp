# # Ex 1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1 = dict(zip(keys, values))
# print(dict1)

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict2={}
# for i,y in zip(keys, values):
#     dict2[y] = i
# print(dict2)

# #Ex 2
# total = 0
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# for people in family.keys():
#     if 3<= family[people] <=12:
#         total += 10
#     elif family[people] > 12:
#         total+=15
#     else:
#         pass
# print(total)

# # #Bonus
# names=[]
# ages=[]
# dict1={}
# total= 0

# name = input("Enter the name (type done if you're done): ")
# while name !="done":

#     age = input(f'Enter {name}s age: ')
#     names.append(name)
#     ages.append(age)
#     name = input("Enter the next name: ")
# # print(ages)
# # print(names)


# for people in dict1.keys():
#     if 3<= int(dict1[people]) <=12:
#         total += 10
#     elif int((dict1[people])) > 12:
#         total+=15
#     else:
#         pass
# print(f'Total: ${total}')

# Ex 3

# # Create a dictionary called brand which value is the information 
# # from part one (turn the info into keys and values).
# brand = {
#     'name': 'Zara',
#     'creation_date': '1975',
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors': ['Gap', 'H&M', 'Benetton'],
#     'number_stores': 7000,
#     'major_color':
#     {'France': 'blue',
#      'Spain': 'red',
#      'US': ['pink', 'green']},

# }
# # Change the number of stores to 2.
# brand['number_stores'] = 2
# print(brand)

# # Print a sentence that explains who Zaras clients are.
# client = brand['type_of_clothes']
# print(f"Zaras clients are {', '.join(client)}")

# # Add a key called country_creation with a value of Spain.
# brand['country_creation'] = 'Spain'
# print(brand)

# # Check if the key international_competitors is in the dictionary.
# # If it is, add the store Desigual.
# if "international_competitors" in brand:
#     print("The key exists")
# (brand['international_competitors']).append("Desigual")

# # Delete the information about the date of creation.
# del brand['creation_date']

# # Print the last international competitor.
# print(brand['international_competitors'][-1])
# print(brand['international_competitors'])

# # Print the major clothes colors in the US. 
# print(brand['major_color']['US'])

# # Print the amount of key value pairs (ie. length of the dictionary).
# print(len(brand))

# # Print the keys of the dictionary.
# print(brand.keys())

# # Create another dictionary called more_on_zara 

# more_on_zara = {
#     "creation_date": 1975, 
#     "number_stores": 10000,
# }

# # Use a method to add the information from 
# # the dictionary more_on_zara to the dictionary brand. 
# brand.update(more_on_zara)
# print(brand ['number_stores'])

# #  Print the value of the key number_stores. What just happened ?
# # the value number_stores was replaced with overwritten with the value from more_on_zara


# Ex 4

# Exercise 4 : Disney Characters

# Instructions

# Use this list :

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}









# # Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# disney_users_A={}
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# for count, value in enumerate(users):
#     disney_users_A[value]=count
# print(disney_users_A)

# # Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# disney_users_B={}
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# for count, value in enumerate(users):
#     disney_users_B[count]=value
# print(disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# disney_users_C={}
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# users_sorted = sorted(users)
# for count, value in enumerate(users_sorted):
#     disney_users_C[value]=count
# print(disney_users_C)


# # Only recreate the 1st result for:
# # The characters, which names contain the letter “i”.
# disney_users_A={}
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# for count, value in enumerate(users):
#     if ("i" in value) == False:
#         disney_users_A[value]=count
#         print("works")
#     else: continue
# print(disney_users_A)

# # The characters, which names start with the letter “m” or “p”.
# disney_users_A={}
# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# for count, value in enumerate(users):
#     if ((value.startswith("M")) or (value.startswith("P")))==0:
#         disney_users_A[value]=count

    
# print(disney_users_A)