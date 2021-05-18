import random

class personna:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.strength = self.roll_dice()   
        self.dexterity = self.roll_dice()   
        self.constitution = self.roll_dice()   
        self.intelligence = self.roll_dice()   
        self.wisdom = self.roll_dice()   
        self.chrisma = self.roll_dice()   

    @staticmethod
    def roll_dice():
        rolled_numbers = []
        for number in range (0,4):
            rolled_numbers.append(random.randint(1,6))
       
        rolled_numbers.remove(min(rolled_numbers))
        return sum(rolled_numbers)

class game:

    def __init__(self):
        self.num_of_players = int(input('How many players are playing? '))
        self.players = []
        for num in range (1, self.num_of_players+1):
            print(f'    Enter info for player #{num}    ')
            age = input('How old is your charecter? ')
            name = input('Whats your charecters name? ')
            player = personna (name, age)
            self.players.append(player)
        print(self.players)

    def write_to_text(self):
            write_string = f''' D&D Char Sheet

            total players: {len(self.players)}''' 

            for index,player in enumerate(self.players):
                add_string = f'''
                ___player #{index+1}___
                age: {player.age}
                name {player.name}
                strength: {player.strength}
                dexterity: {player.dexterity}
                constitution: {player.constitution}
                intelligence: {player.intelligence}
                widom: {player.wisdom}
                chrisma: {player.chrisma}

                
                '''
                write_string += add_string

            with open('game_txt_data.txt', 'w') as f:
                f.write(write_string)


        # def write_to_json(self):
        #     for player in 

g1 = game()
g1.write_to_text()