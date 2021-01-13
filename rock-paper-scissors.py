import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    robot = random.choice(choices)
    player = input("Rock, Paper, Scissors? ")

    # Robot & I choose same shape
    if player == robot:
        print("Tie!")

    # If I chose Rock and...
    elif player == "Rock":
        # Robot chose Paper, Robot wins
        if robot == "Paper":
            print("You lose!", robot, "covers", player)
        # Robot chose Scissors, I win
        else:
            print("You win!", player, "smashes", robot)

    # If I chose Paper and...
    elif player == "Paper":
        # Robot chose Scissors, Robot wins
        if robot == "Scissors":
            print("You lose!", robot, "cut", player)
        # Robot chose Rock, I win
        else:
            print("You win!", player, "covers", robot)

    # If I chose Scissors and...
    elif player == "Scissors":
        # Robot chose Rock, Robot wins
        if robot == "Rock":
            print("You lose...", robot, "smashes", player)
        # Robot chose Paper, I win
        else:
            print("You win!", player, "cut", robot)

    else:
        print("That's not a valid play. Check your spelling!")