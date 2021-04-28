# # Ex 1
# def display_message():
#     print("I am currently learning python")

# display_message()

# # Ex 2
# def favorite_book(title):
#     print (f'One of my favorite books is {title}.')

# favorite_book(input('Name a book: '))

# # Ex 3
# def describe_city(city, country):
#     print(f'{city} is in {country}')
# describe_city(input('Name a city: '), input('What country is it in? '))


# #Ex 4
# import random
# def num_game(num):
#     random_number = random.randint(1, 100)
#     if num==random_number:
#         print("Success!!")
#     else:
#         print(f'The number was {random_number} Maybe next time.')


# num_game(int(input('Guess a number between 1 and 100: ')))


# # Ex 5
# def make_shirt(size= "Large", message="I love Python" ):
#     print (f'Shirt Size: {size} \nMessage: {message}')


# make_shirt()
# make_shirt("Medium",)
# make_shirt("Small","I prefer JS")

#Ex 6

# # Make a list of magician’s names.
# names = ["Lila", "Gandalf", "Harry", "Neville Longbottom"]
# great_list=[]
# # Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# def show_magicians(list):
#     for i in list:
#         print(i)
# show_magicians(names)


# # #Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# def make_great(li):
#     for i in li:
#         i= great_list.append(f'{i} the great')
# make_great(names)
# print(names)
# show_magicians(great_list)


