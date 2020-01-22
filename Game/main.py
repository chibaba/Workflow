# ======== Global Variable =======

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True

# who won? or tie?

winner = None

# who's turn is it
current_player = "X"
    # display board
def display_board():
    print(board[0] + " | " + board[1] + " + board[2]")
    print(board[3] + " | " + board[4] + " + board[5]")
    print(board[6] + " | " + board[7] + " + board[8]")
    
def play_game():

    # display initial board
    display_board()
    # while the game is still on session
    while game_still_going:
        
    # handle A single turn of an arbitrary player    
        handle_turn(current_player)
        
    # check if the game has ended    
        check_if_game_over()
    
    #Flip to the other player
    flip_player()
        
    # the game has ended
    if  winner == "XX" or winner== "0":
        print(winner + "won.")
    elif winner == None:
        print("Tie.")
    # handle a single turn of an arbitarary player
def handle_turn(player):
    position = input("choose a position from 1-9: ")
    position = int(position) -1
    
    board[position] = "X"
    display_board()
    
def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    # check rows
    # check column
    # check_diagonals
    return
def check_if_tie():
    return

def flip_player():
    return
    
    play_game()