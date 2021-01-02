import random
import sys

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
spots = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
computer = 0
user = 0
ties = 0


def game_instructions():
    print("""  
     ____  ____  ___    ____   __    ___    ____  _____  ____ 
    (_  _)(_  _)/ __)  (_  _) /__\  / __)  (_  _)(  _  )( ___)
      )(   _)(_( (__     )(  /(__)\( (__     )(   )(_)(  )__) 
     (__) (____)\___)   (__)(__)(__)\___)   (__) (_____)(____)
    """)
    print(" - Playing Tic-Tac-Toe is easy!")
    print(" - You should get three in a row, column or diagnolly first to win.")
    print(" - Each turn, you must choose an empty spot from 1 to 9.\n")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


def reinitialize_board():
    board.clear()
    spots.clear()
    board.extend(["", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    spots.extend([" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


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


def game_ended(board):
    if " " in board:
        return False
    else:
        return True


def is_valid_entry(spot, player):
    if (spot.isdigit()):
        if 1 <= int(spot) <= 9:
            return True, int(spot)
        else:
            new_spot = input(
                "WARNING: Invalid entry! Enter a number between 1 and 9 that is EMPTY to continue. ")
            chk_validity = is_valid_entry(new_spot, player)
            if chk_validity[0]:
                return True, chk_validity[1]
            else:
                return False, int(new_spot)
    else:
        new_spot = input(
            "WARNING: Invalid entry! Enter a number between 1 and 9 that is EMPTY to continue. ")
        chk_validity = is_valid_entry(new_spot, player)
        if chk_validity[0]:
            return True, chk_validity[1]
        else:
            return False, int(new_spot)


def empty_space(board, spot, player):
    if board[spot] == " ":
        return True, spot
    else:
        new_spot = input("WARNING: Spot already taken! Choose an EMPTY spot to continue. ")
        chk_spot = is_valid_entry(new_spot, player)
        chk_validity = empty_space(board, chk_spot[1], player)
        if chk_validity[0]:
            return True, chk_validity[1]
        else:
            return False, int(new_spot)


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


def ai_play():
    new_array = [i for i in spots if i != " "]
    choice = random.choice(new_array)
    print(" *** Computer played its turn. Now it's yours! *** ")
    return int(choice)


def game():
    global user, computer, ties
    game_instructions()
    print_header()
    while True:
        p1_response = input("Your Turn: Choose an empty space for X and hit ENTER. \n")
        chk_entry_p1 = is_valid_entry(p1_response, "User (X)")
        chk_if_valid_p1 = empty_space(board, chk_entry_p1[1], "User (X)")
        if chk_if_valid_p1[0]:
            board[chk_if_valid_p1[1]] = "X"
            spots[chk_if_valid_p1[1]] = " "

        print_header()

        if did_player_win(board, "X"):
            print("You Won! Congratulations!!!\n")
            user = user + 1
            print("SCORE: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(ties))
            retry = input("\nDo you want to play again? [Y/N] ")
            if retry.lower() == "y":
                reinitialize_board()
                game()
            else:
                print("\nThank you for playing! Hope you enjoyed the game. ~SK")
                sys.exit()

        if game_ended(board):
            print("It's a TIE!")
            ties = ties + 1
            print("SCORE: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(ties))
            retry = input("\nDo you want to play again? [Y/N] ")
            if retry.lower() == "y":
                reinitialize_board()
                game()
            else:
                print("\nThank you for playing! Hope you enjoyed the game. ~SK")
                sys.exit()

        p2_response = ai_play()
        board[p2_response] = "0"
        spots[p2_response] = " "

        print_header()

        if did_player_win(board, "0"):
            print("Computer Won! Congratulations!!!\n")
            computer = computer + 1
            print("SCORE: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(ties))
            retry = input("\nDo you want to play again? [Y/N] ")
            if retry.lower() == "y":
                reinitialize_board()
                game()
            else:
                print("\nThank you for playing! Hope you enjoyed the game. ~SK")
                sys.exit()

        if game_ended(board):
            print("It's a TIE!")
            ties = ties + 1
            print("SCORE: User (X) = " + str(user) + " | Computer (0) = " + str(computer) + " | Ties = " + str(ties))
            retry = input("\nDo you want to play again? [Y/N] ")
            if retry.lower() == "y":
                reinitialize_board()
                game()
            else:
                print("\nThank you for playing! Hope you enjoyed the game. ~SK")
                sys.exit()


game()
