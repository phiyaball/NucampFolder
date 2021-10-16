#!/usr/bin/python3

import time
from animation import animate_t
from emoji import emojize
import names
from threading import ThreadError
#greeting message
def greetings():
    print(emojize(":zzz:, :zzz:, :zzz:"))
    animate_t(2)
    print("\n You've woken up to what seems like an empty room, void of anything physical, with nothing but a humming noise")
    time.sleep(1)
    print("Suddenly a voice calls out to you")
    time.sleep(1)
    print("")
    print("Who goes there?!")

# questions for god
def who_are_you():
    print("Who am I you ask? Good question...")
    time.sleep(2)
    print("I am the creator of all things...")
    time.sleep(2)
    print("I know what you're thinking....")
    time.sleep(2)
    print("And no I'm not THAT omnipotent being...")
    time.sleep(2)
    print("That guy lives across the street")
    time.sleep(2)
    print("\n Around these parts they call me " + (names.get_full_name()))

def doing_here():
    print("You tell me, I was just minding my own business and you came out of nowhere")
    time.sleep(2)

def this_place():
    print("You are in the void, a crossroads where all of time and space come together")
    time.sleep(2)
    print("whatever you do though...")
    time.sleep(2)
    print("DON'T open any doors or you could get sucked into a random time period!")

# 
def door_appears():
    print("\n The entire place rumbles")
    time.sleep(5)
    print("\n Wooosh")
    print("\n Several doors appear seamingly out of no where, too many for the naked eye to count")
    time.sleep(5)

def arrive_frontier():
    print("\n Yeehaw! You've arrived in the frontier era")
    time.sleep(2)
    print("in what appears to be a saloon")
    time.sleep(2)
    print("")
    print("There's a barternder to your right, a pianist to your left and an outlaw sitting directly across from you")

def bartender():
    print("Why hello there partner")
    time.sleep(2)
    print("Haven't seen you in these here parts before")
    time.sleep(2)
    print("Here's a drink")

def pianist():
    print("LaLa" * 10)
    print(emojize(":musical_keyboard:" * 10))
    print(emojize(":musical_note:" * 10))


def outlaw():
    print("You're probably wondering how I know your name")
    time.sleep(2)
    print("Wondering out of all the variables in the universe how is it possible we're sitting here at this exact monent")
    time.sleep(2)
    print("Something something time travel heh")
    time.sleep(2)
    print("Let's just say I was once you")
    time.sleep(2)

def outlaw2():
    print("Sayyyy, you're from the future right?")
    time.sleep(2)
    print("I reckon you can help me answer a question questions that's been eating at me")