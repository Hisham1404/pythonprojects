import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    while True:
        roll = input("Roll the dice? (yes/no) ")
        if roll.lower() == 'yes':
            value = roll_dice()
            print("You rolled a", value)
        else:
            print("Thanks for playing!")
            break

play_game()
