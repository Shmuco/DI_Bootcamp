class charecter():
    def __init__(self, name):
        self.name = name
        self.life = 20.0
        self.attack = 10.0
    
    def basic_attack(self, other_charecter):
        other_charecter.life-=10
        print(f'{other_charecter.name}s attack is {other_charecter.attack}')

class druid(charecter):
    def meditate(self):
        self.life+=10
        print(f'{self.name}s life is {self.life}.')
        self.attack-=2
        print(f'{self.name}s attack is {self.attack}.')
    def animal_help(self):
        self.attack+=5
        print(f'{self.name}s attack is {self.attack}.')
    
    def fight(self, other_charecter):
        other_charecter.life-=(0.75*self.life + 0.75*self.attack)
        print(f'{other_charecter.name}s life is {other_charecter.life}')


class warrior(charecter):
    def brawl(self, other_charecter):
        other_charecter.life-=(2*self.attack)
        print(f'{other_charecter.name}s life is {other_charecter.life}')
        self.attack+=(0.5*self.attack)
        print(f'{self.name}s attack is {self.attack}.')
    
    def train(self):
        self.attack+=2
        print(f'{self.name}s attack is {self.attack}.')

    def roar(self, other_charecter):
        other_charecter.attack-=3
        print(f'{other_charecter.name}s attack is {other_charecter.attack}')
    
    

class mage(charecter):
    def curse(self,other_charecter):
        other_charecter.attack-=2
        print(f'{other_charecter.name}s attack is {other_charecter.attack}')
    
    def summon(self):
        self.attack+=3
        print(f'{self.name}s attack is {self.attack}.')
    
    def cast_spell(self, other_charecter):
        other_charecter.life-=(self.attack/self.life)
        print(f'{other_charecter.name}s life is {other_charecter.life}')


james = druid('james')
harry = warrior('harry')
yankey = mage('yankey')
# james.meditate()
# print(james.life)
# print(james.attack)

    
        