import math
import random

# # Ex 1

# class circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def perimiter(self):
#         print(f'Radius: {self.radius}\nCircuferance: {2*math.pi*self.radius}')

#     def area(self):
#          print(f'Radius: {self.radius}\nArea: {math.pi*self.radius**2}')

# cir = circle(5)

# cir.perimiter()
# cir.area()

# # Ex 2

# class my_list:
#     def __init__(self, letters):
#         self.letters = letters
    
#     def rev(self):
#         self.letters.reverse()
#         return self.letters


#     def sorted(self):
#         self.letters.sort()
#         return self.letters
    
#     def random_list(self):
#         length = len(self.letters)
#         random_list=[random.randint(0,100) for x in self.letters]
#         # for i in range(length):
#         #     random_list.append(random.randint(0,100))
#         return random_list




# letters = my_list(['a','b','c','d','e','f','g','h','i','j','k'])

# print(letters.rev())
# print(letters.sorted())
# print(letters.random_list())


# Ex 3

menu = [
    {
        'name': 'Soup',
        'price': 10,
        'spice_level': 'B',
        'gluten_index': False
    },
    {
        'name': 'Hamburger',
        'price': 15,
        'spice_level': 'A',
        'gluten_index': True
    },
    {
        'name': 'Salad',
        'price': 18,
        'spice_level': 'A',
        'gluten_index': False
    },
    {
        'name': 'French fries',
        'price': 5,
        'spice_level': 'C',
        'gluten_index': False
    },
    {
        'name': 'Beef bourguignon',
        'price': 25,
        'spice_level': 'B',
        'gluten_index': True
    },
]

class menu_manager:
    def __init__(self, menu):
        self.menu = menu
    
    def add_item(self,name,price,spice,gluten_index):
        menu.append({
            'name': name,
            'price': price,
            'spice_level': spice,
            'gluten_index': gluten_index
        })
        print(self.menu)

    def update_item(self,item,property,value):
        for i in self.menu:
            if i['name']==item:
                self.menu[self.menu.index(i)].update({property:value})
                return
        print("That item doesnt exist")
    
    def remove_item(self, item):
        for i in self.menu:
            if i['name']==item:
                self.menu.remove(i)
                print(self.menu)
                return
        print("That item doesnt exist")
        
        