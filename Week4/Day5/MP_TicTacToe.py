game_board ={
  1:1,
  2:2,
  3:3,
  4:4,
  5:5,
  6:6,
  7:7,
  8:8,
  9:9,
}


def display_board():
    board = f'''

       TIC TAC TOE
    *****************
    *   {game_board[1]} | {game_board[2]} | {game_board[3]}   *
    *  - -|- -|- -  *
    *   {game_board[4]} | {game_board[5]} | {game_board[6]}   *
    *  - -|- -|- -  *
    *   {game_board[7]} | {game_board[8]} | {game_board[9]}   *
    *****************
    '''
    print(board)
    

  
def winner_check():
  if (game_board[1] == 'X') & (game_board[2]=='X') & (game_board[3]== 'X'):
    display_board()
    print("Player X is the winner!!")
    exit()
  elif (game_board[1] == 'O') & (game_board[2]=='O') & (game_board[3]== 'O'):
    display_board()
    print("Player O is the winner!!")
    exit()
  elif (game_board[4] == 'X') & (game_board[5]=='X') & (game_board[6]== 'X'):
    display_board()
    print("Player X is the winner!!")
    exit()
  elif (game_board[4] == 'O') & (game_board[5]=='O') & (game_board[6]== 'O'):
    display_board()
    print("Player O is the winner!!")
    exit()
  elif (game_board[7] == 'X') & (game_board[8]=='X') & (game_board[9]== 'X'):
    display_board()
    print("Player X is the winner!!")
    exit()
  elif (game_board[7] == 'O') & (game_board[8]=='O') & (game_board[9]== 'O'):
    display_board()
    print("Player O is the winner!!")
    exit()
  elif (game_board[1] == 'X') & (game_board[5]=='X') & (game_board[9]== 'X'):
    display_board()
    print("Player X is the winner!!")
    exit()
  elif (game_board[1] == 'O') & (game_board[5]=='O') & (game_board[9]== 'O'):
    display_board()
    print("Player O is the winner!!")
    exit()
  elif (game_board[3] == 'X') & (game_board[5]=='X') & (game_board[7]== 'X'):
    display_board()
    print("Player X is the winner!!")
    exit()
  elif (game_board[3] == 'O') & (game_board[5]=='O') & (game_board[7]== 'O'):
    display_board()
    print("Player O is the winner!!")
    exit()
  elif (game_board[1]!=1) and (game_board[2]!=2)and (game_board[3]!=3)and (game_board[4]!=4)and (game_board[5]!=5)and (game_board[6]!=6)and (game_board[7]!=7)and (game_board[8]!=8)and (game_board[9]!=9):
    display_board()
    print("Its a tie!")
    exit()
  
  



def player_input_x():
    play=input("Player X, choose a square (1-9): ")
    if play.isdigit():
      play=int(play)
      if(0<play<10) and game_board[play]== (play):
          game_board[play] ="X"

          winner_check()
          display_board()
          player_input_O()
      else:
        player_input_x()
    else:
      player_input_x()

def player_input_O():
    play=input("Player 0, choose a square (1-9): ")
    if play.isdigit():
      play=int(play)
      if(0<play<10) and game_board[play]== play:
              game_board[play] ="O"

              winner_check()
              display_board()
              player_input_x()
      else:
        player_input_O()
    else:
      player_input_O()
    
    

display_board()
player_input_x()