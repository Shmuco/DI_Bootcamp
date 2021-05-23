import requests
import time
import os

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]


def board_maker(board, level):
    size = 9
    level = level
    response = requests.get(f"http://www.cs.utep.edu/cheon/ws/sudoku/new/?size={size}&level={level}")
    game_board = response.json()['squares']

    for i in game_board:
        board[i['x']][i['y']]=i['value']
       




def solve (board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row ,col = find
    
    for i in range(1,10):
        if valid(board,i,(row,col)):
            board[row][col] = i

            # Keeps sending the updated board through solve 
            # unill the board is compleate and the retun is hit .
                
            if solve(board): 
                return True

            board[row][col]= 0
    


def valid(bo, num, pos):
    
    # Row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Colum
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3): 
        for j in range(box_x*3, box_x*3 + 3): 
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(board,f):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            f.write("-----------------------\n")

        
        for j in range(len(board[0])): 
            if j % 3 == 0 and j != 0:
                f.write(" | ")
            # Prints every number next to each other unless it the last
            if j == 8:
                f.write(str(board[i][j])+'\n')
            else:
                f.write(str(board[i][j])+ " ")
            
    
def find_empty (board):
    # functions searches for an empty space ie one that equals 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # row,colum

    return False


def menu():
    f = open('sudoku.txt','w')
    level = input('Welcome to the Sudoku maker. Please choose your level of dificulty 1-3: ')
    s_time= time.perf_counter()
    f.write(f'Sudoku Level: {level}\n\n')
    board_maker(board, level)
    print_board(board,f)
    solve(board)
    f.write("\n\n\n\n\n\n\n\nSOLVED BOARD\n\n")
    print_board(board,f)
    e_time = time.perf_counter()

    f.close
    os.system('open ./sudoku.txt')
    print(f"\nTIME: {e_time-s_time}")


menu()