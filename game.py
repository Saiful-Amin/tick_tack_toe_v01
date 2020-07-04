

#board

board = ["__","__","__","__","__","__","__","__","__",]
the_game_is_on = True
winner = None
current_player = "X"
def display_board():
    print(board[0]  + "|" + board[1] +"|" + board[2])
    print(board[3]  + "|" + board[4] +"|" + board[5])
    print(board[6]  + "|" + board[7] +"|" + board[8])

def lets_play_the_game():
    global winner
    display_board()
    while the_game_is_on:
        game_turn(current_player)
        check_game_over()
        check_tie()
        player_change()

    if winner == "X" or winner == "O":
        print(winner + "won")
    elif winner == None:
        print("it's a tie")




def game_turn(current_player):
    position = input("choose a position from 1 to 9: ")
    position = int(position) -1
    board[position] = current_player
    display_board()

def check_game_over():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_tie():
    global the_game_is_on
    if "__" not in board:
        the_game_is_on = False
    return

def check_rows():
    global the_game_is_on
    row_1 = board[0] == board[1] == board[2] != "__"
    row_2 = board[3] == board[4] == board[5] != "__"
    row_3 = board[6] == board[7] == board[8] != "__"

    if row_1 or row_2 or row_3:
        the_game_is_on = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

    return

def check_columns():
    global the_game_is_on
    column_1 = board[0] == board[3] == board[6] != "__"
    column_2 = board[1] == board[4] == board[7] != "__"
    column_3 = board[2] == board[5] == board[8] != "__"

    if column_1 or column_2 or column_3:
        the_game_is_on = False

    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    global the_game_is_on
    diagonal_1 = board[0] == board[4] == board[8] != "__"
    diagonal_2 = board[2] == board[4] == board[6] != "__"


    if diagonal_1 or diagonal_2:
        the_game_is_on = False

    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

def player_change():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return



lets_play_the_game()









#display the board
#Player 1 input
#player 2 input
#check Win
    #check rows
    #check Columns
    #check Diagonals
#check tie


