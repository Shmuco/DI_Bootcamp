import math
class circle():
    def __init__(self, radius, diameater=0):
        self.radius = radius
        self.diameater = radius*2
    def area(self):
        area = self.radius*self.radius*math.pi
        print(area)
    def __str__(self):
        return f'This circle has a radis of {self.radius} and a diameter of {self.diameater}'
    def __add__(self, other):
        com_radius = self.radius+other.radius
        com_diameater = self.diameater+other.diameater
        return f'Combined radius = {com_radius}\nCombined diameter = {com_diameater}'
    def __lt__(self, other):
        if self.radius<other.radius:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.radius>other.radius:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.radius==other.radius:
            return True
        else:
            return False
    def list_sort(self,*args):
        li=[]
        for i in args:
            li.append(i.radius)
        print(li)
        print(sorted(li))
    
    


circle(6)
six = circle(6)
seven = circle(7)
eight = circle(8)
nine = circle(9)

six.area()
print(six.diameater)
print(six)
print(six+seven)
print(six>seven)
print(six==seven)
six.list_sort(eight,seven,nine)