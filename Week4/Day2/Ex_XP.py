# #Ex 1 ✅

# #Create a set called my_fav_numbers with all your favorites numbers.
# favnumbers ={14,20,30,40}
# print(favnumbers)
# #Add two new numbers to the set.
# favnumbers.add(50)
# favnumbers.add(60)

# print(favnumbers)
# #Remove the last number.
# favnumbers.remove(60)
# print(favnumbers)
# #Create a set called friend_fav_numbers with your friend’s favorites numbers.
# friend_fav_numbers={1,2,3,4}
# print(friend_fav_numbers)
# #Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# our_fav_numbers= favnumbers.union(friend_fav_numbers)
# print(our_fav_numbers)


# Ex 2 ✅
# No


# # Ex 3 ✅
# for x in range(21):
#     if x!=0:
#         print(x)


# # Ex 4 ✅
# number_list=[]
# x=1.5
# index=1
# while x<=5.0:
#     if index%2 ==0:
#         number_list.append(int(x))
#         x=x+0.5
#         index=index+1
#     else:
#         index = index+1
#         number_list.append(x)
#         x=x+0.5
# print(number_list)

# # Ex 5 ✅
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# print(basket)
# # Remove “Banana” from the list.
# basket.remove('Banana')
# print(basket)
# # Remove “Blueberries” from the list.
# basket.remove('Blueberries')
# print(basket)
# # Add “Apples” to the beginning of the list.
# basket.append("Apples")
# print(basket)
# #Count how many apples are in the basket.
# print(basket.count("Apples"))
# #Empty the basket.
# basket=[]
# print(basket)


# #Ex 6 ✅
# #Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# my_name = "shmuel"
# user_name=input("Guess my name: ")
# while user_name!=my_name:
#     user_name=input("Guess again: ")

# print("Well Done!")

# # E7✅
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# for i in basket:
#     if basket.index(i) %2==0:
#         print(i)



# # Ex 8 ✅
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
# for x in range(1500,2500):
#     if x%7==0:
#         print(x)
#     elif x%5==0:
#         print(x)

# # Ex 9 ✅
# fruits = input("Please input your Favorite fruit: ")
# fruitlist = fruits.split(" ")
# newfruit = input("Enter a Fruit: ")
# if newfruit in fruitlist:
#     print("You chose one of your favorite fruits! Enjoy!")
    
# else:
#     print("You chose a new fruit. I hope you enjoy.")
      
# # Ex 10 ✅
# toppings =[]
# total = 10.00
# topping = input("Enter a pizza topping: ")
# while topping != "quit":
#     print(f"I'll put {topping} on your pizza")
#     toppings.append(topping)
#     topping = input("Enter another topping: ")
# for topping in toppings:
#     total +=2.5
#     print(topping)
# print(f'Total: {total}')

# # Ex11 ✅
# ages =input("Please enter the agees of everyone: ")
# total = 0
# ageslist = ages.split(" ")
# for age in ageslist:
#     a=int(age)
#     if 3<= a <=12:
#         total += 10
#     elif a > 12:
#         total+=15  
#     else: 
#         pass   
# print(f'Total: ${total}')

# Part 4
# names = input("Whats your name? ")
# permitted_list =[]
# while names != "done":
#     age= int(input("How old are you? "))
#     if 16<age<21:
#         permitted_list.append(names)
#         names = input("Whats your name? (Type done when finished) ")
#     else:
#         names = input("Whats your name? (Type done when finished) ")
        
# print(f'{", ".join(permitted_list)} can enter')

 


# #Ex 12✅

# name_list =["John", "Jake", "James", "Jacob", ]
# permitted_list =[]

# for name in name_list:
#     age = int(input(f"{name}, how old are you? "))
#     if age > 16:
#         permitted_list.append(name)
# print(permitted_list)





# # Ex 13✅
# sandwich_orders=["tuna","jam","chicken"]
# finished_sandwiches=[]
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
# for sandwich in finished_sandwiches:
#     print(f'I made your {sandwich} sandwich')

# #Ex 14 ✅
# sandwich_orders=["tuna","jam","chicken","pastrami","pastrami","pastrami"]
# finished_sandwiches=[]
# for sandwich in sandwich_orders:
#     finished_sandwiches.append(sandwich)
# for sandwich in finished_sandwiches:
#     print(f'I made your {sandwich} sandwich')



