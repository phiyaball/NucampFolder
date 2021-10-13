#!/usr/bin/python3

wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150
​elf = "Elf"
elf_hp = 100
elf_damage = 100
​
human = "Human"
human_hp = 150
human_damage = 20
​
orc = "Orc"
orc_hp = 100
orc_damage = 100
​
dragon_hp = 300
dragon_damage = 50
​
while True:
    while True:
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Orc")
​
        choice = input("Choose your character: ")
​
        if  choice.title() in ["1", wizard]:
            character = wizard
            my_damage = wizard_damage
            my_hp = wizard_hp
            break
        if choice == "2" or elf.lower() == choice.lower():
            character = elf
            my_damage = elf_damage
            my_hp = elf_hp
            break
        if choice == "3"  or human:
            character = human
            my_damage = human_damage
            my_hp = human_hp
            break
        if choice == "4"  or orc:
            character = orc
            my_damage = orc_damage
            my_hp = orc_hp
            break
        else:
            print("Unknown character")
​
​
    print("THIS IS THE CHARACTER>>>>", character)
    print("Health:", my_hp)
    print("Damage:", my_damage)
    print("")
​
​
    while True:
​
        dragon_hp = dragon_hp - my_damage   # or dragon_hp -= my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)
        print("")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle.")
            break
​
        my_hp = my_hp - dragon_damage       # or my_hp -= dragon_damage
        print("The Dragon strikes back at", character)
        print("The", character + "'s hitpoints are now:", my_hp)
        print("")
        if my_hp <= 0:
            print("The", character, "has lost the battle.")
            break
​
    play_again = input("Do you want to play again? ")
    if play_again == 1 or play_again == "yes":
        pass
    else:
        break
