#!/usr/bin/python3

from dialog import charselect, greetings_chrona, greetings_timmy
import time

#char_list = ['Chrona', 'Timmy', 'Clocman']

charselect()
while True:
    char_input = input("Choose your char:")
    if char_input == "1" or "Chrona":
        time.sleep(1)
        greetings_chrona()
        continue
    elif char_input == "2" or "Timmy":
        time.sleep(1)
        greetings_timmy()
