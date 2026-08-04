import random

Choice  = {1 : "Stone" ,
           2 : "Paper" ,
           3 : "Scissor"
           }

def game(player):

    computer = random.randint(1, 3)
    
    if player == computer:
        winner = "It's a tie!"

    elif (player == 1 and computer == 3) \
        or (player == 2 and computer == 1) \
        or (player == 3 and computer == 2):

        winner = "You win!"
    else:
        winner = "Computer wins!"

    return computer , winner

