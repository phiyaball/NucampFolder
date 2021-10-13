#!/usr/bin/python3
import random

high_score = 0

print(f'Your high score is {high_score} \n 1) Roll the dice \n 2) Leave the game')

def dice_game():
    global high_score
    choice = int(input("Enter your choice: "))
    while True:
        if choice == 1:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            print(f"You roll a... {dice1}\n You roll a... {dice2}")
            total = dice1 + dice2
            print(f"You rolled a total of: {total}")
            if high_score < total:
                high_score = total
                print("New high score!")
                break
            elif choice == 2:
                print("Goodbye")
                break
            else:
                print("Not an option")
                continue
dice_game()