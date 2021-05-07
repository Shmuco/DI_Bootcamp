from game import Game



def play(self):
    comp_play = self.get_computer_item()
    user_play = self.get_user_item()
    result = self.get_game_result(user_play, comp_play)
    
    return(result)
    



def menu():
    main_menu = print(f'''

        Menu:
        (g) Play a new Game
        (x) Show scores and exit the
        ''')
    user_input = input()
    return user_input


game_on = True

win = 0
loss = 0
draw = 0
while game_on:
    user_input = menu()
    if user_input == "g":
        game_start = Game("start")
        game_result = play(game_start)
      
    

        if game_result == "draw":
            draw +=1
        elif game_result == "win":
            win +=1
        elif game_result == "loss":
            loss +=1
        print(f'''
        Game Results:
        You won {win} times
        You lost {loss} times
        You drew {draw} times
        ''')




    elif user_input == "x": 

        print(f'''
        Final Results:
        You won {win} times
        You lost {loss} times
        You drew {draw} times
        ''')

        print('Thanks for playing!')
        game_on = False

