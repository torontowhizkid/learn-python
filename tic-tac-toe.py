"""
Tic Tac Toe - Simple two user game
"""

# initialize global variables
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]


# print board
def print_header():
    print("\n")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("\n")


# check if board is full
def game_ended(board):
    if " " in board:
        return False
    else:
        return True


# check if a player won
def did_player_win(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False


print_header()

# handle user actions
while True:
    p1_response = input("PLAYER 1 (X): Choose an empty space for X. ")
    board[int(p1_response)] = "X"
    print_header()
    if did_player_win(board, "X"):
        print("PLAYER 1 (X) Won! Congratulations!!!")
        break
    if game_ended(board):
        print("It's a TIE!")
        break

    p2_response = input("PLAYER 2 (0): Choose an empty space for 0. ")
    board[int(p2_response)] = "0"
    print_header()
    if did_player_win(board, "0"):
        print("PLAYER 2 (0) Won! Congratulations!!!")
        break
    if game_ended(board):
        print("It's a TIE!")
        break
