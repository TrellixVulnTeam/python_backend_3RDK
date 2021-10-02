import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

def get_diamond_card():
    return random.choice(diamonds)

while diamonds:
    card = input("Please enter to pick a card, or Q then enter to quit:")
    if card.upper() == "Q":
        break

    new_card = get_diamond_card()
    hand.append(new_card)
    diamonds.remove(new_card)

    print("Your hand: {}".format(new_card))
    print("Remaining Cards: {}".format(diamonds))

if not diamonds:
    print("There are no more cards to pick.")