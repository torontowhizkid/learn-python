import random
import sys

# Initialize global variables
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
spots = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
computer = 0
user = 0
ties = 0
last_start = '0'


# print game instructions - once at the start of the game
def game_instructions():
    print("""  
     ____  ____  ___    ____   __    ___    ____  _____  ____ 
    (_  _)(_  _)/ __)  (_  _) /__\  / __)  (_  _)(  _  )( ___)
      )(   _)(_( (__     )(  /(__)\( (__     )(   )(_)(  )__) 
     (__) (____)\___)   (__)(__)(__)\___)   (__) (_____)(____)
    """)
    print(" - Playing Tic-Tac-Toe is easy!")
    print(" - You should get three in a row, column or diagonally first to win.")
    print(" - Each turn, you must choose an empty spot from 1 to 9.\n")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


# initialize the board when user opts to replay
def reinitialize_board():
    board.clear()
    spots.clear()
    board.extend(["", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    spots.extend([" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


# print board
def print_header():
    print("\n")
    print(" " + board[1] + " | " + board[
        2] + " | " + board[3] + " ")
    print("---|---|---")
    print(" " + board[4] + " | " + board[
        5] + " | " + board[6] + " ")
    print("---|---|---")
    print(" " + board[7] + " | " + board[
        8] + " | " + board[9] + " ")
    print("\n")


# check if game has ended
def game_ended(board):
    if " " in board:
        return False
    else:
        return True


# validate if user entered a valid entry i.e. 1 to 9 only
def is_valid_entry(spot, player):
    if (spot.isdigit()):
        if 1 <= int(spot) <= 9:
            return True, int(spot)
        else:
            new_spot = input(
                "WARNING: Invalid entry! Enter a number between 1 and 9 that is EMPTY to continue. \n>> ")
            chk_validity = is_valid_entry(new_spot, player)
            if chk_validity[0]:
                return True, chk_validity[1]
            else:
                return False, int(new_spot)
    else:
        new_spot = input(
            "WARNING: Invalid entry! Enter a number between 1 and 9 that is EMPTY to continue. \n>> ")
        chk_validity = is_valid_entry(new_spot, player)
        if chk_validity[0]:
            return True, chk_validity[1]
        else:
            return False, int(new_spot)


# validate if user selected an empty spot (not already taken)
def empty_space(board, spot, player):
    if board[spot] == " ":
        return True, spot
    else:
        new_spot = input("WARNING: Spot already taken! Choose an EMPTY spot to continue. \n>> ")
        chk_spot = is_valid_entry(new_spot, player)
        chk_validity = empty_space(board, chk_spot[1], player)
        if chk_validity[0]:
            return True, chk_validity[1]
        else:
            return False, int(new_spot)


# check if game is over, did player win with the new entry
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


# bot automated play
def ai_play():
    new_array = [i for i in spots if i != " "]
    # choice = random.choice(new_array)

    predict_0_move = predict_next_move_win(new_array, "0")
    if predict_0_move[0]:
        choice = predict_0_move[1]
    else:
        predict_X_move = predict_next_move_win(new_array, "X")
        if predict_X_move[0]:
            choice = predict_X_move[1]
        else:
            choice = random.choice(new_array)

    print(" *** Computer played its turn. Now it's yours! *** ")
    return int(choice)


# predict next move of user and bot to win or block
def predict_next_move_win(spots, player):
    for x in spots:
        new_board = board[:]
        new_board[int(x)] = player
        if did_player_win(new_board, player):
            return True, x
    return False, 0

#hint for users
def hint_options():
    hint_array = [i for i in spots if i != " "]
    if len(hint_array) >= 9:
        return "All options from 1 to 9 are available."
    else:
     return "Options available are " + str(hint_array).replace("'", "")

# user actions and validations
def user_gameplay():
    global user, computer, ties, last_start
    p1_response = input("Your Turn: Choose an empty space for X and hit ENTER. \n[HINT]: " + hint_options() + "\n>> ")
    chk_entry_p1 = is_valid_entry(p1_response, "User (X)")
    chk_if_valid_p1 = empty_space(board, chk_entry_p1[1], "User (X)")
    if chk_if_valid_p1[0]:
        board[chk_if_valid_p1[1]] = "X"
        spots[chk_if_valid_p1[1]] = " "

    print_header()

    if did_player_win(board, "X"):
        print("You Won! Congratulations!!!\n")
        user = user + 1
        print(":::: SCORE :::: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(
            ties))
        retry = input("\nDo you want to play again? [Y/N] ")
        if retry.lower() == "y":
            reinitialize_board()
            game()
        else:
            print("\nThank you for playing! Hope you enjoyed the game. ~TWK\n")
            sys.exit()

    if game_ended(board):
        print("It's a TIE!\n")
        ties = ties + 1
        print(":::: SCORE :::: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(
            ties))
        retry = input("\nDo you want to play again? [Y/N] ")
        if retry.lower() == "y":
            reinitialize_board()
            game()
        else:
            print("\nThank you for playing! Hope you enjoyed the game. ~TWK\n")
            sys.exit()


# bot actions and validations
def ai_gameplay():
    global user, computer, ties, last_start
    p2_response = ai_play()
    board[p2_response] = "0"
    spots[p2_response] = " "
    print_header()

    if did_player_win(board, "0"):
        print("Computer Won! Better luck next time!!!\n")
        computer = computer + 1
        print(":::: SCORE :::: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(
            ties))
        retry = input("\nDo you want to play again? [Y/N] ")
        if retry.lower() == "y":
            reinitialize_board()
            game()
        else:
            print("\nThank you for playing! Hope you enjoyed the game. ~TWK\n")
            sys.exit()

    if game_ended(board):
        print("It's a TIE!\n")
        ties = ties + 1
        print(":::: SCORE :::: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(
            ties))
        retry = input("\nDo you want to play again? [Y/N] ")
        if retry.lower() == "y":
            reinitialize_board()
            game()
        else:
            print("\nThank you for playing! Hope you enjoyed the game. ~TWK\n")
            sys.exit()


# main function
def game():
    global user, computer, ties, last_start
    game_instructions()
    print_header()

    if last_start == '0':
        print("=== User will start the Game! ===\n")
        while True:
            user_gameplay()
            ai_gameplay()
            last_start = 'X'
    else:
        print("=== Computer will start the game this time! ===\n")
        while True:
            ai_gameplay()
            user_gameplay()
            last_start = '0'


# call game function
game()
