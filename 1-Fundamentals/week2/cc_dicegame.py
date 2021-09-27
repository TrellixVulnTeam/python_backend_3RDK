import random

high_score = 0

def roll_dice_calc_high_score():
    global high_score
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You roll a... {dice1}")
    print(f"You roll a... {dice2}\n")
    print(f"You have rolled a total of: {str(dice1 + dice2)}")
    if dice1 + dice2 > high_score:
        high_score = dice1 + dice2
        print(f"\nNew high score!: {high_score}")

def dice_game():
    choice = 1
    while choice == 1:
        print(f"Current High Score: {high_score}")
        print("1) Roll Dice")
        print("1) Leave Game")
        choice = int(input("Enter your choice: "))
        if choice == 2:
            print("Goodbye!")
            break
        roll_dice_calc_high_score()

dice_game()