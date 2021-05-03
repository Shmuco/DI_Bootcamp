# # # Ex 1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'
#         print(self.name)

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # 1. Create another cat bread. In order to do so, create a class which inherits from the Cat class.
# class Persian(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # 2. Create a few cat instances.
# jake = Bengal("jake", 12 )
# garfield = Persian("garfield",9)

# # 3. Create a list called my_cats, which will hold all the created cat instances.
# my_cats = [jake,garfield]

# # 4. Create a variable called my_pets. It’s value is an instance of the Pet class. 
# my_pets = Pets(my_cats)

# # 5. Take all the cats for a walk, use the walk method.
# for cat in my_cats:
#     print(cat.walk())


# Ex 2

class dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return(self.weight/self.age*10)
    def fight(self, other_dog):
        
        if other_dog.run_speed() > self.run_speed():
            print(f'{other_dog.name} won the fight')
        else:
            print(f'{self.name} won the fight')


scooby = dog("Scooby", 12, 60)
scrappy = dog("Scrappy", 6, 30)
pluto = dog("Pluto", 15, 70)

pluto.bark()
print(scrappy.run_speed())
scooby.fight(scrappy)


