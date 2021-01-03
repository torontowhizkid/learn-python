"""
Tic Tac Toe - Simple Two User Game
Added additional validations for negative scenarios
"""

# initialize global variables
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
spots = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# print board
def print_header():
    print("\n")
    print("SPOTS AVAILABLE \t ACTUAL GAME")
    print(" " + spots[1] + " | " + spots[2] + " | " + spots[3] + " " + "\t\t\t" + " " + board[1] + " | " + board[
        2] + " | " + board[3] + " ")
    print("---|---|---" + "\t\t\t" + "---|---|---")
    print(" " + spots[4] + " | " + spots[5] + " | " + spots[6] + " " + "\t\t\t" + " " + board[4] + " | " + board[
        5] + " | " + board[6] + " ")
    print("---|---|---" + "\t\t\t" + "---|---|---")
    print(" " + spots[7] + " | " + spots[8] + " | " + spots[9] + " " + "\t\t\t" + " " + board[7] + " | " + board[
        8] + " | " + board[9] + " ")
    print("\n")


# check if board is full
def game_ended(board):
    if " " in board:
        return False
    else:
        return True


# check if user entry is valid
def is_valid_entry(spot, player):
    if (spot.isdigit()):
        if 1 <= int(spot) <= 9:
            return True, int(spot)
        else:
            new_spot = input(
                "WARNING: Invalid entry! Enter a number between 1 and 9 that is EMPTY for " + player + " to continue. ")
            chk_validity = is_valid_entry(new_spot, player)
            if chk_validity[0]:
                return True, chk_validity[1]
            else:
                return False, int(new_spot)
    else:
        new_spot = input(
            "WARNING: Invalid entry! Enter a number between 1 and 9 that is EMPTY for " + player + " to continue. ")
        chk_validity = is_valid_entry(new_spot, player)
        if chk_validity[0]:
            return True, chk_validity[1]
        else:
            return False, int(new_spot)


# check if user selected spot is empty
def empty_space(board, spot, player):
    if board[spot] == " ":
        return True, spot
    else:
        new_spot = input("WARNING: Spot already taken! Choose an EMPTY spot for " + player + " to continue. ")
        chk_spot = is_valid_entry(new_spot, player)
        chk_validity = empty_space(board, chk_spot[1], player)
        if chk_validity[0]:
            return True, chk_validity[1]
        else:
            return False, int(new_spot)


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
    chk_entry_p1 = is_valid_entry(p1_response, "PLAYER 1 (X)")
    chk_if_valid_p1 = empty_space(board, chk_entry_p1[1], "PLAYER 1 (X)")
    if chk_if_valid_p1[0]:
        board[chk_if_valid_p1[1]] = "X"
        spots[chk_if_valid_p1[1]] = " "

    print_header()

    if did_player_win(board, "X"):
        print("PLAYER 1 (X) Won! Congratulations!!!")
        break

    if game_ended(board):
        print("It's a TIE!")
        break

    p2_response = input("PLAYER 2 (0): Choose an empty space for 0. ")
    chk_entry_p2 = is_valid_entry(p2_response, "PLAYER 2 (0)")
    chk_if_valid_p2 = empty_space(board, chk_entry_p2[1], "PLAYER 2 (0)")
    if chk_if_valid_p2[0]:
        board[chk_if_valid_p2[1]] = "0"
        spots[chk_if_valid_p2[1]] = " "

    print_header()

    if did_player_win(board, "0"):
        print("PLAYER 2 (0) Won! Congratulations!!!")
        break

    if game_ended(board):
        print("It's a TIE!")
        break
