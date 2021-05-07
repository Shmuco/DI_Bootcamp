import random
class Game ():
    def __init__(self,game):
        self.game = game
    
    
    def get_user_item(self):
        active = True
        while active:
            user = input("Please select (r)ock, (p)aper or (s)cissors: ")
            if user == "r":
                user = "rock"
            elif user == "p":
                user = "paper"
            elif user == "s":
                user = "scissors"
            if user == 'rock' or user == 'paper' or user == 'scissors':
                active = False
        return user


    def get_computer_item(self):
        li = ["rock", "paper", "scissors"]
        computer = random.choice(li)
        return computer

    def get_game_result(self, user, computer):
        if user == computer:
            print(f'You selected {user} and the computer selected {computer}\nYou Drew.')
            return "draw"
        elif user == "rock" and computer == "scissors":
            print(f'You selected {user} and the computer selected {computer}\nYou Won!')
            return "win"
        elif user == "scissors" and computer == "rock":
            print(f'You selected {user} and the computer selected {computer}\nYou lost.')
            return "loss"
        elif user == "paper" and computer == "rock":
            print(f'You selected {user} and the computer selected {computer}\nYou Won!')
            return "win"
        elif user == "rock" and computer == "paper":
            print(f'You selected {user} and the computer selected {computer}\nYou lost!')
            return "loss"
        elif user == "scissors" and computer == "paper":
            print(f'You selected {user} and the computer selected {computer}\nYou Won!')
            return "win"
        elif user == "paper" and computer == "scissors":
            print(f'You selected {user} and the computer selected {computer}\nYou lost!')
            return "loss"
        




