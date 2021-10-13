#!/usr/bin/python3

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_dmg = 150
elf_dmg = 100
human_dmg = 150

dragon_hp = 300
dragon_dmg = 5

char = input("choose your character:")
if char == 'wizard' or char == 'Wizard' or char == 'human' or char == 'Human' or char == 'elf' or char == 'Elf':
    print("Hello " + char)