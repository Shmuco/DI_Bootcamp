import random
# 1. Create a new python file and import your Dog class from the previous exercise.
from Ex_XP import dog

# 2. In the new python file, create a class named PetDog that inherits from Dog.
class PetDog(dog):
# 3. Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
# 4. train: prints the output of bark and switches the trained boolean to True
    def train(self):
        self.bark()
        self.trained = True
#    play: takes a parameter which value is a few names of other dogs (use *args). 
#    The method should print the following string: “dog_names all play together”. 
    def play(*args):
        dog_names =[]
        for dogs in args:
            dog_names.append(dogs.name)
        dog_names= ", ".join(dog_names)
        print(f'{dog_names} all play together!')
        print(dog_names)

    def do_a_trick(self):
        tricks =["does a barrel roll", "stands on his back", "shakes your hand","plays dead" ]
        num = random.randint(0,3)
        print(f'{self.name} {tricks[num]}.')
        



harry= PetDog("Harry", 12,12,)
eric= PetDog("Eric", 12,12,)
harry.play(eric)
harry.train()
eric.do_a_trick()
