#!/usr/bin/python3

import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D","7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    print("Press Enter to deal or Q to quit")
    deal = input()
    if deal == "":
        card = random.choice(diamonds)
        hand.append(card)
        print("Your cards are", hand)
        diamonds.remove(card)
        print("Remaining cards:", diamonds)
        if not diamonds:
            print("There are no more cards to pick")
    else:
        break
