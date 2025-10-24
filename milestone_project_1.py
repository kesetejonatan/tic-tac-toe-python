# Skapar spelbrädet
board = [' '] * 10  # Index 0 använder vi inte, för enklare numrering

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-') 
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
   
    while True:
        position = input('Make your move (1-9): ')
        if position in ['1','2','3','4','5','6','7','8','9']:
            return position
        else:
            print ('Invalid number. You can only choose numbers between 1 and 9')

def place_marker(board,marker,position):

    board[int(position)] = marker

def check_win(board, marker):
    # Raderna
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True
    # Kolumnerna
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True
    # Diagonalerna
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False
    
def check_tie(board):
    for i in range (1,10):
        if board[i] == ' ':
            return False
    return True
    
def play_game():
    board = [' '] * 10
    game_on = True
    current_player = 'X'

    while game_on:
        display_board(board)
        position = player_input()
        place_marker(board,current_player,position)
        check_tie(board)
        
        if check_win(board,current_player):
            print(f'Player {current_player} won!')
            game_on = False
        
        elif check_tie(board):
            print ('Draw')
            game_on = False
        
        else:
            current_player = 'O' if current_player == 'X' else 'X'



print(play_game())

        


