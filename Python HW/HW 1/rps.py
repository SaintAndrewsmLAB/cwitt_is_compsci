# Name: Carson Witt
# Period: C
# Date: 9/25/2017
# rps.py

##### Rock Paper Scissors Game ######

solid = True

while solid == True:
    solid = False
    p_1 = raw_input("Player 1: Rock, Paper, or Scissors?")
    if p_1 == "Rock":
        valid = False
    elif p_1 == "rock":
        valid = False
    elif p_1 == "Paper":
        valid = False
    elif p_1 == "paper":
        valid = False
    elif p_1 == "Scissors":
        valid = False
    elif p_1 == "scissors":
        valid = False
    else:
        print "Not a valid object statement. Please try again."
        solid = True

while valid == False:
    valid = True
    p_2 = raw_input("Player 2: Rock, Paper, or Scissors?")
    if p_1 == "Rock":
        if p_2 == "Rock":
            print "It's a tie!"
        elif p_2 == "rock":
            print "It's a tie!"
        elif p_2 == "Paper":
            print "Player 2 Wins!"
        elif p_2 == "paper":
            print "Player 2 Wins!"
        elif p_2 == "Scissors":
            print "Player 1 Wins!"
        elif p_2 == "scissors":
            print "Player 1 Wins!"
        else:
            print "Not a valid object statement. Please try again."
            valid = False
    elif p_1 == "rock":
        if p_2 == "Rock":
            print "It's a tie!"
        elif p_2 == "rock":
            print "It's a tie!"
        elif p_2 == "Paper":
            print "Player 2 Wins!"
        elif p_2 == "paper":
            print "Player 2 Wins!"
        elif p_2 == "Scissors":
            print "Player 1 Wins!"
        elif p_2 == "scissors":
            print "Player 1 Wins!"
        else:
            print "Not a valid object statement. Please try again."
            valid = False
    elif p_1 == "Paper":
        if p_2 == "Rock":
            print "Player 1 Wins!"
        elif p_2 == "rock":
            print "Player 1 Wins!"
        elif p_2 == "Paper":
            print "It's a tie!"
        elif p_2 == "paper":
            print "It's a tie!"
        elif p_2 == "Scissors":
            print "Player 2 Wins!"
        elif p_2 == "scissors":
            print "Player 2 Wins!"
        else:
            print "Not a valid object statement. Please try again."
            valid = False
    elif p_1 == "paper":
        if p_2 == "Rock":
            print "Player 1 Wins!"
        elif p_2 == "rock":
            print "Player 1 Wins!"
        elif p_2 == "Paper":
            print "It's a tie!"
        elif p_2 == "paper":
            print "It's a tie!"
        elif p_2 == "Scissors":
            print "Player 2 Wins!"
        elif p_2 == "scissors":
            print "Player 2 Wins!"
        else:
            print "Not a valid object statement. Please try again."
            valid = False
    elif p_1 == "Scissors":
        if p_2 == "Rock":
            print "Player 2 Wins!"
        elif p_2 == "rock":
            print "Player 2 Wins!"
        elif p_2 == "Paper":
            print "Player 1 Wins!"
        elif p_2 == "paper":
            print "Player 1 Wins!"
        elif p_2 == "Scissors":
            print "It's a tie!"
        elif p_2 == "scissors":
            print "It's a tie!"
        else:
            print "Not a valid object statement. Please try again."
            valid = False
    elif p_1 == "scissors":
        if p_2 == "Rock":
            print "Player 2 Wins!"
        elif p_2 == "rock":
            print "Player 2 Wins!"
        elif p_2 == "Paper":
            print "Player 1 Wins!"
        elif p_2 == "paper":
            print "Player 1 Wins!"
        elif p_2 == "Scissors":
            print "It's a tie!"
        elif p_2 == "scissors":
            print "It's a tie!"
        else:
            print "Not a valid object statement. Please try again."
            valid = False
    else:
        print "Not a valid object statement. Please try again."
        valid = False
