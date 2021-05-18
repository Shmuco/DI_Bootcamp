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

# Ex 2

class my_list:
    def __init__(self, letters):
        self.letters = letters
    
    def rev(self):
        self.letters.reverse()
        return self.letters


    def sorted(self):
        self.letters.sort()
        return self.letters
    
    def random_list(self):
        length = len(self.letters)
        random_list=[]
        for i in range(length):
            random_list.append(random.randint(0,100))
        return random_list




letters = my_list(['a','b','c','d','e','f','g','h','i','j','k'])

print(letters.rev())
print(letters.sorted())
print(letters.random_list())

# print (letters)