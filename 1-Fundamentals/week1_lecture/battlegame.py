play_game = True
wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

while play_game:

    dragon_hp = 300

    while True:
        print("Welcome to the Battle Arena!")
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Press 4 to add New Option")
        character = input("Input your character name: ").capitalize()
        if character == "Wizard" or character == "1":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == "Elf" or character == "2":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == "Human" or character == "3":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character == "4":
            character = input("What's the new character name: ").capitalize()
            my_hp = int(input("Input your character HP: "))
            my_damage = int(input("Input your character damage: "))
            break
        else:
            character = "Unknown character"
            print("You chose an unknown character!")
    print(f"You chose {character}!")
    print(f"Your HP is: {my_hp}")
    print(f"Your damage is: {my_damage}\n")

    while True:
        dragon_hp -= my_damage
        print(f"The {character} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon_hp} \n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp -= dragon_damage
        print(f"The Dragon strikes back at {character}!")
        print(f"The {character} hitpoints are now: {my_hp}\n")
        if my_hp <= 0:
            print(f"The {character} has lost the battle")
            break
        exit_game = input("Do you want to exit the game? (True/False) ").lower().strip()
        if exit_game == "true":
            break

    play_again = input("Do you want to play again? (y/n)")
    if play_again == "n":
        break