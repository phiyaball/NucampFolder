#!/usr/bin/python3

<<<<<<< HEAD
from emoji import emojize
from dialog import greetings
from animation import animate_t
import time
import threading
import itertools
import names

greetings()

while True:
    player_input = input("\n Enter your name:")
    print("I don't like it...")
    print("I'm going to call you")
    time.sleep(3)
    player_name = (names.get_full_name())
    print(player_name)
    time.sleep(1)
    global new_name
    print("So what was your name again?")
    new_name = input("\n Enter your new name:(Exactly shown or else!!)")
    if new_name != player_name:
        print("I don't know you, you're dead to me!")
        animate_t(5)
        print("         \n\n GAME OVER!!!!!          ")
        break
    else:
        print("That's what I thought, Hello, " + new_name)
        print("")
        time.sleep(3)
        print ("\n 1. Who are you? \n 2. What am I doing here, \n 3. What is this place?")
        ask_question = input("\n (Choose 1-3):")
        if ask_question == "1":
            print("Who am I you ask? Good question...")
            time.sleep(1)
            print("I am the creator of all things...")
            time.sleep(1)
            print("I know what you're thinking....")
            time.sleep(1)
            print("And no I'm not THAT omnipotent being...")
            time.sleep(1)
            print("\n Around these parts they call me " + (names.get_full_name()))
        continue
        if ask_question == "2":
            print("You tell me, I was just minding my own business and you pop out of nowhere")
            time.sleep(2)
        continue
        if ask_question == "3":
            print("you are in the void, stuck between space and time, where everything and nothing collide to become absolutely jack shit")
            print("pardon my french, I've been alone here so long I forget how to behave around people " + print(emojize(":cloud:")))
        else:
            continue