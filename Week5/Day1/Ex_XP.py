# # Exercise 1: Cats

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def oldest_cat_finder(list):
#     oldest_cat=all_cats[0]
#     for cat in all_cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat=cat
#     print(f'The oldest is {oldest_cat.name} and who is {oldest_cat.age}')

# cat1 = Cat("Tom", 4)
# cat2 = Cat("Bob", 7)
# cat3 = Cat("Gary", 1)

# all_cats=[cat1, cat2, cat3]
# oldest_cat_finder(all_cats)


# # Ex 2

# # 1. Create a class called Dog.
# # 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.


# class Dog:
#     def __init__(self,name,height):
#         self.name = name
#         self.height = height
# # 3. Create a method called bark that prints the following string “<dog_name> goes woof!”.
#     def bark(self):
#         print(f'{self.name} goes woof!')
# # 4. Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#     def jump(self):
#         print(f'{self.name} jumps {self.height*2}cm high!')

# # 5. Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# davids_dog = Dog("Rex", 50)
# # 6. Print the details of his dog (ie. name and height) and call the methods bark and jump.
# print(davids_dog.name, davids_dog.height)
# Dog.bark(davids_dog)
# Dog.jump(davids_dog)

# # 7. Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# sarahs_dog = Dog("Teacup", 20)
# # 8. Print the details of her dog (ie. name and height) and call the methods bark and jump.
# print(sarahs_dog.name, sarahs_dog.height)
# Dog.bark(sarahs_dog)
# Dog.jump(sarahs_dog)
# # 9. Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# if sarahs_dog.height > davids_dog.height:
#     print(f'{sarahs_dog.name} is bigger')
# else:
#     print(f'{davids_dog.name} is bigger')
 

# # Exercise 3 
# class song:
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
# def sing_me_a_song(self):
#     for line in self.lyrics:
#         print(line)

# stairway= song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# sing_me_a_song(stairway)


# # Exercise 4 : Afternoon At The Zoo
# 1. Create a class called Zoo.
# 2. In this class create a method __init__ that takes one parameter: zoo_name.
#    It instantiates two attributes: animals (an empty list) and name (name of the zoo).
class zoo:
    def __init__(self,zoo_name):
        self.name=zoo_name
        self.animals=[]
# 3. Create a method called add_animal that takes one parameter new_animal. 
#    This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self,animal_name):
        self.animals.append(animal_name)
# 4. Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self):
        print(self.animals)
        # for names in self.animals:
        #     print(names)
# 5. Create a method called sell_animal that takes one parameter animal_sold. 
# This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        print(self.animals)
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.     
    def sort_animals(self):
        self.animals.sort()


london_zoo = zoo("London")
london_zoo.add_animal("cat",)
london_zoo.add_animal("dog")
london_zoo.add_animal("pig")
london_zoo.add_animal("badger")
london_zoo.get_animals()
london_zoo.sell_animal("pig")
london_zoo.get_animals()
london_zoo.sort_animals()
london_zoo.get_animals()








